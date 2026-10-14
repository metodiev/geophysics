# Solutions — 14-01-06 The Unsaturated Zone, Infiltration and Soil Moisture

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All soils are **SYNTHETIC**.

Lesson: [06 The Unsaturated Zone, Infiltration and Soil Moisture](../06-unsaturated-zone.md).

---

## ★1 — Retention

With $n = 2.0$, $m = 1 - 1/2 = 0.5$ and $\theta_s - \theta_r = 0.35$.

$h = -0.2$ m: $\alpha\lvert h\rvert = 0.40$,
$$1 + 0.40^{2} = 1.16, \qquad (1.16)^{-0.5} = 0.92848,$$
$$\theta = 0.05 + 0.35(0.92848) = 0.37497, \qquad
S_e = 0.92848.$$

$h = -2.0$ m: $\alpha\lvert h\rvert = 4.0$,
$$1 + 4.0^{2} = 17.0, \qquad (17.0)^{-0.5} = 0.24254,$$
$$\theta = 0.05 + 0.35(0.24254) = 0.13489, \qquad S_e = 0.24254.$$

**Comment.** A ten-fold increase in suction (from 0.2 to 2 m) removed 74% of the
stored water above residual
(0.32497 $\to$ 0.08489 m$^3$ m$^{-3}$). For $n = 2$ the curve is relatively steep; a real
sandy soil with $n = 1.5$ would lose less, and a clay with $n = 1.1$ much less.

---

## ★2 — Inverting the retention curve

$$S_e = \frac{0.30 - 0.05}{0.35} = 0.71429,$$
$$\lvert h\rvert = \frac{1}{\alpha}\left(S_e^{-1/m} - 1\right)^{1/n}
= \frac{1}{2.0}\left(0.71429^{-2} - 1\right)^{1/2}.$$

$0.71429^{-2} = 1.95918$, so $1.95918 - 1 = 0.95918$ and
$\sqrt{0.95918} = 0.97938$:

$$\lvert h\rvert = 0.5 \times 0.97938 = 0.4897\ \mathrm{m}
= 4.80\ \mathrm{kPa}.$$

**Practical note.** This inversion is the operation a numerical model performs at
every node at every time step. It is cheap in closed form for van Genuchten but
becomes a root-find for tabulated retention data, which is why closed forms
dominate practice.

---

## ★3 — Field capacity, wilting point, available water

$$\theta_{fc} = \theta(-3.3) = 0.05 + 0.35\left(1 + (2.0 \times 3.3)^{2}\right)^{-0.5}
= 0.05 + 0.35(1 + 43.56)^{-0.5}$$
$$= 0.05 + 0.35(0.14986) = 0.10243.$$

$$\theta_{wp} = \theta(-150) = 0.05 + 0.35\left(1 + (300)^{2}\right)^{-0.5}
= 0.05 + 0.35(0.003333) = 0.05117.$$

$$\text{AWC} = 0.10243 - 0.05117 = 0.05127\ \mathrm{m^3\,m^{-3}}
= 51.3\ \mathrm{mm\ per\ metre}.$$

**Comment.** This soil holds only 51 mm of plant-available water per metre,
half the lesson's soil (80.9 mm/m). Note also how much of the *total* porosity is
unavailable: the soil reaches field capacity at $\theta = 0.102$ out of
$\theta_s = 0.40$ — three quarters of the pore space is air at field capacity,
which is why resistivity and permittivity change so strongly with water content in
a coarse soil.

---

## ★★4 — Green–Ampt infiltration and ponding

Parameters: $K_s = 5.0 \times 10^{-7}\ \mathrm{m\,s^{-1}}$,
$\psi_f\Delta\theta = 0.15 \times 0.30 = 0.045$ m, $t = 3600$ s, so
$K_s t = 1.80 \times 10^{-3}$ m.

Solve
$$F - 0.045\ln\left(1 + \frac{F}{0.045}\right) = 1.80 \times 10^{-3}.$$

By Newton iteration, $F = 1.3955 \times 10^{-2}$ m $= 13.96$ mm.

$$f = K_s\left(1 + \frac{0.045}{0.013955}\right)
= 5.0 \times 10^{-7}(1 + 3.225) = 2.112 \times 10^{-6}\ \mathrm{m\,s^{-1}}
= 7.60\ \mathrm{mm\,h^{-1}}.$$

