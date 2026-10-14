---
id: 12-06-02
title: "Love Numbers and Theoretical Tides"
level: research
prereqs: ["12-06-01", "07-01-02", "07-06-01"]
tags: [global-geophysics, earth-interior, geodesy, love-numbers, tides, elasticity, non-uniqueness]
---

# Love Numbers and Theoretical Tides

> All models and data in this module are **SYNTHETIC**. The body here is a
> teaching body with chosen radius, density and rigidity. No number below is a
> measurement of the Earth. Externally quoted quantities are the exact constant
> $G$ and the classical results that the text derives or checks.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the degree-2 Love numbers $h_{2}$, $k_{2}$ and $l_{2}$ from the
   tidal forcing and the body's response, with units for every quantity.
2. **Derive** the induced degree-2 potential of a displaced surface as a
   degree-2 shell, and **show** that for any homogeneous body
   $k_{2} = \tfrac{3}{5}h_{2}$ independently of its rheology.
3. **Derive** the fluid limit $h_{2} = 5/2$, $k_{2} = 3/2$ from the
   equipotential condition, and **cross-check** the implied flattening
   $f/q = 5/4$ against the exact Maclaurin spheroid.
4. **Evaluate** the homogeneous-sphere elastic result
   $h_{2} = \frac{5}{2}\left[1 + \frac{19}{2}\frac{\mu}{\rho g R}\right]^{-1}$,
   verify its limits and its $1/\mu$ asymptote, and **state** exactly which part
   of it this lesson derives and which part it checks.
5. **Compute** the observable combinations $\delta = 1 + h_{2} - \tfrac{3}{2}k_{2}$
   (gravity tide) and $\tau = 1 + k_{2} - h_{2}$ (surface tilt) and **interpret**
   their fluid and rigid limits.
6. **Invert** a measured $h_{2}$ for an effective rigidity, **quantify** the
   amplification, and **state** the degeneracy that the inversion leaves.
7. **Model** a Maxwell body and **explain** how the phase lag of the tide makes
   it a dissipation measurement.

## Prerequisites

- [12-06-01 Moment of Inertia, Figure and Interior Constraints](01-moment-of-inertia.md) —
  the interior functionals and the exact spheroid figure used here.
- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../../07-gravity-geodesy/01-gravity-fundamentals/02-gravity-potential.md) —
  the potential, its multipoles and the equipotential condition.
