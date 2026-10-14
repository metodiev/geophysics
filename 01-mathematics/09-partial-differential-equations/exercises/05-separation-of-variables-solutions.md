# Solutions — 01-09-05 Separation of Variables and Boundary Conditions

> **Read this after attempting the exercises, not before.**
>
> Worked solutions with the reasoning; numbers were computed rather than estimated.
> Where a count or an order is quoted, the procedure used to obtain it is stated
> so that it can be repeated. Conventions: $u = X(x)T(t)$; separation constant
> $-\lambda$; $\kappa$ in $\mathrm{m^2\,s^{-1}}$.

---

## ★1 — Insulated end, fixed end

**(a) The two ordinary differential equations.** Substituting $u = XT$ into
$u_t = \kappa u_{xx}$ gives $T'/T = \kappa X''/X = -\kappa\lambda$, hence

$$T' + \kappa\lambda T = 0 \qquad\text{(time)}, \qquad
X'' + \lambda X = 0 \qquad\text{(space)} .$$

The boundary conditions act on the *space* problem: $X'(0) = 0$ and $X(L) = 0$.

**(b) Eigenvalues and eigenfunctions.** For $\lambda = \mu^2 > 0$,
$X = A\cos(\mu x) + B\sin(\mu x)$. The condition $X'(0) = 0$ forces $B = 0$, so
$X = A\cos(\mu x)$. The condition $X(L) = 0$ then requires
$\cos(\mu L) = 0$, i.e.

$$\mu_n = \frac{(n - \tfrac12)\pi}{L}, \qquad
\lambda_n = \frac{(n-\tfrac12)^2\pi^2}{L^2}, \qquad
X_n(x) = \cos\!\left(\frac{(n-\tfrac12)\pi x}{L}\right), \qquad n = 1,2,\dots$$

**Is $\lambda = 0$ allowed?** No. For $\lambda = 0$, $X = A + Bx$ with
$X'(0) = B = 0$ so $X = A$ constant, and then $X(L) = A = 0$ forces $A=0$. Only
the trivial solution exists, so $\lambda = 0$ is not an eigenvalue. This is the
mirror of the both-insulated case, where the constant *is* an eigenvalue — the
difference is that one *fixed* end kills the constant mode. Since the constant mode
is the last to decay, whether it exists changes long-time behaviour qualitatively,
which is why this check is not pedantry. A physical reading: an insulated–fixed
slab cannot reach a uniform temperature, so a non-decaying mode would contradict
the boundary data; the constant is available only when no boundary fixes a value.

**(c) General solution and coefficients.**

$$u(x,t) = \sum_{n=1}^{\infty}b_n\cos\!\left(\frac{(n-\tfrac12)\pi x}{L}\right)
\mathrm{e}^{-\kappa\lambda_nt}, \qquad
b_n = \frac{2}{L}\int_0^Lf(x)\cos\!\left(\frac{(n-\tfrac12)\pi x}{L}\right)dx ,$$

where the factor $2/L$ follows from
$\int_0^L\cos^2(\mu_nx)dx = L/2$ — the orthogonality of the **cosine** basis with
these *quarter-wave* eigenvalues, not the half-wave ones of the Dirichlet problem.

---

## ★2 — Coefficients of the triangular profile

**(a) The general formula.** For the symmetric triangle on $(0,1)$,

$$b_n = 2\int_0^1f(x)\sin(n\pi x)\,dx
= 2\left[\int_0^{1/2}2x\sin(n\pi x)\,dx + \int_{1/2}^{1}2(1-x)\sin(n\pi x)\,dx
\right] .$$

Both integrals are elementary. Combining them (or noting that $f$ is the
antisymmetric continuation about $x=\tfrac12$, so only odd $n$ survive) gives the
closed form

$$b_n = \frac{8}{n^2\pi^2}\sin\!\left(\frac{n\pi}{2}\right) .$$

