# Solutions — 03-12-01 A 1-D Finite-Difference Solver from Scratch

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. Values marked *measured* come from a modified copy
> with the modification stated.

---

## ★1 — Deriving the second difference

$$u_{i+1} = u_i + \Delta x\,u' + \frac{\Delta x^2}{2}u''
+ \frac{\Delta x^3}{6}u''' + \frac{\Delta x^4}{24}u'''' + O(\Delta x^5),$$

$$u_{i-1} = u_i - \Delta x\,u' + \frac{\Delta x^2}{2}u''
- \frac{\Delta x^3}{6}u''' + \frac{\Delta x^4}{24}u'''' + O(\Delta x^5).$$

Adding cancels the odd derivatives:

$$u_{i+1}+u_{i-1} = 2u_i + \Delta x^2 u'' + \frac{\Delta x^4}{12}u'''' + O(\Delta x^6),$$

so

$$u'' = \frac{u_{i+1}-2u_i+u_{i-1}}{\Delta x^2}
- \underbrace{\frac{\Delta x^2}{12}u''''}_{\text{leading error}} + O(\Delta x^4).$$

The leading error coefficient is $\Delta x^2/12$ multiplying the fourth
derivative, which is why halving $\Delta x$ quarters the error.

---

## ★2 — Dimensions

$$[r] = \frac{[\mathrm{m\,s^{-1}}][\mathrm{s}]}{[\mathrm{m}]} = 1,$$

and $r^2(u_{i+1}-2u_i+u_{i-1})$ has the units of $u$ because $r^2$ is
dimensionless. Equivalently, $r^2\Delta x^2 u_{xx} = (c\Delta t)^2u_{xx}$,
which has units $\mathrm{m^2\,s^{-2}\cdot m^{-1}} = \mathrm{m}$, the units of
$u$ if $u$ is a displacement.

The demonstration holds $r = 0.5$ throughout the convergence study, and uses
$r = 1.0$ for the exactness test.

---

## ★3 — The consistent first step

For $u_t = 0$ at $t = 0$, expand $u^{1} = u(\Delta t)$:
$u(\Delta t) = u^0 + \Delta t\,u_t + \frac{\Delta t^2}{2}u_{tt} + O(\Delta t^3)$,
and $u_{tt} = c^2u_{xx}$, so

$$u_i^1 = u_i^0 + \frac{\Delta t^2}{2}c^2 u_{xx}\big|_i^0
= u_i^0 + \tfrac12 r^2\left(u_{i+1}^0 - 2u_i^0 + u_{i-1}^0\right).$$

Using $u^{-1} = 0$ instead makes the scheme's implied initial velocity
$u_t \approx (u^0 - 0)/\Delta t = u^0/\Delta t$, which is enormous. The
measurement that shows the damage: the $k = 0$ mode of the three-level scheme
satisfies $u^{n+1} = 2u^n - u^{n-1}$, whose solution with $u^{-1} = 0$,
$u^0 = 1$ is $u^n = n+1$ — **linear growth without limit**, from a scheme that
is otherwise stable.

---

## ★4 — Measured orders

| test | measured order | comment |
|---|---|---|
| travelling wave, space–time RMS | **2.0048 → 2.0001** | the scheme's true order |
| standing mode, error at $t = 1.0$ s | **4.0011 → 4.0000** | an artefact of when the error is sampled |

The standing-mode number is larger because the leading error is a *phase*
error, so the amplitude error at an instant when the mode is at an extremum is
the square of the phase error — fourth order for a second-order scheme. The
scheme has not become fourth order; the metric has become blind to the leading
term.

---

## ★5 — Energy

$$E^n = \frac{1}{2}\sum_i \left(\frac{u_i^{n+1}-u_i^n}{\Delta t}\right)^2\Delta x
+ \frac{c^2}{2}\sum_i \frac{u_{i+1}^{n+1}-u_i^{n+1}}{\Delta x}
\frac{u_{i+1}^{n}-u_i^{n}}{\Delta x}\Delta x .$$

Measured over 2000 steps: initial $1.252531\times10^{1}$, final
$1.252531\times10^{1}$, relative drift $+4.219\times10^{-15}$. Machine epsilon
is $2.221\times10^{-16}$, so the drift is about 19 ulp accumulated over 2000
steps — exact conservation to round-off.

---

## ★★6 — Deriving the apparent order 4

For a single spatial mode the discrete solution is
$u_i^n = \cos(\omega_{\text{num}}n\Delta t)\sin(kx_i)$ with

$$\omega_{\text{num}} = \frac{2}{\Delta t}\arcsin\!\left(r\sin\frac{k\Delta x}{2}\right)
= kc\left[1 + \frac{(r^2-1)(k\Delta x)^2}{24} + O(\Delta x^4)\right].$$

The phase error is therefore

