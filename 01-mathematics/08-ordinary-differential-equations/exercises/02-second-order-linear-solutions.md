# Solutions — 01-08-02 Second-Order Linear ODEs and Characteristic Equations

> **Read this after attempting the exercises, not before.** Every closed-form
> solution below was substituted back into its ODE numerically; the residual in
> each case is at the level of the difference scheme's round-off, which is
> stated where it is quoted.

---

## ★1 — Three initial-value problems

**(a)** $r^{2}+5r+6 = (r+2)(r+3)$, so $r = -2,-3$: **overdamped**. The general
solution is $x = C_1e^{-2t}+C_2e^{-3t}$. Imposing $x(0) = 1$ gives
$C_1+C_2 = 1$; imposing $x'(0) = -2C_1-3C_2 = 0$ gives $2C_1+3C_2 = 0$.
Solving, $C_1 = 3$, $C_2 = -2$:

$$x(t) = 3e^{-2t} - 2e^{-3t}, \qquad x(1) = 0.306432 .$$

*Check:* $x(0) = 3-2 = 1$ ✓; $x'(0) = -6+6 = 0$ ✓.

**(b)** $r^{2}+4r+4 = (r+2)^{2}$, so $r = -2$ twice: **critically damped**, and
the solution carries the factor of $t$:

$$x(t) = (C_1+C_2t)e^{-2t}.$$

$x(0) = 0$ gives $C_1 = 0$; $x'(t) = C_2e^{-2t}-2C_2te^{-2t}$ gives
$x'(0) = C_2 = 1$, so $x = te^{-2t}$. The maximum is where
$x' = e^{-2t}(1-2t) = 0$, i.e. $t = 0.5$, with

$$x_{\max} = 0.5\,e^{-1} = 0.183940 .$$

**(c)** $r^{2}+2r+5 = (r+1)^{2}+4$, so $r = -1\pm2i$: **underdamped** with
$\omega_0 = \sqrt5 = 2.236068$, $\zeta = 1/\sqrt5 = 0.447214$,
$\omega_d = 2$. The general solution is
$x = e^{-t}(A\cos2t+B\sin2t)$. Here $A = x(0) = 2$, and
$x'(0) = -A+2B = 0$ gives $B = 1$, so

$$x(t) = e^{-t}\left(2\cos2t+\sin2t\right), \qquad x(1) = 0.028328 .$$

The envelope is $\sqrt{A^{2}+B^{2}} = \sqrt5 = 2.236068$, the same number as
$\omega_0$ — a coincidence of this choice of data, not an identity.

---

## ★2 — Roots, $\zeta$ and case

For each equation let $2\zeta\omega_0$ be the coefficient of $x'$ and
$\omega_0^{2}$ the coefficient of $x$.

| Equation | $\omega_0$ | $\zeta$ | Roots | Case |
|---|---|---|---|---|
| (a) $x''+3x'+2x$ | $\sqrt2 = 1.414214$ | $3/(2\sqrt2) = 1.060660$ | $-1,\,-2$ | overdamped |
| (b) $x''+2x'+x$ | 1 | 1 | $-1,\,-1$ | critically damped |
| (c) $x''+x'+x$ | 1 | 0.5 | $-0.5\pm0.866025i$ | underdamped |

For (a) the discriminant is $9-8 = 1>0$, real distinct roots. For (c) the
discriminant is $1-4<0$ and $\omega_d = \sqrt3/2 = 0.866025$,
$T_d = 2\pi/\omega_d = 7.255197$.

---

## ★3 — The full parameter set of one oscillator

Matching coefficients: $\omega_0^{2} = 1$ so $\omega_0 = 1$;
$2\zeta\omega_0 = 0.4$ so $\zeta = 0.2$; and the discriminant is negative
($\zeta<1$), so the case is **underdamped**. Then

$$\omega_d = \omega_0\sqrt{1-\zeta^{2}} = \sqrt{0.96} = 0.979795897 ,$$

$$T_d = \frac{2\pi}{\omega_d} = 6.412749\ \mathrm{s}, \qquad
\tau_{\text{decay}} = \frac{1}{\zeta\omega_0} = 5.000000\ \mathrm{s},$$

$$\delta = \frac{2\pi\zeta}{\sqrt{1-\zeta^{2}}} = 1.282549830, \qquad
Q = \frac{1}{2\zeta} = 2.500 .$$

Envelope half-life: $t_{1/2} = \tau\ln 2 = 3.465736$ s, so
$t_{1/2}/\tau = \ln 2 = 0.693147$. **The envelope obeys the same $\ln 2$ rule
as any exponential; what makes it easy to forget is that the peaks themselves
are one damped period apart, not one decay time apart.**

