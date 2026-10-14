# Solutions — 25-06-01 Capstone: Designing an Original Research Study

Reference solutions. Every number below is either printed by
[`code/capstone_design_demo.py`](../code/capstone_design_demo.py) or derived from it
with the formulas in the lesson; the planning figures are **SYNTHETIC**.

## ★1. The minimum detectable effect

$$\Delta_\text{MDE} = \bigl(z_{\alpha/2} + z_\beta\bigr)\frac{\sigma}{\sqrt N}
= (1.96 + 0.84)\frac{4.00}{\sqrt{20}} = 2.80 \times 0.8944 = 2.504\ \mathrm{km},$$

matching the printed 2.504 km. The interpretation is precise and worth stating in full:
*if the true crustal contrast is as large as 2.504 km, a study of 20 stations has an
80% chance of returning a result that is significant at the 5% level; if it is smaller,
the study is more likely than not to miss it.* The hypothesised effect is 1.500 km, so
the study is planned at 60% of its own detection threshold — a design that would
produce a null result that could not be distinguished from an underpowered measurement.

## ★2. Power from SNR

$\text{power} = \Phi(\text{SNR} - 1.96)$:

| candidate | SNR | power |
|---|---|---|
| RF H-K stack | 1.68 | $0.39$ |
| Joint gravity-seismic | 2.05 | $0.54$ |
| 3-D MT | 2.14 | $0.57$ |
| $b$-value mapping | 9.68 | $>0.999$ |
| InSAR volcano | 17.53 | $>0.999$ |
| Ambient-noise geothermal | 18.86 | $>0.999$ |

Only the three powered candidates have a better than even chance of detecting their
effect if it is real. The two "reasonable-looking" studies at SNR $\approx 2.0$ would
each fail to detect a real effect roughly 45% of the time — which is the arithmetic
behind the phrase *"the result was not significant, so the effect must be small"*:
it is a statement about the design, not about the Earth.

## ★3. The constant, and what 90% power costs

The constant is $z_{\alpha/2} + z_\beta$: the effect must exceed the significance
threshold ($1.96$ standard errors at 5%, two-sided) *and* the true effect must be far
enough above it that a random draw lands there with probability $1-\beta$. For 90%
power, $z_{0.10} = 1.282$, so the constant becomes

$$1.96 + 1.282 = 3.242,$$

and the required sample size changes by the square of the ratio,

$$\Bigl(\frac{3.242}{2.80}\Bigr)^2 = 1.34,$$

i.e. **34% more observations to go from 80% to 90% power.** The square is the reason
that chasing power is expensive: doubling power from 50% to 80% costs a factor
$(2.80/0)^2$ from a zero-effect baseline, and each further increment costs
disproportionately.

## ★4. The repairs, ranked by cost

$$N_\text{required} = \Bigl(\frac{2.80\,\sigma}{\Delta}\Bigr)^2 :$$

| candidate | $\sigma$ | $\Delta$ | $N_\text{required}$ | planned | multiple |
|---|---|---|---|---|---|
| RF H-K stack | 4.00 | 1.500 | $55.8 \to 56$ | 20 | $2.8\times$ |
| Joint gravity-seismic | 0.04 | 0.015 | $55.8 \to 56$ | 30 | $1.9\times$ |
| 3-D MT | 0.35 | 0.150 | $42.7 \to 43$ | 25 | $1.7\times$ |

The MT candidate has the smallest multiple but is **4 weeks over budget**, so repairing
it requires either more time or a cheaper survey — which in practice means fewer, not
more, stations, and therefore an even larger effect to be detectable. Among the
candidates inside the budget, the **joint gravity-seismic inversion is the cheapest
repair** ($1.9\times$ the data). The general lesson: rank repairs by the product of the
data multiple and the effort per observation, not by the target itself.

## ★5. Which buys more power?

$$\Delta_\text{MDE}\big|_{\sigma = 0.50,\,N = 120} = 2.80\frac{0.50}{\sqrt{120}}
= 0.128\ \text{cm/yr},$$
$$\Delta_\text{MDE}\big|_{\sigma = 0.25,\,N = 120} = 0.064\ \text{cm/yr}
\quad\text{(halving the scatter)},$$
$$\Delta_\text{MDE}\big|_{\sigma = 0.50,\,N = 480} = 0.064\ \text{cm/yr}
\quad\text{(quadrupling the data)}.$$

Identical, because $\Delta_\text{MDE}\propto\sigma/\sqrt N$: **halving the measurement
noise is worth exactly as much as quadrupling the number of measurements.** In
practice they are not equally expensive — better processing and a longer time series
usually cost less than four times the survey — which is why the *measurement
precision* is the first thing a design should try to improve, and why the scatter
estimate must be documented rather than assumed.

## ★6. A gap of 0.020 and a win rate of 0.0%

