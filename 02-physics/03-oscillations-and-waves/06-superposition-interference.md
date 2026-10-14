---
id: 02-03-06
title: "Superposition, Interference and Standing Waves"
level: intermediate
prereqs: ["02-03-04", "02-03-05", "01-03-05"]
estimated_minutes: 90
tags: [waves, superposition, interference, standing-waves]
---

# Superposition, Interference and Standing Waves

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the superposition principle and identify the assumption (linearity)
   that licenses it.
2. **Derive** the interference pattern of two monochromatic sources, including
   the exact fringe positions and the far-field approximation
   $x_m \approx m\lambda L/d$, and state when the approximation is valid.
3. **Derive** the standing-wave solution from two counter-propagating waves, find
   its nodes and antinodes, and distinguish it from a travelling wave by its
   energy flux (which is zero).
4. **Apply** the superposition principle to the normal modes of a bounded string
   or layer, and to the two-source pattern used in phased arrays and
   interferometric location.
5. **Account** for energy correctly: interference redistributes energy, it does
   not create or destroy it.
6. **Verify** all of the above numerically, including the quantitative size of
   the small-angle error in the fringe formula.

## Prerequisites

- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](./04-wave-basics.md)
  — phase, wavelength and the phase-velocity relations.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the linear equation whose linearity is used here.
- [01-03-05 Phase, Harmonics and Simple Harmonic Motion](../../01-mathematics/03-trigonometry/05-phase-and-harmonics.md)
  — sum-to-product identities.

## 1. The principle, and the assumption behind it

The **superposition principle** states that if $u_1$ and $u_2$ are solutions of a
linear, homogeneous equation, then $a u_1 + b u_2$ is also a solution for any
constants $a$, $b$. For the wave equation this is immediate: the operator
$\partial_t^2 - c^2\nabla^2$ is linear.

Two caveats separate the principle from a truism:

- **Homogeneity matters.** A linear equation with a source term is not
  superposable in the same way: two sources give the sum of the *source* terms,
  which is the basis of the Green-function method but not of the statement above.
- **Linearity is an assumption about the medium.** In a nonlinear medium
  (finite-amplitude seismic waves, breaking waves, a saturated amplifier) the
  sum of two solutions is not a solution: harmonics are generated, waves interact,
  and interference is no longer reversible.

Almost everything in this lesson is a consequence of superposition, and every
statement has a stated regime beyond which it fails. Interference is the most
general prediction of wave physics; it is also the most fragile.

## 2. Precise definitions

**Interference.** The modification of the resultant amplitude where two or more
waves overlap, arising from the phase relationship between them.

**Constructive interference.** Waves in phase, so their amplitudes add:
$\Delta\varphi = 2m\pi$.

**Destructive interference.** Waves in antiphase, so their amplitudes subtract:
$\Delta\varphi = (2m+1)\pi$.

**Coherence.** A stable phase relationship between two waves. Only coherent waves
produce a *stationary* interference pattern; incoherent waves produce a pattern
that moves or averages out.

**Standing wave.** A solution of the form
$u(x,t) = F(x)\,G(t)$ — spatial and temporal dependence separated — so the
pattern does not travel and the net energy flux is zero.

**Node / antinode.** A location where the amplitude of a standing wave is
permanently zero / maximal.

## 3. Derivations

### 3.1 Two monochromatic sources: the exact condition

Two line sources separated by $d$ on the $z = 0$ plane radiate at frequency
$\omega$ and wavelength $\lambda$; the receivers lie along a line at distance $L$.
At a receiver at position $x$, the distances to the two sources are

$$r_{1,2} = \sqrt{\left(x \pm d/2\right)^2 + L^2} , \tag{1}$$

and, ignoring the slow amplitude factors, the field is proportional to

$$u = e^{ikr_1} + e^{ikr_2}
= 2\cos\!\left(\frac{k(r_1-r_2)}{2}\right)e^{ik(r_1+r_2)/2} . \tag{2}$$

The **exact** interference condition is therefore

$$r_1 - r_2 = m\lambda \quad\text{(constructive)},\qquad
r_1 - r_2 = \left(m+\tfrac12\right)\lambda \quad\text{(destructive)}. \tag{3}$$

