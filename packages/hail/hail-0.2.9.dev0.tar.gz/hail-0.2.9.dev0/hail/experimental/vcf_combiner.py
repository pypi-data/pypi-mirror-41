"""A work in progress pipeline to combine (g)VCFs into an alternate format"""

import hail as hl
from hail.matrixtable import MatrixTable
from hail.expr import ArrayExpression, StructExpression
from hail.ir.matrix_ir import MatrixKeyRowsBy


def transform_one(mt: MatrixTable) -> MatrixTable:
    """transforms a gvcf into a form suitable for combining"""
    mt = mt.annotate_entries(
        # local (alt) allele index into global (alt) alleles
        LA=hl.range(0, hl.len(mt.alleles) - 1),
        END=mt.info.END,
        PL=mt['PL'][0:],
        BaseQRankSum=mt.info['BaseQRankSum'],
        ClippingRankSum=mt.info['ClippingRankSum'],
        MQ=mt.info['MQ'],
        MQRankSum=mt.info['MQRankSum'],
        ReadPosRankSum=mt.info['ReadPosRankSum'],
    )
    mt = mt.annotate_rows(
        info=mt.info.annotate(
            SB=hl.agg.array_sum(mt.entry.SB)
        ).select(
            "DP",
            "MQ_DP",
            "QUALapprox",
            "RAW_MQ",
            "VarDP",
            "SB",
        ))
    mt = mt.drop('SB', 'qual')

    return mt


def merge_alleles(alleles) -> ArrayExpression:
    return hl.array(hl.set(hl.flatten(alleles)))


def renumber_entry(entry, old_to_new) -> StructExpression:
    # global index of alternate (non-ref) alleles
    return entry.annotate(LA=entry.LA.map(lambda lak: old_to_new[lak]))


def combine(ts):
    # pylint: disable=protected-access
    tmp = ts.annotate(
        alleles=merge_alleles(ts.data.map(lambda d: d.alleles)),
        rsid=hl.find(hl.is_defined, ts.data.map(lambda d: d.rsid)),
        filters=hl.set(hl.flatten(ts.data.map(lambda d: hl.array(d.filters)))),
        info=hl.struct(
            DP=hl.sum(ts.data.map(lambda d: d.info.DP)),
            MQ_DP=hl.sum(ts.data.map(lambda d: d.info.MQ_DP)),
            QUALapprox=hl.sum(ts.data.map(lambda d: d.info.QUALapprox)),
            RAW_MQ=hl.sum(ts.data.map(lambda d: d.info.RAW_MQ)),
            VarDP=hl.sum(ts.data.map(lambda d: d.info.VarDP)),
            SB=hl.array([
                hl.sum(ts.data.map(lambda d: d.info.SB[0])),
                hl.sum(ts.data.map(lambda d: d.info.SB[1])),
                hl.sum(ts.data.map(lambda d: d.info.SB[2])),
                hl.sum(ts.data.map(lambda d: d.info.SB[3]))
            ])))
    tmp = tmp.annotate(
        __entries=hl.bind(
            lambda combined_allele_index:
            hl.range(0, hl.len(tmp.data)).flatmap(
                lambda i:
                hl.cond(hl.is_missing(tmp.data[i].__entries),
                        hl.range(0, hl.len(tmp.g[i].__cols))
                          .map(lambda _: hl.null(tmp.data[i].__entries.dtype.element_type)),
                        hl.bind(
                            lambda old_to_new: tmp.data[i].__entries.map(lambda e: renumber_entry(e, old_to_new)),
                            hl.range(0, hl.len(tmp.data[i].alleles)).map(
                                lambda j: combined_allele_index[tmp.data[i].alleles[j]])))),
            hl.dict(hl.range(0, hl.len(tmp.alleles)).map(
                lambda j: hl.tuple([tmp.alleles[j], j])))))
    tmp = tmp.annotate_globals(__cols=hl.flatten(tmp.g.map(lambda g: g.__cols)))

    return tmp.drop('data', 'g')


