# Solutions — 05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All bodies, depths and noise levels are
> SYNTHETIC.

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★1 — A standardised prediction residual

**(a)** $r = (310-300)/\sqrt{5^2+40^2} = 10/40.31 = 0.248$.

**(b)** $|r| = 0.248 < 1.96$, so the model passes at the 5 per cent level. It also
passes at any conventional level: the measurement is far more precise than the
model, so the test can only detect a model error much larger than 40 m.

**(c)** The model contributes $40^2/(40^2+5^2) = 98.5$ per cent of the variance in
the denominator. **The test is a test of the model, not of the well** — which is
the correct design, and also the reason a well can never "validate" a model more
precisely than the model itself is known.

---

## ★2 — Depth error from a velocity error

**(a)** The measured velocity is 5 per cent too high, so the true value is
$3000/1.05 = 2857.1$ m s⁻¹.

**(b)** Wrong: $z = vt/2 = 3000 \times 2.000/2 = 3000.0$ m.
Right: $z = 2857.1 \times 2.000/2 = 2857.1$ m. Error $= +142.9$ m, i.e.
$+5$ per cent.

**(c)** The error is positive (too deep) because a too-fast velocity converts a
given time into too large a depth. A systematic bias is more dangerous than random
noise because it is invisible in the residual: every reflector is shifted by the
same fraction, the section still ties to itself, and the error is only exposed by a
well — which is exactly why wells are used as velocity calibration points.

---

## ★3 — Why using a well as a constraint destroys it as a test

Including the well in the inversion makes the well data part of the objective
function, so the recovered model minimises the mismatch to that well by
construction and the agreement is a property of the algorithm rather than of the
Earth. The test only has content if the model is frozen before the well data are
seen, and then used to predict a quantity the well measures independently. The
order of operations is therefore part of the result and must be documented.

---

## ★4 — The demonstration's two cases

**(a)** Case A: 0.0184 mGal RMS, $0.9\times$ the station noise. Case B:
0.0188 mGal RMS, also $0.9\times$. **Indistinguishable.**

**(b)** Case A downhole RMS 0.0315 mGal $= 1.6\times$ the station noise (pass,
marginally). Case B downhole RMS 1.1655 mGal $= 58.3\times$ the station noise
(fail, decisively).

**(c)** Case A: 783.6 kg m⁻³ implied against 800.0 kg m⁻³ on core — factor 0.98,
i.e. 2 per cent low. Case B: 1268.6 kg m⁻³ implied against 800.0 kg m⁻³ — factor
1.59, i.e. 59 per cent high.

In case B the dominant error is the **mass**, not the radius: the single-body fit
recovered $9.182\times10^{9}$ kg against $1.346\times10^{10}$ kg actually present,
because it had to absorb the deep body into one compact source. The radius used
(120 m) was correct. Equation (4) therefore attributes the whole 59 per cent to
$\delta M/M$.

---

## ★5 — Propagating the radius uncertainty

**(a)** $|\delta(\Delta\rho)/\Delta\rho| = 0.05 + 3(0.10) = 0.35$, i.e. 35 per cent.

**(b)** $0.05 + 3(0.20) = 0.65$, i.e. 65 per cent.

**(c)** The cubed dependence means a borehole must locate a body's *extent* to
about three times better than the density precision required. To quote a density
contrast to 15 per cent with a mass known to 5 per cent, the radius must be known
to 3.3 per cent — for a 120 m body, to $\pm 4$ m, which is better than most
wireline depth control in a deviated hole. This is why density contrasts derived
from surface geophysics plus a single well are almost always over-confident.

---

## ★6 — Designing the test

**(a)** *Prediction:* "The hole will intersect rock with a density contrast of at
least 400 kg m⁻³ relative to the local host, somewhere between 250 and 400 m true
vertical depth."

**(b)** *Precision:* the mass is known to ±11 per cent
($1/9$); for a density precision of 30 per cent the radius must be known to
$(30-11)/3 = 6.3$ per cent. For a 100 m intersection half-length that is ±6 m.

**(c)** *Falsification condition, written before drilling:* "Barren host rock
throughout the entire 250–400 m interval falsifies the model. Partial intersection
with a body of lower contrast than 400 kg m⁻³ falsifies the *property* while
leaving the *mass* possibly correct; in that case report the mass as supported and
the property as falsified."

The last clause is the one most often omitted, and it is the difference between a
test that informs and a test that merely disappoints.

---

## ★7 — Three-hole tomographic test

**(a)** Each hole detects a body whose local gravity gradient exceeds the
instrument's resolution. For a compact body of mass $M$ at horizontal distance
$d$ from the hole and depth $z$ measured along the hole, the along-hole component
is $g_a = GM(z-d_z)/\left(d^2 + (z-d_z)^2\right)^{3/2}$, which peaks at
$|z - d_z| = d/\sqrt{2}$ with amplitude $GM \times 0.385/d^2$. Requiring this to
exceed $3\sigma$ with $\sigma = 0.005$ mGal (a downhole gravimeter is quieter than
a surface one, but this is a SYNTHETIC value) gives
$M_{\min} \approx 3\sigma d^2/(0.385 G) = 1.6\times10^{9} d^2$ kg with $d$ in km.

Three holes at 600 m spacing reduce the maximum distance from any point in the
triangle to the nearest hole from 600 m (one hole at a corner) to 346 m (the
centroid distance). Since $M_{\min} \propto d^2$, the detectability improves by a
factor $(600/346)^2 = 3.0$.

**(b)** The feasible set contracts by roughly that factor in the *mass* direction,
and it acquires three independent depth constraints, which is the important part:
the direction the single hole could not constrain is now constrained from three
azimuths, so the depth ambiguity shrinks by roughly the number of independent
holes rather than by their mass sensitivity.

**(c)** Cost: two extra holes at, say, 300 m depth each, against a threefold
improvement in detectability and a large reduction in depth ambiguity. In
exploration the comparison is usually made against the *expected value of
information* of the extra holes
([18-06-06](../../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md));
the physical improvement must be converted into a decision improvement before the
cost comparison means anything.

---

## ★8 — Discretisation versus model error

**(a)** The demonstration uses 257 points per sphere ($n=9$ per axis after
exclusion of the exterior). Refining to $n = 11, 13, 15$ changes the downhole RMS
by less than 1 per cent once $n \ge 11$ (approximately 400–500 retained points);
the change from $n=9$ to $n=11$ is of order 1 per cent, and beyond that the RMS is
dominated by the *inversion* residual, not the discretisation. **You should
verify the exact counts on your own run; I state the trend and the criterion, not
a measured crossover I have not obtained.**

**(b)** Quote the discretisation error as the difference between the
finest two levels you ran, e.g. < 1 per cent of the downhole RMS. It is a
numerical error on the *test*, and it must be smaller than the effect the test is
looking for.

**(c)** Discretisation error is a property of your representation of a *given*
model: it converges to zero as you refine, and you can measure it. Model error is
the difference between the best model in your family and the Earth: it does not
converge, and the only way to detect it is a test against independent data. The
demonstration's case B has a discretisation error of order 1 per cent and a model
error of 5800 per cent.
