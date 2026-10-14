# Solutions — 21-06-07 ML for Climate Downscaling and Emulation

> Read after attempting. Lesson:
> [07 Climate ML](../07-climate-ml.md). Numbers are **SYNTHETIC**, printed by
> [`code/climate_ml_demo.py`](../code/climate_ml_demo.py).

---

## ★1 — Recovering the lapse rate

$$\beta_2 = -0.00647\ \mathrm{K/m} \times 1000 = -6.47\ \mathrm{K/km},$$

against a true western lapse rate of $6.50$ K/km:

$$\text{error} = \frac{6.47 - 6.50}{6.50} = -0.46\% .$$

The check works here because the truth is a *construction*: the generator states
the lapse rate, so a fitted coefficient can be compared with a known number. In a
real study the environmental lapse rate is itself estimated (from radiosondes or
reanalysis), so the comparison is against another estimate with its own error, and
a discrepancy of half a per cent cannot be attributed to the model. The exercise
is still worth doing on real data: the *sign* and order of magnitude of an
elevation coefficient is a physical check that catches a sign error, a units
error, or elevation entered in feet.

---

## ★2 — RMSE ratios by transfer

| method | later period / in-sample | other region / in-sample |
|---|---|---|
| bilinear interpolation | $1.186/1.169 = 1.01$ | $0.754/1.169 = 0.64$ |
| linear emulator | $0.193/0.166 = 1.16$ | $0.558/0.166 = 3.36$ |
| quadratic emulator | $0.277/0.160 = 1.73$ | $0.556/0.160 = 3.48$ |

The temporal ratio isolates the **distributional** transfer: for the correctly
specified linear model it is $1.16$, i.e. a $16\%$ penalty for a 3.32 K warming.
The spatial ratio isolates the **structural** transfer, and it is $3.36$ — twenty
times larger in absolute terms. The interpolation row is instructive: its
spatial ratio is *below* 1 because its missing elevation term happens to cost less
in the east, where the true lapse rate is weaker.

---

## ★3 — Distance from the noise floor

Floor: 0.15 K.

| method | in-sample | later period | other region | both shifts |
|---|---|---|---|---|
| bilinear | 7.8 | 7.9 | 5.0 | 5.2 |
| linear | 1.11 | 1.29 | 3.72 | 3.76 |
| quadratic | 1.07 | 1.85 | 3.71 | 3.98 |

Only the linear and quadratic models in-sample and the linear model in the later
period are within about $1.3\times$ of the floor — that is, only the correctly
specified model, on the transfer it can handle. Everything else is at least
$1.85\times$ the floor, and the two structural blocks are $3.7$–$5.2\times$.
Reporting the floor is what makes the table interpretable: without it, 0.166 K
looks like "good" and 0.558 K looks like "acceptable", when the first is near
perfect and the second is a $3.7\times$ excess over the irreducible residual.

---

## ★4 — Predicting the eastern error from the lapse mismatch

For a cell with elevation anomaly $\Delta z$ (fine elevation minus coarse-cell
mean), the truth is $y = T_c - \Gamma_e \Delta z + \text{(nonlinear term)}$ and
the model predicts $\hat y = T_c - \Gamma_w \Delta z$, so

$$\text{error} = (\Gamma_e - \Gamma_w)\,\Delta z
= (3.0 - 6.5)\times10^{-3}\,\mathrm{K/m}\times\Delta z .$$

With $\mathrm{sd}(\Delta z) = 120$ m:

$$\mathrm{RMSE} \approx \lvert \Gamma_e - \Gamma_w\rvert\,\mathrm{sd}(\Delta z)
= 3.5\times10^{-3} \times 120 = 0.42\ \mathrm{K}.$$

The measured value is $0.558$ K, larger by about $33\%$, which the remaining terms
account for: the small nonlinear term of the generator, the residual noise
($0.15$ K, adding $0.15^2 = 0.0225$ in quadrature: $\sqrt{0.42^2 + 0.15^2} = 0.446$ K),
and the fact that the fitted coefficient carries a little error so the
mis-specification is not exactly $3.5$ K/km. The order of magnitude and the
zero-mean property are both confirmed: the error is proportional to the elevation
anomaly, so it averages to zero over the domain while being large where the relief
is.

Note the contrast with a *bias*: a bias would show up in the mean error column and
could be removed by subtracting a constant. This error cannot be removed by any
constant correction, because it is a function of the predictor.

---

## ★★5 — Separating "bad temperature extrapolation" from over-parameterisation

**Families.** (A) linear in $(T_c, \Delta z)$; (B) quadratic in $T_c$ with the
elevation interaction; (C) a high-capacity model (degree-5 polynomial or a small
gradient-boosted ensemble) as a capacity control.

**Splits.** (i) random cells within the west and months 1–150; (ii) later period,
west; (iii) other region, west-trained; (iv) both.

**Metric.** RMSE and mean error in K, plus the fitted coefficients so that a
coefficient change can be attributed.

**Result patterns.**

| Observed | Interpretation |
|---|---|
| A and B both degrade under the temporal split, by similar factors | the *temperature* range is the problem (both models extrapolate badly) |
| B degrades more than A under the temporal split while both are equal spatially | over-parameterisation: the extra coefficient buys in-sample fit at the cost of extrapolation variance |
| C is best in-sample and worst in every out-of-sample block | capacity, not specification, is the driver |
| B and A both fail spatially by the same factor | a structural mis-specification common to both; capacity is irrelevant |

