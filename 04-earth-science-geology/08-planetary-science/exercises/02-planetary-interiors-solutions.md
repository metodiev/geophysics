# Solutions — 04-08-02 Planetary Interiors and Magnetic Fields

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Hydrostatic equilibrium

**(a)** $\mathrm{d}M/\mathrm{d}r = 4\pi r^2\rho$ is geometry (a shell's volume);
$g(r) = GM(r)/r^2$ is Newton's theorem that only the enclosed mass contributes;
$\mathrm{d}P/\mathrm{d}r = -\rho g$ is the force balance on a shell.

**(b)** For constant $\rho$: $M(r) = \tfrac43\pi r^3\rho$, so
$g(r) = \tfrac43\pi G\rho r$ and

$$\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho g = -\frac{4}{3}\pi G\rho^2r
\quad\Longrightarrow\quad
P(r) = \frac{2}{3}\pi G\rho^2(R^2 - r^2),$$

using $P(R) = 0$, so $P(0) = \tfrac23\pi G\rho^2R^2$.

**(c)** $P_\mathrm{centre} = \tfrac23\pi(6.6743\times10^{-11})(3934)^2
(3.3895\times10^6)^2 = 2.486\times10^{10}$ Pa $= 24.9$ GPa.

**(d)** The radius and the mass (hence the mean density) are measured — the radius
by imaging or occultation, the mass by tracking a spacecraft or a moon. The
central pressure is **not** measured: it is the integral of an assumed profile.

---

## ★2 — The moment-of-inertia factor

**(a)** With $R_c = R/2$ and $\rho_c = 2\rho_m$:

$$M = \tfrac43\pi R^3\rho_m\left(\frac{2}{8} + \frac{7}{8}\right)
= \tfrac43\pi R^3\rho_m\frac{9}{8},$$

$$C = \tfrac83\pi R^5\rho_m\left(\frac{2}{32} + \frac{31}{32}\right)
= \tfrac83\pi R^5\rho_m\frac{33}{32}.$$

**(b)**

$$\alpha = \frac{C}{MR^2}
= \frac{(8/3)(33/32)}{(4/3)(9/8)}
= \frac{264/96}{36/24} = \frac{2.750}{1.500} = 0.3667 .$$

**(c)** 0.3667 is below the uniform value of 0.4, so the body is centrally
condensed. The departure is modest because the core occupies only $\tfrac18$ of
the volume: to reach $\alpha = 0.33$, as the Earth does, requires either a much
denser core or a mantle whose density also increases with depth — which is
exactly what ★★6 and ★★★8 explore.

**(d)** A measurement that depends on the radial distribution rather than only on
the total moment: the gravitational harmonic $J_2$ (which for a rotating fluid
body is related to $\alpha$ through the Darwin–Radau relation and so does not
independently fix $R_c$), a seismic phase that reflects from the core–mantle
boundary, or the moment of a close-orbit moon's tidal response. In practice it is
seismology on the Earth and the combination of $J_2$, $C_{22}$ and the
libration amplitude on a small body.

---

## ★3 — Dynamo parameters

**(a)** $R_m = \mu_0\sigma UL
= (1.2566\times10^{-6})(3\times10^5)(5\times10^{-4})(2\times10^6) = 377$.

**(b)** $\tau_\eta = \mu_0\sigma L^2
= (1.2566\times10^{-6})(3\times10^5)(4\times10^{12}) = 1.508\times10^{12}$ s
$= 47\,800$ years.

**(c)** It is the time for the field to decay by diffusion if the fluid motion
stopped — equivalently, the timescale on which the field is reorganized by
diffusion rather than by advection. A field that is older than $\tau_\eta$ must
be maintained, and one that is younger need not be.

**(d)** A conducting fluid region, a source of kinetic energy in that region
(convection, precession or tides), and sufficient conductivity and scale that
$R_m$ exceeds the critical value for dynamo action.

---

## ★4 — The dipole moment

**(a)** $\dfrac{4\pi}{\mu_0} = 10^7$ exactly (because $\mu_0 = 4\pi\times10^{-7}$),
so

$$m = (10^7)(2.5\times10^{-5})(6.371\times10^6)^3
= (10^7)(2.5\times10^{-5})(2.5859\times10^{20}) = 6.46\times10^{22}\ \mathrm{A\,m^2}.$$

**(b)** $V_\mathrm{core} = \tfrac43\pi(3.48\times10^6)^3 = 1.765\times10^{20}$ m³,
so $M = 6.46\times10^{22}/1.765\times10^{20} = 366$ A m⁻¹.

**(c)** 366 A m⁻¹ is smaller than the saturation magnetisation of iron (of order
$10^6$ A m⁻¹) by a factor of 2700, so a remanent origin is *energetically*
possible. Amplitude alone therefore does not exclude it.

**(d)** Two arguments do: the field **changes** on a human timescale (secular
variation, and reversals in the geological record), which a fossil cannot do; and
the source region is far above the Curie temperature of iron (near 1043 K), where
ferromagnetic ordering cannot persist, so a stable remanent moment cannot be
carried by the present core at all.

---

## ★★5 — The hydrostatic integration

**(a)** $\rho_\mathrm{mean} = 5513.4$ kg m⁻³; the analytic central pressure is
172.5 GPa and the numerical integration gives 172.5 GPa. The agreement validates
the integration, not the model.

**(b)** Mass from the profile $6.0219\times10^{24}$ kg against a tabulated
$5.9722\times10^{24}$ kg — 0.83 per cent high — and a central pressure of
330.4 GPa.

**(c)**

| $\rho_c$ (kg m⁻³) | $\rho_m$ (kg m⁻³) | mass ($10^{24}$ kg) | $P_\mathrm{centre}$ (GPa) |
|---|---|---|---|
| 10000 | 4000 | 5.3922 | 269.9 |
| 11000 | 4500 | 6.0221 | 330.4 |
| 13000 | 5000 | 6.8285 | 447.1 |
| 12000 | 4200 | 5.9266 | 364.4 |

The central pressure is not identifiable from the mass and radius alone: a family
of profiles spans 270 to 447 GPa while the mass varies by 27 per cent, and the row
that matches the reference pressure has a mass 0.7 per cent low. Mass and radius
fix two numbers; a two-parameter profile has exactly two degrees of freedom, so
they can be made to fit — which is why they carry no information about the
interior.

**(d)** Because the model has as many free parameters as there are data to fit, so
reproducing any one target is guaranteed rather than informative. A validation
requires an *independent* observable — a moment of inertia, a seismic travel time,
a Love number — that was not used in the fit.

---

## ★★6 — The moment of inertia and a failed inversion

**(a)** $\alpha = 0.400004$ against the analytic 0.4, the small excess being the
discretisation error of the grid.

**(b)**

| $\rho_c$ | $\rho_m$ | $\alpha$ | mass ($10^{24}$ kg) |
|---|---|---|---|
| 9000 | 4000 | 0.35251 | 5.2156 |
| 10000 | 4200 | 0.34845 | 5.5734 |
| 11000 | 4500 | 0.34653 | 6.0220 |
| 13000 | 5000 | 0.34196 | 6.8284 |

**(c)** The geodetic inference is $\alpha = 0.3308$; the inversion requires
$\rho_c = 13\,538$ kg m⁻³ at a core radius of 3480 km, and the model then has a
mass of $6.47\times10^{24}$ kg — 8.3 per cent above the tabulated value.

**(d)** The failure says the **two-layer model is inadequate**: every choice of
the two densities gives $\alpha$ above the geodetic value, so the model has too
little central condensation to reach 0.3308 at a physically acceptable core
density. What is missing is a **graded mantle** — a density that increases with
depth within the mantle itself, which a uniform mantle cannot represent. The
Earth's lower mantle is substantially denser than its upper mantle, and that is
exactly the missing central condensation.

---

## ★★7 — Skin depth and induction

**(a)** 319.6 km at 0.1 S m⁻¹, 101.1 km at 1, 58.3 km at 3 and 31.9 km at
10 S m⁻¹.

**(b)** Setting $\delta = 10^5$ m in
$\delta = \sqrt{2/(\mu_0\sigma\omega)}$ with
$\omega = 2\pi/(11.2\times3600) = 1.5585\times10^{-4}$ s⁻¹ gives

$$\sigma = \frac{2}{\mu_0\omega\delta^2}
= \frac{2}{(1.2566\times10^{-6})(1.5585\times10^{-4})(10^{10})} = 1.02\ \mathrm{S\,m^{-1}}.$$

**(c)** At a 3.55-day period, $\omega$ is smaller by a factor of 7.6, so
$\delta$ is larger by $\sqrt{7.6} = 2.76$: 881 km at 0.1 S m⁻¹ and 279 km at
1 S m⁻¹. A conducting layer of order 100 km is then much thinner than $\delta$,
so its inductive response is weak and it is nearly transparent to the varying
field. The long period is a poor discriminator because it cannot distinguish a
100 km conductor from a 30 km one.

**(d)** Induction determines the **conductance**, the product $\sigma t$ (and, for
a body with structure, a frequency-dependent transfer function). To report a
thickness one must assume the conductivity — which is to assume a salinity and a
temperature — and also model the conductivity of the layers above and below, both
of which contribute to the observed response.

---

## ★★★8 — The degeneracy of the interior inversion

**(a)** With the mantle fixed at 4500 kg m⁻³ and the core radius given:

| $R_c$ (km) | required $\rho_c$ (kg m⁻³) | mass ($10^{24}$ kg) | mass error |
|---|---|---|---|
| 2500 | 23 648 | 6.1277 | $+2.6$ per cent |
| 3000 | 16 822 | 6.2680 | $+5.0$ per cent |
| 3480 | 13 538 | 6.4699 | $+8.3$ per cent |
| 4000 | 11 769 | 6.8232 | $+14.3$ per cent |

**(b)** Tabulated in the table above, against $M_\oplus = 5.9722\times10^{24}$ kg.

**(c)** The solutions form a **curve**: a family of (core radius, core density)
pairs reproduces the same $\alpha$, with the required core density falling as the
core radius grows. A single value of $\alpha$ therefore determines a
one-dimensional solution set, not a point, and the mass constraint is what selects
among them — but every member of the curve above also mismatches the mass, and by
a growing amount as the core radius increases. Combining the two constraints
(α and M) still leaves a curve, because the model has two parameters
($R_c$ and $\rho_c$) even when the mantle density is fixed. **Two data and two
parameters give a unique point only if the data are independent and the model is
right; here the model is wrong and the "solution" it produces is the evidence.**

**(d)** The degeneracy is broken by a third, independent observable that weights
the interior differently. A seismic arrival time that samples the core–mantle
boundary gives $R_c$ directly, which was the assumption in ★★6 and is why the
failure there was a failure of the *mantle* model. Failing that, a Love number or
a tidal response constrains the rigidity as a function of depth; a magnetic
induction measurement constrains the conductance of a fluid layer; and a
nutation or libration amplitude constrains the moment of the whole body
independently of the mass. Each adds a different weighting function to the same
inverse problem, and it is the *variety* of weightings, not the precision of any
one, that makes the interior determinate. On the Earth that variety exists and
the interior is known; on most other bodies it does not, and the interior is a
model with a stated uncertainty — which is the honest way to present it.

---

## ★★★9 — Induction at two periods

**(a)** For $T = 3$ days, $\omega = 2\pi/(3\times86400) = 2.424\times10^{-5}$
s⁻¹, so

$$\delta = \sqrt{\frac{2}{(1.2566\times10^{-6})(1)(2.424\times10^{-5})}}
= \sqrt{6.565\times10^{10}} = 2.56\times10^5\ \mathrm{m} = 256\ \mathrm{km}.$$

**(b)** The layer is 50 km thick against a 256 km skin depth, so it is **thin**
compared with $\delta$: the varying field penetrates it almost unattenuated, the
induced currents are weak, and the induced dipole is a small fraction of the
maximum possible response. A detection at that period would require a very
precise magnetometer.

**(c)** At $T = 12$ hours, $\omega = 1.454\times10^{-4}$ s⁻¹, so
$\delta = \sqrt{2/((1.2566\times10^{-6})(1.454\times10^{-4}))} = 105$ km. The
layer is now thinner than but comparable with the skin depth, and the response is
roughly a factor of $(256/105)^2 = 5.9$ stronger in power than at the longer
period. **The response grows as the period shortens**, which is why a short-period
external field is the discriminating one and why the orbital period of a
satellite inside a magnetosphere is chosen carefully.

**(d)** The induced field amplitude is proportional to the *conductance* — the
product of conductivity and thickness — because a thin layer with high
conductivity and a thick layer with low conductivity produce the same integrated
current, and it is the integrated current that makes the induced dipole. So a
detection establishes $\sigma t$, not $t$. Converting one to the other requires
the conductivity, which for an aqueous ocean means the salinity and the
temperature, and neither is measured remotely; and it requires knowing the
conductivity of the ice above and the rock below, because the response is the
sum of all the conducting layers. The practical approach is to fit a
frequency-dependent transfer function with a layered model and to report the
*range* of (thickness, salinity) pairs that fit — which is the honest form of the
inference, and the reason a subsurface ocean's properties are quoted with a
model attached.
