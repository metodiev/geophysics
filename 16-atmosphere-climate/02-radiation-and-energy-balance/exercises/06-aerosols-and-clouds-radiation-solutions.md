# Solutions — 16-02-06 Aerosols, Clouds and Their Radiative Effects

Numbers below were computed, not estimated. All models are **SYNTHETIC**. Lesson:
[06 Aerosols, Clouds and Their Radiative Effects](../06-aerosols-and-clouds-radiation.md).

---

## ★1 — Optical depth from water path

Geometric relation, $\text{LWP} = 50\ \mathrm{g\,m^{-2}} = 0.05\ \mathrm{kg\,m^{-2}}$:

$$\tau = \frac{3\,\text{LWP}}{2\rho_wr_e}.$$

| $r_e$ ($\mu$m) | $3/(2\rho_wr_e)$ (m² kg⁻¹) | $\tau$ (geometric) | interpolated ratio | corrected $\tau$ |
|---|---|---|---|---|
| 8 | $3/(2\times1000\times8\times10^{-6}) = 187.5$ | $187.5\times0.05 = 9.375$ | 1.0559 | 9.899 |
| 16 | $3/(2\times1000\times1.6\times10^{-5}) = 93.75$ | $93.75\times0.05 = 4.688$ | 1.0349 | 4.851 |

The interpolations are linear in $r_e$ between the tabulated ratios: between
$5\ \mu$m (1.0721) and $10\ \mu$m (1.0451),
$1.0451 + \tfrac{8-10}{5-10}(1.0721-1.0451) = 1.0559$; between $15\ \mu$m (1.0368)
and $20\ \mu$m (1.0272),
$1.0368 + \tfrac{16-15}{20-15}(1.0272-1.0368) = 1.0349$.

**Which matters more, and why.** The *relative* correction is larger at the
smaller radius (5.6% at $8\ \mu$m against 3.5% at $16\ \mu$m), because
$Q_{\text{ext}} - 2$ is an oscillation whose amplitude decreases as the size
parameter grows: $x = 2\pi r/\lambda = 91.4$ at $r_e = 8\ \mu$m and 182.8 at
$16\ \mu$m. The *absolute* error is nevertheless larger at the smaller radius
(0.52 in $\tau$ against 0.16), because the optical depth itself is larger there.
Note also that the geometric formula's inverse dependence on $r_e$ dominates: the
ratio of the two optical depths is $9.375/4.688 = 2.0$, i.e. exactly the inverse
radius ratio, and the Mie correction only shifts it to $9.899/4.851 = 2.04$.

---

## ★2 — Emissivity and longwave forcing

$$\tau_{\text{abs}} = k_{\text{abs}}\,\text{LWP} = 49.94\ \mathrm{m^2\,kg^{-1}}
\times 0.030\ \mathrm{kg\,m^{-2}} = 1.4982,$$

$$\varepsilon = 1 - e^{-1.4982} = 1 - 0.22353 = 0.77647,$$

$$T_c = T_s - \Gamma z = 288.15 - 6.5\times3 = 268.65\ \mathrm{K},$$

$$\sigma T_s^4 = 5.670374419\times10^{-8}\times288.15^4 = 390.92\
\mathrm{W\,m^{-2}},\qquad
\sigma T_c^4 = 5.670374419\times10^{-8}\times268.65^4 = 295.37\
\mathrm{W\,m^{-2}},$$

$$\text{CF}_{\text{LW}} = 0.77647\times(390.92 - 295.37) = 0.77647\times95.55
= 74.2\ \mathrm{W\,m^{-2}}.$$

**What the number is and is not.** It is a longwave *overcast scene* forcing for
stated modelling choices ($T_s$, $\Gamma$, $\varepsilon$ from one synthetic
population). It is **not** a measured forcing and it carries no cloud-fraction
information; the observed counterpart would require the joint distribution of
cloud fraction, height and water path.

---

## ★3 — Slope of the albedo–optical-depth relation

$$\left.\frac{\mathrm{d}A}{\mathrm{d}\tau}\right|_{[5,10]} = \frac{0.5330-0.3703}{5}
= 0.03255,\qquad
\left.\frac{\mathrm{d}A}{\mathrm{d}\tau}\right|_{[10,20]} = \frac{0.6907-0.5330}{10}
= 0.01577 .$$

