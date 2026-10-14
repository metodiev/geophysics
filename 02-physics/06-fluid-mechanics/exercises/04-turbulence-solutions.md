# Solutions — 02-06-04 Turbulence, Mixing and Eddy Diffusivity

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. $C_K = 1.5$ and $\kappa = 0.41$ are the
> empirical constants used throughout; neither is derived.

---

## ★1 — Kolmogorov microscales

**(a)** With $\nu = 10^{-6}$, $\varepsilon = 10^{-3}$:

$$\eta = \left(\frac{10^{-18}}{10^{-3}}\right)^{1/4} = (10^{-15})^{1/4} =
1.78\times10^{-4}\ \mathrm{m} = \mathbf{0.178\ mm},$$
$$u_\eta = (10^{-6}\times10^{-3})^{1/4} = (10^{-9})^{1/4} =
\mathbf{5.62\times10^{-3}\ m\,s^{-1}}, \qquad
\tau_\eta = (10^{-6}/10^{-3})^{1/2} = \mathbf{0.0316\ s}.$$

**(b)** $\eta/L = 1.78\times10^{-4}$. About one part in 5600.

**(c)** For $\varepsilon = 1$: $\eta = 3.16\times10^{-5}$ m,
$u_\eta = 3.16\times10^{-2}$ m s⁻¹, $\tau_\eta = 10^{-3}$ s. So
$\eta \propto \varepsilon^{-1/4}$, $u_\eta \propto \varepsilon^{1/4}$,
$\tau_\eta \propto \varepsilon^{-1/2}$: the dissipation scale *shrinks* as the
flow is driven harder, which is the opposite of the naive expectation.

**(d)** Because $\eta$ is where the cascade terminates, and the only quantities
available to set that scale are the rate at which energy is being delivered down
the cascade ($\varepsilon$) and the coefficient that dissipates it ($\nu$). A
larger $\varepsilon$ delivers energy faster, so viscosity must act at a smaller
scale to keep up.

---

## ★2 — Scale separation

**(a)** $\varepsilon \sim U^3/L = 1^3/1 = \mathbf{1\ m^2\,s^{-3}}$.

**(b)** $\eta = (\nu^3/\varepsilon)^{1/4} = (10^{-18}/1)^{1/4} =
3.16\times10^{-5}$ m $= 0.032$ mm.

**(c)** $L/\eta = 1/3.16\times10^{-5} = \mathbf{3.16\times10^{4}}$, and
$Re = UL/\nu = 10^{6}$, $Re^{3/4} = 3.16\times10^{4}$. They agree, which is the
content of the $L/\eta \sim Re^{3/4}$ scaling.

**(d)** $(L/\eta)^3 = 3.16\times10^{13}$ grid points. At $Re = 10^{10}$ (a
geophysical atmosphere) it is $3.2\times10^{22}$. Direct numerical simulation of
geophysical turbulence is therefore impossible, and everything in this lesson
exists to make that impossibility as harmless as possible.

---

## ★3 — The log law

**(a)** $u(z) = \dfrac{0.05}{0.41}\ln\dfrac{z}{10^{-3}} = 0.12195\ln(10^3 z)$:

| $z$ (m) | $u$ (m s⁻¹) |
|---|---|
| 1 | 0.8424 |
| 10 | 1.1232 |
| 100 | 1.4040 |

These reproduce the demo's printed values exactly.

**(b)** $\mathrm{d}u/\mathrm{d}z = u_*/(\kappa z) = 0.12195/z$:
12.1951, 1.2195, 0.12195 s⁻¹ at 1, 10, 100 m.

**(c)** $\nu_t = \kappa u_* z = 0.0205\,z$: 0.0205, 0.205, 2.05 m² s⁻¹.

**(d)** Because $\nu_t \to \infty$ as $z$ increases makes no physical sense: there
is no unbounded reservoir of turbulent energy, and the eddy viscosity must
eventually be limited by the depth of the boundary layer. The divergence signals
that the mixing length $l = \kappa z$ cannot hold far from the wall; it is a
near-wall closure that must be matched to an outer-layer model.

---

## ★4 — Richardson number and suppression

| $\partial\theta/\partial z$ (K m⁻¹) | $N^2$ (s⁻²) | $Ri$ | $1/(1+Ri/0.25)$ |
|---|---|---|---|
| 0.001 | $3.27\times10^{-5}$ | 0.327 | 0.433 |
| 0.01 | $3.27\times10^{-4}$ | 3.27 | 0.0710 |
| 0.05 | $1.635\times10^{-3}$ | 16.35 | 0.0151 |

