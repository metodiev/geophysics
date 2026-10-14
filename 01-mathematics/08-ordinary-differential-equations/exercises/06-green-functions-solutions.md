# Solutions — 01-08-06 Green's Functions and Impulse Response

> **Read this after attempting the exercises, not before.** Every convolution
> below was evaluated by composite Simpson quadrature and compared against
> either a closed form or an independent Runge–Kutta integration; the residuals
> are quoted as computed.

---

## ★1 — A Green's function with one free end

**(a)** We need $-G'' = \delta(x-\xi)$ on $(0,1)$ with $G(0) = 0$ and
$G'(1) = 0$. For $x<\xi$ the equation is homogeneous and $G(0) = 0$, so
$G = c_1x$. For $x>\xi$ the equation is homogeneous and $G'(1) = 0$, so
$G = c_2$ (a constant has zero slope everywhere, in particular at $x=1$).
Continuity at $x = \xi$ requires $c_1\xi = c_2$. Integrating the equation across
the source,

$$\int_{\xi^{-}}^{\xi^{+}}(-G'')\,dx = 1
\;\Longrightarrow\; -G'(\xi^{+})+G'(\xi^{-}) = 1 .$$

Here $G'(\xi^{-}) = c_1$ and $G'(\xi^{+}) = 0$, so $c_1 = 1$ and $c_2 = \xi$.
Hence

$$G(x,\xi) = \begin{cases}x, & x\le\xi\\ \xi, & x\ge\xi\end{cases}
= \min(x,\xi).$$

**(b)** The lesson's Dirichlet–Dirichlet kernel is
$G = x(1-\xi)$ for $x\le\xi$, which grows with $\xi$ and is zero at both ends;
the present kernel is $\min(x,\xi)$, which is zero at $x = 0$ but *non-zero* at
$x = 1$ — as it must be, since the condition there is on the derivative. **The
physical difference is that the free end lets the solution float:** $u(1)$ is an
unknown rather than a prescribed zero, so a source anywhere in the interval
raises the whole free end by the same amount $\xi$ on the far side. In a
geophysical reading: a fluid-pressure problem with a sealed (no-flux) boundary
behaves this way, while a problem with the variable held fixed at both ends does
not.

**(c)** Differentiating, $G'(x,\xi) = 1$ for $x<\xi$ and $0$ for $x>\xi$, so

$$-G'(\xi^{+}) + G'(\xi^{-}) = -0 + 1 = 1 \;\checkmark$$

The finite-difference check of the same statement is what the lesson's Section
3.5 does numerically: with the source placed on a node, the three-point stencil
reproduces $\min(x,\xi)$ to $8.3\times10^{-17}$ at 20 interior nodes.

---

## ★2 — The first-order operator

**(a)** $G(t) = e^{-2t}H(t)$. For $t>0$, $G' + 2G = -2e^{-2t}+2e^{-2t} = 0$; for
$t<0$, $G = 0$. Across $t = 0$, $G$ jumps from 0 to 1, which is exactly the
$e^{0} = 1$ jump that the integration of $LG = \delta$ demands:

$$\int_{0^{-}}^{0^{+}}\left(G'+2G\right)dt = G(0^{+})-G(0^{-}) = 1 \;\checkmark$$

**(b)**
$$y(t) = \int_0^{t}e^{-2(t-s)}e^{-s}ds
= e^{-2t}\int_0^{t}e^{s}ds = e^{-2t}\left(e^{t}-1\right) = e^{-t}-e^{-2t}.$$

**(c)**

| $t$ | $e^{-t}-e^{-2t}$ | Simpson quadrature (20 000 panels) |
|---|---|---|
| 0.5 | 0.238651219 | 0.238651219 |
| 1.0 | 0.232544158 | 0.232544158 |
| 2.0 | 0.117019644 | 0.117019644 |

The quadrature agrees to all printed digits: the integrand is smooth on the
interval of integration (the kernel's jump lies at the moving upper endpoint,
where it contributes a term of order $h^{3}$ via Simpson's endpoint handling),
so the error is far below the digits shown. **This is the standard situation for
a convolution of a discontinuous kernel with a smooth source: the result is
smooth, and the quadrature converges rapidly.**

---

## ★3 — The step response

**(a)** With $G(t) = e^{-\zeta\omega_0t}\sin(\omega_dt)/\omega_d$,
$\omega_d = \sqrt{1-\zeta^{2}} = 0.994987$ and the forcing $f = 1$,

$$x(t) = \int_0^{t}G(t-s)\,ds = \int_0^{t}\frac{e^{-0.1u}\sin(0.994987u)}{0.994987}du
= \frac{1}{\omega_0^{2}}\left[1-e^{-\zeta\omega_0t}\left(\cos\omega_dt
+ \frac{\zeta}{\sqrt{1-\zeta^{2}}}\sin\omega_dt\right)\right].$$

(The closed form follows by integrating the oscillating exponential, and the
coefficient $\zeta/\sqrt{1-\zeta^{2}} = 0.100504$ is the same one that appears in
the homogeneous solution when $x(0) = 0$.)

**(b)** The steady-state value is $1/\omega_0^{2} = 1$. Numerically:

| $t$ | convolution (quadrature) | closed form | difference |
|---|---|---|---|
| 1 | 0.431028109 | 0.431028109 | $4.0\times10^{-15}$ |
| 5 | 0.901449332 | 0.901449332 | $5.7\times10^{-15}$ |
| 20 | 0.920883976 | 0.920883976 | $5.2\times10^{-15}$ |

Note that at $t = 20$ — about two decay times, since
$1/(\zeta\omega_0) = 10$ — the response is within 8 % of its steady value. **The
approach to a constant equilibrium is governed by the same exponential envelope
as the free decay**, which is the $y_\infty$ structure of
[01 First-Order ODEs](../01-first-order-odes.md) appearing in a second-order
system through one of its two roots.

**(c)** With $\zeta = 0$ and driving at $\omega = \omega_0$ the response grows
as

$$x(t) = \frac{t}{2}\sin t \qquad (x(0) = x'(0) = 0,\ \omega_0 = 1),$$

i.e. **linearly in time**, with an envelope $t/2$ — not exponentially, and not
to a finite value. The derivation is in
[03 Oscillators](../03-oscillators.md) ★★4 and the numerical verification is in
[06 Green's Functions](../06-green-functions.md) Section 3.4.

---

## ★★4 — The order of the impulse approximation

**(a)** Ratios of successive errors:

| $\epsilon$ | error | ratio |
|---|---|---|
| 0.400 | $3.99\times10^{-2}$ | — |
| 0.200 | $3.10\times10^{-2}$ | 1.29 |
| 0.100 | $1.81\times10^{-2}$ | 1.72 |
| 0.050 | $9.56\times10^{-3}$ | 1.89 |
| 0.025 | $4.73\times10^{-3}$ | 2.02 |

The ratios approach **2**, so the error is **first order** in $\epsilon$.

**(b)** Replacing $\delta(t)$ by $(\mathbb{1}\{0\le s\le\epsilon\})/\epsilon$ and
expanding the smooth kernel about $s = 0$:

$$\int_0^{t}G(t-s)\frac{\mathbb{1}_{[0,\epsilon]}(s)}{\epsilon}ds
= \frac{1}{\epsilon}\int_0^{\epsilon}\left[G(t)-sG'(t)+O(s^{2})\right]ds
= G(t) - \frac{\epsilon}{2}G'(t)+O(\epsilon^{2}).$$

The first-order term is explicit: **the error is $-\tfrac{\epsilon}{2}G'(t)$**,
so a pulse reproduces $G$ to $O(\epsilon)$ and the leading error is proportional
to the *derivative* of the impulse response, not to its value.

**(c)** At $\epsilon = 0.4$ the "narrow" pulse is 40 % of the time unit, so the
expansion is barely begun: the $O(\epsilon^{2})$ term is large and partially
cancels the first-order one, making the observed ratio 1.29 instead of 2. A
two-point convergence study using $\epsilon = 0.4$ and $0.2$ would report an
"order" of 0.37, which is meaningless. **Always use at least three step sizes,
and check that the ratio is still moving toward its asymptotic value** — the
same discipline as in the lesson's Section 5 for ODE integrators.

---

## ★★5 — Reciprocity

**(a)** Take $x\le\xi$. Then $G(x,\xi) = x(1-\xi)$. For the reversed problem we
need $G(\xi,x)$, i.e. evaluate at first argument $\xi$ with the *source* at $x$.
Since $\xi\ge x$, the second case of the formula applies:
$G(\xi,x) = x(1-\xi)$ ✓. Now take $x\ge\xi$: $G(x,\xi) = \xi(1-x)$, and
$G(\xi,x) = \xi(1-x)$ because $\xi\le x$ means the first case applies with
arguments swapped ✓. **Reciprocity follows from the two branches being the same
expression evaluated with the two arguments in the appropriate order.**

**(b)** For $L = -d^{2}/dx^{2}$, the Lagrange identity gives

$$\int_0^{1}\left(G(x,\xi)L[G(x,\eta)] - G(x,\eta)L[G(x,\xi)]\right)dx
= \left[G(x,\xi)G'(x,\eta) - G(x,\eta)G'(x,\xi)\right]_0^{1},$$

and the right side vanishes for **any** Green's function satisfying homogeneous
Dirichlet conditions at both ends. The left side is
$\int(G(x,\xi)\delta(x-\eta) - G(x,\eta)\delta(x-\xi))dx = G(\eta,\xi) -
G(\xi,\eta)$, so $G(\xi,\eta) = G(\eta,\xi)$: **reciprocity is the symmetry of
the operator, and the assumption used is that the boundary term vanishes.**

**(c)** A source at $A$ with a receiver at $B$ records the same trace (up to
instrument differences) as the reversed configuration. This is what makes it
legitimate to merge several surveys with different source–receiver geometries
into a single data set for inversion, and it is the physical basis of
reciprocity-based quality control in seismic acquisition: a repeat shot with
source and receiver interchanged should reproduce the earlier trace.

---

## ★★6 — Convolution with a smooth source

**(a)** $y(t) = \int_0^{t}e^{-2(t-s)}\left(1-e^{-s}\right)ds$. Split the integral
and use the two results already computed:

$$\int_0^{t}e^{-2(t-s)}ds = \frac{1-e^{-2t}}{2}, \qquad
\int_0^{t}e^{-2(t-s)}e^{-s}ds = e^{-t}-e^{-2t},$$

so

$$y(t) = \frac{1-e^{-2t}}{2} - e^{-t}+e^{-2t}
= \frac{1}{2}-e^{-t}+\frac{e^{-2t}}{2}
= \frac{1}{2}\left(1-e^{-t}\right)^{2}.$$

**(b)** $y' = \tfrac12\cdot2(1-e^{-t})e^{-t} = e^{-t}-e^{-2t}$ and
$y' + 2y = e^{-t}-e^{-2t} + 1-2e^{-t}+e^{-2t} = 1-e^{-t}$ ✓, which is the
forcing. And $y(0) = \tfrac12(1-1)^{2} = 0$ ✓. **Both checks pass, and note that
they are cheap: substituting an ansatz into the ODE and the initial condition is
the fastest verification available and should always be done.**

**(c)** The property used is **linearity plus superposition**: the response to a
sum equals the sum of the responses, so the constant part of the forcing and the
exponential part were convolved separately. The measurement procedure that leans
on it most heavily is **deconvolution of a known source from a recorded signal**:
the recorded trace is treated as a sum of contributions from source, path and
instrument, each a convolution, and each is removed by dividing its transfer
function out. Superposition is also the reason a *stack* of repeated shots is
legitimate when the source is repeatable, and the reason it fails when it is
not.

---

## ★★★7 — Causality and pole placement

**(a)** Solve $1-\omega^{2}+0.2i\omega = 0$:
$\omega^{2}-0.2i\omega-1 = 0$, so

$$\omega = \frac{0.2i\pm\sqrt{-0.04+4}}{2} = \frac{0.2i\pm1.989975}{2}
= \pm0.994987 + 0.1i .$$

Both poles, $\omega = \pm\omega_d + i\zeta\omega_0$, lie in the **upper** half
plane.

**(b)** Inverting the Fourier transform means evaluating
$G(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat G(\omega)e^{i\omega t}d\omega$.
For $t<0$ the factor $e^{i\omega t} = e^{i\operatorname{Re}(\omega)t}
e^{-\operatorname{Im}(\omega)t}$ **decays** as $\operatorname{Im}\omega\to-\infty$,
so Jordan's lemma permits the contour to be closed in the *lower* half plane.
By the residue theorem the integral then equals $-2\pi i$ times the sum of the
residues enclosed — that is, of the residues of the poles in the lower half
plane. With all poles in the upper half plane the contour encloses nothing and
the integral is zero. **A pole in the lower half plane would be enclosed by the
$t<0$ contour and would give a non-zero response before the impulse arrives: an
acausal system.**

**(c)** The error would be exposed by a **phase** measurement. Amplitude alone is
insensitive to which half plane a pole sits in, but the phase lag of a causal
system is completely determined by the amplitude through the Kramers–Kronig
relations; an acausal model must violate them. Concretely, for a
low-$\zeta$ resonance the causal model's phase must rise from $0°$ to $180°$;
the acausal counterpart has a lag that rises only to $180° - 2\times$ (the
contribution of the misplaced pole), i.e. it undershoots, and the discrepancy is
measurable at frequencies within a few linewidths of the peak. **So: fit the
phase, not only the amplitude, and treat a disagreement between the two fits as
evidence of a structural error rather than of noise.**

---

## ★★★8 — Discretising the source

**(a)** With the whole weight on the nearest node, the discrete solution is
*exactly* the Green's function for a source at that node. The exact $G$ for a
source at the true location $\xi$ between nodes differs from it by
$O(h)$: over a cell, $G(x,\xi) - G(x,\xi_{\text{node}})$ is proportional to
$|\xi-\xi_{\text{node}}| = \alpha h$ times a bounded factor. So the error is
first order, and the tabulated ratio of 1.91, 1.91, 1.98 per halving of $h$
confirms it. **First order is the correct expectation, and the tabulated numbers
are evidence, not an assumption.**

**(b)** For a source on a node the exact $G$ is piecewise linear with a slope
jump of $-1$ at the source, so

$$\frac{G_{i+1}-2G_i+G_{i-1}}{h^{2}} = 0 \quad (i\neq\text{node}), \qquad
\frac{G_{j+1}-2G_j+G_{j-1}}{h^{2}} = -\frac{1}{h} \; (i = \text{node}),$$

because for a piecewise-linear function the second difference equals
(slope$^{+}-$slope$^{-})/h$ at the kink and zero elsewhere. The discrete
equations are $-($second difference$) = $rhs with $rhs_j = 1/h$, so the exact
$G$ satisfies them identically, and by uniqueness of the linear system the
discrete solution *is* the exact $G$ at the nodes. For a source between nodes
the same argument works provided the source is distributed with the grid's own
hat function, because the hat-weighted delta is the functional that reproduces a
piecewise-linear solution exactly. Numerically: $8.3\times10^{-17}$ at 20 nodes.

**(c)** The general rule: **a source term is a functional, not a function, and
its discretisation must be the one that the scheme's interpolation reproduces
exactly.** Spreading a point source with a hat function, or using the
Galerkin-consistent load vector, preserves the scheme's order; assigning the
whole source to the nearest node silently drops one order of accuracy. A
geophysical context where this matters directly is **finite-difference
modelling of a point seismic source or of a pumped well**, where the
near-source field is exactly the quantity of interest: a search for a subtle
near-source effect at the 1 % level would be dominated by a first-order source
error that no amount of grid refinement at fixed source handling would remove.
