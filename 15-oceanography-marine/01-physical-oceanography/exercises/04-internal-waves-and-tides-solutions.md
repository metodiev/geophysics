# Solutions — 15-01-04 Internal Waves, Tides and Mixing

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [04 Internal Waves and Tides](../04-internal-waves-and-tides.md).

Constants: $\Omega = 7.292115\times10^{-5}\ \mathrm{s^{-1}}$,
M2 period $12.4206\ \mathrm{h}$ so $\omega_{M2} = 1.4052\times10^{-4}\
\mathrm{rad\,s^{-1}}$.

---

## ★1 — Frequency for $k = m$

$$\omega^{2} = \frac{N^{2}k^{2} + f^{2}m^{2}}{k^{2}+m^{2}}$$

With $k = m$, the relation reduces to $\omega^{2} = (N^{2}+f^{2})/2$, so

$$\omega = \sqrt{\frac{(0.012)^{2} + (1.0\times10^{-4})^{2}}{2}}
= \sqrt{\frac{1.4400\times10^{-4} + 1.0\times10^{-8}}{2}}
= \sqrt{7.20005\times10^{-5}}$$

$$= 8.4856\times10^{-3}\ \mathrm{rad\,s^{-1}},
\qquad T = \frac{2\pi}{\omega} = 740.45\ \mathrm{s} = 12.34\ \mathrm{min}.$$

**Why the scale of $k$ does not matter.** When $k = m$ the two wavenumbers cancel
in the ratio, leaving only their *direction* ($\theta = 45^\circ$). The dispersion
relation depends on the direction of the wavevector, not its magnitude — the
defining property of internal waves discussed in Section 2.2 of the lesson. A
useful corollary: doubling both $k$ and $m$ changes the frequency not at all but
halves the wavelength and doubles the phase speed.

---

## ★2 — The frequency band at $20^\circ$N

Internal waves exist for $f < \omega < N$ (in the northern hemisphere; the lower
bound is $|f|$ in general).

$$f = 2\Omega\sin20^\circ = 2(7.292115\times10^{-5})(0.342020)
= 4.9882\times10^{-5}\ \mathrm{rad\,s^{-1}},$$
$$N = 8.0\times10^{-3}\ \mathrm{rad\,s^{-1}}.$$

In periods: the upper bound is $2\pi/N = 785.4\ \mathrm{s} = 13.09$ min; the
lower bound is $2\pi/f = 1.2596\times10^{5}\ \mathrm{s} = 35.0$ h. So the band
spans **13.1 minutes to 35.0 hours** — two and a half decades, and it narrows as
latitude increases.

---

## ★3 — Dimensional check of $s$

$$\left[\frac{\omega^{2}-f^{2}}{N^{2}-\omega^{2}}\right]
= \frac{\mathrm{s^{-2}}}{\mathrm{s^{-2}}} = \text{dimensionless},
\qquad [s] = 1. \ ✔$$

Both $f$ and $N$ are angular frequencies, so their squares are of the same kind
and may be subtracted and divided. The slope is an angle, hence dimensionless —
which is what allows it to be compared directly with a bathymetric gradient
$\mathrm{d}h/\mathrm{d}x$, also dimensionless.

---

## ★★4 — Mode-1 internal tide wavenumber

From $\omega^{2}(k^{2}+m^{2}) = N^{2}k^{2}+f^{2}m^{2}$,

$$k^{2}(\omega^{2}-N^{2}) = m^{2}(f^{2}-\omega^{2})
\;\Longrightarrow\;
\boxed{k^{2} = m^{2}\frac{\omega^{2}-f^{2}}{N^{2}-\omega^{2}} .}$$

Numerically, with $m = \pi/1000 = 3.1416\times10^{-3}\ \mathrm{m^{-1}}$:

