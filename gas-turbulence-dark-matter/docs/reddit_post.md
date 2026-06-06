# Violent gas from dying stars fooled us into creating dark matter

**Analysis by Paul Singleton, independent researcher, Nottingham, UK. With contributions from a collaborative AI research framework.**

---

For fifty years, astronomers have measured galaxies spinning faster than their visible matter can explain. The gap has been filled with dark matter. This analysis presents evidence that the speed measurements themselves are too high, inflated by violent gas ejected from dying stars. The speed error is what we have been calling dark matter.

When the estimated gas contamination is subtracted from the observed speeds, the corrected velocities match Newton's prediction from visible matter alone. Average difference across 2,925 measurements in 129 galaxies: 1 km/s.

---

## The problem

A radio telescope pointed at the hydrogen gas orbiting a galaxy measures its rotation speed. Add up all the visible matter, apply Newton's gravity, and the predicted speed falls short. Typically 30 to 70 km/s short. This gap has been attributed to dark matter since the 1970s.

## How the speed is measured

The gas emits radio waves at a known frequency (the 21cm hydrogen line). The Doppler shift tells you the speed. The standard method takes the fastest edge of the gas signal at each position and records this as the rotation speed. All the mass estimates and dark matter calculations that follow are built on this number.

## What goes wrong

Old stars die. When a star has burned through roughly 80% of its fuel, it swells into a red giant and ejects its outer layers into the surrounding gas at 10 to 20 km/s. A solar-mass star loses nearly half its mass this way. In a mature galaxy, billions of stars are doing this continuously.

This ejected gas stirs up the surrounding interstellar medium. The 21cm signal from turbulent gas is broader than from calm gas. When the signal is broader, the fastest edge reads higher. Not because the gas is orbiting faster, but because the turbulence pushes the fast edge of the line profile outward.

The galaxy gets assigned a rotation speed that is too high. Every calculation built on that speed inherits the error. The galaxy did not need dark matter. The galaxy needed a better speedometer.

## Why it gets worse in the outer galaxy

Gravity tries to settle the stirred-up gas back into a calm circular orbit. Whether it succeeds depends on how strong gravity is.

In the inner galaxy, gravity is strong. The gas settles quickly between kicks from dying stars. The measurement is accurate. Newton works.

In the outer galaxy, gravity is weak. The gas takes millions of years to settle. The kicks keep coming before it calms down. Turbulence stacks up, layer on layer. The measurement reads increasingly high. The apparent dark matter grows with distance from the centre. Exactly as observed.

The turbulence accumulates as a random walk of partially settling kicks: each kick adds energy, each settling removes some, and the residual builds as the square root of the number of unsettled kicks. This gives a radial power of approximately 0.5, independently matching both the measured turbulence scaling in the interstellar medium (Koley 2023: 0.52 to 0.67) and the deep-regime scaling of MOND.

## Why it gets worse in gas-rich galaxies

In young, gas-rich galaxies, a second source of kicks operates. Rapid star formation produces massive stars that explode as supernovae, blasting the surrounding gas at thousands of km/s. In a small dwarf galaxy, a single supernova can churn up a significant fraction of the entire disc.

The gas in these violent environments cannot dampen the kicks because it is itself being blasted. In an old, settled spiral, the dense calm gas absorbs disturbances and smooths them out. In a young, gas-rich dwarf, there is no cushion. The cushion is on fire.

## Why it was not caught

The turbulence correction was known. Tully and Fouque measured it in 1985: turbulent gas inflates velocity measurements by 10 to 15 km/s. They published the correction. It has been applied as a constant ever since.

But it was applied as a constant. The same 10 to 15 km/s for every galaxy. Nobody made the correction depend on how many old dying stars the galaxy has. A galaxy with more old stars has more gas being pumped into its interstellar medium. The correction should be larger. It was not. The constant correction hid the variable correction.

Current automated pipelines continue this practice. The WALLABY survey, for example, assumes a fixed velocity dispersion of 10 km/s for all 203 galaxies in its rotation curve catalogue, regardless of age, mass, or gas content.

## The result: subtract the gas error, Newton returns

All speeds in km/s. Galaxy types run from old, gas-poor spirals (S0-Sa) to young, gas-rich irregulars (Sm-Irr). S0-Sa are massive, settled galaxies dominated by old stars. Sab through Sd are progressively younger spirals with increasing gas content and star formation. Sm-Irr are small, chaotic, gas-rich dwarfs.