For $|x| \ll L$ and $d \ll L$, expanding equation (1) gives
$r_1 - r_2 \approx xd/L$, so

$$x_m \approx \frac{m\lambda L}{d} : \qquad
\text{fringe spacing } \Delta x \approx \frac{\lambda L}{d} . \tag{4}$$

The approximation's error is $O((x/L)^2)$ relative — **not** small when the
screen is only tens of source-separations away. The demo measures it: at
$L/d = 20$ with $\lambda = 0.5$ m the exact first maximum is at
$x = 10.330981$ m while the far-field formula gives 10.000000 m, an error of
3.2 per cent. The lesson to carry: the formula everyone quotes is a small-angle
result, and *the regime of validity is $x \ll L$ and $d \ll L$*.

### 3.2 A source phase offset steers the pattern

If source 2 leads source 1 by $\delta$, equation (3) becomes
$r_1 - r_2 + \delta\lambda/(2\pi) = m\lambda$, so the pattern translates by

$$\Delta x = \frac{\delta\lambda}{2\pi}\frac{L}{d} \qquad\text{(far field)} ,
\tag{5}$$

and the exact shift is found by solving
$r_1 - r_2 = \delta/k$ by the same geometry as above. The demo's numbers
($\delta = \pi/2$: measured 2.50550 m, small-angle 2.50000 m, exact 2.50568 m)
show the same 0.2 per cent obliquity correction. Two applications, opposite in
direction but identical in algebra: **beam steering** (choose $\delta$ to aim the
pattern) and **interferometric source location** (measure the phase difference at
two receivers and infer where the source is).

### 3.3 Standing waves

Consider two equal counter-propagating waves:

$$u = A\cos(kx - \omega t) + A\cos(kx + \omega t) = 2A\cos(kx)\cos(\omega t) ,
\tag{6}$$

using $\cos(\alpha\pm\beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$. The
result factorises: $F(x) = 2A\cos kx$, $G(t) = \cos\omega t$. Consequences:

- **Nodes** at $kx = (2m+1)\pi/2$, i.e. $x = (2m+1)\lambda/4$; **antinodes** at
  $x = m\lambda/2$.
- The time-averaged kinetic energy density is
  $\tfrac12\rho\langle u_t^2\rangle = \rho A^2\omega^2\cos^2kx$, which is zero at
  the nodes — the *time-averaged* energy profile is $\propto\cos^2kx$ and does
  not move.
- The energy flux $\langle -c^2u_tu_x\rangle = 0$ identically: the two travelling
  components carry equal and opposite fluxes. A standing wave transports no net
  energy, which is what makes it a *resonance* rather than a wave in transit.

### 3.4 Bounded systems and the quantisation of wavelength

A string fixed at $x=0$ and $x=L$ must have a node at each end. Combining a wave
and its reflection (that is, imposing the boundary condition) yields the
standing-wave solutions

$$u_n(x,t) = \sin\!\left(\frac{n\pi x}{L}\right)\cos(\omega_nt),
\qquad \omega_n = \frac{n\pi c}{L} , \qquad n = 1,2,3,\dots \tag{7}$$

These are exactly the normal modes of lesson 02-03-03 in the continuum limit
(compare equation (8) of that lesson with $ka = n\pi/(N+1)$), which is a
satisfying consistency check: the discrete chain and the continuum string agree
mode by mode as $N\to\infty$ at fixed $n$.

Equation (7) quantises the *wavelength* rather than the frequency: only
$\lambda_n = 2L/n$ fits. For a cavity of length $L$ with a free end (an
impedance contrast), the same argument gives a *quarter-wave* resonance,
$L = (2n-1)\lambda/4$, which is the basis of quarter-wave anti-reflection
coatings in optics and of the tuning thickness in seismic interpretation.

### 3.5 Beats, and the bridge to wave packets

Adding two waves of slightly different frequencies at the same place:

$$A\cos\omega_1t + A\cos\omega_2t
= 2A\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)
\cos\!\left(\frac{\omega_2-\omega_1}{2}t\right), \tag{8}$$