$$\text{front depth} = \frac{F}{\Delta\theta} = \frac{0.013955}{0.30}
= 0.0465\ \mathrm{m} = 46.5\ \mathrm{mm}.$$

**Ponding time** for $r = 5\ \mathrm{mm\,h^{-1}} = 1.389 \times 10^{-6}\
\mathrm{m\,s^{-1}}$:
$$K_s = 5.0 \times 10^{-7}\ \mathrm{m\,s^{-1}} = 1.80\ \mathrm{mm\,h^{-1}},$$
$$t_p = \frac{5.0 \times 10^{-7} \times 0.045}
{1.389 \times 10^{-6}(1.389 \times 10^{-6} - 5.0 \times 10^{-7})}
= \frac{2.25 \times 10^{-8}}{1.235 \times 10^{-12}}
= 1.822 \times 10^{4}\ \mathrm{s} = 303.7\ \mathrm{min} = 5.06\ \mathrm{h}.$$

So the soil **does** pond at $5\ \mathrm{mm\,h^{-1}}$, but only after five hours:
$r/K_s = 2.78 > 1$. Note the design implication — a 2-hour storm produces no runoff
on this soil, while a 6-hour storm at the same intensity does.

---

## ★★5 — Unsaturated conductivity collapse

$S_e(0.35) = (0.35-0.06)/(0.42-0.06) = 0.80556$;
$S_e(0.15) = (0.15-0.06)/0.36 = 0.25000$.

With $m = 1 - 1/1.6 = 0.375$, so $1/m = 2.6667$:

$$K(0.35) = 2.0 \times 10^{-6}(0.80556)^{0.5}
\left[1 - (1 - 0.80556^{2.6667})^{0.375}\right]^{2}.$$

$0.80556^{2.6667} = 0.56176$; $1 - 0.56176 = 0.43824$;
$0.43824^{0.375} = 0.73294$; $1 - 0.73294 = 0.26706$;
$0.26706^{2} = 0.07132$; $0.80556^{0.5} = 0.89753$:

$$K(0.35) = 2.0 \times 10^{-6} \times 0.89753 \times 0.07132
= 1.271 \times 10^{-7}\ \mathrm{m\,s^{-1}}.$$

$$K(0.15) = 2.0 \times 10^{-6}(0.25)^{0.5}
\left[1 - (1 - 0.25^{2.6667})^{0.375}\right]^{2}.$$

$0.25^{2.6667} = 0.024803$; $1 - 0.024803 = 0.975197$;
$0.975197^{0.375} = 0.99063$; $1 - 0.99063 = 0.009370$; squared $= 8.780 \times
10^{-5}$; $\sqrt{0.25} = 0.5$:

$$K(0.15) = 2.0 \times 10^{-6} \times 0.5 \times 8.780 \times 10^{-5}
= 8.788 \times 10^{-11}\ \mathrm{m\,s^{-1}}.$$

$$\text{Ratio} = \frac{1.271 \times 10^{-7}}{8.788 \times 10^{-11}} = 1447.$$

**Why it matters.** A wetting front moving through a soil at $\theta = 0.15$
advances 1447 times more slowly than through the same soil at $\theta = 0.35$ under
the same gradient. Recharge therefore happens in a few large wetting events that
push the front past the dry layer, not gradually throughout the year — which is
exactly why recharge is "event-driven" and why a wetter-than-average year recharges
disproportionately.

---

## ★★6 — CRIM inversion and radar velocity

$$\sqrt{\varepsilon} = \sqrt{16} = 4.0, \qquad
\theta = \frac{4.0 - (1-\phi)\sqrt{4.5} - \phi}{\sqrt{81} - 1}
= \frac{4.0 - (1-\phi)(2.12132) - \phi}{8}.$$

**With $\phi = 0.35$:** numerator
$= 4.0 - 0.65(2.12132) - 0.35 = 4.0 - 1.37886 - 0.35 = 2.27114$;
$$\theta = \frac{2.27114}{8} = 0.28389.$$

$$v = \frac{c}{\sqrt{\varepsilon}} = \frac{0.299792458}{4.0}
= 0.074948\ \mathrm{m\,ns^{-1}},$$
$$\text{TWT} = \frac{2 \times 0.4}{0.074948} = 10.67\ \mathrm{ns}.$$

**With $\phi = 0.45$:** numerator
$= 4.0 - 0.55(2.12132) - 0.45 = 4.0 - 1.16673 - 0.45 = 2.38327$;
$$\theta = 0.29791.$$