For $n = 1$: $b_1 = 8/\pi^2 = 0.810569$ ✓, matching the lesson's numerical value.

**(b) $b_3$ and $b_5$.**

$$b_3 = \frac{8}{9\pi^2}\sin\frac{3\pi}{2} = -\frac{8}{9\pi^2} = -0.090063 , \qquad
b_5 = \frac{8}{25\pi^2}\sin\frac{5\pi}{2} = \frac{8}{25\pi^2} = +0.032423 .$$

**(c) Comparison.** The analytic values agree with the numerically computed ones to
all the digits quoted ($0.810569$, $-0.090063$, $+0.032423$). This is the check that
matters for the lesson's numerical work: the quadrature used to obtain the
coefficients in the demonstration is verified against an exact expression, so the
later comparison between the series and the finite-difference solution tests the
*scheme*, not the coefficients.

**(d) Why the even coefficients vanish.** $\sin(n\pi/2) = 0$ for even $n$, directly
from the closed form. Physically: $f$ is odd about $x = \tfrac12$ while
$\sin(2\pi x), \sin(4\pi x), \dots$ are even about that point, so the projections
integrate to zero. Equivalently, the initial state has a symmetry that the even
modes do not share, and the symmetry is preserved by the equation and the boundary
conditions (both are symmetric about $x=\tfrac12$), so an even mode can never be
excited, whatever the amplitude.

**One caveat about the closed form.** It relies on the triangle being *symmetric*
and *peak-valued at the midpoint*. A general piecewise-linear initial condition has
no such form and its coefficients must be integrated; the symmetry argument saves
algebra only in symmetric cases.

---

## ★3 — Geothermal gradient at depth

With $q_0/k = 0.026\ \mathrm{K\,m^{-1}}$ and $A/(2k) = 10^{-6}/5 =
2.0\times10^{-7}\ \mathrm{K\,m^{-2}}$:

| $z$ | $T_s + (q_0/k)z$ | $-Az^2/(2k)$ | $T$ | Radiogenic share |
|---|---|---|---|---|
| 15 km | $10 + 390 = 400.0\ ^\circ$C | $-45.0\ ^\circ$C | $355.0\ ^\circ$C | 11 % |
| 25 km | $10 + 650 = 660.0\ ^\circ$C | $-125.0\ ^\circ$C | $535.0\ ^\circ$C | 19 % |

**Reading the table.** The radiogenic term *reduces* the temperature relative to the
linear extrapolation, and its share grows quadratically with depth: negligible at
5 km, 4 % at 10 km, 23 % at 30 km. The sign surprises people, so it is worth
restating from the physics: radiogenic production adds heat *along the path*, so the
upward heat flow decreases with depth, $q(z) = q_0 - Az$, a decreasing gradient means
a concave geotherm, and concavity means the temperature at depth is *below* the
linear extrapolation. Getting this sign wrong raises the predicted temperature at
30 km by 360 °C.

**What the numbers do not support.** They are computed from illustrative parameters,
and real crustal geotherms deviate because $k$ varies with lithology and
temperature, $q_0$ varies between provinces by a factor of two or more, and $A$
varies by an order of magnitude between granite, basalt and sediment. The
calculation establishes the *structure* of the answer (linear plus quadratic, with
a definite sign) and shows how large the correction can be; it does not provide a
site-specific temperature, and quoting a depth to a temperature isotherm from it
would be unjustified.

---

## ★4 — Steady-state subtraction

**Verification.** For $v(x) = T_0 + (T_1-T_0)x/L$: $v' = (T_1-T_0)/L$ is constant,
so $v'' = 0$ ✓; and $v(0) = T_0$, $v(L) = T_1$ ✓.

**The problem for $w = u - v$.** Since $v$ is time-independent and satisfies the
equation, $w$ satisfies the *same* equation $w_t = \kappa w_{xx}$. The boundary
conditions become homogeneous:

