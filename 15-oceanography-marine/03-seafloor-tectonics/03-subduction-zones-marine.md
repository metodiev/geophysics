---
id: 15-03-03
title: "Marine Subduction Zones, Trenches and Accretionary Prisms"
level: research
prereqs: ["15-03-02", "15-02-01", "15-02-04", "13-01-03"]
tags: [oceanography, marine-geophysics, seafloor-tectonics, subduction-zones, accretionary-prism, flexure]
---

# Marine Subduction Zones, Trenches and Accretionary Prisms

> **All models and data in this module are SYNTHETIC.** The wedge, the bent plate
> and the prism are teaching models with the model constants stated below. No real
> trench, prism, subduction zone or cruise is used, and no number is quoted from a
> published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the critical-taper relation for a cohesionless Coulomb wedge from a
   horizontal force balance, and **verify** it by numerically integrating the same
   balance to the finite angles of a real wedge.
2. **Compute** how the wedge surface slope changes with basal pore pressure, and
   **state** why a décollement's fluid pressure is a first-order control on prism
   geometry.
3. **Derive** the flexural parameter $\alpha=(4D/\Delta\rho g)^{1/4}$ and the
   deflection of an elastic plate under a line load, and **check** the solution
   against an independent Fourier solution of the beam equation.
4. **Convert** a plate deflection into a bending moment and a fibre stress, and
   **compute** the effective elastic thickness implied by a stated yield strength.
5. **Budget** an accretionary prism: sediment flux in, accreted volume, prism
   width at a given taper, and the pore water expelled by compaction.
6. **State** the assumptions under which a taper angle may be inverted for basal
   friction, and **name** the observation that tests the inversion.
7. **Distinguish** accretion from subduction erosion in the same budget, and
   **explain** what each does to forearc topography and to the seismic record.

## Prerequisites

- [15-03-02 Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) —
  what is being subducted.
