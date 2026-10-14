# Solutions — 01-09-02 The Diffusion/Heat Equation and Diffusive Timescales

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. Where a
> numeric answer is given, it was computed rather than estimated by hand. Several
> problems have more than one defensible answer; where that is true it is stated
> explicitly, and where a conclusion depends on an assumed parameter the
> assumption is written out.
>
> **Conventions.** $\kappa$ is the diffusivity in $\mathrm{m^2\,s^{-1}}$;
> $\tau = L^2/\kappa$ is used as written throughout (not $\sqrt{\kappa t}$, not
> $4\kappa t$). One year is $3.156\times10^{7}$ s; one day is $86400$ s. Thermal
> conductivity is $k$ in $\mathrm{W\,m^{-1}K^{-1}}$; permeability is also
> conventionally written $k$ and is prefaced as *permeability* wherever it appears.

---

## ★1 — Thermal diffusivity of two materials

**(a) Granite.**

$$\rho c = 2650\times800 = 2.120\times10^{6}\ \mathrm{J\,m^{-3}K^{-1}}, \qquad
\kappa = \frac{2.5}{2.120\times10^{6}} = 1.179\times10^{-6}\ \mathrm{m^2\,s^{-1}} .$$

**(b) Water-saturated sand.**

$$\rho c = 2100\times1400 = 2.940\times10^{6}\ \mathrm{J\,m^{-3}K^{-1}}, \qquad
\kappa = \frac{1.8}{2.940\times10^{6}} = 6.12\times10^{-7}\ \mathrm{m^2\,s^{-1}} .$$

**Which transmits faster, and by how much.** The ratio is

$$\frac{\kappa_{\text{granite}}}{\kappa_{\text{sand}}}
= \frac{1.179\times10^{-6}}{6.12\times10^{-7}} = 1.93 .$$

Granite transmits a thermal disturbance about twice as fast, so a feature in
granite appears in about half the time, and the diffusive length
$\sqrt{4\kappa t}$ is about $\sqrt{1.93} = 1.4$ times larger at the same time.

**Sensitivity to $c$.** $\kappa$ is inversely proportional to $\rho c$, so a
20 % uncertainty in $c$ gives a 20 % uncertainty in $\kappa$ and hence about
$1/\sqrt{1.2} = 0.91$, i.e. a 9 % uncertainty in the diffusion length at a fixed
time (since $L \propto \sqrt{\kappa}$). The qualitative conclusion — granite faster
than wet sand — is unaffected, since the difference is a factor of two and the
uncertainties are tens of per cent. This contrast between a *linear* effect on
$\kappa$ and a *square-root* effect on lengths recurs constantly and is worth
remembering: distances are more robust than timescales.

**Two remarks.** Both values sit near $10^{-6}\ \mathrm{m^2\,s^{-1}}$ even though
conductivity differs by 40 %, because $\rho c$ moves in the opposite direction
(water has a large heat capacity per volume). And the values are *illustrative*:
porosity, saturation, mineralogy and temperature all move $\kappa$ by tens of per
cent, so any interpretation at the 10 % level must measure $\kappa$ locally.

---

## ★2 — Depth of penetration of a surface perturbation

Using $\tau = L^2/\kappa$ with $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$:

| $L$ | $\tau = L^2/\kappa$ (s) | In years |
|---|---|---|
| 50 m | $2.50\times10^{9}$ | $79.2$ |
| 500 m | $2.50\times10^{11}$ | $7.92\times10^{3}$ |
| 2 km | $4.00\times10^{12}$ | $1.267\times10^{5}$ |

**Which is relevant to what.** The 50 m figure (about 80 years) is the relevant
one for a **borehole palaeoclimate** study at the few-decades-to-century scale: a
50 m borehole records the last century or so, a 100 m hole a few centuries, and
the "depth of penetration" grows only as $\sqrt{t}$. The 500 m to 2 km figures
(thousands to hundreds of thousands of years) are the relevant ones for a
**lithospheric thermal model**, where the timescale must be compared with the age
of the lithosphere before a steady geotherm may be assumed.

