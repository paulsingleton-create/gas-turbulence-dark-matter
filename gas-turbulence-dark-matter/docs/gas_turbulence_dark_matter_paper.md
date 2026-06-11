# Gas Turbulence and the Dark Matter Signal
## A Measurement Contamination Hypothesis for Galaxy Rotation Curves
### Paul Singleton — Independent Researcher, Nottingham, UK
### Updated: June 12, 2026

---

## Abstract

We propose that the apparent dark matter signal in galaxy rotation curves is substantially explained by a systematic measurement error in radio velocity extraction pipelines. Asymptotic Giant Branch (AGB) stars eject gas with non-circular radial velocities of approximately 6.6 km/s. Tilted-ring fitting codes (3DBarolo, ROTCUR) assume purely circular motion (V_rad = 0) and absorb the non-circular component into V_rot, inflating the observed rotation velocity. The inflation scales with the local velocity gradient and the fraction of old stars in the galaxy. Applied to 129 SPARC galaxies, this model achieves R² = 0.927 with five parameters, beats MOND on unseen galaxies in cross-validation, and closes the gap between observed and Newtonian rotation velocities to within 1 km/s on average. The mechanism is supported by independent peer-reviewed observations in M31 (Quirk et al. 2019), pipeline assumptions in WALLABY (203 galaxies), and 30 years of cold gas floor measurements.

---

## 1. The Pipeline Error

### 1.1 What the telescope measures

The true velocity field of a galaxy contains three components:

```
V_los = V_sys + V_rot(R) × sin(i) × cos(θ) + V_rad(R) × sin(i) × sin(θ)
```

Where:
- V_los = line-of-sight velocity (observed)
- V_sys = systemic velocity of the galaxy
- V_rot = circular rotational velocity
- V_rad = radial velocity (non-circular inward/outward motion)
- i = inclination angle
- θ = azimuthal angle

### 1.2 What the pipeline assumes

Standard tilted-ring fitting assumes:

```
V_los = V_sys + V_rot(R) × sin(i) × cos(θ)
```

The V_rad term is dropped. The pipeline has no parameter for radial motion. Any non-circular velocity component is absorbed into V_rot, inflating the reported rotation velocity.

### 1.3 Source of the non-circular gas

AGB stars (asymptotic giant branch, the late evolutionary phase of old stars) eject gas at 10-30 km/s through stellar winds. After deceleration in the interstellar medium, the residual radial velocity is approximately 6.6 km/s. This gas retains non-circular motion that the tilted-ring fitting cannot model.

---

## 2. The Formulas

### 2.1 Formula 1 — Radius/Scale-Length Model (4 parameters)

```
V = V_bar × (1 + 0.0946 × (3.36 × f_old + 4.90 × f_gas) × (R/R_disk)^0.59)
```

R² = 0.895 on 129 SPARC galaxies.

### 2.2 Formula 2 — Gravitational Acceleration Model (5 parameters)

```
V² = V_bar² × (1 + 0.0227 × (7.01 × f_old + 1.97 × f_gas) × (5.22×10⁻⁹ / g_bar)^0.557)
```

R² = 0.927 on 129 SPARC galaxies, 2,925 individual measurements.

### 2.3 Formula 3 — f_old Only (3 parameters)

```
V² = V_bar² × (1 + 0.0227 × 7.01 × f_old × (5.22×10⁻⁹ / g_bar)^0.557)
```

R² = 0.926. One astrophysical variable: the fraction of old stars.

### Variable definitions

| Symbol | Definition | Units |
|--------|-----------|-------|
| V_bar | Circular velocity from baryonic matter (Newton) | km/s |
| V_obs | Observed rotation velocity (pipeline output) | km/s |
| f_old | Fraction of stars older than ~5 Gyr | dimensionless |
| f_gas | Gas fraction (gas mass / total baryonic mass) | dimensionless |
| g_bar | Baryonic gravitational acceleration = V_bar²/R | m/s² |
| R | Galactocentric radius | kpc |
| R_disk | Disc scale length | kpc |

### 2.4 Physical decomposition

The formula parameters correspond to physical quantities:

| Parameter | Value | Physical meaning |
|-----------|-------|-----------------|
| 6.6 km/s | Effective AGB wind speed | Matches observed cold gas floor (6-8 km/s, 30 years of radio observations) |
| 482 km/s | Gradient reference velocity | Determines how the velocity gradient amplifies the wind |
| 0.446 | Settling power | Consistent with random walk with partial gravitational settling (theoretical: 0.5) |
| 7.01 | f_old weight | Old stars contribute ~3.5× more than gas fraction |
| 1.97 | f_gas weight | Gas fraction secondary contributor |