- [07-06-01 Solid Earth Tides and Their Gravity Signature](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the observational side of the same physics: what a gravimeter and a tiltmeter
  actually record.

## 1. Definitions

Let an external body raise a degree-2 tide of amplitude $V_{0}$ at the surface of
a body of radius $R$ and surface gravity $g = GM/R^{2}$, so that the tidal
potential is $V_{\text{tide}} = V_{0}P_{2}(\cos\theta)$. The body responds by

- **deforming radially** by $u(\theta) = h_{2}\,(V_{0}/g)\,P_{2}(\cos\theta)$:
  the **radial displacement Love number** $h_{2}$ converts a potential amplitude
  into a length;
- **changing its own potential** at the surface by
  $\delta V = k_{2}V_{0}P_{2}(\cos\theta)$: the **potential Love number**
  $k_{2}$;
- **displacing tangentially** by $v(\theta) = l_{2}\,(V_{0}/g)\,\partial_{\theta}P_{2}(\cos\theta)$:
  the **Shida number** $l_{2}$, which this lesson does not compute further.

All three are dimensionless because each is a ratio of a response to the forcing
that produced it. This is the whole point: a Love number is an *observable* ratio
in which the geometry has cancelled, leaving the material and the structure. The
reader should be suspicious of that "leaving" — §6 shows it is not a clean
separation.

## 2. The kernel: a displaced surface is a degree-2 shell

Take a homogeneous body of density $\rho$ whose surface is displaced radially by
$u_{2}(\theta) = u P_{2}(\cos\theta)$. The mass that moves is a surface shell of
areal density $\sigma_{2} = \rho u$. Its potential, written as the degree-2
coefficient $V_{2}$ such that $V = V_{2}P_{2}(\cos\theta)$, is

$$
V_{2}(r) = -\frac{4\pi G \sigma_{2}}{5}
\times
\begin{cases}
R^{4}/r^{3}, & r \ge R,\\[2pt]
r^{2}/R, & r < R,
\end{cases}
\qquad
V_{2}(R) = -\frac{4\pi G\rho u R}{5} = -\frac{3}{5}\,g\,u ,
$$

using $g = GM/R^{2} = \tfrac{4}{3}\pi G\rho R$ for a uniform sphere. The
demonstration checks the closed form against a direct quadrature of the shell
potential

```text
    r/R = 0.5: closed  -1.258076e-01   quadrature  -1.258074e-01   rel. err 1.2e-06
    r/R = 1.5: closed  -1.491053e-01   quadrature  -1.491050e-01   rel. err 1.7e-06
    r/R = 2.0: closed  -6.290380e-02   quadrature  -6.290372e-02   rel. err 1.2e-06
```

Two consequences are worth stating separately.

- At $r = R$ the closed form gives $-(4\pi G\rho u/5)R$; dividing by $gu$ gives
  exactly $0.600000$. So **for any homogeneous body,
  $k_{2} = \tfrac{3}{5}h_{2}$**, whatever its rheology: the ratio is geometry.
  The demonstration prints this number, and the elastic table of §4 confirms it
  at every rigidity.
- On the shell itself the potential has no jump: the value at $r = R$ is the
  common limit of the two branches. A quadrature that samples exactly *on* the
  shell sees an integrable singularity and is biased low (the demonstration
  reports $-4.91\times10^{-1}$ against $-5.03\times10^{-1}$, a 2.4% bias); the
  same quadrature 0.4 R away agrees to $6\times10^{-6}$. This is a general
  warning about computing a body's own potential on its own boundary.

## 3. The fluid limit, and a cross-check against the exact figure

For a fluid body, the deformed surface must be an equipotential of the total
potential. Writing the total degree-2 potential on the displaced surface and
setting it to zero:

$$
V_{0} + g\,u - \tfrac{3}{5}g\,u = 0
\qquad\Longrightarrow\qquad
u = \frac{5}{2}\,\frac{V_{0}}{g},
$$

that is $h_{2} = 5/2$, and then

$$
k_{2} = \frac{|V_{2}(R)|}{V_{0}} = \frac{3}{5}\,\frac{g u}{V_{0}} = \frac{3}{2},
\qquad
h_{2} = 1 + k_{2} .
$$

The relation $h_{2} = 1+k_{2}$ is the fluid-body statement that the surface is
an equipotential; it holds exactly, as the demonstration confirms to $0.0\times
10^{0}$.

**Cross-check.** For a *rotational* tide, $V_{0} = \tfrac{1}{3}\omega^{2}R^{2}$,
so the fluid Love number predicts a radial displacement
$u/R = h_{2}(1/3)q = (5/6)q$ with $q = \omega^{2}R^{3}/(GM)$, and therefore a
flattening

$$
f = \frac{a-c}{a} = -\frac{3}{2}\,\frac{u}{R} = \frac{5}{4}\,q .
$$

The exact Maclaurin spheroid of
[lesson 01](01-moment-of-inertia.md) gives $f/q = 1.2488$ at $q = 10^{-3}$,
$1.2463$ at $q = 3\times10^{-3}$ and $1.2379$ at $q = 10^{-2}$, approaching
$1.2500$ as $q\to0$. The two independent routes agree in the limit where the
fluid derivation is valid, which is the strongest evidence this lesson can offer
for the $5/2$: not a quotation, but a consistency check between two derivations.

## 4. The elastic body: Kelvin's homogeneous sphere

For a homogeneous incompressible elastic sphere of rigidity $\mu$, the classical
degree-2 static solution is

$$
h_{2}(\hat\mu) = \frac{5}{2}\frac{1}{1 + \tfrac{19}{2}\hat\mu},
\qquad
\hat\mu \equiv \frac{\mu}{\rho g R},
\qquad
k_{2} = \tfrac{3}{5}h_{2}.
$$

The demonstration evaluates it across the whole rigidity range:

```text
   mu/(rho g R)     mu (Pa)      h2        k2      k2/h2    h2*mu_hat
         0.000     0.000e+00    2.5000    1.5000   0.6000     0.0000
         0.100     2.516e+08    1.2821    0.7692   0.6000     0.1282
         0.500     1.258e+09    0.4348    0.2609   0.6000     0.2174
         1.000     2.516e+09    0.2381    0.1429   0.6000     0.2381
        50.000     1.258e+11    0.0053    0.0032   0.6000     0.2626
       500.000     1.258e+12    0.0005    0.0003   0.6000     0.2631
```

Four checks are visible in that table, and it is worth being explicit about what
each one does and does not establish.

- **The fluid limit** $\hat\mu\to0$ gives $h_{2}\to2.5000$ and $k_{2}\to1.5000$,
  matching §3 exactly. This is a genuine check of the formula's structure.
- **The rigid limit** $\hat\mu\to\infty$ gives $h_{2}\to0$: no deformation, no
  induced potential. Also genuine.
- **The ratio** $k_{2}/h_{2} = 0.6000$ at every rigidity. This is *not* a check
  of the coefficient 19; it follows from §2, which is independent of elasticity.
  It is, however, a strong consistency check: a wrong elastic solution would
  violate it.
- **The asymptote**: the column $h_{2}\hat\mu$ tends to $5/19 = 0.26316$, which
  is the only place the coefficient 19 can be measured from the table. The
  approach is slow ($0.2631$ at $\hat\mu = 500$), so it confirms the *leading*
  coefficient but not the next order.

The internal structure of the coefficient — where the 19 comes from, and how it
changes with a layered body — is a boundary-value problem on the elastodynamic
equations; it is treated in
[12-05-02 Tidal Response and the Quality Factor of the Whole Earth](../05-earth-tides-rotation-global/02-tidal-response.md),
and this lesson uses the homogeneous result as a calibrated reference rather than
pretending to re-derive it. The honest statement is: **the fluid limit is
derived here; the elastic coefficient is a classical result whose limits,
ratio and leading asymptote are verified here.**

## 5. The observables: gravity tide and surface tilt

A gravimeter and a tiltmeter do not measure Love numbers; they measure
combinations of them, because the instrument sits on the deforming surface and
senses both the potential change and the displacement.

- **Gravity-tide amplitude factor**: the gravity change is larger than the
  rigid-body value by the factor
  $\delta = 1 + h_{2} - \tfrac{3}{2}k_{2}$.
- **Surface-tilt factor**: the tilt of the surface relative to the
  equipotential is scaled by $\tau = 1 + k_{2} - h_{2}$.

```text
   mu/(rho g R)      h2       k2      delta      tau
         0.000    2.5000    1.5000     1.2500     0.0000
         0.100    1.2821    0.7692     1.1282     0.4872
         0.500    0.4348    0.2609     1.0435     0.8261
         1.000    0.2381    0.1429     1.0238     0.9048
        50.000    0.0053    0.0032     1.0005     0.9979
```

Read the limits: a perfectly fluid body has $\delta = 1.25$ and $\tau = 0$ (its
surface is an equipotential, so there is *no* tilt relative to the equilibrium
tide); a perfectly rigid body has $\delta = \tau = 1$. Both endpoints are
physical and both are model statements, not observations. The measured $\delta$
says how fluid the body is — but through the single combination $\hat\mu$, so an
observed $\delta$ constrains a *ratio* of rigidity to density and gravity, never
a rigidity.

## 6. Worked example: inverting a measured $h_{2}$

Adopt the synthetic measurement $h_{2} = 0.60 \pm 0.01$. Invert the Kelvin
relation:

$$
\hat\mu = \frac{1}{9.5}\left(\frac{2.5}{h_{2}} - 1\right).
$$

| $h_{2}$ | $\hat\mu$ | $\mu = \hat\mu\rho g R$ (Pa) |
|---|---|---|
| 0.59 | 0.3408 | $8.57\times10^{8}$ |
| 0.60 | 0.3333 | $8.39\times10^{8}$ |
| 0.61 | 0.3261 | $8.21\times10^{8}$ |

The demonstration measures the amplification
$|\mathrm{d}\ln\hat\mu/\mathrm{d}\ln h_{2}| = 1.316$: a 1% error in $h_{2}$ moves
the inferred rigidity by about 1.3%. That looks like a well-posed inversion, and
within the model it is. The degeneracy appears one step out:

```text
   rho (kg/m^3)      mu (Pa)        h2 check
         2500.0    6.9893e+08     0.6000
         3500.0    9.7850e+08     0.6000
         5000.0    1.3979e+09     0.6000
         6000.0    1.6774e+09     0.6000
```

Every row reproduces the same $h_{2}$ with a different density *and* a different
rigidity: what is measured is $\mu/\rho$, and a factor 2.4 in density buys a
factor 2.4 in rigidity. Beyond that, $h_{2}$ is a functional of the whole profile:
a body with a stiff lid over a weak interior can return the same $h_{2}$ as a
uniform body with an intermediate rigidity. The lesson of §6 is therefore:

> A single Love number determines an *effective* rigidity of a *parameterised*
> body. It does not determine a rigidity, and it does not see a profile.

## 7. Frequency dependence: a Maxwell body

The static Love numbers are a limit, not the general case. For a Maxwell solid
with elastic rigidity $\mu$ and Maxwell time $\tau_{M} = \eta/\mu$, the complex
rigidity at angular frequency $\omega$ is

$$
\mu(\omega) = \mu\,\frac{i\omega\tau_{M}}{1 + i\omega\tau_{M}},
$$

and substituting it into the homogeneous solution gives a complex, frequency
dependent pair $(h_{2},k_{2})$. With a synthetic $\hat\mu = 0.5$ and
$\tau_{M} = 9.45\times10^{10}$ s (about 3000 yr):

```text
   period (h)     omega (1/s)     |h2|      |k2|     arg k2 (deg)
         12.0      1.454e-04    0.4348    0.2609         -0.000
       1000.0      1.745e-06    0.4348    0.2609         -0.000
    1000000.0      1.745e-09    0.4348    0.2609         -0.287
  100000000.0      1.745e-11    0.5057    0.3034        -25.209
 1000000000.0      1.745e-12    1.8385    1.1031        -34.116
100000000000.0      1.745e-14    2.4999    1.4999         -0.449
```

Three regimes are visible. Much shorter than $\tau_{M}$ the body is elastic
($|k_{2}| = 0.26$). Near $\omega\tau_{M}\sim1$ the response peaks in phase lag —
$-34^{\circ}$ — which is where dissipation is most efficiently excited and where
the tide is a $Q$ measurement. Much longer than $\tau_{M}$ the body has relaxed
to the fluid value $|k_{2}| = 1.5$.

One caution, stated explicitly: this single-Maxwell-time model has *one*
relaxation time, while a real body has a spectrum of them (different mechanisms,
different depths, different temperatures). A single-frequency inversion returns
an effective property at that frequency, and the frequency dependence is where
the profile information hides — which is why the diurnal and long-period tidal
bands are used jointly.

## 8. Assumptions and regime of validity

| Assumption | Where it enters | What happens when it fails |
|---|---|---|
| Homogeneous, incompressible body | §4 | The coefficient 19 changes; the fluid limit does not |
| Static response (no inertia, no time dependence) | §§2–5 | At frequencies near a body resonance the response is dynamical, and $h_{2}$ is not enough |
| Linear response | all | Tides are small; for a body near its Roche limit they are not |
| A sharp free surface | §2 | A body with an ocean or atmosphere has a different *effective* Love number for the tide raised at the fluid surface |
| Instantaneous, frequency-independent rheology | §§1–6 | §7 replaces it with a Maxwell body; the phase lag is the observable that reveals it |
| Self-gravity described by the spherically symmetric part only | §2 | A strongly deformed or rapidly rotating body needs the figure theory of lesson 01 |

A specifically important non-assumption: the derivation of $k_{2} = \tfrac{3}{5}
h_{2}$ used **only** homogeneity and self-gravity. It is valid for a fluid body,
an elastic body, and a viscous body, and any inversion that returns a
$k_{2}/h_{2}$ ratio different from $0.6$ for a homogeneous body has a bug or a
heterogeneous body.

## 9. Python demonstration

[`code/tidal_love_numbers_demo.py`](code/tidal_love_numbers_demo.py):

1. the degree-2 shell kernel, closed form against quadrature, and the exact
   ratio $k_{2} = \tfrac{3}{5}h_{2}$;
2. the fluid limit derived from the kernel, cross-checked against the exact
   Maclaurin figure;
3. the elastic homogeneous sphere: limits, ratio and the $1/\mu$ asymptote;
4. the observables $\delta$ and $\tau$ across the rigidity range;
5. the inversion of a synthetic $h_{2}$ and the density–rigidity degeneracy;
6. a Maxwell body and the frequency dependence of the phase lag.

```bash
cd 12-global-geophysics-interior/06-geodesy-constraints-interior/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_love_numbers_demo.py
```

## 10. Exercises

[`exercises/02-tidal-love-numbers-exercises.md`](exercises/02-tidal-love-numbers-exercises.md)
and the worked
[`exercises/02-tidal-love-numbers-solutions.md`](exercises/02-tidal-love-numbers-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** Derive $k_{2} = \tfrac{3}{5}h_{2}$ for a homogeneous body from the
> degree-2 shell potential, keeping the units visible.
> **(b)** A gravimeter measures a gravity-tide factor $\delta = 1.13$. Using the
> elastic homogeneous model, compute $h_{2}$, $k_{2}$ and $\hat\mu$, and give
> $\mu$ in Pa for $\rho = 3500\ \mathrm{kg\,m^{-3}}$, $R = 6.0\times10^{6}$ m.
> **(c)** Explain in two sentences why the same $\delta$ would also be produced
> by a body with half that density and twice that rigidity.
> **(d)** A body's tidal phase lag is observed to be $30^{\circ}$ at a period of
> one week. State whether a single-Maxwell-time body can explain it, and what
> additional observation would test the explanation.

A worked version of (a)–(b) is in the lesson-02
[solutions](exercises/02-tidal-love-numbers-solutions.md).

## Common pitfalls

1. **Quoting $h_{2}$ without the $R$, $\rho$, $g$ that make it dimensionless.**
   The number means nothing until the normalisation is stated.
2. **Treating an effective rigidity as a rigidity.** §6 is the counter-example.
3. **Ignoring the ocean or atmosphere** when comparing a tide-gauge observation
   with a solid-body Love number: the water surface is its own equipotential.
4. **Using the static Love number for a resonant tide.** Near a free oscillation
   the dynamic amplification is not described by the static number.
5. **Assuming $k_{2}/h_{2}$ is a material ratio.** It is $3/5$ by geometry for a
   homogeneous body; a different ratio signals heterogeneity, not a new rheology.
6. **Forgetting that on-shell potentials are limits.** A quadrature that samples
   the boundary returns a biased value; the closed form is the limit.

## Related modules

- [12-06-01 Moment of Inertia, Figure and Interior Constraints](01-moment-of-inertia.md) —
  the figure theory that the rotational cross-check in §3 uses.
- [12-06-03 Nutation and Constraints on Core Properties](03-nutation-constraints.md) —
  the same resonance physics at the diurnal frequencies, where a fluid core
  appears.
- [12-05-02 Tidal Response and the Quality Factor of the Whole Earth](../05-earth-tides-rotation-global/02-tidal-response.md) —
  the full elastogravitational boundary-value problem.
- [07-06-01 Solid Earth Tides and Their Gravity Signature](../../07-gravity-geodesy/06-earth-tides-and-rotation/01-solid-earth-tides.md) —
  the observational counterpart in the gravity folder.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  why an effective parameter is often all a finite data set can support.