**The convention matters and must be stated.** The choice $\tau = L^2/\kappa$ gives
values that are a quarter of those from the diffusion-length convention
$L = \sqrt{4\kappa t}$, and $1/\pi$ of those from $L = \sqrt{\pi\kappa t}$. With
$L = \sqrt{4\kappa t}$ the numbers above would be $19.8$ yr, $2.0$ kyr and
$31.7$ kyr. All three conventions appear in the literature; the practical rule is
to state which one is being used and to check the *scaling* rather than the
prefactor.

**Check on the second row.** 500 m in 7920 yr implies a mean "apparent speed" of
$500/7920 = 0.063$ m yr$^{-1} = 6.3$ cm yr$^{-1}$. That number is quoted in
palaeoclimate contexts, but it is not a speed: the corresponding value at 2 km is
$2000/126743 = 0.016$ m yr$^{-1}$, four times smaller, because $L \propto \sqrt{t}$.
Reporting the first without the second is a statement about the chosen depth, not
about the mechanism.

---

## ★3 — Verification of the mode solution

**Verification.** Let $u = \mathrm{e}^{-\lambda t}\sin(kx)$ with
$\lambda = \kappa k^2$ and $k = n\pi/L$. Then

$$u_t = -\lambda u, \qquad u_{xx} = -k^2u, \qquad
u_t - \kappa u_{xx} = -\lambda u + \kappa k^2u = 0 ,$$

so the equation is satisfied for any $n$ provided $\lambda = \kappa k^2$. The
boundary conditions hold because $\sin(0) = \sin(n\pi) = 0$ for integer $n$. Note
that the computation establishes the *rate* as well as the solution: the
eigenvalue is not assumed but forced by the substitution.

**The $n=1$ mode with $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and $L = 1$ km.**

$$\lambda_1 = \frac{\kappa\pi^2}{L^2}
= \frac{10^{-6}\times9.8696}{10^{6}} = 9.8696\times10^{-12}\ \mathrm{s^{-1}} ,$$

$$t_{1/2} = \frac{\ln 2}{\lambda_1}
= \frac{0.6931}{9.8696\times10^{-12}} = 7.02\times10^{10}\ \mathrm{s}
= 2225\ \mathrm{yr} .$$

**What the half-life is and is not.** It is the time for the *amplitude of the
fundamental mode* to fall by half, and it corresponds to a diffusive timescale of
$L^2/(\kappa\pi^2) = 1.01\times10^{11}$ s. It is not the time for a thermal
front to cross the interval; there is no front, and the higher modes decay at
$n^2$ times the rate, so the profile after one half-life is the fundamental plus a
negligible residue. In a real stratified sequence with a contrasting conductivity
layer, the eigenvalue must be found by solving a transcendental equation rather
than read off, as [01-09-05](../05-separation-of-variables.md) §7.1 describes.

---

## ★4 — Deriving the skin depth

**Step 1 — separate real and imaginary parts.** Put $k = \alpha + \mathrm{i}\beta$
with $\alpha,\beta$ real. Then

$$k^2 = \alpha^2 - \beta^2 + 2\mathrm{i}\alpha\beta
= \mathrm{i}\omega\mu\sigma .$$

Equating real and imaginary parts:

$$\alpha^2 - \beta^2 = 0, \qquad 2\alpha\beta = \omega\mu\sigma .$$

**Step 2 — solve.** The first equation gives $\alpha = \pm\beta$; taking the root
with $\beta > 0$ (a wave decaying in the $+z$ direction) and using the second,

$$\beta^2 = \frac{\omega\mu\sigma}{2}
\qquad\Longrightarrow\qquad
\beta = \sqrt{\frac{\omega\mu\sigma}{2}} , \qquad \alpha = \beta .$$

**Step 3 — identify the skin depth.** With $\mathrm{e}^{\mathrm{i}(kz-\omega t)}$
and $k = \alpha + \mathrm{i}\beta$, the field carries the factor
$\mathrm{e}^{\mathrm{i}\alpha z}\mathrm{e}^{-\beta z}$: a wave of wavelength
$2\pi/\alpha$ decaying with an $1/e$ distance

