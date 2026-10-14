# Solutions — 03-12-03 Designing Reusable Model Code: Grids, Operators, Boundaries

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output. Values marked *measured* come from a modified copy with
> the modification stated.

---

## ★1 — The four interfaces

| interface | question it answers |
|---|---|
| `Grid` | what is the mesh, and is it valid? |
| `Operator` | how is a derivative approximated, and at what order? |
| `Boundary` | what happens at the edge, and how much does it reflect? |
| `WaveModel1D` | what equation is being solved, with what time step? |

The point is not the number four, it is that each question has exactly one
owner and therefore exactly one test.

---

## ★2 — Measured operator orders

| operator | nominal | measured (last three doublings) |
|---|---|---|
| centred $\partial_{xx}$ | 2 | 2.0000, 2.0000, 2.0000 |
| five-point $\partial_{xx}$ | 4 | 3.9998, 3.9461, **0.3525** |
| centred $\partial_x$ | 2 | 1.9999, 2.0000, 2.0000 |
| forward $\partial_x$ | 1 | 1.0000, 1.0000, 1.0000 |

The five-point operator collapses at the finest grid (nx = 4096, dx = 2.4e−4)
because its truncation error has fallen to the round-off floor. The floor scales
as $\varepsilon/\Delta x^2$: with $\Delta x = 2.4\times10^{-4}$,
$\Delta x^{-2} = 1.7\times10^{7}$ and
$\varepsilon\Delta x^{-2} = 3.7\times10^{-9}$, comparable to the measured
3.2e−7 error acting through the stencil's coefficients. **Refining past the
floor measures arithmetic, not the method.**

---

## ★3 — Boundary reflection coefficients at $r = 0.5$

| treatment | reflection coefficient |
|---|---|
| rigid ($u = 0$) | 1.017539 |
| naive shift $u(0,n+1)=u(1,n)$ | 0.340320 |
| Reynolds first order | 0.001212 |

The rigid value exceeds 1 because a second reflection arrives inside the 600 s
window. The naive shift is transparent only at $r = 1$; at 1.00 it measures
0.000370. The Reynolds coefficient
$b = (r-1)/(r+1) = -0.333333$ at $r = 0.5$.

---

## ★4 — Why `Grid` is frozen, and the invariants

`@dataclass(frozen=True)` makes the instance's attributes immutable after
construction. A mutable grid allows a run to be started with one mesh and
continued with another: change `dx` mid-run and every derived quantity — the
Courant number, the operator's scaling, the boundary coefficient — is silently
inconsistent with the data already computed. Freezing removes the possibility
rather than testing for it.

Measured invariants:

```
Grid(nx=100, dx=0.0) -> ValueError: dx must be positive, got 0.0
Grid(nx=2, dx=1.0)   -> ValueError: nx must be at least 4, got 2
```

The second exists because a 3-point stencil on fewer than 4 cells overlaps
itself under `np.roll` — the wrap-around makes the operator a different
operator, silently.

---

## ★5 — Units of the boundary condition

$b = (r-1)/(r+1)$ where $r$ is dimensionless, so $b$ is **dimensionless**. The
update

$$u_0^{n+1} = u_1^n + b\left(u_1^{n+1} - u_0^n\right)$$

adds a displacement to a dimensionless multiple of a displacement difference,
so every term has the units of $u$. The dimensional check passes, which is
exactly why the *time-level* bug of ★★8 is invisible to it: passing the wrong
level keeps the units right and changes only which physical state is being
used.

---

## ★★6 — An operator test

```python
import numpy as np

def measure_order(operator, derivative: int, modes: int = 3,
                  refinements: int = 6) -> list[float]:
    errors = []
    for nx in (128 * 2 ** k for k in range(refinements)):
        dx = 1.0 / nx
        x = np.arange(nx) * dx
        k = 2.0 * np.pi * modes
        u = np.sin(k * x)
        analytic = (k * np.cos(k * x) if derivative == 1
                    else -k ** 2 * np.sin(k * x))
        numeric = operator.apply(u, dx)
        errors.append(float(np.sqrt(np.mean((numeric - analytic) ** 2))))
    return [float(np.log2(errors[i] / errors[i + 1]))
            for i in range(len(errors) - 1)]
```

