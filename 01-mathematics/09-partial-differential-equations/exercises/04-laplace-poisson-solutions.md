# Solutions — 01-09-04 Laplace and Poisson Equations in Earth Systems

> **Read this after attempting the exercises, not before.**
>
> **Convention.** Throughout, $V$ is positive, $\mathbf{g} = \nabla V$, and
> $\nabla^2V = -4\pi G\rho$. Every sign below is tied to that choice; with the
> opposite convention ($\Phi = -V$, $\mathbf{g} = -\nabla\Phi$) every Poisson
> equation flips sign.
>
> $G = 6.674\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$;
> $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. Numbers were computed, not
> estimated; where a result is quadrature-limited the limitation is stated.

---

## ★1 — A uniform sphere

**(a) Mass.** With $a = 1.2\times10^{3}$ m and
$\rho = 3.0\times10^{3}\ \mathrm{kg\,m^{-3}}$,

$$V_{\text{sphere}} = \frac{4}{3}\pi a^3 = 7.2382\times10^{9}\ \mathrm{m^3},
\qquad M = \rho V_{\text{sphere}} = 2.1715\times10^{13}\ \mathrm{kg} .$$

**(b) Exterior potential at $r = 5$ km.** By the shell theorem the exterior
potential is that of a point mass at the centre:

$$V = \frac{GM}{r} = \frac{6.674\times10^{-11}\times2.1715\times10^{13}}{5.0\times10^{3}}
= \frac{1.4493\times10^{3}}{5.0\times10^{3}} = 0.28985\ \mathrm{m^2\,s^{-2}} .$$

Note the units: $V$ has units of energy per unit mass, $\mathrm{J\,kg^{-1}} =
\mathrm{m^2\,s^{-2}}$.

**(c) Surface gravity.**

$$g(a) = \frac{GM}{a^2} = \frac{1.4493\times10^{3}}{1.44\times10^{6}}
= 1.0064\times10^{-3}\ \mathrm{m\,s^{-2}} ,$$

which is

$$\frac{1.0064\times10^{-3}}{10^{-5}} = 100.6\ \mathrm{mGal} .$$

For scale, this is a very large anomaly — of order 100 mGal against the Earth's
$\sim 9.8\ \mathrm{m\,s^{-2}}$ — because the body is 2.4 km across and unusually
dense. A realistic ore body at that depth would give microgals to milligals, which
is why feasibility calculations of the kind done in
[01-01-01](../../01-arithmetic/01-number-systems-and-precision.md) precede any
survey design.

**(d) The Laplacian in the three regions.**

| Region | $\nabla^2V$ | Reason |
|---|---|---|
| $r < a$ (inside) | $-4\pi G\rho = -2.515\times10^{-6}\ \mathrm{s^{-2}}$ | Poisson's equation with $\rho = 3000$ |
| $r > a$ (outside) | $0$ | Laplace's equation; the field is harmonic |
| $r = a$ (on the surface) | not defined as a classical function | the density jumps; the equation holds in the distributional sense |

The surface case is worth a sentence. The classical Laplacian requires continuous
second derivatives, which a field whose source has a jump does not possess at the
jump. What *is* well defined is the pair of one-sided limits and the **jump
condition**: the normal derivative of $V$ jumps by exactly $-4\pi G$ times the
surface density of the mass sheet at the discontinuity. For a uniform sphere there
is no surface mass sheet, so $V$ and its tangential derivatives are continuous,
and only the *second* derivative jumps — from $-4\pi G\rho$ inside to $0$ outside.
Stated in terms of the field, $\partial g_r/\partial r$ jumps by $-4\pi G\rho$.
Getting this bookkeeping right is what allows the layered models of
[01-09-05](../05-separation-of-variables.md) to be matched at interfaces.

---

## ★2 — The mean value property

**Statement.** If $u$ is harmonic on an open set containing the closed ball
$B(\mathbf{c},R)$, then