$$\omega^{2} = 1.9746\times10^{-8}, \quad f^{2} = (1.0313\times10^{-4})^{2}
= 1.0636\times10^{-8},$$
$$N^{2} - \omega^{2} = 1.0000\times10^{-4} - 1.9746\times10^{-8}
= 9.9998\times10^{-5},$$
$$k^{2} = (9.8696\times10^{-6})\frac{9.1100\times10^{-9}}{9.9998\times10^{-5}}
= (9.8696\times10^{-6})(9.1102\times10^{-5}) = 8.9912\times10^{-10},$$

$$k = 2.9988\times10^{-5}\ \mathrm{m^{-1}}, \qquad
\lambda = \frac{2\pi}{k} = 2.0952\times10^{5}\ \mathrm{m} = 209.52\ \mathrm{km},$$

$$c = \frac{\omega}{k} = \frac{1.4052\times10^{-4}}{2.9988\times10^{-5}}
= 4.6859\ \mathrm{m\,s^{-1}} .$$

Without rotation, $c_{f=0} = NH/\pi = 3.1831\ \mathrm{m\,s^{-1}}$. The ratio is
$4.6859/3.1831 = 1.4721$.

**Origin of the factor.** The phase speed is
$c = (\omega H/\pi)\sqrt{(N^{2}-\omega^{2})/(\omega^{2}-f^{2})}$, and at fixed
$\omega$ the non-rotating value is $(H/\pi)\sqrt{N^{2}-\omega^{2}}$, so the ratio
is exactly

$$\frac{c}{c_{f=0}} = \frac{\omega}{\sqrt{\omega^{2}-f^{2}}}
= \frac{1}{\sqrt{1-(f/\omega)^{2}}}
= \frac{1}{\sqrt{1-(0.7339)^{2}}} = 1.4722 .$$

The small difference from the tabulated $1.4721$ is the $\omega^{2}/N^{2}$
correction in $\sqrt{N^{2}-\omega^{2}}$. A non-rotating internal tide is a
long-wave limit of the rotating one; rotation lengthens it by a factor that
depends only on the ratio $f/\omega$, and that factor diverges at the tidal
latitude cut-off.

---

## ★★5 — Criticality at two latitudes

$$s = \sqrt{\frac{\omega^{2}-f^{2}}{N^{2}-\omega^{2}}} .$$

**At $30^\circ$N**, $f = 7.2921\times10^{-5}$, $f^{2} = 5.3175\times10^{-9}$:

$$s = \sqrt{\frac{1.9746\times10^{-8} - 5.3175\times10^{-9}}
{(0.012)^{2} - 1.9746\times10^{-8}}}
= \sqrt{\frac{1.4429\times10^{-8}}{1.4398\times10^{-4}}}
= \sqrt{1.0021\times10^{-4}} = 1.0011\times10^{-2},$$

$$\gamma = \frac{8.0\times10^{-3}}{1.0011\times10^{-2}} = 0.799
\;\Rightarrow\; \text{near-critical, efficient generation.}$$

**At $15^\circ$N**, $f = 3.7747\times10^{-5}$, $f^{2} = 1.4248\times10^{-9}$:

$$s = \sqrt{\frac{1.9746\times10^{-8} - 1.4248\times10^{-9}}{1.4398\times10^{-4}}}
= \sqrt{1.2725\times10^{-4}} = 1.1281\times10^{-2},$$

$$\gamma = \frac{8.0\times10^{-3}}{1.1281\times10^{-2}} = 0.709 .$$

**Less critical at $15^\circ$N.** At lower latitude $f$ falls, the characteristic
slope grows (it is largest at the equator, $s = \omega/\sqrt{N^{2}-\omega^{2}} =
1.405\times10^{-2}$ for these values), and with $s$ in the denominator the
criticality falls. Both cases remain in the near-critical band, and the change is
a modest $11\,\%$ — which is the honest size of the effect. It becomes dramatic
only close to the cut-off, where $s\to0$ and everything is supercritical.

---

## ★★6 — Sensitivity of the inferred diffusivity

$K_\rho = \Gamma\epsilon/N^{2}$ with $\epsilon = 5.0\times10^{-9}\
\mathrm{W\,kg^{-1}}$.

