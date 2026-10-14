---
id: 26-05-06
title: "Synthetic Data Generators for Learning and Testing"
level: intermediate
prereqs: []
estimated_minutes: 25
tags: [reference, datasets, synthetic, testing]
---

# Synthetic Data Generators for Learning and Testing

Synthetic data are the only data whose true answer you know. They are therefore
the right tool for validating code, calibrating an inversion, and teaching — and
the wrong tool for any statement about the Earth. This page gives the standard
generators, the formulas behind them, and the provenance rules that keep
synthetic results honest.

## How to use this page

Every generator below is **SYNTHETIC**: it computes data from a model you chose.
The rule that matters is disclosure: a synthetic result must state the true
model, the noise model, the seed and the units, or it is not reproducible and not
interpretable.

**Provenance labels:** OBSERVED, ILLUSTRATIVE, SYNTHETIC — defined in
[26-05-01](./01-datasets-seismology.md#how-to-use-this-page).

*Provenance of this page:* a catalogue and formula list. The generators described
here are deterministic formulas or documented random processes; the numbers all
come from the model, never from the Earth.

## 1. Seismic waveforms and travel times

| Generator | Formula or recipe | Conditions and cautions |
|---|---|---|
| Ricker wavelet | $w(t) = (1 - 2\pi^{2}f_0^{2}t^{2})e^{-\pi^{2}f_0^{2}t^{2}}$ | zero-phase; $f_0$ is the dominant frequency, and the peak frequency of the amplitude spectrum is close to but not exactly $f_0$ |
| Synthetic trace | convolve a reflectivity series $r(t)$ with a wavelet: $s(t) = w(t) \ast r(t)$ | assumes a stationary wavelet; real wavelets change with depth and offset |
| Reflectivity series | $r_i = (Z_{i+1} - Z_i)/(Z_{i+1} + Z_i)$, $Z = \rho v$ | normal incidence only; no multiples, no transmission loss |
| Layered travel time | $t(x) = \sum_i \Delta t_i/\sqrt{1 - p^{2}v_i^{2}}$, $p = \sin\theta/v$ | 1-D media; breaks down with lateral velocity change |
| Travel times from a reference model | use a TauP implementation with a named model such as a standard 1-D Earth model | the model is an input, so the output tests the *algorithm*, not the Earth |
| Array synthetics | sum plane waves across stations with a chosen slowness and back-azimuth | tests beamforming and f–k code, but with a perfectly coherent wavefield, which real data never are |

## 2. Potential fields

| Generator | Formula or recipe | Conditions and cautions |
|---|---|---|
| Buried prism | the closed-form gravity or magnetic response of a rectangular prism | the standard unit test for forward codes; check it against the point-mass limit at large distance |
| Sphere or point mass | $\Delta g_z = Gmz/(x^{2}+z^{2})^{3/2}$ | exactly the model it says it is — which makes it a *weak* test if your code only handles spheres |
| Layer of variable density | a 2-D grid of prisms, or the FFT of a density spectrum multiplied by the gravity kernel | the FFT route imposes periodic boundary conditions, which is a modelling choice, not a detail |
| Magnetic dipole ensemble | sum dipoles with chosen magnetisation, then subtract an IGRF-like reference field | tests reduction-to-pole and anomaly separation code, but the "anomaly" is defined by your choice of reference |
| Fractal (self-affine) surfaces | fractional Brownian motion with Hurst exponent $H$: spectrum $\propto k^{-(2H+1)}$ | realistic-looking topography; the exponent must be stated, because the amplitude at any wavelength depends on it |

## 3. Electromagnetic and electrical data

| Generator | Recipe | Conditions and cautions |
|---|---|---|
| 1-D MT response | compute the impedance of a stack of layers by recursion, then convert to $\rho_a$ and phase | validates the forward code; nothing about dimensionality or noise |
| DC resistivity pseudosection | forward-model a chosen resistivity model with your array geometry, then add noise and invert | the classic closed-loop test: can your inversion recover the model it was built for? |
| Transient EM decay | sum the modes of a conductive body, or use the leading time constant $\tau \approx \mu_0\sigma a^{2}/\pi^{2}$ for a sphere | the single-time-constant form is an approximation; validate against a published decay curve |
| GPR section | convolve a reflectivity series in permittivity with a Ricker wavelet, using $v = c/\sqrt{\varepsilon_r}$ | ignores attenuation and dispersion unless added explicitly |

## 4. Statistical and catalogue data

| Generator | Recipe | Conditions and cautions |
|---|---|---|
| Gaussian noise | `rng.normal(mu, sigma, n)` | independent samples; real geophysical noise is almost always correlated |
| Correlated noise | AR(1): $x_t = \phi x_{t-1} + \epsilon_t$ with $\lvert\phi\rvert < 1$ | the correlation length is set by $\phi$; state it, because it changes the effective sample size |
| Synthetic earthquake catalogue | sample magnitudes from $N \propto 10^{-bM}$ with a stated $b$ and completeness threshold, then place hypocentres along a chosen geometry | tests magnitude–frequency code; the seismicity is a *model*, and any "detected" clustering is put there by construction |
| Bootstrap resample | sample with replacement from the observed data | not a generator of new physics; it reproduces the observed empirical distribution, including its biases |
| Spatially correlated field | Gaussian random field with a chosen covariance function | the variogram you choose is the variogram you get; validating a kriging code with it is circular unless the covariance is also re-estimated |

## 5. Rules for using synthetic data honestly

| Rule | Reason |
|---|---|
| State the true model, its units and its discretisation | otherwise "recovered the model" is not a checkable claim |
| State the noise model and the seed | reproducibility; `numpy.random.default_rng(seed)` is the recommended API |
| Report the test as a validation of *code*, not of the Earth | a synthetic test cannot detect a modelling assumption that both the generator and the inversion share |
| Include a case the method is expected to fail | an inversion tested only on data that suit it has not been tested |
| Regenerate with a different seed and a different true model | sensitivity of the conclusion to a single lucky draw |
| Never mix synthetic and observed data in one figure without labelling | the commonest integrity failure in published figures |

## 6. Software for building synthetic data

| Tool | Access point | Role |
|---|---|---|
| NumPy random generators | [numpy.org generator reference](https://numpy.org/doc/stable/reference/random/generator.html) | The recommended `Generator` API for reproducible random draws |
| NumPy | [numpy.org](https://numpy.org) | Arrays, FFT, convolution, linear algebra |
| SciPy | [scipy.org](https://scipy.org), [SciPy documentation](https://docs.scipy.org/doc/scipy/) | Signal processing, integration, optimisation and statistics |
| ObsPy | [docs.obspy.org](https://docs.obspy.org) | Building and writing synthetic seismic streams in standard formats |
| ObsPy TauP | [obspy.taup](https://docs.obspy.org/packages/obspy.taup.html) | Travel times and ray paths for synthetic seismograms |
| TauP calculator and reference | [seis.sc.edu/taup/](https://seis.sc.edu/taup/) | Independent implementation for cross-checking travel times |
| Cartopy / PyGMT | [cartopy.readthedocs.io](https://cartopy.readthedocs.io), [pygmt.org](https://pygmt.org) | Plotting synthetic fields on real maps without confusing the two |
| Xarray / Zarr | [xarray.dev](https://xarray.dev), [zarr.readthedocs.io](https://zarr.readthedocs.io) | Storing large synthetic volumes with labelled coordinates |

## What synthetic data cannot tell you

- They cannot validate a physical assumption that the generator also makes.
- They cannot establish that a method will work on real data with correlated
  noise, uneven sampling and systematic errors.
- A recovered model that matches the input is evidence about the *algorithm*,
  and only at the resolution and noise level you chose.
- Resolution claims made on synthetic data are claims about the experiment you
  designed, not about the Earth.

## Related pages

- [Open Data: Seismology and Earthquake Catalogues](./01-datasets-seismology.md)
- [Open Data: Gravity, Magnetic and Geodetic](./02-datasets-potential-fields.md)
- [Formula Sheet: Inverse Theory and Statistics](../03-formula-handbook/06-formulas-inverse-statistics.md)
- [Formula Sheet: Waves, Elasticity and Seismology](../03-formula-handbook/03-formulas-waves-seismology.md)
- [19-numerical-modeling-hpc folder overview](../../19-numerical-modeling-hpc/README.md)
- [22-data-engineering-reproducibility folder overview](../../22-data-engineering-reproducibility/README.md)
