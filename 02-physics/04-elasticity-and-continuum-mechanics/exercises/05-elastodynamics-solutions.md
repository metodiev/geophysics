# Solutions — 02-04-05 Elastodynamic Equation of Motion and Wave Speeds

> **Read this after attempting the exercises, not before.** This is the mastery
> lesson; the solutions are written as full derivations where the exercises ask
> for one. Values attributed to the demo are its actual output.

---

## ★1 — The full derivation

**(a)** The three ingredients, with their physical content:

1. Balance of momentum (Newton's second law for a continuum):
   $\partial_j\sigma_{ij} + \rho g_i = \rho\ddot u_i$.
2. Strain–displacement (kinematics): $\varepsilon_{ij} =
   \tfrac12(u_{i,j}+u_{j,i})$.
3. Isotropic linear elasticity (material):
   $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$.

**(b)** Substituting ingredient 3 into ingredient 1, and taking $\lambda$ and
$\mu$ constant (homogeneity) and $\mathbf g = \mathbf 0$:

$$\rho\ddot u_i = \partial_j\left(\lambda\varepsilon_{kk}\delta_{ij}
+ 2\mu\varepsilon_{ij}\right)
= \lambda\,\partial_i u_{k,k} + \mu\left(\nabla^2u_i + \partial_i u_{k,k}\right)
= (\lambda+\mu)\,\partial_i(\nabla\cdot\mathbf u) + \mu\nabla^2u_i ,$$

which in vector form is
$\rho\ddot{\mathbf u} = (\lambda+\mu)\nabla(\nabla\cdot\mathbf u) +
\mu\nabla^2\mathbf u$ — the Navier–Cauchy equation.

**(c)** With $\mathbf u = \nabla\phi + \nabla\times\boldsymbol\psi$ and
$\nabla\cdot\boldsymbol\psi = 0$: $\nabla\cdot\mathbf u = \nabla^2\phi$ and
$\nabla^2\mathbf u = \nabla(\nabla^2\phi) + \nabla\times(\nabla^2\boldsymbol\psi)$.
Substituting and collecting,

$$\nabla\left[\rho\ddot\phi - (\lambda+2\mu)\nabla^2\phi\right]
+ \nabla\times\left[\rho\ddot{\boldsymbol\psi} - \mu\nabla^2\boldsymbol\psi\right]
= \mathbf 0 .$$

The two brackets have independently zero divergence and curl parts, so each
vanishes, giving

$$\ddot\phi = v_p^2\nabla^2\phi, \quad v_p^2 = \frac{\lambda+2\mu}{\rho};
\qquad
\ddot{\boldsymbol\psi} = v_s^2\nabla^2\boldsymbol\psi, \quad
v_s^2 = \frac{\mu}{\rho} .$$

**(d)** P wave: $\mathbf u = A\hat{\mathbf k}e^{i(\mathbf k\cdot\mathbf x-\omega t)}$
gives $\nabla(\nabla\cdot\mathbf u) = -k^2\mathbf u$ and
$\nabla^2\mathbf u = -k^2\mathbf u$, so
$\rho\omega^2 = (\lambda+\mu)k^2+\mu k^2 = (\lambda+2\mu)k^2$ → $v_p$ ✓.
S wave: $\hat{\mathbf e}_s\perp\hat{\mathbf k}$ gives
$\nabla\cdot\mathbf u = 0$, so $\rho\omega^2 = \mu k^2$ → $v_s$ ✓.

---

## ★2 — A crustal rock

**(a)** $M = \lambda+2\mu = 20+44 = 64$ GPa;
$v_p = \sqrt{64\times10^9/2500} = \sqrt{2.56\times10^7} = 5059.64$ m s⁻¹;
$v_s = \sqrt{22\times10^9/2500} = \sqrt{8.8\times10^6} = 2966.48$ m s⁻¹;
ratio 1.705606.

**(b)** $K = \lambda+2\mu/3 = 20+14.666667 = 34.666667$ GPa;
$\nu = \lambda/[2(\lambda+\mu)] = 20/84 = 0.238095$.

**(c)** $K/\mu+4/3 = 34.666667/22+1.333333 = 1.575758+1.333333 = 2.909091$, whose
square root is 1.705606 ✓;
$2(1-\nu)/(1-2\nu) = 2\times0.761905/0.523810 = 2.909091$ ✓.

**(d)** $v_p \approx 5.06$ km s⁻¹ and $v_s \approx 2.97$ km s⁻¹ with
$\nu = 0.238$: plausible for a low-porosity crystalline rock or a well-cemented
sandstone at modest depth. A quartz-rich granite is usually a little faster
(5.5–6.0 km s⁻¹), so this parameter set is on the low side but well within the
range of crustal rocks.

---

## ★3 — A grout

**(a)** Careful: the problem gives $K = 4$ GPa and $\mu = 1.5$ GPa, *not*
$\lambda$. Since $\lambda = K-\frac23\mu = 4-1 = 3$ GPa, we have
$M = \lambda+2\mu = 6$ GPa, so
$v_p = \sqrt{6\times10^9/1400} = \sqrt{4.285714\times10^6} = 2070.20$ m s⁻¹;
$v_s = \sqrt{1.5\times10^9/1400} = \sqrt{1.071429\times10^6} = 1035.10$ m s⁻¹.

**(b)** $v_p/v_s = 2070.20/1035.10 = 2.000000$. Check by the independent route:
$v_p^2/v_s^2 = (K+\frac43\mu)/\mu = (4+2)/1.5 = 4.000000$ ✓, whose square root
is exactly 2. Both bounds of §4.1 of the lesson are satisfied
($2 > 2/\sqrt3$ and $2 > \sqrt2$), as required since this material has
$\lambda = 3$ GPa $> 0$. The two-route check is what caught the temptation to use
$M = K+2\mu$ (i.e. to confuse $\lambda$ with $K$), which would have given
$v_p = 2236.07$ m s⁻¹ and a ratio of 2.160246 — a 8 per cent velocity error from
one symbol confusion.

**(c)** The P-wave polarisation is exactly parallel to the propagation direction
(longitudinal), by definition of the P mode: $\mathbf u \parallel \hat{\mathbf k}$.
The physical reason is that the restoring force comes from the divergence term
$\nabla(\nabla\cdot\mathbf u)$, which points along the gradient of the dilatation —
i.e. along $\mathbf k$ for a plane wave.

**(d)** With $\mu$ rising from 1.5 to 6 GPa and $\lambda$ unchanged at 3 GPa,
$M = 3+12 = 15$ GPa:
$v_p = \sqrt{15\times10^9/1400} = \sqrt{1.071429\times10^7} = 3273.21$ m s⁻¹ and
$v_s = \sqrt{6\times10^9/1400} = \sqrt{4.285714\times10^6} = 2070.20$ m s⁻¹. The
P speed rises by 58 per cent and the S speed by 100 per cent:
**a change in $\mu$ affects $v_s$ twice as much in the squared ratio**, which is
why $v_s$ is the more sensitive indicator of setting, cracking or any process that
changes the shear stiffness.

---

## ★4 — Fluids and shear

**(a)** With $\mu = 0$: $\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij}
= -p\delta_{ij}$ with $p = -K\varepsilon_{kk}$ (and $\lambda = K$ when $\mu = 0$).
The stress is purely isotropic: a fluid can push but cannot shear.