$$u(\mathbf{c}) = \frac{1}{4\pi R^2}\oint_{\lvert\mathbf{r}-\mathbf{c}\rvert = R}
u(\mathbf{r})\,dA ,$$

i.e. the value at the centre equals the average over the sphere.

**Verification for $V = GM/r$ with the source outside the sphere.** Let the mass be
at the origin and the sphere centre at $\mathbf{c}$ with $c = \lvert\mathbf{c}\rvert
> R$. The potential is harmonic throughout the ball (the source is outside), so the
property must hold. To verify it directly, use a multipole-free argument: expand
$1/\lvert\mathbf{r}-\mathbf{r}'\rvert$ with $\mathbf{r}' = \mathbf{c} +
\mathbf{s}$, $\lvert\mathbf{s}\rvert = R$, so

$$V(\mathbf{c}+\mathbf{s}) = \frac{GM}{\lvert \mathbf{c} + \mathbf{s}\rvert}
= \frac{GM}{c}\left[1 + \frac{R}{c}P_1(\cos\gamma)
+ \frac{R^2}{c^2}P_2(\cos\gamma) + \dots\right] ,$$

where $\gamma$ is the angle between $\mathbf{s}$ and $\mathbf{c}$. Averaging over
the sphere kills every $P_n$ with $n\ge1$, because
$\oint P_n(\cos\gamma)\,dA = 0$ for $n\ge1$ while
$\oint P_0\,dA = 4\pi R^2$. Hence

$$\frac{1}{4\pi R^2}\oint V\,dA = \frac{GM}{c} = V(\mathbf{c}) .$$

The demonstration verifies the discrete version of the same statement for a
harmonic solution:
the largest deviation of an interior node from the average of its four neighbours
is $8.73\times10^{-13}$, i.e. zero to the residual tolerance.

**What the property forbids.** It forbids an interior value that is locally
extreme: an isolated peak in a harmonic field is impossible, so a spike in a
potential-field map must come from a source ($\nabla^2V\ne0$), from a boundary, or
from a processing or noise artefact. It is the cheapest consistency test available
on a gridded field, and it is why smoothing operators used in data processing that
do *not* preserve the mean value introduce a bias.

---

## ★3 — Consistency of a Laplace solution

**(a) Value at the centre** $(x,y) = (0.5,0.5)$:

$$u = \frac{\sinh(\pi/2)\sin(\pi/2)}{\sinh\pi}
= \frac{2.30130\times1}{11.54874} = 0.199268 .$$

**(b) Consistency with the reported numbers.** The centre value $0.199268$ is less
than both the reported interior maximum $0.924180$ and the boundary maximum
$0.961349$. That is consistent: the maximum of this particular solution is not at
the centre but near the top boundary where the Dirichlet data are applied, and it
decreases monotonically downward for fixed $x$. Nothing is inconsistent.

It is worth checking the direction of the comparison: the interior maximum
$0.924180$ is smaller than the boundary maximum $0.961349$, and both are smaller
than the largest boundary datum, which is $\sin(\pi/2) = 1$ at
$(x,y) = (0.5,1)$ — the node just inside the top edge is not at that point, which
is why the interior maximum is $0.924$ rather than close to 1.

**(c) The maximum principle.** It says that a non-constant harmonic function
attains its maximum and its minimum on the boundary (for a harmonic function, on
$\partial\Omega$), and that interior values lie strictly between them. The reported
numbers obey this: $0.924180 < 0.961349$, and the interior is bounded by the
boundary data.

**Two practical corollaries.** Any downward continuation or interpolation scheme
that produces an interior value exceeding the maximum boundary datum is wrong, and
any field that shows an interior extremum has a source or an artefact — the
diagnostic used in ★★6.

---

## ★4 — The two-dimensional Green's function

**Solve $\nabla^2u = \delta(\mathbf{r})$ in polar coordinates,** looking for a
radially symmetric solution $u(r)$. For $r > 0$ the delta function vanishes, so

