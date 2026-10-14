# Solutions — 19-08-05 Running a Simple Climate Model

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [05 Running a Simple Climate Model](../05-simulate-climate-model.md).

---

## ★1 — Equilibrium temperature at α = 0.35

$$\frac{(1-0.35)\times1361}{4} = \frac{884.65}{4} = 221.163\ \mathrm{W\,m^{-2}},$$

$$T = \left(\frac{221.163}{5.670374419\times10^{-8}}\right)^{1/4}
= \left(3.9003\times10^{9}\right)^{1/4}.$$

Two square roots: $\sqrt{3.9003\times10^{9}} = 6.2452\times10^{4}$;
$\sqrt{6.2452\times10^{4}} = 249.90$ K. So $T = 249.9$ K, about $4.7$ K below the
$\alpha = 0.30$ value of $254.58$ K.

---

## ★2 — Adding a single grey layer

$$T_s = T_e\left(\frac{2}{2-\varepsilon}\right)^{1/4}
= 249.90\left(\frac{2}{1.1}\right)^{1/4} = 249.90\times1.16158 = 290.3\ \mathrm{K}.$$

So one layer with $\varepsilon = 0.9$ raises the surface by $40.4$ K. Note that the
surface temperature is *not* the layer temperature and is not the effective
temperature: three different temperatures, three different meanings, and confusing
them is the commonest error in reading such a model.

---

## ★3 — Relaxation time

$$\tau = \frac{C}{B} = \frac{2.0\times10^{8}}{1.3} = 1.5385\times10^{8}\ \mathrm{s}
= \frac{1.5385\times10^{8}}{3.15576\times10^{7}} = 4.876\ \mathrm{years}.$$

A run should extend to several $\tau$ — ten times is a safe convention, giving about
$49$ years of model time — before any statement about equilibrium is made. A run of
one $\tau$ leaves $37$ per cent of the initial anomaly, so it cannot support an
equilibrium claim at all.

---

## ★4 — A two-state albedo and consistency

**Warm branch.** Assume $T > 250$, so $\alpha = 0.30$:
$T = ((0.70\times1361)/4/\sigma)^{1/4} = 254.58$ K. Check the assumption:
$254.58 > 250$ ✓ **consistent**, so $254.58$ K is an equilibrium.

**Cold branch.** Assume $T \le 250$, so $\alpha = 0.60$:
$T = ((0.40\times1361)/4/\sigma)^{1/4} = (136.1/5.670374419\times10^{-8})^{1/4}
= (2.4002\times10^{9})^{1/4}$; $\sqrt{}= 4.8992\times10^{4}$,
$\sqrt{}= 221.34$ K. Check: $221.34 \le 250$ ✓ **consistent**.

So with a *sharp* two-state albedo there are **two** consistent equilibria,
$221.3$ K and $254.6$ K, and the model is bistable with no intermediate state. The
smooth transition of the lesson's demonstration produces a third, unstable root
between them (measured $251.89$ K at $S_0 = 1361$ W m$^{-2}$). This is why the shape
of the albedo function — a choice — determines the number of answers: the sharp
version has two, the smooth version three.

---

## ★5 — A manufactured source for T = 1 + 0.5 y⁴

$$T' = 2y^{3}, \qquad (1-y^{2})T' = 2y^{3} - 2y^{5},$$

$$\frac{\mathrm{d}}{\mathrm{d}y}\left[(1-y^{2})T'\right] = 6y^{2} - 10y^{4}.$$

The equation is $D\,\mathrm{d}/\mathrm{d}y[(1-y^{2})T'] + Q - (A + BT) = 0$, so

$$Q(y) = A + B\left(1 + 0.5y^{4}\right) - D\left(6y^{2} - 10y^{4}\right).$$

Substituting back gives an exact continuum residual of zero and a discrete residual
of $O(\Delta y^{2})$, so the measured order is the code's. Note the quartic in $Q$
and the quartic in $T$: the transport term and the feedback both contribute, and a
solution with fewer terms would test fewer of them.

---

## ★6 — Time to a one-kelvin anomaly

$$10\,e^{-t/\tau} = 1 \;\Longrightarrow\; t = \tau\ln 10 = 4.876\times2.302585
= 11.23\ \mathrm{years}.$$

The general relation is $t = \tau\ln(A_0/A)$. Because the decay is exponential,
reaching $1$ K from $10$ K takes $2.30\tau$ and reaching $0.1$ K takes $4.61\tau$:
**each additional decade of closeness costs $\ln 10 = 2.303$ time constants**, which
is why "converged to equilibrium" is a statement that must be quantified before it
is made.

---

## ★7 — A predictive evaluation design

**Observable.** A quantity the model predicts and that was *not* used in
calibration: for example, the annual-mean temperature at a latitude band outside
those used to fit the transport coefficient, or the response to a seasonally varying
insolation the model was never tuned to.

**Split.** Calibrate $A$, $B$ and $D$ on one subset — a latitude range and a
selection of years — and evaluate on the withheld latitudes and years. Report the
calibration residuals and the evaluation residuals separately, with the parameter
count.

**Metric.** Root-mean-square prediction error on the withheld set, compared with the
stated observational uncertainty (so that the comparison is a ratio, not a raw
number), and a *bias* term since a model can have small rms error and a systematic
offset.

**Failure mode that looks like success.** If the withheld set is statistically
similar to the calibration set (same latitudes, adjacent years, the same seasonal
cycle), the "evaluation" is interpolation and a good score means only that the model
can be fitted. The diagnostic is to run the evaluation on data that differs from the
calibration in the *mechanism* being tested — a different season, a different
latitude band, a different forcing — and to check the parameter count against the
number of independent constraints.

---

## ★8 — Reviewing "reproduces the observed temperature record"

**The three questions.**

1. **Was the record used in calibration?** If the parameters were fitted to it, the
   sentence is a restatement of the fit and the honest word is "calibrated".
2. **How many parameters, and how many independent constraints?** If the fitted
   parameters are comparable in number to the independent information in the record,
   the agreement is arithmetic.
3. **Evaluated on what unused observable?** If nothing was withheld, there is no
   prediction test and the claim reduces to curve fitting.

**The strongest defensible claim if all three are unfavourable.** Something of this
form:

> Following the protocol of [19-07-03], the model's four parameters ($A$, $B$, $D$
> and the albedo threshold) were calibrated against the annual-mean temperature
> record, which therefore cannot serve as a test of its validity. On a withheld
> observable — [the chosen variable, unused in the calibration] — the model predicts
> a value of $X \pm Y$, against a measured $M \pm \sigma$; the prediction lies
> $Z\sigma$ from the measurement. The model is accordingly consistent with the
> withheld observable within its stated uncertainty, and we make no claim about
> processes the model does not represent (atmospheric dynamics, clouds, the carbon
> cycle). Its parameters are calibrated and should not be read as measurements.

Every clause of that statement is checkable, which is the point: the claim is not
weaker than the data, and it is not stronger either. Note also what it avoids: the
words "validated", "reproduces the climate", and any number that was fitted.