**(b)** The shear equation becomes
$\ddot{\boldsymbol\psi} = 0$: the vector potential does not evolve, so there is no
propagating shear disturbance. Physically, a shear displacement produces no
restoring stress, so no force acts to reverse it and no wave exists.

**(c)** $v_p = \sqrt{2.2\times10^9/1000} = 1483.2397$ m s⁻¹.

**(d)** A measured $v_s = 100$ m s⁻¹ implies $\mu = \rho v_s^2$; with
$\rho = 2200$ kg m⁻³ that is $\mu = 2.2\times10^7$ Pa = 22 MPa. The rock is
therefore not a fluid at the measurement frequency: it has a small but finite
shear stiffness, which is entirely normal for a saturated rock (the *frame*
carries the shear, not the fluid) and would only be surprising for a genuinely
liquid-filled cavity with no solid frame.

---

## ★5 — Reading the demo

**(a)** $v_p = 5610.836077$ m s⁻¹, $v_s = 3333.333333$ m s⁻¹,
$v_p/v_s = 1.683250823$.

**(b)** Poisson solid ($\lambda = \mu = 30$ GPa): $v_p = 5773.5027$ m s⁻¹,
$v_s = 3333.3333$ m s⁻¹, ratio 1.732050808, and $\sqrt3 = 1.732050808$ ✓ to ten
digits.

**(c)** Water: $v_p = 1483.2397$ m s⁻¹, $v_s = 0$.

**(d)** The single responsible parameter is $\mu$: 30 GPa in granite against 0 in
water, a factor of infinity, which becomes a factor of infinity in $v_s$ and a
factor of $\sqrt{85/2.2} = 6.2$ in $v_p$. The $v_s$ difference is qualitative (a
wave exists or does not); the $v_p$ difference is merely large.

---

## ★6 — Mastery problem: the formulas

**(a)** $v_p^2 = M/\rho$ with $M = \lambda+2\mu = K+\frac43\mu$: the P speed
measures the **uniaxial-strain (constrained) modulus** and density.
$v_s^2 = \mu/\rho$: the S speed measures the **shear modulus** and density. Only
$v_s$ is a pure shear measurement; $v_p$ mixes $K$ and $\mu$.

