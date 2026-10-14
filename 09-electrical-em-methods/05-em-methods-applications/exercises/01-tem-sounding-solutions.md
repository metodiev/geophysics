# Solutions — 09-05-01 TEM Sounding for Aquifers and Mineral Targets

> **Read after attempting.** Lesson: [01 TEM Sounding](../01-tem-sounding.md).

---

## ★1 — Diffusion depths

$\mu_0\sigma = 4\pi\times10^{-7} \times 0.02 = 2.5133\times10^{-8}$
H S/m². Then $\delta = \sqrt{2t/2.5133\times10^{-8}}$:

- $t = 0.1$ ms $= 10^{-4}$ s: $\delta = \sqrt{2\times10^{-4}/2.5133\times10^{-8}}
  = \sqrt{7958} = 89.2$ m;
- $t = 1$ ms: $\delta = \sqrt{7.958\times10^{4}} = 282.1$ m;
- $t = 10$ ms: $\delta = \sqrt{7.958\times10^{5}} = 892.1$ m.

Each decade in time multiplies $\delta$ by $\sqrt{10} = 3.162$.

---

## ★2 — Time into frequency

$f = 1/(2\pi t) = 1/(2\pi\times10^{-3}) = 159.15$ Hz. The conversion is exact
because a diffusive system is described by $\exp(i\omega t - r/\delta)$ with
$\delta = \sqrt{2/(\omega\mu_0\sigma)}$: setting $\omega = 2\pi f$ makes the
frequency and the diffusion time two names for the same number. What is *not*
exact is the further step from $\delta$ to a depth of investigation.

---

## ★3 — Induction number

$$\theta = \frac{2\pi\times1000 \times 4\pi\times10^{-7} \times 0.01 \times 2500}{4}
= \frac{6283.19 \times 1.2566\times10^{-6}\times 25}{4} = 0.0493 .$$

From the measured error table ($0\%$ at $\theta = 0.01$, $-44\%$ at $0.1$), an
interpolation puts the LIN calibration error near $20\%$ at $\theta = 0.05$. **The
calibration does not apply**: the response must be compared with a forward model.

---

## ★4 — The limit and the channels

The measured limit is $H_s/H_p \to -i\theta$: in the low-induction-number regime
the imaginary (quadrature) part is **first order in conductivity** and the real
(in-phase) part is second order. Physically, the quadrature measures the energy
lost to induced currents in the ground, which is proportional to the ground's
conductance at the sensed depth; the in-phase measures the small flux expulsion,
which grows as the square of the conductance. Hence an FDEM or TEM interpretation
recovers conductivity from the quadrature, and the in-phase carries information
only where the ground is conductive enough for $\theta$ to approach unity.

---

## ★5 — Fitting the measured exponent

With $\ln\delta = (13.13, 12.98, 12.13, 11.98)$ roughly and
$\ln z_{50} = (3.875, 3.858, 3.749, 3.503)$ over the four entries,
a least-squares fit gives

$$p = \frac{\text{cov}(\ln\delta, \ln z_{50})}{\text{var}(\ln\delta)}
\approx 0.107,$$

matching the demonstration's printed value. The interpretation: over three decades
of frequency the median depth moves by a factor $1.45$ while $\delta$ moves by a
factor $31.6$. A survey's depth range is therefore far less frequency-dependent
than the diffusion depth suggests, and quoting $\delta$ as a depth overstates the
reach of a high-frequency window by roughly a factor $5$.

---

## ★6 — The equivalence

From the measured table the $4$ m/$0.5$ S/m model differs from the $2$ m/$1$ S/m
model by $2.19\%$ rms over $0.1$–$1000$ Hz, and the $20$ m/$0.1$ S/m model by
$17.27\%$. Against a $1\%$ noise level the $4$ m model is marginally
distinguishable ($2.2\sigma$ rms, but the difference is systematic rather than
random, so it is detectable in principle) and the $20$ m model is clearly
distinguishable. **A factor-two thickness change is at the edge of resolution at
$1\%$ noise; a factor-ten change is not.** This is the quantitative basis for the
"factor $2.4$ at $5\%$ noise" statement of the lesson.

---

## ★7 — Separating the family members (specification)

**Geometry.** Two offsets, $r = 20$ m and $r = 80$ m, both at the same
frequency band; the short offset samples the shallow section where the thin
conductor sits, the long offset integrates deeper and sees the thicker one.

**Statistic.** Fit both models to the two-offset dataset with a single added
parameter per model (the layer depth, and for the pair the thickness and
conductivity) and compare $\chi^{2}$. The models are separated when
$\Delta\chi^{2} > 9$ for the extra parameters, i.e. about $3\sigma$.

**Required noise.** The measured rms difference at one offset is $17.27\%$; with
two independent offsets the separation scales as $\sqrt{2}$, and a $3\sigma$
decision needs a per-offset noise of about $17.27/(3\sqrt{2}) = 4.1\%$ of the
response. So a $4\%$ response repeatability is the design target, which the
measured equivalence table converts into a thickness resolution of roughly a
factor $2.4$.

---

## ★8 — The plane-wave degeneracy

For a half-space, $u = \sqrt{\lambda^{2} + i\omega\mu_0\sigma}$. As
$\lambda \to 0$, $u \to \sqrt{i\omega\mu_0\sigma}$, a constant independent of
$\lambda$, so

$$R = \frac{u - \lambda}{u + \lambda} \to \frac{u}{u} = +1$$

with no frequency dependence at all (the limit is reached uniformly). Physically,
the air above a conductive earth presents an infinite impedance in the
quasi-static limit, so a wave at normal incidence is perfectly reflected
independently of $\omega$: the surface field simply doubles, at every frequency.
A plane-wave or "large loop" model therefore has **no transient response**,
because a transient is a statement about a frequency-dependent reflection. The
loop geometry and the offset $r$ are what carry the frequency dependence, and
that is why the kernel of this lesson retains both.