The slope falls by a factor of 2.06 across the two intervals. **Meaning:** the
albedo has no upper room left — each additional unit of optical depth reflects
proportionally less additional light, because the layer is already approaching its
saturating reflectance, and the only way to raise it further is to make the
reflectance itself larger rather than the layer thicker. This is the reason the
Twomey effect is a small effect, and the reason it is largest for clouds in the
middle of the range ($\tau$ of order a few) rather than for thick ones.

---

## ★4 — Which identity follows from which equation

In the lesson's notation $S = F_\uparrow + F_\downarrow$ and
$D = F_\uparrow - F_\downarrow$, with $D(0) = S(0)$ at the top (no incoming
diffuse radiation) and, for a black surface, $F_\uparrow(\tau_{\text{tot}}) = 0$
so $D(\tau_{\text{tot}}) = -S(\tau_{\text{tot}})$.

For $\omega_0 = 1$ the flux-difference equation is

$$\frac{\mathrm{d}D}{\mathrm{d}\tau} = 2(1-\omega_0)S - \omega_0F_0e^{-\tau/\mu_0}
= -F_0e^{-\tau/\mu_0},$$

which integrates immediately:

$$D(\tau_{\text{tot}}) = D(0) - \mu_0F_0\left(1 - e^{-\tau_{\text{tot}}/\mu_0}\right)
\;\Longrightarrow\;
D(0) = -S(\tau_{\text{tot}}) + \mu_0F_0\left(1-e^{-\tau_{\text{tot}}/\mu_0}\right).$$

Now the reflected fraction is $R = F_\uparrow(0)/(\mu_0F_0) = D(0)/(\mu_0F_0)$ (since
$F_\downarrow(0) = 0$) and the transmitted fraction is
$T = \bigl[F_\downarrow(\tau_{\text{tot}}) + \mu_0F_0e^{-\tau_{\text{tot}}/\mu_0}\bigr]
/(\mu_0F_0) = \bigl[S(\tau_{\text{tot}}) + \mu_0F_0e^{-\tau_{\text{tot}}/\mu_0}\bigr]
/(\mu_0F_0)$. Adding them:

$$R + T = \frac{-S(\tau_{\text{tot}}) + \mu_0F_0(1-e^{-\tau_{\text{tot}}/\mu_0})
+ S(\tau_{\text{tot}}) + \mu_0F_0e^{-\tau_{\text{tot}}/\mu_0}}{\mu_0F_0} = 1 .$$

**The $S$ terms cancel identically.** Nothing about the flux-sum equation, the
closure, the phase function or the asymmetry parameter enters: the identity is a
statement of energy conservation, and energy conservation is entirely contained in
the flux-difference equation. That is also why the two closures tested in the
demonstration both satisfy it to $10^{-16}$ while their *albedos* differ by tens of
per cent.

**Which identity fails for an absorbing layer.** Identities 1 and 2 (no absorption,
hence $R + T = 1$; and $R = 1$ for a white surface) require $\omega_0 = 1$ and fail
once $\omega_0 < 1$, because energy is then genuinely absorbed and
$R + T = 1 - \text{absorptance}$. Identity 3 ($R = 0$, $T = e^{-\tau/\mu_0}$ at
$\omega_0 = 0$) holds for any $\omega_0 = 0$ layer because there is then no diffuse
source at all, and it fails only if a diffuse source is introduced by a scattering
surface or an imperfect bottom boundary condition.

---

## ★5 — The indirect effect for a fourfold increase in droplet number

At fixed liquid-water path, $\text{LWP} \propto N_d r_e^3$ gives
$r_e \propto N_d^{-1/3}$, and $\tau \propto 1/r_e \propto N_d^{1/3}$:

$$r_e = 10/4^{1/3} = 6.300\ \mu\mathrm{m},\qquad
\tau = 15.676\times4^{1/3} = 24.88 .$$

From the delta-Eddington albedo curve, $A(24.88) = 0.7344$, so

$$\Delta A = 0.7344 - 0.6380 = +0.0965 .$$

The asymptotic prediction is

$$\frac{A(1-A)}{3}\ln 4 = \frac{0.6380\times0.3620}{3}\times1.3863 = 0.1062 ,$$