$$w(0,t) = u(0,t) - v(0) = T_0 - T_0 = 0, \qquad
w(L,t) = u(L,t) - v(L) = T_1 - T_1 = 0 ,$$

and the initial condition becomes

$$w(x,0) = f(x) - v(x) ,$$

with $f$ the original initial profile. So the full problem is: solve the heat
equation with zero boundary data and initial condition $f - v$; then
$u = v + w$.

**Why this matters, and when it fails.** The eigenfunctions used for $w$ require
*zero* boundary data, so without the subtraction the expansion would not be
admissible — the series would converge to a function that violates the boundary
data, which shows up numerically as a slowly decaying error near the ends (the
Gibbs-type artefact of a mismatched series). The subtraction is legitimate only when
a steady particular solution exists:

- it fails if the boundary data are time-dependent (then a time-dependent
  particular solution or Duhamel's principle is required,
  [01-09-07](../07-boundary-value-problems.md) §5);
- it fails if a source term is time-dependent, for the same reason;
- it fails if the equation has no steady solution at all — for example a
  well-posedness question worth checking, as when the flux data are inconsistent
  with the enclosed sources (the compatibility condition of
  [01-09-04](../exercises/04-laplace-poisson-solutions.md) ★★5).

---

## ★★5 — Fixed–free string versus fixed–fixed

**Frequencies.** With $X(0) = 0$ and $X'(L) = 0$: $X = \sin(\mu x)$ requires
$\mu L = (n-\tfrac12)\pi$, so

$$\omega_n^{\text{fixed–free}} = \frac{(n-\tfrac12)\pi c}{L} , \qquad
n = 1,2,\dots$$

while the fixed–fixed case gives $\omega_n = n\pi c/L$.

**Which is lower, and why.** The fixed–free fundamental is
$\pi c/(2L)$, exactly **half** the fixed–fixed fundamental $\pi c/L$. Physically, a
free end is a *node-free* end: the boundary cannot support a node, so the wave must
fit a quarter wavelength into $L$ rather than a half wavelength. A quarter
wavelength in the same length means twice the wavelength, hence half the frequency.
The general rule is: **the more restrictive the boundary, the higher the
frequencies.** Replacing a free end by a clamped one shortens the effective
wavelength and raises the pitch, which is exactly what luthiers exploit and what
makes a basin's resonance depend on whether its edge is a free surface or a rigid
basement.

**Ratio of fundamentals.** $\omega_1^{\text{fixed–free}}/\omega_1^{\text{fixed–fixed}}
= 1/2$. The *first overtones* differ less: the second fixed–free mode is
$3\pi c/(2L)$ against the fixed–fixed second mode $2\pi c/L$, a ratio of $0.75$.

**Consistency check.** As $L\to\infty$ the mode spacing tends to zero and the
discrete spectrum merges into a continuum — the correct limit for a semi-infinite
string, which has no discrete resonances.

---

## ★★6 — Decay of a long-wavelength perturbation

**(a) Decay rate and time.** With $\lambda = 200$ km $= 2\times10^{5}$ m, the
wavenumber is $k = 2\pi/\lambda = 3.1416\times10^{-5}\ \mathrm{rad\,m^{-1}}$, and the
decay rate is $\kappa k^2$:

$$\kappa k^2 = 10^{-6}\times(3.1416\times10^{-5})^2
= 10^{-6}\times9.8696\times10^{-10} = 9.870\times10^{-16}\ \mathrm{s^{-1}} ,$$

$$\tau = \frac{1}{\kappa k^2} = 1.013\times10^{15}\ \mathrm{s} = 32.1\ \mathrm{Myr} .$$

**(b) Reconciliation with $L^2/\kappa$.** Taking $L$ equal to a quarter of the
wavelength, $L = \lambda/4 = 50$ km:

$$\frac{L^2}{\kappa} = \frac{(5\times10^4)^2}{10^{-6}} = 2.5\times10^{15}\ \mathrm{s}
= 79.2\ \mathrm{Myr} .$$