The phenomenological formula is mathematically equivalent to the physical V_rad absorption model (R² = 0.9261 vs 0.9266).

---

## 3. Results

### 3.1 Cross-validation

| Metric | Value |
|--------|-------|
| Training galaxies | 100 (random) |
| Test galaxies | 29 (unseen) |
| Splits | 20 |
| Train R² | 0.926 |
| Test R² | 0.926 |
| Overfitting | < 0.001 |

### 3.2 Gap closure by morphological type

Subtract the predicted gas error from observed velocities. Newtonian gravity returns.

| Galaxy Type | V_obs (km/s) | Gas Error (km/s) | Corrected (km/s) | Newton (km/s) | Residual (km/s) |
|------------|-------------|-------------------|-------------------|---------------|-----------------|
| S0-Sa | 188 | -65 | 123 | 126 | -3 |
| Sab-Sb | 241 | -67 | 174 | 167 | +7 |
| Sbc-Sc | 174 | -61 | 114 | 122 | -9 |
| Scd-Sd | 113 | -46 | 67 | 66 | +1 |
| Sm-Irr | 59 | -29 | 30 | 27 | +3 |
| **ALL (129)** | **153** | **-52** | **101** | **100** | **+1** |

### 3.3 Comparison with MOND

| Model | Free Parameters | R² | Median Error |
|-------|----------------|-----|-------------|
| Newton (no DM) | 0 | 0.42 | 41% |
| MOND | 1 | 0.91 | 10.5% |
| f_old only | 3 | 0.93 | 10.1% |
| Standard (Formula 2) | 5 | 0.93 | 9.8% |

### 3.4 The knife test

A 6.6 km/s radial wind produces an average 52 km/s rotational velocity error across 129 galaxies. The amplification occurs through the velocity gradient: V_bar/482 km/s determines how much the pipeline inflates V_rot at each point. Massive galaxies with steep gradients show 65 km/s error; dwarfs show 29 km/s.

---

## 4. Supporting Evidence

### 4.1 The smoking gun: Quirk et al. (2019)

"Asymmetric Drift in the Andromeda Galaxy (M31) as a Function of Stellar Age." Quirk, Guhathakurta et al. (2019), ApJ, 871, 11.

Key findings directly relevant to this hypothesis:

1. **Gas-star velocity offset increases with stellar age** across four evolutionary bins: Main Sequence (0.03 Gyr), Luminous AGB (0.4 Gyr), Faint AGB (2 Gyr), RGB (4 Gyr). The offset scales with the AGB mass-loss phase. This is the direct prediction of our model.

2. **Extraction method matters.** "Gaussian fits result in higher rotation velocities than velocities derived from first moment maps." The choice of kinematic extraction methodology shifts V_rot.

3. **Tilted-ring limitations confirmed.** "The most significant cause of scatter comes from the tilted ring model being an imperfect way to account for the multiple warps."

Quirk et al. attribute the velocity offset to asymmetric drift (old stars lagging). Our model offers an alternative: gas velocities are inflated by V_rad contamination near old stars. Same data, opposite causal direction.

Distinguishing test: asymmetric drift predicts the true rotation curve equals the gas curve (stars are slow). Our model predicts the true curve is closer to the stellar curve (gas reads high). Gaia DR3 data for the Milky Way shows the stellar rotation curve declining while HI gas remains flat, consistent with our model (Jiao et al. 2023; Ou et al. 2024).

Reproduced in IllustrisTNG simulations: Quirk et al. (2020, MNRAS).

### 4.2 Complete evidence chain

| Evidence | Source | Result |
|----------|--------|--------|
| Age predicts velocity dispersion | GALAH DR4, APOGEE DR17, APOKASC-3 | R² = 0.90-0.998 |
| Age predicts rotation curves | SPARC (129 galaxies) | R² = 0.93, beats MOND |
| Zero overfitting | Cross-validation (20 splits) | Train = Test = 0.926 |
| Age predicts DM fraction | Kottur et al. 2025 | r = 0.91 |
| Age predicts RC shape | Kauffmann et al. 2015 | Age beats mass as predictor |
| Gas-star offset scales with age | Quirk et al. 2019 (M31) | Increases through AGB stages |
| Extraction method shifts V_rot | Quirk et al. 2019 | Gaussian > first moment |
| Tilted-ring causes scatter | Quirk et al. 2019 | Confirmed in M31 |
| High-z galaxies show less DM | Sharma et al. 2023 | Prediction confirmed |
| Pipeline assumes constant dispersion | WALLABY (203 galaxies) | 10 km/s for all galaxies |
| Formula = physical V_rad model | Equivalence proof | R² match, 6.6 km/s wind |
| Cold gas floor = fitted wind speed | 30 years radio observations | 6-8 km/s = our 6.6 km/s |
| Stellar curve declines, gas flat | Gaia DR3 (Jiao, Ou, Eilers) | Gas reads higher than stars in outer MW |
| Stellar-gas gap grows with radius | Gaia vs HI comparison | Consistent with V_rad contamination |