*Measured* for the centred second derivative: orders 2.0000 across all five
refinements, with the last error $4.5\times10^{-8}$ at nx = 4096 — no floor
appears because the second derivative's stencil error is
$\Delta x^2 u''''/12$, whose coefficient is small. *Measured* for the five-point
stencil: the floor appears between nx = 2048 and nx = 4096, at an error of about
$3\times10^{-7}$.

The essential detail is the `derivative` argument. Testing a $\partial_x$
stencil against $-k^2\sin(kx)$ reports order 0 and looks like a broken operator;
it is a broken test.

---

## ★★7 — The indexing error

```python
def apply_broken(u, dx):
    flux = u[1:] - u[:-1]
    div = np.zeros_like(u)
    div[1:] += flux          # div[i] gets flux[i-1]: a BACKWARD difference
    div[:-1] -= flux         # div[i] loses flux[i]
    return div / dx ** 2     # = -(u_{i+1} - 2u_i + u_{i-1})/dx^2
```

*Measured* against the analytic $\partial_{xx}$ of a 3-wavelength sine:

| operator | error |
|---|---|
| centred $\partial_{xx}$ | 1.859e−01 |
| broken | 6.257e+02 |

The broken operator returns minus the right answer, so its error is
$\sim2|{-}k^2\sin|$, i.e. 100 % of the signal.

In a time-stepping run at $r = 0.5$ the growth per step is *measured* at
**2.618034**, matching $(3+\sqrt5)/2$ from lesson 02's analysis of the
sign-flipped Laplacian. The agreement identifies the fault; the magnitude alone
would only have said "something is wrong".

---

## ★★8 — The off-by-one-in-time bug

A one-way (absorbing) condition relates the **current** level $n$ and the
**new** level $n+1$:

$$u_0^{n+1} = u_1^{n} + b\left(u_1^{n+1} - u_0^{n}\right).$$

In the three-level scheme the names are `u_prev` $= u^{n-1}$,
`u_cur` $= u^{n}$, `u_next` $= u^{n+1}$. The buggy version passed
`(u_prev, u_next)`, i.e. levels $n-1$ and $n+1$ — skipping the current level
entirely.

*Measured* reflection coefficients:

| levels passed | reflection coefficient |
|---|---|
| `(u_cur, u_next)` — correct | 0.001212 |
| `(u_prev, u_next)` — buggy | 0.338703 |

The two differ by a factor of 280, and both are dimensionally correct, compile,
and produce a plausible-looking wavefield. Only the measurement distinguishes
them.

---

## ★★9 — Operator error versus solution error

At 8 points per wavelength the operators' own errors differ by a factor of 12,
but the solutions' RMS errors differ by 1.4 %. The reason is that at
$r = 0.5$ with $\Delta t \propto \Delta x$ the **temporal** discretisation error
is second order and dominates: the discrete wave scheme's phase error is
$\Delta\omega = kc(r^2-1)(k\Delta x)^2/24$, which is the same for both operators
because it comes from the time differencing, not the space differencing.

The operators' errors only dominate when the spatial term is larger, which
happens at fewer points per wavelength — the 4-point rows — or when the time
step is chosen independently of $\Delta x$ (e.g. held fixed while $\Delta x$ is
refined, in which case the spatial error dominates at fine grids).

**The general lesson:** when two schemes are compared, the comparison is only
meaningful if the error being measured is the one that dominates. State the
regime.

---

## ★★10 — A signature that would have prevented the bug

```python
class Boundary:
    def apply(self, *, current: np.ndarray, new: np.ndarray) -> None: ...
```

Keyword-only parameters force the call site to name the levels
(`apply(current=u_cur, new=u_next)`), so passing `u_prev` as `current` is a
visible error at the point of the call rather than a silent semantic one. The
cost is verbosity in the inner loop, which is real: this is called once per
time step.

Whether to make the same change to `Operator.apply` — I would not. The
operator takes a single field `(u, dx)` and has no ambiguity about which level
it belongs to; the boundary condition's ambiguity is specific to *time levels*,
and it is the only place where naming earns its keep.

---

## ★★★11 — A sponge layer

```python
class Sponge(Boundary):
    def __init__(self, width: int, strength: float) -> None:
        self.width, self.strength = width, strength
    def apply(self, u_cur, u_next) -> None:
        # damping factor: 1 at the interior edge of the layer, 1-strength at the wall
        ramp = np.linspace(0.0, 1.0, self.width)
        factor = 1.0 - self.strength * ramp ** 2
        u_next[:self.width] *= factor
        u_next[-self.width:] *= factor[::-1]
```

*Measured* reflection coefficients on the demonstration's configuration:

| width (cells) | strength | reflection coefficient |
|---|---|---|
| 10 | 0.05 | 0.0184 |
| 20 | 0.05 | 0.0062 |
| 40 | 0.05 | 0.0021 |
| 40 | 0.10 | 0.00094 |
| 80 | 0.05 | 0.00072 |
| 40 | 0.20 | **0.00041** |

Beating the Reynolds condition's 0.0012 requires a 40-cell layer at strength
0.10, or 20 cells at a higher strength. The cost is geometry: 2 × 40 = 80 extra
cells on a 2000-cell domain is 4 %, but on a 200-cell domain it is 40 % — which
is why sponge layers are used in wave-propagation codes with domains of
hundreds of wavelengths and avoided in small ones.

*Measured* caveat: increasing the strength beyond about 0.2 makes the
reflection rise again, because a strong damping gradient is itself an impedance
contrast. The minimum is a genuine optimum, not monotone in either parameter.

---

## ★★★12 — A second-order absorbing condition

Implementing the second-order (Higdon) family

$$\left(\frac{\partial}{\partial t} + c\frac{\partial}{\partial x}\right)^2 u = 0$$

by the standard finite-difference discretisation and using the same measurement
configuration:

| condition | reflection at $r = 0.5$ |
|---|---|
| Reynolds (first order) | 0.001212 |
| Higdon (second order) | **0.000078** |

A factor of 15 improvement, at the cost of a larger stencil (it needs two
interior points and two previous levels) and a stability bound that is more
restrictive in 2-D and 3-D.

**The criterion I used to decide:** the second-order condition is worth the
complexity when the boundary reflection would otherwise be the dominant error
in the quantity of interest. Here the first-order condition's 0.12 % is already
below the numerical dispersion of a 10-point-per-wavelength grid (2.4 % of
phase per wavelength), so on this problem the extra complexity buys nothing.
Where the interior error is small — a spectral-element code, or a very
well-resolved grid — the boundary becomes the dominant error and second order
is required. **Decide by comparing the boundary's number with the interior's
number, not by counting orders.**

---

## ★★★13 — The heterogeneous medium, and which interface changed

Adding a layered velocity and density requires:

| interface | changed? |
|---|---|
| `Grid` | no |
| `Operator` | **yes** — the Laplacian becomes $\partial_x(\mu\partial_x u)/\rho$, which needs the material arrays |
| `Boundary` | yes, partially — the wave speed at each end is needed for $r$ |
| `WaveModel1D` | yes — velocity and density become arrays, and `dt` is derived from the maximum |

*Measured* validation against the analytic displacement reflection coefficient
$R = (Z_1-Z_2)/(Z_1+Z_2)$:

| $Z_1$ | $Z_2$ | $R$ analytic | $R$ measured | relative error |
|---|---|---|---|---|
| 7.50 | 7.50 | 0.00000 | 0.00038 | — |
| 7.50 | 12.00 | −0.23077 | −0.23070 | 0.032 % |
| 4.00 | 8.00 | −0.33333 | −0.33469 | 0.406 % |
| 15.66 | 8.32 | 0.30609 | 0.30649 | 0.130 % |
| 16.00 | 4.00 | 0.60000 | 0.60046 | 0.076 % |
| 7.50 | 1.50 | 0.66667 | 0.66794 | 0.191 % |

Agreement better than half a per cent across six impedance contrasts, and the
matched case returns essentially zero.

**Which interface did *not* change is the interesting result:** `Grid` did not,
and neither did the boundary *concept* — only its parameters. The operator
changed because the equation changed, which is a change of physics, not of
plumbing. A refactor in which the physics change is confined to one interface is
the evidence that the interfaces were drawn in the right places.

*Note on the sign convention:* the commonly quoted
$(Z_2-Z_1)/(Z_2+Z_1)$ is the **pressure** (stress) reflection coefficient. The
**displacement** coefficient measured here is its negative,
$(Z_1-Z_2)/(Z_1+Z_2)$. This was a measured correction to an initial draft
claim: the first version of the demonstration compared against
$(Z_2-Z_1)/(Z_2+Z_1)$ and reported a relative error of −200 % for every case,
i.e. a sign flip, not a small discrepancy. The free-end check confirms the
displacement convention: at $Z_2 \to 0$ the displacement reflection coefficient
is $+1$ (no sign change), while the pressure coefficient is $-1$.
