# Solutions — 08-01-05 The Geodynamo: Mechanism and Evidence

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [05 The Geodynamo: Mechanism and Evidence](../05-dynamo-theory.md).

---

## ★1 — Magnetic diffusivity

$$\eta = \frac{1}{\mu_0\sigma}
= \frac{1}{4\pi\times10^{-7}\times1.0\times10^{6}}
= \frac{1}{1.256637\times10^{-1}} = 0.79577\ \mathrm{m^{2}\,s^{-1}}.$$

**Unit check.** $\left[\mu_0\sigma\right] =
\mathrm{H\,m^{-1}\cdot S\,m^{-1}}$. Since
$1\ \mathrm{H} = 1\ \mathrm{V\,s\,A^{-1}}$ and
$1\ \mathrm{S} = 1\ \mathrm{A\,V^{-1}}$, the product is
$\mathrm{s\,m^{-2}}$, so $\eta$ is $\mathrm{m^{2}\,s^{-1}}$ — a diffusivity, as
required.

---

## ★2 — Diffusion and free-decay times

$$\tau_{\text{diff}} = \frac{L^{2}}{\eta}
= \frac{(1.0\times10^{6})^{2}}{0.79577}
= 1.25664\times10^{12}\ \mathrm{s}
= \frac{1.25664\times10^{12}}{3.1557\times10^{7}} = 3.9821\times10^{4}\ \mathrm{yr}.$$

$$\tau_{\text{free}} = \frac{L^{2}}{2\eta} = \frac{\tau_{\text{diff}}}{2}
= 1.9910\times10^{4}\ \mathrm{yr}.$$

Compare with the lesson's parameters ($\sigma = 5\times10^{5}$,
$L = 2.1\times10^{6}$): there $\eta = 1.5915$ and
$\tau_{\text{free}} = 4.3902\times10^{4}$ yr. Halving $\sigma$ and doubling $L$
scales $\tau_{\text{free}}$ by $L^{2}\sigma = 4\times0.5 = 2$, and indeed
$4.3902/1.9910 = 2.205$; the small residual is the exact ratios
$\left(2.1^{2}\times0.5\right)/\left(1.0^{2}\times1.0\right) = 2.205$. ✔

---

## ★3 — Magnetic Reynolds number

$$Rm = \frac{UL}{\eta} = \frac{1.0\times10^{-3}\times1.0\times10^{6}}{0.79577}
= 1256.7.$$

$Rm\gg1$, so the **advective term dominates**: over the advection time
$L/U = 10^{6}/10^{-3} = 10^{9}\ \mathrm{s} = 31.7$ yr the field is carried with
the fluid, while diffusion needs $3.98\times10^{4}$ yr to erase it. Equivalently,
the balance scale is $\sqrt{\eta L/U} = \sqrt{0.79577\times10^{9}}
= 2.82\times10^{4}\ \mathrm{m} = 28.2\ \mathrm{km}$: structure below that scale
diffuses away.

---

## ★4 — Decay rates by degree

Degree $n$ decays at $n(n+1)\eta/L^{2}$:

| $n$ | $n(n+1)$ | rate ($\mathrm{s^{-1}}$) | decay time (yr) |
|---|---|---|---|
| 1 | 2 | $2\times1.5915/(2.10\times10^{6})^{2} = 7.2175\times10^{-13}$ | $4.3902\times10^{4}$ |
| 2 | 6 | $2.1653\times10^{-12}$ | $1.4634\times10^{4}$ |

The **degree-1 mode is the longer-lived** by a factor of 3, because the rate
scales as $n(n+1)$ and diffusion acts faster on smaller scales. This is the same
geometry as the downward-continuation amplification of
[08-01-03](../03-spherical-harmonic-magnetic.md) §6: higher degrees are more
sensitive to diffusion, which is why a long-lived field is observed to be dipole
dominated.

---

## ★5 — The critical dynamo number

The eigenvalues are $-k\pm\sqrt{\alpha\omega}$, so growth requires
$\alpha\omega > k^{2}$, i.e.

$$\omega_{\text{crit}} = \frac{k^{2}}{\alpha}
= \frac{(2.2778\times10^{-5})^{2}}{3.22\times10^{-5}}
= \frac{5.1884\times10^{-10}}{3.22\times10^{-5}}
= 1.6113\times10^{-5}\ \mathrm{yr^{-1}}.$$

For $\omega = 2\,\omega_{\text{crit}} = 3.2226\times10^{-5}$:

$$D = \frac{\alpha\omega}{k^{2}}
= \frac{3.22\times10^{-5}\times3.2226\times10^{-5}}{5.1884\times10^{-10}}
= 2.000,$$

$$\sqrt{\alpha\omega} = \sqrt{3.22\times10^{-5}\times3.2226\times10^{-5}}
= 3.2213\times10^{-5},$$

$$\lambda_{\max} = -k+\sqrt{\alpha\omega}
= -2.2778\times10^{-5}+3.2213\times10^{-5}
= +9.4350\times10^{-6}\ \mathrm{yr^{-1}},$$

matching the lesson's $+9.4350\times10^{-6}\ \mathrm{yr^{-1}}$ for $D = 2$. The
e-folding time is $1.06\times10^{5}$ yr.

---

## ★6 — Energy and dissipation budget