- [15-02-01 Marine Seismic Reflection](../02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  how the prism's internal structure and the décollement are imaged.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  the shallowest part of the incoming sediment section.
- [13-01-03 Lithospheric Strength](../../13-geodynamics-tectonics/01-geodynamic-principles/03-lithospheric-strength.md) —
  the yield envelopes used to interpret the bending stress.

## 1. Intuition: a wedge is a machine for turning friction into geometry

An accretionary prism is a pile of sediment scraped off a downgoing plate and
thickened by shortening. Its most striking property is that its **shape** is not
arbitrary: for a given set of material properties, the prism sits at a specific
surface slope and basal dip — the **critical taper** — and it returns to that
shape whenever it is perturbed. Excavate it, and it grows back; thicken it, and
it spreads. That is why a wedge's slope is a measurable proxy for its strength and
its fluid pressure.

The second machine in the picture is the incoming plate. Just before it goes down,
it is bent over the trench. The bending is elastic at first, but the fibre
stresses reach the same order as the brittle strength of rock, so the plate yields
and behaves as if it were thinner than its thermal thickness. Two numbers come out
of that: the deflection, which sets the depth of the trench, and the outer-rise
bulge, which is a real bathymetric feature tens of metres high and hundreds of
kilometres wide.

**The honest difficulty of this lesson is that both machines are being inverted
for quantities nobody measures directly.** Basal friction, pore pressure at the
décollement, effective elastic thickness and the accreted-versus-subducted
partition are all model quantities. The taper relation is a *relation between
unknowns*; a prism slope of $9^\circ$ does not give you a basal friction unless
you already know the pore pressure and the internal strength. Every inversion in
this lesson has to be presented as a curve of possible worlds, and the exercises
ask you to say which measurement closes it.

## 2. Precise definitions

**Décollement**: the basal detachment of the wedge, a weak, often
overpressured surface within the incoming sediment section.

**Taper** $\theta=\alpha+\beta$: the sum of the surface slope $\alpha$ and the
basal dip $\beta$ — the wedge's opening angle in the small-angle approximation.

**Pore-pressure ratio** $\lambda=p/\sigma_z$: fluid pressure divided by the total
vertical (lithostatic) stress, with $0\le\lambda<1$. $\lambda=1$ is
lithostatic fluid pressure; there is no upper bound in principle but the effective
stress cannot be negative for a frictional material that transmits shear.
$\lambda_b$ refers to the décollement.

**Stress ratio** $K=\sigma_x'/\sigma_z'$: the horizontal-to-vertical effective
stress ratio. At Coulomb failure with an internal friction angle $\phi$,
$K=(1+\sin\phi)/(1-\sin\phi)$ for the compressional state used here. **This is a
model choice**: the exact slip-line solutions of the wedge problem have
$K$ varying within the wedge, and using one constant $K$ is the central
simplification of this derivation.

**Effective elastic thickness** $T_e$: the thickness of an elastic plate that
would have the same rigidity as the real, partly yielding plate. It is a
*mechanical* quantity and is not the thermal or seismic lithospheric thickness.

**Flexural parameter** $\alpha_f=(4D/\Delta\rho g)^{1/4}$: the length scale over
which a plate on a fluid foundation responds to a load. (The symbol $\alpha$ is
overloaded in this subject; here $\alpha$ alone is the surface slope and
$\alpha_f$ the flexural length, and the demonstration prints both.)

**Subduction erosion**: the removal of forearc material by the subducting plate,
the opposite sign of accretion. Both appear in the same budget, with the
accreted fraction $f_a$ allowed to be negative.

## 3. Derivations

### 3.1 The critical taper from a force balance

Take a wedge of uniform density $\rho$, apex at the trench ($x=0$, $x$ positive
landward), vertical thickness $H(x)=x(\tan\alpha+\tan\beta)$, surface slope
$\alpha$ and basal dip $\beta$. The wedge is everywhere at Coulomb failure, the
décollement has friction $\mu_b$ and pore-pressure ratio $\lambda_b$, and the
internal pore-pressure ratio is $\lambda$. Define the cross-sectional area factor

$$S=\int_0^L H(x)\,\mathrm{d}x=\frac{L^2(\tan\alpha+\tan\beta)}{2} .$$

Four forces act per unit length of trench:

1. **Tectonic push at the back**, from the horizontal stress
   $\sigma_x'=K\sigma_z'=K(1-\lambda)\rho g\,(\text{depth below surface})$:
   $P_b=K(1-\lambda)\rho g\,H(L)^2/2=K(1-\lambda)\rho g(\tan\alpha+\tan\beta)S$.
2. **Basal shear**, $\tau_b=\mu_b\sigma_z'({\rm base})
   =\mu_b(1-\lambda_b)\rho g H(x)$, integrated along the base whose length is
   $L/\cos\beta$: $\;\mu_b(1-\lambda_b)\rho g\,S/\cos\beta$.
3. **Horizontal component of the base-normal traction.** The base carries both
   effective normal stress and pore pressure; vertical equilibrium of the wedge
   requires their total to support the weight $W=\rho g S$,
   $\int(\sigma_n'+p_b)\cos\beta\,\mathrm{d}s=W$, so the horizontal component is
   $\int(\sigma_n'+p_b)\sin\beta\,\mathrm{d}s=W\tan\beta$.
4. **Frontal resistance**, which is zero for a wedge whose toe abuts undeforming
   material (the standard assumption).

Setting push equal to the resistances and dividing by $\rho g S$:

$$K(1-\lambda)(\tan\alpha+\tan\beta)
=\frac{\mu_b(1-\lambda_b)}{\cos\beta}+\tan\beta .$$

Neglecting the differences between $\tan$ and its argument and setting
$\cos\beta\approx1$ gives the **critical-taper relation** used throughout the
literature:

$$\boxed{\;\alpha+\beta=\theta=\frac{\mu_b(1-\lambda_b)+\beta}{K(1-\lambda)}
\;}$$

For $\phi=30^\circ$ ($K=3.000$), $\mu_b=0.55$, $\lambda=\lambda_b=0.40$ and
$\beta=3^\circ$:

$$\theta=\frac{0.55(0.60)+0.05236}{3.000(0.60)}
=\frac{0.38236}{1.800}=0.21242\ \mathrm{rad}=12.17^\circ,\qquad
\alpha=9.17^\circ .$$

**Verification.** The demonstration integrates the finite-angle balance
numerically at that $\alpha$ and finds a residual of $+0.54\%$ of the push, with
the terms $1.0902\times10^{13}$, $9.3589\times10^{12}$ and
$1.4843\times10^{12}\ \mathrm{N\,m^{-1}}$ for push, basal shear and the
base-normal horizontal component. That residual is the small-angle error of the
closed form, not an algebra error: substituting $\alpha=12.17^\circ$ — i.e.
forgetting to subtract $\beta$ — leaves a residual of $+20.7\%$ of the push, so
the balance is a sharp test of the derivation.

### 3.2 Pore pressure is the control

$\theta=\mu_b/K+\beta/[K(1-\lambda)]$, so

$$\frac{\mathrm{d}\alpha}{\mathrm{d}\lambda}
=\frac{\beta}{K(1-\lambda)^2},$$

which is **not** small when $\lambda\to1$. The demonstration's table:

| $\lambda$ | $\alpha$ (deg) | $\theta$ (deg) | $\mathrm{d}\alpha/\mathrm{d}\lambda$ (deg) |
|---|---|---|---|
| 0.00 | 8.50 | 11.50 | — |
| 0.20 | 8.75 | 11.75 | +1.25 |
| 0.40 | 9.17 | 12.17 | +2.08 |
| 0.60 | 10.00 | 13.00 | +4.17 |
| 0.80 | 12.50 | 15.50 | +12.50 |
| 0.90 | 17.50 | 20.50 | +50.00 |

The sensitivity more than doubles between $\lambda=0.4$ and $\lambda=0.6$ and
grows without bound as $\lambda\to1$. **A prism's slope is therefore much more
sensitive to the décollement's fluid pressure than to its friction**, and this is
why an overpressured décollement — for instance one sealed beneath a gas-hydrate
stability zone — is the standard explanation for a shallowly tapering prism. The
same table is the warning: two wedges with $\alpha=9^\circ$ may differ by
$\mu_b(1-\lambda_b)$ from 0.2 to 0.5, and the slope alone cannot say which.

### 3.3 Flexure of the incoming plate

An elastic plate of rigidity
$D=\dfrac{ET_e^3}{12(1-\nu^2)}$ floating on a foundation of density contrast
$\Delta\rho$ satisfies, for a line load $P$ at $x=0$,

$$D\frac{\mathrm{d}^4w}{\mathrm{d}x^4}+\Delta\rho\,g\,w=P\,\delta(x).$$

With $\lambda_f=(k/4D)^{1/4}$, $k=\Delta\rho g$, the bounded solution for $x\ge0$
is

$$w(x)=\frac{P}{8D\lambda_f^{3}}\,
e^{-\lambda_f x}\left(\cos\lambda_f x+\sin\lambda_f x\right),$$

so the peak deflection is $w_0=\dfrac{P}{8D\lambda_f^{3}}=\dfrac{P\alpha_f^{3}}{8D}$,
$w$ is zero again at $x=3\pi\alpha_f/4$, the extremum is at $x=\pi\alpha_f$ with

$$w(\pi\alpha_f)=-w_0e^{-\pi}=-0.0432\,w_0,$$

and the bending moment at the load is $M_0=-Dw''(0)=\dfrac{P}{4\lambda_f}$.

For $T_e=30\ \mathrm{km}$, $E=70\ \mathrm{GPa}$, $\nu=0.25$,
$\Delta\rho=3300-1030=2270\ \mathrm{kg\,m^{-3}}$:

$$D=1.6800\times10^{23}\ \mathrm{N\,m},\qquad k=22\,268.7\ \mathrm{N\,m^{-3}},
\qquad \alpha_f=74.12\ \mathrm{km},$$

and for $P=3.0\times10^{12}\ \mathrm{N\,m^{-1}}$:
$w_0=908.8\ \mathrm{m}$, the bulge is $39.3\ \mathrm{m}$ high at
$x=232.8\ \mathrm{km}$ (at $-232.8$ km on the other side), and $M_0=5.5588\times
10^{16}\ \mathrm{N}$ per unit width.

**Verification.** The demonstration solves the same ODE numerically by FFT on a
periodic 4000 km domain with a narrow Gaussian load, and recovers
$|w(0)|=908.5$ m (agreement to $-0.04\%$) and a bulge of $39.3$ m at
$-232.9$ km. The difference is the finite width of the numerical load. The
agreement of two independent routes — a closed form and a spectral solve — is the
strongest check available for a differential equation of this kind. A further
exact check is the jump condition
$\lim_{\epsilon\to0}D[w''']_{-\epsilon}^{+\epsilon}=P$, which the closed form
satisfies by construction of the $1/8$ coefficient.

### 3.4 Bending stress and the effective elastic thickness

The fibre stress at the plate surface is $\sigma=6M_0/T_e^2$ (the standard
beam result $\sigma=6M/H^2$ for a rectangular section). At $T_e=30\ \mathrm{km}$:

$$\sigma=\frac{6\times5.5588\times10^{16}}{(3.0\times
10^{4})^2}=3.7\times10^{8}\ \mathrm{Pa}=371\ \mathrm{MPa}.$$

That is within a factor of two of the brittle strength of rock at a few
kilometres' depth, so the assumption of a purely elastic 30 km plate is
self-inconsistent: the plate must yield near the load. Holding the deflection
fixed at $908.8\ \mathrm{m}$ and asking what $T_e$ keeps $\sigma$ at
$500\ \mathrm{MPa}$:

$$T_e=30\ \mathrm{km}\times\left(\frac{371}{500}\right)^{2}=16.5\ \mathrm{km},$$

because at fixed deflection $\sigma\propto T_e^{-1/2}$. The demonstration checks
the scaling by recomputing the full solution at $T_e=16.5$ km, which needs a load
of $1.914\times10^{12}\ \mathrm{N\,m^{-1}}$ to produce the same deflection and
then reports $\sigma=500\ \mathrm{MPa}$ exactly.

**This is the meaning of "$T_e$ is an effective thickness":** it is what you must
assume for the elastic solution to be consistent, and it is systematically less
than the thermal thickness. Reporting $T_e$ as a lithospheric thickness is one of
the commonest errors in the literature.

### 3.5 The accretion budget

Let the incoming sediment thickness be $h_s$ and the convergence rate $v_c$. Then
per metre of trench the volume flux of material arriving is

$$q=h_sv_c=400\ \mathrm{m}\times0.050\ \mathrm{m\,yr^{-1}}
=20\ \mathrm{m^2\,yr^{-1}}=20\ \mathrm{km^3\,Myr^{-1}\,km^{-1}} .$$

If a fraction $f_a$ is accreted, the prism's cross-sectional area after time $t$
is $A=f_a q t$, and a wedge of taper $\theta$ has
$A=\tfrac12w^2\tan\theta$, so

$$w=\sqrt{\frac{2A}{\tan\theta}} .$$

For $f_a=0.5$ and $t=10\ \mathrm{Myr}$: $A=100\ \mathrm{km^2}$ and, at
$\theta=12.17^\circ$ ($\tan\theta=0.2157$), $w=30.5\ \mathrm{km}$. For $f_a=1$:
$A=200\ \mathrm{km^2}$, $w=43.1\ \mathrm{km}$. **The width scales as
$\sqrt{f_a}$, so a factor-of-two error in the accreted fraction is a 41% error in
prism width** — a modest sensitivity, which is why prism widths are easier to
match than prism areas.

Compaction expels pore water. With porosity $\phi(z)=\phi_0e^{-z/\lambda_c}$,
$\phi_0=0.60$ and compaction length $\lambda_c=1000\ \mathrm{m}$, a 1 km thick
section holds

$$\int_0^{H}\phi\,\mathrm{d}z=\phi_0\lambda_c\left(1-e^{-H/\lambda_c}\right)
=379\ \mathrm{m^3\,m^{-2}} .$$

Over the $100\ \mathrm{km^2}$ accreted in 10 Myr that is
$3.793\times10^{10}\ \mathrm{m^3}$ per metre of trench, or
$3792.7\ \mathrm{m^3\,yr^{-1}} = 0.120\ \mathrm{L\,s^{-1}}$ per metre of trench,
averaged over the interval. **The flux, not the volume, is the physically useful
number**, and it is the quantity that any study of prism dewatering, of fluid
escape at the seafloor, or of the fluid budget of a subduction zone must explain.

## 4. Physical interpretation

- **The taper is a state, not a coincidence.** A wedge out of equilibrium
  deforms until it regains its critical taper, which is why surface slopes
  cluster over narrow ranges within a single margin.
- **Weak décollements make flat wedges and wide prisms.** A low effective basal
  friction moves the whole load onto the décollement, so the wedge slides along a
  gentle slope instead of building a steep one.
- **The trench depth is a flexure measurement.** The $908.8\ \mathrm{m}$
  deflection is what a plate of that rigidity does under that load; the observed
  depth of the trench is used to infer load and rigidity, with the two trading off
  in exactly the way the trade-off in [15-03-02](02-oceanic-crust-structure.md)
  did.
- **The outer rise is the visible top of a stress field.** The $39.3\ \mathrm{m}$
  bulge is the surface expression of the bending moment, and the normal faults
  that form on the outer rise are the same stress field reaching failure — which is
  also the pathway by which seawater enters the subducted plate.
- **Everything here is inverted for something unmeasured.** The taper gives a
  relation between $\mu_b(1-\lambda_b)$, $\lambda$ and $K$; the flexure gives a
  relation between load, $T_e$ and deflection; the budget gives a relation between
  $f_a$, $h_s$ and $v_c$. The lesson's value is in the relations, not in the
  numbers.

## 5. Assumptions and regime of validity

1. **Two-dimensional, plane strain.** Oblique convergence, along-strike
   variations and trench-parallel flow all break the plane-strain wedge model.
2. **Uniform density, uniform strength.** Real wedges have a density-stratified
   décollement, a weak backstop, and elevated pore pressure in specific strata.
3. **One constant $K$.** The exact (slip-line) solutions have a varying stress
   state; using one $K$ removes the possibility of internal deformation patterns
   and biases $\mu_b$ when the taper is inverted.
4. **Small angles.** Exact for $\theta\lesssim30^\circ$ to a few per cent; the
   $0.54\%$ residual measured here is the size of the approximation at
   $\theta=12^\circ$.
5. **Zero frontal resistance, steady state, no erosion.** A submarine prism in a
   sediment-starved setting is dominated by erosion, not accretion.
6. **Elastic plate.** Valid only where the bending stress stays below the yield
   strength; the $371\ \mathrm{MPa}$ computed above shows that it does not, which
   is why $T_e$ is fitted rather than predicted.
7. **The load is a line load.** Real trench loads are distributed over the
   subducted slab's buoyancy structure, so the outer-rise bulge predicted here is
   a lower bound.
8. **Compaction is exponential and one-dimensional.** Lateral dewatering and
   tectonic overpressure are ignored; both change the expelled volume and the
   direction of flow.
9. **The partition $f_a$ is a choice.** It is the least constrained quantity in
   the whole budget and is usually inferred from the prism's internal structure,
   not from the taper.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| surface slope | $\alpha$ | rad or deg | small-angle only in radians |
| taper | $\theta$ | rad or deg | |
| friction coefficients | $\mu,\mu_b$ | dimensionless | |
| pore-pressure ratio | $\lambda$ | dimensionless | but $\lambda\to1$ is singular |
| stress ratio | $K$ | dimensionless | |
| rigidity | $D$ | $\mathrm{N\,m}$ | $\mathrm{Pa\,m^3}$ |
| foundation modulus | $k$ | $\mathrm{N\,m^{-3}}$ | $(\rho_m-\rho_w)g$ |
| flexural length | $\alpha_f$ | m | $\left(\mathrm{N\,m}/\mathrm{N\,m^{-3}}\right)^{1/4}$ |
| line load | $P$ | $\mathrm{N\,m^{-1}}$ | |
| deflection | $w$ | m | $P/(D\lambda^{3})$ is dimensionally a length |
| bending moment | $M$ | $\mathrm{N}$ | per unit width |
| fibre stress | $\sigma$ | Pa | $M/T_e^{2}$ |
| volume flux | $q$ | $\mathrm{m^2\,yr^{-1}}$ | thickness × velocity |

The two checks worth doing every time: $P/(8D\lambda_f^3)$ must come out in metres,
and $6M_0/T_e^2$ must come out in pascals. A factor-of-$10^{3}$ slip in the
density or in $T_e$ (kilometres versus metres) is the usual cause of failure.

## 7. Worked examples

All numbers are printed by `code/subduction_zones_marine_demo.py`.

### Example 1 — the taper and its verification

$\theta=(0.55\times0.60+0.05236)/(3.000\times0.60)=0.21242\ \mathrm{rad}
=12.17^\circ$, so $\alpha=9.17^\circ$. The numerical balance at that slope has a
residual of $+0.54\%$ of the push ($P=1.0902\times10^{13}$, shear
$9.3589\times10^{12}$, base-normal horizontal $1.4843\times10^{12}\ \mathrm{N\,m^{-1}}$).
Using $\alpha=12.17^\circ$ instead leaves a $+20.7\%$ residual, so the
subtraction of $\beta$ matters.

### Example 2 — how much pore pressure?

To raise the surface slope from $9.17^\circ$ to $12.50^\circ$ at fixed $\mu_b$
and $\beta$, the décollement's pore-pressure ratio must rise from $0.40$ to
$0.80$: $+0.40$ in $\lambda$ buys $3.33^\circ$ of slope, at a local rate of
$12.5^\circ$ per unit $\lambda$ near $\lambda=0.8$. Halving $\mu_b$ instead, from
0.55 to 0.275, *lowers* $\theta$ by
$0.275\times0.6/1.8=0.0917\ \mathrm{rad}=5.25^\circ$ — so pore pressure is the
stronger control near the top of its range.

### Example 3 — flexure, deflection and bulge

$D=1.6800\times10^{23}\ \mathrm{N\,m}$,
$\alpha_f=74.12\ \mathrm{km}$, and with
$P=3.0\times10^{12}\ \mathrm{N\,m^{-1}}$:

$$w_0=\frac{3.0\times10^{12}}{8\times1.6800\times10^{23}\times
(1.3492\times10^{-5})^3}=908.8\ \mathrm{m},$$

with the bulge $908.8\,e^{-\pi}=39.3\ \mathrm{m}$ at
$\pi\alpha_f=232.8\ \mathrm{km}$. The FFT solution of the same equation gives
$908.5$ m and $39.3$ m.

### Example 4 — the plate yields

$\sigma=6M_0/T_e^2$ with $M_0=P/(4\lambda_f)=5.5588\times10^{16}\ \mathrm{N}$
gives $371\ \mathrm{MPa}$ at $T_e=30$ km. Capping the stress at
$500\ \mathrm{MPa}$ at the same deflection requires
$T_e=30\times(371/500)^2=16.5\ \mathrm{km}$, verified in the demonstration by
resolving with $P=1.914\times10^{12}\ \mathrm{N\,m^{-1}}$ and
$D=2.785\times10^{22}\ \mathrm{N\,m}$ ($\alpha_f=47.3$ km).

### Example 5 — the prism and its water

$q=20\ \mathrm{km^3\,Myr^{-1}\,km^{-1}}$, $f_a=0.5$, $t=10\ \mathrm{Myr}$
$\Rightarrow A=100\ \mathrm{km^2}$ and $w=30.5$ km at
$\theta=12.17^\circ$. The compacting section releases
$379\ \mathrm{m^3}$ of water per square metre of section, which is
$3.793\times10^{10}\ \mathrm{m^3}$ per metre of trench over the interval, i.e.
$3792.7\ \mathrm{m^3\,yr^{-1}}$ or $0.120\ \mathrm{L\,s^{-1}}$ per metre of trench.
For comparison, the total sediment flux is $20\ \mathrm{m^2\,yr^{-1}}$ per metre
of trench, i.e. $20\ \mathrm{m^3\,yr^{-1}}$ of rock per metre of trench, so the
expelled water volume is about $190\times$ the accreted solid volume — the
water is not a trace component of the prism budget.

## 8. Python demonstration

`code/subduction_zones_marine_demo.py` prints, with units:

1. the taper constants, the closed-form $\theta$ and $\alpha$, and the residual of
   an independently numerically integrated finite-angle force balance;
2. the $\alpha(\lambda)$ table with its finite-difference slope;
3. $D$, $k$, $\alpha_f$, $w_0$, the bulge amplitude and position, and the
   bending moment;
4. the FFT verification of the flexure solution;
5. the fibre stress and the $T_e$ implied by a $500\ \mathrm{MPa}$ cap, with the
   re-solved check;
6. the accretion budget: sediment flux, prism cross-section and width for three
   accreted fractions, and the compaction water volume and rate;
7. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/03-seafloor-tectonics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_zones_marine_demo.py
```

## 9. Exercises

[`exercises/03-subduction-zones-marine-exercises.md`](./exercises/03-subduction-zones-marine-exercises.md)
and
[`exercises/03-subduction-zones-marine-solutions.md`](./exercises/03-subduction-zones-marine-solutions.md).

## 10. Real-world applications

- **Tsunami generation.** The taper and the décollement's depth control the
  geometry of the fault that is the tsunami source; prism structure influences
  splay faulting ([04-07-05 Tsunami](../../04-earth-science-geology/07-geologic-hazards/05-tsunami.md)).
- **Seismic hazard and megathrust coupling.** The width of the seismogenic zone
  is bounded by the transition from brittle to ductile, which depends on the
  strength and fluid pressure of the interface.
- **Subduction-zone fluid budgets.** Prism dewatering and the hydration state of
  the incoming plate set the water flux into the mantle wedge and hence the
  arc's magmatism.
- **Gas hydrates and slope stability.** Overpressure in the prism is both a
  hazard for submarine landslides and, where the hydrate stability zone seals the
  décollement, a control on taper
  ([15-04-02 Gas Hydrates](../04-seafloor-mapping-and-habitats/02-gas-hydrates.md)).
- **Trench and outer-rise sedimentology.** The sediment thickness entering the
  trench determines whether the margin is accretionary or erosive, and that in
  turn determines the forearc's shape.

## 11. Further reading

- **Dahlen, F. A., "Critical taper model of fold-and-thrust belts and accretionary
  wedges", *Annual Review of Earth and Planetary Sciences*.** Level: research.
  The exact solution and the origin of the taper relation derived above in
  approximate form.
- **Turcotte, D. L., & Schubert, G., *Geodynamics*, Cambridge University Press.**
  Level: graduate textbook. Flexure and the plate-bending equation in the notation
  used here.
- **Watts, A. B., *Isostasy and Flexure of the Lithosphere*, Cambridge University
  Press.** Level: research monograph. The systematic treatment of $T_e$,
  including why it differs from the thermal thickness.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can derive the critical-taper relation from the force balance.
- [ ] I can state the residual the small-angle approximation leaves and how to
      test the derivation numerically.
- [ ] I can compute $\alpha$ for a given $\lambda$ and say how sensitive it is.
- [ ] I can derive $D$, $\alpha_f$, $w_0$ and the bulge amplitude and position.
- [ ] I can convert a deflection into a bending moment and a fibre stress.
- [ ] I can compute the $T_e$ implied by a yield cap at fixed deflection.
- [ ] I can budget a prism's sediment and pore water and state which quantity is
      least constrained.
## Common pitfalls
1. **Inverting a slope for $\mu_b$ while ignoring $\lambda$.** They are
   multiplied and divided by the same factors; the slope alone cannot separate
   them.
2. **Calling $T_e$ a lithospheric thickness.** It is a fitted quantity that
   absorbs yielding, and it is systematically smaller.
3. **Forgetting the bending stress before trusting an elastic solution.** A
   $371\ \mathrm{MPa}$ fibre stress at 30 km is not compatible with a purely
   elastic plate.
4. **Quoting a prism area without a time.** Area is a rate integral; the
   accretion rate is the quantity that must balance the plate convergence.
5. **Treating the accreted fraction as measured.** It is the least constrained
   number in the budget and it is what most interpretations actually hinge on.
6. **Assuming the décollement is a single surface.** Prisms have several
   active and inactive décollements, and the taper responds to whichever is
   currently weakest.
7. **Confusing the bulge with the trench.** The outer-rise bulge is at
   $\pi\alpha_f$ — hundreds of kilometres from the trench axis — and is tens of
   metres high, not kilometres.

## Related modules
- [15-03-02 Oceanic Crust Structure and Ophiolites](02-oceanic-crust-structure.md) —
  the plate being bent and consumed.
- [15-03-04 Fracture Zones, Transform Faults and Oceanic Anomalies](04-fracture-zones.md) —
  the age and structure of the incoming plate that the prism sees.
- [15-04-01 Benthic Habitat Mapping and Classification](../04-seafloor-mapping-and-habitats/01-habitat-mapping.md) —
  how prism and trench topography are mapped and classified.
- [13-03-03 Orogenic Systems](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/03-orogenic-systems.md) —
  the continental-side counterpart of this wedge arithmetic.
- [13-06-01 Isostasy, Flexure and Modelling](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the general theory of the flexure applied here.
- [18-03-01 Why Regularise](../../18-inverse-problems/03-regularization/01-why-regularize.md) —
  why an inversion with three unknowns and one datum needs external information.