$$\delta = \frac{1}{\beta} = \sqrt{\frac{2}{\omega\mu\sigma}} .$$

**Step 4 — the claimed identity.** Since $\omega = 2\pi f$,

$$\mu\sigma\delta^2 = \mu\sigma\cdot\frac{2}{\omega\mu\sigma}
= \frac{2}{\omega} = \frac{1}{\pi f} ,$$

so the diffusion time across one skin depth is exactly $1/(\pi f)$, one radian of
the driving period. The module's demonstration verifies this for every entry of
its parameter table ($0.318$ s at 1 Hz, $3.18\times10^{-4}$ s at 1 kHz).

**Step 5 — the assumption.** The derivation began from
$\nabla^2\mathbf{E} = \mu\sigma\,\partial_t\mathbf{E}$, which drops the
displacement-current term $\mu\epsilon\,\partial_t^2\mathbf{E}$. That step is
legitimate exactly when the conduction current dominates the displacement current,
i.e. $\sigma \gg \omega\epsilon$. Where $\sigma \lesssim \omega\epsilon$ the full
Maxwell equation must be used and the field propagates rather than diffuses — the
case examined in ★★6 of [01-09-01](../exercises/01-classification-exercises.md).
The parabolic model is therefore not a different physics but a *regime*
approximation, and quoting a skin depth outside that regime is a common and
avoidable error.

---

## ★★5 — Aquifer response

**(a) Diffusivity.**

$$D = \frac{T}{S} = \frac{0.02}{2\times10^{-4}} = 100\ \mathrm{m^2\,s^{-1}} .$$

**(b) Time to 20 km**, using the convention $\tau = L^2/D$ stated at the head of
this set:

$$\tau = \frac{(2\times10^{4})^2}{100} = 4.0\times10^{6}\ \mathrm{s}
= 46.3\ \mathrm{d} .$$

For comparison, the diffusion-length convention would give
$L = \sqrt{4Dt} = \sqrt{1.6\times10^{9}} = 4.0\times10^{4}$ m at that time — twice
the nominal $L$, as the convention dictates. The two conventions differ by a
factor of four in *time*, which is why the convention must be stated.

**(c) Why this is an order-of-magnitude statement.** Two reasons, both structural:

- **$D$ is not measured, it is inferred from two other inferred numbers.** $T$ and
  $S$ come from a pumping test whose interpretation assumes homogeneity, a
  particular geometry and a particular model (Theis or leaky); an aquifer that is
  layered, bounded by a leaky confining layer, or fractured will give $T$ and $S$
  that represent a volume rather than a local property. The product $D$ inherits
  the ambiguity of both, and the ratio $T/S$ is notoriously poorly constrained in
  short tests because the drawdown is insensitive to $S$ at early times.
- **The prediction of "observable" hides a detection threshold.** A pressure
  change of $10^{-3}$ m and one of $10^{-1}$ m are both "pressure changes"; the
  distance reached differs, and the radial solution's amplitude decays like
  $1/r$ while the exponent contains $r^2/4Dt$. The time to reach 20 km is a
  timescale, not a detection time.

A defensible sentence states the model, the parameters with their uncertainties,
and the detection threshold. "With $T = 0.02\ \mathrm{m^2\,s^{-1}}$ and
$S = 2\times10^{-4}$ assumed homogeneous, the pressure perturbation at 20 km is
of order the one-day pumping amplitude after about 46 days" is defensible;
"the aquifer responds in 46 days" is not.

---

## ★6 — Cooling of a dyke, and why the factor is modest

**(a) The nominal timescale.**

$$\frac{b^2}{\kappa} = \frac{(500)^2}{10^{-6}} = 2.5\times10^{11}\ \mathrm{s}
= 7922\ \mathrm{yr} .$$

**(b) The slowest mode of a slab.** For a slab of thickness $b$ with both faces
held at a fixed temperature, the eigenfunctions are $\sin(n\pi z/b)$ and the decay
rates are $\kappa n^2\pi^2/b^2$. The slowest is

