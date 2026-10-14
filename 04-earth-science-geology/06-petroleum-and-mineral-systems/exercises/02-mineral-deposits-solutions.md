# Solutions — 04-06-02 Mineral Deposit Types and Their Geophysical Signatures

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

Every anomaly below is a **model result** for a stated geometry with a
**nominal** property contrast. No grade, tonnage or contained-metal figure is
stated anywhere.

---

## ★1 — Magnetic sphere

**(a)** $H = B/\mu_0 = 52\,000\times10^{-9}/(4\pi\times10^{-7}) =
41.38$ A m⁻¹.

**(b)** $m = k\,H\,(4/3)\pi a^{3}
= (0.05)(41.38)(4.18879)(3.375\times10^{6}) = 2.925\times10^{7}$ A m².

**(c)** At $x = 0$, $\Delta Z = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= (10^{-7})(2)(2.925\times10^{7})/(2.7\times10^{7}) = 2.167\times10^{-7}$ T
$= 216.7$ nT.

**(d)** The zero crossing is at $x = \sqrt2\,z = 424.3$ m. It is **independent of
both** $k$ and $a$, because the shape function $(2-u^{2})/(1+u^{2})^{5/2}$ with
$u = x/z$ contains only the geometry: amplitude and width are decoupled, and the
width alone gives the depth.

---

## ★2 — Gravity sphere

**(a)** $\Delta g(0) = G\,\Delta\rho\,(4/3)\pi a^{3}/z^{2}
= (6.674\times10^{-11})(800)(4.18879)(3.375\times10^{6})/(9\times10^{4})
= 8.387\times10^{-6}$ m s⁻² $= 0.839$ mGal.

**(b)** At 600 m, $z^{2}$ is four times larger, so
$\Delta g = 0.2097$ mGal.

**(c)** Ratio $= 4.000$, so $\Delta g \propto z^{-2}$ at fixed mass and
$\propto z^{-3}$ at fixed *density contrast and size*. Both statements are used,
and confusing them is a standard error.

**(d)** Because the anomaly falls as the cube of depth for a given body, doubling
the depth reduces the signal by a factor of eight; instrument sensitivity improves
by factors, not by orders of magnitude, so it cannot rescue a deep small target.
What changes the answer is a *larger* body or a *larger* contrast.

---

## ★3 — Reflection coefficient at an ore contact

**(a)** $Z_\mathrm{ore} = 4000 \times 5800 = 2.320\times10^{7}$
kg m⁻² s⁻¹; $Z_\mathrm{host} = 2700 \times 5400 = 1.458\times10^{7}$.

**(b)** $R = (2.320 - 1.458)/(2.320 + 1.458) = 0.862/3.778 = +0.2282$.

**(c)** $R^{2} = 0.0521$, i.e. **5.2 per cent** of the incident energy — against
about 0.25 per cent for a deep crustal reflection, so a factor of 20 in energy.

**(d)** $R$ is **positive**, so the ore is the higher-impedance unit: on a
normal-polarity section it appears as a **peak** (a hard event) rather than a
trough, the opposite of the gas-sand case of
[lesson 01](./01-petroleum-system-solutions.md).

---

## ★★4 — Conductivity bounds

**(a)** With $\sigma_1 = 10^{-3}$, $\sigma_2 = 10^{3}$ and $f_2 = 0.05$, the
Hashin–Shtrikman bounds are

$$\sigma_- = 1.158\times10^{-3}\ \mathrm{S\,m^{-1}},
\qquad
\sigma_+ = 33.90\ \mathrm{S\,m^{-1}}.$$

**(b)** At $f_2 = 0.30$:
$\sigma_- = 2.286\times10^{-3}$ S m⁻¹ and $\sigma_+ = 222.2$ S m⁻¹.

**(c)** Reciprocal resistivities: at $f_2 = 0.05$, 863.6 Ω m (lower) and
0.0295 Ω m (upper); at $f_2 = 0.30$, 437.5 Ω m and 0.0045 Ω m.

