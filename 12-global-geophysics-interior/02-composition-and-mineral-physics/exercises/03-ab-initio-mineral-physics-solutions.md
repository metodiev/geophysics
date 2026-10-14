# Solutions — 12-02-03 Ab Initio Mineral Physics and Elastic Constants

Worked solutions for
[03-ab-initio-mineral-physics-exercises.md](./03-ab-initio-mineral-physics-exercises.md).
The lesson is
[03 Ab Initio Mineral Physics and Elastic Constants](../03-ab-initio-mineral-physics.md).
All tensors are **SYNTHETIC** teaching values; every number below was produced by the
verification script shipped with this module (`code/ab_initio_mineral_physics_demo.py`
and the arithmetic shown here).

Conventions used throughout: Voigt moduli from the 6×6 matrix $C$,

$$K_V = \frac{C_{11}+C_{22}+C_{33}+2(C_{12}+C_{13}+C_{23})}{9},\qquad
G_V = \frac{C_{11}+C_{22}+C_{33}-(C_{12}+C_{13}+C_{23})+3(C_{44}+C_{55}+C_{66})}{15},$$

Reuss moduli from $S = C^{-1}$,

$$K_R = \Big[(S_{11}+S_{22}+S_{33}) + 2(S_{12}+S_{13}+S_{23})\Big]^{-1},$$
$$G_R = 15\Big[4(S_{11}+S_{22}+S_{33}) - 4(S_{12}+S_{13}+S_{23})
+ 3(S_{44}+S_{55}+S_{66})\Big]^{-1},$$

and Hill values as the arithmetic mean. Christoffel: $M_{ik} = C_{ijkl}n_jn_l$ with
eigenvalues $\rho v^2$. Splitting time: $\delta t = L(1/v_\text{slow}-1/v_\text{fast})$.

---

## ★ Foundational

### ★1 — $K_V$, $G_V$ and $A$ for a cubic tensor

With $C_{11} = 280$, $C_{12} = 110$, $C_{44} = 130$ GPa:

$$K_V = \frac{3C_{11}+6C_{12}}{9} = \frac{3(280)+6(110)}{9}
= \frac{840+660}{9} = \frac{1500}{9} = 166.67\ \mathrm{GPa}.$$

$$G_V = \frac{3C_{11}-3C_{12}+9C_{44}}{15}
= \frac{840-330+1170}{15} = \frac{1680}{15} = 112.00\ \mathrm{GPa}.$$

$$A = \frac{2C_{44}}{C_{11}-C_{12}} = \frac{260}{170} = 1.5294.$$

$A$ is 53 % larger than the isotropic value $A = 1$, so this crystal is **strongly**
elastically anisotropic: shear behaviour depends on direction by roughly the same
amount. Note also $K_R = 166.67$ GPa, identical to $K_V$ — for cubic symmetry the bulk
modulus is the same in both averaging schemes (this is an identity, not a coincidence).

### ★2 — A hexagonal tensor

For hexagonal symmetry only five constants survive, and
$C_{66} = (C_{11}-C_{12})/2$ by construction:

$$C_{66} = \frac{300-120}{2} = 90.0\ \mathrm{GPa}.$$

$$K_V = \frac{2C_{11}+2C_{12}+4C_{13}+C_{33}}{9}
= \frac{600+240+400+320}{9} = \frac{1560}{9} = 173.33\ \mathrm{GPa}.$$

For this particular tensor $C_{11}+C_{12} = 420 = C_{33}+C_{13}$, so $K_R = 173.33$ GPa
as well (see ★★★9 — this is **not** a general hexagonal identity).

### ★3 — Splitting time and anisotropy

Two shear modes with $v_1 = 4.75$, $v_2 = 4.70$ km s$^{-1}$ over $L = 300$ km:

$$\delta t = L\left(\frac{1}{v_2}-\frac{1}{v_1}\right)
= 300\left(\frac{1}{4.70}-\frac{1}{4.75}\right)
= 300\left(0.212766-0.210526\right)$$

