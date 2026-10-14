# Solutions — 09-01-05 Temperature, Pressure and Frequency Dependence

> **Read after attempting the exercises.** Lesson:
> [05 Temperature, Pressure and Frequency Dependence](../05-temperature-and-pressure-effects.md).

---

## ★1 — Linear coefficient

$$\alpha = \frac{E_a}{k_BT^{2}}
= \frac{0.15}{8.617333262\times10^{-5}\times298.15^{2}}
= \frac{0.15}{7.6603} = 0.019581\ \mathrm{K^{-1}}.$$

About 1.96% per kelvin.

---

## ★2 — Arrhenius versus linear

$$\sigma(T) = \sigma_\text{ref}\exp\left[-\frac{E_a}{k_B}
\left(\frac{1}{T}-\frac{1}{T_\text{ref}}\right)\right],$$

$T = 333.15$ K, $T_\text{ref} = 298.15$ K:
$1/333.15 - 1/298.15 = -3.5233\times10^{-4}$,
$E_a/k_B = 2901.1$ K, so the exponent is
$+1.02234$ and $\sigma = 0.05\times\mathrm{e}^{1.02234} = 0.05\times2.7796
= 0.13898\ \mathrm{S\,m^{-1}}$.

Linear form: $\alpha = 0.25/7.6603 = 0.032636\ \mathrm{K^{-1}}$, so
$\sigma \approx 0.05(1 + 0.032636\times35) = 0.05\times2.1423
= 0.10712\ \mathrm{S\,m^{-1}}$: **23% below the Arrhenius value**.

---

## ★3 — Compaction

$$\phi(500) = 0.35\exp(-500/1200) = 0.35\mathrm{e}^{-0.41667}
= 0.35\times0.65924 = 0.23073,$$

$$F = \phi^{-2} = 0.23073^{-2} = 18.79.$$

---

## ★4 — Conductivity profile and effective pressure

$\sigma = \sigma_w/F$; $P_\text{eff} = (2200-1150)\times9.81\times z$, i.e.
$1.03005\times10^{4}\times z$ Pa $= 0.0103005 z$ MPa.

| $z$ (m) | $\phi$ | $F$ | $\sigma$ ($\mathrm{S\,m^{-1}}$) | $\rho$ ($\Omega\,\mathrm{m}$) | $P_\text{eff}$ (MPa) |
|---|---|---|---|---|---|
| 0 | 0.35000 | 8.163 | 0.01837 | 54.4 | 0.00 |
| 500 | 0.23073 | 18.79 | 0.007985 | 125.2 | 5.15 |
| 1500 | 0.10050 | 99.01 | 0.001515 | 660.0 | 15.45 |

Resistivity rises with depth in this model because compaction outruns any
salinity change; the lesson states that a salinity increase opposes it.

---

## ★5 — Freezing versus warming

$\sigma(0)/\sigma(-3)$: $w(-3) = 1/(1+3) = 0.25$, so the ratio is
$1/0.25 = 4.000$ — conductivity falls by a factor 4 over 3 K.

$\sigma(25)/\sigma(0)$ with $E_a = 0.20$ eV: use the lesson's table, which gives
$\sigma(5)/\sigma(25) = 0.057137/0.100000 = 0.57137$; at
$0\ ^\circ\mathrm{C} = 273.15$ K, $1/273.15-1/298.15 = 3.0704\times10^{-4}$,
exponent $-0.2/8.617333\times10^{-5}\times3.0704\times10^{-4} = -0.71263$, so
$\sigma(0)/\sigma(25) = 0.49036$ and the ratio $\sigma(25)/\sigma(0) = 2.039$.

So **3 K of freezing (factor 4) beats 25 K of warming (factor 2)**. In permafrost
work the phase change is the signal; above zero it is only a correction.

---

## ★6 — Charge relaxation

$$\varepsilon = \varepsilon_r\varepsilon_0 = 12\times8.8541878128\times10^{-12}
= 1.06250\times10^{-10}\ \mathrm{F\,m^{-1}},$$

$$\tau_c = \frac{\varepsilon}{\sigma} = \frac{1.06250\times10^{-10}}{0.02}
= 5.3125\times10^{-9}\ \mathrm{s}, \qquad
f_c = \frac{1}{2\pi\tau_c} = 2.995\times10^{7}\ \mathrm{Hz}
\approx 30\ \mathrm{MHz}.$$

A 1 kHz survey is **four decades below** the relaxation frequency: it is
comfortably in the DC regime as far as charge relaxation is concerned. What it is
*not* automatically safe from is induced polarisation, whose relaxation
frequencies are in the 0.01–100 Hz band (see ★6 of
[04](04-clay-and-surface-conduction-solutions.md)).

---

## ★7 — Separating three causes of a 15% decrease

1. **Temperature:** $\alpha = 0.20/7.6603 = 0.026109\ \mathrm{K^{-1}}$; a 5 K
   rise gives $-13.1\%$ in resistivity — almost the whole observed change.
2. **Porosity:** $\rho \propto \phi^{-2}$ (for $m = 2$); a 10% *increase* in
   porosity gives $-17.4\%$ — also enough on its own.
3. **Salinity:** $\rho_w$ down by a factor 1.3 gives $-23.1\%$ — enough on its
   own.

All three are individually sufficient, so the data cannot choose. The decisive
extra measurement is **temperature at the depth of interest** (a thermistor
string or a fibre-optic cable), because it is the only one of the three that can
be measured independently at low cost. With temperature measured, the residual
after removing (1) is $-2\%$, which is below the noise: the honest report is
"the change is consistent with the measured temperature rise, with a residual of
$-2\pm2\%$ attributable to moisture or salinity, which this survey cannot
separate".

---

## ★8 — A combined experiment

1. **Sample preparation:** one homogeneous core plug, fully saturated with a
   single brine, sealed to prevent evaporation.
2. **Instrumentation:** a four-electrode cell with temperature control over
   $-10$ to $+60\ ^\circ\mathrm{C}$, measuring $\sigma$ at a low frequency
   (below 0.1 Hz, to stay in the DC limit) and the complex conductivity over
   0.001–10 kHz at each temperature.
3. **DC measurement:** fit $\ln\sigma$ against $1/T$; the slope gives $E_a$.
4. **IP measurement:** extract $f_c$ from the peak of the phase spectrum at each
   temperature and fit $\ln f_c$ against $1/T$; because $\tau \propto
   \mathrm{e}^{E_a/k_BT}$, this slope gives the *relaxation* activation energy.
5. **Test:** the two activation energies must agree within their confidence
   intervals *and* the residuals of both fits must be structureless. A
   systematic difference means the mechanisms are not the same; a curvature in
   either fit means a single Arrhenius model is inadequate over the range. Report
   both slopes with uncertainties, not just the claim.
