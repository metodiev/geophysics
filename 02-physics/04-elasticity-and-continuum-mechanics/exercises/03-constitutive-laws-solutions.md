# Solutions — 02-04-03 Constitutive Laws and Generalised Hooke's Law

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Voigt matrix and energy

**(a)** $C_{11} = \lambda+2\mu = 70$, $C_{12} = \lambda = 20$,
$C_{44} = \mu = 25$ GPa:

$$\mathbf{C}_V = \begin{pmatrix}
70&20&20&0&0&0\\ 20&70&20&0&0&0\\ 20&20&70&0&0&0\\
0&0&0&25&0&0\\ 0&0&0&0&25&0\\ 0&0&0&0&0&25\end{pmatrix}\ \text{GPa}.$$

**(b)** $K = \lambda+2\mu/3 = 20+16.666667 = 36.666667$ GPa;
$M = \lambda+2\mu = 70$ GPa.

**(c)** $W = \tfrac12C_{1111}\varepsilon_{11}^2 =
\tfrac12\times70\times10^9\times(10^{-3})^2 = 3.5\times10^4$ J m⁻³.
Checking through the closed form:
$\tfrac12\lambda(\operatorname{tr}\varepsilon)^2+\mu\varepsilon_{ij}\varepsilon_{ij}
= \tfrac12\times20\times10^9\times10^{-6}+25\times10^9\times10^{-6} =
10^4+2.5\times10^4 = 3.5\times10^4$ ✓.

**(d)** Pure shear: $W = \tfrac12\times2\times\sigma_{12}\varepsilon_{12}$; with
$\sigma_{12} = 2\mu\varepsilon_{12} = 2\times25\times10^9\times10^{-3} =
5\times10^7$ Pa, $W = 5\times10^7\times10^{-3} = 5\times10^4$ J m⁻³. The ratio to
(c) is $5/3.5 = 1.428571$: at equal strain magnitude, shear stores more energy per
unit than axial compression, because compression also involves the volumetric term
(and the volumetric stiffness here is $M = 70$ GPa while the shear stiffness for
the same strain measure is $2\mu = 50$ GPa, with the factor-of-two in the energy of
the shear pair of components entering as well).

---

## ★2 — Stress from strain

**(a)** $\operatorname{tr}\varepsilon = 0$ identically here, so the $\lambda$ term
vanishes and $\sigma_{ij} = 2\mu\varepsilon_{ij}$:
$\sigma_{11} = 2\times25\times2\times10^{-3} = 100$ MPa;
$\sigma_{22} = \sigma_{33} = -50$ MPa.

**(b)** Mean stress $= (100-50-50)/3 = 0$; the state is **purely deviatoric**, as
it must be since the strain was.

**(c)** The deviatoric strain equals the strain (trace zero), and
$\sigma_{ij} = 2\mu\varepsilon_{ij}$ with $2\mu = 50$ GPa ✓.

**(d)** Because the constitutive relation is
$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$: the
factor 2 is in the definition of the Lamé form, and any statement "the deviatoric
stress is $\mu$ times the deviatoric strain" is wrong by a factor of two. This is
the same convention issue as the engineering shear strain, and it is worth
checking every time a shear modulus appears in a formula.

---

## ★3 — Counting constants

**(a)** A general fourth-rank tensor has 81 components. Minor symmetry in the first
pair ($C_{ijkl} = C_{jikl}$) reduces $i,j$ to 6 combinations, so
$6\times9 = 54$; minor symmetry in the second pair reduces the last two indices
similarly, giving $6\times6 = 36$.

**(b)** Major symmetry $C_{ijkl} = C_{klij}$ says the resulting $6\times6$ matrix is
symmetric, so the independent entries are $6\times7/2 = 21$ ✓.

**(c)** The existence of a strain-energy function (equivalently, the
thermodynamic requirement that a closed elastic cycle do no net work) provides
major symmetry.

**(d)** Cubic: 3 (e.g. halite). Hexagonal/transversely isotropic: 5 (e.g. ice).
The reduction from 21 to 3 requires four independent symmetry operations; each
symmetry is a physical statement about the microstructure's averaging.

---

## ★4 — Voigt conventions

**(a)** The six-vector $(1,0,0,1,0,0)\times10^{-3}$ in engineering convention means
$\varepsilon_{11} = 10^{-3}$ and $2\varepsilon_{23} = 10^{-3}$, i.e.
$\varepsilon_{23} = \varepsilon_{32} = 5\times10^{-4}$.

**(b)** $\sigma_{11} = C_{11}\varepsilon_{11}+C_{12}(\varepsilon_{22}+
\varepsilon_{33}) = 70\times10^{-3} = 70$ MPa (for the ★1 material);
$\sigma_{23} = C_{44}\times(2\varepsilon_{23}) = 25\times10^{-3} = 25$ MPa.