$$= 300 \times 2.2396\times10^{-3} = 0.6719\ \mathrm{s}.$$

The anisotropy is a *relative* quantity, so state which measure:

$$100\frac{v_1-v_2}{\bar v} = 100\frac{0.05}{4.725} = 1.06\,\%,$$

or, as an extremal measure, $100\times(4.75-4.70)/4.75 = 1.05\,\%$. Both round to
about 1 %, which is typical of upper-mantle shear anisotropy, but the definitions differ
and must be stated. Note the size intuition: **0.7 s of splitting over 300 km** is the
kind of delay that a careful shear-wave-splitting measurement resolves routinely.

## ★★ Applied

### ★★4 — Christoffel along $[110]$ for the ★1 tensor

Take $\mathbf n = (1,1,0)/\sqrt2$ and $\rho = 4.10\ \mathrm{g\,cm^{-3}}$. Using the
cubic contraction rules,

$$M_{11} = C_{11}n_1^2 + C_{44}(n_2^2+n_3^2) = \frac{C_{11}+C_{44}}{2}
= \frac{280+130}{2} = 205,$$
$$M_{22} = C_{44}n_1^2 + C_{11}n_2^2 + C_{44}n_3^2 = 205,\qquad
M_{33} = C_{44}(n_1^2+n_2^2) = 130,$$
$$M_{12} = (C_{12}+C_{44})n_1n_2 = \frac{110+130}{2} = 120,\qquad
M_{13} = M_{23} = 0.$$

So

$$M = \begin{pmatrix} 205 & 120 & 0\\ 120 & 205 & 0\\ 0 & 0 & 130\end{pmatrix}
\ \mathrm{GPa},$$

block-diagonal. The eigenvalues are $\{130,\ 205+120=325,\ 205-120=85\}$ GPa, verified
numerically as $[85, 130, 325]$. Hence

$$v = \sqrt{\frac{\lambda}{\rho}}:\quad
v_p = \sqrt{\frac{325}{4.10}} = 8.9033\ \mathrm{km\,s^{-1}},\quad
v_{s,\text{fast}} = \sqrt{\frac{130}{4.10}} = 5.6309\ \mathrm{km\,s^{-1}},$$
$$v_{s,\text{slow}} = \sqrt{\frac{85}{4.10}} = 4.5532\ \mathrm{km\,s^{-1}}.$$

**Splitting:** $5.6309 - 4.5532 = 1.0777$ km s$^{-1}$.

Along $[100]$ the same tensor gives $v_p = 8.2639$ km s$^{-1}$ and a **degenerate**
shear pair $5.6309/5.6309$ km s$^{-1}$: zero splitting. The difference is pure symmetry.
A four-fold axis along $[100]$ maps the two shear polarisations into each other, so
they must have equal speed; along $[110]$ only a two-fold axis remains, and the two
shear polarisations sample different combinations of the same constants — that is why
the maximum shear splitting of a cubic crystal lies along $\langle110\rangle$ and
vanishes along $\langle100\rangle$ and $\langle111\rangle$.

### ★★5 — $G_V$ versus $G_R$

For the ★1 tensor we already have $G_V = 112.00$ GPa. Inverting the matrix,

$$S = C^{-1} \Rightarrow S_{11} = 0.0045882,\quad S_{12} = -0.0012941,\quad
S_{44} = 0.0076923\ \mathrm{GPa^{-1}},$$

$$G_R = \frac{15}{4(3S_{11}) - 4(3S_{12}) + 3(3S_{44})}
= \frac{15}{0.0550588+0.0155294+0.0692308} = \frac{15}{0.1398190} = 107.2816\
\mathrm{GPa}.$$

Fractional difference relative to Voigt:

$$\frac{G_R-G_V}{G_V} = \frac{107.2816-112.00}{112.00} = -4.21\,\%.$$

