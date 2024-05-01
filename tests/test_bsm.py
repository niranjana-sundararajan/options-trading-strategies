import pytest
from src import bs_model, credit_trading, debit_trading
import numpy as np

settlement_values = np.linspace(0, 200, 300)


def test_bs_option_pricing():
    s = 100
    k = 100
    t = 1
    sigma = 0.1
    r = 0.03
    bsm = bs_model.BS_Model(k, s, t, r, sigma)
    assert round(bsm.option_price("put"), 4) == 2.6264
    assert round(bsm.option_price("call"), 4) == 5.5819


def test_bs_greeks(create_graphs=True):
    s = 100
    k = 100
    t = 1
    sigma = 0.25
    r = 0.02
    bsm = bs_model.BS_Model(k, s, t, r, sigma)

    # Delta
    delta_analytical = bsm.delta_analytical("call")
    delta_fwd = bsm.delta("call", method="fwd")
    delta_bwd = bsm.delta("call", method="bwd")
    delta_central = bsm.delta("call", method="central")
    delta_errors = bsm.calc_delta_errors(option_type="call", method="fwd")
    assert round(delta_fwd, 0) != 0 
    assert round(delta_bwd, 0) != 0 
    assert round(delta_central, 0) != 0 
    assert round(delta_analytical, 0) != 0 

    assert round(delta_analytical, 0) == round(delta_fwd, 0)
    assert round(delta_analytical, 0) == round(delta_bwd, 0)
    assert round(delta_analytical, 0) == round(delta_central, 0)
    assert round(delta_analytical, 0) == round(delta_fwd, 0)

    # Gamma
    gamma_analytical = bsm.gamma_analytical()
    gamma_fwd = bsm.gamma("call", method="fwd")
    gamma_bwd = bsm.gamma("call", method="bwd")
    gamma_central = bsm.gamma("call", method="central")
    gamma_errors = bsm.calc_gamma_errors(option_type="call", method="fwd")
    assert round(gamma_fwd, 0) != 0 
    assert round(gamma_bwd, 0) != 0 
    assert round(gamma_central, 0) != 0 
    assert round(gamma_analytical, 0) != 0 

    assert round(gamma_analytical, 0) == round(gamma_fwd, 0)
    assert round(gamma_analytical, 0) == round(gamma_bwd, 0)
    assert round(gamma_analytical, 0) == round(gamma_central, 0)
    assert round(gamma_analytical, 0) == round(gamma_fwd, 0)

    
    # Vega
    vega_analytical = bsm.vega_analytical()
    vega_fwd = bsm.vega("call", method="fwd")
    vega_bwd = bsm.vega("call", method="bwd")
    vega_central = bsm.vega("call", method="central")
    vega_errors = bsm.calc_vega_errors(option_type="call", method="fwd")


    assert round(vega_analytical, 0) == round(vega_fwd, 0)
    assert round(vega_analytical, 0) == round(vega_bwd, 0)
    assert round(vega_analytical, 0) == round(vega_central, 0)
    assert round(vega_analytical, 0) == round(vega_fwd, 0)
    # Rho
    rho_analytical = bsm.rho_analytical("call")
    rho_fwd = bsm.rho("call", method="fwd")
    rho_bwd = bsm.rho("call", method="bwd")
    rho_central = bsm.rho("call", method="central")
    rho_errors = bsm.calc_rho_errors(option_type="call", method="fwd")
    # assert round(rho_analytical,0) == round(rho_fwd,0)
    # assert round(rho_analytical,0) == round(rho_bwd,0)
    # assert round(rho_analytical,0) == round(rho_central,0)
    # assert round(rho_analytical,0) == round(rho_fwd,0)
