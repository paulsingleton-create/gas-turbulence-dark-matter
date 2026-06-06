# Data Sources

## SPARC (included)

The SPARC rotation curve data is included in this repository:
- `sparc_galaxies.csv` - Galaxy properties (Hubble type, luminosity, HI mass, distance, etc.)
- `sparc_rotcurves.csv` - Rotation curve data points (radius, Vobs, Vgas, Vdisk, Vbulge)

Original source: Lelli, McGaugh, Schombert (2016)
http://astroweb.cwru.edu/SPARC/

## APOKASC-3 (download separately)

15,808 evolved stars with asteroseismic ages from Kepler.

Download from VizieR:
```
Catalog: J/ApJS/276/69
Reference: Pinsonneault et al. (2025)
```

Or use the provided download script:
```bash
python code/download_apokasc3.py
```

## GALAH DR4 (download separately)

458,000 stars with spectroscopic parameters and ages.

Download from: https://www.galah-survey.org/dr4/
Requires registration.

## Unified Rotation Curve Corpus (download separately)

438 galaxies from SPARC, THINGS, LITTLE THINGS, WALLABY.

Download from Zenodo:
```
Record: 19563417
Reference: Flynn (2026)
```

## Mass-to-light ratio

All analyses use a constant stellar mass-to-light ratio of M/L = 0.5 at 3.6 micron,
the standard SPARC assumption.
