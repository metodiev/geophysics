# Solutions — 06-05-02 Separating Scattering from Intrinsic Attenuation

The lesson is
[02 Separating Scattering from Intrinsic Attenuation](../02-scattering-vs-intrinsic.md).
All models are **SYNTHETIC**.

## ★ Foundational

**★1.** With $v = 3000\ \mathrm{m\,s^{-1}}$, $a = 500\ \mathrm{m}$:

$$f_c = \frac{v}{2\pi a} = \frac{3000}{2\pi \times 500} = \frac{3000}{3141.6}
= 0.9549\ \mathrm{Hz}.$$

$ka = 2\pi f a/v$, so $ka = 0.1047 f$ per hertz:

| $f$ (Hz) | $ka$ | regime |
|---|---|---|
| 0.1 | 0.0105 | Rayleigh ($ka \ll 1$) |
| 1.0 | 1.047 | transitional ($ka \approx 1$) |
| 10 | 10.47 | geometric ($ka \gg 1$) |

So $ka = 1$ at $0.955\ \mathrm{Hz}$, and the classification is genuinely
transitional only within a factor of about 3 of that frequency: Rayleigh
behaviour needs $ka \lesssim 0.3$ ($f \lesssim 0.29\ \mathrm{Hz}$) and geometric
behaviour needs $ka \gtrsim 3$ ($f \gtrsim 2.9\ \mathrm{Hz}$). A band such as
$[3, 15]\ \mathrm{Hz}$ sits entirely in the geometric regime, which is why the
demonstration's two-band test sees little curvature *within* it.

**★2.**
$$Q_{\text{app}} = \frac{\pi L}{v m} = \frac{\pi \times 10^{4}}{3500 \times 0.05}
= \frac{31415.9}{175} = 179.5,$$
$$\alpha(5\ \mathrm{Hz}) = \frac{\pi f}{Q v}
= \frac{3.141593 \times 5}{179.5 \times 3500} = \frac{15.708}{6.2825\times10^{5}}
= 2.500\times10^{-5}\ \mathrm{m^{-1}} .$$

Unit cancellation: $\pi f t^{*}$ must be dimensionless, and
$t^{*} = m/\pi$ has units of the slope's inverse frequency scale, i.e.
$\mathrm{s}$, since $m f$ is dimensionless. Then $\alpha = \pi f/(Qv)$ is
$\mathrm{s^{-1}}/(\mathrm{m\,s^{-1}}) = \mathrm{m^{-1}}$, as required.

**★3.** $Q_{\text{meas}}$ **is** $Q_{\text{app}}$; there is no separate
"measured" quantity beyond the apparent one.
$$Q_{\text{app}} = \frac{1}{0.020} = 50, \qquad
\frac{1}{Q_{\text{int}}} = 0.020 - 0.005 = 0.015 \Rightarrow Q_{\text{int}} =
66.7 .$$
The inequality that must always hold is $Q_{\text{app}} \le Q_{\text{int}}$
(here $50 \le 66.7$). A small measured $Q$ proves that coherent energy is leaving
the direct arrival; it does **not** prove that the energy became heat, because
scattering moves it to the coda while conserving total energy.

## ★★ Applied

**★★4.** Write the coherent amplitude as the product of an intrinsic and a
scattering factor, $A = A_0\exp(-\alpha_{\text{int}}x)\exp(-\alpha_{\text{scat}}x)
= A_0\exp(-(\alpha_{\text{int}}+\alpha_{\text{scat}})x)$ — this *is* the
assumption: the two mechanisms are independent, so the losses multiply. With the
definition $\alpha = \pi f/(Qv)$ at the same $f$ and $v$,

$$\frac{1}{Q_{\text{app}}} = \frac{\alpha_{\text{app}}v}{\pi f}
= \frac{\alpha_{\text{int}}v}{\pi f} + \frac{\alpha_{\text{scat}}v}{\pi f}
= \frac{1}{Q_{\text{int}}} + \frac{1}{Q_{\text{scat}}} .$$