The two differ by the factor

$$\frac{79.2}{32.1} = 2.47 \approx \frac{\pi^2}{4} = 2.467 .$$

That is exactly as it should be: since $k = 2\pi/\lambda$ and $L = \lambda/4$, we
have $k = \pi/(2L)$, so

$$\frac{1}{\kappa k^2} = \frac{4L^2}{\kappa\pi^2} = \frac{L^2}{\kappa}\cdot
\frac{4}{\pi^2} .$$

The scaling $\tau \sim L^2/\kappa$ is correct; the prefactor depends on the
definition of $L$ and on the eigenvalue, and quoting a time without saying which
convention was used is off by a factor of 2.5 — small enough to look like data, large
enough to change an interpretation.

**(c) Why the thickness does not enter.** The perturbation is a Fourier mode with a
*wavelength* set by the initial condition, and its decay rate is $\kappa k^2$ for
any domain. The layer thickness enters only through the *boundary conditions*: if
the layer's boundaries are remote compared with the wavelength (a "deep" layer), the
mode behaves as in an infinite medium and the thickness is irrelevant, exactly as
here (200 km wavelength in a 1 km layer, with the layer's thermal structure imposed
by the surroundings rather than by fixed-temperature boundaries). If the wavelength
were comparable to the thickness, the boundaries would quantise the allowed
wavenumbers and the thickness would enter — but then the problem would be a slab
problem with the eigenvalues of [01-09-05](../05-separation-of-variables.md) §2.2,
not a single-mode decay.

**Physical reading of the 32 Myr.** A 200 km thermal anomaly takes tens of millions
of years to decay away by conduction. That is longer than typical intraplate
magmatic events and comparable to the time since major orogenic events, which is
why long-wavelength lithospheric thermal anomalies persist and why a single
short-lived event cannot leave a long-wavelength thermal signature.

---

## ★★7 — The Robin eigenvalue problem

**(a) The transcendental equation.** The space problem is
$X'' + \lambda X = 0$ with $X'(0) = 0$ and $-X'(L) = hX(L)$. The first condition
gives $X = \cos(\mu x)$ with $\mu = \sqrt{\lambda}$, and the second gives

$$-\left(-\mu\sin(\mu L)\right) = h\cos(\mu L)
\qquad\Longrightarrow\qquad
\boxed{\ \tan(\mu L) = \frac{h}{\mu}\ }$$

i.e., with $\mu_n$ the $n$-th positive root,

$$\lambda_n = \mu_n^2 .$$

This is the standard result for a convective (Robin) boundary. Note that the
equation is *transcendental*: the eigenvalues must be found numerically, and the
eigenfunctions are $\cos(\mu_nx)$ with non-uniformly spaced $\mu_n$.

**(b) The limit $h\to\infty$.** As $h\to\infty$ the right side diverges, so
$\tan(\mu L)\to\infty$, which requires $\mu L\to(n-\tfrac12)\pi$, i.e.

$$\mu_n \to \frac{(n-\tfrac12)\pi}{L} \qquad (h\to\infty),$$

which are exactly the Dirichlet–Neumann eigenvalues (a fixed temperature at
$x = L$ combined with insulation at $x = 0$). The physical statement is that an
*infinitely* efficient convective surface pins the surface temperature to the
ambient value: Robin becomes Dirichlet. A useful intermediate check is that for
moderately large $h$ the roots are close to the Dirichlet–Neumann values but
shifted downward (since $\tan$ is positive just below its asymptotes for this
branch pattern), so the modes decay slightly *faster* than in the idealised case.

**(c) The other limit and the physical meanings.**

- $h\to\infty$: the surface temperature is prescribed; the boundary removes or
  supplies heat without limit. This is the idealisation used for a borehole
  surface and is a good approximation for a well-mixed ocean or a rapidly
  convecting region.
