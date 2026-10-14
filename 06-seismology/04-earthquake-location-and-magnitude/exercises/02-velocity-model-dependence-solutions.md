# Solutions — 06-04-02 Dependence on the Velocity Model and Joint Inversion

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [02 Dependence on the Velocity Model and Joint Inversion](../02-velocity-model-dependence.md).

---

## ★1 — Uniform scaling

$$
T/s = 24.000/1.03 = 23.301\ \mathrm{s}.
$$

Every slowness in the integrand $\int \mathrm{d}\ell/v$ is divided by the same
factor, so the integral is divided by it; Fermat's principle gives the same
stationary path for both models, so the ray geometry is untouched.

---

## ★2 — The residual scale

$$
1 - \frac{1}{1.02} = 1 - 0.980392 = 0.019608 .
$$

Near station: $0.019608\times14.423 = 0.283\ \mathrm{s}$.
Far station: $0.019608\times118.029 = 2.315\ \mathrm{s}$.

Both are far above $\sigma_t = 0.050\ \mathrm{s}$.

---

## ★3 — Why more stations do not help

The delay is common to every station in the same sense that it mimics a source
displacement, so it adds coherently across the network rather than averaging
down.

---

## ★4 — Bound versus bias

$$
\sigma_z = \sqrt{\frac{2}{2.2295}} = \sqrt{0.8970} = 0.947\ \mathrm{km},
\qquad
1.96\sigma_z = 1.856\ \mathrm{km}.
$$

The $+2$ per cent bias is $-5.75\ \mathrm{km}$, i.e. $-3.10$ times the bound:
the systematic error is three times larger than the quoted random one, and in a
direction the bound does not describe.

---

## ★5 — Why a 1 per cent error fails everywhere

With $d = 0.01$ the residual at a station of time $T$ is
$0.009901\,T$. Even at the nearest station, $T = 14.423\ \mathrm{s}$ gives
$0.143\ \mathrm{s}$, and any depth change shifts all times by at most
$|z/(v r)|\,\delta z$, which is a fraction of the total time. The mean removal
can absorb a constant part but not the part that grows with distance, so the best
achievable rms stays above $\sigma_t$ at every grid node — which is what the
printed row for $d = +1.0$ per cent shows (minimum rms $0.2733\ \mathrm{s}$).

---

## ★6 — The sign of the bias

A positive $d$ makes predicted times too small, leaving a positive residual that
increases with epicentral distance (it is $\approx d\,T_i$). Because
$\partial T/\partial z = z/(v r)$ is *larger* for nearby stations than for
distant ones, raising the source removes more time at near stations than at far
ones — exactly the pattern needed to fit a residual that grows with distance.
Hence a faster model gives a shallower hypocentre for this geometry. At
teleseismic distances the ray angles steepen and the correlation between $T_i$
and $\partial T_i/\partial z$ can reverse, so the rule is geometry-specific.

---

## ★7 — Joint inversion with a borehole prior

Parameterise the model as a single scale $s$ with a Gaussian prior
$s = 1.00 \pm 0.03$, keep the depth grid, and sample (or grid-search) the product
of the likelihood $\exp(-\chi^{2}/2)$ with that prior. Depending on the sign of
the actual borehole offset, the posterior depth interval shifts by of order
$3\ \mathrm{per\ cent} \times (\text{bias scale})$: with the measured sensitivity
of about $-2.9\ \mathrm{km}$ per per cent near the reference, a 3 per cent prior
standard deviation corresponds to roughly $\pm 8\ \mathrm{km}$ of depth, i.e. the
prior dominates the picks. The reported depth interval would widen from the
$5.50\ \mathrm{km}$ of the fixed-model scan to something of order $10$ to
$15\ \mathrm{km}$, and the dominant term would then be the prior, not the data.

---

## ★8 — Depth-dependent versus uniform error

**Metric:** the located depth bias, in km, for each of the two perturbed models
relative to a control run with the reference model.

**Control:** the reference model with the same grid, event and stations, which
must return 12.00 km.

**Expected outcome:** they differ, because the two perturbations change
arrival times differently as a function of distance — a shallow error affects
near stations most, exactly where depth sensitivity is largest. A uniform error
of the same average size can therefore produce a bias of the opposite sign or a
much smaller magnitude. The conclusion to draw is that the "2 per cent velocity
error" quoted in Section 4 is a *lower bound* on the realistic case, not a
representative one.