Numerical check with the demonstration's values:
$$Q_{\text{int}} = 100 \Rightarrow 1/Q_{\text{int}} = 0.010000, \qquad
1/Q_{\text{scat}} = 0.0077476,$$
$$1/Q_{\text{int}} + 1/Q_{\text{scat}} = 0.0177476,$$
$$\text{measured } 1/Q_{\text{meas}} = 0.018167,$$
$$\frac{0.018167 - 0.0177476}{0.0177476} = \frac{4.194\times10^{-4}}
{1.77476\times10^{-2}} = +2.36\%,$$
which reproduces the demonstration's table entry exactly. The same computation
for the $Q_{\text{int}} = 20$ row gives $0.059756$ against $0.057748$, i.e.
$+3.48\%$: the rule degrades as the total loss grows, which is the stated regime
of validity (a few per cent up to roughly $30\%$ total loss over the path).

**★★5.** **(a)** Ratio $= 240/120 = 2.00$. Propagating independent relative
errors: $\sigma_{\text{ratio}}/\text{ratio} =
\sqrt{(\sigma_{240}/240)^{2} + (\sigma_{120}/120)^{2}} =
\sqrt{(0.0375)^{2} + (0.0667)^{2}} = \sqrt{0.001406 + 0.004449} = 0.07649$, so
the ratio is $2.00 \pm 0.15$.

**(b)** Yes. The ratio differs from 1 by $1.00/0.15 = 6.7$ standard errors.

**(c)** The apparent $Q$ is larger in the lower band, i.e. $1/Q$ is larger at
high frequency — the signature of a loss that grows with frequency, which is the
scattering signature (the low-frequency half of a band stretching toward the
Rayleigh $f^{4}$ regime gives a *larger* apparent $Q$ than the high-frequency
half, as the demonstration measures: 215.6 versus 110.6, ratio 1.95). A purely
intrinsic attenuator with frequency-independent $Q$ would give a ratio of
exactly $1.00$ and a ratio error near zero (the demonstration's uniform anelastic
stack returns 100.00 in both bands).

**(d)** An intrinsic relaxation peak inside the analysis band also produces a
ratio away from 1 (the $1/Q(f)$ curvature of
[lesson 01](../01-attenuation-measurement.md) §6), and a scattering medium whose
band lies entirely within one regime can produce a ratio near 1 — so the test
detects *a frequency dependence*, and attributing it to scattering versus a
relaxation needs a wider band or a coda measurement.

**★★6.** Relative standard error:
$$4.670219\times10^{-4} / 7.751223\times10^{-3} = 6.03\%.$$
Since the standard error of a mean falls as $1/\sqrt{N}$,
$$N = 667 \times \left(\frac{6.03}{1}\right)^{2} = 667 \times 36.4 = 2.43\times10^{4}$$
realisations for $1\%$, and $667 \times (6.03/2)^{2} = 667 \times 9.09 =
6.07\times10^{3}$ for $2\%$.

For a **real** structure this is not available: realisations would mean genuinely
different Earths with the same statistics, and one Earth is what we have. A single
path's apparent $Q$ is therefore not an estimate of a population value; it is a
measured number whose "error bar" from the fit understates the structural
uncertainty. This is the reason scattering $Q$ values are usually *modelled* for a
stated statistical description of the medium, and the reason the two-band
frequency test (a shape test, not an amplitude test) is the more robust
diagnostic.

## ★★★ Research-oriented

**★★★7.** **Design.**

