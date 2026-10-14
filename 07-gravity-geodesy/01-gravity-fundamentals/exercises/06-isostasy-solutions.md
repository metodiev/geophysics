# Solutions — 07-01-06 Isostasy: Pratt, Airy and Flexural Models

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [06 Isostasy: Pratt, Airy and Flexural Models](../06-isostasy.md).

---

## ★1 — Airy root and deficit

$$t = \frac{\rho_{c}}{\rho_{m}-\rho_{c}}\,h
= \frac{2650}{3250-2650}\times1200
= 4.4167\times1200 = 5300.0\ \mathrm{m} = 5.300\ \mathrm{km}.$$

$$\text{deficit} = \left(\rho_{m}-\rho_{c}\right)t = 600\times5300
= 3.180\times10^{6}\ \mathrm{kg\,m^{-2}},$$

which equals $\rho_{c}h = 2650\times1200 = 3.180\times10^{6}\
\mathrm{kg\,m^{-2}}$. ✔

The ratio $t/h = \rho_{c}/\left(\rho_{m}-\rho_{c}\right) = 4.4167$ is the same for
every height: the root is *proportional* to the topography in the Airy model, which
is worth stating because it is a falsifiable prediction (a plot of $t$ against $h$
should be a straight line through the origin).

---

## ★2 — Predicted Bouguer anomaly, two ways

**From the slab term.** The Bouguer reduction removes the attraction of the
topography, $+2\pi G\rho_{c}h$, while the compensation contributes
$-2\pi G\left(\rho_{m}-\rho_{c}\right)t$, and the two are equal by construction:

$$\Delta g_{B} = -2\pi G \rho_{c} h = -4.1930\times10^{-10}\times2650\times1200
= -1.33356\times10^{-3}\ \mathrm{m\,s^{-2}} = -133.356\ \mathrm{mGal}.$$

**From the root deficit.**

$$\Delta g_{B} = -2\pi G \left(\rho_{m}-\rho_{c}\right)t
= -4.1930\times10^{-10}\times600\times5300 = -1.33356\times10^{-3}\
\mathrm{m\,s^{-2}} = -133.356\ \mathrm{mGal}.$$

Both give $-133.356\ \mathrm{mGal}$, which is the point: in the thin-slab
approximation the Airy model's Bouguer anomaly is fixed by the topography alone,
and the isostatic correction that removes it is exactly the root's effect. **A
perfectly compensated plateau has an isostatic anomaly of zero, and it cannot be
otherwise.**

---

## ★3 — Pratt column and its deficit

$$\rho(h) = \frac{\rho_{0}D}{D+h}
= \frac{2700\times35000}{35000+2000}
= \frac{9.45\times10^{7}}{3.7\times10^{4}}
= 2554.05\ \mathrm{kg\,m^{-3}}.$$

$$\text{Pratt deficit} = D\left(\rho_{0}-\rho(h)\right)
= 35000\times\left(2700-2554.05\right)
= 5.10811\times10^{6}\ \mathrm{kg\,m^{-2}}.$$

Airy deficit at the same topography:
$\rho_{0}h = 2700\times2000 = 5.40000\times10^{6}\ \mathrm{kg\,m^{-2}}$.

$$\frac{5.10811 - 5.40000}{5.40000} = -5.41\%.$$

So Pratt's compensation is $5.4\%$ weaker at $h = 2\ \mathrm{km}$ with
$D = 35\ \mathrm{km}$, equivalent to $0.0541\times2\pi G\rho_{0}h =
0.0541\times226.7 = 12.3\ \mathrm{mGal}$ of uncancelled signal. The difference
grows with $h/D$, which is why deep compensation depths ($D$ of tens of kilometres)
make the two models hard to distinguish for gentle topography and easy for
high plateaus.

---

## ★★4 — Finite root geometry

$$g_{\text{cyl}} = 2\pi G\,\Delta\rho\left[t + R - \sqrt{R^{2}+t^{2}}\right],
\qquad t = 5300\ \mathrm{m},\ R = 80\,000\ \mathrm{m}.$$

$$\sqrt{R^{2}+t^{2}} = \sqrt{6.4000\times10^{9} + 2.8090\times10^{7}}
= \sqrt{6.42809\times10^{9}} = 80\,175.4\ \mathrm{m}.$$

$$g_{\text{cyl}} = 4.1930\times10^{-10}\times600\times\left(5300 + 80000 -
80175.4\right) = 4.1930\times10^{-10}\times600\times5124.6
= 1.289\times10^{-3}\ \mathrm{m\,s^{-2}} = 128.94\ \mathrm{mGal}.$$

