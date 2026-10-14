# Solutions — 08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [02 Time-Domain EM (TDEM)](../02-time-domain-em.md).

---

## ★1 — Constants of a synthetic body

$$D=\frac{1}{\mu_0\sigma}=\frac{1}{1.2566\times10^{-6}\times0.02}
=3.9789\times10^{7}\ \mathrm{m^2\,s^{-1}},$$

$$\tau_1=\frac{\mu_0\sigma d^2}{\pi^2}
=\frac{1.2566\times10^{-6}\times0.02\times900}{9.8696}
=\frac{2.2619\times10^{-5}}{9.8696}
=2.2918\ \mathrm{\mu s},$$

$$\tau_2=\frac{\tau_1}{4}=0.5730\ \mathrm{\mu s},\qquad
\sqrt{Dt}=\sqrt{3.9789\times10^{7}\times10^{-3}}
=\sqrt{3.9789\times10^{4}}=199.47\ \mathrm{m}.$$

**Units:** $\mu_0\sigma d^2$ is
$\mathrm{H\,m^{-1}}\cdot\mathrm{S\,m^{-1}}\cdot\mathrm{m^2}
=\mathrm{s}$; $\sqrt{Dt}=\sqrt{\mathrm{m^2\,s^{-1}}\cdot\mathrm{s}}=\mathrm{m}$.
The second mode is four times faster, which is why a late-time slope sees only
$\tau_1$.

---

## ★2 — Dimensional analysis

$\mu_0\sigma d^2$: with $\mathrm{S}=\mathrm{A^2\,s^3\,kg^{-1}\,m^{-2}}$ and
$\mathrm{H}=\mathrm{kg\,m^2\,s^{-2}\,A^{-2}}$,
$\mathrm{H\,m^{-1}}\cdot\mathrm{S\,m^{-1}}=\mathrm{s^2\,m^{-2}}$, so multiplying
by $d^2$ gives $\mathrm{s^2}$ — a time squared, hence
$\sqrt{\mu_0\sigma}\,d$ is a time and $\mu_0\sigma d^2$ is a time. ✔

$\sqrt{Dt}$: $D=\mathrm{m^2\,s^{-1}}$, times $\mathrm{s}$, square-root →
$\mathrm{m}$. ✔

$\sigma d$ has units $\mathrm{S\,m^{-1}}\cdot\mathrm{m}=\mathrm{S}$ — a
**conductance** (siemens), the sheet conductance of a layer. It is the quantity
that controls the flux a slab can remove, and therefore the early-time amplitude.

---

## ★3 — Can the system see it?

$$\tau_1=\frac{1.2566\times10^{-6}\times0.05\times(200)^2}{9.8696}
=\frac{2.5132\times10^{-3}}{9.8696}=2.546\times10^{-4}\ \mathrm{s}
=254.6\ \mathrm{\mu s}.$$

The first usable channel is $50\ \mathrm{\mu s}=0.196\,\tau_1$, so the system sees
the body from a fifth of its decay constant onward — comfortably inside the
window, and the late-time slope would be well determined if the record extends to
a few $\tau_1$ (hundreds of microseconds). The lesson's $8.5\tau_1$ noise-limited
window is $2.2\ \mathrm{ms}$, far longer than the record needs.

The general rule this illustrates: **a larger body has a longer decay constant**
because $\tau\propto d^2$, so the timing window of a system must be matched to the
product $\sigma d^2$, not to $\sigma$ alone.

---

## ★4 — Separation of variables

Diffusion equation for $B(z,t)$ with $B=1$ at $t=0$:

$$\frac{\partial B}{\partial t}=D\frac{\partial^2B}{\partial z^2},
\qquad B(0,t)=B(d,t)=0.$$

Substituting $B=Z(z)T(t)$:

