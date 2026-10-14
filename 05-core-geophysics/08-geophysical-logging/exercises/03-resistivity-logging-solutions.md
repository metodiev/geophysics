# Solutions — 05-08-03 Resistivity, Induction and Laterolog Tools

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Three families

| Tool | Physical measurement | Requirement |
|---|---|---|
| Induction | Secondary field from eddy currents induced by a transmitter coil; responds to conductivity | None — works in oil-base mud, air or an empty hole |
| Focused laterolog | Voltage needed to drive a known, focused current into the formation | Conductive borehole fluid to couple current |
| Pad micro-resistivity | Resistance between electrodes pressed against the wall | Wall contact; gives $R_{xo}$, not $R_t$ |

---

## ★2 — Skin depth at 20 kHz

$503\sqrt{\rho/f}$ with $f = 2\times10^{4}$ Hz:

| $\rho$ (Ω m) | $\delta$ (m) |
|---|---|
| 1 | 3.6 |
| 10 | 11.2 |
| 100 | 35.6 |

For a deep-reading tool the *large* values matter: at 100 Ω m the field penetrates
35.6 m, so the measurement is mediated by a volume far larger than the hole, which
is why deep induction tools use low frequencies and why a very resistive formation
gives a small secondary field.

---

## ★3 — Units

$250\ \mathrm{mS\,m^{-1}} = 0.25\ \mathrm{S\,m^{-1}} \Rightarrow R = 4.0$ Ω m.
Conductivity logs are plotted in mS m⁻¹ or in mmho m⁻¹; the two are numerically
identical, so a factor-of-1000 suspicion is misplaced — but a factor-of-1
confusion between S m⁻¹ and mS m⁻¹ is a real risk.

---

## ★4 — The two averaging rules

**(a)** Shallow ($L = 0.15$ m): $\rho_{\text{avg}} = 8.50$ Ω m against
$1/\sigma_{\text{avg}} = 1.46$ Ω m, ratio 5.81. Deep ($L = 1.50$ m):
16.59 against 11.15 Ω m, ratio 1.49.

**(b)** The deep weighting extends well beyond the 0.30 m invaded radius, so most of
its response comes from the virgin formation; the two averages then differ only in
how the *residual* filtrate in the transition is weighted. The shallow weighting
sits mostly inside the invaded zone, where the 21:1 contrast dominates and the two
rules diverge strongly.

**(c)** An induction–laterolog difference over an invaded or thinly bedded interval
is **expected** and carries information; it is not evidence that either tool is
faulty. Reducing the difference requires either a deeper-reading pair or an
explicit averaging model.

---

## ★5 — Saturation

**(a)** $S_w = (0.1/(0.20^2\times50))^{1/2} = (0.1/2.0)^{1/2} = 0.2236$.

**(b)** With the reading 20 per cent low, $R_{\text{app}} = 40$ Ω m:
$S_w = (0.1/(0.04\times40))^{1/2} = (0.0625)^{1/2} = 0.2500$.

**(c)** The error is $+0.0264$, i.e. $+11.8$ per cent, and the direction is
**high**: a low resistivity reading always makes the formation look wetter. The
governing factor is the ratio $R_{mf}/R_w$ (which sets the sign) and the invasion
radius relative to the tool's depth of investigation (which sets the size).

---

## ★6 — Temperature

Using a stated approximate form $R_w(T) = R_w(T_0)\,[T_0 + 21.5]/[T + 21.5]$ with
temperatures in °C — a widely used *empirical* conversion, quoted here as a
convention with its source to be stated in any report — with $T_0 = 60$ °C,
$T = 100$ °C and $R_w(60) = 0.1$ Ω m:

$$R_w(100) = 0.1\,\frac{60+21.5}{100+21.5} = 0.1\,\frac{81.5}{121.5}
= 0.0671\ \Omega\,\mathrm{m}.$$

Since $S_w \propto R_w^{1/n}$ with $n = 2$, the saturation falls by a factor
$\sqrt{0.671} = 0.819$, i.e. **18 per cent lower** — a change larger than most of
the uncertainty terms in a real interpretation. The conversion must be stated, and
$R_w$ must be reported at a named temperature.

---

## ★7 — Radial laterolog model

A defensible implementation: solve $\nabla\cdot(\sigma\nabla V) = 0$ in cylindrical
coordinates with a stated electrode current distribution (a disc source of radius
$a$ plus guard electrodes maintained at equal potential), compute the potential
difference, and form $\rho_a = K\Delta V/I$ with $K$ from the tool geometry. Then
vary $r_i$ with $R_{xo} = 1$ Ω m and $R_t = 20$ Ω m.

Expected findings: (i) the response saturates once $r_i$ exceeds about the electrode
spacing, so a deep laterolog is blind to invasion beyond that radius — which is the
same geometric-factor statement as the demo's $a = 0.019$; (ii) the two-reading
inversion is therefore ill-conditioned exactly when the invasion is deep, i.e.
precisely when the correction is most needed; (iii) the residual accuracy depends
on the assumed profile shape, as in the lesson.

---

## ★8 — A programme for an oil-based-mud, thin-bedded, anisotropic reservoir

- **Tools:** multi-frequency, multi-spacing **induction** (mandatory: no conductive
  mud), a **density–neutron–P$_\mathrm{e}$** triple for mineralogy and porosity, an
  **NMR** for lithology-independent porosity and bound-fluid volume, a **sonic**
  for the tie and for anisotropy (dipole if available), and an **image log** for
  dips and fractures.
- **Acquisition:** low frequencies for depth reach, several spacings for a genuine
  radial profile, slow logging over the reservoir for NMR polarisation, and a
  deviation survey in the same run.
- **Processing:** environmental corrections identified by name and version, a
  multi-spacing radial inversion for the invasion profile (rather than a
  two-reading step model), and depth matching to the gamma-ray reference.
- **Interpretation:** a shaly-sand saturation model, not Archie, with the clay
  parameters from core or from NMR bound water; anisotropy handled explicitly in the
  tie.
- **Limiting measurement:** in this setting it is usually the **shaly-sand
  saturation model's clay parameters**, not the resistivity. State that, and design
  the core programme around it.