Change in $\theta$: $0.29791 - 0.28389 = +0.0140$ — i.e. a ten-point porosity
assumption error changes the inferred water content by about **0.014**, less than
the $\pm 0.02$ target of ★★★7. This is the robustness noted in the lesson: the
mineral and air end members have similar permittivities, so their contributions
partly cancel in the denominator.

---

## ★★★7 — A soil-moisture monitoring programme to $\pm 0.02$

**Target.** $\theta$ to $\pm 0.02$ volumetric, over the top metre, with a stated
temporal resolution (say daily) and spatial support (say 1 m$^2$).

**Error budget.** From the lesson, $\mathrm{d}\varepsilon/\mathrm{d}\theta = 46.2$
near $\theta = 0.155$ and about $2\sqrt{\varepsilon}\times 8 \approx 64$ at
$\varepsilon = 16$ (differentiating $\sqrt{\varepsilon} = \ldots + 8\theta$ gives
$\mathrm{d}\varepsilon/\mathrm{d}\theta = 2\sqrt{\varepsilon}\,(\sqrt{81}-1) =
16\sqrt{\varepsilon}$). At $\varepsilon = 16$ that is 64, so
$$\delta\theta = \frac{\delta\varepsilon}{64} = \frac{\delta\varepsilon}{64}.$$
For $\delta\theta = 0.02$ we need $\delta\varepsilon = 1.28$, i.e. a relative
permittivity accuracy of $1.28/16 = 8\%$. That is comfortable for a
ground-coupled GPR with a known target geometry, and comfortable for a
capacitance sensor, so **the physics does not set the limit — calibration and
representativeness do.**

**Calibration arithmetic.** Gravimetric sampling: a 100 cm$^3$ ring, dried at
$105\ ^\circ$C to constant mass. The volumetric water content is
$$\theta = \frac{m_{\text{wet}} - m_{\text{dry}}}{\rho_w V_{\text{ring}}}.$$
With a balance reading to 0.01 g and a ring volume known to 1%, a typical
$\theta = 0.25$ has mass difference 25 g, so the mass error contributes
$0.01/25 = 0.04\%$ — negligible. The dominant error is the **ring volume and the
sample disturbance**, realistically 2–3% of $\theta$, i.e. $\pm 0.006$. So
$\pm 0.02$ is achievable, but only with 3–5 replicate samples per calibration
point.

**How many samples and over what range.** The relation between a sensor reading
and $\theta$ is nonlinear near the dry and wet ends, so calibration must cover the
range of interest: at least five water contents spanning $0.05$ to saturation
$\theta_s$, and at least three replicates each — **15 gravimetric samples
minimum** per soil horizon. Sampling only near the ambient water content is the
classic error: the fit is excellent where you did not need it and wrong where you
do.

**Clay-rich horizon.** Clay-bound water has a permittivity well below that of free
water (roughly 5–6 rather than 81), and clays also have high specific surface, so
CRIM over-predicts the water content of a clay-rich soil and the correction is
mineral-specific. If the profile contains a clay horizon, calibrate it separately
or expect a bias of 0.02–0.05 in that layer.

**A systematic error precision cannot see.** *Representativeness*: the sensor
measures a $\sim$100 cm$^3$ volume, GPR averages over a Fresnel zone of order
1 m$^2$, and the profile is heterogeneous at both scales. A perfectly calibrated
sensor and a perfectly calibrated radar can disagree by 0.05 in $\theta$ while both
are "right" for their own support volume. The fix is a third, independent
measurement with a different support (a neutron probe in an access tube, or a
time-lapse ERT difference), and reporting the support volume with every number.

---

## ★★★8 — What the erfc test proves, and a full verification suite

**What the $\mathrm{erfc}$ test verifies.** The numerical result
$\theta(z,t) = \theta_i + \Delta\theta\,\mathrm{erfc}\left(z/2\sqrt{Dt}\right)$ solves
the *linear* diffusion equation $\theta_t = D\theta_{zz}$ with a step initial
condition. The test therefore verifies: the time-stepping loop, the spatial
second-difference stencil, the Dirichlet/free-drainage boundary treatment at the
two ends, the handling of units in $D\Delta t/\Delta z^{2}$, and the choice of time
step. Measured: maximum deviation $8.3 \times 10^{-6}$, i.e.
$3.1 \times 10^{-5}$ of the step, consistent with first-order-in-time,
second-order-in-space truncation.

