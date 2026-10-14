# Solutions — 01-01-02 Orders of Magnitude and Fermi Estimation

> Attempt the exercises first. These solutions show one valid route and state
> where the answer is inherently a range. Numeric values marked "verified" were
> computed and checked rather than estimated by hand.

---

## ★1 — Orders of magnitude

| | Value | 1 s.f. | Order of magnitude |
|---|---|---|---|
| (a) | 8.4×10³ | 8×10³ | 3 |
| (b) | 2.7×10⁻⁵ | 3×10⁻⁵ | −5 |
| (c) | 6.02×10²³ | 6×10²³ | 24 |
| (d) | 9.81 | 10 | 1 |

**Note on (d).** Rounding 9.81 to one significant figure gives 10, whose order of
magnitude is 1. This is a case where the rounding changes the leading digit;
$\log_{10} 9.81 \approx 0.99$, which rounds to 1. Both "about 10" and "order 1"
are correct statements.

---

## ★2 — Seconds in a century; metres per degree of latitude

**Century.** $100\ \text{yr} \times 3.15\times10^{7}\ \text{s/yr}
= 3.15\times10^{9}\ \text{s} \approx 3\times10^{9}$ s (verified).

**Metres per degree of latitude.** The full circumference is $2\pi R$ with
$R = 6.371\times10^{6}$ m:

$$2\pi (6.371\times10^{6}) \approx 4.00\times10^{7}\ \mathrm{m}.$$

Divide by 360°:

$$\frac{4.00\times10^{7}}{360} \approx 1.11\times10^{5}\ \mathrm{m}
\approx 111\ \mathrm{km\ per\ degree}.$$

So a degree of latitude is about **111 km** (verified). This is worth memorising:
it converts map distances to degrees instantly, and it is why 1 arc-minute of
latitude is approximately 1 nautical mile (1852 m) — a historical coincidence
that is still the definition's origin.

**Why the two-step method worked.** Step 1 (circumference) is a coarse estimate;
step 2 (divide by 360) is exact given step 1. The uncertainty is dominated by
step 1, which is excellent because $R$ is known to many digits. The answer is
therefore good to far better than "one order of magnitude" — **estimates are
often much better than their worst case, and you should say which regime you are
in.**

---

## ★3 — Sketch before computing

**Reasoning.** The point-mass anomaly is $g_z = GM/d^{2}$. With
$M = 10^{12}$ kg and $d = 10^{3}$ m:

$$g_z \sim \frac{(6.7\times10^{-11})(10^{12})}{10^{6}}
= \frac{6.7\times10^{1}}{10^{6}} = 6.7\times10^{-5}\ \mathrm{m\,s^{-2}}.$$

Convert to mGal: $6.7\times10^{-5} / 10^{-5} = 6.7$ mGal (verified).

**Answer.** The anomaly is about **7 mGal**, which is **far above** the 0.01 mGal
threshold — a factor of ~670. Unambiguously detectable.

**Why the sketch is useful.** You did not need the exact constant, only the
scaling: mass up 10³ from the earlier $10^{9}$ kg example, depth up from 300 m
to 1000 m (factor 3.33 in depth → factor ~11 reduction), so $7.4\times10^{-2}
\times 10^{3} / 11 \approx 6.7$ mGal. **Scaling from a previous result is often
faster than computing from scratch, and it is the same skill.**

---

## ★★4 — Mass of the atmosphere