a fast carrier with a slow envelope at $|\omega_2-\omega_1|/2$. The envelope
maximum-to-maximum time is $2\pi/|\omega_2-\omega_1|$. This is the time-domain
face of the wave packet of lesson 02-03-07, and equation (10) of lesson 02-03-03
is the same identity applied to space and time separately.

### 3.6 Energy bookkeeping

For two equal-amplitude coherent waves, the intensity is

$$I = |u_1+u_2|^2 = |u_1|^2 + |u_2|^2 + 2\Re\{u_1u_2^*\} . \tag{9}$$

The interference term averages to zero over a phase difference spanning $2\pi$,
so

$$\langle I\rangle = I_1 + I_2 \qquad\text{(average)}, \qquad
I_{\max} = 4I_1, \qquad I_{\min} = 0 \quad\text{(equal amplitudes)}. \tag{10}$$

The demo verifies the average exactly: the mean of $|1+e^{i2\pi c}|^2$ over one
full period is 2.000000000000 against the sum $1+1$ of the two intensities, with
a difference of $2.2\times10^{-15}$. **Interference is a redistribution, not a
source of energy**, and any claimed interference effect that violates equation
(10) is wrong.

## 4. Physical interpretation

**Interference is how a system measures a length in wavelengths.** The whole of
interferometry — Michelson, VLBI, seismic arrays, fibre-optic DAS — is the
observation that a phase difference is a length divided by a wavelength, so a
known wavelength converts a phase into a distance.

**Standing waves are the fingerprint of a boundary.** A travelling wave carries
energy away; a standing wave is trapped. Where boundaries exist, the spectrum
becomes discrete — the origin of mode frequencies, of musical pitch, of resonances
in a sedimentary layer, and of the selective transmission of a thin bed.

**Zero net flux is not zero energy.** A standing wave has energy density
oscillating locally, with the local kinetic and potential energies exchanging
twice per period; the *net* transport is zero because the two travelling
components cancel. Confusing the two statements leads to the mistaken belief that
a resonance "cannot" lose energy — it loses energy to whatever couples it to the
outside, which is what gives it a finite $Q$ (lesson 02-03-02).

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linearity | superposition holds | Harmonics, wave–wave interaction, shocks |
| Coherence | stable phase relation | Moving sources or scatterers blur the pattern; a finite coherence length limits the observable order $m$ |
| Monochromatic | one frequency | A pulse is a superposition of frequencies; if the medium is dispersive the pattern moves (lesson 02-03-07) |
| Equal amplitudes and no geometric spreading | $1/\sqrt r$ or $1/r$ neglected | Contrast falls with distance; the fringe pattern is modulated by the amplitude envelope |
| Small-angle geometry for $\lambda L/d$ | $x \ll L$, $d \ll L$ | The exact condition (3) must be used; the error is $O((x/L)^2)$ |
| Boundaries at nodes for equation (7) | fixed ends | Free ends, impedance contrasts and radiating boundaries give different quantisation |

## 6. Units and dimensional analysis

- Equation (3): both sides are lengths ✓.
- Equation (4): $[\lambda L/d] = \mathrm{m\times m/m} = \mathrm{m}$ ✓; note the
  formula is *not* dimensionally a wavelength, it is a distance on the screen,
  which is why it scales with $L$.
- Equation (5): $\delta$ is in radians (dimensionless) and
  $\lambda L/(2\pi d)$ scales as $\mathrm{m\times m/m}$, a distance ✓.
- Equation (7): $[c/L] = \mathrm{s^{-1}}$ ✓, so $\omega_n$ is an angular
  frequency; $n$ is a positive integer and must be dimensionless.
- Equation (9): each term is an intensity, and the cross term has the same units
  as the squares ✓.

A quick check of the node positions: $(2m+1)\lambda/4$ for $m=0$ gives
$\lambda/4$ from a node, which for a fixed-end string at $x=0$ is the first
antinode at $\lambda/4$ — exactly what the demo measures (0.25, 0.75, 1.25,
1.75, 2.25 m for $\lambda = 1$ m, using the *cosine* convention where $x=0$ is an
antinode; for the sine convention the nodes move to multiples of $\lambda/2$).
State your convention.

## 7. Python demonstration