The shear is the same in every row; only the stratification changes. With the
numbers used, the suppression factor spans a factor of **29**, which is the
quantitative content of "stratification controls turbulent transport".

---

## ★★5 — Buoyancy frequency

**(a)** $N^2 = \dfrac{g}{\theta}\dfrac{\partial\theta}{\partial z} =
\dfrac{9.81}{300}\times0.01 = 3.27\times10^{-4}\ \mathrm{s^{-2}}$, so
$N = \mathbf{0.0181\ s^{-1}}$.

**(b)** $2\pi/N = 347$ s, about 5.8 minutes. Observed internal-wave periods in
the ocean thermocline are of this order, which is the reason $N$ is worth
computing.

**(c)** $Ri = N^2/(\partial u/\partial z)^2 = 3.27\times10^{-4}/(0.02)^2 =
\mathbf{0.817}$. That exceeds the critical $0.25$, so the layer is expected to
be laminar or at most intermittently turbulent; sustained turbulence requires
$Ri \lesssim 0.25$.

**(d)** $(\partial u/\partial z)^2 = N^2/0.25 = 1.31\times10^{-3}$, so
$|\partial u/\partial z| = \mathbf{0.0362\ s^{-1}}$.

---

## ★★6 — Reading the demo

**(a)** Ocean surface layer: $\eta = 0.5520$ mm, $u_\eta = 1.7673$ mm s⁻¹,
$\tau_\eta = 0.3123$ s.

**(b)** $\nu_t$ at $y = 1$ m is $0.0205$ m² s⁻¹, and the demo reports
$2.101\times10^{4}$ times the molecular value. Four orders of magnitude.

**(c)** The last column is **1.000000 at every height**. It is identically one
because the log law *is* the mixing-length closure with $l = \kappa z$: the
profile was obtained by assuming the closure and then integrated. Its agreement
is therefore a self-consistency check, not a test. The closure is tested by
comparing measured profiles with the log law, and by measuring $z_0$ and $u_*$
independently — not by re-deriving the profile from the closure.

**(d)** Neutral: $K = 1.0$ m² s⁻¹. With $\mathrm{d}\theta/\mathrm{d}z = 0.05$
K m⁻¹: $K = 0.01506$ m² s⁻¹. Ratio $\approx \mathbf{66}$. The mean shear is
identical in both cases, so the resolved field cannot distinguish them.

---

## ★★7 — Mixing times

**(a)** $t = h^2/K = 100/10^{-3} = 10^{5}$ s $= 1.16$ days.
**(b)** $t = 2500/0.1 = 2.5\times10^{4}$ s $= 0.29$ days.
**(c)** $t = 1.6\times10^{7}/10^{-4} = 1.6\times10^{11}$ s $= \mathbf{5070\
years}$.

**(d)** Because $K$ differs by three orders of magnitude (0.1 against
$10^{-4}$ m² s⁻¹) and $h^2$ by more than four. A stirred mixed layer is mixed
in hours; the abyss is ventilated over millennia. The physical difference is the
energy supply: wind and convection stir the mixed layer daily, whereas the
abyssal interior receives energy only from internal-wave breaking and from
boundary processes. Both numbers describe seawater; the difference is the *flow*,
which is the whole point of the lesson.

---

## ★★8 — Where gradient diffusion fails

**(a)** $\overline{w'\theta'} = +0.05\ \mathrm{K\,m\,s^{-1}}$ (upward) with
$\partial\overline{\theta}/\partial z = +10^{-3}\ \mathrm{K\,m^{-1}}$ gives

$$K = -\frac{\overline{w'\theta'}}{\partial\overline{\theta}/\partial z} =
-\frac{0.05}{10^{-3}} = \mathbf{-50\ m^2\,s^{-1}}.$$

**(b)** A **negative** diffusivity would move heat from cold to hot: it violates
the second law. It is not a small error or a sign convention; the closure has
produced an unphysical coefficient.

**(c)** The flux is carried by large convective eddies — plumes and thermals
originating at the heated surface — which transport warm air upward into a
region where the mean profile is stable. The flux at a point is set by the
*origin* of the air (the surface), not by the local gradient at the point of
measurement. This is precisely the non-local transport that a local closure
cannot represent.

**(d)** A mass-flux (or plume) model represents the transport by an ensemble of
coherent updraughts and downdraughts with their own temperature and velocity,
giving up the idea of a local diffusivity and gaining the ability to transport
counter to the gradient. Its cost is more state variables per grid column and a
further set of closure assumptions (entrainment and detrainment rates). See
[16-atmosphere-climate](../../../16-atmosphere-climate/README.md).