---

## ★4 — A record, inverted for the parameters

**(a)** The logarithmic decrement is the logarithm of the peak ratio:

$$\delta = \ln 1.30 = 0.262364265 .$$

Since $\delta = 2\pi\zeta/\sqrt{1-\zeta^{2}}$, put
$z = \zeta/\sqrt{1-\zeta^{2}} = \delta/(2\pi) = 0.0417570$; then
$\zeta = z/\sqrt{1+z^{2}}$:

$$\zeta = \frac{0.0417570}{\sqrt{1+0.0017436}} = 0.041720 .$$

**(b)** $\omega_d = 2\pi/T_d = 2\pi/2.5 = 2.513274$ rad/s, and

$$\omega_0 = \frac{\omega_d}{\sqrt{1-\zeta^{2}}}
= \frac{2.513274}{0.999129} = 2.515464\ \mathrm{rad/s}.$$

The fractional difference is $1-\sqrt{1-\zeta^2} = 8.71\times10^{-4}$, i.e.
**0.087 %**: for $\zeta = 0.042$ the damped and undamped frequencies are
indistinguishable in practice, which is a general feature of lightly damped
systems.

**(c)** $Q = 1/(2\zeta) = 11.985$. The amplitude falls by a factor $e$ after a
time $\tau = 1/(\zeta\omega_0) = 9.529$ s, which is
$\tau/T_d = 3.811$ cycles. Equivalently, with $\delta = \ln 1.3$ the number of
cycles to reduce the amplitude by $e$ is $1/\delta = 3.811$.

---

## ★5 — Gravimeter design

**(a)** $\omega_0 = 2\pi/T_0 = \pi = 3.141593$ rad/s, so
$k = m\omega_0^{2} = 0.1\times9.869604 = 0.986960\ \mathrm{N\,m^{-1}}$.

**(b)** $c = 2\zeta\sqrt{km} = 2(0.7)\sqrt{0.0986960} = 1.4\times0.314158
= 0.439823\ \mathrm{N\,s\,m^{-1}}$. The free-decay time is the reciprocal of
the slowest decay rate; for $\zeta<1$ that rate is $\zeta\omega_0$, so

$$\tau_{\text{decay}} = \frac{1}{0.7\pi} = 0.454728\ \mathrm{s},
\qquad 6\tau_{\text{decay}} = 2.728\ \mathrm{s}.$$

**(c)** For $\zeta = 3$: $c = 2(3)\times0.314158 = 1.884948$ N s m⁻¹. The slow
root is $-\omega_0(\zeta-\sqrt{\zeta^{2}-1}) = -\pi(3-2.828427) = -0.538965$
s⁻¹, so $\tau_{\text{decay}} = 1.855$ s and six e-foldings take 11.13 s.
**The instrument is now four times slower than at $\zeta = 0.7$**: over-damping
does not settle a system faster, it settles it more slowly, because the slow
root approaches zero as $\zeta$ grows. In a gravimeter the practical consequence
is a reading that drifts for tens of seconds after each disturbance.

**(d)** The two roots of the free response are
$-\omega_0(\zeta\pm\sqrt{\zeta^{2}-1})$ for $\zeta\ge1$ and
the real part $-\zeta\omega_0$ with an oscillation for $\zeta<1$. The decay
time is minimised where $\zeta\omega_0$ is largest subject to a non-oscillatory
response, which is at **critical damping $\zeta = 1$**:
$\tau_{\min} = 1/\omega_0 = 1/\pi = 0.318310$ s. (At $\zeta = 1$ the solution
contains the factor $t$, so the envelope decays slightly more slowly than
$e^{-\omega_0t}$; the reading is still settled in about $3\tau_{\min}$, which
is what a design specification would quote.) Note that a small amount of
overshoot is usually acceptable, which is why practical instruments sit near
$\zeta = 0.5$–$0.7$ rather than exactly at 1.

---

## ★6 — Buoyancy oscillation

**(a)** $\omega_0 = N = 0.015$ rad/s, so

$$T = \frac{2\pi}{N} = \frac{6.283185}{0.015} = 418.879\ \mathrm{s}
= 6.981\ \mathrm{min}.$$

**(b)** $N^{2} = -(g/\rho)\,d\rho/dz$ gives

$$\frac{d\rho}{dz} = -\frac{N^{2}\rho}{g} = -\frac{(0.015)^{2}(1025)}{9.81}
= -0.02351\ \mathrm{kg\,m^{-4}}.$$

