# Solutions — 12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite

Worked solutions for
[05-core-mantle-boundary-exercises.md](./05-core-mantle-boundary-exercises.md).
The lesson is
[05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](../05-core-mantle-boundary.md).
All models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — The two faces of the CMB

**(a) SH.** $Z_\text{mantle} = 5.57 \times 7.26 = 40.438$,
$Z_\text{core} = 9.90 \times 0 = 0$, so

$$R = \frac{0 - 40.438}{0 + 40.438} = -1.0000.$$

Exactly −1: total reflection with polarity reversal, at every frequency, for any
core density. The reason is that a fluid has no shear modulus, so its S impedance
is identically zero — this is not an approximation but a statement about
constitutive behaviour.

**(b) P.** $Z_\text{mantle} = 5.57 \times 13.72 = 76.420$,
$Z_\text{core} = 9.90 \times 8.06 = 79.794$, so

$$R = \frac{79.794 - 76.420}{79.794 + 76.420} = \frac{3.374}{156.214} = +0.0216.$$

With $\rho_\text{core} = 10.50$: $Z_\text{core} = 84.630$, giving

$$R = \frac{84.630 - 76.420}{84.630 + 76.420} = \frac{8.210}{161.050} = +0.0510.$$

A denser core **increases** the P contrast by a factor of 2.4, so the boundary
becomes *less* transparent to P. Note the asymmetry: the P reflection coefficient is
a *measurable* number that depends on the core's density, while the S coefficient is
pinned at −1 and carries no information about density at all. The densest part of
the Earth is therefore constrained from the *P* side.

### ★2 — The postcursor delay

$$v_s' = 7.26 \times (1 - 0.15) = 6.171\ \mathrm{km\,s^{-1}},$$
$$\delta t = 2 \times 18 \times \left(\frac{1}{6.171} - \frac{1}{7.26}\right)
= 36 \times (0.162048 - 0.137741) = 36 \times 0.024307 = 0.875\ \mathrm{s}.$$

Units: $h$ in km, the bracket in s km$^{-1}$, so the product is in seconds. A useful
habit: the bracket is a *slowness difference*, and it is small — here
0.0243 s km$^{-1}$ — which is why centimetre-scale velocity differences are
resolvable but kilometres of thickness are not.

### ★3 — D'' thickness from a pressure difference

$$h_{D''} = \frac{\Delta P}{\rho g}
= \frac{12.0\ \mathrm{GPa}}{59.38\ \mathrm{MPa\,km^{-1}}}
= \frac{12\,000}{59.38} = 202.1\ \mathrm{km}.$$

(A GPa is 1000 MPa, so the conversion is $12.0 \times 1000/59.38$.) The result is a
*depth below the CMB*, and it is meaningful only as long as the geotherm actually
reaches the transition pressure: if $C$ were negative the layer would not exist at
all.

---

## ★★ Applied

### ★★4 — The $(h,\delta)$ family behind 1.800 s

