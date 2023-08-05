"""
Vapor-compressor chiller
"""
from __future__ import division
import pandas as pd
from math import log, ceil
import numpy as np
import cea.config
from cea.optimization.constants import VCC_T_COOL_IN
from cea.constants import HEAT_CAPACITY_OF_WATER_JPERKGK

__author__ = "Thuy-An Nguyen"
__copyright__ = "Copyright 2015, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Thuy-An Nguyen", "Tim Vollrath", "Jimeno A. Fonseca"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"


# technical model

def calc_VCC(mdot_kgpers, T_sup_K, T_re_K, q_nom_chw_W, number_of_VCC_chillers):
    """
    For th e operation of a Vapor-compressor chiller between a district cooling network and a condenser with fresh water
    to a cooling tower following [D.J. Swider, 2003]_.
    The physically based fundamental thermodynamic model(LR4) is implemented in this function.
    :type mdot_kgpers : float
    :param mdot_kgpers: plant supply mass flow rate to the district cooling network
    :type T_sup_K : float
    :param T_sup_K: plant supply temperature to DCN
    :type T_re_K : float
    :param T_re_K: plant return temperature from DCN
    :rtype wdot : float
    :returns wdot: chiller electric power requirement
    :rtype qhotdot : float
    :returns qhotdot: condenser heat rejection
    ..[D.J. Swider, 2003] D.J. Swider (2003). A comparison of empirically based steady-state models for
    vapor-compression liquid chillers. Applied Thermal Engineering.
    """

    if mdot_kgpers == 0:
        wdot_W = 0
        q_cw_W = 0

    elif q_nom_chw_W == 0:
        wdot_W = 0
        q_cw_W = 0

    else:
        q_chw_W = mdot_kgpers * HEAT_CAPACITY_OF_WATER_JPERKGK * (T_re_K - T_sup_K)  # required cooling at the chiller evaporator
        T_cw_in_K = VCC_T_COOL_IN  # condenser water inlet temperature in [K]

        if q_chw_W <= q_nom_chw_W:  # the maximum capacity is assumed to be 3.5 MW, other wise the COP becomes negative

            # Tim Change:
            # COP = (tret / tcoolin - 0.0201E-3 * qcolddot / tcoolin) \
            #  (0.1980E3 * tret / qcolddot + 168.1846E3 * (tcoolin - tret) / (tcoolin * qcolddot) \
            #  + 0.0201E-3 * qcolddot / tcoolin + 1 - tret / tcoolin)

            A = 0.0201E-3 * q_chw_W / T_cw_in_K
            B = T_re_K / T_cw_in_K
            C = 0.1980E3 * T_re_K / q_chw_W + 168.1846E3 * (T_cw_in_K - T_re_K) / (T_cw_in_K * q_chw_W)

            COP = 1 / ((1 + C) / (B - A) - 1)

            if COP < 0:
                print (mdot_kgpers, T_sup_K, T_re_K, q_chw_W, COP)

            wdot_W = q_chw_W / COP
            q_cw_W = wdot_W + q_chw_W  # heat rejected to the cold water (cw) loop

        else:

            A = 0.0201E-3 * q_nom_chw_W / T_cw_in_K
            B = T_re_K / T_cw_in_K
            C = 0.1980E3 * T_re_K / q_nom_chw_W + 168.1846E3 * (T_cw_in_K - T_re_K) / (T_cw_in_K * q_nom_chw_W)

            COP = 1 / ((1 + C) / (B - A) - 1)

            if COP < 0:
                print (mdot_kgpers, T_sup_K, T_re_K, q_nom_chw_W, COP)

            wdot_W = (q_nom_chw_W / COP) * number_of_VCC_chillers
            q_cw_W = wdot_W + q_chw_W  # heat rejected to the cold water (cw) loop


    chiller_operation = {'wdot_W': wdot_W, 'q_cw_W': q_cw_W}

    return chiller_operation


# Investment costs