def combine_gvcfs(mts):
    """merges vcfs using multi way join"""

    # pylint: disable=protected-access
    def localize(mt):
        return mt._localize_entries('__entries', '__cols')

    def fix_alleles(alleles):
        ref = alleles.map(lambda d: d.ref).fold(lambda s, t: hl.cond(hl.len(s) > hl.len(t), s, t), '')
        alts = alleles.map(
            lambda a: hl.switch(hl.allele_type(a.ref, a.alt))
                        .when('SNP', a.alt + ref[hl.len(a.alt):])
                        .when('Insertion', a.alt + ref[hl.len(a.ref):])
                        .when('Deletion', a.alt + ref[hl.len(a.ref):])
                        .default(a.alt)
        )
        return hl.array([ref]).extend(alts)

    def min_rep(locus, ref, alt):
        mr = hl.min_rep(locus, [ref, alt])
        return (hl.case()
                  .when(alt == '<NON_REF>', hl.struct(ref=ref[0:1], alt=alt))
                  .when(locus == mr.locus, hl.struct(ref=mr.alleles[0], alt=mr.alleles[1]))
                  .or_error("locus before and after minrep differ"))

    mts = [hl.MatrixTable(MatrixKeyRowsBy(mt._mir, ['locus'], is_sorted=True)) for mt in mts]
    mts = [mt.annotate_rows(
        # now minrep'ed (ref, alt) allele pairs
        alleles=hl.bind(lambda ref, locus: mt.alleles[1:].map(lambda alt: min_rep(locus, ref, alt)),
                        mt.alleles[0], mt.locus)) for mt in mts]
    ts = hl.Table._multi_way_zip_join([localize(mt) for mt in mts], 'data', 'g')
    combined = combine(ts)
    combined = combined.annotate(alleles=fix_alleles(combined.alleles))
    return hl.MatrixTable(
        MatrixKeyRowsBy(
            combined._unlocalize_entries('__entries', '__cols', ['s'])._mir,
            ['locus', 'alleles'],
            is_sorted=True))

# NOTE: these are just @chrisvittal's notes on how gVCF fields are combined
#       some of it is copied from GenomicsDB's wiki.
# always missing items include MQ, HaplotypeScore, InbreedingCoeff
# items that are dropped by CombineGVCFs and so set to missing are MLEAC, MLEAF
# Notes on info aggregation, The GenomicsDB wiki says the following:
#   The following operations are supported:
#       "sum" sum over valid inputs
#       "mean"
#       "median"
#       "element_wise_sum"
#       "concatenate"
#       "move_to_FORMAT"
#       "combine_histogram"
#
#   Operations for the fields
#   QUAL: set to missing
#   INFO {
#       BaseQRankSum: median, # NOTE : move to format for combine
#       ClippingRankSum: median, # NOTE : move to format for combine
#       DP: sum
#       ExcessHet: median, # NOTE : this can also be dropped
#       MQ: median, # NOTE : move to format for combine
#       MQ_DP: sum,
#       MQ0: median,
#       MQRankSum: median, # NOTE : move to format for combine
#       QUALApprox: sum,
#       RAW_MQ: sum
#       ReadPosRankSum: median, # NOTE : move to format for combine
#       SB: elementwise sum, # NOTE: after being moved from FORMAT
#       VarDP: sum
#   }
#   FORMAT {
#       END: move from INFO
#   }
#
# The following are Truncated INFO fields for the specific VCFs this tool targets
# ##INFO=<ID=BaseQRankSum,Number=1,Type=Float>
# ##INFO=<ID=ClippingRankSum,Number=1,Type=Float>
# ##INFO=<ID=DP,Number=1,Type=Integer>
# ##INFO=<ID=END,Number=1,Type=Integer>
# ##INFO=<ID=ExcessHet,Number=1,Type=Float>
# ##INFO=<ID=MQ,Number=1,Type=Float>
# ##INFO=<ID=MQRankSum,Number=1,Type=Float>
# ##INFO=<ID=MQ_DP,Number=1,Type=Integer>
# ##INFO=<ID=QUALapprox,Number=1,Type=Integer>
# ##INFO=<ID=RAW_MQ,Number=1,Type=Float>
# ##INFO=<ID=ReadPosRankSum,Number=1,Type=Float>
# ##INFO=<ID=VarDP,Number=1,Type=Integer>