**(a)** $N = 0.008$, $N^{2} = 6.40\times10^{-5}$:

$$\Gamma = 0.20: \quad K_\rho = \frac{0.20 \times 5.0\times10^{-9}}
{6.40\times10^{-5}} = 1.5625\times10^{-5}\ \mathrm{m^{2}\,s^{-1}},$$
$$\Gamma = 0.50: \quad K_\rho = \frac{0.50 \times 5.0\times10^{-9}}
{6.40\times10^{-5}} = 3.906\times10^{-5}\ \mathrm{m^{2}\,s^{-1}}.$$

**(b)** $\Gamma = 0.20$, $N = 0.016$, $N^{2} = 2.56\times10^{-4}$:

$$K_\rho = \frac{0.20 \times 5.0\times10^{-9}}{2.56\times10^{-4}}
= 3.906\times10^{-6}\ \mathrm{m^{2}\,s^{-1}} .$$

**(c)** The $\Gamma$ change ($0.20\to0.50$) moves the answer by a factor
$2.5$. The $N$ change (doubling) moves it by a factor $1/4 = 0.25$, i.e. a
factor **4** in the opposite direction. The $N$ error is therefore the larger of
the two — and it compounds with the $\Gamma$ error, since both multiply into the
same expression. With a $20\,\%$ $N$ error and a factor-2.5 $\Gamma$ range, an
inferred diffusivity can reasonably span a factor of 4 before any measurement
error is counted. That is the arithmetic behind the lesson's insistence that
$K_\rho$ is an inference, not a measurement.

---

## ★★7 — $\mathrm{Ri}$ at $z = 95$ m by hand

Central differences with a $20\ \mathrm{m}$ span:

$$U(105) = 0.60\tanh\!\left(\frac{105-100}{25}\right) = 0.60\tanh(0.20)
= 0.60(0.19738) = 0.11843\ \mathrm{m\,s^{-1}},$$

$$U(85) = 0.60\tanh\!\left(\frac{85-100}{25}\right) = 0.60\tanh(-0.60)
= 0.60(-0.53705) = -0.32223\ \mathrm{m\,s^{-1}},$$

$$\frac{\mathrm{d}U}{\mathrm{d}z} \approx \frac{0.11843 - (-0.32223)}{20}
= \frac{0.44066}{20} = 0.022033\ \mathrm{s^{-1}},$$

$$N(95) = 0.010 + 0.006\tanh\!\left(\frac{95-100}{20}\right)
= 0.010 + 0.006\tanh(-0.25) = 0.010 - 0.006(0.24492)
= 0.0085305\ \mathrm{s^{-1}},$$

$$\mathrm{Ri} = \frac{(0.0085305)^{2}}{(0.022033)^{2}}
= \frac{7.2769\times10^{-5}}{4.8544\times10^{-4}} = 0.1499 .$$

The demonstration's table gives $0.124$ at $z = 90$ m and $0.174$ at
$z = 100$ m, so a linear interpolation to $95$ m gives
$\sim0.149$ — agreement to three figures. The residual disagreement is the sign
of the interpolation's curvature: $\mathrm{Ri}$ has its minimum at $z = 89.3$ m,
so the function is not linear across this $20\ \mathrm{m}$ window and a
central-difference $\mathrm{d}U/\mathrm{d}z$ slightly *underestimates* the local
shear below the minimum.

**The practical lesson.** A $20\ \mathrm{m}$ difference window changes
$\mathrm{Ri}$ by $20\,\%$ here, and the instability criterion is
$\mathrm{Ri}<1/4$: a coarse difference can move a layer from "marginally
unstable" to "marginally stable". Resolution is part of the answer, not a
technicality.

---

## ★★★8 — A microstructure survey to a factor 2

**(a) Instrument.** A free-falling microstructure profiler measuring shear at
millimetre scales (for $\epsilon$) plus co-located conductivity, temperature and
pressure (for $N^{2}$). A single profiler carries both; using separate
instruments introduces a matching problem that costs more than it saves.

