# Solutions — 13-03-02 Rifting, Break-Up and Passive Margin Formation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Where a problem admits more than one defensible route, the route taken is
> stated.

Lesson: [02 Rifting, Break-Up and Passive Margin Formation](../02-rift-and-breakup.md).

---

## ★1 — Uniform stretching geometry

$$
t_c = \frac{32}{1.6} = 20.0\ \mathrm{km}, \qquad
a = \frac{110}{1.6} = 68.75\ \mathrm{km}.
$$

Finite extension: $(\beta-1)\times100 = 60\%$.
Natural strain: $\ln 1.6 = 0.470$.
They differ by a factor $0.60/0.470 = 1.28$ — the same factor that appears at
every $\beta$, and the reason the convention must be stated.

---

## ★2 — Closed-form initial subsidence

$$
A = \frac{(\rho_m - \rho_c)t_{c0}}{\rho_m - \rho_w}
= \frac{(3330-2800)(32)}{3330-1030}
= \frac{530\times32}{2300} = 7.374\ \mathrm{km},
$$

$$
B = \frac{\rho_m\alpha T_m (a - t_{c0})^{2}}{2a(\rho_m-\rho_w)}
= \frac{3330\times3\times10^{-5}\times1300\times(110-32)^{2}}
{2\times110\times2300}
= \frac{129.87\times6084}{506000} = 1.561\ \mathrm{km}.
$$

(Intermediate values: $\rho_m\alpha T_m = 129.87\ \mathrm{kg\,m^{-3}}$;
$(78\ \mathrm{km})^{2}/(2\times110\ \mathrm{km}) = 27.65\ \mathrm{km}$, and
$129.87\times27.65\times10^{3}/(2300) = 1561\ \mathrm{m}$.)

$$
S(0) = \left(1 - \frac{1}{1.6}\right)(7.374 - 1.561)
= 0.375\times5.813 = 2.180\ \mathrm{km}.
$$

---

## ★3 — Decay constants

$$
\tau(110) = \frac{110^{2}}{\pi^{2}\times31.558} = \frac{12100}{311.5}
= 38.85\ \mathrm{Myr},\qquad
\tau(200) = \frac{40000}{311.5} = 128.42\ \mathrm{Myr}.
$$

Ratio $200^{2}/110^{2} = 3.31$. The meaning: $\tau \propto a^{2}$, so the
cooling time is set by the **square** of the lithospheric thickness. A margin
underlain by a $200\ \mathrm{km}$ lithosphere subsides for three times longer
than one underlain by $110\ \mathrm{km}$. This is why the shape of the post-rift
curve is a probe of lithospheric thickness, and why attributing a slow curve to
a low viscosity (rather than a thick lithosphere) is a model choice, not a
result.

---

## ★4 — Strain rate for a fast rift

Natural strain: $\ln 2.5 = 0.916$.
For $12\ \mathrm{Myr}$:
$\dot\varepsilon = 0.9163/12 = 0.07636\ \mathrm{Myr^{-1}}$.
Convert: $0.07636\ \mathrm{Myr^{-1}} = 0.07636\times10^{3}$ nanostrain per year
$= 76.4\ \mathrm{nstrain\,yr^{-1}}$.

Velocity gradient: over $100\ \mathrm{km}$, the extension rate is
$\dot\varepsilon L = 0.07636\times100 = 7.64\ \mathrm{km\,Myr^{-1}}
= 7.64\ \mathrm{mm\,yr^{-1}}$. That is a large but not absurd rate — comparable
to the fastest continental rifts, and a reminder that a fast rift is not slow in
absolute terms even though the strain rate is called "fast" only relative to
$10^{-16}\ \mathrm{s^{-1}}$-scale mantle strain.

---

## ★5 — Thermal part versus crustal part

The exact closed forms are worth writing out, because the two terms have
different $\beta$-dependence even though both grow with $\beta$.

Initial:
$$
S(0) = \left(1 - \frac{1}{\beta}\right)(A - B),
\qquad A = 8.065,\ B = 1.829,\ A-B = 6.236\ \mathrm{km}.
$$

Equilibrium: the mantle term must be evaluated with the **thinned crustal
thickness**, so with
$C = \rho_m\alpha T_m/\left[2a(\rho_m-\rho_w)\right] = 2.2586\times10^{-4}\
\mathrm{km^{-1}}$ we have

$$
S(\infty) = A\left(1-\frac{1}{\beta}\right)
+ C\left[\left(a - \frac{t_{c0}}{\beta}\right)^{2} - (a - t_{c0})^{2}\right] .
$$

Evaluating:

$$
\beta = 1.5:\quad S(0) = 2.079,\quad
C[(101.667)^{2} - 90^{2}] = C(10336-8100) = 0.505,\quad
S(\infty) = 2.688+0.505 = 3.193\ \mathrm{km}.
$$
$$
\beta = 1.25:\quad S(0) = 1.247,\quad
C[(97)^{2} - 90^{2}] = C(9409-8100) = 0.296,\quad
S(\infty) = 1.612+0.296 = 1.909\ \mathrm{km}.
$$

So the thermal part $S(\infty)-S(0)$ is

$$
1.115\ \mathrm{km}\ (\beta = 1.5), \qquad 0.662\ \mathrm{km}\ (\beta = 1.25),
$$

and it is **not** a simple multiple of the crustal term: the crustal term grows
by $2.688/1.612 = 1.667$ while the thermal term grows by
$1.115/0.662 = 1.684$. They differ because the thermal part contains two
physically distinct contributions:

- $B(1-1/\beta)$, which is large *because the initial column was hot*
  ($B\times0.333 = 0.610\ \mathrm{km}$ at $\beta = 1.5$) — this is subsidence
  caused by removing the hot-mantle buoyancy the stretched column started with;
- $C[(a-t_{c0}/\beta)^{2}-(a-t_{c0})^{2}]$, the genuine cooling of the thinned
  mantle lithosphere to the equilibrium geotherm ($0.505\ \mathrm{km}$ at
  $\beta = 1.5$).

The ratio (thermal)/(crustal) drifts slowly upward with $\beta$
($0.411 \to 0.414$ over $1.25 \to 1.5$), so "both scale as $(1-1/\beta)$" is an
approximation good to a few per cent, and it fails badly if the two terms are
given separate physical interpretations without the two-part split above.

---

## ★6 — Correcting a biased decay constant

The demonstration measured a fitted $\tau$ that is $3.2\%$ **long** when fitted
from $t=0$ over $0$–$200\ \mathrm{Myr}$ (fitted $51.77$ against analytic
$50.17$), and unbiased when fitted after $25\ \mathrm{Myr}$.

That bias direction is specific to a fit over the whole curve; the problem
statement's $\tau = 43\ \mathrm{Myr}$ is shorter than the analytic value for
$a = 125\ \mathrm{km}$ ($50.17\ \mathrm{Myr}$), which is the signature of a
**thick-lithosphere** or **viscosity** mismatch rather than of the fitting
window. Applying the demonstration's bias naively would push the value up to
$43\times1.032 \approx 44.4\ \mathrm{Myr}$.

The defensible answer: the refit-after-$25\ \mathrm{Myr}$ value is the one to
compare with $a^{2}/(\pi^{2}\kappa)$, because that is the regime in which the
solution is dominated by the first eigenmode and the analytic result applies.
The from-$t=0$ value contains the kink of the initial condition and is biased
long by a few per cent; the correction is small but larger than the precision at
which such fits are usually reported.

---

## ★7 — From subsidence to $\beta$ with an uncertainty

$$
S(0) = \left(1-\frac{1}{\beta}\right)(A-B) \quad\Rightarrow\quad
\beta = \left(1 - \frac{S}{A-B}\right)^{-1}.
$$

For $S = 3.4\ \mathrm{km}$ and $A - B = 6.236\ \mathrm{km}$:
$1 - 0.545 = 0.455$, so $\beta = 2.198$.

For $S = 3.1\ \mathrm{km}$: $1 - 0.497 = 0.503$, $\beta = 1.987$.
For $S = 3.7\ \mathrm{km}$: $1 - 0.593 = 0.407$, $\beta = 2.457$.

So $\beta = 2.20^{+0.26}_{-0.21}$ for a $\pm0.3\ \mathrm{km}$ subsidence
uncertainty. The asymmetry is real and comes from the $1/\beta$ non-linearity.

Dominant contribution: $\partial\beta/\partial S = \beta^{2}/(A-B)
= 4.83/6.236 = 0.775$ per km, whereas the density sensitivity enters through
$A - B$. With densities known to $1\%$,
$A = 530\times35/2300 = 8.065$ and a $1\%$ change in
$(\rho_m-\rho_c)$ changes $A$ by $0.081\ \mathrm{km}$; a $1\%$ change in
$(\rho_m - \rho_w)$ changes $A$ by $0.081\ \mathrm{km}$ in the opposite sense.
These are an order of magnitude smaller than the $0.3\ \mathrm{km}$ subsidence
error. **The subsidence measurement dominates**, provided the crustal thickness
used to convert water depth to $\beta$ is itself secure.