$$\delta\phi = (\omega_{\text{num}}-kc)\,t = O(\Delta x^2).$$

At $t$ where the exact solution is at an extremum, the computed solution is
$\cos(\delta\phi)$ times the same extremum, so the absolute error is
$|1 - \cos\delta\phi| \approx \delta\phi^2/2 = O(\Delta x^4)$.

The scheme is second order; the *metric* at that instant is fourth order. At an
instant where the exact solution crosses zero the error is
$\sin(\delta\phi) = O(\Delta x^2)$ and the measured order returns to 2 — which
is why the time-averaged and space-averaged metric in the demonstration is
fourth order only for the standing mode and second order for the travelling
wave.

---

## ★★7 — Exactness versus the degenerate mode

Both statements are true and they concern different initial conditions.

- The **travelling wave** launched with the exact solution at $t = 0$ and
  $t = \Delta t$ has almost all its energy at wavenumbers below $k\Delta x = \pi$,
  where the dispersion relation at $r = 1$ gives $\omega = kc$ exactly. Error
  $3.1\times10^{-15}$.
- The **$2\Delta x$ mode with $u_t = 0$** sits exactly at $k\Delta x = \pi$,
  where the two roots of the stability polynomial coincide at $G = -1$. The
  amplification matrix is defective, and the exact initial condition cannot be
  represented in the eigenspace; the residual grows linearly, $2n-1$.

The growth requires **both** $r = 1$ exactly **and** $u_t = 0$ **and** the
grid's shortest wavelength. Since $k\Delta x = \pi$ is a single point in a
continuum and $r = 1$ is a single value, the pathology has measure zero. It is
worth knowing because a diagnostic that excites the sawtooth (for example a
random initial condition, which contains all wavenumbers) will find it.

---

## ★★8 — Phase-speed deficit at 5 points per wavelength

Interpolating between 8 points ($k\Delta x = 0.7854$, deficit 2.39 %) and
4 points ($k\Delta x = 1.5708$, deficit 11.25 %): at 5 points,
$k\Delta x = 2\pi/5 = 1.2566$, which is $0.80$ of the way along the interval,
giving a deficit of about **7.5 %**.

Practical rule: **use at least ten points per wavelength for waveform
modelling; five is the absolute floor and costs several per cent of phase
error per wavelength travelled.** For a 100-wavelength propagation path, a
2.4 % phase error per wavelength is 2.4 wavelengths of accumulated error — the
waveform is destroyed even though the scheme is stable.

---

## ★★9 — The naive energy

*Measured*: defining the potential term with the gradient at level $n$ only,

$$E^n_{\text{naive}} = \frac{1}{2}\sum_i \left(\frac{u_i^{n+1}-u_i^n}{\Delta t}\right)^2\Delta x
+ \frac{c^2}{2}\sum_i \left(\frac{u_{i+1}^{n}-u_i^{n}}{\Delta x}\right)^2\Delta x,$$

the energy decays by 99.94 % over 401 steps: initial $2.005\times10^4$, final
$1.253\times10^1$.

The apparent damping is a property of *the diagnostic*, not the scheme. The
naive potential energy uses the gradient at level $n$ while the kinetic term
uses the velocity at $n+1/2$; the two are not in phase, and their sum is not
conserved. The correct form pairs the gradient at $n$ with the gradient at
$n+1$, which is what makes the product symmetric under time reversal. The
scheme is time-reversible by construction (swap $n+1$ and $n-1$ and the update
is unchanged), so any *correctly staggered* energy must be exactly conserved.

---

## ★★10 — Why the error rises past $\Delta x \approx 8\times10^{-5}$

At that spacing the discretisation error has fallen below the round-off floor,
and further refinement only adds operations. The accumulated round-off error
grows with the number of floating-point operations, which scales as
$n_{\text{steps}} \sim 1/\Delta x$ and $n_{\text{cells}} \sim 1/\Delta x$, so
the floor grows roughly as $\Delta x^{-1/2}$ to $\Delta x^{-1}$ depending on
how the errors accumulate.

Measured: $6.2027\times10^{-13}$ at $nx = 12800$ (25600 steps),
$4.1569\times10^{-13}$ at $n x = 25600$ (51200 steps) — a drop that stops —
and $1.9805\times10^{-12}$ at $nx = 51200$ (102400 steps), a rise by a factor
of 4.8 for a doubling of the number of steps. If the error accumulated as
$\sqrt{N}$, a doubling would give $\sqrt2 = 1.41$; as $N$, 2.0. The measured
4.8 is larger than either, which is consistent with the *discretisation* error
having stopped falling and the sum of two comparable terms fluctuating rather
than growing monotonically. The honest statement is: **the error stops
decreasing and starts to fluctuate at the few-times-$10^{-13}$ level; the
optimum grid is where the discretisation curve meets that floor, and beyond it
refinement is not a strategy.**

---