$$\frac{1}{r}\frac{d}{dr}\left(r\frac{du}{dr}\right) = 0
\qquad\Longrightarrow\qquad
r\frac{du}{dr} = A \qquad\Longrightarrow\qquad u = A\ln r + B .$$

**Fix $A$ by flux.** Integrate $\nabla^2u = \delta$ over a disc of radius
$\varepsilon$ and use the divergence theorem:

$$\oint_{\lvert\mathbf{r}\rvert=\varepsilon}\frac{\partial u}{\partial n}\,ds
= \oint \frac{A}{\varepsilon}\,\varepsilon\,d\theta = 2\pi A = 1
\qquad\Longrightarrow\qquad A = \frac{1}{2\pi} .$$

So the fundamental solution is

$$u(r) = \frac{1}{2\pi}\ln r + B = \frac{1}{2\pi}\ln\frac{1}{r} + B' ,$$

and the potential of a line source of strength $\lambda$ per unit length is
$2G\lambda\ln(1/r) + B$ in gravitational units.

**Why the additive constant is irrelevant.** Only derivatives of $u$ are physical
(fields, fluxes, forces), and a constant shifts $u$ without changing any
derivative. The constant is fixed by the convention chosen for the datum (for
example $u = 0$ at $r = 1$) and must be stated when a value is quoted. This is the
same freedom as the additive constant in the Neumann problem of ★★5.

**What fails with the 3-D kernel.** Using $1/(4\pi r)$ in a two-dimensional model
corrupts two things. First, the *scaling with distance*: $1/r$ falls off too fast,
so the model under-predicts the far-field amplitude and over-predicts the decay
rate, which in an inversion is absorbed into spurious "deep" or "dense" structure.
Second, the *behaviour at infinity*: $\ln(1/r)\to-\infty$ slowly, so a 2-D model has
no finite total potential and no monopole term that decays — a 2-D body is
effectively an infinite line. That is why a "2-D" gravity profile must be
interpreted with a finite strike length in mind, and why 2-D inversions of real
data must either constrain the strike length or accept a model that does not
represent the ends.

---

## ★★5 — Uniqueness for the Neumann problem, and compatibility

**Proof.** Let $u_1,u_2$ both be harmonic in $\Omega$ with
$\partial u_1/\partial n = \partial u_2/\partial n = g$. Set $w = u_1-u_2$. Then
$\nabla^2w = 0$ in $\Omega$ and $\partial w/\partial n = 0$ on $\partial\Omega$.
Green's first identity gives

$$\int_\Omega w\nabla^2w\,dV + \int_\Omega\lvert\nabla w\rvert^2\,dV
= \oint_{\partial\Omega} w\frac{\partial w}{\partial n}\,dA .$$

The first term vanishes because $\nabla^2w = 0$, and the boundary term vanishes
because $\partial w/\partial n = 0$. Hence
$\int_\Omega\lvert\nabla w\rvert^2 = 0$, so $\nabla w = 0$ in $\Omega$ and
$w$ is constant. Therefore **$u_1 = u_2 + \text{const}$: unique up to an additive
constant** — and the boundary *flux* cannot determine the constant, since adding a
constant changes no derivative.

**Compatibility condition.** Integrate Poisson's equation over $\Omega$ and use the
divergence theorem:

$$\oint_{\partial\Omega}\frac{\partial u}{\partial n}\,dA
= \int_\Omega\nabla^2u\,dV = -4\pi G\,M_{\text{enc}} ,$$

so the prescribed flux must satisfy

$$\oint_{\partial\Omega} g\,dA = -4\pi G\,M_{\text{enc}} .$$

**Physical interpretation.** The left side is the total flux of the gravitational
field through the closed surface; by Gauss's law it equals $-4\pi G$ times the
enclosed mass. So a Neumann problem on a closed surface is *solvable only if the
data are consistent with the mass inside* — which is the statement that you cannot
ask for zero net flux through a surface enclosing a nonzero mass. In practice this
is why a gravity model cannot be posed purely in terms of field components on a
closed box without either including the mass density as an unknown or accepting an
inconsistency in the data.