**What it does not verify.** Everything that makes Richards' equation *Richards'*
equation: the retention curve $\theta(h)$, the conductivity function $K(\theta)$,
the inverse retention $h(\theta)$, the mixed-form nonlinear update, the gravity
term, and the flux boundary condition. A solver with $K$ hard-coded to a wrong
constant would pass this test perfectly.

**(i) Manufactured solution for the linearised equation.** Take a domain
$0 \le z \le L$ with Dirichlet conditions and the exact solution
$$\theta(z,t) = \theta_0 + A\sin\left(\frac{\pi z}{L}\right)e^{-D\pi^{2}t/L^{2}}.$$
Then $\theta_t = -D\pi^{2}/L^{2}\times[\text{the same sine}]$ and
$\theta_{zz} = -\pi^{2}/L^{2}\times[\text{the same sine}]$, so $\theta_t = D\theta_{zz}$
**identically**: the function is an exact solution with no source term, and the
exponential decay is exactly the diffusion eigenmode. Feeding the analytic initial
and boundary values to the code and comparing at $t = L^{2}/(\pi^{2}D)$ (where the
amplitude has decayed by $e^{-1}$) gives a clean error measure with no numerical
integration of anything.

**(ii) Grid-convergence test with an observed order.** Refine
$\Delta z \to \Delta z/2 \to \Delta z/4$ at a fixed time and compute
$$\lVert E\rVert = \max_j\lvert \theta_j - \theta(z_j)\rvert, \qquad
p = \log_2\frac{\lVert E(\Delta z)\rVert}{\lVert E(\Delta z/2)\rVert}.$$
A correct second-order spatial discretisation with a first-order-in-time explicit
stepper gives $p \approx 2$ only if $\Delta t$ is refined **in proportion to**
$\Delta z^{2}$ (to keep the temporal error from dominating). Reporting $p$ without
stating the $\Delta t$ refinement is meaningless; that is the point of the test.
Unlike the Dupuit parabola of lesson 03, this problem has a non-polynomial
solution, so the scheme's exactness class does not mask the order.

**(iii) Physical limits with known exact values.** Two cheap and decisive ones:

  - $\theta(h \to 0) = \theta_s$ exactly and $K(\theta_s) = K_s$ exactly (the
    demonstration checks both: $\theta(0) = 0.4200$ and $K(\theta_s) =
    1.0000 \times 10^{-5}$);
  - the **unit-gradient steady state**: with a constant surface flux $r < K_s$ and
    free drainage, the long-time profile satisfies $K(\theta) = r$ at every depth,
    with $\theta \to \theta_{eq} = K^{-1}(r)$. The demonstration computes
    $\theta_{eq} = 0.3792$ and shows the surface approaching it. Both limits are
    independent of the discretisation, so they catch errors in the constitutive
    relations that the linear tests cannot see.

**(iv) The mass-balance check.** $\int r\,\mathrm{d}t - \int q_{\text{base}}\,
\mathrm{d}t = \Delta(\text{storage})$, closing to round-off ($8.3 \times 10^{-11}$
mm in the demonstration). This is the only test that detects a **conservation**
bug — a wrong sign in a flux, a mishandled interface, or water silently created by
a clipping operation. A solver can pass (i), (ii) and (iii) and still violate (iv).

**What each test catches that the others do not.**

| Test | Catches | Misses |
|---|---|---|
| erfc | time-stepper, stencil, BC implementation | constitutive relations, conservation |
| manufactured solution | spatial order, BCs, source handling | constitutive relations, conservation |
| grid convergence | implementation order, $\Delta t$ coupling | any error that is grid-independent |
| physical limits | retention and conductivity functions | conservation, order of accuracy |
| mass balance | flux sign errors, clipping losses | wrong but conservative physics |

Together the five are the standard of evidence for a hydrological model, and none
of them alone is sufficient. This is the same standard that
[module 19](../../../19-numerical-modeling-hpc/README.md) applies to larger codes.

---

## Mastery checkpoint — worked

Synthetic silt loam: $\theta_s = 0.46$, $\theta_r = 0.10$,
$\alpha = 1.2\ \mathrm{m^{-1}}$, $n = 1.5$ (so $m = 1 - 1/1.5 = 0.33333$),
$K_s = 2.0 \times 10^{-6}\ \mathrm{m\,s^{-1}}$, $\theta_i = 0.22$.