The Hill average is $G_\text{Hill} = (112.00+107.2816)/2 = 109.641$ GPa. **Use Hill**
for an isotropic-equivalent velocity: $G_V$ is an upper bound (uniform-strain
assumption) and $G_R$ a lower bound (uniform-stress assumption), and no polycrystal can
violate either. Hill is not a physical bound but is the standard, central estimate, and
it is what the lesson's demo reports. The spread of 4.2 % between the bounds is also a
useful diagnostic: it is the same order as the full single-crystal shear anisotropy, so
quoting an "isotropic-equivalent" $v_s$ without saying which average is a hidden
systematic.

### ★★6 — A violated Born criterion

With $C_{44} = 130$ GPa and $C_{11}-C_{12} = -5$ GPa, the violated criterion is
$C_{11}-C_{12} > 0$ (equivalently $C_{66} > 0$). The strain-energy matrix
$W = \tfrac12\epsilon_IC_{IJ}\epsilon_J$ is then **not positive definite**: there is a
shear strain of the form $(\epsilon_1,\epsilon_2)$ with $\epsilon_2 = -\epsilon_1$ that
*reduces* the energy. A material in that state would spontaneously shear without limit —
there is no elastic equilibrium, and the "crystal" is unphysical.

Two things follow, and both are habits worth keeping. First, the tensor still fits a
distorted structure perfectly well and still returns wave speeds from the Christoffel
equation; the failure surfaces only as a **negative eigenvalue** of $M$, whose square
root is imaginary (the demo prints `imaginary: unstable` as $C_{44}$ is driven through
zero). Second, the physical conclusion is *not* "the crystal is exotic" but "the
calculation is wrong" — a bad pseudopotential, an unconverged cutoff, or a
miscounted strain (a factor-of-two in strain amplitude is the classic error). Born
stability is the first and cheapest check on any computed tensor.

### ★★7 — Alignment from an observed anisotropy

$$\text{alignment fraction} = \frac{A_\text{observed}}{A_\text{single crystal}}
= \frac{1.2\,\%}{6\,\%} = 0.20 = 20\,\%.$$

Assumptions: (i) the aggregate anisotropy is linear in the alignment fraction, i.e. it
scales as $A_\text{obs} = fA_\text{crystal}$; (ii) one crystal phase dominates;
(iii) the measured fast direction coincides with the crystal's fast axis, so no
orientation average reduces the signal; (iv) $A$ is defined the same way on both sides
(extremal here). Each assumption can fail by a factor of two, so "20 % alignment"
should be read as "of order 20 %, if the fabric is single-phase and simple".

## ★★★ Research-oriented

### ★★★8 — A computation-to-seismology workflow

1. **Structural convergence.** Relax the cell and all internal coordinates at fixed
   pressure; check that forces are below the convergence threshold and that the result
   is reproducible against a tighter cutoff. *Catches:* unconverged geometry, which
   contaminates every elastic constant.
2. **Energy–volume equation of state.** Fit $E(V)$ to a Birch–Murnaghan form and read
   $K_0$, $K_0'$, $V_0$. Cross-check against the experimental diamond-anvil $P$–$V$ curve
   if one exists. *Catches:* wrong volume, wrong bulk modulus — an error no elasticity
   calculation can repair. **This step uses no seismological data.**
3. **Born stability.** Evaluate $C_{11}-C_{12} > 0$, $C_{11}+2C_{12} > 0$, $C_{44} > 0$
   (cubic) or the full positive-definiteness test in the crystal's own symmetry.
   *Catches:* unphysical tensors and, indirectly, bad pseudopotentials or distorted
   cells.
4. **Symmetry audit.** Count independent constants against the assumed space group;
   confirm that the tensor is invariant under the generator operations. *Catches:* a
   structure that has quietly relaxed into a lower-symmetry phase.
5. **Elastic-constant consistency.** Compare with a finite-difference *stress* route and
   with a second derivative of the energy; verify that $K_V = K_R$ where the symmetry
   demands it (cubic). *Catches:* numerical noise, basis-set artefacts, and the classic
   factor-of-two strain error.