**Two consequences worth recording.** (i) Since only the gradient of $V$ is
physical, a reported potential is meaningless without its datum; and (ii) in
potential-field inversion the constant is part of the null space, and every
inversion must either remove it or acknowledge it. This is the continuous origin of the fact, used in
[01-09-08](../08-weak-solutions.md) §5, that the discrete stiffness matrix of a
pure Neumann problem has an eigenvalue of zero with the constant function as its
eigenvector — and therefore that Lax–Milgram's coercivity hypothesis fails for
that problem.

---

## ★★6 — An interior maximum in a gravity map

**(a) The shortest argument.** Laplace's equation holds at every point outside any
mass, and a non-constant harmonic function cannot attain an extreme value in the
interior of its domain (the maximum principle). A local maximum in the *observed*
field therefore cannot be explained by a harmonic field, so either the field is not
harmonic there (a source), or the field is not what the processing claims (a
boundary, an artefact, or noise).

A stronger and cheaper argument, when a gridded field is available, is the mean
value property: at a strict local maximum the value exceeds the average of any
small neighbourhood, which a harmonic function forbids. Testing this on the grid is
one line of code.

**(b) The three explanations consistent with the mathematics.**

1. **A source is present** ($\nabla^2V\ne0$): a dense, shallow or magnetised body,
   a void, or a density contrast whose scale is small enough that the anomalous
   local field dominates the smooth regional field over the survey area. This is
   the explanation a geophysicist hopes for, and it is the only one that makes the
   maximum an *observation* rather than a defect.
2. **The boundary/datum is responsible:** the survey boundary is close (3 km). The
   maximum principle applies on a bounded domain with the field determined by its
   boundary values; if the regional field or the datum is imposed as a boundary
   condition, an interior maximum can be produced by the imposed data rather than
   by a source. In practice a local maximum near a survey edge usually means the
   regional trend was removed using an assumption that does not hold there.
3. **A processing or noise artefact:** a levelling error between survey lines, an
   incorrect free-air or Bouguer correction, terrain-correction residue, or
   short-wavelength noise. Analytic continuation of a noisy field *cannot* produce
   a harmonic result, and the resulting map may have local extrema everywhere at
   the noise scale. Since the noise is not harmonic, this explanation violates no
   theorem.

**(c) Which to test first, and how.** Test the **artefact** explanation first,
because it is the cheapest and it must be excluded before the others mean anything:

- check the maximum against the survey's own error estimate (tie-line
  misclosures, repeat readings) and against the terrain-correction residual where
  the topography is rough;
- recompute the field with a different regional-residual separation and see
  whether the maximum survives — a feature that moves when the regional is
  changed is an artefact of the regional, not a body;
- apply a short-wavelength test: upward-continue the field by a few hundred metres
  and see whether the maximum persists. A genuine compact source's anomaly falls
  off with altitude in a way that can be predicted; noise falls off much faster.

Only after the artefact is excluded does it make sense to ascribe the maximum to a
source, and even then the depth–density trade-off of ★★7 and ★★★9 must be reported.

---

## ★★7 — How much contrast can hide behind a null vector?

**(a) The estimate.** The demonstration measures two responses of the same shell
pair: with the density change left uncompensated (the "positive shell" alone) the
exterior potential changes by $4.982\times10^{-2}$ relative; with the
zero-total-mass compensation in place, by $-1.183\times10^{-7}$, i.e. zero to
quadrature accuracy. The ratio is the stated cancellation factor
$4.212\times10^{5}$.

If a measurement is sensitive at 1 part in $10^{7}$ in relative potential, then an
uncompensated signal $s$ can be masked by a compensating perturbation provided
$s/4.212\times10^{5}\lesssim10^{-7}$, i.e.

$$s \lesssim 10^{-7}\times4.212\times10^{5} = 4.2\times10^{-2} .$$