| Galaxy type | Measured speed | Gas error | Corrected speed | Newton | Difference |
|-------------|---------------|-----------|----------------|--------|------------|
| S0-Sa (old spirals) | 188 km/s | -65 km/s | 123 km/s | 126 km/s | -3 km/s |
| Sab-Sb | 241 km/s | -67 km/s | 174 km/s | 167 km/s | +7 km/s |
| Sbc-Sc | 174 km/s | -61 km/s | 114 km/s | 122 km/s | -9 km/s |
| Scd-Sd | 113 km/s | -46 km/s | 67 km/s | 66 km/s | +1 km/s |
| Sm-Irr (young irregulars) | 59 km/s | -29 km/s | 30 km/s | 27 km/s | +3 km/s |
| **All (2,925 points)** | **153 km/s** | **-52 km/s** | **101 km/s** | **100 km/s** | **+1 km/s** |

The gas error is age-dependent. Old galaxies (S0-Sa) lose 65 km/s. Young irregulars lose 29 km/s. This is not a constant subtracted. It scales with how many dying stars the galaxy has.

The gap closure measured by absolute errors is 69%. Measured by sum of squares it is 87%. Both are reported for transparency. The difference arises because a small number of galaxies with large individual errors pull down the absolute measure. These likely arise from local events within galaxies: clusters of stars reaching the mass-loss phase simultaneously, a recent supernova near the line of sight, or regions with unusual star formation history. The formula uses one age estimate per galaxy. The galaxy is not uniform. With spatially resolved age data, the closure would be expected to increase.

## One variable does the job

One galaxy property, the fraction of old stars, predicts 92% of the velocity variation attributed to dark matter. Three fitted parameters. Adding the gas fraction pushes it to 93% with five parameters, but the two variables correlate at r = -0.96. They are effectively one variable measured two ways: evolutionary age.

That a single variable can predict 92% across galaxies spanning four orders of magnitude in mass suggests galaxy evolution is remarkably uniform. Every galaxy runs the same process. The variation is small because they have all converged toward the same equilibrium.

## Cross-validation: the formula works on unseen galaxies

To test for overfitting, the 129 galaxies were split into 100 for training and 29 for testing, repeated across 20 random splits. The formula predicts unseen galaxies at R-squared = 0.926, matching its training performance. The drop is less than 0.001. Zero overfitting. The formula generalises.

On unseen galaxies alone, the formula outperforms MOND (R-squared = 0.910), which requires no fitting but has no physical mechanism.

## The testable prediction

If this mechanism is correct, the dark matter signal should be weaker in the young universe. At redshifts above 0.5, most stellar populations have not yet reached the mass-loss phase. Less gas is being ejected. Less turbulence. The speedometer error is smaller. The apparent dark matter fraction should decrease with lookback time. This is testable with the James Webb Space Telescope.

## What this does not explain

This analysis addresses galaxy rotation curves measured through gas spectral lines. It does not address gravitational lensing, the Bullet Cluster, the cosmic microwave background, or galaxy cluster dynamics. These observations measure mass through gravitational effects on light or galaxy motions, not through gas spectroscopy. A measurement error in gas spectral lines would not directly affect them. They may require separate explanations.

## The punchline

The galaxies were never spinning too fast. The speedometer was reading high.

---

## Below the line: the numbers

**The formulas**

The clean formula (no circularity, uses distance from centre):
V = Vbar x (1 + 0.095 x (3.36 x f_old + 4.90 x f_gas) x (R/Rdisk)^0.59)

In plain language: take the speed Newton predicts from visible matter. Add a correction that grows with the old-star fraction, the gas fraction, and the distance from the centre. The correction gets bigger further out because gravity gets weaker and the gas cannot settle between kicks.

The standard formula (uses local gravitational acceleration, beats MOND):
V-squared = Vbar-squared x (1 + 0.023 x (7.01 x f_old + 1.97 x f_gas) x (5.22e-9 / g_bar)^0.56)

In plain language: same idea, but instead of distance, this version uses the local gravitational field strength. Where gravity is strong, the correction is small. Where gravity is weak, the correction is large. The old-star term is 3.6 times stronger than the gas term because continuous mass loss from billions of dying stars produces more cumulative turbulence than occasional supernovae.

The power 0.56 is close to the square root. This is the signature of a random walk: turbulence accumulating through partial settling of repeated kicks. Pure accumulation without settling would give power 1.0 (tested and rejected, R-squared = 0.72). Partial settling with residual accumulation gives power 0.5.