1. **Two-band frequency test** (direct arrivals). Band the regional S or coda-free
   P arrivals into $[0.5, 2]\ \mathrm{Hz}$ and $[2, 8]\ \mathrm{Hz}$; metric: the
   ratio of fitted apparent $Q$ in the two bands, with the standard error
   propagated from the fits. Expected signature: intrinsic $\Rightarrow$ ratio
   $\approx 1$ within errors, unless a relaxation peak lies inside a band;
   scattering $\Rightarrow$ ratio $> 1$ systematically, with the low band giving
   the larger apparent $Q$ only if the pair of bands straddles the Rayleigh-to-
   geometric transition. (Careful: the sign depends on where the bands sit
   relative to $f_c$ — this is the failure mode to state before starting.)
2. **Coda-versus-direct comparison.** Metric: $1/Q_{\text{app}}$ from direct
   arrivals minus $1/Q_{\text{coda}}$ from a fixed coda window, for the same ray.
   Expected signature: intrinsic-dominated $\Rightarrow$ the difference is small
   (the coda samples the same material and decays with $Q_{\text{int}}$);
   scattering-dominated $\Rightarrow$ the difference is a large fraction of
   $1/Q_{\text{app}}$. Assumption to state: single scattering and a coda window
   free of depth phases.
3. **Spatial coherence** on the 30-station array. Metric: the frequency-dependent
   decorrelation length of the direct arrival across nearby station pairs
   ($< 5\ \mathrm{km}$). Expected signature: scattering decorrelates the field
   over a length set by $a$, so coherence falls with station separation at fixed
   amplitude; intrinsic attenuation does not change coherence.

**What counts as evidence for intrinsic attenuation:** a self-consistent set in
which (i) the two-band ratio is unity or explained by a relaxation whose
parameters also predict the measured dispersion, (ii) the coda and direct
measurements agree within their errors, and (iii) coherence is preserved across
$\gtrsim a$ separations. **What counts as failure to separate:** a large
discrepancy between coda and direct $Q$, a two-band ratio far from 1 that cannot
be fitted by a relaxation, or a coherence length inconsistent with the assumed
$a$ — in any of these cases the only honest report is
$Q_{\text{app}}$ with its band, plus the bound $Q_{\text{app}} \le Q_{\text{int}}$.

**★★★8.** **Construction.** Model A: an intrinsic medium with
$1/Q_{\text{int}} = 1/150$ independent of frequency within the band. Model B: an
elastic random medium, $Q_{\text{int}} = \infty$, whose heterogeneity produces
$\alpha_{\text{scat}}(f)$ that happens to fit a straight line in $f$ over
$[2, 8]\ \mathrm{Hz}$ with $\alpha_{\text{scat}} = \pi f/(150v)$. Both give the
same $m = \pi \Delta x t^{*}$ over that band, so the fitted slope — and hence
$Q_{\text{app}} = 150$ — is identical. The demonstration does this explicitly in
the opposite direction: it computes the second type of medium and measures
$Q_{\text{app}} = 129.07$ where the truth is $Q_{\text{int}} = \infty$, and it
shows in §5 that any $Q_{\text{scat}} \ge Q_{\text{app}}$ can be combined with
the corresponding $1/Q_{\text{int}}$ to fit the same data.

**Why a wider band separates them.** The two models differ in the frequency
dependence *outside* the fitted band, and the difference is organised by $ka$:

| regime | intrinsic (single relaxation) | scattering |
|---|---|---|
| $ka \ll 1$ (Rayleigh) | $1/Q$ tends to a constant far below the peak, and *falls* above it | $1/Q \propto f^{4}$ (steep rise with $f$) |
| $ka \gg 1$ (geometric) | $1/Q$ constant (plateau) | $1/Q \approx$ constant, $\alpha \approx 1/(2a)$, set by $a$ |

So extending to $[0.5, 30]\ \mathrm{Hz}$ exposes the Rayleigh $f^{4}$ turn-on if
the heterogeneity is small-scale, and the plateau level in the geometric regime
gives an independent handle on $a$ through $\alpha = 1/(2a)$ — which the intrinsic
model has no way to fake, because its plateau level is fixed by material
properties, not by a length scale. The honest caveat is that the extrapolation is
only as good as the assumed statistical model of the heterogeneity.
