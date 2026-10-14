# Solutions — 11-03-06 Integrating Borehole Data with Seismic

> **Read after attempting the exercises.** Numbers were computed rather than
> estimated; where a value is an assumption it is labelled.

Lesson: [06 Integrating Borehole Data with Seismic](../06-borehole-and-integration.md).

---

## ★1 — Impedance and reflection coefficient

$$Z_1 = 3200\times2350 = 7.520\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}
= 7.52\ \mathrm{MRayl},$$
$$Z_2 = 3600\times2420 = 8.712\times10^{6} = 8.71\ \mathrm{MRayl},$$
$$r = \frac{Z_2-Z_1}{Z_2+Z_1} = \frac{1.192}{16.232} = 0.0734 .$$

A 7% reflection coefficient is a strong, easily mapped event — comparable to a
clean sand/shale interface.

---

## ★2 — Time–depth conversion

$$t(2000) = \frac{2}{0.4}\ln\left(1+\frac{0.4\times2000}{1900}\right)
= 5\ln(1.421053) = 5\times0.351397 = 1.7570\ \mathrm{s}.$$

With the wrong $v_0 = 2000$:

$$z = \frac{2000}{0.4}\left(e^{0.4\times1.7570/2}-1\right)
= 5000\left(e^{0.351397}-1\right) = 5000\times0.421053
= 2105.3\ \mathrm{m}.$$

**Error: +105.3 m (+5.3%)** at 2 km, from a 5.3% error in $v_0$ alone. The depth
error is proportional to depth and to the fractional velocity error — the
central message of the lesson's §3.

---

## ★3 — Which averages are exact

- **Density:** mass per unit volume is additive, so the cell density is exactly
  the volume-fraction-weighted arithmetic mean of the constituent densities.
- **Velocity:** the *transit time* through the cell is exactly the sum of the
  constituent travel times, which makes $1/v$ the volume-fraction-weighted mean
  — a harmonic average of velocity. The resulting product
  $\rho_{\text{cell}}v_{\text{cell}}$ is only an approximation to the
  amplitude-relevant impedance; the rigorous long-wavelength construction is
  Backus averaging (★★5).

---

## ★★4 — Diagnosing a stretch

| time (s) | required shift (ms) |
|---|---|
| 1.0 | 20 |
| 2.0 | 44 |

A constant shift would give 20 ms at both times; the observed doubling is
**linear in time**, which is the signature of a *velocity* error, not of a
wavelet or a datum problem. From $t_{\text{seis}} = t_{\text{well}}/(1+\varepsilon)$,

$$\text{shift} = t_{\text{well}}\frac{\varepsilon}{1+\varepsilon},$$

so at 1.0 s: $\varepsilon/(1+\varepsilon) = 0.0200 \Rightarrow \varepsilon =
0.0204$; at 2.0 s: $2\varepsilon/(1+\varepsilon) = 0.0440 \Rightarrow
\varepsilon = 0.0225$. **The velocity is about 2.1–2.3% too fast in the seismic
model.**

**What to change:** the time-depth function (re-fit $v_0$ and $k$ to the check
shots), and if the seismic volume was migrated with the wrong function, the
depth conversion must use the *well* function while the *times* stay as the
seismic has them — the stretch goes into the conversion, not into the tie.

**If not corrected:** at 2.5 km the depth error is
$2500\times0.022 \approx 55$ m, twice the vertical resolution, which is a
structural error an interpreter would read as a real feature.

---

## ★★5 — Backus averaging for a two-component stack

Sand (35%): $\mu = 9.00$ GPa, $\lambda = 9.5625$ GPa, $M = \lambda+2\mu =
27.5625$ GPa. Shale (65%): $\mu = 6.144$ GPa, $\lambda = 7.206$ GPa,
$M = 19.496$ GPa. $\bar\rho = 0.35(2250)+0.65(2400) = 2347.5\
\mathrm{kg\,m^{-3}}$.

$$\left\langle \frac{1}{M}\right\rangle = \frac{0.35}{27.5625}
+ \frac{0.65}{19.496} = 1.2698\times10^{-2} + 3.3340\times10^{-2}
= 4.6038\times10^{-2}\ \mathrm{GPa^{-1}},$$
$$C_{33} = \left\langle M^{-1}\right\rangle^{-1} = 21.721\ \mathrm{GPa},$$
$$\left\langle \frac{\lambda}{M}\right\rangle
= 0.35\times0.34694 + 0.65\times0.36961 = 0.36168,$$
$$\left\langle \frac{4\mu(\lambda+\mu)}{M}\right\rangle
= 0.35\times24.245 + 0.65\times16.829 = 19.424\ \mathrm{GPa},$$
$$C_{11} = 19.424 + 21.721\times0.36168^{2}
= 19.424 + 2.841 = 22.265\ \mathrm{GPa}.$$

Velocities:

$$v_{p,v} = \sqrt{\frac{21.721\times10^{9}}{2347.5}} = 3041.8\
\mathrm{m\,s^{-1}}, \qquad
v_{p,h} = \sqrt{\frac{22.265\times10^{9}}{2347.5}} = 3079.7\
\mathrm{m\,s^{-1}}.$$

**Verification against the travel-time average:**