**The comparison**

| Model | Params | R-squared | Median error | Within 10% | Within 15% | Closed (abs) | Closed (SS) |
|-------|--------|-----------|-------------|-----------|-----------|-------------|------------|
| Newton | 0 | 0.42 | 41% | 6% | 11% | 0% | 0% |
| MOND | 1 | 0.91 | 10.5% | 48% | 67% | 66% | 85% |
| Just f_old | 3 | 0.93 | 10.1% | 50% | 67% | 69% | 87% |
| Standard (g_bar) | 5 | 0.93 | 9.8% | 51% | 67% | 69% | 87% |
| Kick-damp | 6 | 0.93 | 9.8% | 51% | 68% | 69% | 88% |

Closed (absolute) uses absolute errors with no cancellation. Closed (sum of squares) is the standard statistical measure.

**The datasets**

| Survey | Telescope | What was tested | Sample | Result |
|--------|-----------|----------------|--------|--------|
| GALAH DR4 | Anglo-Australian | Velocity dispersion vs age | 458,000 stars | Age-velocity R-squared = 0.998 |
| APOGEE DR17 | Sloan 2.5m | Same test, independent pipeline | 145,000 stars | Confirmed, R-squared = 0.976 |
| APOKASC-3 | Kepler | Age-velocity on asteroseismic ages | 11,852 stars | Confirmed, R-squared = 0.90 |
| SPARC | Spitzer | Rotation curves vs age and gas | 129 galaxies | R-squared = 0.93 |
| Kottur et al. 2025 | Various | Dark matter vs galaxy age | 16 galaxies | r = 0.91 |
| Kauffmann et al. 2015 | SDSS + HI | Rotation curve shape vs properties | 187 galaxies | Age beats mass |

Each dataset was analysed independently. No dataset was used to calibrate the results from another. The convergence across independent surveys, telescopes, and methods is the strongest evidence that the age-velocity relationship is physical, not a pipeline artefact.

**Supporting references**

Tully and Fouque (1985): turbulence inflates velocities, constant correction applied.
Sellwood and Balbus (1999): gas turbulence floor at 5-7 km/s in all disc galaxies.
Ianjamasimanana et al. (2017): velocity dispersion systematically overestimated by standard methods.
Koley (2023): turbulence power law 0.52-0.67 (this analysis recovers 0.59).
Kottur et al. (2025): dark matter content correlates with galaxy age, r = 0.91.
Kauffmann et al. (2015): rotation curve shape correlates with age, not mass.
Flynn and Cannaliato (2025, Frontiers in Astronomy and Space Sciences): velocity correction correlates with stellar population.

**Data and code**

SPARC database: Lelli, McGaugh, Schombert (2016). 129 galaxies, public.
APOKASC-3: Pinsonneault et al. (2025). 11,852 stars, public via VizieR.
Unified rotation curve corpus: Flynn (2026). 438 galaxies, public via Zenodo.
Full analysis code and worked examples will be available on GitHub.

**Attribution**

This analysis was developed interactively across multiple AI platforms (Claude, GPT, Grok, DeepSeek) with human direction, verification, and interpretation at every step. The mechanism, key physical insights, and critical questions originated with the human researcher.

---

**A note on MOND**

This formula was developed independently of MOND using a different mathematical form fitted to the SPARC data. The two approaches produce comparable results because both appear to describe the same underlying pattern: velocities are inflated more where the gravitational field is weaker.

MOND proposes that gravity itself changes below an acceleration threshold of 1.2 x 10^-10 m/s-squared. No physical mechanism has been identified for this change, and no laboratory, spacecraft, or solar system measurement has detected it. This analysis proposes that the velocity measurements are contaminated by turbulent gas from dying stars, and the contamination becomes significant where gravity is too weak to settle the gas between kicks.

MOND treats its threshold as a universal constant. This analysis predicts the threshold depends on the stellar population age and should vary with cosmic epoch. At high redshift, where fewer stars have reached the mass-loss phase, the contamination should be smaller and the apparent dark matter fraction should decrease. This is the key observational test that separates the two interpretations.

Milgrom's achievement in capturing the pattern with a single number in 1983 was extraordinary. This analysis suggests what that number may have been measuring.

---

*"The constant correction hid the variable correction."*

*Posted to r/CoherencePhysics*
