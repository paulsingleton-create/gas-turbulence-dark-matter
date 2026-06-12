# gas-turbulence-dark-matter

Evidence that dark matter in galaxy rotation curves is a gas turbulence measurement artefact from dying stars.

## The claim

Galaxy rotation speeds measured through radio spectral lines are systematically inflated by turbulent gas ejected from old dying stars. When the estimated gas contamination is subtracted, the corrected velocities match Newton's prediction from visible matter alone. Average difference across 2,925 measurements in 129 galaxies: 1 km/s.

## The result

| Galaxy type | Measured | Gas error | Corrected | Newton | Difference |
|-------------|----------|-----------|-----------|--------|------------|
| S0-Sa (old spirals) | 188 km/s | -65 km/s | 123 km/s | 126 km/s | -3 km/s |
| Sab-Sb | 241 km/s | -67 km/s | 174 km/s | 167 km/s | +7 km/s |
| Sbc-Sc | 174 km/s | -61 km/s | 114 km/s | 122 km/s | -9 km/s |
| Scd-Sd | 113 km/s | -46 km/s | 67 km/s | 66 km/s | +1 km/s |
| Sm-Irr (young irregulars) | 59 km/s | -29 km/s | 30 km/s | 27 km/s | +3 km/s |
| **All (2,925 points)** | **153 km/s** | **-52 km/s** | **101 km/s** | **100 km/s** | **+1 km/s** |

## The formulas

**Clean formula (no circularity, 4 parameters, R² = 0.895):**

```
V = Vbar × (1 + 0.095 × (3.36 × f_old + 4.90 × f_gas) × (R/Rdisk)^0.59)
```

**Standard formula (5 parameters, R² = 0.927, beats MOND):**

```
V² = Vbar² × (1 + 0.023 × (7.01 × f_old + 1.97 × f_gas) × (5.22e-9 / g_bar)^0.56)
```

Where:
- `Vbar` = rotation speed predicted by Newton from visible matter
- `f_old` = fraction of old stars (estimated from Hubble type and gas fraction)
- `f_gas` = gas fraction (gas mass / total baryonic mass)
- `g_bar` = local baryonic gravitational acceleration
- `R/Rdisk` = distance from centre in units of disc scale length

## Performance comparison

| Model | Params | R² | Median error | Gap closed (abs) | Gap closed (SS) |
|-------|--------|-----|-------------|-----------------|----------------|
| Newton | 0 | 0.42 | 41% | 0% | 0% |
| MOND | 1 | 0.91 | 10.5% | 66% | 85% |
| Just f_old | 3 | 0.93 | 10.1% | 69% | 87% |
| Standard (g_bar) | 5 | 0.93 | 9.8% | 69% | 87% |

## Cross-validation

20 random splits (100 train / 29 test). Train R² = 0.926. Test R² = 0.926. Drop < 0.001. Zero overfitting. The formula generalises to unseen galaxies and outperforms MOND on held-out data.

## Quick start

```bash
# Install dependencies
pip install numpy scipy pandas matplotlib

# Run the main analysis
python code/fit_rotation_curves.py

# Run cross-validation
python code/cross_validation.py

# Generate the comparison table
python code/compare_models.py
```

## Data sources

All data is public:

- **SPARC** (Lelli, McGaugh, Schombert 2016): 175 galaxies with full baryonic decomposition. Download from [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/)
- **APOKASC-3** (Pinsonneault et al. 2025): 15,808 stars with asteroseismic ages. Available via [VizieR J/ApJS/276/69](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=J/ApJS/276/69)
- **GALAH DR4**: 458,000 stars with spectroscopic ages. Available via [galah-survey.org](https://www.galah-survey.org/)

See `data/README.md` for download instructions.

## Repository structure

```
gas-turbulence-dark-matter/
  LICENSE              MIT license
  README.md            This file
  code/
    fit_rotation_curves.py    Main analysis: fit formula to SPARC
    cross_validation.py       20-fold cross-validation
    compare_models.py         Newton vs MOND vs this analysis
    utils.py                  Shared functions
  data/
    README.md                 Data download instructions
    sparc_galaxies.csv        Galaxy properties (included)
    sparc_rotcurves.csv       Rotation curve data (included)
  results/
    comparison_table.csv      Model comparison results
    gap_closure_by_type.csv   Gap closure per galaxy type
    cross_validation.csv      CV results per split
  docs/
    reddit_post.md            The full analysis write-up
    references.md             Supporting literature
```

## Supporting evidence

| Survey | Telescope | Sample | Result |
|--------|-----------|--------|--------|
| GALAH DR4 | Anglo-Australian | 458,000 stars | Age-velocity R² = 0.998 |
| APOGEE DR17 | Sloan 2.5m | 145,000 stars | Confirmed, R² = 0.976 |
| APOKASC-3 | Kepler | 11,852 stars | Confirmed on asteroseismic ages, R² = 0.90 |
| SPARC | Spitzer | 129 galaxies | Rotation curves R² = 0.93 |
| Kottur et al. 2025 | Various | 16 galaxies | DM correlates with age, r = 0.91 |
| Kauffmann et al. 2015 | SDSS + HI | 187 galaxies | Rotation curve shape correlates with age |

## Key references

- Tully & Fouque (1985): Turbulence inflates velocities, constant correction applied
- Sellwood & Balbus (1999): Gas turbulence floor at 5-7 km/s
- Ianjamasimanana et al. (2017): Velocity dispersion systematically overestimated
- Koley (2023): Turbulence power law 0.52-0.67
- Kottur et al. (2025): Dark matter correlates with galaxy age
- Kauffmann et al. (2015): Rotation curve shape correlates with age, not mass
- Flynn & Cannaliato (2025): Velocity correction correlates with stellar population

## Attribution

This analysis was developed interactively across multiple AI platforms (Claude, GPT, Grok, DeepSeek) with human direction, verification, and interpretation at every step. The mechanism, key physical insights, and critical questions originated with the human researcher.

## License

MIT. See LICENSE file. Use it, check it, break it, improve it.

## Contact

Reddit: [r/EmergentAIPersonas](https://www.reddit.com/r/EmergentAIPersonas/)