**(a) Retention and conductivity.**

$h = -0.5$ m: $\alpha\lvert h\rvert = 0.60$; $0.60^{1.5} = 0.46476$;
$(1.46476)^{-0.33333} = 0.88056$;
$$\theta = 0.10 + 0.36(0.88056) = 0.41699, \qquad S_e = 0.88056.$$

$h = -5.0$ m: $\alpha\lvert h\rvert = 6.0$; $6.0^{1.5} = 14.697$;
$(15.697)^{-0.33333} = 0.39943$;
$$\theta = 0.10 + 0.36(0.39943) = 0.24379, \qquad S_e = 0.39943.$$

Conductivity, with $1/m = 3$:

$$K(0.41699) = 2.0 \times 10^{-6}(0.88056)^{0.5}
\left[1 - (1 - 0.88056^{3})^{0.33333}\right]^{2}.$$
$0.88056^{3} = 0.68299$; $1 - 0.68299 = 0.31701$;
$0.31701^{1/3} = 0.68175$; $1 - 0.68175 = 0.31825$; squared $= 0.10128$;
$\sqrt{0.88056} = 0.93838$:
$$K = 2.0 \times 10^{-6} \times 0.93838 \times 0.10128
= 1.901 \times 10^{-7}\ \mathrm{m\,s^{-1}}.$$

$$K(0.24379) = 2.0 \times 10^{-6}(0.39943)^{0.5}
\left[1 - (1 - 0.39943^{3})^{0.33333}\right]^{2}.$$
$0.39943^{3} = 0.063727$; $1 - 0.063727 = 0.936273$;
$0.936273^{1/3} = 0.97832$; $1 - 0.97832 = 0.02168$; squared
$= 4.700 \times 10^{-4}$; $\sqrt{0.39943} = 0.63201$:
$$K = 2.0 \times 10^{-6} \times 0.63201 \times 4.700 \times 10^{-4}
= 5.941 \times 10^{-10}\ \mathrm{m\,s^{-1}}.$$

The ratio is $1.901 \times 10^{-7}/5.941 \times 10^{-10} = 320$: a decrease of
$\theta$ by 0.17 cuts the conductivity by more than two orders of magnitude.