- $h\to0$: $-X'(L) = 0$, i.e. the surface is **insulated** — no heat leaves at all.
  The eigenvalues tend to the Neumann–Neumann values $\mu_n = n\pi/L$ with
  $\mu_0 = 0$ included: the constant mode reappears, and the problem is
  conservative.
- Finite $h$: the surface exchanges heat with a reservoir at the ambient temperature
  at a rate proportional to the difference. This is the physically realistic case
  for a land surface exchanging with air, and its dimensionless form is the Biot
  number $hL/k$. The practical consequence is a *finite* decay time for every mode
  including the constant one, which is what makes the steady state well defined —
  compare [01-09-07](../07-boundary-value-problems.md) §7.2, where the same Biot
  number appears in the finite-difference flux residual.

**Why this is not a detail.** The three cases give qualitatively different
long-time behaviour (decay to uniform, decay to a linear profile, decay to zero
relative to the ambient), and they differ by a factor of order unity in every
timescale. Choosing the wrong one is a modelling error of the kind that no
refinement can fix.

---

## ★★8 — Cooling of a sphere

**(a) Decay rates.** With $k_n = n\pi/a$ and the diffusion equation in radial
form, the decay rates are

$$\lambda_n = \kappa k_n^2 = \frac{\kappa n^2\pi^2}{a^2} ,$$

so $\lambda_1 = \kappa\pi^2/a^2$ and $\lambda_2 = 4\kappa\pi^2/a^2$.

**(b) The ratio and its consequence.** $\lambda_2/\lambda_1 = 4$. After the
fundamental has decayed by a factor $1/e$, the second mode has decayed by
$\mathrm{e}^{-4} = 0.018$; after two fundamental time constants it is
$\mathrm{e}^{-8} = 3.4\times10^{-4}$; after three, $\mathrm{e}^{-12} =
6.1\times10^{-6}$. So a single exponential describes the cooling well once the
elapsed time exceeds about two fundamental time constants, and poorly before that.
Two practical consequences:

- **Fitting a single exponential to early-time cooling overestimates the time
  constant** (the profile still contains the faster-decaying second mode), and the
  bias grows if the observations start close to the emplacement time. Fitting
  should either begin after $t\gtrsim2a^2/(\kappa\pi^2)$ or use two exponentials.
- **The high modes are why a "cooling time" is ambiguous** unless the quantity being
  cooled (surface temperature, centre temperature, mean temperature) is specified:
  each has a different combination of modes, so each relaxes at a different apparent
  rate. This is the same ambiguity that appears in
  [01-09-04](../exercises/04-laplace-poisson-solutions.md) ★1(d) for the interface
  bookkeeping and in ★★7 of this set for boundary conditions: the answer depends on
  what is being measured as much as on the medium.

**(c) Time constant for granite.** With $\kappa = 1.18\times10^{-6}\ \mathrm{m^2\,s^{-1}}$
(the value computed in [01-09-02](../exercises/02-heat-equation-solutions.md) ★1 for
granite) and $a = 500$ m:

$$\tau_1 = \frac{a^2}{\kappa\pi^2} = \frac{2.5\times10^{5}}{1.18\times10^{-6}
\times9.8696} = 2.15\times10^{10}\ \mathrm{s} \approx 680\ \mathrm{yr} .$$

The diffusive scale $a^2/\kappa$ is $2.12\times10^{11}$ s $= 6700$ yr, i.e. about
ten times longer; the ratio is $\pi^2$, as in Section 6(b). A 1 km-diameter
granite body therefore loses its thermal anomaly in of order a thousand years,
which is why small intrusions leave no long-lived thermal signature, and why the
thermal aureole of a small dyke is a transient phenomenon recorded only in the
contact rock.

---

## ★★★9 — How many terms are needed?

**Method.** Coefficients from the analytic form of ★2,
$b_n = 8\sin(n\pi/2)/(n^2\pi^2)$; the reference is the same series truncated at
$N = 400$ terms (the truncation error of that reference is far below $10^{-8}$ for
all three times); the error metric is the maximum over 399 interior points. The
smallest $N$ for which the metric falls below $10^{-8}$ is reported.

