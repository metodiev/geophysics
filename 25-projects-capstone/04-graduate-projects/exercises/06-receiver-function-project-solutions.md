# Solutions — 25-04-06 Project: Crustal Structure from Receiver Functions

Reference solutions. Every number below is printed by
[`code/receiver_function_demo.py`](../code/receiver_function_demo.py); all data are
**SYNTHETIC**.

## ★1. The three delay times

With $\eta_p = \sqrt{V_p^{-2}-p^{2}}$ and $\eta_s = \sqrt{V_s^{-2}-p^{2}}$:

$$t_\text{Ps} = H(\eta_s-\eta_p),\qquad
t_\text{PpPs} = H(\eta_s+\eta_p),\qquad
t_\text{PpSs+PsPs} = 2H\eta_s .$$

Ps is the upgoing S leg minus the downgoing P leg — a *difference* of slownesses.
PpPs is the P leg down and up plus the S leg up — a *sum*. PpSs+PsPs is two S legs
and no P leg, hence twice $\eta_s H$. All sharing the same $H$, the three
combinations $\eta_s-\eta_p$, $\eta_s+\eta_p$, $2\eta_s$ fix $\eta_p$, $\eta_s$ and
$H$ separately: three independent equations, three unknowns.

For the demonstration's model ($H = 35.0$ km, $V_p = 6.30$, $V_s = 3.600$,
$p = 0.060$):

$$\eta_p = \sqrt{0.0251953 - 0.0036} = 0.146954,\qquad
\eta_s = \sqrt{0.0771605 - 0.0036} = 0.271220,$$
$$t_\text{Ps} = 35.0\,(0.271220-0.146954) = 4.3493\ \mathrm{s}\ \checkmark$$

matching the printed value, and with
$t_\text{PpPs} = 14.6361\ \mathrm{s}$,
$t_\text{PpSs+PsPs} = 18.9854\ \mathrm{s}$.

## ★2. Delay times for $H = 30$ km, $V_p = 6.00$, $V_p/V_s = 1.80$, $p = 0.060$ s/km

$V_s = 6.00/1.80 = 3.333333\ \mathrm{km\,s^{-1}}$.

$$\eta_p = \sqrt{1/36 - 0.0036} = \sqrt{0.0241778} = 0.155492,$$
$$\eta_s = \sqrt{1/11.1111 - 0.0036} = \sqrt{0.0864} = 0.293938 .$$

| phase | computation | time (s) |
|---|---|---|
| Ps | $30\,(0.293938-0.155492)$ | $4.1534$ |
| PpPs | $30\,(0.293938+0.155492)$ | $13.4829$ |
| PpSs+PsPs | $2 \cdot 30 \cdot 0.293938$ | $17.6363$ |

The ordering Ps < PpPs < PpSs+PsPs holds for every physically admissible model,
which is why the stacking windows are defined in that order.

## ★3. Independence and what two phases leave undetermined

Each delay time has the form $H f(k)$: it is linear in $H$ for fixed $k$, so a
single phase defines a **hyperbola** $t = H f(k)$ in the $(H,k)$ plane, not a point.
Stacking two phases intersects two hyperbolas, which generally still leaves a
one-parameter family of solutions when the two $f(k)$ are close; stacking all three
intersects a third hyperbola with a *different* $f(k)$ and pins the point. The
method works because the Ps, PpPs and PpSs+PsPs hyperbolas cross at a large angle —
that angle is the conditioning.

## ★4. The half-maximum region as resolution

Width $= 46.75 - 24.75 = 22.00\ \mathrm{km}$, i.e. $\pm 11.0\ \mathrm{km}$, or
$22.00/0.25 = 88$ grid steps. The grid step is a *search* parameter; the
half-maximum region is the *resolution*. Reporting $H = 35.00\ \mathrm{km}$ to two
decimals is only meaningful with the grid step and the half-maximum region beside
it, and the honest statement is $H = 35 \pm 11\ \mathrm{km}$ for this noise level
and this filter. A real study narrows it by stacking many stations and by using
sharper arrivals, never by refining the grid.

