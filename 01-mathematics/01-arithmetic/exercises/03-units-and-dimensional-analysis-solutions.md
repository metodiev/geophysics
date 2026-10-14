# Solutions — 01-01-03 Units, SI Conventions and Dimensional Analysis

> Attempt the exercises first. Every numeric value below was computed and
> checked. Where an answer is a judgement call, that is stated.

---

## ★1 — SI base units

| | Quantity | Unit | In base units |
|---|---|---|---|
| (a) | Force | newton (N) | $\mathrm{kg\,m\,s^{-2}}$ |
| (b) | Pressure, stress | pascal (Pa) | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| (c) | Energy, work | joule (J) | $\mathrm{kg\,m^{2}\,s^{-2}}$ |
| (d) | Power | watt (W) | $\mathrm{kg\,m^{2}\,s^{-3}}$ |

**How to derive these rather than recall them.** Start from a defining relation:

- $F = ma$: $[\text{N}] = \mathrm{kg}\cdot\mathrm{m\,s^{-2}}$.
- $p = F/A$: $\mathrm{kg\,m\,s^{-2}} / \mathrm{m^{2}} = \mathrm{kg\,m^{-1}\,s^{-2}}$.
- $W = Fd$: $\mathrm{kg\,m\,s^{-2}}\cdot\mathrm{m} = \mathrm{kg\,m^{2}\,s^{-2}}$.
- $P = W/t$: $\mathrm{kg\,m^{2}\,s^{-2}}/\mathrm{s} = \mathrm{kg\,m^{2}\,s^{-3}}$.

**Pattern worth noticing.** Pressure and energy *density* share units. Pressure is
$\mathrm{kg\,m^{-1}\,s^{-2}}$; energy density (energy per unit volume) is

$$\frac{\mathrm{kg\,m^{2}\,s^{-2}}}{\mathrm{m^{3}}} = \mathrm{kg\,m^{-1}\,s^{-2}},$$

**identical to pressure.** So pressure *is* energy density, dimensionally. This
is not a naming coincidence but a physical identity, and it is why a seismic
energy density can legitimately be quoted in pascals.

---

## ★2 — Conversions

| | Given | Conversion | Result |
|---|---|---|---|
| (a) | 250 mGal | $\times10^{-5}$ | $2.50\times10^{-3}\ \mathrm{m\,s^{-2}}$ |
| (b) | 45 000 nT | $\times10^{-9}$ | $4.5\times10^{-5}\ \mathrm{T}$ |
| (c) | 3.2 g/cm³ | $\times10^{3}$ | $3.2\times10^{3}\ \mathrm{kg\,m^{-3}}$ |
| (d) | 65 mW/m² | $\times10^{-3}$ | $6.5\times10^{-2}\ \mathrm{W\,m^{-2}}$ |

**Magnitude checks (do these every time):**

- (a) 250 mGal is a large but plausible *regional* gravity anomaly. In SI it must
  be small ($\sim10^{-3}$), because 1 m/s² is enormous compared with gravity
  anomalies. ✓
- (b) 45 000 nT is a typical total field strength, and $4.5\times10^{-5}$ T sits
  comfortably inside the 25 000–65 000 nT = $2.5$–$6.5\times10^{-5}$ T range. ✓
- (c) 3.2 g/cm³ is a typical crustal rock density; 3200 kg/m³ is
  $\sim1.2\times$ the 2700 kg/m³ anchor and entirely plausible for a mafic rock. ✓
- (d) 65 mW/m² is a typical continental heat flow, and it lies inside the
  60–90 mW/m² anchor range. ✓

**Every one of these checks used the anchor table from lesson 02.** That is the
point of memorising anchors.

---

## ★3 — Dimensional check of $v = \sqrt{g\lambda/(2\pi)}$

**Check.** $[g] = \mathrm{L\,T^{-2}}$ and $[\lambda] = \mathrm{L}$, so

