# Solutions — 16-06-03 Abrupt Climate Change and Tipping Elements

> Read after attempting the exercises. Lesson:
> [03 Abrupt Climate Change and Tipping Elements](../03-abrupt-climate-change.md).

---

## ★1 — Verifying a steady solution

With $q = -0.0522$, so $|q| = 0.0522$ and $H = 0.10$:

$$\frac{\Delta T}{20} = \frac{1}{1+2|q|} = \frac{1}{1+0.1044} = 0.90547,$$

$$\frac{\Delta S}{2} = \frac{H}{2|q|} = \frac{0.10}{0.1044} = 0.95785,$$

$$G = 0.90547 - 0.95785 = -0.05238.$$

Residual: $|G - q| = |{-0.05238} - ({-0.0522})| = 1.8\times10^{-4}$, i.e.
$0.35\%$ of the root's magnitude — consistent with the root being reported to
four decimals. The steady solutions of the model are the fixed points of
$q\mapsto G(|q|)$; a residual of this size is a rounding artefact, not an error.

---

## ★2 — Branch temperatures at $Q = 400$

Warm branch:

$$T = \frac{0.70 \times 400 - 210}{2} = \frac{280-210}{2} = 35.0\
\mathrm{{}^{\circ}C}.$$

Self-consistency requires $T > -10\ \mathrm{{}^{\circ}C}$: $35.0 > -10$. ✔

Cold branch:

$$T = \frac{0.38 \times 400 - 210}{2} = \frac{152-210}{2} = -29.0\
\mathrm{{}^{\circ}C}.$$

Self-consistency requires $T \le -10\ \mathrm{{}^{\circ}C}$:
$-29.0 \le -10$. ✔

Both branches are self-consistent, so $Q = 400\ \mathrm{W\,m^{-2}}$ lies inside
the bistable range (which the demonstration brackets as
$[271.5, 499.5]\ \mathrm{W\,m^{-2}}$).

---

## ★3 — Warm-branch limit

$$\frac{0.70Q - 210}{2} = -10
\quad\Longrightarrow\quad
0.70Q - 210 = -20
\quad\Longrightarrow\quad
Q = \frac{190}{0.70} = 271.43\ \mathrm{W\,m^{-2}}.$$

Reducing the forcing below about $271.4\ \mathrm{W\,m^{-2}}$ leaves only the cold
branch: at that point the warm solution ceases to exist rather than becoming
unstable, which is the defining behaviour of a fold (saddle-node) bifurcation.

---

## ★4 — Threshold sensitivity to a closure parameter

$$\frac{\Delta Q}{\Delta\alpha_{\text{ice}}}
= \frac{678.5-379.5}{0.72-0.50} = \frac{299.0}{0.22}
= 1359\ \mathrm{W\,m^{-2}}\ \text{per unit albedo},$$

i.e. $13.59\ \mathrm{W\,m^{-2}}$ per $0.01$ of albedo. A closure parameter that
cannot be measured to better than a few hundredths therefore moves the modelled
threshold by tens of watts per square metre. The lower edge is insensitive
(it depends only on the warm albedo and the threshold), so the *width* of the
bistable range is what the closure controls — an asymmetry worth noting when
quoting a single "tipping point".

---

## ★5 — Why the middle solution is unstable

The flow in the salinity equation is
$\mathrm d\Delta S/\mathrm dt = -2|q|\Delta S + 2H$, and the circulation responds
to $\Delta S$ through $q = \Delta T/\Delta T_{\text{ref}} -
\Delta S/\Delta S_{\text{ref}}$: a larger $\Delta S$ makes $q$ more negative.
Around a steady state, a small increase in $\Delta S$ therefore increases $|q|$,
which strengthens the transport out of the salinity anomaly — a stabilising
feedback. The sign of the *net* effect depends on whether the transport term
outweighs the forcing term, and it changes between the outer and the middle roots;
for the middle root the net effect is destabilising.

**Numerical test.** Perturb the steady state by a small amount (for example
$\pm1\%$ in $\Delta S$), integrate, and compare the sizes of the perturbation at
$t$ and $2t$: growth indicates instability, decay indicates stability. Doing this
for the three roots at $H = 0.15$ shows the outer two decaying and the middle one
growing — no eigenvalues required.

---

## ★6 — The mean of two branches

$$\frac{+14.09 + (-40.35)}{2} = -13.13\ \mathrm{{}^{\circ}C}.$$

$-13.13\ \mathrm{{}^{\circ}C}$ is not a steady solution: at
$Q = 340.25\ \mathrm{W\,m^{-2}}$ the only steady solutions are $+14.09$ and
$-40.35\ \mathrm{{}^{\circ}C}$ (and an unstable intermediate one). The mean lies
in the gap between two branches, where the model has no state at all. It is a
number computed from two incompatible states, not an expected temperature —
and the same objection applies to any ensemble mean when members occupy different
branches.

---

## ★7 — Bifurcation or artefact? (specification)

**Observable to vary.** The control parameter (here $H$), in small steps, both
increasing and decreasing, with the state carried over from the previous step
(continuation). A genuine fold produces a jump on the forward sweep at one
parameter value and a jump back at a *different* value on the reverse sweep: the
two-sweep signature of hysteresis.

**Diagnostic to monitor.** The state variable and, if available, the number of
steady solutions found by root finding at each parameter value. Plotting the
forward and backward branches together reveals a loop for a fold.

**What indicates an artefact.** (i) The jump moves when the time step, the grid or
the solver tolerance is changed. (ii) The forward and backward sweeps coincide
(no hysteresis). (iii) The jump coincides with a known numerical limit such as a
CFL boundary, or with a discontinuity introduced by a diagnostic threshold in the
output rather than in the state. (iv) The state after the jump violates a
conservation law the model is supposed to respect.

A useful additional test is to start from several different initial conditions at
the same parameter value inside the suspected bistable range: if two different
steady states are reached, the bistability is real.

---

## ★8 — Critique of a threshold prediction

**What the statement reports.** A property of a model: for that model, with those
closures, that forcing history and that initial condition, a transition occurs at
$Z$ kelvin of global-mean warming. It is a true statement about the model.

**What additional information is needed for a scientific claim about the Earth.**

1. **Validation of the process.** Evidence that the mechanism the model uses for
   the transition is the mechanism that operates in the real component, tested on
   an independent observable.
2. **Closure uncertainty.** The threshold must be reported as a range over the
   plausible closures — the demonstration shows the same model moving its
   threshold by $13.59\ \mathrm{W\,m^{-2}}$ per $0.01$ of one albedo parameter.
3. **Forcing definition.** Which warming metric, over what period, at what
   spatial scale, and with what forcing pathway; different definitions give
   different thresholds.
4. **Rate dependence.** Whether the threshold depends on how fast the forcing is
   applied; if so, the statement needs a rate as well as a magnitude.
5. **Model structure.** Whether the prediction is robust across independent
   models or is a feature of one model family.
6. **Reversibility.** Whether the transition reverses on the same pathway, which
   changes its practical significance entirely.

Without at least (1), (2) and (5), the statement should be phrased as "this model
transitions at $Z$", with the model's closures stated alongside — which is a
useful prediction, but a different one.