The sign is **negative**: density increases with depth, which is the definition
of stable stratification. A positive value would mean denser water above
lighter water, and the parcel's restoring force would be directed away from
equilibrium — the equation would change sign and the displacement would grow
exponentially rather than oscillate.

**(c)** The equation neglects (i) **damping and mixing**, which reduces the
restoring force and hence the observed frequency, and (ii) **vertical shear of
the horizontal flow**, which couples the oscillation to the mean flow; with
sufficient shear the perturbation can draw energy from the mean flow and grow
(Kelvin–Helmholtz instability). It also assumes a parcel that does not exchange
heat with its surroundings (adiabatic motion); in the ocean this is a good
approximation, in the atmosphere it is not, and one uses the potential
temperature and the *Brunt–Väisälä* frequency defined with respect to it.

---

## ★★★7 — A free oscillation of the Earth

**(a)** $\omega_0 = 2\pi/T = 2\pi/1500 = 4.188790\times10^{-3}$ rad/s. The
amplitude envelope decays with time constant

$$\frac{2Q}{\omega_0} = \frac{2(250)}{4.188790\times10^{-3}}
= 1.193662\times10^{5}\ \mathrm{s} = 1.3816\ \mathrm{d}.$$

**(b)** After $n$ complete oscillations the elapsed phase is $2\pi n$, and the
amplitude envelope factor is $e^{-\pi n/Q}$ (because the decay per radian of
phase is $1/(2Q)$ and a full oscillation is $2\pi$ radians). For $n = 10$,

$$e^{-\pi(10)/250} = e^{-0.125664} = 0.881911,$$

so **88.2 % of the amplitude** remains. Energy goes as amplitude squared:

$$0.881911^{2} = 0.777767, \qquad\text{i.e. } 77.8\ \% .$$

**(c)** With $Q = 1000$ the decay time is $4\times$ longer and the half-width of
the spectral peak, $\Delta\omega/\omega_0 = 1/Q$, is $4\times$ **narrower**. Both
follow from the one identity

$$\frac{1}{Q} = \frac{\Delta\omega}{\omega_0} = \frac{1}{\omega_0\tau_{\text{decay}}},$$

which is the time–bandwidth relation in mechanical form: **a long-ringing mode
is a sharp spectral peak, and the two are the same statement.** A modal peak in
a spectrum and a decay rate in a time series are two measurements of $Q$.

---

## ★★★8 — Continuity through $\zeta = 1$

**(a)** With $\omega_0 = 1$, $x(0) = 1$, $x'(0) = 0$, evaluating at $t = 1$:

| $\epsilon$ | $x(1)$ at $\zeta = 1-\epsilon$ | $x(1)$ at $\zeta = 1+\epsilon$ | $\Delta(\epsilon)$ |
|---|---|---|---|
| $10^{-2}$ | 0.734527695 | 0.736980259 | $2.4526\times10^{-3}$ |
| $10^{-3}$ | 0.735636207 | 0.735881460 | $2.4525\times10^{-4}$ |
| $10^{-4}$ | 0.735746619 | 0.735771145 | $2.4525\times10^{-5}$ |

(The value at $\zeta = 1$ itself is $2e^{-1} = 0.735758882$.)

**(b)** Each decade reduction in $\epsilon$ reduces $\Delta$ by a factor
$10.00$: the power law is $p = 1$, i.e. **$\Delta$ is linear in $\epsilon$**,
with $\Delta \approx 0.2453\,\epsilon$ (so $dx/d\zeta = -0.1226$ at
$\zeta = 1$, approached from both sides with the same magnitude).

**(c)** The solution depends on $\omega_d$ only through the combination
$\cos(\omega_dt)$ and $\sin(\omega_dt)/\omega_d$, and **both are even functions
of $\omega_d$**: their Taylor series contain only even powers, i.e. only powers
of $\omega_d^{2} = 1-\zeta^{2}$. The solution is therefore an analytic function
of $\zeta$ in a neighbourhood of $\zeta = 1$, and the square root in
$\omega_d = \sqrt{1-\zeta^{2}}$ never appears undressed. The practical
consequence for a code is twofold: **use one continuous formula rather than
three cases if you can, and if you must branch, decide the branch from
$|\zeta-1|$ with an explicit tolerance rather than from a strict comparison of
floating-point values.** A branch chosen at machine precision will flip between
the complex and real formulas, and while the *values* agree to $10^{-7}$ near
the transition (Section 3.3 of the lesson) the *floating-point behaviour* of
the two branches does not have to.
