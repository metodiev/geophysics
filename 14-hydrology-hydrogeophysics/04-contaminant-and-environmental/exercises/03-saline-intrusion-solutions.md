# Solutions — 14-04-03 Seawater Intrusion and Coastal Aquifer Monitoring

> Read after attempting. Lesson:
> [03 Seawater Intrusion and Coastal Aquifer Monitoring](../03-saline-intrusion.md).
> All models **SYNTHETIC**.

---

## ★1 — Ghyben–Herzberg with two saline densities

$$\frac{\rho_f}{\rho_s - \rho_f} = \frac{1000}{1027-1000} = \frac{1000}{27}
= 37.04, \qquad z = 37.04\times1.50 = 55.6\ \mathrm{m}.$$

For $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$ the ratio is
$1000/25 = 40.0$ and $z = 60.0\ \mathrm{m}$.

**Direction.** A *denser* saline end member pushes the interface *up* (shallower
fresh water), because the pressure balance is reached with a shorter saline
column: the ratio is $1/(\rho_s - \rho_f)$ and the denominator grows. The
difference is substantial — $4.4\ \mathrm{m}$, $7\%$ of the depth — for a
$0.2\%$ change in the saline density, which is the same 40:1 amplification
operating on the density rather than on the head. **This is why the saline
end-member density must be stated, not assumed.**

---

## ★2 — Interface rise and volume change

$$
\Delta z = \frac{\rho_f}{\rho_s - \rho_f}\Delta h
= 40\times0.30 = 12.0\ \mathrm{m},
\qquad
z_\text{new} = 40\times1.20 = 48.0\ \mathrm{m}.
$$

Fresh-water volume per unit area, $V = \phi(h+z)$:

$$V_0 = 0.25\times(1.50+60.0) = 0.25\times61.50 = 15.375\
\mathrm{m^{3}\,m^{-2}},$$

$$V_1 = 0.25\times(1.20+48.0) = 0.25\times49.20 = 12.300\
\mathrm{m^{3}\,m^{-2}} .$$

The loss is $3.075\ \mathrm{m^{3}\,m^{-2}}$, i.e. $20.0\%$ — and the head fell by
$20.0\%$. **The head and the fresh-water volume scale together**; it is the
*depth* that carries the 40:1 amplification. Reporting "the interface rose 12 m"
without the volume change exaggerates the hydrological severity and reporting
only the head hides where the water went.

---

## ★3 — Resistivity and the log contrast

$\sigma_b = \phi^{m}\sigma_w/a = 0.35^{1.8}\sigma_w$, and
$0.35^{1.8} = e^{1.8\ln 0.35} = e^{-1.889} = 0.1511$.

At $c = 0$: $\sigma_w = 0.050\ \mathrm{S\,m^{-1}}$,
$\sigma_b = 0.007556\ \mathrm{S\,m^{-1}}$, $\rho_b = 132.3\
\Omega\,\mathrm{m}$.

At $c = 0.20$: $\sigma_w = 0.050 + 0.20\times3.95 = 0.840\
\mathrm{S\,m^{-1}}$, $\sigma_b = 0.12692\ \mathrm{S\,m^{-1}}$,
$\rho_b = 7.88\ \Omega\,\mathrm{m}$.

Fraction of the log contrast, with
$\rho(c = 1) = 1/(0.1511\times4.00) = 1.655\ \Omega\,\mathrm{m}$:

$$\frac{\ln 132.3 - \ln 7.88}{\ln 132.3 - \ln 1.655}
= \frac{4.885 - 2.064}{4.885 - 0.504} = \frac{2.821}{4.381} = 0.644 .$$

**A saline fraction of $0.20$ produces $64\%$ of the log-resistivity contrast.**
Any interpretation that reads a partial anomaly as a proportional salinity is
wrong by a factor of three at this point: the relation between $c$ and
$\ln\rho$ is strongly non-linear because $\rho$ is the reciprocal of a linear
function of $c$.

---

## ★★4 — Transition-zone width