---

## ★8 — Crust-only thinning

**Derivation.** With the crust thinned to $t_{c0}/\beta_f$ and the mantle
lithosphere unchanged,

$$
\Phi_{\text{str}}(0) = (\rho_c-\rho_m)\frac{t_{c0}}{\beta_f}
+ \rho_m\alpha T_m\frac{(a-t_{c0})^{2}}{2a},
$$

because the mantle part of the deficit is identical to the reference column's
(same thickness, same temperature). The crustal term scales by $1/\beta_f$ and
the mantle term cancels exactly:

$$
\Phi_{\text{str}} - \Phi_{\text{ref}}
= (\rho_m-\rho_c)t_{c0}\left(1-\frac{1}{\beta_f}\right),
$$

$$
\boxed{\;S(0) = \left(1-\frac{1}{\beta_f}\right)A\;}
$$

with $A = 8.065\ \mathrm{km}$. At $\beta_f = 1.5$:
$S(0) = 0.3333\times8.065 = 2.688\ \mathrm{km}$.

**Comparison with uniform stretching at the same $\beta$.** Uniform gives
$(1-1/\beta)(A-B) = 2.079\ \mathrm{km}$. The ratio is

$$
\frac{S_{\text{crust-only}}}{S_{\text{uniform}}}
= \frac{A}{A-B} = \frac{8.065}{6.236} = 1.293 ,
$$

that is $+609\ \mathrm{m}$, or $+29\%$. The reason is exactly the $B$ term: the
uniform model's freshly stretched mantle lithosphere is *hot* and therefore
buoyant, which suppresses the initial subsidence. Thinning only the crust leaves
a cold, dense mantle lithosphere in place, so there is no such buoyancy bonus
and the margin subsides as much as the crustal thinning alone demands.

**Post-rift thermal subsidence.** Essentially none in this limit. Thermal
subsidence requires a thinned mantle lithosphere to cool; with $\beta_m = 1$ the
thermal structure is never perturbed, so $S(\infty) = S(0)$. The model predicts a
margin with a large syn-rift subsidence and a flat post-rift sag.

**Distinguishing observation.** The ratio of post-rift thermal subsidence to
initial subsidence. Uniform stretching predicts
$[S(\infty)-S(0)]/S(0) = 0.54$ at $\beta = 1.5$ (from ★5: $1.115/2.079$).
Crust-only thinning predicts $\approx 0$. A margin that subsided several
kilometres during rifting and then recorded almost no thermal sag is telling
you that the mantle lithosphere was not thinned — or that the subsidence was
not caused by stretching at all. Heat flow and gravity give the independent
check on mantle-lithosphere thickness.

*(A caution: in this derivation the mantle lithosphere's temperature structure
is left completely untouched. Real depth-dependent stretching lies between this
end-member and the uniform model, and a quantitative treatment needs an explicit
pre-rift geotherm and the material mapping $z \mapsto z'$ during stretching —
neither of which is avoidable if the numbers matter.)*

---

## ★9 — One rift or two? (specification)

**Data.** A water-loaded, decompacted backstrip curve on a margin, sampled at
$\ge 20$ horizons spanning $0$–$120\ \mathrm{Myr}$ after break-up, each with an
independent depth uncertainty (from biostratigraphy and decompaction, typically
$\pm 100$–$300\ \mathrm{m}$).

**Models.** (i) $S(t) = S_0 + S_{th}[1-e^{-t/\tau}]$ with $\beta$ and $\tau$
free. (ii) Two events: $\beta_1$ at $t=0$, then $\beta_2$ at $t = \Delta t$, with
the thermal subsidence being the sum of two decaying contributions and the
initial subsidence the isostatic sum of the two stretching increments.

**Metric.** $\chi^{2}$ per degree of freedom, plus an $F$-test or an
information criterion (AIC/BIC) because the models have different parameter
counts. Report the recovered parameters with a covariance, and the correlation
between $\Delta t$ and $\beta_2$.

**Indistinguishability.** The two models converge when
$\Delta t \ll \tau$: the second event's thermal anomaly is then still
near its initial amplitude, and the pair $(\beta_1, \beta_2)$ is equivalent to a
single $\beta$ to within the noise, with $\Delta t$ degenerate with the
amplitudes. Quantitatively, expect degeneracy when
$\Delta t \lesssim 0.2\tau$ (here $\lesssim 10\ \mathrm{Myr}$) **and** the
sampling interval exceeds $\Delta t$. The experiment therefore has to be
designed with a sampling interval shorter than the rift duration it hopes to
resolve.
