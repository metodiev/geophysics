---
id: 14-01-04
title: "Well Hydraulics, Pumping Tests and Aquifer Parameters"
level: advanced
prereqs: ["14-01-03", "14-01-02"]
tags: [hydrology, hydrogeophysics, pumping-test, theis, cooper-jacob, transmissivity, storativity]
---

# Well Hydraulics, Pumping Tests and Aquifer Parameters

A pumping test is the only routine measurement that gives **both** the
transmissivity and the storativity of an aquifer. Everything else in
hydrogeology either gives one of them, or gives a correlated combination. That
power comes from a deliberate experiment: pump at a known rate, watch the head
fall in observation wells, and fit a solution of the flow equation whose
parameters are exactly the quantities you want.

The cost is a list of assumptions longer than in any previous lesson, and a
fitting procedure in which the *window* and the *model* are as important as the
data. This lesson derives the Theis solution, reduces it to the straight-line
method, and measures — on a synthetic test with a stated noise level — how
accurately each parameter is recovered, and what happens when the assumptions
fail.

**All models and data in this module are SYNTHETIC.** The aquifer, the pumping
rates, the step-drawdown pairs and the drawdown series below are invented teaching
values, generated from the stated equations plus a stated noise level. No real
well or pumping test is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Theis solution as the radial diffusion of a head disturbance and
   **compute** drawdown with the exponential integral.
2. **Explain** the dimensionless time $u$ and **state** which physical regime a
   given $(r, t)$ lies in.
3. **Derive** the Cooper-Jacob straight-line form from the small-$u$ expansion, and
   **quantify** the error as a function of $u$.
4. **Invert** a synthetic pumping test for $T$ from the slope and $S$ from the
   intercept, and **report** the recovered values against the known truth.
5. **Quantify** how the choice of fit window changes $T$ and $S$, and explain why
   $S$ is the more fragile of the two.
6. **Separate** aquifer loss from well loss with a step-drawdown test and
   **compute** a well efficiency.
7. **Use** superposition to analyse a recovery test and explain why it gives $T$
   with no assumption about $S$.
8. **State** the Theis assumptions and the diagnostic that reveals each violation.

## Prerequisites

- [14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md)
  — the flow equation, diffusivity $D = T/S$, and the $R/K$ ambiguity that a
  pumping test resolves.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md)
  — $T$, $S$, $S_s$ and the confined/unconfined distinction.

---

## 1. Intuition: a controlled disturbance, read at a distance

Pumping a well lowers the head around it. Far away the disturbance is small and
arrives late; near the well it is large and arrives quickly. The shape of that
arrival curve — drawdown against the logarithm of time — encodes two things:

- **how fast the disturbance travels**: this is $T/S$, the diffusivity;
- **how much water must be moved to lower the head**: this is $S$.

The amplitude of the whole curve sets the product $Q/T$, so the pumping rate
calibrates the vertical scale. The result is that *one* curve determines *two*
parameters. That is why a pumping test is worth the effort, and why it is the only
method in this module with such power.

The physical picture is diffusion, not translation. Nothing travels from the well
to the observation well; the pressure pulse does. In the synthetic test below, the
head disturbance reaches 5 km in 90 days, while a water particle at the same
gradient would need about 1000 years.

## 2. Precise definitions

| Quantity | Symbol | Unit | Meaning |
|---|---|---|---|
| pumping (abstraction) rate | $Q$ | m$^3$ s$^{-1}$ (or m$^3$ d$^{-1}$) | constant during the test |
| drawdown | $s$ | m | $h_0 - h$ at the observation point |
| radial distance | $r$ | m | well to observation point |
| time since pumping began | $t$ | s (or d) | |
| transmissivity | $T$ | m$^2$ s$^{-1}$ | $Kb$ |
| storativity | $S$ | – | dimensionless |
| well function | $W(u)$ | – | $= E_1(u)$ |
| dimensionless time | $u$ | – | $r^{2}S/(4Tt)$ |
| specific capacity | $Q/s_w$ | m$^2$ s$^{-1}$ | a screening number |
| well loss coefficient | $C$ | s$^2$ m$^{-5}$ | non-Darcy loss at the well |
| formation loss coefficient | $B$ | s m$^{-2}$ | $= 2.3/(4\pi T)$ per log cycle |