$$w_{10\text{–}90} = 2\times1.2816\times\sqrt{2}\,\sigma
= 3.625\times5.0 = 18.1\ \mathrm{m},$$

which is $18.1/30 = 60\%$ of the interface depth. Two consequences: the
transition zone is the dominant feature, not a correction; and a survey that
reports "the interface at $30\ \mathrm{m}$" when the 10–90% band spans
$20.9$–$39.1\ \mathrm{m}$ has quoted a model, not a measurement. Report the depth
*and* the width.

---

## ★★5 — Spacings for detecting an interface rise

From the lesson's two-layer results for $\rho_1 = 222.2\
\Omega\,\mathrm{m}$ over $\rho_2 = 2.78\ \Omega\,\mathrm{m}$ at
$z_i = 20\ \mathrm{m}$, a $1\ \mathrm{m}$ rise changes $\rho_a$ by
$-0.16\%$ at $a = 5\ \mathrm{m}$, $-0.98\%$ at $10\ \mathrm{m}$, $-4.30\%$ at
$20\ \mathrm{m}$ and $-11.64\%$ at $40\ \mathrm{m}$. With a $2\%$ (one-sigma)
repeatability, only $a = 20\ \mathrm{m}$ and $40\ \mathrm{m}$ detect it.
**Place the main spacings at $a \gtrsim 1$–$2\,z_i$.**

The smallest spacings are excluded because they sample only the fresh layer above
the interface: the sensitivity kernel decays with depth, so at $a = 0.25\,z_i$
the interface contributes almost nothing to the measured potential difference.
Adding small spacings increases the survey cost and the inversion's parameter
count while adding no information about the target.

**A $0.2\ \mathrm{m}$ rise.** The signal scales roughly linearly for small
changes, so the expected anomalies are $0.2\times$ those above: $-0.032\%$ at
$5\ \mathrm{m}$, $-0.86\%$ at $20\ \mathrm{m}$, $-2.33\%$ at $40\ \mathrm{m}$.
With a $2\%$ repeatability **none of them is detectable**. What changes is the
requirement: either the repeatability must improve to about $0.5\%$ (via a
permanent installation, reciprocal measurements and a fixed array — the standard
recipe for time-lapse ERT), or the survey must target the *largest* available
spacing, where the fractional change is greatest, and the change must be
monitored as a trend over several seasons rather than in one pair of surveys.

---

## ★★6 — Clay equivalence versus contrast strength

With $c_\text{eq} = \sigma_\text{clay}/[\phi^{m}(\sigma_s-\sigma_f)]$,
$\phi^{m} = 0.09$ and $\sigma_\text{clay} = 0.02\ \mathrm{S\,m^{-1}}$:

| $\sigma_s$ ($\mathrm{S\,m^{-1}}$) | $\sigma_s-\sigma_f$ | $c_\text{eq}$ |
|---|---|---|
| 4.00 | 3.95 | $0.020/(0.09\times3.95) = 0.056$ |
| 0.80 | 0.75 | $0.020/(0.09\times0.75) = 0.296$ |
| 0.50 | 0.45 | $0.020/(0.09\times0.45) = 0.494$ |

**Operational consequence.** Against a full-strength seawater end member, a clay
conductance misleads by at most about $6\%$ of the saline fraction — small enough
to be tolerable in a screening survey. Against a *brackish* end member of
$0.5\ \mathrm{S\,m^{-1}}$ it misleads by $49\%$: **a fresh clayey rock and a
half-saline clean rock are the same measurement.** A survey on a coast whose
pristine pore water is already conductive must carry a clay indicator, or it
cannot claim to have measured intrusion at all. The rule is that the safe
operating regime of the method is set by the ratio
$\sigma_\text{clay}/[\phi^{m}(\sigma_s-\sigma_f)]$, not by the instrument.

---

## ★★★7 — A well-field monitoring programme (model answer)

**(a) Methods and justification.**

