# Solutions — 09-06-01 Cross-Hole and Borehole-to-Surface Tomography

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [01 Cross-Hole and Borehole-to-Surface Tomography](../01-cross-hole-tomography.md).

---

## ★1 — Geometric factor and forward check

$$r_{AM} = \sqrt{12^{2}+0^{2}} = 12.000000,\quad
r_{BM} = \sqrt{12^{2}+2^{2}} = \sqrt{148} = 12.165525,$$
$$r_{AN} = \sqrt{12^{2}+2^{2}} = 12.165525,\quad
r_{BN} = \sqrt{12^{2}+0^{2}} = 12.000000 .$$

The bracket is
$\frac{1}{12} - \frac{1}{12.165525} - \frac{1}{12.165525} + \frac{1}{12}
= 0.0833333 - 0.0821995 - 0.0821995 + 0.0833333
= 2.2677\times10^{-3}\ \mathrm{m^{-1}}$ (the computer value is
$2.2676794\times10^{-3}$; the last digits differ from a hand evaluation because
of rounding).

$$K = \frac{4\pi}{2.267679\times10^{-3}} = 5541.51\ \mathrm{m},$$
$$\frac{\Delta V}{I} = \frac{50.000\times2.267679\times10^{-3}}{4\pi}
= 9.0228\times10^{-3}\ \Omega,$$
$$\rho_a = K\,\frac{\Delta V}{I} = 5541.51\times9.0228\times10^{-3}
= 50.000\ \Omega\,\mathrm{m} = \rho_0 .\ ✔$$

The $4\pi$ is inside the factor: $\rho_a = \rho$ only if the $\Delta V/I$ formula
is divided by $4\pi$, because the whole-space Green's function is
$I\rho/(4\pi r)$. Forgetting it returns $4\pi\rho_0 = 628.3\ \Omega\,\mathrm{m}$.

---

## ★2 — Pole-pole kernel at a midpoint

$$J(\mathbf{r}) = -\frac{\mathbf{u}_A\cdot\mathbf{u}_M}
{16\pi^{2}\sigma_0^{2}\,r_A^{2}\,r_M^{2}}
\qquad [\Omega^{2}\,\mathrm{m^{-2}}].$$

At the midpoint of $A=(0,0,0)$ and $M=(10,0,0)$: $r_A = r_M = 5\ \mathrm{m}$,
$\mathbf{u}_A = +\hat{\mathbf{x}}$ and $\mathbf{u}_M = -\hat{\mathbf{x}}$, so
$\mathbf{u}_A\cdot\mathbf{u}_M = -1$ and

$$J = -\frac{-1}{16\pi^{2}(0.05)^{2}(5^{2})(5^{2})}
= \frac{1}{16\pi^{2}\times0.0025\times625}
= \frac{1}{246.74} = +4.053\times10^{-3}\ \Omega^{2}\mathrm{m^{-2}} .$$

$J>0$ means that *increasing* the conductivity there **increases** the measured
potential difference: the perturbation is between the two electrodes, where extra
conduction pushes more current towards the receiver.

---

## ★3 — Reading the resolution diagonal

A resolution diagonal of 0.787 beside the electrodes says that $78.7\%$ of a
conductivity anomaly placed there is recovered at that cell, whereas 0.168 in the
middle says that only $16.8\%$ is: an anomaly midway between the holes appears
mostly smeared into its neighbours, so its reported amplitude must not be read as
a rock property.

---

## ★4 — Kernel values at three points

$\sigma_0 = 0.05$, $A=(0,0,0)$, $M=(10,0,0)$.

**(i)** $\mathbf{r}=(5,0,0)$: $r_A=r_M=5$, $\mathbf{u}_A\cdot\mathbf{u}_M=-1$,
$J = +4.053\times10^{-3}\ \Omega^{2}\mathrm{m^{-2}}$ (from ★2).

**(ii)** $\mathbf{r}=(5,3,0)$: $r_A=r_M=\sqrt{25+9}=\sqrt{34}=5.830952$, and
$\mathbf{u}_A=(5,3,0)/5.830952$,
$\mathbf{u}_M=(-5,3,0)/5.830952$, so
$\mathbf{u}_A\cdot\mathbf{u}_M = (-25+9)/34 = -16/34 = -0.470588$ and

$$J = -\frac{-0.470588}{16\pi^{2}\times0.0025\times34^{2}}
= \frac{0.470588}{16\pi^{2}\times0.0025\times1156}
= \frac{0.470588}{456.4} = +1.031\times10^{-3}\ \Omega^{2}\mathrm{m^{-2}} .$$

