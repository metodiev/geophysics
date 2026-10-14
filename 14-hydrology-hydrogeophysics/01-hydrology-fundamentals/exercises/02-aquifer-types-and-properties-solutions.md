# Solutions — 14-01-02 Aquifers, Porosity, Permeability and Storativity

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All rocks are **SYNTHETIC**.

Lesson: [02 Aquifers, Porosity, Permeability and Storativity](../02-aquifer-types-and-properties.md).
Constants: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$\mu_w = 1.002 \times 10^{-3}\ \mathrm{Pa\,s}$,
$\beta_w = 4.4 \times 10^{-10}\ \mathrm{Pa^{-1}}$,
$1\ \mathrm{darcy} = 9.869233 \times 10^{-13}\ \mathrm{m^2}$.

---

## ★1 — Porosity and water content

$$n = 1 - \frac{\rho_b}{\rho_s} = 1 - \frac{2.10}{2.68} = 1 - 0.78358 = 0.21642.$$

Water in $1\ \mathrm{m^3}$ of saturated rock at $n = 0.21642$:
$0.21642\ \mathrm{m^3} = 216.4\ \mathrm{L}$. (Using $\rho_w = 1000\
\mathrm{kg\,m^{-3}}$, 1 m$^3$ of water is exactly 1000 L.)

Comment: $216\ \mathrm{L}$ is the *total* pore water. The drainable volume is
$S_y \times 1\ \mathrm{m^3}$, which for a typical $S_y = 0.15$ is only 150 L —
see ★2.

---

## ★2 — Specific retention and drainage

$$S_r = n_e - S_y = 0.24 - 0.22 = 0.02.$$

Drainage from a unit-area column over $\Delta h = 2\ \mathrm{m}$:

$$V = S_y\,A\,\Delta h = 0.22 \times 1\ \mathrm{m^2} \times 2\ \mathrm{m}
= 0.44\ \mathrm{m^3} = 440\ \mathrm{L}.$$

Note that $S_r$ here (0.02) is much smaller than $n - n_e = 0.04$, the
*immobile connected* fraction. The ordering to remember is
$$S_y \le n_e \le n = 0.28, \qquad S_r = n_e - S_y = 0.02.$$

---

## ★3 — Conductivity to permeability

$$k = \frac{K\mu_w}{\rho_w g}
= \frac{(5.0 \times 10^{-5})(1.002 \times 10^{-3})}{1000 \times 9.81}
= 5.107 \times 10^{-12}\ \mathrm{m^2}.$$

Units: $\mathrm{m\,s^{-1}} \cdot \mathrm{Pa\,s} = \mathrm{kg\,m^{-1}\,s^{-1}}$;
divided by $\mathrm{kg\,m^{-3}} \cdot \mathrm{m\,s^{-2}} = \mathrm{kg\,m^{-2}\,s^{-2}}$
gives $\mathrm{m^2}$ ✔.

In darcy:
$$k = \frac{5.107 \times 10^{-12}}{9.869233 \times 10^{-13}}
= 5.175\ \mathrm{D}.$$

Comment: 5 darcy is a very permeable gravel, consistent with a hydraulic
conductivity of $5 \times 10^{-5}\ \mathrm{m\,s^{-1}}$ ($\approx 4.3\
\mathrm{m\,d^{-1}}$). If the same $K$ had been measured with water at
$5\ ^\circ\mathrm{C}$ ($\mu_w = 1.519 \times 10^{-3}\ \mathrm{Pa\,s}$), the
inferred $k$ would be $7.74 \times 10^{-12}\ \mathrm{m^2}$ — 52% larger, and wrong,
because the viscosity was not the 20 $^\circ$C value.

---

## ★★4 — Confined storage from compressibilities