so the asymptotic form **overestimates the exact change by 10%** ($0.1062$ against
$0.0965$). The reason is that the exact sensitivity is not constant along the path:
$A$ rises from 0.638 to 0.734, and the integrand $A(1-A)/3$ falls from 0.0770 to
0.0650 over the same interval (lesson §3.6 table), so an evaluation at the initial
state overestimates the average. **An effect of 0.096 in albedo for a fourfold
change in droplet number is small; detecting it against a 2 per cent radiometric
error is the subject of ★10.**

---

## ★6 — Sign of the aerosol direct effect

Thin-layer criterion, with $r = (\alpha_s-1)/(\alpha_s+1)$:

$$\left.\frac{\mathrm{d}\alpha}{\mathrm{d}\tau_a}\right|_{0}
= \frac{q + r(a\alpha_s\mu_0 + p) - c\alpha_s\mu_0 - \frac{2\alpha_s}{1+\alpha_s}}
{\mu_0(1-r)},\qquad
a = \tfrac32(1-\omega_0g),\ c = 2(1-\omega_0),\ p = \tfrac32\omega_0g\mu_0,\ q = \omega_0 .$$

**(a)** $g = 0.3$, $\mu_0 = 0.6$, $\alpha_s = 0.3$, $\omega_0 = 0.85$:
$r = -0.7/1.3 = -0.53846$, $1-r = 1.53846$,
$a = 1.5(1-0.255) = 1.1175$, $c = 0.3$, $p = 1.5\times0.85\times0.3\times0.6 = 0.2295$,
$q = 0.85$, $2\alpha_s/(1+\alpha_s) = 0.46154$.

Numerator:
$0.85 + (-0.53846)(1.1175\times0.3\times0.6 + 0.2295) - 0.3\times0.3\times0.6 - 0.46154$
$= 0.85 - 0.53846(0.20115+0.2295) - 0.054 - 0.46154$
$= 0.85 - 0.53846(0.43065) - 0.51554 = 0.85 - 0.23189 - 0.51554 = +0.10257 .$

Dividing by $\mu_0(1-r) = 0.6\times1.53846 = 0.92308$:
$\mathrm{d}\alpha/\mathrm{d}\tau_a = +0.1111$. **The layer brightens the scene**
(a thin layer with $\omega_0 = 0.85$ over a surface of albedo $0.30$ reflects more
than the absorption removes).

**(b)** Bisecting the numerator for a sign change at $\alpha_s = 0.3$ gives the
critical value $\omega_0 = 0.7685$. Below it the layer dims, above it it brightens.

**(c)** Increasing $g$ to 0.6 raises the critical single-scattering albedo to
$0.8361$, and at $\omega_0 = 0.85$ the slope falls from $+0.1111$ to $+0.0174$
(computed from the same expression with $g = 0.6$). **Physically:** a larger $g$
means the particle scatters more of what it intercepts into the forward
direction, so less of it comes back out of the top as diffuse reflection. The
layer must therefore be a better scatterer (larger $\omega_0$) merely to break
even, and near the threshold the effect is much weaker. In the limit $g \to 1$ the
particle is a pure forward scatterer and the direct effect on the planetary albedo
vanishes entirely, whatever $\omega_0$ is.

---

## ★7 — Phase-function truncation

$$b_{\text{Edd}} = \tfrac12\left(1 - \tfrac32g\mu_0\right),\qquad \mu_0 = 0.6 .$$

| $g$ | $b_{\text{Edd}}$ | exact azimuth-averaged HG $b$ | ratio |
|---|---|---|---|
| 0.70 | $\tfrac12(1-0.63) = 0.1850$ | 0.1468 | 1.260 |
| 0.8619 | $\tfrac12(1-0.7757) = 0.1121$ | 0.0613 | 1.829 |

Also worth computing: the ratio is exactly 1 at $g = 0$ (isotropic scattering is
represented exactly by the first two moments), 1.011 at $g = 0.30$, 1.26 at
$g = 0.70$ and 1.83 at $g = 0.86$. **The closure error is not a constant of the
method; it is a function of how forward-peaked the phase function is.**