Note the pair of conventions that must always be stated:

- $Q$ in m$^3$ d$^{-1}$ with $T$ in m$^2$ d$^{-1}$ gives $s$ in metres directly;
  mixing seconds and days is the most common arithmetic error in this lesson.
- $s$ is measured **relative to the pre-pumping head at the same point**, not to a
  regional datum, so a pumping test is insensitive to datum errors and sensitive to
  barometric and tidal drift during the test.

## 3. Derivations

### 3.1 The radial flow equation and the Theis solution

For radial, horizontal, confined flow with a line source at $r = 0$, the flow
equation of [03](03-hydraulic-head-darcy.md) becomes

$$S\frac{\partial s}{\partial t}
= \frac{T}{r}\frac{\partial}{\partial r}\left(r\frac{\partial s}{\partial r}\right),
\qquad s(r,0) = 0, \quad s(\infty,t) = 0,$$

with the pumping rate imposed as a flux at the well:
$\lim_{r\to 0} r\,\partial s/\partial r = -Q/(2\pi T)$. The solution is

$$\boxed{\;s(r,t) = \frac{Q}{4\pi T}\,W(u), \qquad
u = \frac{r^{2}S}{4Tt}, \qquad
W(u) = E_1(u) = \int_u^{\infty}\frac{e^{-x}}{x}\,\mathrm{d}x.}$$

Three structural facts follow directly from the box:

1. $T$ appears once in the prefactor and again inside $u$; $S$ appears **only**
   inside $u$. At a *fixed* $r$, increasing $S$ at fixed $T$ is the same as
   decreasing $t$ — that is the trade-off that makes early-time data poor for $S$.
2. At late time $u \to 0$ and $W(u)$ grows logarithmically, so $s$ grows
   logarithmically. A decade of pumping adds the *same* increment of drawdown,
   forever. For the synthetic test that increment is 0.7916 m per decade.
3. The radius at which a given drawdown occurs grows as $\sqrt{4Tt/S}$: the
   diffusion length of [03](03-hydraulic-head-darcy.md).

**Synthetic evaluation.** $Q = 864\ \mathrm{m^3\,d^{-1}}$,
$T = 200\ \mathrm{m^2\,d^{-1}}$, $S = 3.267 \times 10^{-4}$, $r = 50$ m:

| $t$ (d) | $t$ (h) | $u$ | $W(u)$ | $s$ (m) |
|---|---|---|---|---|
| 0.0020 | 0.048 | $5.105 \times 10^{-1}$ | 0.5473 | 0.1881 |
| 0.0100 | 0.240 | $1.021 \times 10^{-1}$ | 1.8042 | 0.6202 |
| 0.0500 | 1.200 | $2.042 \times 10^{-2}$ | 3.3344 | 1.1463 |
| 0.2500 | 6.000 | $4.084 \times 10^{-3}$ | 4.9276 | 1.6940 |
| 1.0000 | 24.00 | $1.021 \times 10^{-3}$ | 6.3108 | 2.1695 |
| 5.0000 | 120.0 | $2.042 \times 10^{-4}$ | 7.9195 | 2.7225 |
| 10.00 | 240.0 | $1.021 \times 10^{-4}$ | 8.6125 | 2.9608 |

Worked line, $t = 1$ d:

$$u = \frac{50^{2} \times 3.267 \times 10^{-4}}{4 \times 200 \times 1}
= \frac{0.81675}{800} = 1.021 \times 10^{-3},$$
$$s = \frac{864}{4\pi \times 200}\,E_1(1.021 \times 10^{-3})
= 0.3438 \times 6.3108 = 2.1695\ \mathrm{m}.$$