Slab value: $2\pi G\Delta\rho t = 4.1930\times10^{-10}\times600\times5300
= 1.33356\times10^{-3}\ \mathrm{m\,s^{-2}} = 133.356\ \mathrm{mGal}$.

**Unexplained residual:**

$$2\pi G\,\Delta\rho\left[\sqrt{R^{2}+t^{2}} - R\right]
= 4.1930\times10^{-10}\times600\times175.4
= 4.4126\times10^{-5}\ \mathrm{m\,s^{-2}} = 4.413\ \mathrm{mGal},$$

which is $4.413/133.356 = 3.31\%$ of the compensation.

**Comment.** For this narrower root ($R/t = 15.1$) the residual is $3.3\%$; for the
lesson's $R = 100\ \mathrm{km}$ root under $3\ \mathrm{km}$ of relief
($R/t = 7.5$) it was $6.6\%$. The residual grows as the root becomes narrow
compared with its thickness, exactly like the finite-body effect in the Bouguer
slab (lesson [04](../04-gravity-reduction.md), Section 3). Note that this residual is
positive: the finite root attracts less than the infinite slab would, so the
Bouguer anomaly is *less* negative than the perfect-compensation prediction.

---

## ★★5 — Flexural parameters for $T_{e} = 15$ km

$$D = \frac{E\,T_{e}^{3}}{12\left(1-\nu^{2}\right)}
= \frac{7.0\times10^{10}\times\left(1.5\times10^{4}\right)^{3}}
{12\times\left(1-0.0625\right)}
= \frac{7.0\times10^{10}\times3.375\times10^{12}}{11.25}
= 2.1000\times10^{22}\ \mathrm{N\,m}.$$

$$\alpha = \left(\frac{D}{\Delta\rho\,g}\right)^{1/4}
= \left(\frac{2.1000\times10^{22}}{400\times9.81}\right)^{1/4}
= \left(5.352\times10^{18}\right)^{1/4} = 4.80975\times10^{4}\ \mathrm{m}
= 48.098\ \mathrm{km}.$$

$$\lambda_{\text{transition}} = 2\pi\alpha = 302.21\ \mathrm{km}.$$

**Compensation fractions** from
$w/w_{\text{Airy}} = \left[1+\left(2\pi/\lambda\right)^{4}\alpha^{4}\right]^{-1}$:

| $\lambda$ (km) | $\lambda/\alpha$ | fraction of the Airy root |
|---|---|---|
| 100 | 2.079 | 0.01185 |
| 200 | 4.158 | 0.16095 |
| 400 | 8.316 | 0.75425 |