$$\lambda_1 = \frac{\kappa\pi^2}{b^2}, \qquad
t_1 = \frac{1}{\lambda_1} = \frac{b^2}{\kappa\pi^2}
= \frac{2.5\times10^{11}}{9.8696} = 2.53\times10^{10}\ \mathrm{s}
= 803\ \mathrm{yr} .$$

**(c) Why the two differ only by $\pi^2$.** Both expressions describe the same
diffusive process and are built from the same two quantities, $b$ and $\kappa$.
They differ by the eigenvalue of the problem, which for a slab with fixed faces is
$\pi^2$ — a factor of $9.87$. This is the practical content of the scaling
statement $\tau \sim L^2/\kappa$: **the order-one constants depend on geometry and
boundary conditions and must be computed, not guessed, when a number is being
quoted.** Scaling arguments are for comparisons; published timescales need the
eigenvalue.

**Two refinements that change the answer by more than the constants.** A dyke
cooling into its host does not have fixed face temperatures (the host heats up,
so a Robin or interface condition is appropriate, which *slows* the cooling); and
latent heat release during solidification adds an effective heat capacity, which
also slows it. Both should be mentioned before a cooling time is compared with,
say, an age constraint.

---

## ★★7 — Pore-pressure front migration

**(a) Distances**, using the diffusion length $\ell = \sqrt{4Dt}$ with
$D = 0.5\ \mathrm{m^2\,s^{-1}}$:

| Time | Seconds | $\ell = \sqrt{4Dt}$ |
|---|---|---|
| 30 d | $2.592\times10^{6}$ | $2.28\times10^{3}$ m (2.3 km) |
| 365 d | $3.156\times10^{7}$ | $7.94\times10^{3}$ m (7.9 km) |

**(b) Ratio of distances versus ratio of times.**

$$\frac{\ell_{365}}{\ell_{30}} = 3.49, \qquad
\frac{t_{365}}{t_{30}} = 12.17, \qquad
\sqrt{12.17} = 3.49 .$$

**(c) Why they differ.** Diffusion has no speed: the length reached grows as
$\sqrt{t}$, so a twelvefold increase in time gives only a 3.5-fold increase in
distance. Equivalently, the *apparent* front speed $\ell/t$ falls as
$t^{-1/2}$ — it is $0.076$ m s$^{-1}$ over 30 days and $0.025$ m s$^{-1}$ over a
year, a factor of three different for the same rock.

The two ratios would be equal only if the front advanced at a constant speed —
that is, if the governing equation were hyperbolic rather than parabolic. So a
measured set of arrival times that *does* scale linearly with distance is direct
evidence against a purely diffusive mechanism, and is one of the diagnostics used
in the induced-seismicity literature to argue for fluid flow along a permeable
conduit rather than pressure diffusion through a porous matrix. The test is
practical, not academic: it distinguishes mechanisms rather than merely fitting
them.

**A caution on measuring a front.** The quantity $\ell$ above is the diffusion
length of the *amplitude* profile, not the edge of a compact region; the pressure
perturbation is nonzero everywhere, and a "front" is defined by a detection
threshold. Since the amplitude falls with distance and time, the apparent front
position depends on the threshold, which is a further reason the ratio test in (b)
should be applied to amplitudes at fixed threshold rather than to a nominal
leading edge.

---

## ★8 — The fundamental solution and its normalisation

**The integral.** Substitute $s = x/\sqrt{4\kappa t}$, so
$dx = \sqrt{4\kappa t}\,ds$:

$$\int_{-\infty}^{\infty}\Phi\,dx
= \frac{1}{\sqrt{4\pi\kappa t}}\int_{-\infty}^{\infty}
\mathrm{e}^{-x^2/(4\kappa t)}dx
= \frac{1}{\sqrt{4\pi\kappa t}}\cdot\sqrt{4\pi\kappa t}
= 1 ,$$

using $\int_{-\infty}^{\infty}\mathrm{e}^{-s^2}ds = \sqrt{\pi}$. The result is
independent of $t$: the total is conserved as the solution spreads.