6. **Extrapolation to mantle pressure and temperature.** Apply a thermal equation of
   state, and add the temperature dependence of the constants (which can be large and is
   the weakest link). *Catches:* using a 0 K tensor at 2500 K.
7. **Aggregate averaging.** Convert the single-crystal tensor to an isotropic-equivalent
   medium via a stated averaging scheme (Voigt/Reuss/Hill, or self-consistent for a
   strongly anisotropic aggregate). *Catches:* silently using one bound as if it were
   the truth.
8. **Texture model.** Multiply the single-crystal anisotropy by an alignment fraction
   from a deformation/fabric model (or treat $f$ as a free parameter and report the
   required $f$). *Catches:* claiming a mantle anisotropy that needs 150 % alignment.
9. **Forward modelling of observables.** Predict the actual measured quantity —
   splitting time along a specific ray, or $d\ln v_s/d\ln v_p$ — not merely an
   anisotropy percentage. *Catches:* the mismatch between "6 % crystal anisotropy" and
   "the seismometer records 0.8 s of splitting".
10. **Compare and invert.** Only now compare with data, and invert for the *combinations*
    that the data constrain. *Catches:* over-interpretation, since several
    (phase, fraction, orientation, temperature) combinations fit the same observation.

Steps 2, 3 and 5 are internal checks: they involve no seismic data at all, which is what
makes the workflow diagnostic rather than circular.

### ★★★9 — When does $K_V = K_R$ for a hexagonal crystal?

Write $P = C_{11}+C_{12}$, $Q = C_{13}$, $R = C_{33}$. Then

$$K_V = \frac{2P+4Q+R}{9}.$$

For the Reuss side, the compliances of a hexagonal crystal reduce to
$2S_{11}+S_{33}+2S_{12}+4S_{13} = (2R+P-4Q)/\Omega$ with
$\Omega = PR-2Q^2$, so

$$K_R = \frac{\Omega}{2R+P-4Q} = \frac{PR-2Q^2}{P+2R-4Q}.$$

Putting both over the common denominator $9(P+2R-4Q)$:

$$K_V-K_R = \frac{(2P+4Q+R)(P+2R-4Q) - 9(PR-2Q^2)}{9(P+2R-4Q)}.$$

Expand the numerator:

$$(2P+4Q+R)(P+2R-4Q) = 2P^2+5PR+4QR-4PQ-16Q^2+2R^2,$$
$$-9(PR-2Q^2) = -9PR+18Q^2,$$
$$\text{sum} = 2P^2-4PQ-4PR+4QR+2R^2+2Q^2 = 2\Big[(P-R)^2+Q^2-2Q(P-R)\Big]
= 2\big[(P-R)-Q\big]^2.$$

Therefore

$$\boxed{\,K_V-K_R = \frac{2\left(C_{11}+C_{12}-C_{33}-C_{13}\right)^2}
{9\left(C_{11}+C_{12}+2C_{33}-4C_{13}\right)}\,}$$

and $K_V = K_R$ **if and only if** $C_{11}+C_{12} = C_{33}+C_{13}$.

Check against two tensors:

| tensor | $P-R-Q$ | $K_V$ | $K_R$ | $K_V-K_R$ | formula |
|---|---|---|---|---|---|
| ★2: 300/120/100/320/90 | 0.0 | 173.3333 | 173.3333 | 0.0000 | 0.0000 |
| 290/230/110/280/95 | 130.0 | 195.5556 | 189.6875 | 5.8681 | 5.8681 |

The ★2 tensor hits the equality by accident (it was generated with
$C_{11}+C_{12} = C_{33}+C_{13} = 420$), which is exactly the trap: the lesson's demo
tensor also happens to satisfy this, so a "check" of $K_V = K_R$ there proves nothing
about the general case. The residual $5.87$ GPa in the second line is about 3 % of $K$
— small but not zero, and far larger than the rounding one might blame.

