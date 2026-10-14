# Solutions — 10-05-03 Thermal Methods for Shallow Subsurface Investigation

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Periods: $P_{\text{day}} = 86400\ \mathrm{s}$,
> $P_{\text{year}} = 365.25(86400) = 3.1558\times10^{7}\ \mathrm{s}$.

Lesson: [03 Thermal Methods](../03-thermal-nearsurface.md).

---

## ★1 — Granite diffusivity and annual depth

$$\kappa = \frac{k}{\rho c} = \frac{2.50}{2650\times790}
= \frac{2.50}{2.0935\times10^{6}} = 1.194\times10^{-6}\ \mathrm{m^2\,s^{-1}},$$

$$\omega_{\text{year}} = \frac{2\pi}{3.1558\times10^{7}}
= 1.9911\times10^{-7}\ \mathrm{rad\,s^{-1}},$$

$$\mu = \sqrt{\frac{2(1.194\times10^{-6})}{1.9911\times10^{-7}}}
= \sqrt{11.994} = 3.463\ \mathrm{m}.$$

The demonstration prints $\kappa = 1.194\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ and
$\mu_{\text{annual}} = 3.463\ \mathrm{m}$ for the same material. Note that granite
is dry and conductive; its diffusivity is $4.8$ times that of dry soil.

---

## ★2 — The 1% depth for the daily wave

The amplitude at depth is $A e^{-z/\mu}$, so $A(z)/A = 0.01$ requires

$$z = \mu\ln(100) = 4.60517\,\mu, \qquad
\mu = \sqrt{\frac{\kappa P}{\pi}} = \sqrt{\frac{(2.50\times10^{-7})(86400)}{\pi}}
= 0.08292\ \mathrm{m},$$

$$z = 4.60517(0.08292) = 0.3819\ \mathrm{m}.$$

The general expression is $z_{f} = \mu\ln(1/f)$ for a fraction $f$; the factor
$4.605$ is $\ln 100$. Below about $0.4\ \mathrm{m}$ in dry soil the daily cycle is
under 1% of the surface amplitude, and in granite (from ★1,
$\mu_{\text{day}} = 0.1812\ \mathrm{m}$) the same fraction needs
$0.83\ \mathrm{m}$.

---

## ★3 — Units

| Quantity | Unit | Why |
|---|---|---|
| $k$ | $\mathrm{W\,m^{-1}\,K^{-1}}$ | $\mathbf q = -k\nabla T$ |
| $\rho c$ | $\mathrm{J\,m^{-3}\,K^{-1}}$ | energy per volume per kelvin |
| $\kappa = k/(\rho c)$ | $\mathrm{m^2\,s^{-1}}$ | $\mathrm{(W\,m^{-1}K^{-1})/(J\,m^{-3}K^{-1})}$ |
| $e = \sqrt{k\rho c}$ | $\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}$ | $\sqrt{\mathrm{W\,m^{-1}K^{-1}}\cdot\mathrm{J\,m^{-3}K^{-1}}}$ |

For $\mu$: $\kappa$ is $\mathrm{m^2\,s^{-1}}$ and $\omega$ is
$\mathrm{rad\,s^{-1}}$ (dimensionless per second), so $2\kappa/\omega$ is
$\mathrm{m^{2}}$ and its square root is $\mathrm{m}$ ✔.

---

## ★★4 — Annual record, both estimators

$$d = 2.5-0.5 = 2.0\ \mathrm{m}, \qquad
\omega = 1.9911\times10^{-7}\ \mathrm{rad\,s^{-1}},$$
$$\ln\frac{A_1}{A_2} = \ln 3 = 1.09861, \qquad
\Delta\phi = \omega(45\times86400) = 0.77414\ \mathrm{rad},$$

$$\kappa_{\text{amp}} = \frac{\omega d^2}{2(\ln A_1/A_2)^2}
= \frac{(1.9911\times10^{-7})(4)}{2(1.09861)^2} = 3.299\times10^{-7}
\ \mathrm{m^2\,s^{-1}},$$
$$\kappa_{\text{ph}} = \frac{\omega d^2}{2(\Delta\phi)^2}
= \frac{(1.9911\times10^{-7})(4)}{2(0.77414)^2} = 6.645\times10^{-7}
\ \mathrm{m^2\,s^{-1}}.$$

The ratio is $2.01$. **A $0.05\ \mathrm{K}$ sensor error cannot explain this.**
Applying the uncertainty formula with, say, $A_1 = 6.0$ and $A_2 = 2.0$:

$$\frac{\sigma_\kappa}{\kappa}\bigg|_{\text{amp}} =
\frac{2}{1.09861}\sqrt{\left(\frac{0.05}{6.0}\right)^2+
\left(\frac{0.05}{2.0}\right)^2} = 4.74\%,$$

so the two estimates differ by 100% against a fractional uncertainty of about 5%
— a twenty-sigma discrepancy. The correct conclusion is that the assumption of a
homogeneous conductor fails between $0.5$ and $2.5\ \mathrm{m}$: the conductivity
or the diffusivity varies with depth (a moisture profile, a soil horizon, a
lithological boundary). The next step is a two-layer model, not an average.

---

## ★★5 — Probe slope and validity window