**Decomposition.** Mass = (mean surface pressure) × (Earth's surface area) / g.
This follows from hydrostatic balance: the surface pressure equals the weight per
unit area of the overlying column,
$p_s = M_{\text{atm}} g / A$.

**Inputs.**

- Mean sea-level pressure $p_s \approx 1.013\times10^{5}$ Pa
- Earth radius $R = 6.371\times10^{6}$ m, so
  $A = 4\pi R^{2} = 4\pi (6.371\times10^{6})^{2} \approx 5.10\times10^{14}\ \mathrm{m^{2}}$
- $g \approx 9.81\ \mathrm{m\,s^{-2}}$

**Compute.**

$$M_{\text{atm}} = \frac{p_s A}{g}
= \frac{(1.013\times10^{5})(5.10\times10^{14})}{9.81}
\approx \frac{5.17\times10^{19}}{9.81}
\approx 5.3\times10^{18}\ \mathrm{kg}\ \text{(verified)}.$$

**Compare with the standard figure.** The commonly quoted total mass of the
atmosphere is about $5.15\times10^{18}$ kg — the decomposition recovers it to
about 3%, which is better than the "one order of magnitude" the method promises.

**Why this works so well.** The estimate inherits the precision of the inputs,
and mean sea-level pressure is known very precisely because it is measured
everywhere, continuously. The method is only as rough as its weakest input.

**Interesting consequence.** The atmosphere is about $10^{-6}$ of the Earth's
mass ($5.97\times10^{24}$ kg). It is a trace film — yet it is the entire context
for climate, weather, and much of remote sensing (
[16-atmosphere-climate](../../../16-atmosphere-climate/README.md)).

---

## ★★5 — Pore-pressure diffusion delay

**Scaling.** $\tau \sim L^{2}/\kappa$ with $L = 500$ m.

**For $\kappa = 10^{-2}\ \mathrm{m^{2}\,s^{-1}}$ (verified):**

$$\tau \sim \frac{(500)^{2}}{10^{-2}} = \frac{2.5\times10^{5}}{10^{-2}}
= 2.5\times10^{7}\ \mathrm{s}
= \frac{2.5\times10^{7}}{86400} \approx 290\ \text{days}.$$

So roughly **9–10 months** for the pressure front to diffuse 500 m.

**For $\kappa = 10^{-1}\ \mathrm{m^{2}\,s^{-1}}$ (verified):**

$$\tau \sim \frac{2.5\times10^{5}}{10^{-1}} = 2.5\times10^{6}\ \mathrm{s}
\approx 29\ \text{days}.$$

**Why the sensitivity is exactly linear in $1/\kappa$.** The scaling is
$\tau \propto L^{2}/\kappa$, so $\tau$ depends on $\kappa$ as $1/\kappa$ — a
factor-of-10 increase in diffusivity gives a factor-of-10 *decrease* in delay.
There is no square or other complication. This is why hydraulic diffusivity is
the single most important parameter in induced-seismicity timing, and why it is
so difficult to constrain: it varies over orders of magnitude with fracture
density, effective stress, and saturation, and it can change as pressure
diffuses.

**Practical consequence.** In real injection-induced sequences, delays of days
to years are observed at distances of hundreds of metres to kilometres, and the
inferred diffusivities span roughly $10^{-3}$ to $10^{0}\ \mathrm{m^{2}\,s^{-1}}$
depending on the setting. A single-number estimate is therefore a starting
hypothesis, not a prediction. The full treatment, including rate-and-state
friction, is in
[06-12 Induced and Triggered Seismicity](../../../06-seismology/12-induced-and-triggered-seismicity/README.md).

---

## ★★6 — Magnetotelluric period for 10 km depth

**Given.** Skin depth $\delta \approx 503\sqrt{\rho\,T}$ metres, with $\rho$ in
Ω·m and $T$ in seconds. Want $\delta = 10^{4}$ m and $\rho = 100$ Ω·m.

**Solve for $T$.**

$$\sqrt{\rho T} = \frac{\delta}{503} = \frac{10^{4}}{503} \approx 19.88.$$

$$\rho T \approx 395.3 \quad\Longrightarrow\quad
T = \frac{395.3}{100} \approx 4.0\ \mathrm{s}\ \text{(verified)}.$$

**Answer.** About **$T \approx 4$ s**.

**Is this practical?** Yes — periods of seconds are routine in
magnetotellurics, and modern broadband instruments cover roughly $10^{-3}$ to
$10^{3}$ s. Sounding to 10 km in a 100 Ω·m half-space sits comfortably in the
middle of the practical band.

**Why the square root matters.** Because $\delta \propto \sqrt{T}$, reaching
ten times deeper requires a **hundred times longer** period. This is the same
$\sqrt{\ }$ that appears in all diffusion problems, and it is why deep
sounding is fundamentally harder than shallow sounding — you must wait, and
natural EM signals are weaker at long periods. Development in
[08-04 Electromagnetic Induction](../../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md).

**Caveat.** The relation assumes a uniform half-space. Real Earth structure
makes the apparent resistivity frequency-dependent, so this calculation gives a
*planning* estimate, not an interpretation.

---

## ★★7 — Detectability of a buried ferrous object

**Step 1 — volume.** For a 20 kg steel object at 7800 kg/m³:

$$V = \frac{20}{7800} \approx 2.56\times10^{-3}\ \mathrm{m^{3}}.$$

**Step 2 — dipole moment.** With $M \approx 1\ \mathrm{A\,m^{-1}}$ (a modest
induced magnetisation — a conservative assumption for steel in Earth's field):

$$m = M V \approx 1 \times 2.56\times10^{-3} = 2.56\times10^{-3}\ \mathrm{A\,m^{2}}.$$

**Step 3 — field at 3 m, equator-like geometry.** Using the equatorial dipole
formula from the lesson's demonstration,
$B = \mu_0 m /(4\pi r^{3})$:

$$B = \frac{(4\pi\times10^{-7})(2.56\times10^{-3})}{4\pi (3)^{3}}
= \frac{10^{-7} \times 2.56\times10^{-3}}{27}
\approx 9.5\times10^{-12}\ \mathrm{T} = 9.5\times10^{-3}\ \mathrm{nT}.$$

**Step 4 — compare with resolution.** The answer is about
**$10^{-2}$ nT**, against a typical total-field magnetometer resolution of
0.1 nT — **an order of magnitude below detection.**

**Conclusion. Detection of this object by total-field magnetics alone is not
possible at 3 m depth with a 0.1 nT instrument — unless the object's
magnetisation is substantially higher than assumed.**

**Assumptions and their importance (state these explicitly):**

| Assumption | Effect if wrong |
|---|---|
| $M = 1\ \mathrm{A\,m^{-1}}$ | Real steel can reach $10^{2}$–$10^{4}$ A/m if strongly magnetised; this would change the answer by 2–4 orders of magnitude and make it detectable |
| Dipole approximation | Valid because $r = 3$ m ≫ object size (~0.13 m); good to ~$10^{-3}$ |
| Object is a compact body | A long pipe or rebar behaves differently |
| No background gradient | In practice, geological and cultural gradients dominate |

**The professional lesson.** This calculation's *value* is not the number
$10^{-2}$ nT. It is the realisation that **the magnetisation assumption
dominates the result**. A sensible follow-up is therefore to ask what $M$ is
required for detection:

$$M_{\text{min}} = M \times \frac{0.1}{9.5\times10^{-3}} \approx 10.5\ \mathrm{A\,m^{-1}},$$

so the object is detectable if $M \gtrsim 11\ \mathrm{A\,m^{-1}}$. Whether that
is plausible depends on the object's material and history — a question that
only field measurement or laboratory testing can answer.

**This is the correct form of a feasibility study: identify the controlling
assumption, then bound it.** Related: magnetic methods in
[08-03 Magnetic Anomalies and Modelling](../../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md)
and buried-object detection in
[11-06 Geotechnical and Engineering Geophysics](../../../11-exploration-geophysics/06-geotechnical-and-engineering/README.md).

---

## ★★★8 — Cooling of the core–mantle boundary

This is a research-style exercise: the answer is a range, and the *comparison
with the literature* is the deliverable.

**Part A — CMB heat loss timescale (naive).**

Given CMB heat flow $Q \approx 10\ \mathrm{TW} = 10^{13}$ W (a commonly quoted
order of magnitude) and outer-core mass $M_{oc} \sim 10^{24}$ kg with specific
heat capacity $c_p \sim 10^{3}\ \mathrm{J\,kg^{-1}\,K^{-1}}$, the heat content
is $\sim 10^{27}$ J/K. Losing $10^{13}$ W:

$$\frac{10^{27}}{10^{13}} = 10^{14}\ \mathrm{s}
\approx 3\times10^{6}\ \mathrm{yr\ per\ kelvin}.$$

So the core cools on the order of **a few million years per kelvin of
temperature drop** by conduction alone (verified arithmetic).

**Part B — how much can it cool before solidifying?**

A crude bound: solidification releases latent heat
$L \sim 10^{6}$ J/kg, so solidifying the whole outer core would release
$\sim 10^{30}$ J. At $10^{13}$ W that is $10^{17}$ s ≈ 3 Ga. But the outer core
will not fully solidify during Earth's history, so this is an upper bound, not a
prediction.

**Part C — the honest answer.**

The naive calculation above gives timescales of order $10^{6}$ yr/K and
$10^{17}$ s for complete solidification. **Both are sensitive to assumptions that
this estimate cannot constrain:**

1. **CMB heat flow is poorly known.** Published estimates span roughly 5–15 TW,
   and some argue for higher values. A factor-of-2 error in $Q$ is a
   factor-of-2 error in every timescale.
2. **Compositional convection matters.** The geodynamo is driven largely by
   *buoyancy from light-element release* at the inner-core boundary, not by
   thermal convection alone. Ignoring compositional buoyancy changes the energy
   budget qualitatively, not just quantitatively.
3. **Radiogenic heating in the core** (if any) would offset cooling.
4. **The inner core's growth history** is itself an inference from palaeomagnetic
   and seismological evidence, not an input.
5. **Thermal conductivity of the core** is actively debated: higher values
   require a larger CMB heat flow and imply a younger inner core. This is a
   current research controversy, not a settled parameter.

**Part D — the comparison, and why your estimate diverges.**

Isotopic and thermal-evolution models constrained by palaeomagnetic evidence
(the field is at least ~3.5 Ga old) and by the inner core's inferred age
(hundreds of Myr to ~1.5 Ga depending on conductivity) place the CMB heat flow
and core thermal history in a much narrower and differently-balanced regime than
Part A suggests. **Your estimate diverges because it treats the core as a
passive cooling body, whereas the actual constraint is that the geodynamo must
have operated for billions of years** — that requirement, not the heat capacity,
sets the parameters.

**The methodological lesson.** Dimensional analysis and energy-balance estimates
are invaluable for *bounding* a problem and for telling you which quantities
matter. They are not sufficient to *solve* it when the system is constrained by
a long-term requirement rather than by an instantaneous balance. Recognising
which situation you are in is itself a research skill.

**Where to check.** Review papers on the thermal evolution of the core and the
geodynamo's energetics appear in *Reviews of Geophysics*, *Earth and Planetary
Science Letters*, and *Physics of the Earth and Planetary Interiors*. Consult
current literature via your library; the numbers have shifted substantially over
the past two decades as core conductivity estimates changed. See also
[12-04 Geomagnetic Field and Core Dynamics](../../../12-global-geophysics-interior/04-geomagnetism-and-core/README.md).

---

## ★★★9 — Numerical verification of the diffusion scaling

**Method.** Solve $\partial_t T = \kappa\, \partial_{zz} T$ on a half-space
$z \ge 0$ with $T(z,0) = 0$ and $T(0,t) = T_0$ for $t>0$. Diagnostic: the time
$t_{1/2}(L)$ at which $T(L,t) = T_0/2$.

**Exact solution (for reference).** The analytic solution is

$$T(z,t) = T_0\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa t}}\right),$$

