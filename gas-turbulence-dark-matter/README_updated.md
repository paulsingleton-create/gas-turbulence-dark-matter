# gas-turbulence-dark-matter

Evidence that dark matter in galaxy rotation curves is a gas turbulence measurement artefact from dying stars.

## The claim

Galaxy rotation speeds measured through radio spectral lines are systematically inflated by non-circular gas ejected from old dying stars. Tilted-ring fitting pipelines (3DBarolo, ROTCUR) assume purely circular motion (V_rad = 0) and absorb the radial component into V_rot. When the estimated gas contamination is subtracted, the corrected velocities match Newton's prediction from visible matter alone. Average difference across 2,925 measurements in 129 galaxies: 1 km/s.

## The mechanism

The true velocity field contains a radial term the pipeline drops:

```
True:     V_los = V_sys + V_rot(R) × sin(i) × cos(θ) + V_rad(R) × sin(i) × sin(θ)
Pipeline: V_los = V_sys + V_rot(R) × sin(i) × cos(θ)
```

AGB stars eject gas at ~6.6 km/s radially after ISM deceleration. This matches 30 years of radio observations of the cold gas floor (6-8 km/s). The 50 km/s rotation error is not 50 km/s of local turbulence — it is 6.6 km/s of radial wind amplified by the velocity gradient (V_bar/482 km/s) across the beam.

The phenomenological formula is mathematically equivalent to this physical V_rad absorption model (R² = 0.9261 vs 0.9266).

## The result

| Galaxy type | Measured | Gas error | Corrected | Newton | Difference |
|------------|----------|-----------|-----------|--------|------------|
| S0-Sa (old spirals) | 188 km/s | -65 km/s | 123 km/s | 126 km/s | -3 km/s |
| Sab-Sb | 241 km/s | -67 km/s | 174 km/s | 167 km/s | +7 km/s |
| Sbc-Sc | 174 km/s | -61 km/s | 114 km/s | 122 km/s | -9 km/s |
| Scd-Sd | 113 km/s | -46 km/s | 67 km/s | 66 km/s | +1 km/s |
| Sm-Irr (young irregulars) | 59 km/s | -29 km/s | 30 km/s | 27 km/s | +3 km/s |
| **All (2,925 points)** | **153 km/s** | **-52 km/s** | **101 km/s** | **100 km/s** | **+1 km/s** |

## The formulas

**Clean formula** (no circularity, 4 parameters, R² = 0.895):

```
V = Vbar × (1 + 0.095 × (3.36 × f_old + 4.90 × f_gas) × (R/Rdisk)^0.59)
```

**Standard formula** (5 parameters, R² = 0.927, beats MOND):

```
V² = Vbar² × (1 + 0.023 × (7.01 × f_old + 1.97 × f_gas) × (5.22e-9 / g_bar)^0.56)
```

**f_old only** (3 parameters, R² = 0.926, one astrophysical variable):

```
V² = Vbar² × (1 + 0.023 × 7.01 × f_old × (5.22e-9 / g_bar)^0.56)
```

Where:

- `Vbar` = rotation speed predicted by Newton from visible matter
- `f_old` = fraction of old stars (estimated from Hubble type and gas fraction)
- `f_gas` = gas fraction (gas mass / total baryonic mass)
- `g_bar` = local baryonic gravitational acceleration (m/s²)
- `R/Rdisk` = distance from centre in units of disc scale length

## Performance comparison

| Model | Params | R² | Median error | Gap closed (abs) | Gap closed (SS) |
|-------|--------|-----|-------------|-----------------|-----------------|
| Newton | 0 | 0.42 | 41% | 0% | 0% |
| MOND | 1 | 0.91 | 10.5% | 66% | 85% |
| Just f_old | 3 | 0.93 | 10.1% | 69% | 87% |
| Standard (g_bar) | 5 | 0.93 | 9.8% | 69% | 87% |

## Cross-validation

20 random splits (100 train / 29 test). Train R² = 0.926. Test R² = 0.926. Drop < 0.001. Zero overfitting. The formula generalises to unseen galaxies and outperforms MOND on held-out data.

## The smoking gun: Quirk et al. (2019)

Quirk, Guhathakurta et al. (2019, ApJ, 871, 11) measured the gas-star velocity offset in M31 across four stellar age bins: Main Sequence (0.03 Gyr), Luminous AGB (0.4 Gyr), Faint AGB (2 Gyr), RGB (4 Gyr). The offset **increases with stellar age through the AGB mass-loss stages** — exactly the prediction of this model.