**Reported counts.**

| $t$ | Terms for a $10^{-8}$ maximum-norm error | Error with $N = 5$ |
|---|---|---|
| $0.5$ | 1 | $0$ (below round-off) |
| $0.05$ | 5 | $5.2\times10^{-13}$ |
| $0.005$ | 15 | $1.7\times10^{-3}$ |

**(b) The trend, and why.** The $n$-th mode carries the factor
$\mathrm{e}^{-n^2\pi^2t}$, so the terms that must be retained are those with
$n^2\pi^2t\lesssim\ln(1/\epsilon)$ for target accuracy $\epsilon$. Solving for the
largest needed $n$:

$$N \approx \frac{1}{\pi}\sqrt{\frac{\ln(1/\epsilon)}{t}} .$$

For $\epsilon = 10^{-8}$, $\ln(1/\epsilon) = 18.42$, so
$N\approx 1.366/\sqrt{t}$:

| $t$ | Predicted $N$ | Measured $N$ |
|---|---|---|
| $0.5$ | $1.93$ | 1 |
| $0.05$ | $6.11$ | 5 |
| $0.005$ | $19.3$ | 15 |

The prediction is an upper bound and the measured values are slightly lower, which
is expected: the bound treats every mode up to $N$ as needing to be below the
tolerance, whereas in fact the modes just below the cutoff are suppressed by the
coefficients $b_n\sim n^{-2}$ and by cancellation. The *scaling*
$N\propto t^{-1/2}$ is what matters, and it is reproduced.

**(c) The practical rule.** Choose $N$ from
$N \gtrsim \frac{1}{\pi}\sqrt{\ln(1/\epsilon)/t}$, then verify by increasing $N$ by
50 % and checking that the answer does not change. Two refinements worth adopting:

- the required $N$ grows without bound as $t\to0$, so **the series is the wrong tool
  for very short times** (where the initial profile must be represented directly);
- if the required accuracy is $\epsilon$, the *reference* used to verify the series
  must have truncation error well below $\epsilon$ — with $\epsilon = 10^{-8}$ a
  400-term reference is adequate at $t = 0.005$ because
  $\mathrm{e}^{-400^2\pi^2\times0.005}$ underflows, but at $t = 10^{-4}$ it would not
  be, and the "measured error" would then be dominated by the reference.

**(d) Limits of the conclusion.** The counts are for one initial profile, one
equation and one accuracy target, and they rest on the analytic coefficients — so
they test the convergence of the expansion, not any quadrature. For a profile whose
coefficients decay only like $1/n$ (a function with a derivative discontinuity
misaligned with the boundary), the mode count would be far larger, and near that
discontinuity the series error would converge only linearly in $1/N$. The rule
(c) should therefore be applied with the *decay rate of one's own coefficients* in
mind, never as a universal constant.

---

## ★★★10 — Layered conduction and the slowest mode

**(a) Layer matching and the transcendental equation.** Consider $n$ layers with
conductivity $k_j$ and diffusivity $\kappa_j$, layer $j$ occupying
$z_j<z<z_{j+1}$. Within each layer a separated mode has the form

$$T_j(z,t) = \left[A_j\cos(q_jz) + B_j\sin(q_jz)\right]\mathrm{e}^{-\lambda t},
\qquad q_j^2 = \frac{\lambda}{\kappa_j} ,$$

where the *same* $\lambda$ appears in every layer (the decay rate is global) and the
wavenumber $q_j$ differs because the diffusivity does. The matching conditions at
each interface $z_{j+1}$ are

$$T_j = T_{j+1} \quad\text{(continuity of temperature)}, \qquad
k_j\frac{\partial T_j}{\partial z} = k_{j+1}\frac{\partial T_{j+1}}{\partial z}
\quad\text{(continuity of flux)} .$$

