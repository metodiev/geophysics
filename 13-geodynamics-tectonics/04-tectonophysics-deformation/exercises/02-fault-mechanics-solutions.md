# Solutions — 13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Fault Mechanics, Coulomb Stress and Stress Transfer](../02-fault-mechanics.md).

---

## ★1 — Resolved stresses and the nearest plane to failure

With $\sigma_1 = 150$, $\sigma_3 = 50\ \mathrm{MPa}$: mean $= 100\ \mathrm{MPa}$,
$\Delta\sigma/2 = 50\ \mathrm{MPa}$. The angle $\theta$ is measured from the
fault **normal** to $\sigma_1$, and the failure function to maximise is
$\lvert\tau\rvert - \mu(\sigma_n-p)$.

| $\theta$ | $2\theta$ | $\sigma_n$ (MPa) | $\lvert\tau\rvert$ (MPa) | CFF $= \lvert\tau\rvert - \mu\sigma_n$ (MPa) |
|---|---|---|---|---|
| $20^\circ$ | $40^\circ$ | $100+50\cos 40^\circ = 138.30$ | $50\sin 40^\circ = 32.14$ | $32.14 - 103.72 = -71.58$ |
| $30^\circ$ | $60^\circ$ | $100+50(0.5) = 125.00$ | $50(0.8660) = 43.30$ | $43.30 - 93.75 = -50.45$ |
| $45^\circ$ | $90^\circ$ | $100.00$ | $50.00$ | $50.00 - 75.00 = -25.00$ |

All three are negative, so none fails at this stress state, and among the three
the **$45^\circ$ plane is nearest failure**.

The global optimum is not among them. It lies at
$\theta_{\text{opt}} = 45+\phi/2 = 63.435^\circ$ (normal angle), where
$\sigma_n = 100+50\cos 126.87^\circ = 70.00\ \mathrm{MPa}$,
$\lvert\tau\rvert = 50\sin 126.87^\circ = 40.00\ \mathrm{MPa}$ and
$\mathrm{CFF} = 40.00 - 52.50 = -12.50\ \mathrm{MPa}$.

**Why the optimum is not where the shear is largest.** At $\theta = 45^\circ$ the
shear is maximal but so is the normal stress; moving toward $\theta = 63.4^\circ$
gives up $10\ \mathrm{MPa}$ of shear and gains $22.5\ \mathrm{MPa}$ of reduced
clamping, a net improvement of $12.5\ \mathrm{MPa}$. This trade is the physical
content of the Coulomb criterion, and it is why the optimum angle depends on
$\mu$ while the maximum-shear angle does not.

**Convention warning.** If $\theta$ is instead measured from the fault plane
(rather than its normal), every angle above is replaced by its complement and the
optimum reads $26.565^\circ = 45^\circ-\phi/2$. Both conventions appear in the
literature; state which you are using.

---

## ★2 — Friction angles and optimal angles

$\mu = 0.6$: $\phi = \arctan 0.6 = 30.96^\circ$, so
$\theta_{\text{opt}} = 45 - 15.48 = 29.52^\circ$.
$\mu = 0.85$: $\phi = \arctan 0.85 = 40.36^\circ$, so
$\theta_{\text{opt}} = 45 - 20.18 = 24.82^\circ$.

Stronger friction gives a *shallower* optimal angle — counter-intuitive until one
notices that a stronger material needs a lower shear-to-normal ratio, so it
fails on a plane nearer the $\sigma_1$ direction where the normal stress is
higher and the shear lower.

---

## ★3 — Failure differential stress at $8\ \mathrm{km}$

$$
\sigma_v = \rho g z = 2800\ \mathrm{kg\,m^{-3}} \times 9.81\ \mathrm{m\,s^{-2}}
\times 8000\ \mathrm{m} = 2.197\times10^{8}\ \mathrm{Pa} = 219.7\ \mathrm{MPa}.
$$

$\sin\phi = \sin 36.87^\circ = 0.6$, and the identity
$2\mu/(\cos\phi+\mu\sin\phi) = 2\sin\phi = 1.2$:

$$
\Delta\sigma = 1.2 \times 219.7 \times (1-0.4) = 158.2\ \mathrm{MPa}.
$$

Units: $[\Delta\sigma] = [\text{dimensionless}][\mathrm{kg\,m^{-3}}]
[\mathrm{m\,s^{-2}}][\mathrm{m}] = \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$. ✔

---

## ★4 — Surface shear stress versus distance

With $s = 1\ \mathrm{m}$, $d = 10\ \mathrm{km}$, $\mu_e = 30\ \mathrm{GPa}$,

$$
\sigma_{xy}(x, 0) = \frac{2\mu_e s}{\pi}\frac{d}{d^{2}+x^{2}} .
$$

At $x = 0$: $\dfrac{2\times3\times10^{10}}{\pi}\times\dfrac{10^{4}}
{(10^{4})^{2}} = 1.910\times10^{10}\times10^{-4} = 1.910\times10^{6}\
\mathrm{Pa} = 1.910\ \mathrm{MPa}$.

At $x = 5\ \mathrm{km}$:
$1.910\times10^{10}\times\dfrac{10^{4}}{1.25\times10^{8}}
= 1.910\times10^{10}\times8.0\times10^{-5} = 1.528\times10^{6}\ \mathrm{Pa}$.

At $x = 20\ \mathrm{km}$:
$1.910\times10^{10}\times\dfrac{10^{4}}{5\times10^{8}} = 3.820\times10^{5}\
\mathrm{Pa}$; asymptote $2\mu_e s d/(\pi x^{2}) = 1.910\times10^{10}\times
10^{4}/(4\times10^{8}) = 4.775\times10^{5}\ \mathrm{Pa}$. Ratio $0.800$ —
$20\%$ low.

At $x = 100\ \mathrm{km}$: exact $= 1.910\times10^{10}\times10^{4}/
(1.01\times10^{10}) = 1.891\times10^{4}\ \mathrm{Pa}$; asymptote
$= 1.910\times10^{10}\times10^{4}/10^{10} = 1.910\times10^{4}\ \mathrm{Pa}$.
Ratio $0.990$ — $1\%$ low.

**Answer to the question as posed:** only at $100\ \mathrm{km}$ is the
asymptote good to better than $5\%$; at $20\ \mathrm{km}$ the finite-$d$
correction is still $20\%$. The asymptotic form requires $x \gg d$, and
$20\ \mathrm{km}$ is only twice $d$.

---

## ★5 — Four receiver strikes at $(20, 4)\ \mathrm{km}$

First compute the stress change there:
$\sigma_{xy} = \frac{\mu_e s}{\pi}\left[\frac{z+d}{(z+d)^{2}+x^{2}}
- \frac{z-d}{(z-d)^{2}+x^{2}}\right]$ with all lengths in metres,
$s = 1\ \mathrm{m}$, $d = 10^{4}\ \mathrm{m}$, $x = 2\times10^{4}$,
$z = 4\times10^{3}$:

- $(z+d) = 1.4\times10^{4}$; $(z+d)^{2}+x^{2} = 1.96\times10^{8}+4\times10^{8}
  = 5.96\times10^{8}$; first term $= 2.349\times10^{-5}$.
- $(z-d) = -6\times10^{3}$; $(z-d)^{2}+x^{2} = 3.6\times10^{7}+4\times10^{8}
  = 4.36\times10^{8}$; second term $= -1.376\times10^{-5}$.
- Difference $= 3.725\times10^{-5}\ \mathrm{m^{-1}}$;
  $\sigma_{xy} = 9.549\times10^{9}\times3.725\times10^{-5}
  = 3.557\times10^{5}\ \mathrm{Pa} = 0.3557\ \mathrm{MPa}$.

Then $\Delta\mathrm{CFS} = \sigma_{xy}(\cos 2\phi + \mu\sin 2\phi)$:

| $\phi$ | $2\phi$ | $\cos 2\phi + 0.75\sin 2\phi$ | $\Delta\mathrm{CFS}$ (MPa) |
|---|---|---|---|
| $0^\circ$ | $0^\circ$ | $1.00$ | $+0.356$ |
| $18.4^\circ$ | $36.8^\circ$ | $0.800 + 0.75(0.600) = 1.250$ | $+0.445$ |
| $45^\circ$ | $90^\circ$ | $0 + 0.75 = 0.750$ | $+0.267$ |
| $90^\circ$ | $180^\circ$ | $-1.00$ | $-0.356$ |

Promoted: $0^\circ$, $18.4^\circ$ and $45^\circ$, most strongly at $18.4^\circ$
(consistent with $\phi_{\text{opt}} = \tfrac12\arctan 0.75 = 18.43^\circ$).
Inhibited: $90^\circ$, by the same magnitude as the parallel case.

---

## ★6 — Resolving a stress change onto a vertical plane

Only $\sigma_{xy} = \sigma_{yx} \ne 0$. For a vertical plane with normal
$n = (\cos\phi, \sin\phi, 0)$:

$$
\Delta\sigma_n = n_i \Delta\sigma_{ij} n_j = 2\sigma_{xy}n_x n_y
= 2\sigma_{xy}\cos\phi\sin\phi = \sigma_{xy}\sin 2\phi . ✔
$$

For the strike direction $\hat s = (-\sin\phi, \cos\phi, 0)$:

$$
\Delta\tau = \hat s_i \Delta\sigma_{ij} n_j
= \sigma_{xy}(\hat s_x n_y + \hat s_y n_x)
= \sigma_{xy}(-\sin^{2}\phi + \cos^{2}\phi) = \sigma_{xy}\cos 2\phi . ✔
$$

Under $\phi \to \phi + 90^\circ$: $\cos 2\phi \to -\cos 2\phi$ and
$\sin 2\phi \to -\sin 2\phi$, so
$\Delta\mathrm{CFS} \to -\Delta\mathrm{CFS}$. **Interpretation:** a fault plane
and the plane at right angles to it have opposite normal vectors, so the
resolved stresses change sign; promoting one mechanism inhibits its conjugate.

---

## ★7 — What fraction of the half-space is promoted?

The sign of $\sigma_{xy}$ on the vertical plane at distance $x$ (equivalently the
sign of the integrand) changes at $z = \sqrt{x^{2}+d^{2}}$. For each $x$, the
promoted interval is $0 < z < \sqrt{x^{2}+d^{2}}$, so the promoted fraction of
the region $\{0 < z < H\}$, $-\infty < x < \infty$ is

$$
f(H) = \frac{\displaystyle\int_0^{H}\sqrt{x^{2}+d^{2}}\,\mathrm dx}
{\displaystyle H\int_0^{H}\mathrm dx} \times \frac{1}{2},
$$

where the factor $1/2$ accounts for the symmetry $x \to -x$ and the integral
runs over half the axis. For $H \gg d$, use
$\sqrt{x^{2}+d^{2}} \approx x$:

$$
f \approx \frac{\int_0^{H}x\,\mathrm dx}{H\cdot H}\cdot\frac{1}{2}
= \frac{H^{2}/2}{H^{2}}\cdot\frac{1}{2} = \frac{1}{4} .
$$

So in an infinite domain, **one quarter** of the area is promoted and three
quarters shadowed on the fault-parallel mechanism. The demonstration's $82.8\%$
is much larger because its grid stops at $30\ \mathrm{km}$ depth — comparable to
$d = 12\ \mathrm{km}$ — so most of the sampled area lies inside the promoted lobe
$z < \sqrt{x^{2}+d^{2}}$. As the sampled depth grows, the fraction must fall
toward $25\%$, and that is the correct prediction to check.

---

## ★8 — Does a $1.31\ \mathrm{MPa}$ change predict failure?

No. The fault was $2\ \mathrm{MPa}$ from failure and the stress change is
$1.31\ \mathrm{MPa}$, so the calculation leaves it $0.69\ \mathrm{MPa}$ short
*within the model* — and that statement is itself conditional on a stress state
that is not known to $0.69\ \mathrm{MPa}$.