Solve $1.800 = 2h\left(1/v_s' - 1/7.26\right)$ for each $h$:

| $h$ (km) | $\delta$ (%) | $v_s'$ (km s$^{-1}$) |
|---|---|---|
| 10 | 39.52 | 4.391 |
| 20 | 24.63 | 5.472 |
| 30 | 17.88 | 5.962 |
| 40 | 14.04 | 6.241 |

**What a mineral physicist rejects.** A 40 % shear-velocity reduction is far beyond
what any plausible assemblage at CMB pressures and temperatures can produce — a
factor-of-two change in $v_s$ would require near-melting of the rock at the
*top* of the layer while remaining solid below, which is a strong dynamical
constraint in itself. So the 10 km/40 % end of the family is ruled out not by
seismology but by mineral physics, and the seismic answer must be reported as the
surviving range (roughly 20–40 km, 14–25 %). This is the practical division of
labour: **seismology gives the family, mineral physics prunes it.**

### ★★5 — Shut-off temperatures and the $\gamma$ lever

$$T_\text{thresh} = T_\text{ref} + \frac{C}{\gamma}
= 2600 + \frac{12\,000}{\gamma}\ \text{K}:$$

| $\gamma$ (MPa K$^{-1}$) | $C/\gamma$ (K) | $T_\text{thresh}$ (K) |
|---|---|---|
| 7 | 1714 | 4314 |
| 8 | 1500 | 4100 |
| 9 | 1333 | 3933 |

The plausible range spans **3933–4314 K**, a spread of **380 K** from a ±12 %
change in $\gamma$. Note the direction: a *steeper* Clapeyron slope means the
transition pressure rises faster with temperature, so the switch-off happens at a
*lower* temperature. Observing "D'' is absent here" therefore says only that
$T_\text{CMB} > T_\text{thresh}$, and turning that inequality into a temperature
requires $\gamma$.

### ★★6 — A 12 s delay converted to thickness

$$h = \frac{v_s\,\Delta t}{2}
= \frac{7.26 \times 12.0}{2} = 43.56\ \mathrm{km}.$$

With a velocity 2 % lower ($v_s = 7.115$): $h = 42.69$ km; with 3 % lower
($v_s = 7.042$): $h = 42.25$ km. So a 3 % velocity error is a 3 % thickness error —
small in relative terms, but systematic: it applies to every measurement in a study
in the same direction, so it does not average out. Report the thickness as
"43.6 km for the stated velocity model; approximately 3 % smaller for every 3 %
lower average $v_s$ above the boundary."

The deeper issue is that the *same* systematic error also moves the reference CMB
depth, since the whole path length is converted with the same model; the errors are
correlated and partially cancel. That cancellation is a reason to prefer
*differential* measurements (D'' reflection minus CMB reflection) rather than
absolute ones, exactly as the lesson's delay formula does.

### ★★7 — A thickness bound as a constraint on $\delta$

Solve the delay relation for $\delta$ given $h$ and $\delta t = 0.90$ s:

$$\frac{1}{v_s'} = \frac{1}{v_s} + \frac{\Delta t}{2h}
\;\Longrightarrow\;
v_s' = \left(\frac{1}{7.26} + \frac{0.90}{2h}\right)^{-1},\qquad
\delta = 1 - \frac{v_s'}{7.26}.$$

| $h$ (km) | $v_s'$ (km s$^{-1}$) | $\delta$ (%) |
|---|---|---|
| 5 | 4.391 | 39.52 |
| 8 | 5.155 | 29.00 |
| 10 | 5.472 | 24.63 |
| 12 | 5.706 | **21.40** |

The upper bound of 12 km therefore implies $\delta \ge$ **21.4 %** — a *lower*
bound on the velocity reduction, and a strong one. The corresponding density
change, under the demonstration's parametrisation $\rho' = \rho(1 + 1.30\delta)$,
is $1 + 1.30 \times 0.214 = 1.278$, i.e. a **28 % density increase**. That is a
physically demanding requirement — a slow *and* dense layer at the base of the
mantle — and this is exactly the argument used to say that ULVZs must be
chemically distinct from the surrounding mantle rather than merely hot. Note the
logic: the bound converts a *thickness* limit into a *composition* limit.

---

## ★★★ Research-oriented

### ★★★8 — Energy conservation with attenuation

A lossy layer is modelled by a complex velocity,
$v \to v\left(1 + i/2Q\right)$, which makes the layer's impedance complex and the
reflection coefficient non-unimodular: $|R(f)| = e^{-\pi f t_\text{two-way}/Q}$
for a two-way time $t$ inside the attenuating layer. The energy ratio of the
reflected pulse to the lossless case is then, to good approximation, the square of
that factor evaluated at the dominant frequency:

| $t_\text{2-way}$ (s) | $\lvert R\rvert$ at $f = 0.08$ Hz, $Q = 100$ | energy ratio |
|---|---|---|
| 3.0 | 0.9925 | 0.985 |
| 12.0 | 0.9703 | 0.941 |

So a $Q = 100$ layer 12 s thick in two-way time removes about **6 % of the
reflected energy**, while a 3 s layer removes 1.5 %. Two consequences:

1. **The measured quantity is now two numbers, not one.** The delay gives
   $2h(1/v'-1/v)$ and the energy deficit gives $2hf/Qv'$ — two equations in
   $(h, v', Q)$. If $Q$ is assumed (from laboratory or other data), the degeneracy
   of the lossless case is broken; if $Q$ is a third unknown, no new information is
   gained and the problem is worse.
2. **The frequency dependence is a second lever.** Since the energy deficit grows
   with $f$, comparing two frequency bands separates the *layer thickness* (a time
   shift, nearly frequency-independent) from the *attenuation* (an amplitude effect
   growing with frequency). This is the same logic that makes spectral studies
   useful in any attenuating medium.

### ★★★9 — Sensitivity of the shut-off temperature, and the best test

$$T_\text{thresh} = T_\text{ref} + \frac{C}{\gamma}
\;\Longrightarrow\;
\frac{\mathrm{d}T_\text{thresh}}{\mathrm{d}\gamma} = -\frac{C}{\gamma^{2}}.$$

At $C = 10\ \mathrm{GPa} = 10^{10}$ Pa and
$\gamma = 8\ \mathrm{MPa\,K^{-1}} = 8\times10^{6}$ Pa K$^{-1}$:

$$\frac{\mathrm{d}T_\text{thresh}}{\mathrm{d}\gamma}
= -\frac{10^{10}}{\left(8\times10^{6}\right)^{2}}
= -1.5625\times10^{2}\ \mathrm{K\ per\ MPa\,K^{-1}}$$

i.e. **−156 K per MPa K$^{-1}$**. Because the derivative scales as $1/\gamma^{2}$,
the constraint is *weakest* where $\gamma$ is largest: at $\gamma = 4$ the
derivative is −625 K per MPa K$^{-1}$, so the same observational uncertainty in
temperature translates into a much tighter constraint on $\gamma$.

**The best observational test.** The strongest constraint comes not from the
*thickness* but from the *presence or absence* of the discontinuity, because
presence/absence is a binary outcome that maps directly onto an inequality
$T_\text{CMB} \gtrless T_\text{thresh}$. The design:

- **measure** whether a D'' discontinuity exists in regions whose CMB temperature
  is independently estimated (from tomography, converted to temperature with its
  own sensitivity);
- **what else must be known**: $C$, the pressure offset of the transition above the
  CMB pressure at the reference temperature — which is a mineral-physics output, and
  is itself uncertain by several GPa;
- **residual ambiguity**: even a perfect binary map yields only the ratio $C/\gamma$
  and hence a *line* in the $(C,\gamma)$ plane. Breaking that requires an
  independent determination of $\gamma$ (from experiments or computations) or of
  $C$ (from an independent thermometric constraint on one region). Quantitatively:
  a ±3 GPa uncertainty in $C$ translates to ±375 K in $T_\text{thresh}$ at
  $\gamma = 8$, comparable to the ±380 K from the $\gamma$ range of exercise ★★5.

The honest conclusion: **the D'' discontinuity is a thermometer only for
temperature *differences* between regions, not for absolute temperatures** — the
same conclusion as for the 410/660 pair in lesson 03, and for the same reason.

### ★★★10 — Measuring thickness and velocity drop separately

The lossless normal-incidence response of a layer contains exactly two numbers per
frequency band (a phase, i.e. a time shift, and a magnitude), and the layer has
three unknowns $(h, \delta, \rho'/\rho)$. So **at least one relation must come from
outside** — typically a mineral-physics or dynamical assumption about $\rho'$
(as in the lesson's $1.30\,\delta$). Given that, the design is:

**Observables.**

1. **The postcursor delay** at two or more ray parameters/azimuths, giving
   $2h(1/v_s' - 1/v_s)$ and a consistency check on lateral uniformity.
2. **The amplitude of the top-of-layer reflection** as a function of frequency. Its
   low-frequency limit gives the impedance contrast $r_\text{top}$ directly, and
   its notch structure gives $2h/v_s'$ — the internal two-way time, i.e. the
   thickness. This is the measurement the lesson's Section 3 shows is *not*
   available in the assumed model, because $r_\text{top}$ is only 1–5 %.
3. **A short-period phase** (S or P at ~1 Hz, e.g. a high-frequency core
   reflection) whose wavelength is a few kilometres, so that the top and bottom
   interfaces appear as separate arrivals.

**Frequency band required.** The notch spacing in $R(f)$ is
$\Delta f = 1/(2h/v_s')$: for $h = 20$ km and $v_s' = 6$, that is 0.15 Hz. So a
usable band is **0.05–1 Hz**, i.e. five or more notches, requiring recordings with
energy above 0.5 Hz at CMB distances — a demanding but standard requirement in
modern broadband studies.

**Predicted resolution.** With five resolvable notches at frequencies up to 1 Hz,
$2h/v_s'$ is determined to about 1/(5 × 1 Hz) = 0.2 s, i.e.
$h$ to ±1 km at $v_s' = 6$ km s$^{-1}$ — and *independently* of $\delta$, because
the notch spacing is a time in the layer. Combined with the delay, $\delta$ is then
determined to a few per cent. **The residual assumption is unavoidable**: the
density–velocity relation, which converts the measured $r_\text{top}$ into a
statement about $\rho'$. Reporting a ULVZ density therefore requires saying which
relation was assumed, and a study that does not is not reproducible.

---

## Mastery checkpoint — worked version

> ScS postcursor delay 1.8 s; a D'' discontinuity at 210 km above the CMB;
> $v_s = 7.26$, $\rho = 5.57$; outer core $\rho = 9.90$;
> $\rho g = 59.38\ \mathrm{MPa\,km^{-1}}$.

**(a) ULVZ thickness and the compensating $\delta$.**

For $\delta = 12\ \%$: $v_s' = 7.26 \times 0.88 = 6.3888\ \mathrm{km\,s^{-1}}$, and

$$h = \frac{\Delta t}{2\left(1/v_s' - 1/v_s\right)}
= \frac{1.8}{2\left(0.156524 - 0.137741\right)}
= \frac{1.8}{0.037566} = 47.92\ \mathrm{km}.$$

For $h = 25$ km, invert the same relation:

$$\frac{1}{v_s'} = \frac{1}{7.26} + \frac{1.8}{2 \times 25}
= 0.137741 + 0.036000 = 0.173741
\;\Rightarrow\;
v_s' = 5.756\ \mathrm{km\,s^{-1}},$$
$$\delta = 1 - \frac{5.756}{7.26} = 0.2072 \;\text{i.e. } 20.7\ \%.$$

So the same 1.8 s corresponds to **48 km at 12 %** or **25 km at 21 %**: the delay
fixes neither.

**(b) A 300 K warmer CMB.** With
$\mathrm{d}h/\mathrm{d}T = -\gamma/(\rho g) = -8/59.38 = -0.1347\
\mathrm{km\,K^{-1}}$:

$$\Delta h = -0.1347 \times 300 = -40.4\ \mathrm{km}
\;\Rightarrow\;
h = 210 - 40.4 = 169.6\ \mathrm{km}.$$

(Directly: $\Delta P$ drops by $300 \times 8\ \mathrm{MPa} = 2.4\ \mathrm{GPa}$, and
$2400/59.38 = 40.4$ km.)

**(c) Why 210 km may be an overestimate.** Two mechanisms:

1. **The dividing velocity.** Every thickness here is $v_s\Delta t/2$; if the true
   average $v_s$ above the reflector is 3 % lower than the 7.26 assumed, the
   thickness is 3 % smaller, i.e. 6 km, and the error is *systematic* — it applies
   to every measurement in the study in the same direction.
2. **An inflated delay.** The delay is a difference between two picked arrivals in
   data that may contain unmodelled structure above the reflector or a contaminating
   multiple; any such contribution adds to $\Delta t$ and therefore to $h$. A
   further, subtler cause is *Fresnel-zone smearing*: a reflector narrower
   laterally than the first Fresnel zone returns energy that a plane-layer
   back-projection distributes over an artificially thick depth range.

**(d) Measured versus inferred.** Directly **measured**: the two travel times and
their difference (a time). **Inferred**: the thickness (needs $v_s$), the velocity
drop $\delta$ (needs the thickness), the density contrast (needs an assumed
$\rho$–$v$ relation), and the CMB temperature (needs $\gamma$, $C$ and
$T_\text{ref}$). The chain is long, and each link is a place where two studies can
disagree without either being wrong.