$$\bar{v} = \frac{1}{\dfrac{0.35}{3500}+\dfrac{0.65}{2850}}
= \frac{1}{3.2807\times10^{-4}} = 3048.1\ \mathrm{m\,s^{-1}},$$

which is 0.21% above the Backus vertical velocity — the same order as the
lesson's 0.19%. And

$$\varepsilon = \frac{C_{11}-C_{33}}{2C_{33}} = \frac{5.444}{2\times21.721}
= +0.0125,$$

positive, as the parallel-versus-series argument requires.

---

## ★★6 — A 60° phase error

From the demonstration's table, a 60° rotation gives a correlation of **0.500**
with the zero-phase synthetic, and the picked trough moves from −13.0 ms to
+8.0 ms, a displacement of **21 ms**.

In depth at 3 km with $v = 3150\ \mathrm{m\,s^{-1}}$:

$$\Delta z = \frac{v\,\Delta t}{2} = \frac{3150\times0.021}{2} = 33\ \mathrm{m}.$$

So a 60° phase error both halves the tie correlation and moves a picked horizon
by 33 m — larger than the seismic resolution, and systematic. Phase is not a
cosmetic parameter.

---

## ★★★7 — A calibration programme

**Measurements.**

1. **Check shots or a VSP** in the well: levels at 250 m spacing to 1.5 km, then
   through the target interval at 100 m spacing, plus one level at total depth.
2. **Sonic and density logs** over the same interval, calibrated to the check
   shots and to core where available.
3. **A zero-offset VSP** for a direct wavelet estimate (phase), rather than a
   statistical wavelet from the seismic.

**Model forms to test.**

1. linear in depth: $v = v_0+kz$ (2 parameters);
2. logarithmic/compaction: $v = v_0 + k\ln(1+z/z_0)$ (3 parameters);
3. layer-based: interval velocities between calibration levels (many
   parameters, over-parameterised at the top).

**Metric.** For each form, the RMS travel-time residual at the calibration
levels *and* the residual at levels withheld from the fit (cross-validation).
The withheld-level residual is what discriminates between forms, because a
richer form always fits the calibration set better.

**Number of levels.** The demonstration's noise study (2 ms picks, 200
realisations) shows a mean depth error of 3.0 m at $n = 2$ levels, 2.4 m at 5,
1.8 m at 10 and 1.3 m at 20 — so beyond about 5 levels the *noise* limit is a few
metres and further levels buy little. The binding error is the **model form**:
a straight-line time-depth assumption in this geometry gave **+156.8 m** at
3 km. Hence: sample levels to make the form testable (at least 5, well
distributed in depth), and spend the effort on form selection, not on more
levels of the wrong form.

**Expected accuracy.** With the right form, a tested wavelet and a proper tie:
depth error dominated by velocity uncertainty, of order 0.5–1% of depth
(15–30 m at 3 km) if a check shot reaches the target interval; several per cent
(>50 m) if the velocity function is extrapolated from shallow levels only.

---

## ★★8 — Backus derivation for two components

**Vertical (in series).** For a vertically propagating wave the normal stress
$\sigma_{33}$ is continuous across horizontal interfaces and uniform in $z$ at
long wavelengths; the vertical strains of the two layers add:

$$\varepsilon_{33} = f_1\frac{\sigma_{33}}{M_1} + f_2\frac{\sigma_{33}}{M_2}
\qquad\Longrightarrow\qquad
C_{33} = \frac{\sigma_{33}}{\varepsilon_{33}}
= \left(\frac{f_1}{M_1}+\frac{f_2}{M_2}\right)^{-1},$$

with $M = \lambda+2\mu$: a **harmonic** average, which is the general
$\langle M^{-1}\rangle^{-1}$ result.

**Horizontal (in parallel).** For in-plane deformation the in-plane strain is
continuous and the stresses add. Taking the two layers side by side and
requiring equal lateral strain (which the layered geometry enforces for a
long-wavelength lateral disturbance), the effective in-plane modulus is the sum
of the layer contributions weighted by volume fraction, corrected for the
cross-coupling term $C_{13}$ that the vertical free contraction introduces:

$$C_{11} = \left\langle \frac{4\mu(\lambda+\mu)}{\lambda+2\mu}\right\rangle
+ C_{33}\left\langle\frac{\lambda}{\lambda+2\mu}\right\rangle^{2},$$

which reduces to $\langle M\rangle$ when the layers are identical.

**Inequality.** Since $1/M$ is a convex function of $M$, Jensen's inequality
gives $\langle 1/M\rangle^{-1} \le \langle M\rangle$ with equality only for
$M_1 = M_2$. The correction term
$C_{33}\langle\lambda/M\rangle^{2}$ is positive and of second order in the
contrast, so $C_{11} \ge C_{33}$, with strict inequality whenever the layers
differ. Hence $\varepsilon = (C_{11}-C_{33})/(2C_{33}) \ge 0$: **layering always
makes the horizontal P direction faster.**

**Wavelength condition.** The derivation assumes the wavelength is long
compared with the layer thicknesses (the long-wavelength, or quasi-static,
limit), so that the stress and strain fields can be averaged independently of
frequency. At wavelengths comparable to the layer thickness, the medium is
dispersive and the equivalent-medium description fails — which is exactly the
regime in which fine layering produces the frequency-dependent effects that
make a wavelet travel faster than its phase velocity suggests.