**Physical meaning.** $\Phi$ is the solution for a unit amount of heat released at
a point, so the conserved integral is conservation of thermal energy. Its
conservation also makes $\Phi$ the Green's function: the solution for an arbitrary
initial condition is $u = \int\Phi(x-y,t)u_0(y)\,dy$, and the conservation
statement is then the statement that the spatial average of a solution with
periodic or insulated boundaries does not change. A source term would change mass,
and is handled by Duhamel's principle
([01-09-07](../07-boundary-value-problems.md) §5).

**What the derivation requires at infinity.** Convergence of the integral needs
$\Phi\to0$ fast enough as $\lvert x\rvert\to\infty$, which holds for every $t>0$
because the Gaussian decays faster than any polynomial. There is no boundary
condition at finite distance: the problem is posed on the whole line. On a bounded
domain the integral is *not* conserved unless the boundary conditions permit no
flux (insulated ends, or periodic). This is not a subtlety — it is the mechanism
behind a bug found while producing this module's demonstration, where a
measurement of $d\langle x^2\rangle/dt = 1.939$ instead of the exact $2\kappa = 2$
was traced entirely to 3 % of the mass leaking through a boundary placed too close
to the spreading pulse. Re-running the same experiment on a domain three times
wider gave $2.000000$, i.e. agreement to six decimal places. **Before believing any
measured scaling, check that the boundary is not participating in it.**

---

## ★★★9 — Convergence for discontinuous initial data

**Setup.** Write $u = (1-x) + w$. Then $w$ satisfies $w_t = \kappa w_{xx}$ with
$w(0,t) = w(1,t) = 0$ and

$$w(x,0) = u(x,0) - (1-x) =
\begin{cases} x, & x < 0.5,\\ x-1, & x > 0.5,\end{cases}$$

a sawtooth (odd about $x = \tfrac12$), whose Fourier sine coefficients are
computed by quadrature. Only even $n$ contribute; the computed values are
$b_1 = 0$, $b_2 = 0.318310 = 1/\pi$, $b_3 = 0$, $b_4 = -0.159155 = -1/(2\pi)$,
$b_6 = +0.106103 = 1/(3\pi)$. The exact solution is
$u = (1-x) + \sum_n b_n\sin(n\pi x)\mathrm{e}^{-n^2\pi^2t}$, truncated at
$n = 60$ (the truncation is below $10^{-15}$ for the times used).

**Measured orders** in the maximum norm, explicit scheme with
$\kappa\Delta t/\Delta x^2 = 0.4$:

| $t$ | $N = 50$ | 100 | 200 | 400 | order sequence |
|---|---|---|---|---|---|
| $10^{-2}$ | $4.233\times10^{-4}$ | $1.113\times10^{-4}$ | $2.829\times10^{-5}$ | $7.117\times10^{-6}$ | 1.93, 1.98, 1.99 |
| $10^{-3}$ | $3.554\times10^{-3}$ | $1.074\times10^{-3}$ | $2.774\times10^{-4}$ | $7.087\times10^{-5}$ | 1.73, 1.95, 1.97 |
| $10^{-4}$ | $1.878\times10^{-2}$ | $9.502\times10^{-3}$ | $2.220\times10^{-3}$ | $6.779\times10^{-4}$ | 0.98, 2.10, 1.71 |

**Reading the table.** At $t = 10^{-2}$ the order is a clean 2. At $t = 10^{-3}$ it
is 1.73 on the coarsest pair and 1.97 on the finest. At $t = 10^{-4}$ the sequence
0.98, 2.10, 1.71 is **erratic**, not merely low: the order has no stable value on
the grids used.

**The controlling quantity.** The initial data are smoothed over a layer whose
thickness is set by the diffusion length

$$\ell(t) = \sqrt{4\kappa t} ,$$

and what matters is how many **cells** that layer occupies,
$\ell/\Delta x = \sqrt{4\kappa t}/\Delta x$:

| $t$ | $N=50$ | 100 | 200 | 400 | order observed |
|---|---|---|---|---|---|
| $10^{-2}$ | 10.2 | 20.2 | 40.2 | 80.2 | stable 2 |
| $10^{-3}$ | 3.2 | 6.4 | 12.7 | 25.4 | nearly 2 |
| $10^{-4}$ | 1.0 | 2.0 | 4.0 | 8.0 | erratic |