$$\text{slope} = \frac{T(200)-T(50)}{\ln(200/50)} = \frac{0.3324-0.2412}{1.38629}
= 0.065779\ \mathrm{K},$$

$$k = \frac{q}{4\pi\,\text{slope}} = \frac{1.00}{4\pi(0.065779)}
= 1.210\ \mathrm{W\,m^{-1}\,K^{-1}}.$$

The true value behind the synthetic numbers is $1.20$, so the slope method
over-estimates by $+0.8\%$ even when the two temperatures are exact — the residual
of the logarithmic approximation.

**Validity window.** The approximation requires $x = r^2/(4\kappa t) \ll 1$.
Solving for the 1% error with $r = 1.5\ \mathrm{mm}$ and
$\kappa = 7.50\times10^{-7}\ \mathrm{m^2\,s^{-1}}$ gives $t = 25.12\ \mathrm{s}$,
at which $x = 0.0299$. So the first usable measurement is about
$25\ \mathrm{s}$ after switch-on; at $1\ \mathrm{s}$ the approximation is wrong by
$185\%$ and even has the wrong sign (the exact $E_1$ is small but positive while
$\ln(4\kappa t/r^2)-\gamma$ is still negative). Fitting a straight line to the
first few seconds returns a conductivity that is too high.

---

## ★★6 — Averaging cycles

Uncertainty scales as $1/\sqrt{N}$ for independent measurements of the same
quantity, so

$$N = \left(\frac{5.9}{2.0}\right)^2 = 8.7 \;\Rightarrow\; N = 9
\text{ cycles}.$$

**Assumption.** That the noise on each cycle's amplitude and phase estimate is
independent and zero-mean. That fails when the error is not random but systematic:
a slowly drifting sensor offset, an air gap that closes as the soil wets, or a
seasonal change of the true amplitude. Averaging nine cycles of a drifting record
reduces the random part and leaves the bias untouched, and the reported
uncertainty then understates the true error. The check is to compute the
uncertainty of the *mean* from the scatter of the individual cycles rather than
from the single-cycle noise.

---

## ★★★7 — Separating geothermal flux from the annual wave (specification)

**Sensors.** At least five depths spanning $0.5$–$30\ \mathrm{m}$, with spacing
increasing with depth (the annual wave is resolvable only in the top few metres),
and one shallow sensor for the surface forcing. Each sensor's calibration and
depth must be known to better than the effect being measured: for a typical
gradient of $25\ \mathrm{K\,km^{-1}}$, $30\ \mathrm{m}$ spans $0.75\ \mathrm{K}$, so
$0.05\ \mathrm{K}$ sensors and $0.2\ \mathrm{m}$ depth accuracy are adequate.

**Record length.** At least two full annual cycles, ideally three, so that the
annual amplitude and phase are determined rather than assumed.

**Model.** $T(z,t) = T_0 + \Gamma z + A e^{-z/\mu}\cos(\omega t - z/\mu)$, with
$\Gamma$ the geothermal gradient, $A$, $\mu$ and $T_0$ unknown; fit
$\Gamma$, $A$ and $\mu$ jointly, because fitting the gradient to a seasonal
average biases it (the annual wave is not zero-mean over a partial year).

**Metric.** The fitted $\Gamma$ with its formal uncertainty and the residual
pattern versus depth. A residual that oscillates in depth with the annual
wavelength means the model has absorbed a real layering into $\mu$.

**Control.** A *synthetic* recovery: generate a profile with a known $\Gamma$,
$A$ and $\mu$, sample it at the planned depths and times, and confirm that the
pipeline recovers $\Gamma$ within the stated uncertainty. If it does not, the
plan — not the geology — is at fault.

**Falsification.** The prediction "the annual wave is negligible below
$3\mu$" is falsified if the fitted $\Gamma$ changes by more than its uncertainty
when the shallowest two sensors are dropped from the fit. That is a direct test
of whether the geothermal signal has been separated from the surface forcing.

---

## ★★★8 — Detecting a buried object from surface temperature (specification)

**Forcing.** Natural diurnal solar forcing, with the surface heat flux measured
(at least the net radiometer flux), because the anomaly is proportional to the
flux and the model needs a known input.

**Observable.** The surface temperature field (or the shallow temperature at
$0.05\ \mathrm{m}$) sampled as an image at several times through the diurnal
cycle, with the same instrument and geometry each time.

**Model and metric.** A two-layer (or buried-inclusion) thermal model with the
object's effusivity and depth as parameters; the metric is the *contrast* between
the object's trace and a neighbouring background trace, normalised by the
background spatial standard deviation, evaluated at the time of flux reversal.
Reporting an absolute temperature difference without that normalisation makes the
result incomparable between days.

**Strongest confounder.** Spatial variation of the soil itself — moisture patches,
vegetation, litter, slope and shading produce contrasts of the same order as a
shallow buried object. The control is a repeat survey after a rain event: a real
object keeps its position and shape, while a moisture patch moves and fades.

**Abandon criterion.** If the object contrast at the flux reversal is below the
background spatial standard deviation on *two different days with different
moisture states*, the method cannot deliver the object and a different method
(GPR, EMI or a pit) should be used. Thermal detection is a *screening* tool, and
the honest deliverable is a ranked set of leads with their false-alarm rate.