## ★5. Why exact recovery is not accuracy

The synthetic receiver function was built at the same ray-theoretical arrival times
the stack searches for, so the grid peak lands on the generating model by
construction: the demonstration tests the *implementation of the method*, not the
method's agreement with the Earth. What it does establish is (i) the trade-off is
real and phase-dependent — the single-phase peaks are $28.50/1.925$,
$36.75/1.630$ and $23.50/2.000$, each far from the true pair; (ii) the stack's
half-maximum region is broad even under ideal conditions; and (iii) the assumed
$V_p$ propagates one-for-one into $H$. Those are properties of the estimator, and
they transfer to real data unchanged.

## ★6. A $5\%$ error in the assumed $V_p$

$H$ scales with the assumed $V_p$: at small $p$,
$\eta_s-\eta_p \approx (V_s^{-1}-V_p^{-1}) = (V_p/k)^{-1}-V_p^{-1}
= (k-1)/V_p$, so $t \propto H/V_p$ and $H_\text{est} = H_\text{true}
V_p^\text{(assumed)}/V_p^\text{(true)}$. With the true $V_p$ $5\%$ lower:

$$H_\text{est} = \frac{35.0}{0.95} = 36.8\ \mathrm{km},$$

about $5\%$ (strictly $5.26\%$) too thick. The ratio $k = V_p/V_s$ is a
*slowness ratio* and is insensitive to the velocity scale at small $p$, so nearly
the whole error lands in $H$: a $V_p$ error inflates the crust and leaves the
compositional proxy almost untouched. This is why the assumed $V_p$ must be printed
with the thickness, and why an independent $V_p$ — or an inversion that measures
$V_s$ directly — is the only cure.

## ★★★7. A study that removes the assumed $V_p$

**Goal.** Determine $H$ and $V_p/V_s$ (equivalently $V_s$) such that no assumed
$V_p$ enters the answer.

**Additional observations, and what each measures.**

1. **Surface-wave dispersion** (Rayleigh phase/group velocity, 5–40 s, from ambient
   noise or earthquakes) measures the absolute $V_s(z)$ profile. It is independent
   of $V_p$ to first order and constrains $H$ and the mean crustal $V_s$ directly.
2. **Receiver functions** (this project) measure the *sharpness* and *depth
   placement* of the Moho, i.e. the impedance and velocity contrasts at depth, but
   only through the ratio $k$.
3. **P-wave refraction or a nearby borehole/well-log $V_p$** fixes the velocity
   scale that H-K must otherwise assume; if no such measurement exists, the joint
   dispersion + RF inversion supplies the absolute $V_s$ instead and $V_p$ becomes
   an output to be checked for plausibility.

**Why the combination removes the ambiguity.** H-K's trade-off is a family of
$(H, k)$ pairs that reproduce the same three delay times; dispersion breaks it
because a $V_s(z)$ that keeps the delay times fixed while changing $H$ cannot
simultaneously fit the absolute surface-wave velocities. Formally, the RF kernel is
sensitive to ratios and contrasts, the dispersion kernel to absolute values —
their Jacobians are not parallel, so the joint Hessian is well conditioned where
either alone is not.

**Resolutions to report.** $H$: the 95% marginal interval from a
dispersion+RF joint inversion and, independently, the half-maximum region of the
H-K stack for comparison. $V_p/V_s$: the same two, plus the spread over
back-azimuth as the anisotropy/dip test. $V_s(z)$: a checkerboard or
layer-thickness trade-off test, quoting the shallowest and deepest well-resolved
nodes.

**The demonstration that the ambiguity is gone.** Run the *same* two-stage
experiment as this project's ★5, but with the assumed $V_p$ deliberately wrong by
$\pm 5\%$. H-K alone moves $H$ by $\pm 5\%$ and $k$ barely at all; the joint
inversion must recover $H$ and $V_s(z)$ within their stated uncertainties in both
cases. If the joint inversion's $H$ still tracks the input $V_p$, the ambiguity has
only been hidden behind a fixed layer thickness, not removed — the failure mode to
test for explicitly.