$$S_s = \rho_w g(\alpha + n\beta_w)
= 1000 \times 9.81 \left(2.0 \times 10^{-9} + 0.20 \times 4.4 \times 10^{-10}\right)$$
$$= 9810 \times (2.0 \times 10^{-9} + 8.80 \times 10^{-11})
= 9810 \times 2.088 \times 10^{-9}
= 2.048 \times 10^{-5}\ \mathrm{m^{-1}}.$$

$$S = S_s b = 2.048 \times 10^{-5} \times 25 = 5.121 \times 10^{-4}.$$

Volume released over $A = 4\ \mathrm{km^2} = 4 \times 10^{6}\ \mathrm{m^2}$ under
$\Delta h = 8\ \mathrm{m}$:

$$V = S A \Delta h = 5.121 \times 10^{-4} \times 4 \times 10^{6} \times 8
= 1.639 \times 10^{4}\ \mathrm{m^3} \approx 16{,}400\ \mathrm{m^3}.$$

Unconfined comparison, $S_y = 0.20$, $\Delta h = 1\ \mathrm{m}$:

$$V = 0.20 \times 4 \times 10^{6} \times 1 = 8.0 \times 10^{5}\ \mathrm{m^3}.$$

Ratio: $8.0 \times 10^{5} / 1.639 \times 10^{4} = 48.8$. **One metre of
water-table decline in the unconfined case releases 49 times more water than eight
metres of head decline in the confined case.** Note also the asymmetry of the
split in $S_s$: the rock term contributes
$2.0\times10^{-9}/2.088\times10^{-9} = 96\%$ and the water expansion only 4%. In a
soft unit ($\alpha \sim 3 \times 10^{-8}$) the water term is a tenth of a per cent
and $\beta_w$ can be neglected entirely — but only then.

---

## ★★5 — Kozeny–Carman on a sand and a clay

With $\rho_w g/\mu_w = 9.790 \times 10^{6}\ \mathrm{s^{-1}\,m^{-1}}$ and
$c_{\text{KC}} = 180$:

Sand, $d = 0.30\ \mathrm{mm} = 3.0 \times 10^{-4}\ \mathrm{m}$, $n = 0.30$:
$$K = 9.790 \times 10^{6} \times
\frac{(3.0\times10^{-4})^{2}(0.30)^{3}}{180(0.70)^{2}}
= 9.790 \times 10^{6} \times 5.510 \times 10^{-11}
= 2.697 \times 10^{-4}\ \mathrm{m\,s^{-1}}.$$

Clay, $d = 0.002\ \mathrm{mm} = 2.0 \times 10^{-6}\ \mathrm{m}$, $n = 0.45$:
$$K = 9.790 \times 10^{6} \times
\frac{(2.0\times10^{-6})^{2}(0.45)^{3}}{180(0.55)^{2}}
= 9.790 \times 10^{6} \times 6.694 \times 10^{-15}
= 6.554 \times 10^{-8}\ \mathrm{m\,s^{-1}}.$$

Ratio: $2.697 \times 10^{-4}/6.554 \times 10^{-8} = 4116$.

**Which result should not be trusted.** The clay. Kozeny–Carman assumes a clean
granular medium with a single flow path through pores of a well-defined diameter.
Fine-grained sediment has bound water, surface conduction, clay-mineral
interlayers, and a pore-size distribution spanning orders of magnitude, so the
relation under-predicts the conductivity of the *mobile* fraction and has no
meaning as a grain-size formula at all. The sand result is order-of-magnitude
defensible.

---

## ★★6 — Layered effective conductivities

$$\sum_i b_i K_i = 1(10^{-4}) + 4(10^{-6}) + 5(10^{-7})
= 1.045 \times 10^{-4}\ \mathrm{m^2\,s^{-1}},$$
$$K_h = \frac{1.045 \times 10^{-4}}{10} = 1.045 \times 10^{-5}\ \mathrm{m\,s^{-1}}.$$