so $T = T_0/2$ when $\mathrm{erfc}(x) = 1/2$, i.e. $x = x_{1/2}$ where
$x_{1/2} \approx 0.4769$. Therefore

$$t_{1/2} = \frac{L^{2}}{4\,\kappa\, x_{1/2}^{2}} \approx 1.099\,\frac{L^{2}}{\kappa}.$$

**Verified constant.** $4 x_{1/2}^{2} \approx 4(0.4769)^{2} \approx 0.9098$, so
$1/0.9098 \approx 1.099$. The proportionality constant is therefore **≈1.1**,
not the ≈0.1 that a careless reading of "of order 0.1" might suggest. This is
exactly why the dimensional estimate cannot supply the constant.

**Report.** Your numerical experiments should confirm:

| Quantity varied | Expected dependence | Confirmed? |
|---|---|---|
| Depth $L$ (with $\kappa$ fixed) | $t_{1/2} \propto L^{2}$ | exponent ≈ 2 on log–log axes |
| Diffusivity $\kappa$ (with $L$ fixed) | $t_{1/2} \propto 1/\kappa$ | exponent ≈ −1 |
| Amplitude $T_0$ | no dependence | $t_{1/2}$ independent of $T_0$ |

**Why dimensional analysis cannot give the constant.** The scaling exponents
follow from requiring both sides to have the same dimensions; that is a
requirement, not a solution. The constant depends on the *shape* of the initial
and boundary conditions — a step change, a linear ramp, and a sinusoid all
satisfy the same diffusion equation but have different constants. Dimensionless
constants carry information about geometry and boundary conditions that
dimensions alone cannot.

**Numerical caution.** To measure $t_{1/2}$ reliably you must resolve the
diffusive boundary layer, whose thickness grows as $\sqrt{\kappa t}$. Your grid
spacing $\Delta z$ must be small compared with that layer at the diagnostic time,
and your time step must satisfy the explicit-scheme stability condition
$\Delta t \le \Delta z^{2}/(2\kappa)$. Diagnose convergence by halving
$\Delta z$ and $\Delta t$ and confirming that $t_{1/2}$ stops changing. Without
this test you cannot distinguish a physical result from a discretisation
artefact. This is the practice of *verification*, developed in
[19-numerical-modeling-hpc](../../../19-numerical-modeling-hpc/README.md).

---

## Self-assessment

- [ ] I can estimate any geophysical quantity to within a factor of ~3 using
      the anchor list.
- [ ] I compute a *first* estimate before running code, every time.
- [ ] I can phrase a feasibility study as "signal vs resolution × safety factor".
- [ ] I know that $\tau \sim L^{2}/\kappa$ and can apply it to heat, pressure,
      or EM fields.
- [ ] I can say which of my assumptions controls my answer, and bound it.
- [ ] I state the uncertainty of an estimate rather than implying precision.
