---
id: 06-01-04
title: "Reflected, Refracted and Converted Body Waves"
level: advanced
prereqs: ["06-01-02", "02-04-03"]
tags: [seismology, zoeppritz, reflection-coefficient, refraction, converted-waves, energy]
---

# Reflected, Refracted and Converted Body Waves

A wave that meets a change in material properties splits. This lesson derives
the split from the two conditions that any interface must satisfy — displacement
and traction are continuous — obtains the reflection coefficients in full,
derives Snell's law as a by-product rather than an assumption, and then measures
the energy balance and the arrival pattern.

```
.venv/bin/python 06-seismology/01-elastic-wave-propagation/code/body_wave_arrivals_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the normal-incidence reflection and transmission coefficients from
   continuity of displacement and traction, and **state** which sign convention
   each published formula uses.
2. **Derive** the energy-flux balance, identify the correct flux factor, and
   **show** by measurement that replacing it with $v_1/v_2$ is an error.
3. **Derive** Snell's law from phase matching at the interface, and **state**
   the critical angle and what happens beyond it.
4. **Write down** the structure of the Zoeppritz system as four equations in
   four unknowns, and **explain** why conversion between P and SV appears at
   oblique incidence but not at normal incidence.
5. **Measure** the energy partition at a set of incidence angles and **verify**
   it sums to one.

## Prerequisites

- [06-01-02 P and S Waves](./02-p-and-s-waves.md) — the speeds and
  polarisations.
- [02-04-03 Constitutive Laws and Generalised Hooke's
  Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)
  — how stress is obtained from strain.
- [02-03-08 Reflection, Refraction and Snell's Law for
  Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md)
  — the scalar version of §4.

## 1. Intuition: an interface can only do two things

At an interface, whatever the waves on either side are doing, the material must
not tear and must not interpenetrate. Those two statements are:

- **displacement is continuous** (no tear, no overlap),
- **traction is continuous** (no net force on a massless plane).

Everything else follows. The scalar case has two waves (reflected, transmitted)
and two conditions. The elastic case has, in the sagittal plane, **four** waves
— reflected P, reflected SV, transmitted P, transmitted SV — and four
conditions: $u_x$, $u_z$, $\sigma_{zz}$, $\sigma_{xz}$. That is the whole of the
Zoeppritz problem: four equations, four unknowns, no physics beyond the two
statements above.

## 2. Precise definitions

Throughout this lesson, quantities are labelled 1 for the medium the wave is
leaving and 2 for the medium it enters, $\theta$ for P angles, $\gamma$ for S
angles, and subscripts $i$ and $t$ for incident and transmitted.

$$Z = \rho v \quad\text{(acoustic impedance, }\mathrm{kg\,m^{-2}\,s^{-1}}\text{)},
\qquad
p = \frac{\sin\theta}{v} \quad\text{(ray parameter, }\mathrm{s\,m^{-1}}\text{)}.
\tag{1}$$

- **Reflection coefficient** $R$: the amplitude ratio of a reflected wave to the
  incident wave, at the same interface and the same mode.
- **Transmission coefficient** $T$: the same ratio for the transmitted wave.
- **Conversion**: a reflected or transmitted wave whose *type* differs from the
  incident one; the coefficient is then written $R_{ps}$, $T_{ps}$, etc.
- **Critical angle** $\theta_c$: the incidence angle at which the transmitted
  angle reaches $90°$, $\sin\theta_c = v_1/v_2$.
- **Post-critical**: incidence beyond $\theta_c$, where the transmitted leg is
  **evanescent** — its vertical wavenumber is imaginary, it carries no net
  vertical energy, and the reflection coefficient becomes complex.

## 3. Normal incidence, in full

### 3.1 The two conditions

Let a P wave of unit displacement amplitude travel in the $+x$ direction in
medium 1. Write the total displacement as

$$u_1 = e^{i(k_1x-\omega t)} + R\,e^{i(-k_1x-\omega t)}, \qquad
u_2 = T\,e^{i(k_2x-\omega t)}, \tag{2}$$

where $R$ and $T$ are both measured **on the $+x$ displacement component**. For
a P wave in a rod-like geometry the only stress is
$\sigma_{xx} = \rho v^2\,\partial u/\partial x$.

**Condition A — displacement continuous at $x=0$:**

$$u_1(0)=u_2(0) \;\Longrightarrow\; 1+R = T. \tag{3}$$

**Condition B — traction continuous at $x=0$:**

$$\rho_1v_1^2\,(ik_1)\,(1-R) = \rho_2v_2^2\,(ik_2)\,T
\;\Longrightarrow\; \rho_1v_1(1-R) = \rho_2v_2\,T. \tag{4}$$

Substituting $k=\omega/v$ is the step that turns $\rho v^2k$ into $\rho v\omega$;
the common $\omega$ cancels, leaving the impedances. **This is why the impedance
and not the speed controls reflection.**

### 3.2 The solution, and the sign conventions

Substituting (3) into (4): $Z_1(1-R) = Z_2(1+R)$, hence

$$R^{(\text{disp})} = \frac{Z_1-Z_2}{Z_1+Z_2}, \qquad
T^{(\text{disp})} = \frac{2Z_1}{Z_1+Z_2}. \tag{5}$$

These are the coefficients for the **displacement amplitude on the $+x$
axis**. Many texts write

$$R^{(\text{stress})} = \frac{Z_2-Z_1}{Z_2+Z_1} = -R^{(\text{disp})}, \tag{6}$$

which is the same physical statement with the reflected wave's amplitude measured
as a **stress** (or with the reflection axis defined so that the reflected
leg's displacement is positive when it points backwards). **Both are in
circulation and they differ by a sign.** The lesson's convention is (5) unless
stated otherwise; when comparing with a published formula, check which of (5)
and (6) its author uses before concluding that there is a discrepancy.

### 3.3 The energy-flux balance

The time-averaged vertical energy flux of a plane wave of displacement amplitude
$A$, speed $v$, density $\rho$ and incidence angle $\theta$ is

$$\Phi = \tfrac12\rho\omega^2A^2v\cos\theta. \tag{7}$$

For the normal-incidence problem $\cos\theta=1$ for every leg, so flux
conservation $\Phi_i=\Phi_r+\Phi_t$ gives

$$\tfrac12\rho_1\omega^2v_1 = \tfrac12\rho_1\omega^2v_1R^2
+ \tfrac12\rho_2\omega^2v_2T^2
\;\Longrightarrow\;
1 = R^2 + \frac{Z_2}{Z_1}T^2
\;\Longleftrightarrow\;
R^2+\frac{\rho_2v_2}{\rho_1v_1}T^2 = 1. \tag{8}$$

**The flux factor is $Z_2/Z_1$, not $v_1/v_2$.** The two coincide only when the
densities are equal. With the SYNTHETIC model of §8 ($\rho_1=2400$, $\rho_2=2600$,
$v_1=3000$, $v_2=4500$) the measured sums are

| balance used | value | error from 1 |
|---|---|---|
| $R^2 + (Z_2/Z_1)T^2$ | 0.9999999999999998 | $2.2\times10^{-16}$ |
| $R^2 + (v_1/v_2)T^2$ | 0.4436885865 | 0.5563 |
| $R^2 + T^2$ | 0.6371882086 | 0.3628 |

The substitution of $v_1/v_2$ for $Z_2/Z_1$ is a numerical error of 56 per cent
here, and the whole discrepancy is accounted for by
$(Z_2/Z_1)/(v_1/v_2)=2.4375$ against the density ratio $\rho_2/\rho_1=1.083333$
— see the demonstration for the arithmetic. **Verify the flux factor against a
case with a density contrast whenever you write it down.**

## 4. Snell's law, derived from phase matching

**Step 1 — the requirement.** All the waves at the interface must oscillate in
step along the interface; otherwise the boundary conditions could not hold at
all times. Every leg therefore has the same horizontal factor
$\exp\!\big(i(k_x x-\omega t)\big)$, so the **horizontal wavenumber**
$k_x = k\sin\theta = \omega\sin\theta/v$ and the **frequency** $\omega$ are the
same for every leg.

**Step 2 — the consequence.** Writing $p = \sin\theta/v = k_x/\omega$,

$$p = \frac{\sin\theta_i}{v_1} = \frac{\sin\theta_r}{v_1}
= \frac{\sin\theta_t}{v_2} = \frac{\sin\gamma_r}{v_{s1}}
= \frac{\sin\gamma_t}{v_{s2}}. \tag{9}$$

This is **Snell's law**, and the quantity $p$ is conserved along the whole ray
system. It was not assumed: it is the statement that the interface cannot
imprint a different spatial period on the two sides.

**Step 3 — the critical angle.** If $v_2>v_1$ then $\sin\theta_t = p v_2$ reaches
1 at $\sin\theta_c = v_1/v_2$. Beyond that, $\sin\theta_t>1$ has no real
solution, $\cos\theta_t = i\sqrt{p^2v_2^2-1}$ is imaginary, and the transmitted
wave becomes evanescent. The reflection then carries all the energy, with a
frequency-dependent phase shift, and the reflection coefficient acquires a
complex phase that no ray picture can explain.

## 5. The Zoeppritz system

### 5.1 The four waves and the four equations

With $z$ positive downward and the interface at $z=0$, write the potentials as
in [06-01-03](./03-surface-waves.md) §2 and label the amplitudes:

| leg | medium | type | amplitude |
|---|---|---|---|
| incident P | 1 | P | 1 |
| reflected P | 1 | P | $B_1$ |
| reflected SV | 1 | S | $C_1$ |
| transmitted P | 2 | P | $A_2$ |
| transmitted SV | 2 | S | $C_2$ |

The four conditions are (using $u_x=\phi_x+\psi_z$, $u_z=\phi_z-\psi_x$ and the
stress relations of [06-01-01](./01-wave-equation-elastic.md) §4):

$$u_x:\; p\,(1+B_1) + s_1r_1C_1 - p\,A_2 - r_2C_2 = 0,$$
$$u_z:\; s_1q_1(1-B_1) - p\,C_1 - q_2A_2 - p\,C_2 = 0,$$
$$\sigma_{zz}:\; \left[-( \lambda_1+2\mu_1)q_1^2-\lambda_1p^2\right](1+B_1)
+ 2\mu_1ps_1r_1C_1 - \left[\dots\right]_2 = 0, \tag{10}$$
$$\sigma_{xz}:\; -2\mu_1ps_1q_1(1+B_1) + \mu_1(p^2-r_1^2)C_1
+ 2\mu_2ps_2q_2A_2 - \mu_2(p^2-r_2^2)C_2 = 0,$$

with $q=\sqrt{v_p^{-2}-p^2}$, $r=\sqrt{v_s^{-2}-p^2}$ and sign factors $s$ that
are $+1$ for a downgoing leg and $-1$ for an upgoing one. Equation (10) is the
**Zoeppritz system**: four linear equations in $(B_1,C_1,A_2,C_2)$. The
coefficients are the only content; the rest is linear algebra.

### 5.2 What the structure tells you before any number is computed

- **Conversion needs an oblique angle.** In the $u_z$ and $\sigma_{xz}$ rows the
  coupling terms between P and SV are both proportional to $p=\sin\theta/v$.
  At $p=0$ the system decouples into a $2\times2$ P problem and a $2\times2$ SV
  problem, and no converted wave exists. Measured: at $p=0$ the reflected and
  transmitted SV amplitudes are both $0.0\times10^{0}$ exactly.
- **The normal-incidence limit is a test.** Extracting the P block of (10) at
  $p=0$ must reproduce (6). Measured: the oblique solver at $p=0$ gives
  $+0.2380952381$ against the closed form $+0.2380952381$, difference
  $5.55\times10^{-17}$.
- **The four conditions are checkable independently.** The demonstration
  re-derives each side's fields by explicit differentiation of that side's own
  potential form — *not* from the coefficient table used to assemble (10) — and
  evaluates the jump at $z=0$:

| quantity | medium 1 | medium 2 | relative jump |
|---|---|---|---|
| $u_x$ | $1.1061290335\times10^{-4}$ | $1.1061290335\times10^{-4}$ | $2.4\times10^{-16}$ |
| $u_z$ | $2.3286845519\times10^{-4}$ | $2.3286845519\times10^{-4}$ | $1.2\times10^{-16}$ |
| $\sigma_{zz}$ | $2.6137613349\times10^{3}$ | $2.6137613349\times10^{3}$ | $1.7\times10^{-16}$ |
| $\sigma_{xz}$ | $7.1229837620\times10^{2}$ | $7.1229837620\times10^{2}$ | $3.2\times10^{-16}$ |

  Agreement at machine precision is what an independent route should give. This
  is the check that found a sign error in the transmitted columns of (10) during
  development — an error to which both the normal-incidence limit and the energy
  sum were blind, because neither senses the overall sign of the transmission.

### 5.3 Energy partition at oblique incidence

With displacement-amplitude ratios $R_{pp}$, $R_{ps}$, $T_{pp}$, $T_{ps}$ and the
flux factors of (7):

$$1 = R_{pp}^2 + \frac{\rho_1v_{s1}\cos\gamma_1}{\rho_1v_{p1}\cos\theta_1}R_{ps}^2
+ \frac{\rho_2v_{p2}\cos\theta_2}{\rho_1v_{p1}\cos\theta_1}T_{pp}^2
+ \frac{\rho_2v_{s2}\cos\gamma_2}{\rho_1v_{p1}\cos\theta_1}T_{ps}^2. \tag{11}$$

For an evanescent leg the corresponding term is **omitted**, because an
evanescent wave carries no net vertical energy. Measured for the synthetic model
of §8, with $\theta_c=41.81°$:

| $\theta_1$ (°) | $R_{pp}$ | $R_{ps}$ | $T_{pp}$ | $T_{ps}$ | flux sum |
|---|---|---|---|---|---|
| 5 | −0.235125 | 0.046793 | 0.763216 | −0.038975 | 1.000000 |
| 15 | −0.213286 | 0.128607 | 0.775232 | −0.117093 | 1.000000 |
| 25 | −0.182556 | 0.173164 | 0.810644 | −0.195646 | 1.000000 |
| 35 | −0.200497 | 0.135430 | 0.928945 | −0.274802 | 1.000000 |
| 40 | −0.363445 | 0.009710 | 1.168692 | −0.312409 | 1.000000 |
| 45 | −0.830438 | 0.436592 | — (evanescent) | 0.400503 | 1.000000 |
| 55 | −0.758172 | 0.481741 | — (evanescent) | 0.436206 | 1.000000 |

The sums are 1 to the printed precision at every angle, including the
post-critical cases where the transmitted P term is removed. Beyond the critical
angle the printed P amplitudes are magnitudes, since the amplitudes are complex.

## 6. Units and dimensional analysis

$q$ and $r$ in (10) are $\mathrm{s\,m^{-1}}$ (vertical slowness), so
$q^2$ is $\mathrm{s^2\,m^{-2}}$; multiplying by a modulus in Pa gives
$\mathrm{kg\,m^{-1}\,s^{-2}}\cdot\mathrm{s^2\,m^{-2}}=\mathrm{kg\,m^{-3}}$,
which combines with the dimensionless amplitude ratios to give a stress once
the $\omega^2$ factored out of the potentials is restored. The clean way to see
it is to note that **every row of (10) must be dimensionally homogeneous**, since
each row is one physical condition; the first two rows are velocities
($p$ and $q$ are slownesses, multiplied by amplitudes carrying
$\mathrm{m\,s^{-1}}$ after the $\omega$ is factored out of $\phi$), and the last
two are stresses. Impedances in (1) are
$\mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-1}}=\mathrm{kg\,m^{-2}\,s^{-1}}$;
$Z_2/Z_1$ and hence the flux factor in (8) is dimensionless.

## 7. Arrivals, and how they are named

| name | path | exists |
|---|---|---|
| P | turns in the mantle | all distances to the shadow zone |
| S | turns in the mantle as a shear wave | as P, later |
| PcP | reflects off the core–mantle boundary | all distances, always after P |
| ScS | the S analogue | as PcP |
| Pn | refracts along the Moho | beyond the Moho critical distance |
| PP, PPP | surface multiples | at increasing time |
| Pdiff | diffracts along the core–mantle boundary | inside the shadow zone |
| PKIKP | through the outer and inner core | beyond ~110° |

Measured at source depth 10 km with the model ObsPy bundles:

| distance (°) | P (s) | S (s) | PcP (s) | ScS (s) | Pn (s) | S−P (s) |
|---|---|---|---|---|---|---|
| 2 | 33.827 | 59.760 | 509.736 | 932.942 | 33.827 | 25.933 |
| 5 | 75.073 | 133.923 | 510.744 | 934.802 | 75.090 | 58.851 |
| 10 | 143.691 | 257.110 | 514.323 | 941.402 | 143.861 | 113.419 |
| 15 | 212.015 | 379.318 | 520.213 | 952.264 | 212.632 | 167.304 |
| 30 | 368.735 | 667.645 | 550.512 | 1008.197 | — | 298.910 |
| 60 | 606.671 | 1099.990 | 652.518 | 1197.222 | — | 493.319 |

Three structural statements are visible in the table: Pn exists only at short
distances, because beyond the critical distance the Moho head wave is overtaken;
PcP is always later than P, as a reflection must be; and S−P grows roughly
linearly with distance, which is what makes it a distance measure.

At 20° the direct P phase has **five** separate arrivals —
272.676, 274.399, 274.619, 278.030 and 278.358 s — because the upper-mantle
discontinuities fold the travel-time curve. See
[06-02-05](../02-ray-theory-and-travel-times/05-shadow-zones.md).

## 8. The Python demonstration

`body_wave_arrivals_demo.py` uses the SYNTHETIC two-layer model
$v_{p1}=3000$, $v_{s1}=1732$, $\rho_1=2400$; $v_{p2}=4500$, $v_{s2}=2600$,
$\rho_2=2600$ (all SI). Results are quoted in §§3.3 and 5.2 above; the remaining
measurements are:

- $Z_1 = 7.2\times10^{6}$, $Z_2 = 1.17\times10^{7}$
  $\mathrm{kg\,m^{-2}\,s^{-1}}$, so $R^{(\text{stress})}=+0.2380952381$,
  $R^{(\text{disp})}=-0.2380952381$ and $T^{(\text{disp})}=+0.7619047619$.
- At $\theta_1=25°$: $\theta_2=39.340477°$, $\gamma_1=14.122249°$,
  $\gamma_2=21.485710°$, with $p=1.408727539\times10^{-4}\ \mathrm{s\,m^{-1}}$
  equal to $\sin\theta_1/v_{p1}$ and to $\sin\theta_2/v_{p2}$ to the printed
  digits — Snell's law is satisfied by construction of the solve and verified
  here as a consistency check.
- The four continuity conditions match to $\sim10^{-16}$ ($5.2$).
- The energy partition sums to 1.000000 at every angle ($5.3$).
- The TauP arrival tables of §7.

## 9. Exercises

**★1.** Derive (5) from (3) and (4) in three lines. Then derive (6) from (5) and
state in words which physical amplitude each one measures.

**★2.** A layer has $Z_1=5.0\times10^6$ and $Z_2=7.5\times10^6\
\mathrm{kg\,m^{-2}\,s^{-1}}$. Compute $R^{(\text{disp})}$, $R^{(\text{stress})}$,
$T^{(\text{disp})}$ and verify (8) numerically. Is the reflection a polarity
reversal?

**★3.** Derive Snell's law from phase matching for the $P$–$SV$ system, and show
that the converted-wave angles obey the same $p$.

**★4.** State the critical angle for the model of §8 and compute it in degrees.

**★★5.** Show that at normal incidence $T^{(\text{disp})}=1+R^{(\text{disp})}$
and that this is a statement of displacement continuity rather than of energy
conservation.

**★★6.** Recompute the energy balance with the wrong flux factor $v_1/v_2$ for
a model with $\rho_1=\rho_2$. Show that the error vanishes when the densities are
equal, and use that to explain why the mistake propagates in textbooks.

**★★7.** Run the demonstration, then change $v_{p2}$ to $6.0$ km/s and report
the new critical angle and the new energy table. State which rows become
post-critical.

**★★8.** The flux sum in the table is 1 at 45°, where the transmitted P leg is
evanescent. Explain in one sentence why removing that term is correct rather
than an approximation.

**★★★9.** Extend the solver to a three-layer model with two interfaces (six
unknowns, six conditions). State how many equations the Zoeppritz structure
becomes and why the number grows as $2n$ for $n$ unknowns per side.

**★★★10.** A gas sand has a large drop in $v_p$ at nearly constant $v_s$ and
nearly constant density. Predict the sign of $R^{(\text{disp})}$ at the top of
the sand at normal incidence, and state how the amplitude would change if the
sand were brine-filled instead. Use the derivation, not a rule of thumb.

## 10. Common mistakes

1. **Mixing the two sign conventions.** Decide once, write it down in the
   header of your notebook, and check against (5) and (6).
2. **Using $v_1/v_2$ as the energy-flux factor.** It is $Z_2/Z_1$; the measured
   error for a plausible density contrast is 56 per cent (§3.3).
3. **Treating $R^2+T^2=1$ as energy conservation.** It is not, and it is wrong
   by 36 per cent in the same model.
4. **Believing that conversion requires anisotropy or a curved interface.** It
   requires only an oblique angle and a contrast in either speed; the mechanism
   is in the $p$-proportional coupling terms of (10).
5. **Using real arithmetic past the critical angle.** $q$ or $r$ becomes
   imaginary; the amplitudes become complex and the phase matters.
6. **Forgetting that Snell's law applies to S legs too.** The same $p$ gives
   $\sin\gamma = p\,v_s$ for the converted legs, which is why converted S angles
   are smaller than the corresponding P angles.
7. **Assuming the first arrival is P at every distance.** Beyond about 98° the
   direct P phase does not exist at all; see
   [06-02-05](../02-ray-theory-and-travel-times/05-shadow-zones.md).

## 11. Real-world applications

- **Reflection seismology.** The whole method is the $p\to0$ limit of (10):
  normal-incidence reflection coefficients are read off a stacked section and
  inverted for impedance. The sign convention error of §3.2 is the single most
  common bookkeeping bug in that workflow.
- **Amplitude-versus-offset (AVO).** The *deviation* from normal incidence —
  the $p$-proportional coupling in (10) — is what distinguishes a gas sand from
  a brine sand, because gas lowers $v_p$ much more than $v_s$.
- **Converted-wave exploration.** Recording the $T_{ps}$ leg (a downward P
  converted to an upward S at a target) gives an independent image whose
  sensitivity to fluid is different from the P image.
- **The Moho and the core.** $Pn$ and $PcP$ in §7 are the phases by which the
  depths of the Moho and the core–mantle boundary were first measured; both are
  applications of the same four conditions.
- **Shear-wave splitting.** $T_{ps}$ from a layer with aligned cracks arrives
  as two modes; see [06-01-08](./08-anisotropic-propagation.md).

## 12. Further reading

- [06-01-02 P and S Waves](./02-p-and-s-waves.md) — the speeds and impedances
  used here.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time
  Curve](../02-ray-theory-and-travel-times/02-snell-and-layering.md) — the
  ray-geometry counterpart of §4, with the head-wave branches.
- [06-01-06 Interface Waves, Head Waves and the Total
  Wavefield](./06-interface-waves.md) — where the evanescent legs of §5.3 are
  treated as waves rather than as excluded terms.
- [03-10-06 Travel Times with TauP and Phase
  Naming](../../03-scientific-computing/10-obspy-and-seismic-data/06-taup-travel-times.md)
  — how the arrivals of §7 are named, computed and picked.
- [https://seis.sc.edu/taup/](https://seis.sc.edu/taup/) — the TauP reference
  implementation whose phase naming this lesson uses.

## 13. Related lessons

- [06-01-01 From Hooke's Law and Newton to the Elastodynamic
  Equation](./01-wave-equation-elastic.md) — the starting point of the
  derivation.
- [06-01-03 Rayleigh and Love Waves](./03-surface-waves.md) — the trapped part
  of the same wavefield.
- [06-02-05 Shadow Zones, Triplications and the Low-Velocity
  Zone](../02-ray-theory-and-travel-times/05-shadow-zones.md) — what a big
  velocity drop does to the arrival pattern.

## 14. Self-assessment

- [ ] Derive (5) from the two interface conditions.
- [ ] State both sign conventions and which one a given textbook uses.
- [ ] Derive the energy-flux balance and justify the factor $Z_2/Z_1$.
- [ ] Show numerically that $v_1/v_2$ is the wrong factor when densities differ.
- [ ] Derive Snell's law by phase matching in four lines.
- [ ] Write the four Zoeppritz equations and say which term vanishes at normal
      incidence.
- [ ] Compute the energy partition at one oblique angle and get 1.
- [ ] Explain why an evanescent leg contributes no flux term.
- [ ] Name four phases that exist only beyond the Moho critical distance or the
      core shadow, and say why.