$$\sum_i \frac{b_i}{K_i} = \frac{1}{10^{-4}} + \frac{4}{10^{-6}}
+ \frac{5}{10^{-7}} = 10^{4} + 4 \times 10^{6} + 5 \times 10^{7}
= 5.401 \times 10^{7}\ \mathrm{s},$$
$$K_v = \frac{10}{5.401 \times 10^{7}} = 1.852 \times 10^{-7}\ \mathrm{m\,s^{-1}}.$$

Ratio $K_h/K_v = 1.045 \times 10^{-5}/1.852 \times 10^{-7} = 56.4$.

Transmissivity from $K_h$: $T = K_h b = 1.045 \times 10^{-5} \times 10
= 1.045 \times 10^{-4}\ \mathrm{m^2\,s^{-1}} = 9.03\ \mathrm{m^2\,d^{-1}}$
(multiplying by 86400 s d$^{-1}$).

Sanity check on the arithmetic of $K_v$: the sum is dominated by the last term
($5 \times 10^{7}$ of $5.401 \times 10^{7}$, i.e. 92.6%), so $K_v \approx
10/5\times10^{7} = 2.0 \times 10^{-7}$, and the exact value must be $1/1.05$ of
that — $1.852 \times 10^{-7}$ ✔. The 5 m layer with
$K = 10^{-7}\ \mathrm{m\,s^{-1}}$ is half the thickness and controls vertical flow
completely, while $K_h$ is set by the 1 m layer at $10^{-4}$.

---

## ★★★7 — A programme to measure $S_y$ and $S_s$

**Targets.** $S_y$ to $\pm 0.01$; $S_s$ to $\pm 20\%$.

**Experiment 1 — column drainage for $S_y$** (undisturbed sample, saturated, then
drained to equilibrium with a falling head). $S_y = V_{\text{drained}}/V_{\text{sample}}$.
For a sample of $V = 1000\ \mathrm{cm^3}$, $\pm 0.01$ in $S_y$ corresponds to
$\pm 10\ \mathrm{cm^3}$ of water, i.e. $\pm 10\ \mathrm{g}$ by mass. A balance
reading to 0.1 g and a sample bored to $\pm 1\%$ volume meets the target with margin.
The precision requirement is therefore not the instrument but the sample:
**three to five samples are needed**, because $S_y$ is heterogeneous at the
centimetre scale.

**Experiment 2 — $S_s$ from a known recharge event.** With a water-level recorder
of $\pm 5\ \mathrm{mm}$ precision and a recharge event of a known
$\Delta V = 50\ \mathrm{mm}$ of water, $S_s = \Delta V/(b \Delta h)$. For
$b = 25\ \mathrm{m}$ and $S_s = 2 \times 10^{-5}\ \mathrm{m^{-1}}$, the expected
response is
$$\Delta h = \frac{\Delta V}{S_s b} = \frac{0.050}{2 \times 10^{-5} \times 25}
= 100\ \mathrm{m},$$
so a *confined* unit cannot be pushed by rainfall and this experiment must be run
as a pumping test instead. (This is exactly why the arithmetic must be done before
the field programme.) For the pumping-test route, the required precision is set by
the drawdown resolution at late time: resolving $S$ to 20% needs the late-time
drawdown to be measured to about 20%, which $\pm 5\ \mathrm{mm}$ on a
$0.5\ \mathrm{m}$ drawdown satisfies by a factor of 20.

**Experiment 3 — pumping test for $S$ (hence $S_s$).** Fit the Theis solution; the
recovered $S$ is sensitive to the late-time data, so the test must run long enough
for the storativity to appear (see
[04 Well Hydraulics and Pumping Tests](../04-well-hydraulics.md)). State the
fitting window explicitly.

**Systematic errors that precision alone misses.**

1. **Column drainage:** evaporation from the sample and residual air entrapment
   after wetting. A sample that was never fully saturated under vacuum gives a
   *high* $S_y$ that is really desaturation.