**(c)** If the vector is read as the tensor convention (i.e. as
$\varepsilon_{23} = 10^{-3}$ without the factor of two), the resulting
$\sigma_{23}$ is 50 MPa — a factor of two too large.

**(d)** Run the two implementations (fourth-rank contraction versus the
$6\times6$ route) and compare; they agree only if the conventions match. The
demo's cross-check reports zero difference, which is exactly this test.

---

## ★5 — Reading the demo

**(a)** Both symmetry residuals are 0.000e+00 Pa.

**(b)** Strain energy 4.826000e+05 J m⁻³ from both routes, difference
0.000e+00 J m⁻³.

**(c)** $S_{1111} = 1.358025\times10^{-11}$ Pa⁻¹ against
$1/E = 1.358025\times10^{-11}$ Pa⁻¹.

**(d)** The round-trip error is $4.337\times10^{-19}$ — round-off. It certifies
that the stiffness and compliance implementations are a true inverse pair, which
is the strongest available check on a constitutive implementation.

---

## ★6 — A measured set of constants

**(a)** $\mu = \rho v_s^2 = 2350\times1900^2 = 8.4835\times10^9$ Pa =
8.4835 GPa. $M = \rho v_p^2 = 2350\times3200^2 = 2.4064\times10^{10}$ Pa =
24.064 GPa. Then $\lambda = M-2\mu = 24.064-16.967 = 7.097$ GPa, and
$K = \lambda+2\mu/3 = 7.097+5.656 = 12.753$ GPa.

**(b)** $K = 12.753$ GPa and $\lambda+2\mu/3 = 7.097+5.656 = 12.753$ ✓;
$M = K+4\mu/3 = 12.753+11.311 = 24.064$ ✓.

**(c)** $C_{11} = M = 24.064$, $C_{12} = \lambda = 7.097$, $C_{44} = \mu = 8.4835$
GPa, so $C_{11}-C_{12}-2C_{44} = 24.064-7.097-16.967 = 0.000$ GPa: the test passes
identically, which is not a measurement of isotropy at all.

**(d)** Because the constants were *derived* from $\lambda$ and $\mu$ through the
isotropic relations, the identity holds by construction. The identity is a test of
a *measured stiffness matrix* — for example one determined from velocities at
several propagation directions — not of a set of constants that were computed
assuming isotropy. This distinction is the point of the exercise.

---

## ★7 — Drained and undrained moduli