In this demonstration the second pattern is what occurs ($0.277$ versus $0.193$ K
under warming, $0.556$ versus $0.558$ K across regions), which is why the
temporal block is the one that exposes the quadratic model.

---

## ★★6 — How large is the warming relative to the training range?

The demonstration prints the mean coarse temperature for each period: $13.88$ K
and $17.20$ K, a shift of $3.32$ K. The training period's own *range* is much
wider than that shift: the coarse field is
$12.0 - 0.6\,\text{lat} + 3.0\sin(2\pi t/12) + 0.03t + \mathrm{AR}(1)$, so over
months 1–150 the seasonal term alone spans $\pm3$ K, the latitude term spans
$\pm1.8$ K and the trend adds up to $+4.5$ K, giving a total span of order 12–15 K
across the training set.

So the temporal block asks the model to predict at temperatures
$\tfrac{1}{4}$–$\tfrac{1}{3}$ of one training-range width beyond the training
mean — a **modest** extrapolation, and one the training set already brackets in
part (the warmest training months are close to the coolest test months). That is
why the correctly specified model loses only $16\%$ and why the ill-specified one
loses $73\%$: there is little room for a well-specified model to fail, and just
enough for an over-fitted one to be exposed. A genuinely severe test would hold
out the warm end of the training range entirely, which is what an emulation study
for a strong-forcing scenario must do.

---

## ★★★7 — Detecting a regime-dependent lapse rate in real data

**Diagnostic.** Fit the downscaling regression *with the lapse rate as a
function of a regime indicator* — for example a smooth interaction
$\Gamma(x) = \Gamma_0 + \Gamma_1\,g(x)$ where $g$ is a plausible regime variable
(continentality, a moisture index, snow-cover climatology, or simply longitude) —
and test whether $\Gamma_1$ is distinguishable from zero. Equivalently, fit the
lapse rate separately in two halves of the domain and compare the coefficients
with their standard errors, remembering that the two estimates are correlated.

**Data needed.** A fine-resolution reference (stations or a fine reanalysis) with
enough density in *both* regimes, and a fine elevation dataset that is accurate in
both. The test is the comparison of lapse-rate estimates per regime; the metric is
$\hat\Gamma$ with its standard error, not the downscaled RMSE, because the RMSE
mixes the lapse error with every other error.

**Confound.** Elevation-dependent biases in the input product produce exactly the
same signature: if the coarse product is too warm at high elevation in the east,
the fitted eastern lapse rate is too small even when the true atmosphere has one
lapse rate. The separation requires an independent estimate of the coarse field's
elevation bias — for example from a comparison with radiosondes or from a
triple-collocation study against a second reanalysis. Without it, a regime-varying
$\hat\Gamma$ is not evidence of a regime-varying atmosphere.

**Result that shows the regime rather than the noise.** $\hat\Gamma_1$ exceeds
three standard errors, the two regime estimates bracket physically plausible lapse
rates, and the same pattern is recovered in a period held out from the fit. A
pattern that appears only in-sample, or that moves when the elevation dataset is
swapped, is a data artefact.

---

## ★★★8 — Validating for a future period in a new region

**Blocks.**

1. **Later period, same region** — the distributional transfer; train on the
   earlier part, test on the later, with the warmest part of the record held out
   entirely rather than merely later.
2. **Held-out region** — the structural transfer, chosen to include a regime
   difference (relief, continentality) rather than a convenient split.
3. **Both** — the deployment case, and the only block whose number belongs in an
   abstract that claims future regional skill.
4. **Leave-one-station-out** within each block, to separate station-level
   idiosyncrasy from the transfer.

**Metrics.** RMSE and mean error in K, reported *per elevation band* and per
season, because a domain-averaged RMSE cancels the elevation-dependent error
(measured here: mean error $-0.001$ K with RMSE 0.558 K). Add the lapse-rate
coefficient per block so the mechanism is visible, and the residual's spatial
autocorrelation if the output feeds a downstream model that assumes independence.

**Reference data.** Station observations with their own representativeness
uncertainty (a station is a point; a grid cell is an area), plus an independent
reanalysis for the coarse input, and a stated elevation dataset.

**What the protocol cannot establish.** It cannot establish performance in a
region whose regime is absent from the training pool — a new region with a
different lapse rate, moisture regime or land-cover class is outside every block
listed; nor in a future whose forcing exceeds the training range; nor that the
elevation dataset's errors cancel; and not the station representativeness error,
which is a property of the observation network rather than of the model.

---

## ★★★9 — One headline number

I would choose the **RMSE in K of the combined transfer block** — later period
*and* held-out region — with the mean error beside it, and I would print three
quantities with it:

1. **the transfer definition** — which block the number belongs to (later period,
   other region, both, and the model's training region and period);
2. **the irreducible floor** — the fine-scale residual noise (0.15 K here), so the
   reader can see how much of the RMSE is the model and how much is the data;
3. **the elevation-band or class-conditional breakdown** — the RMSE per elevation
   band (or per season), which is what exposes a mis-specified response hiding
   behind a domain average.

A reader cannot interpret the headline without them, because the same model
produces 0.166 K, 0.193 K, 0.558 K and 0.564 K on four blocks; because "0.56 K"
is either excellent or useless depending on whether the noise floor is 0.15 K or
2 K; and because a single domain average can be zero-bias and still be wrong by
1 K wherever the relief is large — which is exactly where a downscaled field is
usually worth having.