To turn it into a probability one needs (i) the background stressing rate, so the
residual $0.69\ \mathrm{MPa}$ can be converted into a time; (ii) a failure
criterion that is stochastic rather than deterministic — a rate-and-state
nucleation model with a distribution of fault strengths — so that "close to
failure" maps onto a probability; and (iii) an uncertainty on $\Delta
\mathrm{CFS}$ itself, which for a real event is dominated by the unknown slip
distribution and the neglected pore-pressure change.

---

## ★9 — The 3-D correction to the parallel-fault normal stress

In the far field, a point-source strike-slip earthquake is a double couple with
moment tensor $M_{ij} = M_0(\hat s_i n_j + \hat s_j n_i)$. The static stress
change at a receiver is

$$
\Delta\sigma_{ij} = \frac{3M_0}{4\pi r^{3}}\left[(\hat s \cdot \hat r)(n \cdot \hat r)
+ \ldots\right]
$$

with the full radiation pattern; the components that matter here are those not
present in the 2-D model: $\Delta\sigma_{xx}$, $\Delta\sigma_{yy}$,
$\Delta\sigma_{zz}$ and $\Delta\sigma_{xz}$ are all non-zero in 3-D.

For a **parallel vertical plane** (normal $\hat x$), the normal-stress change is
$\Delta\sigma_{xx}$. In the far field this is
$\Delta\sigma_{xx} \propto (\ldots)$ with the sign depending on azimuth relative
to the fault: it is compressional in the quadrants where the P-wave first motion
is away from the source, dilatational where it is toward. Therefore the correct
statement is: **parallel faults are promoted in the compressional quadrants and
inhibited in the dilatational ones, through the normal-stress term**, and the
2-D result $\Delta\sigma_n = 0$ is an artefact.

**Sign near the fault ends.** At the ends of the slip patch the stress change
rotates: $\Delta\sigma_{xx}$ is extensional in the "shadow" beyond the fault tip
and compressional beside the slipped zone. That is why the 3-D maps show four
lobes for the normal-stress change superposed on the shear-stress pattern, and
why the 2-D model's $\Delta\mathrm{CFS}$ (which has only the shear lobes)
systematically under-predicts the extent of the promoted region near the fault
ends.

---

## ★10 — Testing the aftershock correlation (specification)

**Synthetic catalogue generation.** (i) Draw a main-shock slip distribution from
a prescribed random field (e.g. a von Kármán spectrum) with a stated mean slip
and correlation length; (ii) compute $\Delta\mathrm{CFS}$ on a grid of receiver
mechanisms with a stated $\mu$; (iii) generate aftershocks as a Poisson process
whose rate density is
$\lambda(x) \propto \exp[\Delta\mathrm{CFS}(x)/\sigma_a]$ with a stated
activation parameter $\sigma_a$, plus a spatially uniform background of the same
total rate. This gives a catalogue with a **known** coupling between
$\Delta\mathrm{CFS}$ and rate.

**Noise model.** Location errors of $1$–$3\ \mathrm{km}$ (a Gaussian error added
to each hypocentre) and mechanism errors drawn from a distribution of nodal-plane
rotation, $\pm15^\circ$–$20^\circ$. Magnitudes truncated at the detection
threshold $M_c$.

**Metric and null distribution.** The test statistic is the difference in mean
$\Delta\mathrm{CFS}$ between the observed aftershocks and a randomised catalogue
that preserves the spatial distribution but draws mechanisms at random. Its null
distribution is obtained by 1000 randomisations; report a $z$-score, not a
bare difference.

**Falsification.** The correlation is falsified if the observed statistic lies
inside the central $95\%$ of the null distribution **when the simulation's
activation parameter is known to be non-zero** — that is a failure of the
detection method, not of the physics. Conversely, a positive result with a
spatially uniform synthetic catalogue (no $\Delta\mathrm{CFS}$ dependence) would
show that the mechanism randomisation itself induces an apparent correlation,
which is the most common way such tests produce false positives.