def calc_Cinv_VCC(qcold_W, locator, config, technology_type):
    """
    Annualized investment costs for the vapor compressor chiller

    :type qcold_W : float
    :param qcold_W: peak cooling demand in [W]
    :param gV: globalvar.py

    :returns InvCa: annualized chiller investment cost in CHF/a
    :rtype InvCa: float

    """
    Capex_a_VCC_USD = 0
    Opex_fixed_VCC_USD = 0
    Capex_VCC_USD = 0

    if qcold_W > 0:
        VCC_cost_data = pd.read_excel(locator.get_supply_systems(config.region), sheetname="Chiller")
        VCC_cost_data = VCC_cost_data[VCC_cost_data['code'] == technology_type]
        max_chiller_size = max(VCC_cost_data['cap_max'].values)
        # if the Q_design is below the lowest capacity available for the technology, then it is replaced by the least
        # capacity for the corresponding technology from the database
        if qcold_W < VCC_cost_data.iloc[0]['cap_min']:
            qcold_W = VCC_cost_data.iloc[0]['cap_min']

        if qcold_W <= max_chiller_size:

            VCC_cost_data = VCC_cost_data[(VCC_cost_data['cap_min'] <= qcold_W) & (VCC_cost_data['cap_max'] > qcold_W)]
            Inv_a = VCC_cost_data.iloc[0]['a']
            Inv_b = VCC_cost_data.iloc[0]['b']
            Inv_c = VCC_cost_data.iloc[0]['c']
            Inv_d = VCC_cost_data.iloc[0]['d']
            Inv_e = VCC_cost_data.iloc[0]['e']
            Inv_IR = (VCC_cost_data.iloc[0]['IR_%']) / 100
            Inv_LT = VCC_cost_data.iloc[0]['LT_yr']
            Inv_OM = VCC_cost_data.iloc[0]['O&M_%'] / 100
            InvC = Inv_a + Inv_b * (qcold_W) ** Inv_c + (Inv_d + Inv_e * qcold_W) * log(qcold_W)
            Capex_a_VCC_USD = InvC * (Inv_IR) * (1 + Inv_IR) ** Inv_LT / ((1 + Inv_IR) ** Inv_LT - 1)
            Opex_fixed_VCC_USD = Capex_a_VCC_USD * Inv_OM
            Capex_VCC_USD = InvC
        else:  # more than one unit of ACH are activated
            number_of_chillers = int(ceil(qcold_W / max_chiller_size))
            Q_nom_each_chiller = qcold_W / number_of_chillers

            for i in range(number_of_chillers):
                VCC_cost_data = VCC_cost_data[
                    (VCC_cost_data['cap_min'] <= Q_nom_each_chiller) & (VCC_cost_data['cap_max'] > Q_nom_each_chiller)]
                Inv_a = VCC_cost_data.iloc[0]['a']
                Inv_b = VCC_cost_data.iloc[0]['b']
                Inv_c = VCC_cost_data.iloc[0]['c']
                Inv_d = VCC_cost_data.iloc[0]['d']
                Inv_e = VCC_cost_data.iloc[0]['e']
                Inv_IR = (VCC_cost_data.iloc[0]['IR_%']) / 100
                Inv_LT = VCC_cost_data.iloc[0]['LT_yr']
                Inv_OM = VCC_cost_data.iloc[0]['O&M_%'] / 100
                InvC = Inv_a + Inv_b * (Q_nom_each_chiller) ** Inv_c + (Inv_d + Inv_e * Q_nom_each_chiller) * log(Q_nom_each_chiller)
                Capex_a1 = InvC * (Inv_IR) * (1 + Inv_IR) ** Inv_LT / ((1 + Inv_IR) ** Inv_LT - 1)
                Capex_a_VCC_USD = Capex_a_VCC_USD + Capex_a1
                Opex_fixed_VCC_USD = Opex_fixed_VCC_USD + Capex_a1 * Inv_OM
                Capex_VCC_USD = Capex_VCC_USD + InvC

    return Capex_a_VCC_USD, Opex_fixed_VCC_USD, Capex_VCC_USD


def main():
    Qc_W = 3.5
    T_chw_sup_K = 273.15 + 6
    T_chw_re_K = 273.15 + 11
    mdot_chw_kgpers = Qc_W/(HEAT_CAPACITY_OF_WATER_JPERKGK*(T_chw_re_K-T_chw_sup_K))
    chiller_operation = calc_VCC(mdot_chw_kgpers, T_chw_sup_K, T_chw_re_K)
    print chiller_operation



if __name__ == '__main__':
    main()