These are **two conditions per interface, plus two at the outer boundaries**: $2n$
conditions for $2n$ unknown coefficients $(A_j,B_j)$. A nonzero solution exists only
if the determinant of that $2n\times2n$ system vanishes, and the determinant is a
function of $\lambda$ alone (through the $q_j(\lambda)$). Hence

$$\det M(\lambda) = 0$$

is the transcendental equation for the modal decay rates. It has infinitely many
roots $\lambda_1<\lambda_2<\dots$, just as the homogeneous problem does, but the
function is a sum of products of $\cos$ and $\sin$ of $\sqrt{\lambda}$ terms and has
no closed-form roots.

**Two checks worth building in.** First, with all layers identical the determinant
must reduce to $\sin(qH) = 0$, recovering $q_n = n\pi/H$ — a one-line test that the
matching matrix is assembled correctly. Second, the flux matching must use
$k\,\partial_zT$ and not $\partial_zT$ alone; using the derivative is the
classic error and produces a spurious interface source whose size scales with the
conductivity contrast.

**(b) Finding the slowest mode.** The slowest decay rate $\lambda_1$ is the smallest
positive root of $\det M(\lambda) = 0$, and it dominates long-time behaviour. An
algorithm:

1. establish a bracket: the problem's slowest rate lies between the smallest
   eigenvalue of the *slowest* layer treated as homogeneous
   ($\kappa_{\min}\pi^2/H^2$) and the smallest of the *fastest* layer; a bisection
   or a safeguarded Newton scheme on $\log\det M$ finds the root once bracketed;
2. evaluate $\det M$ with a stable elimination rather than an explicit determinant
   expansion, because the matrix entries contain $\cos$ and $\sin$ of large
   arguments and the determinant can lose many digits to cancellation;
3. refine with a secant or Newton step using the derivative from finite differences
   of $\log\det M$, since only the sign is needed for bisection.

**What can make it fail.** Three failure modes, all of which I would check before
trusting a number:

- **Cancellation in $\det M$**: with many thin layers, the determinant is a
  difference of exponentially large terms. The cure is a transfer-matrix
  formulation with scaling, or a shooting method with orthonormalisation, rather
  than a direct determinant;
- **Missing the bracket**: if the initial interval does not contain the root, the
  bisection converges to a spurious sign change or reports failure. Plotting
  $\log\lvert\det M\rvert$ against $\lambda$ over several decades is the cheap
  guard;
- **A root that is not physical**: negative or complex $\lambda$ indicate a mis-set
  boundary condition (or a genuinely convective instability in a problem where the
  sign of the buoyancy term matters). For a pure conduction problem all roots must
  be real and positive, and a complex root is a bug.

**(c) When the problem becomes non-separable.** Separation requires that the
operator be separable in the chosen coordinates: the domain must be a coordinate
box, the coefficients must depend on one variable at a time, and the boundary
conditions must be on coordinate surfaces. The problem stops being separable as soon
as any of the following holds:

- the conductivity varies in two or three directions ($k(x,z)$), so the operator
  $\nabla\cdot(k\nabla T)$ does not split;
- the geometry is not a coordinate box — a salt dome, a dipping layer, a wedge, a
  borehole with an inclined axis;
- a boundary condition couples directions (a convective condition on a sloping
  surface, a radiation condition with an oblique angle);
- the material is anisotropic with non-axis-aligned principal axes.

The numerical alternative is then a **discretisation**: finite differences or, where
the geometry is irregular, finite elements or finite volumes in the weak
formulation of [01-09-08](../08-weak-solutions.md). The variational form handles
discontinuous $k$ naturally, which is precisely the case that layered media
represent; that is why production geothermal and basin models use finite elements
(or a layer-matching code where the layering is simple enough) rather than series.
The series solution retains its value as a *verification*: a finite-element code can
be checked against a layered series solution on a geometry where both are valid,
which is the standard first test of any new thermal code.