1. **Time-lapse ERT**, permanent electrodes, because the primary observable is a
   bulk conductivity change driven by a pore-fluid salinity change. Justification:
   the contrast is up to $80\times$ (lesson Section 6), it is entirely in the
   fluid and therefore rock-independent, and differencing removes the static
   array and geological errors.
2. **TDEM or EM induction soundings**, because they respond to the bulk
   conductivity with better sensitivity to a conductive layer at depth and
   without electrode contact problems; they provide the deep half of the section
   that a surface ERT array cannot reach economically.
3. **Head and salinity sampling** at the well field, because the Ghyben–Herzberg
   lever is 40:1 in the other direction: the head is the early warning and the
   fluid sample is the ground truth that separates salinity from clay.

**(b) Observables and thresholds.** For a $0.5\ \mathrm{m}$ rise: with the
lesson's sensitivity of $-4.30\%$ per metre at $a = 2\,z_i$, the signal is
$-2.15\%$. A permanent ERT installation with reciprocal measurements and
stacking reaches a repeatability of about $1\%$ or better, so the change is
detectable at roughly two sigma — but only at spacings near $2\,z_i$. The head
record resolves $0.5\ \mathrm{m}$ of interface rise as $0.0125\
\mathrm{m}$ of head, which is below the accuracy of a routine water-level
measurement; **the head is not the detector at this magnitude, it is the
explanation.**

**(c) What each method cannot exclude alone.**

| method | alternative it cannot exclude | how the combination helps |
|---|---|---|
| ERT alone | a clay layer with fresh water | a clay indicator (gamma or NMR) plus the EM deep sounding |
| EM/TDEM alone | the same clay ambiguity, plus a conductive lithology change | the layered geometry from ERT and the borehole log |
| head alone | a density change (temperature, salinity of the ambient water) | the salinity sample and the temperature log |
| sampling alone | the extent of the intrusion (a single well is a point) | the two geophysical methods, which interpolate between wells |

The programme is defensible only if the *cross-checks* are scheduled with the same
repeatability as the primary measurement; a one-off clay indicator cannot
validate a time-lapse conductivity change.

---

## ★★★8 — Where the static relation fails

**(a) Two assumptions that fail first.**

1. **Static water.** The relation presumes no flow, so it predicts the interface
   position for a given head but nothing about the *time* to reach it or the
   shape near a pumping well. What it hides is the **transition zone** and the
   slow, dispersive migration of the interface that follows a head change; a
   surveyed interface lags the head by years in a low-permeability aquifer.
2. **Sharp interface.** Dispersion widens the boundary to tens of metres, so a
   "depth to the interface" is a location on a gradient. What it hides is that
   the *first* saline water to arrive at a well comes from the upper edge of the
   transition zone, not from the sharp interface; the water quality degrades
   before the interface appears to move.

**(b) Why upconing can exceed regional intrusion.** The regional interface rises
by $40\,\delta h$ for a regional head change $\delta h$. Beneath a pumping well the
*local* drawdown is concentrated in a cone of radius comparable to the aquifer
thickness $b$, and the interface is drawn up toward the screen. The vertical
gradient near the well scales as the local drawdown divided by the distance to
the interface, which is far larger than the regional gradient $(\delta h /
\text{regional scale})$. In practice a well with a few metres of local drawdown
can pull saline water into the screen while the regional interface has barely
moved — and the damage is localised, immediate and irreversible in the sense
that the well must be shut in. **The volume is small and the consequence is
large**, which is the opposite of the regional case.

**(c) Distinguishing observation.** *Upconing* is local: the salinity increase
appears at one well or one part of the field, the deep screen shows it before the
shallow screen does (or vice versa depending on screen depth), it correlates with
that well's pumping record, and it decays when pumping stops. *Regional
intrusion* is coherent over kilometres: the same trend appears at every well on
the transect, it correlates with the regional head record rather than with any
single well, and it does not reverse when one well is shut off. A time-lapse
resistivity transect with wells at several spacings along the flow direction is
what separates the two, because it measures the *spatial extent* of the change,
which no single well can.