**(d)** The bounds differ by four to five orders of magnitude because the two
extremes represent **different connectivities**: the lower bound corresponds to
isolated sulphide inclusions in a resistive matrix, the upper bound to a rock in
which the sulphide itself forms the continuous phase. At a few per cent sulphide
the upper geometry is impossible, so a real disseminated deposit sits near the
lower bound and a massive or stringer deposit moves towards the upper one. This
is why **connectivity, not abundance, controls the electromagnetic response**.

---

## ★★5 — Placer density and anomaly

**(a)** With $\phi = 0.35$:
$f = 0$: $\rho = 0.35(1000) + 0.65(2650) = 350 + 1722.5 = 2072.5$ kg m⁻³.
$f = 0.10$: $\rho = 350 + 0.65[0.10(4600) + 0.90(2650)] = 350 + 0.65(460 + 2385)
= 350 + 1849.25 = 2199.3$ kg m⁻³.

**(b)** $\Delta\rho = 2199.3 - 2072.5 = 126.8$ kg m⁻³.

**(c)** $g = 2\pi G\Delta\rho\,t = 2\pi(6.674\times10^{-11})(126.8)(10)
= 5.315\times10^{-7}$ m s⁻² $= 0.0532$ mGal.

**(d)** Ilmenite is **weakly magnetic** (and magnetite in the same assemblage is
strongly magnetic), so the assemblage changes the **susceptibility** as well as
the density. The second method is therefore **magnetics**, and in practice it is
the first method applied, because the susceptibility contrast is usually the
larger signal.

---

## ★★6 — Half-width depth rule

**(a)** $z = 1.997\,x_{1/2} = 1.997(200) = 399.4$ m, so about 400 m to the centre.

**(b)** The zero crossing is at $\sqrt2\,z = 564.8$ m.

**(c)** The dipole (point-source) approximation requires $z \gtrsim 3a$, i.e. the
body radius must be less than about a third of the depth. If the anomaly's
amplitude implies a large $a$ that violates this, the rule underestimates the
depth and a finite-body forward model is required.

**(d)** Because the shape function depends only on $x/z$. The amplitude fixes the
product $k\,a^{3}$ (the moment) and the width fixes $z$; the two are separate
observations, so a *depth* can be obtained from a survey with no independent
knowledge of the magnetisation, which is exactly what makes magnetics useful in
reconnaissance over unknown geology.

---

## ★★★7 — Reading the demonstration

Quoted output from `mineral_deposits_demo.py`:

**(a)** $m = 1.6667\times10^{7}$ A m²; peak $416.7$ nT; zero crossing
$282.8$ m.

**(b)** $u = 0.500683$; the half-maximum lies at $0.5007\,z$, so
$z = 1.9973\,x_{1/2}$; the recovered depth is exactly the 200 m input.

**(c)** $\Delta\rho = 1500$: 1.048 mGal; 900: 0.629 mGal; 150: 0.105 mGal;
$-400$: $-0.280$ mGal.

**(d)** $z = 300$ m: 0.466 mGal and 123.5 nT. $z = 500$ m: 0.168 mGal and
26.7 nT. $z = 1000$ m: 0.042 mGal and 3.3 nT. $z = 2000$ m: 0.010 mGal and
0.4 nT. The dipole formulas are accurate only for $z \gtrsim 3a$, so the 300 m row
(with $a = 100$ m) is at the edge of validity and the 2000 m row is well inside
it.

**(e)** Host volcanic $Z = 15.125$ MRayl; massive sulphide $R = +0.2498$; skarn
$+0.1192$; banded iron formation $+0.1729$; mafic intrusion $+0.1187$.