---

## 5. What This Model Does Not Yet Address

### 5.1 Gravitational lensing

Lensing measures total mass independently of velocity pipelines. This model does not claim lensing is directly contaminated. However, three mechanisms may reduce the inferred lensing dark matter:

1. **Baryonic mass subtraction error.** Lensing dark matter = total mass - baryonic mass. Baryonic mass estimates carry 40% uncertainty in stellar mass-to-light ratios and factor-of-2 uncertainty in molecular gas. If baryonic mass is systematically underestimated, lensing dark matter is overestimated.

2. **Hydrostatic mass bias.** In galaxy clusters, gas-based mass estimates are 10-30% too low due to non-thermal pressure support, bulk motions, and turbulence. This is a known problem in cluster physics.

3. **Cumulative gas feedback.** Older galaxies have more red giants, more AGB mass loss, and more energy deposited into the surrounding medium over cosmic time. This creates structured gas environments (shells, filaments, density waves from overlapping feedback) that alter the mass distribution and potentially affect lensing profiles.

The key prediction: if the lensing dark matter fraction correlates with the stellar population age of the lens independently of total mass, this model has an explanation. If it does not correlate, this pathway is excluded.

### 5.2 CMB and large-scale structure

Not addressed in the current model. These require separate treatment.

### 5.3 Compatibility with dark matter

This model may explain 50-70% of the dark matter signal in rotation curves. It is not necessarily incompatible with a reduced dark matter component. Galaxy dynamics may contain overlooked systematic velocity terms AND dark matter may still exist. These are not mutually exclusive.

---

## 6. Predictions

| Prediction | Test | Status |
|-----------|------|--------|
| Gas reads faster than stars, gap scales with age | Quirk et al. 2019 (M31) | Confirmed |
| Young galaxies show less DM | Sharma et al. 2023 (high-z) | Confirmed |
| Stellar rotation curve declines, gas flat | Gaia DR3 vs HI (Milky Way) | Confirmed |
| Pipeline using constant dispersion | WALLABY (203 galaxies) | Confirmed |
| Fitted wind = cold gas floor | 30 years radio data | Confirmed |
| Gas-star gap grows with radius | Gaia vs HI | Confirmed |
| Lensing DM correlates with stellar age | Not yet tested | Open |
| Multi-tracer RC gives different results | Hα vs HI vs CO for same galaxy | Open |

---

## 7. Data and Code

All code, data, and rotation curve plots are available at:

**GitHub:** github.com/paulsingleton-create/gas-turbulence-dark-matter

- SPARC galaxy data (Lelli, McGaugh & Schombert 2016)
- Rotation curve fitting code (Python)
- Cross-validation scripts
- Rotation curve comparison plots (129 galaxies)
- MIT License

---

## References

- Quirk et al. (2019), ApJ, 871, 11 — Asymmetric drift in M31 by stellar age
- Quirk et al. (2020), MNRAS — IllustrisTNG confirmation
- Lelli, McGaugh & Schombert (2016) — SPARC database
- Sharma et al. (2023), MNRAS 506 — Dark matter fraction at high redshift
- Kottur et al. (2025) — DM fraction correlates with galaxy age
- Kauffmann et al. (2015) — Age beats mass for rotation curve shape
- Jiao et al. (2023) — Milky Way rotation curve declining (Gaia DR3)
- Ou et al. (2024) — Milky Way circular velocity (Gaia DR3)
- Eilers et al. (2019) — Milky Way rotation curve from RGB stars

---

## Contact

Paul Singleton
GitHub: github.com/paulsingleton-create
Reddit: r/EmergentAIPersonas (u/Humor_Complex)

---

*153 - 52 = 101. Newton says 100.*
*The gas is cold. The speedometer reads high.*
*The algorithm has no drawer for V_rad. It goes into V_rot.*
