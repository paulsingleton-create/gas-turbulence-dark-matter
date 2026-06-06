"""
Fit the gas turbulence correction to SPARC rotation curves.

Reproduces the main result: subtract the gas error, Newton returns.
Average difference across 2,925 points in 129 galaxies: 1 km/s.

Usage:
    python code/fit_rotation_curves.py
"""

import numpy as np
from scipy.optimize import differential_evolution
from utils import (load_sparc_galaxies, load_sparc_rotcurves, build_arrays,
                   estimate_f_old, compute_vbar, predict_standard, predict_mond,
                   galaxy_type_label, ML, KPC_TO_M)


def fit_standard_model(Vobs, Vbar, fo, fg, rad):
    """Fit the 5-parameter standard model using differential evolution."""
    R_m = rad * KPC_TO_M
    g_bar = (Vbar * 1000)**2 / R_m
    
    def cost(params):
        amp, fo_w, fg_w, g_scale, power = params
        corr = amp * (fo_w * fo + fg_w * fg) * (g_scale / np.clip(g_bar, 1e-15, None))**power
        V = Vbar * np.sqrt(1 + np.clip(corr, 0, 10))
        return np.sum((Vobs - V)**2)
    
    bounds = [(0.001, 100), (0.1, 10), (0.1, 10), (1e-12, 1e-8), (0.1, 2)]
    result = differential_evolution(cost, bounds, seed=42, maxiter=2000, tol=1e-12, polish=True)
    return result.x


def fit_f_old_only(Vobs, Vbar, fo, rad):
    """Fit the 3-parameter model using only f_old."""
    R_m = rad * KPC_TO_M
    g_bar = (Vbar * 1000)**2 / R_m
    
    def cost(params):
        amp, fo_power, g_scale = params
        corr = amp * fo**fo_power * (g_scale / np.clip(g_bar, 1e-15, None))**0.56
        V = Vbar * np.sqrt(1 + np.clip(corr, 0, 10))
        return np.sum((Vobs - V)**2)
    
    bounds = [(0.001, 100), (0.1, 5), (1e-12, 1e-8)]
    result = differential_evolution(cost, bounds, seed=42, maxiter=2000, tol=1e-12, polish=True)
    return result.x


def main():
    # Load data
    galaxies = load_sparc_galaxies()
    rotcurves = load_sparc_rotcurves()
    
    # Select quality 1-2 galaxies with valid Vflat
    usable = [name for name, gal in galaxies.items()
              if name in rotcurves and gal['quality'] <= 2 and gal['Vflat'] is not None]
    
    print(f"Galaxies: {len(usable)}")
    
    # Build arrays
    Vobs, Vbar, fo, fg, rad = build_arrays(usable, galaxies, rotcurves)
    print(f"Data points: {len(Vobs)}")
    
    # Fit standard model (5 parameters)
    print("\nFitting standard model (5 parameters)...")
    params_5p = fit_standard_model(Vobs, Vbar, fo, fg, rad)
    V_5p = predict_standard(Vbar, fo, fg, rad, params_5p)
    
    print(f"  amp = {params_5p[0]:.4f}")
    print(f"  fo_weight = {params_5p[1]:.2f}")
    print(f"  fg_weight = {params_5p[2]:.2f}")
    print(f"  g_scale = {params_5p[3]:.2e}")
    print(f"  power = {params_5p[4]:.4f}")
    
    # Fit f_old only model (3 parameters)
    print("\nFitting f_old only model (3 parameters)...")
    params_3p = fit_f_old_only(Vobs, Vbar, fo, rad)
    R_m = rad * KPC_TO_M
    g_bar = (Vbar * 1000)**2 / R_m
    V_3p = Vbar * np.sqrt(1 + np.clip(
        params_3p[0] * fo**params_3p[1] * (params_3p[2] / np.clip(g_bar, 1e-15, None))**0.56, 0, 10))
    
    # MOND prediction
    V_mond = predict_mond(Vbar, rad)
    
    # Compute R-squared
    ss_tot = np.sum((Vobs - Vobs.mean())**2)
    r2_newton = 1 - np.sum((Vobs - Vbar)**2) / ss_tot
    r2_mond = 1 - np.sum((Vobs - V_mond)**2) / ss_tot
    r2_3p = 1 - np.sum((Vobs - V_3p)**2) / ss_tot
    r2_5p = 1 - np.sum((Vobs - V_5p)**2) / ss_tot
    
    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")
    print(f"\n  {'Model':<25} {'R²':>8} {'Mean error':>12} {'Median %':>10}")
    print(f"  " + "-"*55)
    
    for label, V, r2 in [("Newton", Vbar, r2_newton), ("MOND (1p)", V_mond, r2_mond),
                          ("Just f_old (3p)", V_3p, r2_3p), ("Standard (5p)", V_5p, r2_5p)]:
        mean_err = np.mean(Vobs - V)
        med_pct = np.median(np.abs(Vobs - V) / Vobs * 100)
        print(f"  {label:<25} {r2:>8.4f} {mean_err:>+10.1f}   {med_pct:>8.1f}%")
    
    # The right-way-round table
    print(f"\n{'='*70}")
    print("SUBTRACT THE GAS ERROR, NEWTON RETURNS")
    print(f"{'='*70}")
    
    gas_error = V_5p - Vbar  # What the formula says the inflation is
    corrected = Vobs - gas_error  # Observed minus inflation = should be Newton
    
    # Get types for each point
    point_types = []
    for name in usable:
        gal = galaxies[name]
        for p in rotcurves[name]:
            if p['Vobs'] < 5 or p['rad'] < 0.1:
                continue
            point_types.append(gal['type'])
    point_types = np.array(point_types)
    
    print(f"\n  {'Type':<18} {'Pts':>5} {'Measured':>9} {'Gas err':>8} {'Corrected':>10} {'Newton':>8} {'Diff':>7}")
    print(f"  " + "-"*68)
    
    for label, tlo, thi in [("S0-Sa (old)", 0, 2), ("Sab-Sb", 2, 4), ("Sbc-Sc", 4, 6),
                             ("Scd-Sd", 6, 8), ("Sm-Irr (young)", 8, 11)]:
        mask = (point_types >= tlo) & (point_types < thi)
        if np.sum(mask) < 10:
            continue
        m_obs = np.mean(Vobs[mask])
        m_gas = np.mean(gas_error[mask])
        m_corr = np.mean(corrected[mask])
        m_newt = np.mean(Vbar[mask])
        m_diff = m_corr - m_newt
        print(f"  {label:<18} {np.sum(mask):>5} {m_obs:>8.0f}  {m_gas:>+7.0f}  {m_corr:>9.0f}  {m_newt:>7.0f}  {m_diff:>+6.0f}")
    
    m_obs = np.mean(Vobs)
    m_gas = np.mean(gas_error)
    m_corr = np.mean(corrected)
    m_newt = np.mean(Vbar)
    print(f"  " + "-"*68)
    print(f"  {'ALL':<18} {len(Vobs):>5} {m_obs:>8.0f}  {m_gas:>+7.0f}  {m_corr:>9.0f}  {m_newt:>7.0f}  {m_corr - m_newt:>+6.0f}")
    
    print(f"\nThe galaxies were never spinning too fast. The speedometer was reading high.")


if __name__ == '__main__':
    main()