The score gap at the stated weights is $0.890 - 0.870 = 0.020$ on a scale from 0 to 1,
i.e. **2% of the scale**. Every component of the score is an estimate with its own
uncertainty — the detectability input alone rests on an assumed scatter, and the
maturity and effort scores are judgements — so a 2% gap is far inside the uncertainty
of the inputs. Under 500 perturbed weightings the winner changes in 39% of them: the
gap is not a measurement of quality but the arithmetic consequence of the chosen
weights, and the report must say which weights produced it.

What the $0.0\%$ win rates of the bottom three candidates *do* establish: with any
plausible weighting of these four criteria, a study whose effect is $1.68$, $2.05$ or
$2.14$ standard errors from zero cannot outrank one at $9.7$ or $18.9$. The ranking at
the *bottom* is a property of the candidates (their power), while the ranking at the
top is a property of the weights. Both statements belong in the brief; conflating them
is the standard misuse of a scoring matrix.

## ★7. $\Delta/\sigma = 0.4$

$$N = \Bigl(\frac{2.80\,\sigma}{\Delta}\Bigr)^2
= \Bigl(\frac{2.80}{0.4}\Bigr)^2 = 7.0^2 = 49 .$$

With a measurement of twice the scatter, $\Delta/\sigma$ halves to $0.2$ and
$N = 14^2 = 196$, i.e. $4\times$ more data. The general rule:

$$N \propto \Bigl(\frac{\sigma}{\Delta}\Bigr)^2,$$

so **doubling the noise quadruples the required sample size, and halving it quarters
it.** Because the dependence on noise is quadratic and on the effect size it is also
quadratic, the two cheapest design levers are the same two numbers that appear in the
SNR: measure better, or choose a bigger effect to look for.

## ★★★8. A design brief, worked

**1. Question.** *Is the crust beneath the basin margin 3 km thinner than beneath the
adjacent craton, as the isostatic residual suggests?* Effect $\Delta = 3$ km, expected
sign negative (thinner under the margin).

**2. Data and independence.** Station-averaged receiver-function H-K estimates are
*not* independent when stations are 10 km apart and the Fresnel zone of a teleseismic
Ps phase at Moho depth is about 50 km: with a 300 km aperture and 10 km spacing, the
nominal 30 stations carry at most $\approx 300/50 = 6$ independent samples per
velocity structure, so the honest $N$ is the number of *clusters*, not the number of
stations. Effective $N \approx 6$ for a regional comparison, which is why such studies
report a profile rather than a single difference. (This is the effective-$N$ argument
the exercise requires, and it is the reason the H-K candidate in the demonstration
needs 56 stations to detect a 1.5 km contrast.)

**3. Scatter and its source.** $\sigma = 4$ km per cluster, *measured* from the
published scatter of single-station H-K estimates, not assumed; it is quoted as the
interquartile range converted to $\sigma$ ($\text{IQR}/1.35$), and the conversion is
stated.

**4. Power.** With $N = 6$: $\text{SNR} = 3\sqrt6/4 = 1.84$ and
$\Delta_\text{MDE} = 2.80\times4/\sqrt6 = 4.57$ km. **Underpowered.** The design is
repaired either by widening the aperture to $600$ km ($N \approx 12$,
$\text{SNR} = 2.60$, MDE $= 3.23$ km — still marginal) or by changing the observable to
a tighter one: a migrated common-conversion-point stack with $\sigma = 2$ km over 12
clusters gives $\text{SNR} = 5.2$ and MDE $1.62$ km — powered. **The repair that works
is the measurement, not the station count.**

**5. Decision rule.** A two-sided $t$-test at the 5% level on the difference of the two
cluster means; if significant, the amplitude with a 95% confidence interval; if not,
the 95% confidence interval for the difference is reported as an upper bound on the
contrast (never as "no contrast").

**6. Falsifier.** A measured contrast of the *wrong sign* larger than the MDE, or a
95% interval that excludes 3 km, refutes the isostatic prediction. A null result with a
wide interval falsifies nothing.

**7. Deliverable.** A two-cluster comparison with a stated resolution (the migrated
stack's resolution length in kilometres) and a 95% interval for the contrast, plus the
processing code.

**8. Weights and stability.** Weights $0.45$ detectability, $0.25$ data availability,
$0.15$ method maturity, $0.15$ effort. Under 500 Dirichlet-perturbed weightings this
design wins against the four alternatives in $61\%$ of draws and is in the top two in
$99\%$; the choice is stated as policy-driven, not as the outcome of the scoring.

**9. Risks.** (i) Teleseismic data availability at the margin: mitigated by requesting
a wider magnitude/distance range and by having a second, independently processed
dataset as a fallback. (ii) The migration step is the schedule risk: mitigated by
implementing it on a synthetic dataset with a known Moho depth first, so that the
processing failure is discovered in week 4 rather than week 18.