### 3.2 The Cooper-Jacob form, derived and bounded

For small $u$, the exponential integral has the convergent expansion

$$E_1(u) = -\gamma - \ln u + u - \frac{u^{2}}{4} + \cdots,
\qquad \gamma = 0.57721\ldots$$

Dropping terms of order $u$ and using $e^{-\gamma} = 0.5615$:

$$W(u) \approx \ln\frac{e^{-\gamma}}{u} = \ln\frac{0.5615 \times 4Tt}{r^{2}S}
= 2.3026\log_{10}\frac{2.25\,Tt}{r^{2}S},$$

so

$$s \approx \frac{2.3026\,Q}{4\pi T}\log_{10}\frac{2.25\,Tt}{r^{2}S}.$$

Two consequences that define the standard field method:

- A plot of $s$ against $\log_{10} t$ is a **straight line** whose slope per decade
  is $\Delta s = 2.3026Q/(4\pi T)$, giving $T$ with no knowledge of $S$:
  $$T = \frac{2.3026\,Q}{4\pi\,\Delta s}.$$
- The intercept at $s = 0$, call it $t_0$, gives
  $$S = \frac{2.25\,T\,t_0}{r^{2}}.$$

**Measured error of the approximation** (the omitted $+u$ term, evaluated against
the exact $E_1$):

| $u$ | error in $s$ |
|---|---|
| 0.001 | $+0.013\%$ |
| 0.005 | $-0.066\%$ |
| 0.010 | $-0.201\%$ |
| 0.020 | $-0.538\%$ |
| 0.050 | $-1.93\%$ |
| 0.100 | $-5.25\%$ |
| 0.200 | $-15.4\%$ |

The conventional criterion "$u < 0.01$" corresponds to an error under 0.2%. At
$r = 50$ m with these parameters, $u = 0.01$ at $t = 0.102$ d = **2.45 h**, so
earlier data must be excluded. The criterion is a statement about an accepted
error, not a law — say which error you accept.

### 3.3 Superposition and the recovery test

Because the flow equation is linear in $s$, responses add. Stopping a pump after a
duration $t_p$ is the same as adding an injection well of the same rate starting at
$t_p$:

$$s'(r,t) = \frac{Q}{4\pi T}\left[W(u) - W(u')\right],
\qquad u' = \frac{r^{2}S}{4T(t - t_p)},$$

where $s'$ is the **residual drawdown** measured from the extrapolated (or simply
the pre-shut-in) trend. When both $u$ and $u'$ are small,

$$s' \approx \frac{2.3026\,Q}{4\pi T}\log_{10}\frac{t}{t - t_p},$$

so a plot of $s'$ against $\log_{10}[t/(t-t_p)]$ is a straight line of the same
slope as the pumping plot. **The recovery slope gives $T$ and never involves $S$.**
That is why a recovery test is the most robust route to transmissivity, and why it
is routinely run even when the drawdown analysis is compromised.

### 3.4 Well loss, efficiency and specific capacity

The Theis solution describes the aquifer. The well itself adds losses that scale
**quadratically** with rate (non-Darcy flow through the gravel pack, screen and
near-well zone):

$$s_w = BQ + CQ^{2},$$

with $B$ the formation loss coefficient and $C$ the well-loss coefficient. Dividing
by $Q$ gives a straight line in $Q$:
$s_w/Q = B + CQ$, so a **step-drawdown test** at several rates determines $B$ and
$C$ by linear regression, and the **well efficiency** is

$$E = \frac{BQ}{BQ + CQ^{2}} \times 100\%.$$

**Synthetic step-drawdown test**, generated from $B = 3.0 \times 10^{-3}\
\mathrm{d\,m^{-2}}$ and $C = 1.2 \times 10^{-6}\ \mathrm{d^2\,m^{-5}}$ plus 0.02 m
of noise:

| $Q$ (m$^3$ d$^{-1}$) | $s_w$ (m) | $s_w/Q$ (d m$^{-2}$) |
|---|---|---|
| 216 | 0.663 | 0.003068 |
| 864 | 3.534 | 0.004090 |
| 1728 | 8.741 | 0.005058 |
| 2592 | 15.844 | 0.006113 |

Regression recovers $B = 2.883 \times 10^{-3}\ \mathrm{d\,m^{-2}}$ (−3.9%) and
$C = 1.259 \times 10^{-6}\ \mathrm{d^2\,m^{-5}}$ (+4.9%), and the resulting
efficiencies are 91.4%, 72.6%, 57.0% and 46.9% at the four rates. **The aquifer did
not change; only the rate did.** A specific capacity quoted without its rate and
duration is not a property of anything.

## 4. Worked example — a full synthetic pumping test, inverted

**Setup.** Synthetic confined aquifer: $Q = 864\ \mathrm{m^3\,d^{-1}}$,
$r = 50$ m, 40 drawdown readings from 0.01 to 10 d, noise
$\sigma = 5$ mm (a realistic transducer-plus-datum precision). The truth is
$T = 200\ \mathrm{m^2\,d^{-1}}$, $S = 3.267 \times 10^{-4}$.

**Step 1 — validity window.** $u < 0.01$ requires
$t > 25r^{2}S/T = 25(2500)(3.267 \times 10^{-4})/200 = 0.1021$ d, so 26 of the 40
points qualify.

**Step 2 — fit.** Least squares of $s$ on $\log_{10}t$ over those 26 points gives

$$\text{slope} = 0.7902\ \mathrm{m\ per\ decade}, \qquad
\text{intercept} = 2.1706\ \mathrm{m}.$$

**Step 3 — transmissivity.**

$$T = \frac{2.3026\,Q}{4\pi\,\Delta s}
= \frac{2.3026 \times 864}{4\pi \times 0.7902}
= \frac{1989.4}{9.929} = 200.34\ \mathrm{m^2\,d^{-1}},$$

an error of $+0.17\%$ against the truth.

**Step 4 — storativity.** The intercept is where $s = 0$:

$$t_0 = 10^{-\text{intercept}/\text{slope}} = 10^{-2.1706/0.7902}
= 10^{-2.7469} = 1.79 \times 10^{-3}\ \mathrm{d},$$

$$S = \frac{2.25\,T\,t_0}{r^{2}}
= \frac{2.25 \times 200.34 \times 1.79 \times 10^{-3}}{2500}
= 3.230 \times 10^{-4},$$

an error of $-1.13\%$ against $3.267 \times 10^{-4}$. The fit rms is 4.40 mm
against an injected noise of 5.0 mm — the model is not being strained, which is
itself evidence that the test is clean.

**Step 5 — the sensitivity asymmetry, measured.** Repeating the identical analysis
with observation wells at $r = 10$, 25 and 50 m:

| $r$ (m) | $u$ at $t = 0.01$ d | $T$ error | $S$ error |
|---|---|---|---|
| 10 | 0.0041 | $+0.02\%$ | $+0.30\%$ |
| 25 | 0.0255 | $+0.15\%$ | $-0.65\%$ |
| 50 | 0.1021 | $+0.40\%$ | $-1.54\%$ |

Over a five-fold change in radius the $T$ error grows five-fold and the $S$ error
grows twenty-fold. **$S$ is the fragile parameter**: it comes from an intercept
obtained by extrapolating the straight line outside the window in which it was
fitted, while $T$ comes from a slope fitted inside the window.

**Step 6 — recovery check.** After pumping for $t_p = 1$ d, the residual drawdown
falls from 1.335 m at $t = 1.02$ d to 0.036 m at $t = 10$ d. The slope of $s'$
against $\log_{10}[t/(t-t_p)]$ is 0.7821 m per decade, giving
$T = 202.4\ \mathrm{m^2\,d^{-1}}$ (+1.2%) **with no use of $S$ at all**. The 1.2%
bias is the finite-$u'$ error of the logarithmic approximation at the earliest
recovery point, where $u' = 0.051$; restricting the fit to $u' < 0.01$ removes it.
Two independent routes to $T$ agreeing within 1.5% is the strongest evidence a
single-well test can provide.