Additionally: "Gaussian fits result in higher rotation velocities than velocities derived from first moment maps." The extraction method shifts V_rot.

Additionally: "The most significant cause of scatter comes from the tilted ring model being an imperfect way to account for the multiple warps." Tilted-ring problems confirmed.

Reproduced in IllustrisTNG simulations: Quirk et al. (2020, MNRAS).

## Milky Way confirmation

Gaia DR3 stellar rotation curves (Eilers 2019, Jiao 2023, Ou 2024) show a **declining** rotation curve from 237 km/s at 5 kpc to 170 km/s at 26 kpc. The HI gas curve stays flat at ~220 km/s. The gas-star gap grows with radius — from negative in the inner disc to +50 km/s at 26 kpc. This is consistent with increasing V_rad contamination in the outer disc where old stellar populations dominate.

Jiao et al. (2023) reject a flat Milky Way rotation curve at 3σ significance.

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

- **SPARC** (Lelli, McGaugh, Schombert 2016): 175 galaxies with full baryonic decomposition. Download from astroweb.cwru.edu/SPARC
- **APOKASC-3** (Pinsonneault et al. 2025): 15,808 stars with asteroseismic ages. Available via VizieR J/ApJS/276/69
- **GALAH DR4**: 458,000 stars with spectroscopic ages. Available via galah-survey.org

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
    paper.md                  Full technical paper
    reddit_post.md            The original analysis write-up
    references.md             Supporting literature
```

## Supporting evidence

| Evidence | Source | Result |
|----------|--------|--------|
| Age predicts velocity dispersion | GALAH DR4, APOGEE DR17, APOKASC-3 | R² = 0.90-0.998 |
| Age predicts rotation curves | SPARC (129 galaxies) | R² = 0.93, beats MOND |
| Zero overfitting | Cross-validation (20 splits) | Train = Test = 0.926 |
| Age predicts DM fraction | Kottur et al. 2025 | r = 0.91 |
| Age predicts RC shape | Kauffmann et al. 2015 | Age beats mass |
| Gas-star offset scales with age | Quirk et al. 2019 (M31) | Increases through AGB stages |
| Extraction method shifts V_rot | Quirk et al. 2019 | Gaussian > first moment |
| Tilted-ring causes scatter | Quirk et al. 2019 | Confirmed in M31 |
| High-z galaxies show less DM | Sharma et al. 2023 | Prediction confirmed |
| Pipeline assumes constant dispersion | WALLABY (203 galaxies) | 10 km/s for all galaxies |
| Formula = physical V_rad model | Equivalence proof | R² match, 6.6 km/s wind |
| Cold gas floor = fitted wind speed | 30 years radio observations | 6-8 km/s = our 6.6 km/s |
| Stellar curve declines, gas flat | Gaia DR3 vs HI (Milky Way) | Gas reads higher in outer disc |

## Key references

- Quirk et al. (2019), ApJ, 871, 11: Gas-star velocity offset scales with stellar age in M31
- Quirk et al. (2020), MNRAS: Reproduced in IllustrisTNG simulations
- Jiao et al. (2023): Milky Way rotation curve declining, Gaia DR3
- Ou et al. (2024): Milky Way circular velocity from Gaia DR3
- Eilers et al. (2019): MW rotation curve from RGB stars
- Tully & Fouque (1985): Turbulence inflates velocities, constant correction applied
- Sellwood & Balbus (1999): Gas turbulence floor at 5-7 km/s
- Ianjamasimanana et al. (2017): Velocity dispersion systematically overestimated
- Sharma et al. (2023): DM fraction decreases at high redshift
- Kottur et al. (2025): Dark matter correlates with galaxy age
- Kauffmann et al. (2015): Rotation curve shape correlates with age, not mass

## Attribution

Paul Singleton — Independent researcher, Nottingham, UK.

This analysis was developed interactively across multiple AI platforms (Claude, Gemini, GPT, Grok, DeepSeek) with human direction, verification, and interpretation at every step. The mechanism, key physical insights, and critical questions originated with the human researcher.

## License

MIT. See LICENSE file. Use it, check it, break it, improve it.

## Contact

Paul Singleton
Reddit: u/Humor_Complex | r/EmergentAIPersonas
GitHub: github.com/paulsingleton-create