**Why delta-Eddington scaling helps.** The truncation error arises because a
two-moment representation of the phase function cannot distinguish a narrow
diffraction peak near $\Theta = 0$ from the rest of the forward lobe: the Eddington
quadrature effectively counts part of that peak as backscatter. Delta-Eddington
scaling removes the peak analytically,
$p' = (1-g^2)\delta(\Theta) + g^2p_{\text{HG}}(g')$ with $g' = g/(1+g)$, and
renormalises $\tau$ and $\omega_0$ accordingly. The remaining phase function has
$g' = 0.463$ instead of $0.862$, i.e. it is far better represented by two moments:
the measured thin-layer ratio falls from 1.829 to 1.224, and it *improves* with
$\tau$ (1.224 at $\tau = 0.002$ to 1.191 at $\tau = 0.2$) because the neglected
multiple scattering contributes at order $\tau^2$. The residual 22 per cent is the
honest accuracy of this closure for an albedo at this asymmetry.

---

## ★8 — Validation protocol for a two-stream reflectance code

Strongest to weakest, with the failure signature of each:

1. **Exact energy identities.** $\omega_0 = 1$ with a black surface must give
   $R + T = 1$ to machine precision at every $\tau$; $\omega_0 = 1$ with a white
   surface must give $R = 1$ exactly; $\omega_0 = 0$ must give
   $T = e^{-\tau/\mu_0}$ and $R = 0$. *Failure signature:* residuals that scale like
   $\tau$ rather than vanishing — a normalisation or sign error, not a
   discretisation error. These are algebraic, so no tolerance is needed beyond
   round-off.
2. **Independent solution of the same equations.** Discretise the two-point
   boundary-value problem (second-order finite differences, a few hundred cells)
   and compare. *Failure signature:* a difference that grows with $\tau$ or with
   the number of cells — an implementation error in the closed-form algebra, since
   the equations are identical.
3. **Grid convergence of that independent solution.** *Failure signature:* the
   difference from the closed form stops decreasing like $h^2$; a boundary-condition
   treatment error at one end.
4. **Analytic thin-layer limit.** $R/\tau \to b(\mu_0)/\mu_0$ as $\tau \to 0$, where
   $b$ is the backscattered beam fraction of the phase function used. *Failure
   signature:* a ratio that does not approach the phase-function value — the wrong
   beam sign in the flux-sum equation (this check is the only one in the list that
   the energy identities cannot detect, because they are insensitive to the flux
   sum).
5. **Reciprocity / consistency checks.** $R(\mu_0)$ computed from the model at two
   values of $\mu_0$ must satisfy the symmetry properties expected of the
   directional-hemispherical reflectance for the symmetric part of the phase
   function; and the albedo must be monotone increasing in $\tau$, in $\omega_0$
   and in $\alpha_s$. *Failure signature:* non-monotonicity in the grid of
   parameters — usually a sign error that only shows up away from the tested
   identities.
6. **Asymptotic behaviour.** $R \to 1$ as $\tau \to \infty$ for $\omega_0 = 1$ and
   $\mu_0 > 0$; $R \to 0$ as $\omega_0 \to 0$; $\varepsilon \to 1$ as
   $\tau_{\text{abs}} \to \infty$. *Failure signature:* saturation at a value other
   than the limit — a normalisation error in the source terms.

**The extra check not in the lesson:** a *brightness-scaling* test. For a
conservative layer over a black surface, the reflectance of the system
"layer + layer" built by the adding method from two identical half-layers must
equal the reflectance of a single layer of twice the optical depth, to the
accuracy of the adding method. It tests the *composition* property of the
solution, which none of the checks above does, and it catches errors that are
invisible for a single homogeneous slab (for instance a boundary condition that is
correct at the top and bottom but wrong internally).

---

## ★9 — Critique of the cloud-radiative-forcing decomposition

**Model artefacts rather than physics.**

1. **The shortwave term uses a two-stream albedo**, whose truncation error is
   $\approx +22\%$ (delta-Eddington) to $+83\%$ (plain Eddington) at small $\tau$.
2. **The longwave term uses a single emissivity** $\varepsilon = 1-e^{-\tau_{\text{abs}}}$
   with $\tau_{\text{abs}}$ from a grey absorption coefficient. Real infrared
   transfer is spectrally selective; the grey model forces all the longwave energy
   through one channel.
3. **The cloud temperature is prescribed** by $T_s - \Gamma z$ from stated
   conventions. The longwave forcing is proportional to
   $\sigma T_s^4 - \sigma T_c^4$, so it is proportional to that choice.
4. **The clear-sky albedo (0.12) and the surface albedo beneath the cloud (0.12)
   are inputs.** The shortwave forcing is the difference of two model states, so it
   inherits both.