**(b)** Physically: a P wave is resisted by both the volumetric and the shear
stiffness, while an S wave is resisted only by the shear stiffness, so the P wave
always has more restoring force for the same inertia. Algebraically,
$v_p^2-v_s^2 = (\lambda+\mu)/\rho = (K+\mu/3)/\rho > 0$ since stability requires
$K>0$ and $\mu>0$; hence $v_p/v_s > 2/\sqrt3$.

**(c)** $\mu/\rho = v_s^2 = 4\times10^6$ m² s⁻², so
$\mu = 4\times10^6\rho$; $M/\rho = 1.6\times10^7$, so
$M = 1.6\times10^7\rho$ and $\lambda = M-2\mu = (1.6\times10^7-8\times10^6)\rho =
8\times10^6\rho$, giving $\lambda/\mu = 2$;
$K = \lambda+2\mu/3 = (8+2.666667)\times10^6\rho$, so
$K/\mu = 10.666667/4 = 2.666667$, and
$\nu = \lambda/[2(\lambda+\mu)] = 2/[2\times3] = 1/3 = 0.333333$. A rock with
$\nu = 1/3$ and $v_p/v_s = 2.0$ is plausible for a soft, water-saturated sediment
or a high-porosity rock without a strong mineral framework, so yes, plausible at
the soft end.

**(d)** $v_p/v_s = 4000/3900 = 1.025641$, so $K/\mu+4/3 = 1.051939$, giving
$K/\mu = -0.281394 < 0$. A negative bulk modulus means the material would expand
under hydrostatic compression, which violates the stability condition $K>0$; so
this pair of velocities is **not** consistent with a stable isotropic elastic
solid. The pair could be reconciled by anisotropy (in which case $v_p$ and $v_s$
refer to different directions and the isotropic formulas do not apply), by
dispersion (the two velocities measured at different frequencies in an attenuating
medium), or by a measurement error — the most common explanation in practice.

---

## ★7 — Mastery problem: partial saturation

**(a)** $\rho$ changes (the pore fluid's mass is added); $K$ (and hence $\lambda$
and $M$) changes, because the pore fluid's bulk modulus enters the saturated
modulus; **$\mu$ does not change**, because a fluid cannot support shear stress.

**(b)** $v_s = \sqrt{\mu/\rho}$ with $\mu$ fixed and $\rho$ increasing as fluid is
added, so **$v_s$ decreases**. Since neither $\mu$ nor the fluid distribution
enters, this holds for uniform and patchy saturation alike.

**(c)** $\rho_{\text{sat}} = \rho_{\text{dry}} + \phi\rho_w =
2150+0.25\times1000 = 2400$ kg m⁻³. With $\mu/\rho_{\text{dry}} = 2000^2 =
4\times10^6$ m² s⁻² the shear modulus is $4\times10^6\times2150 =
8.6\times10^9$ Pa = 8.6 GPa, so
$v_s^{\text{sat}} = \sqrt{8.6\times10^9/2400} = \sqrt{3.583333\times10^6} =
1892.97$ m s⁻¹ — a 5.35 per cent decrease.

**(d)** $v_p = \sqrt{(K_{\text{sat}}+4\mu/3)/\rho}$ requires $K_{\text{sat}}$, which
depends on the fluid *distribution* as well as its modulus and saturation. The two
bracketing models are (i) **Gassmann with a homogeneous fluid mixture** (Wood's
average for the fluid modulus), which is the low-frequency limit and predicts a
*dip* in $v_p$ for a gas sand; and (ii) the **patchy-saturation (Hill/Reuss)
average of the two fully saturated moduli**, which is an upper bound and predicts
$v_p$ above the Gassmann value at every intermediate saturation. Real data lie
between them, with the position set by the ratio of the patch size to the
diffusion length.

---

## ★8 — Reading the plane-wave and divergence checks

**(a)** P along $x$ and the $(1,1,1)$ direction: residual $0.000$ and
$5.82\times10^{-11}$; S: $2.91\times10^{-11}$. Relative residuals
$1.7\times10^{-16}$ to $2.3\times10^{-16}$, i.e. round-off.

**(b)** P field: $\nabla\cdot\mathbf u = -0.030257$, $|\nabla\times\mathbf u| =
0.000000$; S field: $\nabla\cdot\mathbf u = 0.000000$,
$|\nabla\times\mathbf u| = 0.030257$; mixed field: both $-0.030257$ and
$0.021913$.