**(a)** The slow (drained) test determines the frame moduli $K_{\text{dry}}$ and
$\mu$; the fast (undrained) test determines $K_{\text{sat}}$ and the same $\mu$
(the shear modulus is unaffected by a pore fluid, whether drained or undrained, in
Gassmann's theory).

**(b)** $K_{\text{sat}} = K_{\text{dry}} + \frac{(1-K_{\text{dry}}/K_{\min})^2}
{\phi/K_f+(1-\phi)/K_{\min}-K_{\text{dry}}/K_{\min}^2}$ with
$K_{\min} = 36$, $K_f = 2.2$, $\phi = 0.15$:
$(1-12/36)^2 = 0.444444$;
$0.15/2.2+0.85/36-12/1296 = 0.068182+0.023611-0.009259 = 0.082534$;
$K_{\text{sat}} = 12+0.444444/0.082534 = 12+5.385 = 17.385$ GPa — 45 per cent
above the dry value.

**(c)** With $\mu = 9$ GPa:
$v_p^{\text{dry}} = \sqrt{(12+12)/2100} = \sqrt{1.142857\times10^7} =
3380.6$ m s⁻¹ (using $K+4\mu/3 = 12+12 = 24$ GPa);
$v_p^{\text{sat}} = \sqrt{(17.385+12)\times10^9/2250} = \sqrt{1.306\times10^7} =
3613.9$ m s⁻¹. So the saturated rock is 6.9 per cent faster, and
$v_s = \sqrt{9\times10^9/2100} = 2070$ m s⁻¹ dry against
$\sqrt{9\times10^9/2250} = 2000$ m s⁻¹ saturated — the shear speed *falls* with
saturation because the density rises while $\mu$ does not.

**(d)** Vary the loading frequency and look for dispersion between the low- and
high-frequency limits; or measure with the sample connected to a reservoir at
controlled pore pressure and compare with a sealed (undrained) configuration.

---

## ★8 — Averaging bounds

**(a)** Voigt: $\bar K = 0.5\times10+0.5\times40 = 25$ GPa.

**(b)** Reuss: $1/\bar K = 0.5/10+0.5/40 = 0.05+0.0125 = 0.0625$, so
$\bar K = 16$ GPa.

**(c)** The Hashin–Shtrikman bounds lie inside $[16, 25]$ GPa and depend on the
geometry only through which phase is the host; they are tighter because they use
the exact solution for a spherical inclusion in a host, whereas Voigt and Reuss
assume uniform strain and uniform stress respectively — both of which are
kinematically and statically inadmissible in general.

**(d)** The Voigt bound is attained by a composite loaded *parallel* to stiff
lamellae (constant strain in the stiff direction), and the Reuss bound by a
composite loaded *normal* to compliant layers (constant stress). For a layered
medium, those are exactly the two geometries of §3.6 of the lesson — which is why
the bounds are the correct answers in those two limiting cases rather than mere
inequalities.

---

## ★★★9 — Orthorhombic anisotropy

**(a)** Orthorhombic: 9 independent constants,
$C_{11},C_{22},C_{33},C_{44},C_{55},C_{66},C_{12},C_{13},C_{23}$, with all other
entries zero.

**(b)** A uniaxial stress along $x$ produces
$\varepsilon_{11} = S_{11}\sigma_{11}$, $\varepsilon_{22} = S_{12}\sigma_{11}$,
$\varepsilon_{33} = S_{13}\sigma_{11}$: normal strains along all three axes, but
no shear, because $S$ has no coupling between the normal stress on $x$ and the
shear strains in the symmetry planes. The general statement in the question —
"shear strains in the other two planes" — is actually wrong for an orthorhombic
material; the correct statement is that the normal strains are all three
non-zero and the couplings $S_{14}, S_{15}, S_{16}$ vanish. This is a good
reminder that symmetry reduces coupling but does not *create* it.

**(c)** $\varepsilon_{11} = S_{11}\sigma_{11}+S_{12}\sigma_{22}+S_{13}\sigma_{33}$,
with $S_{11} = (C_{22}C_{33}-C_{23}^2)/\det$ and analogous expressions; the
explicit inversion of a general $3\times3$ block is the standard route.

**(d)** Gassmann's relation is derived for an isotropic (or at least
hydrostatically loaded) frame; in an anisotropic rock the fluid pressure acts on
the pore space, whose compressibility is directional, so the fluid-substitution
result requires more than a single $K_{\text{dry}}$ — it requires the full
anisotropic dry stiffness tensor, the pore-geometry information that connects it
to the mineral and fluid moduli, and in general a poroelastic formulation with
anisotropic coefficients.

---

## ★★★10 — Adiabatic versus isothermal moduli

**(a)** $K_S-K_T = K_T^2\alpha^2TV/C_V$. Taking
$C_V \approx C_p$ (the difference is a few per cent for water),
$V = 1/\rho = 1.003\times10^{-3}$ m³ kg⁻¹:
$K_T^2\alpha^2TV/C_V =
(2.2\times10^9)^2\times(2.1\times10^{-4})^2\times298\times1.003\times10^{-3}/4182
= 4.84\times10^{18}\times4.41\times10^{-8}\times2.989\times10^{-1}/4182$.
Numerator: $4.84\times10^{18}\times4.41\times10^{-8} = 2.134\times10^{11}$;
times $0.2989$ = $6.378\times10^{10}$; divided by 4182 =
$1.525\times10^7$ Pa = 15.25 MPa. So $K_S \approx K_T + 0.015$ GPa, a 0.7 per cent
difference.

**(b)** From $K_T = 2.2$ GPa and $\rho = 997$:
$c_T = \sqrt{K_T/\rho} = \sqrt{2.2\times10^9/997} = 1485.6$ m s⁻¹;
with $K_S = 2.215$ GPa, $c_S = \sqrt{2.215\times10^9/997} = 1490.6$ m s⁻¹.
The observed ultrasonic speed at 25 °C is near 1497 m s⁻¹, so the measured
value exceeds both; the residual is a real effect (the temperature coefficients
of $\rho$ and $K$, and the exact temperature of the measurement), and the honest
conclusion is that the adiabatic/isothermal difference explains *part* of the
gap, not all of it. Verify the source of the 1497 m s⁻¹ figure you use and state
the temperature.

**(c)** Fractional difference between the adiabatic and isothermal predictions:
$1490.6/1485.6-1 = 0.34$ per cent in velocity, which is of the same order as the
0.7 per cent difference in $K$ (the velocity goes as the square root, hence half
the fractional change). Report your own numbers with the temperature stated.

**(d)** For rocks the thermoelastic coupling term is far smaller (small thermal
expansion and large moduli), so the difference is negligible; for fluids it is
comparable with other effects. The consequence for saturated rocks is that
ultrasonic (adiabatic, undrained) measurements and static (isothermal, often
drained) measurements differ for two independent reasons, and the two corrections
must be applied separately — this is a standard part of laboratory-to-field
velocity upscaling.
