# -*- coding: utf-8 -*-
"""start IPython shell with hgvs initialized. Intended to be used for
experimenting, debugging, and generating bug reports."""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging

import IPython

hgvs_g = "NC_000007.13:g.36561662C>T"
hgvs_c = "NM_001637.3:c.1582G>A"
hgvs_p = "NP_001628.1:p.(Gly528Arg)"

header_string = """############################################################################
hgvs-shell -- interactive hgvs
hgvs version: {v}
data provider url: {hdp.url}
schema_version: {sv}
data_version: {dv}
sequences source: {hdp.seqfetcher.source}

The following variables are defined:
* hp -- hgvs parser
* hdp -- hgvs data provider
* vm -- VariantMapper
* am37 -- AssemblyMapper, GRCh37
* am38 -- AssemblyMapper, GRCh38
* hv -- hgvs Validator
* hn -- hgvs Normalizer

hgvs_g, hgvs_c, hgvs_p -- sample variants as hgvs strings
var_g, var_c, var_p -- sample variants, as parsed SequenceVariants

When submitting bug reports, include the version header shown above
and use these variables/variable names whenever possible.

"""


def shell():
    logging.basicConfig(level=logging.INFO)

    import hgvs
    logging.info("Starting hgvs-shell " + hgvs.__version__)

    import hgvs.assemblymapper
    import hgvs.dataproviders.uta
    import hgvs.normalizer
    import hgvs.parser
    import hgvs.variantmapper
    import hgvs.validator
    from hgvs.utils.context import variant_context_w_alignment

    hp = hgvsparser = hgvs.parser.Parser()

    hdp = hgvs.dataproviders.uta.connect()
    vm = variantmapper = hgvs.variantmapper.VariantMapper(hdp)
    am37 = easyvariantmapper = hgvs.assemblymapper.AssemblyMapper(hdp, assembly_name='GRCh37')
    am38 = easyvariantmapper = hgvs.assemblymapper.AssemblyMapper(hdp, assembly_name='GRCh38')
    hv = hgvs.validator.Validator(hdp)
    hn = hgvs.normalizer.Normalizer(hdp)

    var_g = hgvsparser.parse_hgvs_variant(hgvs_g)
    var_c = hgvsparser.parse_hgvs_variant(hgvs_c)
    var_p = hgvsparser.parse_hgvs_variant(hgvs_p)

    IPython.embed(
        header=header_string.format(
            v=hgvs.__version__,
            hdp=hdp,
            sv=hdp.schema_version(),
            dv=hdp.data_version(),
        ))

# <LICENSE>
# Copyright 2018 HGVS Contributors (https://github.com/biocommons/hgvs)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# </LICENSE>