**(b) Sampling in space.** Profiles separated by a few kilometres, of order
$10^{2}$ profiles over a region a few hundred kilometres across, so that the
*mean* of $\epsilon$ over the population is estimated and not a single cast. The
required number follows from the variance: dissipation is log-normally
distributed, so the standard error of the mean of $\ln\epsilon$ falls as
$1/\sqrt{n}$; with a per-cast standard deviation of about $1$ in $\ln\epsilon$
(a common value), $n = 100$ casts give $\pm0.1$ in $\ln\epsilon$, i.e.
$\pm10\,\%$ — adequate.

**(c) Sampling in time.** Repeat the section at least twice, separated by more
than a tidal period (12.4 h), so that the tidal and inertial contributions are
sampled rather than aliased into a bias.

**(d) The quantity to average.** $\langle\epsilon/N^{2}\rangle$, not
$\langle\epsilon\rangle/\langle N^{2}\rangle$: the ratio is what enters the
Osborn relation and the two averages differ because $\epsilon$ and $N^{2}$ are
correlated. Also state whether the average is over depth, over profiles, or both,
and report it as a geometric mean if the distribution is log-normal.

**(e) Error budget.** Per-cast $\epsilon$ (a factor of about $2$ in a single
realisation), $N^{2}$ from unresolved fine structure (tens of per cent),
$\Gamma$ (a factor of $2.5$ across the defensible range), and the averaging
statistics ($\pm10\,\%$ if $n = 100$).

**(f) The dominant assumption.** $\Gamma$. It enters multiplicatively, its range
is a factor $2.5$, and — unlike the others — *no amount of additional profiling
reduces it*. That is the honest answer: the survey can be designed to control the
measurement error, and it cannot be designed to control the closure.

---

## ★★★9 — The tidal cut-off, and why an observation at $76^\circ$N is weak evidence

**Derivation.** A freely propagating internal tide requires the square root in
$s = \sqrt{(\omega^{2}-f^{2})/(N^{2}-\omega^{2})}$ to be real, i.e.
$\omega > f$. With $f = 2\Omega\sin\phi$:

$$\sin\phi = \frac{\omega_{M2}}{2\Omega}
= \frac{1.4052\times10^{-4}}{2(7.292115\times10^{-5})}
= \frac{1.4052\times10^{-4}}{1.458423\times10^{-4}} = 0.96351,$$

$$\phi = 74.47^\circ \approx 74.5^\circ .$$

So for $|\phi| > 74.5^\circ$ the dispersion relation has no real solution at the
M2 frequency and the tide is evanescent.

**Why absence of an observed M2 internal tide at $76^\circ$N is weak evidence.**

1. **Generation, not propagation, may be the reason.** The cut-off is a
   propagation limit. Even at $70^\circ$N, where propagation is permitted, a
   basin with no critical topographic slope nearby produces no internal tide —
   and conversely, a *near-local* generation site just equatorward of the
   observation latitude can pump energy into the evanescent region, which decays
   with distance but is still detectable close to the source. A null result
   therefore conflates "cannot propagate" with "was never generated locally".
2. **The horizon of the test is a few degrees, and the stratification is
   unknown.** The cut-off latitude depends only on $\omega$ and $\Omega$ and is
   sharp, but $76^\circ$N is only $1.5^\circ$ past it, and $N$ at those latitudes
   is weak and seasonally variable; $N$ appears in the vertical-mode structure
   and in the generation efficiency, so a low-$N$ column can suppress the signal
   for reasons that have nothing to do with the cut-off. Additional complications:
   the M2 frequency itself varies with the nodal cycle, the background flow
   Doppler-shifts $\omega$ by $-kU$, and an ice cover (typical at that latitude)
   prevents the surface signature from being observed at all.

A convincing test would compare the *decay with distance from a known generation
site* computed for an evanescent wave against the observed decay, at several
latitudes on both sides of $74.5^\circ$, with independent estimates of $N$ and of
the background flow. Absence alone does not carry the argument.