$$[g\lambda] = \mathrm{L^{2}\,T^{-2}} \quad\Longrightarrow\quad
\left[\sqrt{g\lambda}\right] = \mathrm{L\,T^{-1}} = [v].$$

**Balanced.** ✓ (The $2\pi$ is dimensionless, as required.)

**What it describes.** This is the **deep-water phase speed of a surface gravity
wave** in a fluid — a relation you will meet in tsunami physics, oceanography,
and surface-wave seismology. At depth $h \gg \lambda$ the wave does not feel the
bottom, so the only available parameters are $g$ and $\lambda$, and dimensional
analysis forces the form $v \propto \sqrt{g\lambda}$ up to a dimensionless
constant that this method cannot supply.

**Numerical check.** For a tsunami in the deep ocean, the *long-wavelength*
limit differs, but test the estimate with $\lambda = 200$ m:

$$v \approx \sqrt{\frac{9.81 \times 200}{2\pi}} = \sqrt{\frac{1962}{6.283}}
= \sqrt{312} \approx 17.7\ \mathrm{m\,s^{-1}}.$$

Ocean swell with a 200 m wavelength travelling at ~18 m/s is entirely realistic —
good swell at a surf beach. ✓

**The lesson.** Dimensional analysis gave the *form*; it could not give the
$2\pi$. That constant had to come from solving the fluid equations
(see [02-physics](../../../02-physics/03-oscillations-and-waves/README.md)).

---

## ★★4 — Is $Q$ dimensionless, and is the attenuation exponent?

**Part 1.** $Q = 2\pi E_{\text{stored}}/E_{\text{dissipated}}$ is a ratio of two
energies. Both have dimension $\mathrm{M\,L^{2}\,T^{-2}}$, so the ratio is

$$[Q] = \frac{\mathrm{M\,L^{2}\,T^{-2}}}{\mathrm{M\,L^{2}\,T^{-2}}} = 1.$$

**$Q$ is dimensionless.** ✓ This is why $Q$ is quoted as a bare number, and why
it is a *material property* rather than a scale-dependent quantity.

**Part 2.** The exponent is $\pi f x/(Qv)$. Since $Q$ and $\pi$ are
dimensionless, check $fx/v$:

$$[f] = \mathrm{T^{-1}},\quad [x] = \mathrm{L},\quad [v] = \mathrm{L\,T^{-1}},$$

$$\left[\frac{fx}{v}\right]
= \frac{\mathrm{T^{-1}\cdot L}}{\mathrm{L\,T^{-1}}}
= \mathrm{T^{-1}\cdot L \cdot L^{-1} \cdot T}
= 1.$$

**Dimensionless.** ✓

**Why this matters physically.** Because the argument of an exponential *must* be
dimensionless, the form
$A = A_0\exp(-\pi f x/(Qv))$ is the only possibility consistent with the physics:
the amplitude ratio can depend only on how many wavelengths the wave has
travelled. Indeed $\pi f x/(Qv) = \pi x/(Q\lambda)$ where $\lambda = v/f$ is the
wavelength, so attenuation is governed by **distance measured in wavelengths
divided by $Q$**. That is a genuine physical insight obtained from a dimensional
argument.

**Numerical feel.** With $Q = 100$, one wavelength of travel reduces amplitude by
a factor $\exp(-\pi/100) \approx 0.969$ — about 3% per wavelength. High-$Q$ rock
($Q \sim 1000$) loses only 0.3% per wavelength. This is why seismic waves
propagate tens of wavelengths before becoming unrecognisable.

---

## ★★5 — Dimensions of gravitational potential

**Part 1.** $V = -GM/r$:

$$[V] = \frac{[\mathrm{G}][\mathrm{M}]}{[\mathrm{L}]}
= \frac{\mathrm{L^{3}M^{-1}T^{-2}\cdot M}}{\mathrm{L}}
= \mathrm{L^{2}\,T^{-2}}.$$