Why no analogous equality for the shear modulus: the denominators in the Reuss formula
involve $S_{44}, S_{55}, S_{66}$ as well as $S_{11}+S_{22}+S_{33}$ and
$S_{12}+S_{13}+S_{23}$, so the difference $G_V-G_R$ cannot be written as a perfect
square in a few constants; it vanishes identically only for an elastically isotropic
crystal (two independent constants, with $C_{44} = (C_{11}-C_{12})/2$), which is why
$G_V \ne G_R$ is the rule, not the exception, in every lower symmetry.

### ★★★10 — Alignment of a strongly anisotropic inner core

Take $v_s = 3.5$ km s$^{-1}$ with a single-crystal S anisotropy of 20 %, i.e. ±10 %:
$v_\text{fast} = 3.85$, $v_\text{slow} = 3.15$ km s$^{-1}$. Over $L = 2500$ km, with the
fast axis fully aligned with the ray plane,

$$\delta t_\text{aligned} = 2500\left(\frac{1}{3.15}-\frac{1}{3.85}\right)
= 2500\left(0.317460-0.259740\right) = 2500 \times 0.057720 = 144.30\ \mathrm{s}.$$

An observed splitting of 2 s then requires an **effective alignment**

$$f = \frac{\delta t_\text{observed}}{\delta t_\text{aligned}}
= \frac{2}{144.30} = 0.0139 \approx 1.4\,\%.$$

Two readings are possible and the arithmetic alone cannot choose between them:

* either the single-crystal anisotropy is far smaller than 20 % (a weakly anisotropic
  phase strongly aligned), or
* the crystal is indeed strongly anisotropic but almost randomly oriented, so the
  directional signal is largely averaged out.

**What would break the degeneracy?** Several observables constrain different
combinations: (i) the *shape* of the anisotropy pattern over many ray directions, since
a textured aggregate has a smooth angular dependence with a specific symmetry while a
different phase has a different symmetry; (ii) the ratio of P to S anisotropy,
$A_P/A_S$, which is a fixed fingerprint of the crystal but not of the alignment
fraction; (iii) the pressure and temperature dependence of the anisotropy, compared with
a computed elastic tensor; (iv) the *sign and direction* of travel-time anomalies
relative to the rotation axis, which links the fabric to an independent physical
process. Combining (i) and (ii) is the practical route: alignment scales both $A_P$ and
$A_S$ together, whereas a change of candidate phase changes their ratio.

---

## Mastery checkpoint — worked solution

> A cubic crystal has $C_{11} = 250$, $C_{12} = 120$, $C_{44} = 100$ GPa and
> $\rho = 4.00\ \mathrm{g\,cm^{-3}}$.

### (a) Born stability

$$C_{11}-C_{12} = 130\ \mathrm{GPa} > 0,\qquad
C_{11}+2C_{12} = 490\ \mathrm{GPa} > 0,\qquad
C_{44} = 100\ \mathrm{GPa} > 0.$$

All three are positive, so the strain-energy matrix is positive definite and the
crystal is **elastically stable**. (Equivalently: $C_{44} > 0$ and
$|C_{12}| < C_{11}$.)

### (b) $K$, $A$, and the Hill shear modulus

$$K = \frac{C_{11}+2C_{12}}{3} = \frac{250+240}{3} = \frac{490}{3}
= 163.33\ \mathrm{GPa}\quad(\text{and } K_R \text{ is identical: } 163.33\ \mathrm{GPa}).$$

$$A = \frac{2C_{44}}{C_{11}-C_{12}} = \frac{200}{130} = 1.5385.$$

$$G_V = \frac{3C_{11}-3C_{12}+9C_{44}}{15} = \frac{750-360+900}{15}
= \frac{1290}{15} = 86.00\ \mathrm{GPa},$$

$$G_R = \frac{15}{4\cdot3S_{11}-4\cdot3S_{12}+3\cdot3S_{44}}
= 82.2785\ \mathrm{GPa},$$