**(b) Available water capacity.**
$$\theta_{fc} = \theta(-3.3) = 0.10 + 0.36\left[1 + (1.2 \times 3.3)^{1.5}\right]^{-1/3}.$$
$1.2 \times 3.3 = 3.96$; $3.96^{1.5} = 7.8808$; $(8.8808)^{-1/3} = 0.48301$:
$$\theta_{fc} = 0.10 + 0.17388 = 0.27388.$$
$$1.2 \times 150 = 180; \quad 180^{1.5} = 2414.9; \quad (2415.9)^{-1/3} = 0.074536:$$
$$\theta_{wp} = 0.10 + 0.026833 = 0.12683.$$
$$\text{AWC} = 0.27388 - 0.12683 = 0.14705\ \mathrm{m^3\,m^{-3}}
= 147.0\ \mathrm{mm\ per\ metre}.$$
This is a high-available-water soil (nearly twice the lesson's synthetic soil),
because its retention curve is gentle in the plant-relevant suction range.

**(c) Ponding times.** $K_s = 2.0 \times 10^{-6} \times 3.6 \times 10^{6} =
7.2\ \mathrm{mm\,h^{-1}}$, and $\Delta\theta = 0.46 - 0.22 = 0.24$,
$\psi_f\Delta\theta = 0.25 \times 0.24 = 0.060$ m.

$r = 12\ \mathrm{mm\,h^{-1}} = 3.333 \times 10^{-6}\ \mathrm{m\,s^{-1}}$:
$$t_p = \frac{2.0 \times 10^{-6} \times 0.060}
{3.333 \times 10^{-6}(3.333 \times 10^{-6} - 2.0 \times 10^{-6})}
= \frac{1.20 \times 10^{-7}}{4.444 \times 10^{-12}}
= 2.70 \times 10^{4}\ \mathrm{s} = 7.50\ \mathrm{h}.$$

$r = 24\ \mathrm{mm\,h^{-1}} = 6.667 \times 10^{-6}\ \mathrm{m\,s^{-1}}$:
$$t_p = \frac{1.20 \times 10^{-7}}{6.667 \times 10^{-6} \times 4.667 \times 10^{-6}}
= 3.857 \times 10^{3}\ \mathrm{s} = 64.3\ \mathrm{min}.$$

**Both rates pond** (both exceed $K_s = 7.2$ mm h$^{-1}$), but the heavier rain
ponds seven times sooner. Note the check that would catch an arithmetic slip:
$t_p$ must fall between the two, and the ratio $7.50/1.07 = 7.0$ is consistent
with the $\sim r^{-2}$ scaling for rates well above $K_s$.

**(d) Green–Ampt at $t = 30$ min.** $\psi_f\Delta\theta = 0.060$ m,
$K_s t = 2.0 \times 10^{-6} \times 1800 = 3.60 \times 10^{-3}$ m:
$$F - 0.060\ln\left(1 + \frac{F}{0.060}\right) = 3.60 \times 10^{-3}.$$
Solving by Newton iteration, $F = 2.3251 \times 10^{-2}$ m $= 23.25$ mm:
$$f = 2.0 \times 10^{-6}\left(1 + \frac{0.060}{0.023251}\right)
= 2.0 \times 10^{-6}(3.5806) = 7.161 \times 10^{-6}\ \mathrm{m\,s^{-1}}
= 25.78\ \mathrm{mm\,h^{-1}},$$
$$\text{front depth} = \frac{F}{\Delta\theta} = \frac{0.023251}{0.24}
= 0.0969\ \mathrm{m}.$$
Consistency check: $f = 25.78\ \mathrm{mm\,h^{-1}}$ is between $K_s = 7.2$ and the
initial rate, and it is falling as the front deepens ✔.

**(e) CRIM and GPR.** With $\phi = 0.46$ and $\theta = 0.25$:
$$\sqrt{\varepsilon_{\text{eff}}} = (1 - 0.46)\sqrt{4.5} + 0.25\sqrt{81}
+ (0.46 - 0.25)(1)$$
$$= 0.54(2.12132) + 0.25(9) + 0.21
= 1.14551 + 2.25 + 0.21 = 3.60551,$$
$$\varepsilon_{\text{eff}} = 12.9997, \qquad
v = \frac{0.299792458}{3.60551} = 0.083148\ \mathrm{m\,ns^{-1}},$$
$$\text{TWT through 0.5 m} = \frac{2 \times 0.5}{0.083148}
= 12.03\ \mathrm{ns}.$$

**(f) After tilling.** $\alpha = 2.4\ \mathrm{m^{-1}}$, $\theta_s = 0.50$,
$\theta_r = 0.10$:
$2.4 \times 3.3 = 7.92$; $7.92^{1.5} = 22.289$ (since
$\sqrt{7.92} = 2.81425$); $(1 + 22.289)^{-1/3} = (23.289)^{-1/3} = 0.35010$:
$$\theta_{fc} = 0.10 + 0.40(0.35010) = 0.24004.$$

$2.4 \times 150 = 360$; $360^{1.5} = 6830.9$; $(1 + 6830.9)^{-1/3} =
(6831.9)^{-1/3} = 0.052729$:
$$\theta_{wp} = 0.10 + 0.40(0.052729) = 0.12109.$$

$$\text{AWC} = 0.24004 - 0.12109 = 0.11897\ \mathrm{m^3\,m^{-3}}
= 119.0\ \mathrm{mm\ per\ metre},$$
a fall of **19.0%** from 147.0 mm/m. Meanwhile, with
$\Delta\theta = 0.50 - 0.22 = 0.28$ and $\psi_f\Delta\theta = 0.070$ m, the ponding
time at $24\ \mathrm{mm\,h^{-1}}$ becomes
$$t_p = \frac{2.0 \times 10^{-6} \times 0.070}{6.667 \times 10^{-6} \times
4.667 \times 10^{-6}} = 4.50 \times 10^{3}\ \mathrm{s} = 75.0\ \mathrm{min},$$
up from 64.3 min (+17%).

**Which change matters more.** The available water capacity falls 19% while the
ponding time rises 17%. The farmer cares more about the available water capacity,
because it is the reservoir the crop draws on between rains and it determines
whether an irrigation season is needed at all; a 17% delay in ponding matters only
in intense-storm environments where runoff already occurs. The deeper point is that
the two effects have **opposite signs** and come from the same parameter change,
which is why both must be computed rather than asserted from a general claim like
"tilling improves infiltration".