2. **Recharge-event method:** any water leaving the unit during the event (leakage
   to an adjacent layer, or lateral flow) is attributed to storage, biasing $S_s$
   high.
3. **Pumping test:** the abstraction rate itself and partial penetration of the
   well; both change the drawdown curve's shape in ways that can be absorbed into
   $S$.

---

## ★★★8 — Which uncertainty to attack

Baseline for ★5's sand: $K = 2.697 \times 10^{-4}\ \mathrm{m\,s^{-1}}$ at
$c_{\text{KC}} = 180$.

**$c_{\text{KC}}$ from 10 to 200** (the constant appears to the first power, so $K$
scales as $1/c_{\text{KC}}$):

| $c_{\text{KC}}$ | $K$ (m s$^{-1}$) | relative to 180 |
|---|---|---|
| 10 | $4.855 \times 10^{-3}$ | $18.0\times$ |
| 180 | $2.697 \times 10^{-4}$ | $1.0\times$ |
| 200 | $2.428 \times 10^{-4}$ | $0.90\times$ |

Range: a factor of **20.0**.

**$n$ uncertain by $\pm 15\%$** ($n = 0.30 \to 0.255$ or $0.345$):

| $n$ | $K$ (m s$^{-1}$) | relative to $n = 0.30$ |
|---|---|---|
| 0.255 | $1.462 \times 10^{-4}$ | $0.54\times$ |
| 0.300 | $2.697 \times 10^{-4}$ | $1.00\times$ |
| 0.345 | $4.685 \times 10^{-4}$ | $1.74\times$ |

Range: a factor of **3.20**.

**$n$ from a density log with $\pm 0.02$ porosity units** ($n = 0.28$ or $0.32$):

| $n$ | $K$ (m s$^{-1}$) | relative to $n = 0.30$ |
|---|---|---|
| 0.28 | $2.073 \times 10^{-4}$ | $0.768\times$ |
| 0.30 | $2.697 \times 10^{-4}$ | $1.000\times$ |
| 0.32 | $3.469 \times 10^{-4}$ | $1.286\times$ |

Range: $-23\%$ to $+29\%$, a factor of **1.67**.

**Which to attack first.** $c_{\text{KC}}$ dominates by a wide margin (20× against
3.2× against 1.67×), but it is *not reducible by better measurement* — it is a
model constant. The correct response is therefore not to refine $c_{\text{KC}}$ but
to **calibrate it**: measure $K$ on one sample (or from one well test) and solve
the relation for $c_{\text{KC}}$. That removes the $c_{\text{KC}}$ term from the
budget entirely and leaves $n$ as the leading uncertainty, which *is* reducible —
by a grain-density measurement and a caliper log rather than an assumed
$2.65\ \mathrm{g\,cm^{-3}}$. So: calibrate the model constant once, then spend the
effort on porosity. If no calibration is possible, the honest statement is that
$K$ from grain size is known to within a factor of 20 at best, and no amount of
care with $n$ will change that.

---

## Mastery checkpoint — worked

Synthetic core: $\rho_b = 2.05\ \mathrm{g\,cm^{-3}}$, assumed
$\rho_s = 2.67\ \mathrm{g\,cm^{-3}}$, $K = 2.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$
at $20\ ^\circ\mathrm{C}$, $b = 15\ \mathrm{m}$ over $A = 1\ \mathrm{km^2}$.

**(a) Total porosity.**
$$n = 1 - \frac{2.05}{2.67} = 1 - 0.767790 = 0.23221.$$
The value is a *density* porosity: if the true grain density were
$2.62\ \mathrm{g\,cm^{-3}}$ (a clay-bearing rock) rather than 2.67, then
$n = 1 - 2.05/2.62 = 0.21756$ — 1.5 porosity units lower, i.e. a 6.3% relative
error in $n$ from the mineralogy assumption alone.