The degradation begins when the layer occupies only a few cells. At $t = 10^{-4}$
the coarsest grid has one cell per layer: the initial condition is represented by
a single node and the solution in that first cell is essentially unrepresented, so
the error is dominated by the initial layer and does not respond to refinement in a
regular way. On the finer grids the layer is resolved (4 and 8 cells) and the order
returns towards 2, but the sequence is not monotone because the coarse-grid error
is not yet in the asymptotic regime.

**The physical explanation.** The operator *does* smooth instantly — the exact
solution is analytic for every $t>0$, and the series above confirms it, with the
high modes attenuated as $\mathrm{e}^{-n^2\pi^2t}$. What the grid must still
resolve is the **spatial width of the initially smoothed layer**, and that width
is $\sqrt{4\kappa t}$: a smooth function with a small feature, not a discontinuity.
It is therefore the same resolution requirement as for any sharp feature, with the
"sharpness" set by the elapsed time rather than by the data. Two consequences:

- comparing a numerical solution with an exact one at very short times is a test
  of the *initial-layer resolution*, not of the scheme's asymptotic order, and a
  low or erratic order there is not evidence of a bug;
- the resolution demand is *relaxed* by waiting: a run to $t = 10^{-2}$ needs 10
  cells for the layer, whereas the same physical profile at $t = 10^{-4}$ needs the
  same 10 cells at a grid four times finer.

**Limits of this conclusion.** The numbers are for one equation, one initial
condition and one scheme family, and for a *cell-centred* grid on which the initial
step is represented exactly at the nodes (so no error is contributed by the
sampling itself). A point source, a discontinuous coefficient, or a discontinuity
misaligned with the grid will show *persistent* sub-optimal order rather than
merely a short-time transient, and would need its own investigation.

---

## ★★★10 — Critique of a diffusivity inference

**The sentence to be examined.**

> "The 5 km migration of seismicity in 12 months implies a hydraulic diffusivity
> of $0.7\ \mathrm{m^2\,s^{-1}}$, hence a permeability of about
> $10^{-9}\ \mathrm{m^2}$, consistent with a fractured reservoir."

**Step 1 — the arithmetic the sentence performs.** From $\tau = L^2/D$ with
$L = 5\times10^{3}$ m and $\tau = 1$ yr $= 3.156\times10^{7}$ s,

$$D = \frac{L^2}{\tau} = \frac{2.5\times10^{7}}{3.156\times10^{7}}
= 0.792\ \mathrm{m^2\,s^{-1}} ,$$

which the sentence rounds to $0.7$. Then, from $D = k_{\text{perm}}/(\mu S_s)$ with
$k_{\text{perm}} = 10^{-9}\ \mathrm{m^2}$ and $\mu = 10^{-3}\ \mathrm{Pa\,s}$,

$$S_s = \frac{k_{\text{perm}}}{\mu D} = \frac{10^{-9}}{10^{-3}\times0.792}
= 1.26\times10^{-6}\ \mathrm{m^{-1}} .$$

*(Using the paper's own rounded $D = 0.7$ gives $1.43\times10^{-6}\ \mathrm{m^{-1}}$;
both are quoted below so that the rounding is visible.)*

**Step 2 — the assumptions, separated by kind.**

*Physics.*

1. Pore-pressure diffusion is the triggering mechanism (not poroelastic stress
   transfer, aseismic slip, or dynamic stress changes).
2. The front's position is well defined and is identified with the diffusion
   length, i.e. a detection-threshold effect is ignored.
3. The medium is homogeneous and isotropic in $D$ over the 5 km scale, so a single
   diffusivity exists.
4. The initial condition is a point (or line) source at the injection well, so
   $L^2/D$ is the right scaling (a distributed source has a different effective
   origin).
5. The triggering front's time is the event time, not an earlier nucleation time.

*Numbers.*

6. The event really lies 5 km from the injection point (location uncertainty is
   often hundreds of metres, and a 20 % distance error is a 44 % error in $D$ since
   $D \propto L^2$).