**Part 2.** $g = -\nabla V$, so $[g] = [V]/[\text{length}] =
\mathrm{L^{2}\,T^{-2}}/L = \mathrm{L\,T^{-2}}$ ✓ — correct acceleration
dimensions.

**Part 3 — why potential is energy per unit mass.** Energy per unit mass is

$$\frac{[\text{energy}]}{[\text{mass}]}
= \frac{\mathrm{M\,L^{2}\,T^{-2}}}{\mathrm{M}} = \mathrm{L^{2}\,T^{-2}},$$

**identical to $[V]$.** So gravitational potential *is* energy per unit mass;
the units agree because the physics agrees.

**Why this is worth knowing.** It gives you an instant way to check any potential
in any context — gravitational, electric, or a scalar potential introduced in EM
modelling. If a quantity called "potential" does not come out as $\mathrm{L^2T^{-2}}$
(gravitational) or $\mathrm{M\,L^{2}\,T^{-3}\,A^{-1}}$ (electric), something is
wrong. It also explains the useful fact that a potential difference in
$\mathrm{m^{2}\,s^{-2}}$ can be converted to an equivalent height by dividing by
$g$: this is the **geopotential metre** used in geodesy
([07-gravity-geodesy](../../../07-gravity-geodesy/README.md)).

---

## ★★6 — Magnetotelluric impedance

**Given.** $E$ in $\mathrm{V\,m^{-1}}$, $H$ in $\mathrm{A\,m^{-1}}$.

**Step 1 — volts in base units.** $V = W/A$ (power over current), and
$W = \mathrm{kg\,m^{2}\,s^{-3}}$, so

$$[\mathrm{V}] = \mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}.$$

**Step 2 — electric field.** $E = V/d$, so

$$[\mathrm{V\,m^{-1}}] = \mathrm{kg\,m\,s^{-3}\,A^{-1}}.$$

**Step 3 — impedance.**

$$[Z] = \frac{[\mathrm{V\,m^{-1}}]}{[\mathrm{A\,m^{-1}}]}
= \frac{\mathrm{kg\,m\,s^{-3}\,A^{-1}}}{\mathrm{A\,m^{-1}}}
= \mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}.$$

**Step 4 — identify with the ohm.** $R = V/I$, so

$$[\Omega] = \frac{\mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}}{\mathrm{A}}
= \mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}.$$

**They agree.** ✓ The impedance of an electromagnetic wave in a medium is
dimensionally the same as electrical resistance — and physically, too: both
measure the ratio of a "driving" field to the resulting "flow".

**Application.** MT impedance is quoted in Ω, and the apparent resistivity is

$$\rho_a = \frac{|Z|^{2}}{\mu_0 \omega} \ \ [\Omega\cdot\mathrm{m}].$$

You can check this dimensionally: $[Z^{2}] = \mathrm{kg^{2}m^{4}s^{-6}A^{-4}}$,
$[\mu_0\omega] = \mathrm{kg\,m\,A^{-2}s^{-2}}\cdot\mathrm{s^{-1}}
= \mathrm{kg\,m\,A^{-2}s^{-3}}$, and the ratio is
$\mathrm{kg\,m^{3}\,s^{-3}\,A^{-2}}$ — which is
$\mathrm{L^{3}M\,T^{-3}I^{-2}}$, the dimensions of $\Omega\cdot\mathrm{m}$. ✓
Development in
[08-04 Electromagnetic Induction](../../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md).

---

## ★★7 — Viscous relaxation timescale

### (a) The two groups have different dimensions

**Group 1: $\eta/(\rho g L)$.**

$$[\eta] = \mathrm{M\,L^{-1}\,T^{-1}}, \qquad
[\rho g L] = \mathrm{M\,L^{-3}}\cdot\mathrm{L\,T^{-2}}\cdot\mathrm{L}
= \mathrm{M\,L^{-1}\,T^{-2}}.$$