**Closure sensitivity, quantified.** At $\text{LWP} = 5\ \mathrm{g\,m^{-2}}$,
$R_\delta = 0.1904$ and $R_{\text{plain}} = 0.2086$, a difference of $0.0182$,
which at $\mu_0S = 816.6\ \mathrm{W\,m^{-2}}$ is $14.9\ \mathrm{W\,m^{-2}}$ of
shortwave forcing — larger than the entire net forcing at that water path
($+4.45\ \mathrm{W\,m^{-2}}$) and of the same sign as the cloud's cooling.
At $\text{LWP} = 20\ \mathrm{g\,m^{-2}}$ the spread is
$(0.3496-0.3409)\times816.6 = 7.1\ \mathrm{W\,m^{-2}}$, while the net forcing there
is $-3.3\ \mathrm{W\,m^{-2}}$. **In other words, the closure error at small and
moderate water path is several times the size of the net effect the model is trying
to describe.** The *sign structure* survives — thin high cloud still warms, thick
low cloud still cools — because both closures shift the shortwave term in the same
direction; the *crossover water path* does not survive and must not be quoted.

**What a global mean would require.** The joint distribution of (i) cloud
fraction, (ii) cloud height, (iii) liquid-water path and effective radius, (iv)
solar zenith angle and insolation, and (v) surface albedo, together with the
correlation between them (high clouds are systematically thinner, low clouds are
systematically thicker and warmer, and the insolation at a given cloud depends on
latitude and season). The global mean is the double integral of the local forcing
weighted by that distribution — it is **not** the sum, and not the product by any
single cloud fraction, of the numbers in the lesson's tables.

---

## ★10 — Design of a detection experiment

**Observable.** The scene reflectance (or the albedo) at the top of the atmosphere
at a fixed solar geometry, plus the liquid-water path from a passive microwave
retrieval — both *measured* quantities in the synthetic experiment.

**Retrieval.** The optical depth $\tau$ is *retrieved* by inverting the modelled
$R(\tau,\mu_0)$; the effective radius is then *retrieved* from $\tau$ combined with
LWP through $\tau = 3\,\text{LWP}/(2\rho_wr_e)$; the droplet number follows from
$r_e \propto N_d^{-1/3}$ and is the most *modelled* quantity in the chain.

**Error propagation.** With a 2 per cent relative error on $R$ and the sensitivity
$\mathrm{d}R/\mathrm{d}\tau$ from the model, the error on the retrieved $\tau$ is
$\sigma_\tau \approx 0.02\,R/(\mathrm{d}R/\mathrm{d}\tau)$. From the lesson's
synthetic retrieval, that is $\pm0.1$ at $\tau = 2$ and $\pm2.6$ at $\tau = 32$:
the *same* radiometric error gives a 26-fold larger optical-depth error at the
larger optical depth, because the albedo saturates. Propagating onward: with a 10
per cent error on LWP, the error on $r_e$ is at least 10 per cent, and the error
on a change in $N_d$ is the sum of both, in quadrature:
$\sigma_{\ln N_d} \approx 3\sqrt{(\sigma_{\ln r_e})^2}$, because
$\ln N_d = -3\ln r_e + \text{const}$ at fixed LWP.

**Confounders to exclude.** (i) A change in LWP at unchanged droplet number changes
$\tau$ and therefore albedo, mimicking the effect; (ii) a change in cloud fraction
or geometry changes the scene reflectance without any microphysical change;
(iii) a change in the surface albedo beneath a thin cloud changes the scene
albedo through the multiple-reflection term; (iv) a change in the aerosol
environment changes the direct effect and hence the background; (v) sampling bias
if the observations are not matched in solar geometry, season and location.
A defensible design holds (i), (ii), (iii) and (v) fixed by construction or by
stratification, and reports the residual dependence on (iv) as a systematic.

**Conclusion you would be entitled to draw.** At most: *the retrieved optical
depth is larger in the high-droplet-number population at fixed liquid-water path
by more than the propagated uncertainty, with the listed confounders controlled*.
That is an inference about the model-derived quantity $r_e$, not a measurement of
droplet number, and it is not a measurement of a radiative forcing: a forcing is a
difference between two *model* states, and it requires the response of all
simultaneously varying variables to be calculated, not one of them.

**Status summary for the design.** Measured: reflectance, liquid-water path.
Retrieved: optical depth, effective radius. Modelled: droplet number, albedo
change attributable to droplet number, and any forcing computed from it.