---

## ★★★9 — The energy cascade and what is resolved

**(a)** In equilibrium the turbulence neither grows nor decays, so
$\varepsilon = P$. The shear production is the Reynolds stress working against
the mean shear, $P \sim U^2\,(U/L)$: the velocity scale of the energy-containing
eddies is $U$ and their turnover rate is $U/L$. Hence $\varepsilon \sim U^3/L$.
Note that this argument uses only the large scales: at that end of the range
viscosity does not appear.

**(b)** By Kolmogorov's first similarity hypothesis, the statistics of the small
scales depend only on $\varepsilon$ (the rate at which energy arrives) and $\nu$
(the coefficient that removes it), because the small scales have no memory of the
large-scale geometry. Only one length can be formed from $\nu$ and
$\varepsilon$, namely $(\nu^3/\varepsilon)^{1/4}$; dimensional analysis
therefore fixes $\eta$ uniquely. The hypothesis is *not* that the small scales
are independent of the large ones — they depend on $\varepsilon$, which is set by
the large scales — but that they depend on them only through $\varepsilon$.

**(c)** $\tau_L \sim L/U$ and $\tau_\eta = (\nu/\varepsilon)^{1/2}$.
Their ratio:
$\dfrac{L/U}{(\nu/\varepsilon)^{1/2}} =
\dfrac{L}{U}\left(\dfrac{\varepsilon}{\nu}\right)^{1/2}$, and with
$\varepsilon \sim U^3/L$ this becomes
$\dfrac{L}{U}\cdot\dfrac{U^{3/2}}{L^{1/2}\nu^{1/2}} =
\left(\dfrac{UL}{\nu}\right)^{1/2} = Re^{1/2}$.

**(d)** The atmosphere's $\eta \sim 1$ mm is a *microscale*; the largest resolved
scale in a model with 100 m vertical grid spacing is 100 m, and the largest
energetic scale might be $10^{4}$–$10^{6}$ m. Taking $L \sim 10^{5}$ m and
$\eta \sim 10^{-3}$ m, the ratio is $10^{8}$, and the resolved ratio is only up
to $10^{5}$–$10^{6}$ in the vertical. So roughly **one to three decades of the
eight-to-nine available decades are resolved in the vertical**, and the rest —
including all of the inertial subrange and the dissipation range — is
parameterised. That is the honest accounting behind any statement that a climate
model "resolves" the boundary layer.

---

## ★★★10 — Intermittency

**(a)** Volume average:
$\varepsilon_{\text{avg}} = 0.05\times10^{-7} + 0.95\times10^{-10} =
5.0\times10^{-9} + 9.5\times10^{-11} = \mathbf{5.10\times10^{-9}\
\mathrm{m^2\,s^{-3}}}$.

**(b)** A model with uniform $\varepsilon_{\text{avg}} = 5.10\times10^{-9}$:

- in active patches, $\varepsilon_{\text{model}}/\varepsilon_{\text{true}} =
  5.10\times10^{-9}/10^{-7} = 0.051$, i.e. it **underestimates by a factor of
  20**;
- in quiet regions, $5.10\times10^{-9}/10^{-10} = 51$, i.e. it
  **overestimates by a factor of 51**.

The column integral is right by construction; every local value is wrong by one
to two orders of magnitude, and the sign of the error depends on where you look.

**(c)** Two candidate tests: (i) the **vertical profile of a tracer** whose
evolution depends on the *distribution* of mixing, not only its integral — for
example the shape of an injected dye patch or the curvature of a nutrient
profile; and (ii) the **dissipation-rate probability distribution** measured by
microstructure profilers, which is highly skewed and has a long tail that a
uniform $\varepsilon$ cannot reproduce. A column-integrated test cannot
distinguish a uniformly mixed column from a column with intense mixing in 5 per
cent of its volume — the same integral is obtained — which is exactly why it is
insufficient.

**(d)** Intermittency is the statement that $\varepsilon$ is concentrated: its
probability distribution is skewed, with most of the volume dissipating far
below the mean and a small fraction dissipating far above it. The mean
$\varepsilon$ is a single number and can be identical for a uniform and an
intermittent field; consequentially, any closure built only on the mean has
discarded the very structure that controls local mixing. This is the same lesson
as section 4 of the lesson: an averaged quantity does not determine the
transport.