$$\left[\frac{\eta}{\rho g L}\right]
= \frac{\mathrm{M\,L^{-1}\,T^{-1}}}{\mathrm{M\,L^{-1}\,T^{-2}}}
= \mathrm{T}.$$

**Dimensions of time.** ✓

**Group 2: $\eta/(\rho g L^{2})$.**

$$[\rho g L^{2}] = \mathrm{M\,L^{-3}}\cdot\mathrm{L\,T^{-2}}\cdot\mathrm{L^{2}}
= \mathrm{M\,T^{-2}},$$

$$\left[\frac{\eta}{\rho g L^{2}}\right]
= \frac{\mathrm{M\,L^{-1}\,T^{-1}}}{\mathrm{M\,T^{-2}}}
= \mathrm{L^{-1}\,T}.$$

**Not dimensionless and not a time** — it has dimensions of
$\mathrm{T/L}$, i.e. inverse velocity. The two groups differ by one power of
length, which changes the dimensions from time to inverse velocity. **This is
exactly the kind of subtle error dimensional analysis exists to catch**, and it
is why the exercise warned you.

### (b) Numerical evaluation

With $\eta = 10^{21}\ \mathrm{Pa\,s}$, $\rho = 3300\ \mathrm{kg\,m^{-3}}$,
$g = 10\ \mathrm{m\,s^{-2}}$, so $\rho g = 3.3\times10^{4}$:

| $L$ | $\eta/(\rho g L)$ | In years (verified) |
|---|---|---|
| 1 km ($10^{3}$ m) | $3.03\times10^{13}$ s | $\approx 9.6\times10^{5}$ yr |
| 100 km ($10^{5}$ m) | $3.03\times10^{11}$ s | $\approx 9.6\times10^{3}$ yr |
| 2000 km ($2\times10^{6}$ m) | $1.52\times10^{10}$ s | $\approx 480$ yr |

### (c) Which is relevant, and does it match observation?

**The 2000 km case is the relevant one — and it matches.** Post-glacial rebound
involves loads with horizontal extent of order $10^{3}$ km (the Fennoscandian and
Laurentide ice sheets). The estimate gives $\tau \approx 480$ yr, which is the
correct order of magnitude: observed relaxation times for these ice-sheet
histories are of order $10^{3}$–$10^{4}$ years for the upper mantle.

**Why the $L$ dependence is so strong.** $\tau \propto 1/L$ here, so a
factor-of-2000 change in $L$ gives a factor-of-2000 change in $\tau$ — five
orders of magnitude across the table. **Large loads relax much faster than small
ones**, because the driving stress (proportional to load height times $\rho g$)
scales with the load's *lateral extent* while the viscous resistance does not
scale the same way.

**A caveat you should notice.** The real Earth has a *layered* viscosity: an
elastic lithosphere over a low-viscosity asthenosphere over a higher-viscosity
lower mantle. A single-viscosity estimate is therefore a *bounding* calculation,
not a prediction. That is precisely why the formal inversion for mantle
viscosity from rebound data (see
[13-geodynamics-tectonics](../../../13-geodynamics-tectonics/README.md) and the
subsection on glacial isostatic adjustment) couples a layered Earth model to the
observed relative sea-level record across thousands of sites — a large inverse
problem built on exactly this one-line timescale.

**Observe the method.** We obtained a physically meaningful, quantitatively
useful number ($\sim500$ yr) from dimensional analysis plus one anchor value of
mantle viscosity, and we immediately identified its central limitation. That
sequence — estimate, compare, state limits — is the professional pattern.

---

## ★★8 — Geothermal gradient from heat flow

**Formula.** Fourier's law in one dimension gives $q = k\,(\mathrm{d}T/\mathrm{d}z)$,
so

$$\frac{\mathrm{d}T}{\mathrm{d}z} = \frac{q}{k}.$$

**Insert values.** $q = 72\ \mathrm{mW\,m^{-2}} = 0.072\ \mathrm{W\,m^{-2}}$,
$k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$:

$$\frac{\mathrm{d}T}{\mathrm{d}z}
= \frac{0.072}{2.5} = 0.0288\ \mathrm{K\,m^{-1}}
= 28.8\ \mathrm{K\,km^{-1}}.$$

$$\boxed{\text{gradient} \approx 29\ \mathrm{K\,km^{-1}}}$$

**Check against the anchors.** Lesson 02 listed a crustal geothermal gradient
anchor of $\sim25$ K/km and surface heat flow of 60–90 mW/m². An input of
72 mW/m² with a conductivity of 2.5 W/(m·K) gives 29 K/km — consistent with the
anchor, and inside the expected band (continental gradients are typically
20–30 K/km, higher in extensional provinces, lower in stable cratons). ✓

**Dimensional note.** $\mathrm{W\,m^{-2}}/\mathrm{W\,m^{-1}\,K^{-1}} =
\mathrm{K\,m^{-1}}$ ✓.

**Why this inverse form is used in practice.** You measure $q$ (with a
heat-flow probe) and $k$ (on a core sample), and you *infer* the gradient, which
you cannot measure directly below the shallowest borehole. This is a small
inverse problem, and it illustrates the general shape: measure a response, know
a material property, infer a state. See
[12-03 Geotherms and the Earth's Heat Budget](../../../12-global-geophysics-interior/03-geotherms-and-heat-budget/README.md).

---

## ★★★9 — Buckingham Pi: Rayleigh and Nusselt numbers

### Step 1 — list the variables and their dimensions

For convection in a layer, the relevant quantities are:

| Quantity | Symbol | Dimensions |
|---|---|---|
| Layer depth | $L$ | $\mathrm{L}$ |
| Temperature contrast | $\Delta T$ | $\Theta$ |
| Gravity | $g$ | $\mathrm{L\,T^{-2}}$ |
| Density | $\rho$ | $\mathrm{M\,L^{-3}}$ |
| Thermal expansivity | $\alpha$ | $\Theta^{-1}$ |
| Thermal diffusivity | $\kappa$ | $\mathrm{L^{2}\,T^{-1}}$ |
| Dynamic viscosity | $\eta$ | $\mathrm{M\,L^{-1}\,T^{-1}}$ |
| Specific heat capacity | $c_p$ | $\mathrm{L^{2}\,T^{-2}\,\Theta^{-1}}$ |
| Heat flux | $q$ | $\mathrm{M\,T^{-3}}$ |

### Step 2 — count and form the groups

Nine quantities in four base dimensions ($\mathrm{M}$, $\mathrm{L}$, $\mathrm{T}$,
$\Theta$) gives $9 - 4 = 5$ independent dimensionless groups. Two of them are the
physically dominant ones:

$$\mathrm{Ra} = \frac{\alpha\,\rho\,g\,\Delta T\,L^{3}}{\kappa\,\eta},
\qquad
\mathrm{Nu} = \frac{qL}{k\,\Delta T}
= \frac{\text{convective heat transport}}{\text{conductive heat transport}},$$

where $k = \rho c_p \kappa$ is the thermal conductivity. The remaining groups
involve $c_p$ and are absorbed into $\mathrm{Nu}$ and $\mathrm{Ra}$ for
incompressible convection — which is why these two numbers suffice.

**Interpretation of $\mathrm{Ra}$.** It compares the buoyancy driving force
against the two dissipative processes (thermal diffusion and viscous
resistance). It is *not* a ratio of forces but of timescales: $\mathrm{Ra} =
\tau_{\text{diffusion}}\tau_{\text{viscous}}^{-1}$ scaled appropriately.

### Step 3 — the scaling relation, and a caution about $\beta$

Convection theories and experiments relate the two by a power law

$$\mathrm{Nu} \propto \mathrm{Ra}^{\beta}.$$

**Do not assume a value of $\beta$.** Reported values depend on the
Rayleigh-number regime, boundary conditions, heating mode (bottom-heated vs
internally heated), and whether the flow is steady or time-dependent. Values
near $\beta \approx 1/3$ are frequently quoted for high-$\mathrm{Ra}$,
basal-heated convection in the "classical" scaling regime, but the literature
contains a range (roughly 0.2–0.4 for different regimes and formulations), and
some studies argue for regime transitions. **Consult and cite the primary
literature before using a specific exponent in your own work.** Reviews of
mantle convection and the "heat transport scaling" literature are the right
entry point; search *Reviews of Geophysics* and *Physics of the Earth and
Planetary Interiors*.

### Step 4 — estimate $\mathrm{Nu}$ for the mantle

Using the Rayleigh number computed in the lesson ($\mathrm{Ra} \approx
1.78\times10^{7}$) and the marginal-stability normalisation
$\mathrm{Ra}_c \approx 10^{3}$:

$$\frac{\mathrm{Ra}}{\mathrm{Ra}_c} \approx 1.78\times10^{4}.$$

Taking $\beta = 1/3$ as an illustrative value (see the caution above):

$$\mathrm{Nu} \sim \left(\frac{\mathrm{Ra}}{\mathrm{Ra}_c}\right)^{1/3}
= (1.78\times10^{4})^{1/3} \approx 26.$$

**Interpretation.** The mantle transports roughly **25–30 times more heat by
convection than conduction alone would carry**. Convection therefore dominates
mantle heat transport, which is consistent with the observed heat flow, the
existence of plate tectonics, and the temperature structure inferred from
seismology.

**Sensitivity.** Because $\beta = 1/3$, $\mathrm{Nu}$ depends only on the
*cube root* of $\mathrm{Ra}$. Our $\mathrm{Ra}$ is itself only an
order-of-magnitude estimate, but a factor-of-10 error in $\mathrm{Ra}$ changes
$\mathrm{Nu}$ by only $\sim2.15$. **This is the payoff of a fractional
exponent: the conclusion is robust to input uncertainty.** The qualitative
claim — convection dominates — is safe; the precise value 26 is not.

### Step 5 — state the limitations

1. $\mathrm{Ra}$ was computed with a single, uniform viscosity. The real mantle
   is strongly temperature-dependent in viscosity, and this changes both the
   effective $\mathrm{Ra}$ and the scaling exponent. This is a first-order issue
   in modern mantle convection, not a detail.
2. The exponent $\beta$ is regime-dependent (see Step 3).
3. Internal heating from radiogenic elements is neglected; widespread internal
   heating changes the scaling and can reduce the effective exponent.
4. The calculation assumes a planar layer; spherical geometry matters for
   global convection.

**The honest conclusion:** *the mantle is vigorously convecting and convection
dominates its heat transport, by roughly an order of magnitude — with the precise
magnitude dependent on the viscosity structure and the assumed scaling regime.*
That is a defensible scientific statement, and it is what dimensional analysis
can legitimately deliver.

---

## ★★★10 — Unit forensics on gravity gradients

### (a) Dimensions of the three units

**Eötvös.** $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$, i.e. dimensions
$\mathrm{T^{-2}}$.

**$\mathrm{s^{-2}}$.** By inspection, dimensions $\mathrm{T^{-2}}$.

**mGal/km.** mGal is an acceleration, $\mathrm{L\,T^{-2}}$; dividing by a length
gives

$$\left[\frac{\mathrm{mGal}}{\mathrm{km}}\right]
= \frac{\mathrm{L\,T^{-2}}}{\mathrm{L}} = \mathrm{T^{-2}}.$$

**All three have dimensions $\mathrm{T^{-2}}$.** ✓ They are all *spatial
gradients of gravitational acceleration*, since

$$[\nabla g] = \frac{[\text{acceleration}]}{[\text{length}]}
= \frac{\mathrm{L\,T^{-2}}}{\mathrm{L}} = \mathrm{T^{-2}}.$$

**This is the pedagogically important point.** The three units are *not*
different kinds of quantity — they are the same quantity in different clothes.
That is precisely what makes the confusion easy and the error hard to spot by
inspection. A dimensional check alone will *not* flag it; only a numerical
conversion check will.

### (b) Conversion between mGal/km and Eötvös

Work from first principles. A gradient of 1 mGal per 1 km is
$10^{-5}\ \mathrm{m\,s^{-2}}$ per $10^{3}$ m:

$$\frac{10^{-5}}{10^{3}} = 10^{-8}\ \mathrm{s^{-2}}.$$

In Eötvös, dividing by $10^{-9}$:

$$\boxed{1\ \mathrm{mGal\,km^{-1}} = 10\ \mathrm{\acute{E}tv\ddot{o}s}}
\ \text{(verified)}.$$

Equivalently, $1\ \mathrm{E} = 0.1\ \mathrm{mGal\,km^{-1}}$.

### (c) Is Paper C consistent?

- Papers A and B: 2.4 Eötvös $= 2.4\times10^{-9}\ \mathrm{s^{-2}}$ ✓ **they
  agree.**
- Paper C: 24 mGal/km $= 24 \times 10^{-8} = 2.4\times10^{-7}\ \mathrm{s^{-2}}$
  $= \mathbf{240}$ **Eötvös** (verified).

$$\frac{2.4\times10^{-7}}{2.4\times10^{-9}} = 100.$$

**Paper C is a factor of 100 larger than Papers A and B.** Note the trap:
$24$ versus $2.4$ looks like a factor of 10, and the remaining factor of 10 comes
from the unit conversion. **A superficial comparison of the leading numbers finds
only one of the two factors of ten.**

**Also note the equivalent direction:** 2.4 Eötvös $= 0.24$ mGal/km (verified).
So if Paper C had reported 0.24 mGal/km it would have been consistent.

### (d) Likely origin, and a referee's response

**Most likely origin.** A conversion slip involving the Gal–mGal factor
($1\ \mathrm{Gal} = 10^{3}\ \mathrm{mGal}$), or a mistyped Eötvös definition —
for instance treating $1\ \mathrm{E}$ as $10^{-7}\ \mathrm{s^{-2}}$ instead of
$10^{-9}\ \mathrm{s^{-2}}$. Both are ordinary unit-slip errors, and both are
invisible to dimensional analysis because the dimensions are *correct* in all
three papers.

**Referee's comment:**

> "Papers A and B report the same gradient as 2.4 Eötvös and
> $2.4\times10^{-9}$ s⁻², which are consistent. Paper C's value of 24 mGal/km
> converts to 240 Eötvös, a factor of 100 larger, and therefore appears to be
> inconsistent with the other two. All three units have dimensions of
> $\mathrm{T^{-2}}$ (they are all spatial gradients of gravity), so this
> discrepancy will not be caught by a dimensional check. Please confirm which
> value is correct and state the unit conversion explicitly, since at least one
> of the three reports is in error."

**The methodological lesson.** Dimensional analysis is necessary but not
sufficient. It catches errors of *form*. It cannot catch errors of *magnitude
within a shared dimension* — and those are exactly the errors that unit
conventions, with their many non-SI units, make easy to commit. The remedy is
(a) always show your conversion factors explicitly, and (b) sanity-check
magnitudes against known ranges, as in ★2.

---

## Self-assessment

- [ ] I can state the seven SI base quantities and their defining constants.
- [ ] I can convert mGal ↔ Gal ↔ m/s² ↔ µm/s², and nT ↔ T ↔ G ↔ γ, from memory.
- [ ] I can dimensionally check any equation and say what class of error a
      failure indicates.
- [ ] I can explain why dimensional analysis cannot detect a wrong dimensionless
      constant, with an example.
- [ ] I can identify the controlling dimensionless group in a convection
      problem and say why it governs behaviour.
- [ ] I know that units sharing dimensions can still differ by orders of
      magnitude, so I check magnitudes against anchors.