**(c)** The mixed field is the sum of a gradient part and a curl part, so it has
both a non-zero divergence and a non-zero curl. A real seismic wavefield is
generally such a mixture: a P arrival and an S arrival overlap in time, so the
recorded displacement carries dilatation and rotation simultaneously. Separating
them requires either a 3-component recording and a divergence/curl computation, or
the polarisation analysis that is standard in seismic processing.

**(d)** It demonstrates that the plane-wave solutions satisfy the *full fourth-rank*
elastodynamic equation, i.e. that the derivation's algebra (including the
coefficients $\lambda+2\mu$ and $\mu$) is correct. It does **not** demonstrate that
the Earth is isotropic, homogeneous, linear or elastic — those are the assumptions
listed in §6, and each requires an independent observational test.

---

## ★★★9 — Mastery problem: the S-wave shadow and the core radius

**(a)** Slowness conservation: $\sin\theta_1/v_{p1} = \sin\theta_2/v_{p2}$ with
$v_{p1} = 6000$, $v_{p2} = 8000$ m s⁻¹ gives
$\theta_c = \sin^{-1}(6000/8000) = 48.5904^\circ$ for a P wave at the
crust–liquid interface.

**(b)** An incident S wave at the interface generates: reflected S (SV) in the
solid, converted reflected P in the solid, transmitted P in the liquid — and no
transmitted S, because $\mu = 0$ in the liquid. If mode conversion is allowed, the
number of waves is three, not four, and the four-wave problem of lesson 02-03-08
§3.5 loses one transmitted branch here.

**(c)** The transmitted P wave exists because the boundary conditions require
continuity of normal traction and of normal displacement, and a shear motion at the
interface produces a normal traction through the coupling of the two media (the
incident S wave has a traction component normal to the interface that the fluid
must match with a pressure). The liquid cannot support the *tangential* traction,
which is why no S wave is transmitted: the tangential-traction condition can only
be satisfied by the solid's own reflected waves.

**(d)** The absence of direct S arrivals beyond the S-wave shadow boundary
(depending on the Earth model and the source depth, beyond a distance of order
100°–105°) fixes the maximum angular distance an S ray can travel through the
mantle before it must enter the core. Converting that angle into a radius requires
(i) a velocity model for the mantle (the ray geometry) and (ii) the source depth
and the station distance. Combining S-shadow observations with P-wave travel-time
data that pass through and around the core, and with the free-oscillation spectrum,
yields the core radius; modern reference models give 3480 km. **Quote your source
for that number** (the standard reference is the PREM model of Dziewonski &
Anderson, 1981) and note that different models agree only to within a few
kilometres, with the residual differences reflecting trade-offs with the velocity
structure above and below the boundary.

---

## ★★★10 — Stress-induced anisotropy

**(a)** For a pre-stressed medium the linearised equation of motion contains an
effective stiffness
$B_{ijkl} = C_{ijkl} + \delta_{ij}\sigma_{kl} - \sigma_{jk}\delta_{il}$
(sign conventions differ between sources and must be checked), where
$\sigma_{kl}$ is the (static) pre-stress. The second term is the "geometric"
stiffness of a stressed solid; consult a continuum-mechanics text for the
derivation and state which convention you are quoting.

**(b)** Take an isotropic rock and apply a uniaxial pre-stress along $z$. The term
$\delta_{ij}\sigma_{kl}$ has a different structure for the $z$-direction than for
the $x$–$y$ plane, while the material $C_{ijkl}$ is unchanged; the sum therefore
has a symmetry axis along $z$ and is transversely isotropic (VTI) to first order in
$\sigma/C$. The symmetry axis is the stress direction.

**(c)** The size of the effect is of order $\sigma/C$ (with $C$ a relevant modulus).
For $\sigma = 10$ MPa and $\mu = 30$ GPa the ratio is $3.3\times10^{-4}$; the
resulting fractional change in $v_s$ is of order $10^{-4}$, i.e. 0.03 per cent.
Even for a deviatoric stress of 100 MPa the effect is of order 0.3 per cent —
which is why stress-induced anisotropy is usually small compared with
crack- or lattice-induced anisotropy at seismogenic depths, except in weak or
highly stressed rocks near failure. State the argument you use; this is an
order-of-magnitude estimate, not a calculation.

**(d)** Two discriminating observations: (i) **the stress dependence** — apply or
change a stress (in the laboratory, or observe the tidal modulation of the
splitting) and see whether the anisotropy changes with it, which is diagnostic of
stress-induced anisotropy; and (ii) **the correlation with tectonic strain** — for
intrinsic anisotropy from lattice-preferred orientation, the fast direction aligns
with the finite-strain or flow direction (mantle flow), whereas stress-induced
splitting aligns with the *current* stress field. Where the two directions
coincide, the observations cannot separate them and a third constraint (a
laboratory measurement of the rock's intrinsic anisotropy) is required.