[`code/interference_demo.py`](./code/interference_demo.py) computes the exact
two-source field, verifies the energy identity, measures the standing-wave
profile and shifts the pattern with a source phase offset. Observed output:

```text
wavelength 0.5 m, source separation d = 2.0 m, screen distance L = 40.0 m, d/L = 0.05
maxima nearest the axis (m): -22.9710, -10.2940, +0.0000, +10.2940, +22.9710
measured half-spacing of the central pair = 10.294000 m
exact condition r1 - r2 = lambda          = 10.330981 m (-0.358 per cent)
small-angle lambda L/d                    = 10.000000 m (-3.204 per cent)
```

```text
mean of |1 + exp(i 2 pi c)|^2 over one full period of c = 2.000000000000
sum of the two separate intensities (1 + 1)           = 2.000000000000
difference = +2.220e-15
```

```text
u(x,t) = 2A cos(kx) cos(omega t), wavelength 1.0 m, A = 1 m,
max |<u^2>_t - 2 A^2 cos^2(kx)| over the grid = 2.220e-16 m^2
predicted nodes at odd multiples of lambda/4: 0.25, 0.75, 1.25, 1.75, 2.25 m
measured nodes from <u^2>_t:                   0.25, 0.75, 1.25, 1.75, 2.25 m
max |u| over the whole field = 2.000000 (predicted 2A = 2.000000)
```

```text
 delta (rad)   measured max x (m)   small-angle (m)    exact (m)
      0.0000              0.00000           0.00000      0.00000
      1.5708              2.50550           2.50000      2.50568
      3.1416              5.04100           5.00000      5.04108
```

### What to observe

| Observation | Consequence |
|---|---|
| The exact fringe position is 3.2 per cent above $\lambda L/d$ at $L/d = 20$ | The far-field formula has a quantified error; state the geometry before using it |
| The measured maximum sits 0.36 per cent *below* the exact position | The $1/\sqrt r$ amplitude weighting tilts the maximum; the exact condition (3) is for equal amplitudes |
| The average of $|1+e^{i2\pi c}|^2$ is 2 to 15 digits | Energy bookkeeping is exact, not approximate — a useful test of any interference code |
| The measured standing-wave profile matches $2A^2\cos^2kx$ to $2\times10^{-16}$ | The time average over exactly one period is exact when the sampling is chosen to span a period |
| Nodes lie at odd multiples of $\lambda/4$ from the antinode at $x=0$ | Node spacing is half a wavelength; the convention (sine or cosine) must be stated |
| The measured pattern shift matches the exact solution to 0.007 per cent and the far-field formula to 0.2 per cent | The steering relation is the same small-angle approximation in a different guise |

> **Breaking exercise.** Change $L$ to 8 m (so $L/d = 4$) and predict, before
> running, the percentage error of the far-field fringe formula. Then check
> whether the error scales like $(x/L)^2$.

## 8. Common mistakes

1. **Using $\lambda L/d$ outside its regime.** It is a small-angle result; the
   error has already reached 3 per cent at $L/d = 20$.
2. **Forgetting that interference requires coherence.** Two independent lamps do
   not produce fringes; two independent seismic vibrators do not either, unless
   they are synchronised.
3. **Adding amplitudes where intensities are needed (or vice versa).** Add fields
   *before* squaring when the sources are coherent; add intensities when they are
   not.
4. **Believing that destructive interference destroys energy.** It moves it to
   the constructive regions; the average is the sum.
5. **Confusing standing waves with travelling waves.** A standing wave has fixed
   nodes and zero net energy flux; its energy is stored, not transported.
6. **Mixing sine and cosine conventions for node positions.** A node at
   $\lambda/4$ in one convention is at $\lambda/2$ in the other; state which
   boundary condition you imposed.
7. **Assuming a bounded layer resonates at any frequency.** Only the discrete set
   $\omega_n = n\pi c/L$ (or the quarter-wave set) satisfies the boundary
   conditions.
8. **Ignoring the finite temporal coherence of a real source.** A source with
   bandwidth $\Delta f$ has a coherence time $\sim1/\Delta f$, which limits the
   path difference over which fringes survive to $c/\Delta f$ — the coherence
   length.