**(iii)** $\mathbf{r}=(5,0,3)$: $r_A = r_M = \sqrt{25+9} = 5.830952$,
$\mathbf{u}_A=(5,0,3)/5.830952$, $\mathbf{u}_M=(-5,0,3)/5.830952$,
$\mathbf{u}_A\cdot\mathbf{u}_M = (-25+9)/34 = -0.470588$; the geometry is a
rotation of (ii), so $J = +1.031\times10^{-3}\ \Omega^{2}\mathrm{m^{-2}}$.

**Ordering and geometry.** The kernel is largest at the midpoint, where the two
unit vectors are exactly opposed ($\cos\theta = -1$) and both distances are
smallest; moving off-axis reduces the cosine magnitude and increases both
distances, and the two effects compound. (ii) and (iii) are exactly equal because
the configuration is axially symmetric about the line $AM$; any anisotropy in the
true sensitivity would come from the medium, not from this kernel.

---

## ★5 — How many numbers does the survey measure?

The singular spectrum spans $3.0\times10^{3}$ in condition number, so every
direction is formally recoverable at the noise level used
($\sigma_d = 3.99\times10^{-7}\ \Omega$ against $s_{\min}m \sim
1.96\times10^{-7}\times0.5$). The count of "independent numbers" is therefore not
fixed by the spectrum alone: it depends on the noise. Two reasons the count is
less than the 24 cells:

1. **Damping.** The resolution diagonal is 0.12–0.79, never 1: the inversion
   trades amplitude for stability, so the effective number of resolvable
   parameters is closer to 12–16 than to 24.
2. **Geometry.** Even with no damping, cells that are only sampled by nearly
   parallel sensitivity distributions are combined, not separated; the
   demonstration's equivalence model (§7 of the lesson) shows that a change of
   model norm 7.04 produces a data change of $1.4\times10^{-7}\ \Omega$, which is
   below the noise.

---

## ★6 — A uniform perturbation, from the identity

For a uniform relative perturbation, the response is exactly linear:
$\rho \to \rho(1+\delta)$ changes $\Delta V/I$ by the same relative amount, so

$$\frac{\Delta V}{I} \to 9.0228\times10^{-3}\times(1 - 0.01)
= 8.9326\times10^{-3}\ \Omega,$$

a change of $-9.02\times10^{-5}\ \Omega$. The piece of information used is the
normalisation identity: the volume integral of the kernel equals
$-1/(4\pi\sigma_0^{2}r_{AM})$, i.e. the exact uniform-perturbation derivative.
Without that identity the uniform case would have to be integrated over the whole
volume, which is exactly what the identity saves you from.

---

## ★7 — Designing to reduce equivalence

Model answer. The equivalence factor is $\|\mathbf{m}_{\text{alt}}-\mathbf{m}_{\text{true}}\|/\|\mathbf{m}_{\text{est}}-\mathbf{m}_{\text{true}}\|$,
and for a given model norm it scales inversely with the smallest singular value of
the scaled Jacobian. Design targets: (a) raise $s_{\min}$ by adding electrode
depth combinations that break the near-parallel structure of the sensitivity
distribution — in the demonstration, interleaving the source and receiver depths
(e.g. source depths at 3, 5.5, 8, 10.5, 13, 15.5, 18 m and receiver depths
offset by half a step) is the cheapest way to do this without a third hole;
(b) keep the bipole length short compared with the depth sampling so that each
quadrupole has a compact, well-localised sensitivity; (c) do not exceed the
number of electrodes available, since more quadrupoles of the same type adds
little. **Criterion for success:** recompute the singular spectrum, form the
equivalence model of §7 and require the ratio to fall below 2 in three
independent noise realisations. A design that cannot state its expected spectrum
is not a design.

---

## ★8 — Measuring the cost of the unparameterised region

Model answer. Build the same survey twice: once with the model space covering the
full inter-hole volume including the first 0.3 m beside each electrode, and once
with the demonstration's 2 m exclusion. Generate data from a forward model — a
finite-difference solution of the Poisson equation with the anomaly placed *inside*
the excluded region — in each case. Invert with the restricted parameterisation
and report (i) the relative data misfit, (ii) the bias in the recovered anomaly
amplitude at the nearest parametrised cell, and (iii) the same quantities when
the anomaly is placed in the parametrised region as a control. **Statistic that
reveals it:** the difference between the two misfits, normalised by the noise
(the excluded-region anomaly produces an excess misfit above the noise floor),
together with the recovered-amplitude bias at the nearest cell. A null result on
the control case is what makes the experiment interpretable.
