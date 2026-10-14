# Solutions — 17-08-02 Thermal Remote Sensing for Geothermal Systems

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [02 Thermal Remote Sensing for Geothermal Systems](../02-geothermal-rs.md).

---

## ★1 — Brightness temperature of a grey surface

The surface emits $L = \varepsilon B_\lambda(T)$ with $\varepsilon < 1$. The
naive inversion finds $T_{\text{app}}$ with
$B_\lambda(T_{\text{app}}) = \varepsilon B_\lambda(T)$. Since $B_\lambda$
increases with $T$ and $\varepsilon < 1$, $\varepsilon B_\lambda(T) <
B_\lambda(T)$, hence $T_{\text{app}} < T$. The inverse is exact *for a
blackbody*; the error comes entirely from mis-specifying $\varepsilon$.

---

## ★2 — Anomaly from a flux

$$
\Delta T = \frac{q\,z}{k} = \frac{0.15 \times 20}{2.0} = 1.5\ \mathrm{K}.
$$

---

## ★3 — Units

Heat flux: $\mathrm{W\,m^{-2}}$. Thermal conductivity:
$\mathrm{W\,m^{-1}\,K^{-1}}$. Gradient: $\mathrm{K\,m^{-1}}$ (reported in
$\mathrm{mK\,m^{-1}}$). Thermal inertia:
$\mathrm{J\,m^{-2}\,K^{-1}\,s^{-1/2}}$.

---

## ★4 — Noise limit versus emissivity limit

Noise-limited flux:

$$
q_{\min} = \mathrm{NE}\Delta T \cdot \frac{k}{z} = 0.20 \times \frac{2.0}{20}
= 0.020\ \mathrm{W\,m^{-2}}.
$$

Emissivity-equivalent flux:

$$
q_{\varepsilon} = 1.37 \times \frac{2.0}{20} = 0.137\ \mathrm{W\,m^{-2}}.
$$

The emissivity limit is $0.137 / 0.020 = 6.9$ times the noise limit — it
dominates. Improving the detector below a $0.02$ emissivity error buys nothing.

---

## ★5 — Interpolating the emissivity error

Between $0.95 \to -3.45$ and $0.90 \to -6.99$ the fraction is

$$
\frac{0.95 - 0.93}{0.95 - 0.90} = 0.4.
$$

$$
\text{error}(0.93) \approx -3.45 + 0.4\,(-6.99 + 3.45)
= -3.45 + 0.4\,(-3.54) = -3.45 - 1.416 = -4.87\ \mathrm{K}.
$$

---

## ★6 — Thermal-inertia amplitudes

$$
A(750) = \frac{12.0}{\sqrt{750/1000}} = \frac{12.0}{0.8660} = 13.86\ \mathrm{K},
\qquad
A(3000) = \frac{12.0}{\sqrt{3}} = 6.93\ \mathrm{K}.
$$

The low-inertia surface (dry, rocky) swings nearly twice as far as the
high-inertia one (wet, vegetated).

---

## ★7 — LST validation for geothermal work (specification)

- **References.** Co-located radiometers or thermistors at representative
  surfaces, plus a stable, well-characterised calibration target (a water body,
  or a large uniform playa).
- **Emissivity.** Taken from a spectral library matched to the surface, not
  assumed unity; its uncertainty is the dominant term and must be stated.
- **Atmosphere.** A radiative-transfer correction driven by a local atmospheric
  profile or an operational reanalysis, with the residual as an error term.
- **Metric.** Bias and RMSD of the *anomaly* (retrieved minus background), not of
  absolute temperature, because the geothermal signal is an anomaly.
- **Confound.** Topography and aspect drive surface temperature by several
  kelvin and are *not* geothermal; without a topographic or difference-based
  correction, a sunny slope would register as an anomaly.

---

## ★8 — For and against "the model sets the limit"

**For.** An emissivity error of $0.02$ moves the retrieved temperature by
$1.37\ \mathrm{K}$, equivalent to $0.137\ \mathrm{W\,m^{-2}}$ — nearly seven
times the noise-limited flux. Any improvement in $\mathrm{NE}\Delta T$ below the
emissivity error is masked by a larger, systematic error.

**Against.** The emitter of a *large* contrast (a fumarole field, a hot spring)
produces anomalies of many kelvin, far above the emissivity error; there the
detector noise sets the limit, and a better detector maps the anomaly more
finely.

**Condition.** Improving the detector helps only once the emissivity (and
atmosphere) uncertainty has been reduced below the noise-equivalent flux. The
practical order of work is therefore: constrain the surface model first, sharpen
the detector second.
