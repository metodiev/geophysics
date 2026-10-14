# Solutions — 23-06-08 Laboratory Uncertainty Budgets and Reporting

The lesson is [08 Laboratory Uncertainty Budgets and Reporting](../08-lab-data-uncertainty.md).
All values are **SYNTHETIC**.

## ★1

$$u_A = \frac{s}{\sqrt{n}} = \frac{0.30}{\sqrt{9}} = 0.10000,$$

$$u_B(\text{certificate}) = \frac{U}{k} = \frac{0.80}{2} = 0.40000,$$

$$u_B(\text{resolution}) = \frac{0.02}{2\sqrt{3}} = 0.00577,$$

$$u_B(\text{temperature}) = \frac{0.04}{\sqrt{3}} = 0.02309 .$$

Note the two different rectangular conventions and why both appear: a **resolution** of
0.02 means a value anywhere in a ±0.01 interval, so $a = 0.01$ and
$a/\sqrt{3} = 0.00577$; a **temperature coefficient** quoted as "±0.04" is usually the
half-width itself, so $a = 0.04$ and $u = 0.02309$. Getting this wrong changes a term by a
factor of two, and it is the commonest Type B error in laboratory budgets.

## ★2

$$u_c = \sqrt{0.10000^{2} + 0.40000^{2} + 0.00577^{2} + 0.02309^{2}}
= \sqrt{0.010000 + 0.160000 + 0.000033 + 0.000533}
= \sqrt{0.170566} = 0.412997,$$

$$U = 2u_c = 0.825994 .$$

| Term | $u$ | Variance share |
|---|---|---|
| repeatability | 0.10000 | 5.86 % |
| certificate | 0.40000 | **93.80 %** |
| resolution | 0.00577 | 0.02 % |
| temperature | 0.02309 | 0.31 % |

The certificate dominates at 93.80 %: nine repeats were performed to constrain a term that is
5.86 % of the variance, and improving it by a factor of three would change $u_c$ from 0.412997
to $\sqrt{0.160533+0.000011+0.000533} = 0.401134$, i.e. 2.9 %. The lesson's recommendation
follows directly: **find the dominant term before spending effort on repeats**.

## ★3

$$\nu_{\text{eff}} = \frac{u_c^{4}}{\sum \dfrac{u_i^{4}}{\nu_i}}
= \frac{0.412997^{4}}{\dfrac{0.10000^{4}}{8}} ,$$

with the Type B terms having infinite degrees of freedom (their $u_i^4/\nu_i \to 0$). With
$u_c^4 = 0.029111$ and $0.10000^4/8 = 1.25\times10^{-5}$:

$$\nu_{\text{eff}} = \frac{0.029111}{1.25\times10^{-5}} = 2327
\;\Rightarrow\; t_{95}(2327) = 1.961 .$$

So the coverage factor is effectively 1.96 — a **well-measured Type A term combined with
dominant Type B terms** gives a large $\nu_{\text{eff}}$ even with only nine repeats. The
general rule: $\nu_{\text{eff}}$ is governed by the *smallest* uncertainty terms with finite
degrees of freedom, so a budget dominated by an infinite-dof certificate is automatically
well-behaved, and a budget dominated by a 2-repeat Type A term is not.

## ★4

$$\phi = \frac{4.20}{0.998 \times 18.44} = \frac{4.20}{18.4031} = 0.228222
= 22.8222\ \% .$$

| Term | Relative $u$ | Variance share |
|---|---|---|
| mass difference $4.20 \pm 0.015$ g | 0.3571 % | **81.49 %** |
| bulk volume $18.44 \pm 0.030$ cm³ | 0.1627 % | 16.91 % |
| fluid density $0.998 \pm 0.0005$ | 0.0501 % | 1.60 % |

$$\frac{\delta\phi}{\phi} = \sqrt{0.3571^{2} + 0.1627^{2} + 0.0501^{2}}\ \%
= \sqrt{0.12752 + 0.02647 + 0.00251}\ \% = 0.3956\ \% ,$$

$$u(\phi) = 0.3956\ \% \times 22.8222 = 0.0903 \text{ points}, \qquad
U = 2 \times 0.0903 = \mathbf{0.18}\ \text{points} .$$

So the reportable statement is $\phi = 22.82 \pm 0.18\ \%$ ($k = 2$, $n$ specimens), with the
**mass difference** as the dominant term. Note how small the numbers are: this specimen is
much smaller than the lesson's (18.4 cm³ of pore-free volume against 32.6), so the same
absolute uncertainties are relatively larger, and the volume term has risen from 21 % to 17 %
of the variance while the mass term stayed dominant at 81 %.

## ★5

$$d = 12.40 - 12.30 = 0.10, \qquad
u_{\text{combined}} = \sqrt{0.05^{2} + 0.04^{2}} = \sqrt{0.0025+0.0016}
= \sqrt{0.0041} = 0.06403,$$