**Interpretation.** With this thinner plate ($T_{e} = 15\ \mathrm{km}$ against the
lesson's $25\ \mathrm{km}$), the transition is at $302\ \mathrm{km}$ instead of
$401\ \mathrm{km}$: a weaker plate compensates at shorter wavelengths. A load
$100\ \mathrm{km}$ wide is carried almost entirely by the plate
($1.2\%$ compensated), so an Airy model applied to it would over-predict the root
by two orders of magnitude and produce a spurious isostatic anomaly. **$T_{e}$ is
therefore not a detail of the flexural model; it is the parameter that decides which
model is applicable.**

---

## ★★6 — The $\left(\Delta\rho,t\right)$ trade-off

From $\Delta g_{B} = -2\pi G\,\Delta\rho\,t$:

$$\Delta\rho\,t = \frac{\left|\Delta g_{B}\right|}{2\pi G}
= \frac{200\times10^{-5}}{4.1930\times10^{-10}}
= 4.76919\times10^{6}\ \mathrm{kg\,m^{-2}}.$$

| $\Delta\rho$ ($\mathrm{kg\,m^{-3}}$) | required $t$ (km) |
|---|---|
| 400 | 11.923 |
| 600 | 7.948 |
| 800 | 5.961 |

**How much does the answer change?** From $11.923$ to $5.961\ \mathrm{km}$: a
factor of two, i.e. $\pm 50\%$ about the central case. Note also that the *top*
of the root (the crust–mantle boundary) moves by the same amount, so a Moho depth
reported from gravity alone carries a systematic uncertainty of tens of percent
unless an independent density constraint exists. The two end-member contrasts are
both geologically defensible in different settings, which is why the ambiguity
cannot be dismissed as "unrealistic errors".

---

## ★★★7 — Distinguishing Airy from flexure under a 4 km plateau (specification)

**Data.** (i) A dense gravity profile across the plateau and its flanks, with
terrain and Bouguer reductions of the accuracy computed in lesson
[04](../04-gravity-reduction.md); (ii) topography with an accuracy better than the
anomaly's implied elevation error; (iii) an independent estimate of the crustal
thickness at one or more points (receiver functions, wide-angle seismics, or a
borehole reaching the crust–mantle boundary); (iv) if available, a geoid profile
over the same region.

**Predicted difference.** With $\rho_{c} = 2670$, $\rho_{m} = 3270\
\mathrm{kg\,m^{-3}}$, $E = 7.0\times10^{10}\ \mathrm{Pa}$, $\nu = 0.25$:

- local Airy root for $h = 4\ \mathrm{km}$: $t = 17.800\ \mathrm{km}$, which
  explains the whole topography, so the predicted Bouguer anomaly is
  $-2\pi G\rho_{c}h = -0.111969\times4000 = -447.9\ \mathrm{mGal}$ and the
  isostatic anomaly is $0$;
- a plate with $T_{e} = 25\ \mathrm{km}$ ($\alpha = 63.75\ \mathrm{km}$) supporting a
  load $200\ \mathrm{km}$ across ($\lambda \approx 400\ \mathrm{km}$, the lesson's
  convention) compensates a fraction $0.4986$ of the Airy root, i.e. a deflection of
  $8.874\ \mathrm{km}$, and leaves

$$\left(1-0.4986\right)\times447.9 = 224.6\ \mathrm{mGal}$$

of the Bouguer anomaly unexplained.

The models therefore differ by about $225\ \mathrm{mGal}$, two orders of magnitude
above the $1$–$5\ \mathrm{mGal}$ accuracy of a careful survey: **the discrimination
is not limited by the gravity measurement but by the reductions and by the density
contrast.** Note carefully what the contrast does and does not affect. The Bouguer
anomaly of a compensated region is $-2\pi G\rho_{c}h$ whatever $\Delta\rho$ is, and
the flexural anomaly is $-2\pi G\rho_{c}h$ times the compensation fraction; but the
*predicted Moho depth* changes from $17.800\ \mathrm{km}$ at $\Delta\rho = 600\
\mathrm{kg\,m^{-3}}$ to $26.700\ \mathrm{km}$ at $400\ \mathrm{kg\,m^{-3}}$. So a
measured Moho depth alone cannot choose between the models unless the contrast is
pinned independently — for example by the seismic velocity–density relation or by
gravity over a region whose compensation is known to be local.

**Parameter to estimate.** $T_{e}$ (equivalently $\alpha$), by fitting the observed
anomaly profile to the flexural prediction. Report the posterior (or the
$\chi^{2}$ surface) in $\left(T_{e},\Delta\rho\right)$, not a single number: the
correlation between them is the honest output.

**Falsification.** If a profile with $T_{e}$ fixed at the seismically or
heat-flow-implied value cannot fit the observed flanks (a systematic, sign-changing
residual), the flexural model is rejected. If the flanks fit for a wide range of
$T_{e}$, the data do not constrain the plate and the correct report is the admitted
range. For the Airy model, the falsification test is simpler: measure the Moho
depth beneath the plateau and its flanks; local Airy compensation requires it to
differ by exactly $\rho_{c}h/\Delta\rho$. A measured difference that is smaller by
half falsifies Airy and supports flexure.

**Control.** Apply the procedure to a region known from independent data to be in
local isostatic equilibrium and confirm that the fitted $T_{e}$ is small (the models
coincide). A method that reports a large $T_{e}$ everywhere has not been shown to be
sensitive to anything.

---

## ★★★8 — Breaking the $\left(\Delta\rho,t\right)$ trade-off with seismic data

**What each data set constrains.**

- Gravity constrains one number per site: the *product* $\Delta\rho\,t$ (the mass
  deficiency per unit area), through $\Delta g_{B} = -2\pi G\Delta\rho\,t$.
- A receiver function or a wide-angle seismic profile constrains the *depth* $t$ (its
  thickness, hence the depth to the discontinuity) with a known sensitivity to
  velocity: from module [06](../../../06-seismology/08-receiver-functions-and-crustal-structure/README.md),
  a single Ps delay gives a curve of $\left(H,k\right)$ pairs, so seismic data alone
  also leave a trade-off — but a *different* one, between thickness and the
  compressional-to-shear velocity ratio.
- A shear-velocity profile from surface waves or ambient noise gives $v_{s}$ as a
  function of depth, which converts seismic thickness into a density estimate
  through a velocity–density relation.

**How the combination improves the answer.** Represent each data set as a
constraint in the $\left(t, \Delta\rho\right)$ plane:

$$\text{gravity: } \Delta\rho = \frac{4.76919\times10^{6}}{t},
\qquad
\text{seismic: } t = t_{\text{seis}} \pm \sigma_{t},
\qquad
\text{density: } \Delta\rho = \Delta\rho_{\text{petro}} \pm
\sigma_{\rho}.$$

The gravity curve is a hyperbola; the seismic constraint is a horizontal band and
the petrophysical constraint a vertical band. The intersection is a small region.

**Arithmetic (SYNTHETIC).** From question ★★6, gravity alone gives
$\Delta\rho\,t = 4.76919\times10^{6}\ \mathrm{kg\,m^{-2}}$, i.e. $t = 11.923\
\mathrm{km}$ for $\Delta\rho = 400$ and $7.948\ \mathrm{km}$ for $600\
\mathrm{kg\,m^{-3}}$ — a $3.975\ \mathrm{km}$ range, or $\pm 25\%$ about
$9.94\ \mathrm{km}$.

Now suppose receiver functions give $t = 8.5 \pm 0.5\ \mathrm{km}$ (a statement
about the Moho depth with a modest velocity assumption). Intersecting the hyperbola:

$$\Delta\rho = \frac{4.76919\times10^{6}}{8.5\times10^{3}}
= 561.1\ \mathrm{kg\,m^{-3}}.$$

The same $0.5\ \mathrm{km}$ of thickness uncertainty now propagates into
$\Delta\rho$ as

$$\sigma_{\Delta\rho} = \Delta\rho\,\frac{\sigma_{t}}{t}
= 561.1\times\frac{0.5}{8.5} = 33.0\ \mathrm{kg\,m^{-3}},$$

versus a $\pm 200\ \mathrm{kg\,m^{-3}}$ range before the seismic constraint. The
thickness is now known to $6\%$ instead of $25\%$, and the remaining uncertainty is
dominated by the seismic velocity assumption, not by gravity.

**The honest caveat.** The two data sets do not constrain independent quantities:
the seismic thickness depends on the velocity model used to convert delay to depth,
and the petrophysical density comes from a velocity–density relation. A joint
inversion must carry those correlations through, or the reported improvement is
fictitious. The correct deliverable is a joint posterior in
$\left(t,\Delta\rho,v_{p}/v_{s}\right)$ with the shared assumptions stated.

---

## ★★★9 — Testing for isostatic equilibrium (specification)

**Observable.** The isostatic anomaly — the residual after removing a stated
compensation model from a reduced Bouguer anomaly — mapped over the region, together
with the correlation between that residual and topography.

**Test.** For a region *in* equilibrium the residual should be uncorrelated with
topography and have an amplitude consistent with the reduction's noise. For a region
*out* of equilibrium the residual correlates with topography (either sign: a load
without a root gives positive, an excess root gives negative), and the amplitude of
the correlation is a measure of the departures.

**Quantitative statement to report.** The slope of the residual-versus-elevation
regression in $\mathrm{mGal\,m^{-1}}$, its uncertainty, and the residual scatter. In
the thin-slab language the slope expected for full (Airy) compensation is zero,
while for zero compensation it is $2\pi G\rho_{c} = 0.111969\
\mathrm{mGal\,m^{-1}}$ (the lesson's $h = 1\ \mathrm{km}$ Bouguer anomaly). A
measured slope of, say, $0.03\ \mathrm{mGal\,m^{-1}}$ means roughly a quarter of the
topography is uncompensated, and that fraction has an uncertainty obtained from the
regression's standard error.

**Control.** Apply the identical machinery to a SYNTHETIC region constructed to be
exactly Airy-compensated, with the same topography, the same reduction noise and the
same station distribution. The measured slope must be consistent with zero; if it is
not, the pipeline has a bias (an incorrect density, a terrain truncation, a datum
tilt) and the real result cannot be trusted.

**The easiest masquerader.** A wrong **Bouguer density** produces a residual that is
exactly proportional to elevation — indistinguishable from a real uncompensated
fraction, and the lesson's Nettleton experiment
([lesson 04](../04-gravity-reduction.md), Section 6) measured the size of that
confusion: a $125\ \mathrm{kg\,m^{-3}}$ density bias shifted the recovered density
and left a residual correlation of $0.598$. It is ruled out by determining the
density independently (samples, boreholes, or a scan whose residual correlation is
reported), or by showing that the residual-elevation slope is stable when the
density is varied within its plausible range. A second masquerader is a
**truncated terrain correction**, which correlates with local relief and hence with
elevation; the test for it is the convergence check of lesson 04, Section 7.