## 9. Real-world applications

- **Seismic interferometry and ambient-noise correlation.** The cross-correlation
  of noise recorded at two stations recovers the Green function between them, and
  its arrival time is a travel time; the underlying algebra is equation (2), with
  the noise providing the coherent superposition. Data are available from
  [EarthScope](https://www.earthscope.org) and [ORFEUS](https://www.orfeus-eu.org)
  and are processed with [ObsPy](https://docs.obspy.org).
- **Phased arrays and beam steering.** Array processing uses equation (5) in
  reverse: apply phase delays to steer sensitivity toward a direction, and use the
  pattern to reject noise from elsewhere.
- **Thin-bed tuning and quarter-wave resonance.** A layer one quarter-wavelength
  thick produces the maximum reflection amplitude; interpreting amplitude against
  thickness requires knowing which side of the tuning peak the bed sits on
  (see [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Reflection and anti-reflection coatings.** The same quarter-wave argument sets
  the design of optical coatings and of acoustic matching layers on transducers.
- **Normal modes of the Earth and of buildings.** Equation (7) in three dimensions
  is the free-oscillation problem; the discrete spectrum is what makes modal
  analysis possible (lesson 02-03-03).
- **SONAR and RADAR.** Interference of the direct and reflected paths produces the
  multipath fading that dominates low-altitude radar and shallow-water acoustics.

## 10. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** Interference, standing waves and the modal decomposition
  of a bounded medium. Level: advanced.
- **Born, M., & Wolf, E. *Principles of Optics* (Cambridge University Press).**
  The definitive treatment of two-source interference, coherence and the
  far-field approximation of §3.1. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** Array design and interference in
  field practice. Level: intermediate.
- **Shearer, P. M. *Introduction to Seismology* (3rd ed., Cambridge University
  Press, 2019).** Array analysis and the resolution of sources with multiple
  stations. Level: intermediate.
- **Strogatz, S. H. *Nonlinear Dynamics and Chaos* (CRC Press).** Beats and coupled
  oscillators, with the intuition before the formalism. Level: beginner to
  intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [04 Wave Description](./04-wave-basics.md) — the phase bookkeeping used here.
- [05 Deriving the Wave Equation from Continuum Physics](./05-wave-equation-derivation.md)
  — the linearity that makes superposition valid.
- [07 Dispersion, Group Velocity and Phase vs Group Speed](./07-dispersion.md) —
  beats generalised to wave packets.
- [09 Diffraction, Scattering and Resolution Limits](./09-diffraction.md) —
  interference with a continuum of sources.
- [03 Coupled Oscillators and Normal Modes](./03-coupled-oscillators.md) — the
  discrete version of §3.4.
- [01-10-02 The Fourier Transform](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md)
  — the general decomposition of which superposition is the first case.
- [06-seismology](../../06-seismology/README.md) — array processing and ambient
  noise.

Exercises:
[`exercises/06-superposition-interference-exercises.md`](./exercises/06-superposition-interference-exercises.md)
and
[`exercises/06-superposition-interference-solutions.md`](./exercises/06-superposition-interference-solutions.md).

## Self-assessment checklist

- [ ] I can state the superposition principle and name the assumption behind it.
      (Section 1)
- [ ] I can derive the exact two-source interference condition and the far-field
      fringe spacing, and state the error of the latter. (Section 3.1)
- [ ] I can derive the standing-wave solution from two counter-propagating waves
      and locate its nodes and antinodes. (Section 3.3)
- [ ] I can show that a standing wave carries no net energy and explain why that
      does not contradict energy conservation. (Sections 3.3, 3.6)
- [ ] I can derive the quantised modes of a bounded string and relate them to the
      discrete-chain normal modes. (Section 3.4)
- [ ] I can compute the energy bookkeeping of two-beam interference and state
      $I_{\max}$, $I_{\min}$ and $\langle I\rangle$. (Section 3.6)
- [ ] I can explain the difference between coherent and incoherent superposition
      and give one geophysical example of each. (Sections 2, 9)
- [ ] I can state the quarter-wave rule and give two applications.
      (Sections 3.4, 9)
