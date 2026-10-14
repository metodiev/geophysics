# Solutions — 04-05-01 Landform Processes and Shapes

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Throughout, every rate is reported together with the coefficient it depends on.
$\kappa$, $K$ and $k_s$ are **model inputs** unless a problem states otherwise.

---

## ★1 — Curvature and relaxation time

**(a)** At a divide the steady state of
$\partial z/\partial t = \kappa \partial^{2}z/\partial x^{2} + U$ is
$\partial^{2}z/\partial x^{2} = -U/\kappa$:

$$\frac{\partial^{2}z}{\partial x^{2}}
= -\frac{1\times10^{-4}}{2\times10^{-3}} = -5.0\times10^{-2}\ \mathrm{m^{-1}}.$$

**(b)** Radius of curvature $= 1/|{-5.0\times10^{-2}}| = 20.0$ m.

**(c)** $\tau = L^{2}/\kappa = 50^{2}/2\times10^{-3} = 1.25\times10^{6}$ yr
$= 1.25$ Myr.

**(d)** $\tau \propto 1/\kappa$, so doubling $\kappa$ halves $\tau$ to 0.625 Myr.
$\tau \propto L^{2}$, so doubling $L$ *quadruples* $\tau$ to 5.0 Myr. The
quadratic dependence on length is the reason a wide ridge can be sharp for
geologically implausible times and still be in steady state.

---

## ★2 — Dating a scarp

**(a)**

$$t = \frac{h^{2}}{4\pi\kappa s_{\max}^{2}}
= \frac{8^{2}}{4\pi(1\times10^{-3})(0.5)^{2}}
= \frac{64}{3.1416\times10^{-3}} = 2.037\times10^{4}\ \mathrm{yr}.$$

**(b)** $\sqrt{4\kappa t} = \sqrt{4(1\times10^{-3})(2.0372\times10^{4})}
= \sqrt{81.49} = 9.027$ m. The scarp has been smeared over about 9 m on either
side of its originally vertical face.

**(c)**
$s_{\max} = h/(2\sqrt{\pi\kappa t})
= 8/(2\sqrt{\pi(1\times10^{-3})(2.0372\times10^{4})})
= 8/(2\sqrt{64.0}) = 0.5000$. Exact, because the age was constructed from the
formula.

**(d)** $t = 64/(4\pi(5\times10^{-4})(0.25)) = 4.074\times10^{4}$ yr, a factor of
$2.000$ larger. Since $t \propto 1/\kappa$ and $1/\kappa$ also appears nowhere
else, the age error is exactly the diffusivity error.

---

## ★3 — Slope–area relation

**(a)** $S = 30\,(10^{6})^{-0.5} = 30/1000 = 0.030000$ (3.00 per cent).

**(b)** $S = 30\,(10^{7})^{-0.5} = 30/3162.28 = 0.0094868$ (0.9487 per cent).

**(c)** $S = 30\,(10^{8})^{-0.5} = 30/10^{4} = 0.003000$ (0.3000 per cent).

**(d)** $S A^{\theta} = 30$ at all three areas, to the precision of the
arithmetic. Steepness is an *area-normalised* slope, which is exactly why it is
the quantity that is compared between channels, and why $k_s$ and $\theta$ must
be quoted together.

---

## ★★4 — Inverting the steepness index

**(a)** $k_s = (U/K)^{1/n}$ with $n = 1$ gives $U = K k_s = 10^{-5} \times 30 =
3.0\times10^{-4}$ m yr⁻¹ $= 0.30$ mm yr⁻¹.

**(b)** With $n = 2$, $U = K k_s^{n} = 10^{-5} \times 900 = 9.0\times10^{-3}$
m yr⁻¹ $= 9.0$ mm yr⁻¹ — a factor of 30 larger for the same $k_s$.

**(c)** Because $U = K k_s^{n}$, the implied uplift depends exponentially on the
slope exponent that the study did not measure. A $k_s$ is therefore a statement
about *slope at a reference area*; converting it to an uplift or an erosion rate
requires $n$, $K$ and $\theta$, all of which are model choices or calibrations.
A comparison between two studies is legitimate only if all four are reported with
their units.

---

## ★★5 — The $\chi$-transform

**(a)** With $A/A_0 = (1 + x/x_0)^{2}$ and $m/n = 0.5$,