$$\frac{T'}{DT}=-\frac{Z''}{Z}=\frac{1}{\tau}\ (\text{constant}),$$

so $T=e^{-t/\tau}$ and $Z''=-\frac{1}{D\tau}Z$, i.e.
$Z=\sin(k z)$ with $k^2=1/(D\tau)$, and the boundary conditions force
$k_n=n\pi/d$, $n=1,2,\dots$ Hence

$$\tau_n=\frac{1}{Dk_n^2}=\frac{1}{D}\left(\frac{d}{n\pi}\right)^2
=\frac{\mu_0\sigma d^2}{n^2\pi^2}.$$

The initial condition enters only through the amplitudes: with $B(z,0)=1$,

$$1=\sum_n a_n\sin\frac{n\pi z}{d},\qquad
a_n=\frac{2}{d}\int_0^d\sin\frac{n\pi z}{d}\,\mathrm{d}z
=\frac{4}{n\pi}\ (n\ \text{odd}),\ 0\ (n\ \text{even}).$$

**The step's flat initial condition is why the amplitudes fall as $1/n$ and why
many modes must be summed to represent early times.** Once $t\gtrsim0.5\tau_1$ the
$n=3$ term is down by $e^{-8}\approx3\times10^{-4}$, and the record is a single
exponential.

---

## ★5 — What a decay constant determines

**(a)** $\sigma d^2 = \pi^2\tau/\mu_0
= 9.8696\times2.0\times10^{-6}/1.2566\times10^{-6} = 15.708\ \mathrm{S\,m}$.

**(b)** Combining with $\sigma d=0.20\ \mathrm{S}$:

$$d=\frac{\sigma d^2}{\sigma d}=\frac{15.708}{0.20}=78.5\ \mathrm{m},\qquad
\sigma=\frac{\sigma d}{d}=\frac{0.20}{78.5}=2.55\times10^{-3}\ \mathrm{S\,m^{-1}}.$$

**(c)** A late-time-only interpretation could have said
$\sigma d^2=15.7\ \mathrm{S\,m}$ and nothing more: every $(d,\sigma)$ on the
hyperbola $\sigma=15.7/d^2$ fits the decay equally well, and the conductances of
those models range over a factor of 16 or more.

---

## ★6 — Attributing the $0.13\%$

The mechanisms available are the spatial discretisation, the time discretisation
and the switch-off initial condition. The lesson's convergence table settles it:

| $N$ | measured vs continuum ratio |
|---|---|
| 16 | $1.06235$ |
| 32 | $1.06235$ (step-IC fit, $0.99887$ of the discrete eigenvalue) |

More usefully, the discrete eigenvalue at $N=32$ is $+0.0804\%$ from the
continuum, and the kink error at $t=0.2\tau_1$ with $32$ cells is
$2.99\times10^{-3}$ of the peak. The measured late-time value $0.5087$ sits
$0.13\%$ **below** the continuum value while the discrete eigenvalue sits
$0.08\%$ **above** it, so the dominant contributor is the time-stepping error of
the explicit scheme: at $\lambda=0.4$ with $dt\propto dz^2$, a factor-of-four
reduction of $dt$ reduces that error fourfold (measured: $1.9\times10^{-3}$ →
$4.8\times10^{-4}$). **The $0.13\%$ is numerical, and it is smaller than the
model error from an unknown thickness by more than two orders of magnitude**
(a $10\%$ thickness error gives $20\%$ in $\sigma$).

---

## ★7 — Two-channel experiment specification

**Target.** $\sigma$ and $d$ for a conductor with $d\in[20,50]\ \mathrm{m}$ and
$\sigma\approx0.01\ \mathrm{S\,m^{-1}}$, noise $1\times10^{-4}$ of the early
amplitude.

**Predicted decay constants.** $\tau_1=\mu_0\sigma d^2/\pi^2$:
$d=20\ \mathrm{m}\to0.5093\ \mathrm{\mu s}$;
$d=50\ \mathrm{m}\to3.183\ \mathrm{\mu s}$ (computed as
$1.2566\times10^{-6}\times0.01\times2500/9.8696$).

**Timing.** The transmitter must produce a stable current and switch off in a
time short compared with $\tau_1$; for a $0.5\ \mathrm{\mu s}$ decay constant
that demands a sub-microsecond ramp and a receiver with a bandwidth above about
$1\ \mathrm{MHz}$. This is the practical constraint that makes the smallest
targets hard: **the system's own timing must be matched to the smallest $\tau$ you
intend to resolve.**

**Channels.** Two fits, not a single global fit: (i) an early-amplitude fit over
$0.03$–$0.2\tau_1$, calibrated against the transmitter moment, giving $\sigma d$;
(ii) a late slope over $2.5$–$4\tau_1$, giving $\sigma d^2$. Inverting the pair:

$$d=\frac{\sigma d^2}{\sigma d},\qquad \sigma=\frac{(\sigma d)^2}{\sigma d^2}.$$

**Uncertainty.** With a $0.02\%$ noise-driven error on $\tau$ (the lesson's
Monte-Carlo figure) the statistical error on $\sigma d^2$ is $0.04\%$ — utterly
negligible. The dominant errors are systematic: (1) the early-amplitude
calibration (transmitter moment, receiver gain, geometry) enters $\sigma d$ — and
hence $d$ linearly and $\sigma$ quadratically; (2) self-induction at early times
biases the amplitude fit; (3) the slab model itself.

**Prediction and honest conclusion.** The experiment will return $\sigma d^2$ to
better than $1\%$ and $\sigma d$ to whatever the amplitude calibration is good
for (rarely better than $10\%$). The derived $d$ therefore carries a $\gtrsim10\%$
error and $\sigma\gtrsim20\%$. **The measurement is a conductance–depth
determination, not a conductivity determination,** and the specification is only
honest if it says so.

---

## ★8 — Can the ring depth differ by more than a factor of order unity?

A scaling argument. The only length in the problem is built from $D$ and $t$:
$L=c\sqrt{Dt}$ for some dimensionless $c$; there is no other combination with the
dimensions of length (the source's own length scale, the loop radius, enters only
as a prefactor in the amplitude, not in the depth law, provided the loop is small
compared with the diffusion length). Therefore

- the similarity solution's half-decay depth has $c=0.9539$;
- the "ring" depth quoted as $\sqrt{2t/(\mu_0\sigma)}=\sqrt{2Dt}$ has
  $c=\sqrt2=1.414$;
- the diffusion length $\sqrt{Dt}$ has $c=1$.

All three differ by **less than a factor of 1.5**, and no scaling argument can
make them differ by more: they are the only candidates, and each is $O(1)\times
\sqrt{Dt}$. Whether the true current maximum in a 3-D loop-over-halfspace
geometry sits at $c=1.0$ or $c=1.4$ is a question that requires the actual 3-D
solution (see [08-05-03](../03-em-modelling.md)); it cannot be settled by dimensional
analysis. **What dimensional analysis does settle is that the depth of the
induction maximum grows as $\sqrt{t}$ in every one of these conventions**, which is
the transferable statement. The measurement that would settle the coefficient is a
3-D forward model of the loop geometry compared, channel by channel, with the
record's amplitude — not the decay time alone, which is insensitive to $c$.