So **an uncompensated contrast producing up to about 4 % in the exterior potential
can be cancelled below a 1-in-$10^{7}$ measurement by a spherically symmetric,
zero-total-mass redistribution of the same mass.** In the demonstration's own
terms, that is a density change of order $500\ \mathrm{kg\,m^{-3}}$ over a
significant fraction of the body's volume.

**(b) Assumptions.**

- The data constrain the exterior potential (or its gradient) somewhere outside the
  body; a borehole traversing the body would break the ambiguity at once.
- The cancellation factor $4.2\times10^{5}$ is the measured one for this geometry
  (a shell pair inside a 30 km ball observed at $2R$); a different geometry has a
  different factor, and the factor is itself a function of the observation height
  and of how much of the mass is redistributed.
- The perturbation is spherically symmetric, because only then is the cancellation
  exact (★★★9 shows that a non-spherical perturbation is detectable).
- The data are noiseless at the stated level; with 1 % noise the factor is
  irrelevant, since 1 % already masks everything below 1 %.

**(c) Why neither extreme answer is right.** The answer is not "only zero contrast
is undetectable", because the cancellation factor is finite: a *modest*
uncompensated signal can be hidden by a compensating shell. And it is not "any
contrast up to 4 % is undetectable", because the estimate applies to the exterior
*potential* and to a *spherically symmetric* compensation; it does not say that a
4 % density change anywhere in the body is invisible, and it says nothing about
observations *inside* the body (a borehole or a mine shaft would see the
redistribution directly), and it does not apply to a non-spherical perturbation. The precise statement is the one written in (a),
with its assumptions attached — which is the difference between a quantitative
claim and a slogan.

---

## ★★8 — Downward continuation

**Derivation.** Represent the field on the measurement plane by its Fourier
components, $V(x,z=0) = \int A(k)\mathrm{e}^{\mathrm{i}kx}dk$. A harmonic field
whose sources lie below must decay upward, so its extension to height $z$ is

$$V(x,z) = \int A(k)\mathrm{e}^{\mathrm{i}kx}\mathrm{e}^{-kz}dk
\qquad (z\ \text{positive upward}),$$

because $\mathrm{e}^{-kz}$ is the only exponential in $z$ that is bounded as
$z\to+\infty$ for $k>0$ (and its mirror for $k<0$). Continuing *downward*, i.e. to
$z = -h$ with $h>0$, multiplies the component of wavenumber $k$ by

$$\mathrm{e}^{+kh} .$$

Downward continuation is therefore exactly a backward-diffusion problem with depth
playing the role of time, and the same ill-posedness applies
([01-09-07](../07-boundary-value-problems.md) §6).

**The cutoff.** Requiring $\mathrm{e}^{kh} > 100$ gives

$$kh > \ln 100 = 4.6052 \qquad\Longrightarrow\qquad
k > \frac{4.6052}{1000\ \mathrm{m}} = 4.605\times10^{-3}\ \mathrm{rad\,m^{-1}} ,$$

$$\lambda = \frac{2\pi}{k} < 1364\ \mathrm{m} .$$

So for a 1 km continuation, **every wavelength shorter than about 1.4 km is
amplified by more than a factor of 100.** A 0.1 % error in the measured field
becomes a 10 % error in the continued field at that wavelength, and the
amplification grows exponentially as the wavelength shortens: at 500 m it is
$\mathrm{e}^{2\pi\times1000/500} = \mathrm{e}^{12.6} = 2.9\times10^{5}$, and at
100 m it is $\mathrm{e}^{62.8} = 1.9\times10^{27}$.

**What this implies for resolution.** A downward-continued gravity or magnetic map
appears sharper, and it is tempting to read the sharpened features as structure at
the continuation depth. The calculation above says that below a wavelength set by
the noise level and the continuation distance, the sharpening is amplified noise.
Practical rules that follow:

- **choose the cutoff from the noise**, not by eye: the shortest wavelength that
  may be continued is the one for which $\mathrm{e}^{kh}$ times the data error
  equals an acceptable model error, i.e. $\lambda_{\min} = 2\pi h/\ln(\eta/\delta)$
  for target error $\eta$ and data error $\delta$;
- **state the continuation distance and the filter** in any published continued
  map, because the two together determine the resolution and neither is
  recoverable from the map itself;
- **expect upward and downward continuation to be asymmetric**: upward
  continuation is stable and can be done with no filter, downward cannot. The
  asymmetry is a property of the equation, not of the software.

---

## ★★★9 — A non-spherical zero-mass perturbation

**Construction.** Inside a uniform ball of radius $R = 30$ km and density
$2800\ \mathrm{kg\,m^{-3}}$, add $+500\ \mathrm{kg\,m^{-3}}$ in the shell
$0.4R\le r<0.7R$ of the **upper** hemisphere, and
$-500\ \mathrm{kg\,m^{-3}}$ in the same radial shell of the **lower** hemisphere.
The total mass change is exactly zero (the two halves have equal volume by
symmetry), but the perturbation is odd under $z\to-z$: it is a dipole pattern.

**Exterior potential** on the axis, by axisymmetric quadrature
(Section 4c of `code/laplace_poisson.py`, so the numbers are reproducible):

```text
      z0 / R             V(ball)           V(dipole)   relative change
         1.2    5.8707915627e+02    5.9372409429e+02        1.1319e-02
         2.0    3.5224634757e+02    3.5472284419e+02        7.0306e-03
         4.0    1.7612305782e+02    1.7675206640e+02        3.5714e-03
```

**(a) Is it a null vector?** No. The relative change is $1.1\times10^{-2}$ at
$1.2R$, far above the $10^{-7}$-level quadrature noise, and monotonically decaying
with height. It is therefore detectable in principle, unlike the spherically
symmetric perturbation of the same total mass (Section 4b of the module's
demonstration, where the relative change is $-1.2\times10^{-7}$).

**(b) The multipole explanation.** The exterior potential of any body can be
written as a series in spherical harmonics,
$V = GM/r + (\text{dipole})/r^2 + (\text{quadrupole})/r^3 + \dots$ The
**monopole** term is $GM/r$, and this perturbation has zero net mass, so its
monopole vanishes. But the perturbation is not spherically symmetric, so the
**dipole and higher moments are not zero**, and they generate a nonzero exterior
field. The rule is therefore:

> A perturbation is in the null space of the exterior-potential map **only if every
> multipole moment vanishes**, and for a compact body that means the perturbation
> must be not merely mass-balanced but spherically symmetric — the shell-theorem
> case.

So "zero total mass" is *sufficient* for a null vector only together with spherical
symmetry. It is not sufficient on its own.

**(c) How the relative effect varies with height.** The measured ratios
$1.1319\times10^{-2} : 7.0306\times10^{-3} : 3.5714\times10^{-3}$ at
$z_0/R = 1.2, 2.0, 4.0$. From 2.0 to 4.0 the relative effect halves
(ratio $1.97$), and from 1.2 to 2.0 it falls by a factor 1.61 — consistent with a
$1/z_0$ dependence once the near-field departure is accounted for. That $1/z_0$
dependence is exactly the signature of a **dipole**: at leading order
$V_{\text{tot}}\propto M/z_0$ (monopole) while
$V_{\text{pert}}\propto p/z_0^2$ (dipole), so

$$\frac{V_{\text{pert}}}{V_{\text{tot}}} \propto \frac{p}{M z_0} \propto
\frac{1}{z_0} .$$

The lesson generalises to a diagnostic: **the rate at which a relative anomaly
decays with distance reveals the order of the dominant multipole**, and hence
whether the perturbation has a monopole, a dipole or only quadrupole and higher
content. A perturbation whose *first* nonzero moment is of order $n$ has a relative
effect falling as $z_0^{-n}$.

**(d) What the computation does and does not establish.**