## ★★★11 — Contamination of the Fourier-phase estimator

*Measured* with the complex-mode estimator (initial state
$u^0 = \mathrm{e}^{\mathrm{i}kx}$, $u^1 = \mathrm{e}^{\mathrm{i}k(x-c\Delta t)}$):

| $k\Delta x$ | points/$\lambda$ | measured deficit | theory | contamination |
|---|---|---|---|---|
| 0.049 | 128 | 0.0076 % | 0.0075 % | 0.0001 % |
| 0.393 | 16 | 0.5410 % | 0.4831 % | 0.058 % |
| 0.785 | 8 | 2.3913 % | 1.9458 % | 0.45 % |
| 1.257 | 5 | 4.8954 % | 4.4263 % | 0.47 % |
| 1.571 | 4 | 11.2459 % | 7.9786 % | 3.27 % |
| 2.332 | 2.7 | 24.596 % | 18.084 % | 6.5 % |

The contamination rises from a thousandth of a per cent at 128 points per
wavelength to 6.5 % at 2.7. Its cause is that the initial condition is not an
exact eigenvector of the discrete scheme: because the scheme's $\omega$ differs
from $kc$, the state contains both discrete roots, and the tracked Fourier
coefficient is their sum. The two roots have equal magnitude, so the
contamination does not decay.

**Is the estimator usable above $k\Delta x = 1$?** Marginally. At $k\Delta x =
1.257$ the contamination is 0.47 %, which is 10 % of the effect being measured;
at $k\Delta x = 1.571$ it is 3.27 %, which is 41 % of the effect. The
defensible rule is: **above $k\Delta x \approx 1$, do not quote a measured phase
speed without also quoting the estimator, because the measurement and the
contamination are of the same order.** The cleaner alternative is to excite one
root exactly, which requires knowing $\omega$ in advance — and that is circular
unless the eigenvector is constructed from the recursion's characteristic
polynomial, which is itself derived from the dispersion relation.

---

## ★★★12 — The fourth-order five-point stencil

*Measured* with
$\partial_{xx} \approx (-u_{i-2}+16u_{i-1}-30u_i+16u_{i+1}-u_{i+2})/(12\Delta x^2)$:

| quantity | centred 3-point | five-point | 
|---|---|---|
| operator order (measured) | 2.0000 | 3.9998 |
| stability limit $r_{\max}$ | 1.0000 | **0.8944** |
| order in the wave solve | 2.00 | 2.00 |

Two results worth stating carefully.

**The stability limit is not 1.** The five-point Laplacian has eigenvalue
$-5/\Delta x^2$ at the sawtooth wavenumber rather than $-4/\Delta x^2$, so the
wave scheme is stable only for $r \le 2/\sqrt5 = 0.8944$. Measured by scanning
$r$: growth appears between $r = 0.894$ and $r = 0.895$, and the growth rate at
$r = 0.90$ matches the von Neumann prediction.

**The wave solve does not improve to order 4.** The *spatial* operator is
fourth order, but the temporal discretisation is still second order, and
because the convergence study refines $\Delta t \propto \Delta x$ the total
error stays second order. To gain order in time you need a higher-order
time-stepping scheme; improving the stencil alone buys accuracy at a *fixed*
$\Delta t$, not order.

**Points per wavelength at which the two agree:** *measured* at
$nx = 256$ with a single mode, the two schemes give the same space–time RMS
error at about **14 points per wavelength**. Below that the five-point stencil
is better; above it the temporal error dominates both equally.

---

## ★★★13 — A worked specification for a 1 Hz surface wave

Target: a 1 Hz Rayleigh wave crossing a 100 km basin, wavespeed 3 km/s.

- **Wavelength:** $\lambda = v/f = 3/1 = 3$ km.
- **Grid spacing (10 points per wavelength):** $\Delta x = 0.3$ km.
- **Number of cells:** 100 km / 0.3 km = 334 cells; add absorbing regions of
  20 cells at each end → 374, round to **400**.
- **Time step (CFL 0.5):** $\Delta t = 0.5 \times 0.3\ \mathrm{km} / 3\
  \mathrm{km\,s^{-1}} = 0.05$ s.
- **Number of steps for the wave to cross:** $100/3 = 33.3$ s of travel, so
  667 steps; add the source's own duration → **1000** steps.
- **Memory:** one array of 400 `float64` = 3.2 kB; three time levels = 9.6 kB.
- **Operations:** $1000 \times 400 \times 5$ flops $\approx 2\times10^6$ —
  trivial.

Every assumption is explicit: 10 points per wavelength (from the dispersion
table), CFL 0.5 (from lesson 02), 20 cells of absorbing boundary (from lesson
03's measured reflection), and a homogeneous wavespeed. Change any of them and
the specification changes. The value of writing it down is that the numbers are
all derived from measured properties of the scheme rather than chosen because
they look round.