7. $\tau$ is 12 months, not "within 12 months" (a 6-month delay halves $D$).
8. $\mu = 10^{-3}\ \mathrm{Pa\,s}$ and, critically, that $S_s$ is whatever the
   inference needs it to be rather than what the rock is.

**Step 3 — is the quoted permeability realistic?** Here the sentence has a real
problem of magnitude. A permeability of $10^{-9}\ \mathrm{m^2}$ is

$$10^{-9}\ \mathrm{m^2} \div 9.869\times10^{-13}\ \mathrm{m^2\,D^{-1}}
\approx 1.0\times10^{3}\ \mathrm{D} \ (\text{about 1000 darcy}),$$

which is characteristic of unconsolidated gravel or a very open fracture, not of
"a fractured reservoir" in the ordinary sense. Conversely, if the permeability were
taken as $10^{-15}\ \mathrm{m^2}$ (about 1 mD, a plausible matrix value), the
inference would require

$$S_s = \frac{10^{-15}}{10^{-3}\times0.792} = 1.3\times10^{-12}\ \mathrm{m^{-1}} ,$$

six orders of magnitude below any defensible value for rock (a compressibility
estimate, $\rho_wg(\alpha + n\beta)$ with $\alpha \sim 10^{-10}\ \mathrm{Pa^{-1}}$
and $n = 0.01$, gives $S_s \approx 1.0\times10^{-6}\ \mathrm{m^{-1}}$). No
combination of ordinary parameters gives a permeability near $1\ \mathrm{mD}$ with
$D = 0.79\ \mathrm{m^2\,s^{-1}}$: the required $D$ is simply too high.

**The storage the inference implies, and whether it is realistic.** With
$k_{\text{perm}} = 10^{-9}\ \mathrm{m^2}$ and $D = 0.79$ (or 0.7) the implied
storage is $1.26\times10^{-6}$ (or $1.43\times10^{-6}$) $\mathrm{m^{-1}}$, which
*is* the right order for stiff rock from the compressibility estimate of
[01-09-02](../02-heat-equation.md) §4.2. So the sentence is self-consistent in the
storage, and anomalous in the permeability. Stating only one of the two hides the
tension — and $D$ is a *ratio*, so a single number can never determine both members
of the pair.

**Step 4 — one independent test.** Measure the storage directly, and the ambiguity
collapses: $S_s$ can be constrained by a well test (which measures $S$ from the
late-time response), by tidal or barometric efficiency (which measures it without
pumping), or by laboratory compressibility on core with a porosity log. Given an
independent $S_s \approx 10^{-6}\ \mathrm{m^{-1}}$, the inferred permeability is
$\sim 8\times10^{-10}\ \mathrm{m^2}$ (about 800 D) — which either stands as an
extreme claim that can be checked against injection tests, or falsifies the pure
diffusion model. Either outcome is informative, which is what an independent test
is for.

**Step 5 — a defensible rewrite.**

> "Seismicity migrated about 5 km in 12 months, which is consistent with a
> pressure-diffusion front with $D \approx 0.8\ \mathrm{m^2\,s^{-1}}$ under the
> assumptions of a homogeneous medium and a point source. If the specific storage
> is the $10^{-6}\ \mathrm{m^{-1}}$ typical of stiff rock, this implies an
> effective permeability of order $10^{-9}\ \mathrm{m^2}$ — several hundred darcy,
> high enough that it is more plausibly attributed to channelled flow along a
> fault-damaged zone than to a bulk rock property. Independent constraints on
> $S_s$ and on the permeability from well tests would test the interpretation; in
> their absence we note that the requirement $D = L^2/\tau$ alone does not
> determine either quantity."

That version states the model, the parameters, the direction of the tension, and
what would settle it. The original sentence, by contrast, converts an assumption
into a measurement in one step.

**What the critique is not saying.** It is not claiming that the migration is not
diffusive, nor that the reservoir is not fractured. The measurement of a
$\sqrt{t}$-type migration is genuine evidence; the objection is to presenting the
*consistency* of one assumed parameter pair as a measurement of its members.