$$E_n = \frac{0.10}{0.06403} = 1.562 .$$

**Verdict: inconsistent** ($E_n > 1$), but only just — the difference is 1.56 times the
combined standard uncertainty, so the two results are unlikely to come from the same
distribution but not wildly so.

What to do next, in order:

1. **Check the units and the basis.** A factor of 10 or a dry-mass/wet-mass confusion produces
   exactly this kind of "small" discrepancy.
2. **Compare the protocols rather than the numbers**: specimen preparation, saturation, the
   temperature, the calibration chain. A difference of 0.10 on a property of 12.3 (0.8 %) is
   the size of a preparation difference, not of a repeatability difference.
3. **Re-examine the budgets for an omitted systematic term** — a shared reference with a
   correlated error, a temperature coefficient applied only by one laboratory, a rounding
   difference. If one laboratory's budget is missing a 0.05 term, its honest $u$ is larger and
   $E_n$ falls below 1.
4. **Only then** consider a third measurement or a referee laboratory.

What **not** to do: report the average of the two, which hides the inconsistency and produces
a value supported by no measurement; or inflate both budgets until $E_n < 1$, which is the
same error with better manners.

## ★6

A model answer.

**Uncertainty statement per property.** Each must carry value, $U$, $k$ (or the coverage),
$n$, the dominant term and the conditions. For example:

| Property | Statement | Dominant term | Conditions |
|---|---|---|---|
| Porosity | $22.8 \pm 0.4$ % ($k = 2$, $n = 40$) | mass difference (81 %) | dried to constant mass, $\rho_w = 0.998$ g/cm³ |
| Permeability | $1.06 \pm 0.12$ mD ($k = 2$, $n = 12$) | differential pressure (75 %) | Klinkenberg-corrected, gas, 20 °C, $P_e$ stated |
| $V_P$ | $4.50 \pm 0.05$ km/s ($k = 2$, $n = 40$) | timing/delay (75 %) | 1 MHz, dry, 20 °C, net travel time |
| $V_S$ | $2.60 \pm 0.04$ km/s ($k = 2$, $n = 40$) | coupling repeatability | 0.5 MHz, dry, 20 °C |
| Thermal conductivity | $2.18 \pm 0.09$ W/(m·K) ($k = 2$, $n = 12$) | temperature drop and contact series | 20–100 °C, dry, divided bar, thickness series |

**The two properties dominated by preparation rather than the instrument.** Both are
demonstrable with the lessons' arithmetic:

1. **Porosity**, where the between-specimen variability (1.5 points from
   [01](../01-sample-preparation.md)) gives a standard error of 0.24 points at $n = 40$, while
   the instrument terms contribute 0.09 points — so the reported uncertainty is **2.6× larger
   than the instrument's** and is entirely a sampling and preparation statement. The arithmetic:
   $1.5/\sqrt{40} = 0.237$ against $u_{\text{instr}} = 0.090$, and
   $\sqrt{0.237^2+0.090^2} = 0.254$ points, i.e. 0.51 points at $k = 2$.
2. **Permeability**, where the Klinkenberg extrapolation and the specimen's own heterogeneity
   contribute more than the flow measurement, and where the saturation state
   ([01](../01-sample-preparation.md)) changes the value by more than the instrument's budget —
   the gas measurement at one pressure is 2.6× the liquid-equivalent value in the lesson's
   example, so a protocol error dwarfs any instrument improvement.

**Metadata for the data table.** Per property: the instrument and its calibration date; the
method; the conditions (temperature, saturation, fluid, pressure/stress, frequency); the
number of determinations and what "one determination" means (one specimen or one repeat); the
uncertainty, its coverage factor and its dominant term; and the traceability statement with
the reference's uncertainty.

**Inter-laboratory comparison.** Two or three specimens of the same lithology, circulated
between the participating laboratories, with **the same protocol** specified in advance (this
is what makes the comparison a test of the measurement and not of the preparation). Criterion:
$E_n \le 1$ for each property, and for a $k = 2$ budget an $E_n$ in the range 0.5–1 is the
expected outcome of a *sound* budget — values far below 1 should trigger a review of the
budgets for overstatement, and values above 1 a review of the protocols for an omitted
systematic term.

**What the reader cannot recover, and the sentence that fixes it.** The reader cannot know
which *specimen* each value belongs to once the table is averaged, nor whether the values were
measured on the same plugs — so the correlations between properties (porosity and velocity,
say) cannot be reconstructed, and neither can the fact that a batch of specimens shared one
preparation error. The sentence to add:

> "All properties in each row were measured on the same specimen. The uncertainties are
> quoted per property and are not independent: all specimens in this table were dried and
> saturated in a single batch, so a batch-level systematic error in saturation would shift
> every porosity and every velocity in the same direction."

That sentence turns a table of numbers into a dataset that can be used responsibly.