$$V = \frac{4}{3}\pi L^{3} = \frac{4}{3}\pi(2.0\times10^{6})^{3}
= 3.351\times10^{19}\ \mathrm{m^{3}},$$

$$\frac{B^{2}}{2\mu_0} = \frac{(5.0\times10^{-4})^{2}}{2\times1.256637\times10^{-6}}
= 9.947\times10^{-2}\ \mathrm{J\,m^{-3}},$$

$$E_{\text{mag}} = 9.947\times10^{-2}\times3.351\times10^{19}
= 3.333\times10^{18}\ \mathrm{J} = 3.333\times10^{6}\ \mathrm{TJ}.$$

$$J = \frac{B}{\mu_0 L}
= \frac{5.0\times10^{-4}}{1.256637\times10^{-6}\times2.0\times10^{6}}
= 1.989\times10^{-4}\ \mathrm{A\,m^{-2}},$$

$$P_{\text{ohm}} = \frac{J^{2}}{\sigma}V
= \frac{(1.989\times10^{-4})^{2}}{1.0\times10^{5}}\times3.351\times10^{19}
= 1.326\times10^{7}\ \mathrm{W},$$

$$\frac{E_{\text{mag}}}{P_{\text{ohm}}}
= \frac{3.333\times10^{18}}{1.326\times10^{7}}
= 2.513\times10^{11}\ \mathrm{s}
= 7.964\times10^{3}\ \mathrm{yr}.$$

Check against the identity $L^{2}/(2\eta)$ with $\eta = 1/(\mu_0\sigma)
= 7.9577$: $L^{2}/(2\eta) = 4.0\times10^{12}/15.915
= 2.513\times10^{11}\ \mathrm{s}$, the same number. ✔

---

## ★7 — A time-dependent dynamo experiment (specification)

**Model.** Two coupled amplitudes with $\alpha$-quenching and a fixed target
amplitude $B_0$:

$$\dot{P} = -kP + \frac{\alpha}{1+(B/B_0)^{2}}T, \qquad
\dot{T} = \omega P - kT, \qquad B = \sqrt{P^{2}+T^{2}}.$$

With $\alpha = \omega = \sqrt{D}\,k$ (so $D$ is the single control parameter) the
linear growth rate is $k(\sqrt D - 1)$, and saturation occurs at
$B\to B_0\sqrt{D-1}$ in the long-time limit.

**Supercriticality required.** To reach $0.9B_{\text{sat}}$ within
$T_{\text{run}} = 10^{9}$ yr the initial growth must be fast enough:
$e^{k(\sqrt D-1)T_{\text{run}}} \gg 1$, so

$$k(\sqrt D-1)T_{\text{run}} \gtrsim 3
\quad\Longrightarrow\quad
\sqrt D - 1 \gtrsim \frac{3}{k\,T_{\text{run}}}.$$

With $k = 2.2778\times10^{-5}\ \mathrm{yr^{-1}}$ and
$T_{\text{run}} = 10^{9}$ yr, $k\,T_{\text{run}} = 2.278\times10^{4}$, so
$\sqrt D \gtrsim 1.00013$ — i.e. $D \gtrsim 1.0003$. **The dynamical requirement
is weak**: any dynamo even slightly supercritical amplifies from a seed in
$10^{9}$ yr. What is *not* weak is the energy requirement of §5 of the lesson:
supplying the dissipation is the hard constraint, not the growth rate.

**Numerical scheme.** Integrate with a second-order Runge–Kutta scheme and a
timestep bounded by both the growth and the decay timescale,
$\Delta t \le 0.05/k$. Start from $P = T = 10^{-6}B_0$, integrate until
$|\mathrm{d}B/\mathrm{d}t| < 10^{-6}k B_0$, and report $B_{\text{sat}}/B_0$ against
$\sqrt{D-1}$.

**Convergence test.** Halve $\Delta t$; the saturated amplitude must change by
less than 0.1%. A second test: with the quenching disabled and the field below
$10^{-3}B_0$, the measured logarithmic growth rate must equal $k(\sqrt D-1)$ to
three digits.

---

## ★8 — Why the energy ratio is not evidence

Take $J = B/(\mu_0 L)$, $E_{\text{mag}} = \dfrac{B^{2}}{2\mu_0}V$ and
$P_{\text{ohm}} = \dfrac{J^{2}}{\sigma}V$. Then

$$\frac{E_{\text{mag}}}{P_{\text{ohm}}}
= \frac{B^{2}}{2\mu_0}\cdot\frac{\sigma}{J^{2}}
= \frac{B^{2}}{2\mu_0}\cdot\frac{\sigma\mu_0^{2}L^{2}}{B^{2}}
= \frac{\mu_0\sigma L^{2}}{2}
= \frac{L^{2}}{2\eta}.$$

Every factor of $B$ cancels. The ratio contains no information about the field,
the flow or the dynamo: it is a restatement of the definition of $\eta$ and the
assumed geometry $J\sim B/(\mu_0 L)$, i.e. the assumption that the field varies
on the scale $L$.

**Why an identity is not evidence.** Evidence must be a statement that could have
been false. "The observed decay time of the field is comparable with the
diffusion time computed from an independent conductivity measurement" would be
evidence; "the ratio of my computed energy to my computed dissipation equals the
diffusion time" is arithmetic. The distinction matters in the dynamo literature
because several proposed "confirmations" are of the second kind: they test the
internal consistency of a model, not the model against the Earth.