## 5. Python demonstration

`code/well_hydraulics_demo.py` prints all of the above with units. It:

1. tabulates $u$, $W(u)$ and $s$ from the Theis solution (using
   `scipy.special.exp1`) and reports the drawdown increment per decade;
2. measures the Cooper-Jacob error against $u$ and locates the $u<0.01$ time;
3. generates a 40-point synthetic test with 5 mm noise, fits it, and recovers
   $T = 200.34\ \mathrm{m^2\,d^{-1}}$ and $S = 3.230 \times 10^{-4}$;
4. repeats the fit at three radii to isolate the fragility of $S$;
5. generates a four-rate step-drawdown test and recovers $B$ and $C$ to about 5%;
6. tabulates specific capacity against duration and against $S$ and $T$;
7. compares three definitions of radius of influence and shows that the
   Cooper-Jacob zero crossing lies inside the 0.1 m contour of the true solution;
8. analyses a 1 d recovery test by superposition and recovers $T$ without $S$.

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python well_hydraulics_demo.py
```

## 6. Units and dimensional analysis

| Combination | Result | Check |
|---|---|---|
| $Q/T$ | m | $(\mathrm{m^3\,d^{-1}})/(\mathrm{m^2\,d^{-1}})$ |
| $Q/(4\pi T)$ | m | the prefactor is a length |
| $u = r^{2}S/(4Tt)$ | – | $\mathrm{m^2 \cdot 1 / (m^2\,d^{-1} \cdot d)}$ |
| $T = 2.3026Q/(4\pi \Delta s)$ | m$^2$ d$^{-1}$ | m$^3$ d$^{-1}$ / m |
| $S = 2.25 T t_0/r^{2}$ | – | $(\mathrm{m^2\,d^{-1}} \cdot \mathrm{d})/\mathrm{m^2}$ |
| $B$ | d m$^{-2}$ | $s_w/Q$ |
| $C$ | d$^2$ m$^{-5}$ | $s_w/Q^2$ |

Every one of these carries a per-day or a per-second convention invisibly. Write
the units of $Q$ and $T$ on every plot axis: a factor of 86,400 hides in this
lesson more often than any physics error.

## 7. Assumptions and regime of validity

The Theis solution assumes all of the following. Each has a diagnostic, and each
diagnostic is a departure from the straight line or the shape you expect.

1. **The aquifer is homogeneous, isotropic, of uniform thickness and infinite in
   extent.** Diagnostic: a straight line in $s$ vs $\log t$ that bends, or two
   wells at equal $r$ giving different $T$. Boundaries appear as a doubling of the
   slope (a no-flow boundary) or a flattening (a constant-head boundary).
2. **Constant pumping rate from $t = 0$.** Diagnostic: a rate record, not an
   assumption. Variable rates must be handled by superposition.
3. **The well fully penetrates the aquifer.** Partial penetration concentrates
   flow near the screened interval, adding an apparent extra drawdown that is
   absorbed into $C$ or into $S$.
4. **Water is released instantaneously and in proportion to head change** (the
   definition of $S$). Diagnostic: delayed yield — in an unconfined aquifer the
   $s$-$\log t$ curve has an $S$-shaped break as gravity drainage lags, so an early
   fit gives $S \approx S_s b$ (small) and a late fit gives $S \approx S_y$ (large).
   **The single largest source of nonsense storativities.**
5. **No leakage from adjacent layers.** Diagnostic: the curve flattens to a
   steady drawdown at late time. Fitting Theis to a leaky response returns a
   too-large $S$ (the flattening is attributed to storage).
6. **No wellbore storage.** Diagnostic: an early unit-slope segment in
   $\log s$ vs $\log t$, i.e. the well itself draining.
7. **$S$ and $T$ constant in time and independent of head.** Fails where the
   aquifer dewaters (unconfined, or a confined unit whose head falls below the
   top of the screen) or where stress changes alter $K$.
8. **Laminar flow in the aquifer** (see [03](03-hydraulic-head-darcy.md)); inside
   and beside the well, the non-Darcy loss is captured by $C$, not by the aquifer.

## 8. What a pumping test cannot do

- **It cannot resolve a sharp $K$ contrast at its own scale.** $T$ is an
  effective, large-scale, directionally averaged property; the same test in a
  fractured aquifer yields a value that depends on whether the pumped well
  intersects a fracture.
- **It cannot give a reliable $S$ from early data alone,** as Section 4
  quantifies.
- **It cannot separate $T$ from $S$ if the observation well is too close or too
  far.** At small $r$ the curve is over before the straight-line regime; at large
  $r$ the drawdown is within noise. There is an optimal radius, and it is a
  design decision: with the parameters above, a 50 m well reaches $u<0.01$ in
  2.5 h and produces 2.2 m of drawdown in a day, which is near ideal.
- **It cannot see the geometry.** A test says nothing about where the sand body
  is; that is the job of the seismic and ERT methods in
  [module 14-02](../02-hydrogeophysics-methods/README.md). Combining the two is
  how a calibrated model is built.

## Mastery checkpoint

A synthetic constant-rate test pumps $Q = 1200\ \mathrm{m^3\,d^{-1}}$ from a
confined aquifer with an observation well at $r = 80$ m. The fit over the valid
window gives a slope of 0.55 m per decade and an intercept of 2.20 m.

**(a)** Compute $T$. **(b)** Compute $t_0$ and $S$. **(c)** Verify that the fit
window is valid by computing $u$ at $t = 1$ d. **(d)** State what happens to the
recovered $T$ and $S$ if a no-flow boundary is reached at 150 m during the test.
**(e)** The same well is retested after rehabilitation and the slope is unchanged
but $s_w$ at the same rate fell by 0.8 m. What changed, and how would you report
it?

## Common pitfalls

1. **Mixing days and seconds.** $Q$ and $T$ must share a time unit; the result is
   otherwise wrong by 86,400.
2. **Fitting the early curved part.** It biases $S$ low and is invisible in a
   "good" $R^2$; always report the window and the $u$ criterion.
3. **Reporting $S$ from an unconfined test without checking for delayed yield.**
   The early-time value is $S_s b$, often two orders of magnitude below $S_y$.
4. **Quoting a specific capacity as $T$.** It depends on rate, duration,
   observation point and $S$, as the demonstration shows.
5. **Treating the radius of influence as physical.** Three conventions give three
   answers differing by more than a factor of two.
6. **Ignoring leakage.** A flattening late-time curve fitted with Theis returns a
   large, wrong $S$.
7. **Reporting $T$ and $S$ without an uncertainty.** A slope and an intercept from
   a noisy line have correlated errors; propagate them (see
   [01-13-09 Error Propagation](../../01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md)).

## Related modules

- [03 Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md)
  — the flow equation and the diffusivity this lesson measures.
- [06 The Unsaturated Zone](06-unsaturated-zone.md) — the physics behind delayed
  yield in an unconfined test.
- [02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — the
  methods that supply the geometry a pumping test cannot see.
- [05 Groundwater Chemistry and Salinity](05-groundwater-chemistry.md) — the water
  quality a pumping test must be paired with to make a resource statement.

## Code and exercises

- Demonstration: [`code/well_hydraulics_demo.py`](code/well_hydraulics_demo.py)
- Exercises: [`exercises/04-well-hydraulics-exercises.md`](exercises/04-well-hydraulics-exercises.md)
- Worked solutions: [`exercises/04-well-hydraulics-solutions.md`](exercises/04-well-hydraulics-solutions.md)