*Establishes:* that for this geometry and these quadrature parameters, a
non-spherical zero-total-mass perturbation produces a measurable exterior signal;
that the signal falls off like a dipole's; and that the exact null space of the
exterior-potential map is much smaller than the set of mass-balanced
perturbations.

*Does not establish:* that *every* non-spherical mass-balanced perturbation is
detectable *in practice*. At a $1.1\times10^{-2}$ relative level, this particular
dipole would be lost in a survey with 5 % noise; and a perturbation whose lowest
nonzero moment were of high order would produce a signal decaying as
$z_0^{-n}$ and hence be negligible at the observation height. The correct
conclusion is the one the theory supplies: the *exact* null space is the
spherically symmetric mass-balanced perturbations, while the *effective* null
space in the presence of noise contains much more. Conflating the two is the error
criticised in ★★★10.

---

## ★★★10 — Two claims examined

**The governing equation and its data requirement.** Both claims concern a field
measured outside its sources, so the equation is Laplace's equation outside and
Poisson's inside: **elliptic**, requiring one boundary condition at every point of
the boundary of the region, with no characteristics and no propagation direction.
The theorems available are: uniqueness for the Dirichlet problem; the mean value
property and maximum principle; and analyticity of the exterior field.

**Claim (a): "the anomaly requires a body at 4 km depth".**

*Complete-and-noise-free requirement.* For the statement to be a theorem rather
than a preference, one would need the anomalous field on a **closed surface
enclosing the source**, at every point, exactly. Then uniqueness of the Dirichlet
problem determines the potential inside, hence $\nabla^2V$ inside, hence the source
density by Poisson's equation. Real data are a patch at the Earth's surface,
sampled on a grid, with noise; the null-space argument of ★★7 and ★★★9 then applies.

*Prior information silently used.* A statement of the form "requires a depth"
always contains at least one of: a maximum permissible density or magnetisation
contrast; a positivity constraint; a compact-support or depth-extent assumption;
a smoothness or minimum-structure preference (i.e. a regularisation); or a
geological constraint from other data. The word "requires" hides whichever of these
was imposed.

*Rewritten.* "Within the resolution of the data and with the density contrast
bounded by the measured core properties, the anomaly is consistent with a body at
4 km; equivalent bodies with the same anomaly exist between about 3 and 7 km, and
the shallower end is favoured by the minimum-structure model norm we used." That
sentence names the prior, quantifies the ambiguity interval, and discloses the
selection rule. It is longer and it is defensible.

**Claim (b): "the potential-field data rule out a body deeper than 8 km".**

*Complete-and-noise-free requirement.* Excluding a model requires showing that its
predicted anomaly is inconsistent with the data at the stated confidence level —
which requires a forward model, a noise model, and a statement of the parameter
range considered. In particular, "ruled out" for a deep body requires an *upper*
bound on the source property (density or magnetisation) and a *lower* bound on the
resolution at the relevant wavelength.

*Prior information silently used.* The upper bound on the source property does the
real work. A deeper body can always be made to fit by increasing its density or
magnetisation, unless that is bounded. Where does the bound come from? Usually from
petrophysics on samples or from a global statistical distribution — that is, from
data other than the potential field.

*Rewritten.* "For density contrasts up to $300\ \mathrm{kg\,m^{-3}}$ (the range
measured on core from the region), models deeper than 8 km predict an anomaly whose
amplitude falls below the noise by more than $3\sigma$; models between 8 and 12 km
are therefore excluded at that confidence, given the assumed contrast bound."
Again: the bound, the noise level, and the parameter range are explicit.

**The unifying point.** Both claims are about the same mathematics: the exterior
field determines the source **only** if the data are complete and exact, and real
data are neither. The correct response is not to abandon interpretation but to
publish the trade-off — the equivalence class, the prior, and the noise — so that a
reader can see which of the conclusions rests on data and which on assumption. As
[01-09-08](../08-weak-solutions.md) §7 shows, this is not a philosophical
reservation but the singular spectrum of the forward map written out in plain
language.