**(b) Specific retention and the ordering.** With $n_e = 0.20$ and $S_y = 0.15$:
$$S_r = n_e - S_y = 0.05, \qquad S_y = 0.15 < n_e = 0.20 < n = 0.23221.$$
The gap $n - n_e = 0.032$ is connected-but-immobile or isolated pore water; the
gap $n_e - S_y = 0.05$ is water that can move but does not drain under gravity.
Both gaps are real and both are excluded from a yield calculation.

**(c) Water in place and drainable volume per km$^2$.**
$$V_{\text{in place}} = n A b = 0.23221 \times 10^{6} \times 15
= 3.483 \times 10^{6}\ \mathrm{m^3},$$
$$V_{\text{drainable}} = S_y A b = 0.15 \times 10^{6} \times 15
= 2.25 \times 10^{6}\ \mathrm{m^3}.$$
The difference is $1.233 \times 10^{6}\ \mathrm{m^3}$ — a resource estimate that
used $n$ instead of $S_y$ would overstate the yield by 55%
($3.483/2.25 = 1.548$).

**(d) Intrinsic permeability.**
$$k = \frac{K\mu_w}{\rho_w g} = \frac{(2.0 \times 10^{-5})(1.002 \times 10^{-3})}
{1000 \times 9.81} = 2.043 \times 10^{-12}\ \mathrm{m^2}
= 2.070\ \mathrm{D}.$$

**(e) Kozeny–Carman grain size.** Solve for $d$ with $c_{\text{KC}} = 180$:
$$d = \sqrt{\frac{K\,\mu_w\,c_{\text{KC}}(1-n)^{2}}{\rho_w g\,n^{3}}}
= \sqrt{\frac{(2.0\times10^{-5})(1.002\times10^{-3})(180)(0.76779)^{2}}
{(1000)(9.81)(0.23221)^{3}}}$$
$$= \sqrt{1.731 \times 10^{-8}} = 1.316 \times 10^{-4}\ \mathrm{m}
= 0.132\ \mathrm{mm}.$$
Back-substitution returns $K = 2.000 \times 10^{-5}\ \mathrm{m\,s^{-1}}$ ✔.
**Is it consistent?** $0.132\ \mathrm{mm}$ is a fine-sand grain size, which for a
clean granular sediment at $n = 0.23$ is chemically and mechanically plausible. But
the measured $K$ is *the* input to this inversion, so the test is not
self-consistent by construction — it only checks that the required grain size is
physically sensible. A *matrix* permeability of $2 \times 10^{-5}\
\mathrm{m\,s^{-1}}$ with $0.13\ \mathrm{mm}$ grains is plausible for a well-sorted
fine sand; the same $K$ in a fractured rock would be a *fracture* permeability and
Kozeny–Carman would be the wrong model entirely. Distinguishing the two cases needs
a second, independent measurement (a grain-size analysis, a packer test, or a
borehole image log).

**(f) The question about $S = 0.15$.** Ask: *is the unit confined or unconfined, and
over what area and thickness was $S$ derived?* $S = 0.15$ is a **specific yield**,
i.e. an unconfined storativity: it cannot be the storativity of a confined unit,
where the same rock would give $S = S_s b = 1.0812 \times 10^{-5} \times 15
= 1.622 \times 10^{-4}$ (using $\alpha = 10^{-9}\ \mathrm{Pa^{-1}}$,
$n = 0.23221$, $\beta_w = 4.4 \times 10^{-10}\ \mathrm{Pa^{-1}}$). The two differ
by a factor of 925. If the unit is confined, the number 0.15 is wrong by three
orders of magnitude and a 30 m head decline would release
$1.622 \times 10^{-4} \times 30 \times 10^{6} = 4.87 \times 10^{3}\
\mathrm{m^3}$ per km$^2$, not the $4.5 \times 10^{6}\ \mathrm{m^3}$ implied by
$S = 0.15$.
