"""
Shared utility functions for the gas turbulence dark matter analysis.
"""

import numpy as np
import csv


# Constants
ML = 0.5  # Mass-to-light ratio at 3.6 micron
KPC_TO_M = 3.086e19  # kpc to metres
A0_MOND = 1.2e-10  # MOND acceleration threshold (m/s^2)


def estimate_f_old(hubble_type, f_gas):
    """
    Estimate the fraction of old stars from Hubble type and gas fraction.
    
    S0-Sa (type 0-1): high f_old (~0.65)
    Sm-Irr (type 9-10): low f_old (~0.15)
    
    This is a crude proxy. Improvement with measured stellar population
    ages is expected to improve the fit.
    """
    raw = 0.5 * max(0, 1 - hubble_type / 12) + 0.5 * (1 - f_gas)
    return 0.1 + 0.6 * raw


def load_sparc_galaxies(filepath='data/sparc_galaxies.csv'):
    """Load SPARC galaxy properties."""
    galaxies = {}
    with open(filepath, 'r') as f:
        for row in csv.DictReader(f):
            try:
                name = row['name']
                l36 = float(row['L36_GLsun']) if row['L36_GLsun'] else 0
                mhi = float(row['MHI_GMsun']) if row['MHI_GMsun'] else 0
                M_star = ML * l36
                M_gas = 1.33 * mhi  # Include helium correction
                total = M_star + M_gas
                vflat = row['Vflat_kms']
                
                galaxies[name] = {
                    'type': int(row['hubble_type']),
                    'f_gas': M_gas / total if total > 0 else 0.5,
                    'Vflat': float(vflat) if vflat and vflat != 'None' and float(vflat) > 0 else None,
                    'quality': int(row['quality']),
                    'Rdisk': float(row['Rdisk_kpc']) if row.get('Rdisk_kpc') and float(row['Rdisk_kpc']) > 0 else 1.0,
                }
            except (ValueError, KeyError):
                continue
    return galaxies


def load_sparc_rotcurves(filepath='data/sparc_rotcurves.csv'):
    """Load SPARC rotation curve data."""
    rotcurves = {}
    with open(filepath, 'r') as f:
        for row in csv.DictReader(f):
            try:
                name = row['name']
                if name not in rotcurves:
                    rotcurves[name] = []
                rotcurves[name].append({
                    'Vobs': float(row['Vobs_kms']),
                    'Vgas': float(row['Vgas_kms']),
                    'Vdisk': float(row['Vdisk_kms']),
                    'Vbulge': float(row['Vbulge_kms']),
                    'rad': float(row['rad_kpc']),
                })
            except (ValueError, KeyError):
                continue
    return rotcurves


def compute_vbar(point):
    """Compute baryonic velocity from rotation curve components."""
    vdisk = point['Vdisk'] * np.sqrt(ML)
    vgas = point['Vgas']
    vbulge = point['Vbulge'] * np.sqrt(ML)
    Vbar_sq = vdisk**2 + abs(vgas) * vgas + vbulge**2
    return np.sqrt(max(Vbar_sq, 1.0))


def build_arrays(galaxy_names, galaxies, rotcurves):
    """Build numpy arrays for fitting from a list of galaxy names."""
    Vobs_l, Vbar_l, fo_l, fg_l, rad_l = [], [], [], [], []
    
    for name in galaxy_names:
        gal = galaxies[name]
        fo = estimate_f_old(gal['type'], gal['f_gas'])
        
        for p in rotcurves[name]:
            if p['Vobs'] < 5 or p['rad'] < 0.1:
                continue
            Vbar = compute_vbar(p)
            Vobs_l.append(p['Vobs'])
            Vbar_l.append(Vbar)
            fo_l.append(fo)
            fg_l.append(gal['f_gas'])
            rad_l.append(p['rad'])
    
    return (np.array(Vobs_l), np.array(Vbar_l), np.array(fo_l),
            np.array(fg_l), np.array(rad_l))


def predict_standard(Vbar, fo, fg, rad, params=None):
    """
    Standard formula (5 parameters, g_bar version).
    
    V² = Vbar² × (1 + amp × (fo_w×f_old + fg_w×f_gas) × (g_scale/g_bar)^power)
    """
    if params is None:
        params = [0.0227, 7.01, 1.97, 5.22e-9, 0.5568]
    
    amp, fo_w, fg_w, g_scale, power = params
    R_m = rad * KPC_TO_M
    g_bar = (Vbar * 1000)**2 / R_m
    
    corr = amp * (fo_w * fo + fg_w * fg) * (g_scale / np.clip(g_bar, 1e-15, None))**power
    return Vbar * np.sqrt(1 + np.clip(corr, 0, 10))


def predict_mond(Vbar, rad):
    """MOND prediction using the simple interpolation function."""
    R_m = rad * KPC_TO_M
    g_bar = (Vbar * 1000)**2 / R_m
    ratio = np.clip(g_bar / A0_MOND, 1e-10, 1e10)
    denom = np.clip(1 - np.exp(-np.sqrt(ratio)), 1e-10, None)
    return np.sqrt(g_bar / denom * R_m) / 1000


def galaxy_type_label(hubble_type):
    """Convert numeric Hubble type to label."""
    if hubble_type < 2:
        return "S0-Sa"
    elif hubble_type < 4:
        return "Sab-Sb"
    elif hubble_type < 6:
        return "Sbc-Sc"
    elif hubble_type < 8:
        return "Scd-Sd"
    else:
        return "Sm-Irr"