$$G_\text{Hill} = \frac{86.00+82.2785}{2} = 84.139\ \mathrm{GPa}.$$

The Hill pair also gives the isotropic-equivalent velocities:
$v_p = 8.299$, $v_s = 4.586$ km s$^{-1}$ (from
$v_p = \sqrt{(K+4G/3)/\rho}$, $v_s = \sqrt{G/\rho}$ with the Hill moduli).

### (c) $v_p$ and $v_s$ along $[100]$

Along $[100]$, $\mathbf n = (1,0,0)$, so $M = \mathrm{diag}(C_{11}, C_{44}, C_{44})$
GPa. The eigenvalues are $250$, $100$, $100$ GPa:

$$v_p = \sqrt{\frac{250}{4.00}} = \sqrt{62.5} = 7.9057\ \mathrm{km\,s^{-1}},$$
$$v_s = \sqrt{\frac{100}{4.00}} = \sqrt{25} = 5.0000\ \mathrm{km\,s^{-1}}\
(\text{twice — degenerate by the four-fold axis}).$$

### (d) Splitting along $[110]$, and the implied alignment

Along $[110]$, $M_{11} = M_{22} = (C_{11}+C_{44})/2 = 175$ GPa,
$M_{12} = (C_{12}+C_{44})/2 = 110$ GPa and $M_{33} = C_{44} = 100$ GPa, so the
eigenvalues are $100$ GPa (the $\hat{\mathbf z}$ shear) and $175\pm110$ GPa. The three
speeds are therefore

$$v_p = \sqrt{\frac{175+110}{4.00}} = \sqrt{\frac{285}{4}} = 8.4410\
\mathrm{km\,s^{-1}},$$
$$v_{s,\text{fast}} = \sqrt{\frac{100}{4.00}} = 5.0000\ \mathrm{km\,s^{-1}},\qquad
v_{s,\text{slow}} = \sqrt{\frac{175-110}{4.00}} = \sqrt{\frac{65}{4}} = 4.0311\
\mathrm{km\,s^{-1}}.$$

So the three speeds along $[110]$ are $(8.4410,\ 5.0000,\ 4.0311)$ km s$^{-1}$ and the
shear splitting per 100 km is

$$\delta t = 100\left(\frac{1}{4.0311}-\frac{1}{5.0000}\right)
= 100\left(0.248072-0.200000\right) = 4.8069\ \mathrm{s}.$$

Over a 400 km path with full alignment this becomes
$4.8069 \times 4 = 19.228$ s. An observed splitting of 2 s therefore implies

$$f = \frac{2}{19.228} = 0.1040 \approx 10.4\,\%$$

**effective alignment**, with the same caveats as ★★7: a single phase, a simple fabric,
and a measured fast direction close to the crystal fast axis. Note the order of
magnitude — a 1.54 anisotropy factor and a 4.8 s/100 km splitting powers a *much*
stronger prediction than the 10 % alignment the data seem to allow, which is the
standard tension in mantle-anisotropy interpretations.

---

## Marking and sanity guide

* Any answer that quotes a velocity without $\sqrt{\lambda/\rho}$ (or that mixes GPa with
  km s$^{-1}$ without the $10^{9}$/$\rho$ conversion) loses the point regardless of the
  final number. Check units at every interface: $[\mathrm{GPa}] =
  10^{9}\ \mathrm{kg\,m^{-1}s^{-2}}$, $\rho$ in kg m$^{-3}$, $v$ in m s$^{-1}$, and
  1 km s$^{-1} = 10^{3}$ m s$^{-1}$.
* Born checks must be written as inequalities, not as "it looks fine".
* The three Christoffel solutions must be labelled (quasi-P, quasi-S), not "P and two
  S", away from symmetry directions.
* Any anisotropy percentage must state its definition (extremal vs mean vs axial); the
  same crystal can give 7.46 % and 3.45 % by two equally defensible conventions.
* Alignment answers must be reported as an inferred fraction with its assumptions, never
  as a measurement.