**(f)** $f = 0.01$: $\sigma$ from $1.0303\times10^{-3}$ to $6.690$ S m⁻¹;
0.05: $1.1579\times10^{-3}$ to 33.90; 0.10: $1.3333\times10^{-3}$ to 68.97;
0.20: $1.7500\times10^{-3}$ to 142.9; 0.40: $3.000\times10^{-3}$ to 307.7.

**(g)** The demo's placer section uses a porosity of 0.30, giving 2155.0 kg m⁻³ at
$f = 0$; $f = 0.05$ gives $\Delta\rho = +89.2$, $f = 0.20$ gives
$\Delta\rho = +357.0$, and a 20 m thick layer at $f = 0.20$ gives $0.299$ mGal
(0.075 mGal for the same contrast at 5 m).

**(h)** The sphere anomalies, the half-width rule and the reflection coefficients
are **exact consequences of the stated formulas** for the stated geometry. The
Hashin–Shtrikman results are **variational bounds** that hold for any geometry and
therefore constrain rather than predict. The densities, velocities,
conductivities, the inducing field and the susceptibility are **nominal literature
values** entering as inputs; change any of them and every computed number changes,
with the anomalies scaling linearly in the contrast and cubically in the depth.

---

## ★★★8 — Interpretation and its limits

**(a)** Expected pattern:

| Zone | Magnetics | Radiometrics (K) | IP (chargeability) |
|---|---|---|---|
| Potassic core | **High** (magnetite added) | **High** (K-feldspar, biotite) | Low to moderate |
| Phyllic shell | **Low** (magnetite destroyed) | Low | **High** (pyrite added) |
| Propylitic outer | Neutral to slightly low | Low to moderate | Low |

The single most misleading anomaly if interpreted alone is the **magnetic high of
the core**: it is a genuine part of the system, but it marks the potassic
alteration, and the ore in many porphyries sits at the margin between the
potassic and phyllic zones where the sulphide and the magnetite-destructive
alteration meet. Interpreting the magnetic high as "the ore" puts the drill hole
in the wrong place, systematically and confidently.

**(b)** At 20 m thick and 100 m across, at 150 m depth:

- **EM** is the best candidate, because the target's *conductance* (conductivity
  times thickness) is what the method responds to, and the sulphide conductivity
  contrast is one to three orders of magnitude. A thin but very conductive body
  is still a strong EM target.
- **Gravity** would need a detectable mass. With $\Delta\rho = 1500$ kg m⁻³ and a
  slab-equivalent of 20 m over 100 m, the anomaly is of order tens of microgal —
  small for a surface survey without a very well-constrained regional field.
- **Seismic** requires the body to be thick relative to the wavelength. At
  150 m depth with a 30 m dominant wavelength, a 20 m body is near or below the
  tuning limit, so it would appear as an amplitude or travel-time anomaly rather
  than a discrete reflection.

**(c)** Two explanations for a reversed apparent polarity:

1. **Strong remanent magnetisation** that is not parallel to the present field —
   common in rocks magnetised during a reversed-polarity interval or in strongly
   magnetised pyrrhotite-bearing rocks. Discriminating observation: a palaeomagnetic
   measurement on a sample, or an anomaly shape that cannot be fitted by
   induced-only modelling at any susceptibility.
2. **An incorrect removal of the regional field**, which can leave a residual with
   the wrong sign or the wrong shape. Discriminating observation: re-derive the
   anomaly with a different, physically justified regional, and check whether the
   reversal survives.

**(d)** The laterite profile: a fresh ultramafic rock (dense, low porosity) at
depth, a saprolite above it (hydrous, porous, therefore **low density and low
resistivity**) and a ferruginous cap at the surface (dense, resistive, magnetic).
Gravity therefore shows a **relative low** over thick saprolite, and resistivity
shows a **conductor**; both are inverted to give the thickness of the weathered
zone, which is the *host* of nickel in a laterite deposit. The exploration target
for nickel is the **saprolite**, not the ferruginous cap — the cap is the residue
that has lost the elements of interest.
