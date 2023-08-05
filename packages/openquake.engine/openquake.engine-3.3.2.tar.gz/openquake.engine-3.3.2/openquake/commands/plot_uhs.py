# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2018 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
import numpy
from openquake.baselib import sap
from openquake.calculators import getters
from openquake.commonlib import calc
from openquake.commands import engine


def make_figure(indices, n_sites, oq, pmaps):
    """
    :param indices: the indices of the sites under analysis
    :param n_sites: total number of sites
    :param oq: instance of OqParam
    :param pmaps: a list of probability maps per realization
    """
    # NB: matplotlib is imported inside since it is a costly import
    import matplotlib.pyplot as plt

    fig = plt.figure()
    n_poes = len(oq.poes)
    uhs_by_rlz = []
    for pmap in pmaps:
        hmap = calc.make_hmap_array(pmap, oq.imtls, oq.poes, n_sites)
        uhs_by_rlz.append(calc.make_uhs(hmap, oq))
    periods = [imt.period for imt in oq.imt_periods()]
    for i, site in enumerate(indices):
        for j, poe in enumerate(oq.poes):
            ax = fig.add_subplot(len(indices), n_poes, i * n_poes + j + 1)
            ax.grid(True)
            ax.set_xlim([periods[0], periods[-1]])
            ax.set_xlabel(
                'UHS on site %d, poe=%s, period in seconds' % (site, poe))
            if j == 0:  # set Y label only on the leftmost graph
                ax.set_ylabel('SA')
            fields = [f for f in uhs_by_rlz[0].dtype.names
                      if f.startswith(str(poe))]
            for r, all_uhs in enumerate(uhs_by_rlz):
                ax.plot(periods, list(all_uhs[site][fields]), label=r)
    plt.legend()
    return plt


@sap.Script
def plot_uhs(calc_id, sites='0'):
    """
    UHS plotter.
    """
    # read the hazard data
    dstore = engine.read(calc_id)
    rlzs_assoc = dstore['csm_info'].get_rlzs_assoc()
    getter = getters.PmapGetter(dstore, rlzs_assoc)
    getter.init()
    oq = dstore['oqparam']
    indices = list(map(int, sites.split(',')))
    n_sites = len(dstore['sitecol'])
    if not set(indices) <= set(range(n_sites)):
        invalid = sorted(set(indices) - set(range(n_sites)))
        print('The indices %s are invalid: no graph for them' % invalid)
    valid = sorted(set(range(n_sites)) & set(indices))
    print('Found %d site(s); plotting %d of them' % (n_sites, len(valid)))
    pmaps = getter.get_pmaps(numpy.array(indices))
    plt = make_figure(valid, n_sites, oq, pmaps)
    plt.show()


plot_uhs.arg('calc_id', 'a computation id', type=int)
plot_uhs.opt('sites', 'comma-separated string with the site indices')