$$\chi = \int_{0}^{x}\left(1 + \frac{x'}{x_0}\right)^{-1}\mathrm{d}x'
= x_0\ln\!\left(1 + \frac{x}{x_0}\right).$$

At $x = 5000$ m with $x_0 = 1000$ m:
$\chi = 1000\ln 6 = 1000 \times 1.791759 = 1791.76$ m.

**(b)** $z$ against $\chi$ has slope
$-(U/K)A_0^{-m/n} = -(1\times10^{-4}/1\times10^{-5})(1\times10^{5})^{-0.5}
= -10/316.228 = -3.16228\times10^{-2}$ (dimensionless).

**(c)** Elevation drop $= 3.16228\times10^{-2} \times 1791.76 = 56.66$ m.

**(d)** A kink in the $z$–$\chi$ plot marks a **knickpoint**: the reach below it
and the reach above it have different steepness for the same drainage-area
scaling, so the channel is not in steady state and the kink records the position
of a disturbance that is still migrating upstream. A straight line over the whole
profile is what a channel in steady state looks like.

---

## ★★6 — Hack's law and drainage density

**(a)** $L = 1.4\,(250)^{0.6} = 1.4 \times 27.464 = 38.45$ km.

**(b)** Total channel length $= 4.5 \times 38.45 = 173.02$ km, so
$D_d = 173.02/250 = 0.6921$ km⁻¹.

**(c)** $1/(2D_d) = 1/(2 \times 0.6921) = 0.7224$ km $= 722$ m.

**(d)** $k$ has units of km$^{1-2h}$, i.e. km$^{-0.2}$ for $h = 0.6$, because the
right-hand side of $L = kA^{h}$ must have units of km. Two studies that quote
"$k = 1.4$" in different length units (km versus miles) are reporting different
physical coefficients, and neither can be substituted into the other's dataset.

---

## ★★★7 — Reading the demonstration

Quoted output, from `landforms_demo.py` with $\kappa = 1\times10^{-3}$ m² yr⁻¹,
$h = 10$ m, $t = 10^{4}$ yr:

**(a)** Analytic $s_{\max} = 0.892062$; numerical $0.891471$ at
$\Delta x = 0.25$ m. Observed convergence orders of the profile error on the probe
points: $0.988$ then $0.997$.

**(b)** Slope error at the finest grid: $6.63\times10^{-4}$, i.e. **0.066 per
cent**. The first-order (not second-order) behaviour is expected: a vertical step
is represented by a grid only to first order in $\Delta x$.

**(c)** Recovered concavity $\theta = 0.450000$ (input 0.45); steepness index
$k_s = 1.000000\times10^{1}$ at both ends of the $10^{5}$–$10^{8}$ m² area range.

**(d)** Relative difference between the fitted and analytic $z$-on-$\chi$ slope:
$3.83\times10^{-15}$ — machine precision.

**(e)** Knickpoint celerity $c = KA^{m}$: $5.0119\times10^{-3}$ m yr⁻¹ at
$A = 10^{6}$ m², so 100 km takes $1.995\times10^{7}$ yr; $1.4125\times10^{-2}$
m yr⁻¹ at $A = 10^{7}$ m², so 100 km takes $7.079\times10^{6}$ yr.

**(f)** The regression recovers $\theta$ to six decimals because the *data were
generated from the same equation*: the code is being checked against itself, and
what the agreement demonstrates is that the arithmetic and the fitting are
correct. It says nothing about whether real channels obey $\theta = 0.45$, because
that is a claim about the erosion law, and the erosion law is a model input here.
A genuine test requires measured channel profiles and an independent constraint
on $U$ or $K$.

---

## ★★★8 — Interpretation and its limits

**(a)** Two mechanisms, both of which produce an apparent age factor of 3 with one
assumed $\kappa$:

1. **Different material or vegetation, hence different $\kappa$.** A scarp in
   clay-rich till has a lower diffusivity than one in sandy colluvium, so the same
   slope persists longer and the assumed single $\kappa$ gives an *older* apparent
   age for the till scarp. Testable with grain-size analysis and, more directly,
   with an independent estimate of $\kappa$ from repeat surveys or from a dated
   independent surface.
2. **Different actual ages with different rates of scarp production** — for
   example one scarp produced by a single surface rupture and the other by
   cumulative displacement that includes older surface traces. Testable by
   palaeoseismic trenching, which exposes the number and geometry of ruptures.

A third, also real: the scarps may have had different initial geometries (a
bevel, a fan at the toe, or an initially non-vertical face), which changes $h$ and
therefore the age.

**(b)** If the true transport on steep slopes is faster than linear diffusion
predicts, then the effective diffusivity is *larger* than the $\kappa$ that a
linear model calibrated on gentle slopes would supply. From
$t = h^{2}/(4\pi\kappa s_{\max}^{2})$, an assumed $\kappa$ that is too small
returns a **$t$ that is too large**: the age is overestimated. The sign follows
directly from $t \propto 1/\kappa$.

**(c)** $U = -\kappa\,\partial^{2}z/\partial x^{2}
= (2\times10^{-3})(5.1\times10^{-2}) = 1.02\times10^{-4}$ m yr⁻¹, i.e. about
0.10 mm yr⁻¹.

The two largest uncertainties are:

1. **$\kappa$**, which enters linearly and is calibrated rather than measured; it
   varies by an order of magnitude between sites.
2. **The curvature estimate itself**, which depends on the DEM resolution, the
   smoothing scale and whether the crest is genuinely at steady state — local
   convexity from a single tree-throw mound or a hollow can change the sign of a
   second derivative at the 10 m scale.

**(d)** The contrasts and one method each:

| Contrast | Method |
|---|---|
| Resistivity (sand higher than clay) | ERT or electromagnetic induction |
| Permittivity and low loss (sand radar-transparent) | GPR |
| P-wave velocity and density (sand slightly stiffer, less dense) | Seismic refraction or surface waves |
| Shear modulus (compaction state) | Multichannel surface-wave analysis |
The point of the list is that the channel is a *resistivity and permittivity*
target first; the elastic contrasts between a sand fill and a clay floodplain are
small, which is why a P-wave reflection survey is usually the wrong first choice
for a 12 m deep palaeo-channel.
