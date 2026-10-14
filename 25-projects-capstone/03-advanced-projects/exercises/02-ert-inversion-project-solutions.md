# Solutions — 25-03-02 Project: ERT Inversion with Resolution Assessment

> Read after attempting. Lesson:
> [02 ERT Inversion](../02-ert-inversion-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/ert_inversion_demo.py`](../code/ert_inversion_demo.py).

---

## ★1 — Reflectance and limits

$$k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1} = \frac{500-50}{500+50} = \frac{450}{550}
= 0.8182.$$

**Limits.** At very short spacing the current never reaches the second layer, so
$\rho_a \to \rho_1 = 50\ \Omega\,\mathrm{m}$. At very long spacing the current
samples the half-space, so $\rho_a \to \rho_2 = 500\ \Omega\,\mathrm{m}$. The
approach is algebraic in $a/h$, not exponential, which is why even a spacing of
$6h$ has not converged: the demonstration's curve reaches
$483\ \Omega\,\mathrm{m}$ against $1000\ \Omega\,\mathrm{m}$ at
$a = 6h = 60\ \mathrm{m}$.

---

## ★2 — Misfit per datum and per degree of freedom

$$\frac{\chi^{2}}{n} = \frac{28.631}{25} = 1.145, \qquad
\frac{\chi^{2}}{\nu} = \frac{28.631}{25-3} = \frac{28.631}{22} = 1.301.$$

The demonstration prints the rms residual $1.070\sigma = \sqrt{1.145}$.

**Which belongs in a report.** The **per-degree-of-freedom** value is the
statistical test: with a correct noise model, $\chi^{2}/\nu$ has unit expectation
and standard deviation $\sqrt{2/\nu} = \sqrt{2/22} = 0.302$, so $1.301$ is
$1.0\sigma$ above expectation — an acceptable fit. The per-datum value is the
rms residual and is the more intuitive summary of the scatter, but it is not the
test statistic because the 3 fitted parameters have absorbed some of the
misfit. Quote both, and say which is which.

---

## ★3 — Absolute uncertainties

| parameter | fitted | relative 1σ | absolute 1σ |
|---|---|---|---|
| $\rho_1$ | $100.367\ \Omega\,\mathrm{m}$ | $1.43\%$ | $\pm 1.44\ \Omega\,\mathrm{m}$ |
| $\rho_2$ | $1155.38\ \Omega\,\mathrm{m}$ | $11.42\%$ | $\pm 131.9\ \Omega\,\mathrm{m}$ |
| $h$ | $10.5558\ \mathrm{m}$ | $4.20\%$ | $\pm 0.443\ \mathrm{m}$ |

Note that the $\rho_2$ interval of $\pm 132\ \Omega\,\mathrm{m}$ does **not**
contain the true $1000\ \Omega\,\mathrm{m}$ at $1\sigma$ (the error is
$155\ \Omega\,\mathrm{m} = 1.18\sigma$), so the demonstration's fit is a
$1.2\sigma$ fluctuation — entirely ordinary, and a reminder that a single
realisation of a noisy inverse problem lands inside its own error bar only about
$68\%$ of the time.

---

## ★★4 — The trade-off exponent

Using natural (or any consistent) logarithms:

$$\frac{\mathrm{d}\ln\rho_2}{\mathrm{d}\ln h}
= \frac{\ln(2233.8/721.1)}{\ln(13.00/8.00)}
= \frac{1.1304}{0.4855} = 2.33.$$

So along the trade-off, $\rho_2 \propto h^{2.33}$: a $10\%$ increase in thickness
requires a $26\%$ increase in half-space resistivity to keep the same fit.

Transverse resistance $\rho_2 h$: $721.1 \times 8.00 = 5.77\times10^{3}$ and
$2233.8 \times 13.00 = 2.90\times10^{4}\ \Omega\,\mathrm{m^{2}}$ — a ratio of
$5.03$ for a thickness ratio of only $1.625$.

**Which is conserved.** Neither is conserved to better than a factor of two, which
is itself the result: this sounding is neither in the thin-layer (transverse
resistance) nor the conductive-layer (conductance) equivalence regime over the
spacings observed. The honest statement is that the trade-off is **local and
steep** — exponent $2.33$ — rather than an exact equivalence with a conserved
product, and the only way to state it is to tabulate the accepted pairs as in
§5(b) of the lesson.

---

## ★★5 — Depth of investigation

$$a/2 = \frac{36.68}{2} = 18.34\ \mathrm{m}, \qquad
a/3 = \frac{36.68}{3} = 12.23\ \mathrm{m}.$$

**Can a 25 m thick surface layer be resolved?** No, on either rule. The
sensitivity-based depth of investigation is $12$–$18\ \mathrm{m}$, and the longest
spacing (60 m) probes to about $30\ \mathrm{m}$ only under the most generous
$a/2$ rule applied to the *maximum* spacing. A 25 m layer sits at or beyond the
limit of what this spread constrains, so its thickness would be reported as a
number driven by the parameterisation rather than by the data — which is exactly
the situation the depth-of-investigation calculation exists to detect. The fix is
more spread: to place the 50%-sensitivity spacing beyond 50 m requires spacings
beyond 100 m, i.e. about a factor of three more electrode spread.

---

## ★★6 — Linearised versus profile interval

$$\frac{\pm 0.35}{\pm 0.44} = 0.80,$$

so the profile interval is $20\%$ narrower. The profile likelihood re-optimises
the other two parameters at each fixed $h$, so it measures the *true* shape of
the one-dimensional misfit surface, whereas the linearised interval extrapolates
the surface's curvature at the minimum and assumes it stays quadratic out to
$\Delta\chi^{2}=1$. Here the surface steepens faster than the quadratic
approximation predicts, which is the ordinary behaviour of an inverse problem in
log-parameters when the noise is multiplicative rather than additive.

**Which to quote.** The **linearised** interval, because it is the conservative
one, with the profile interval reported alongside as evidence that the
non-linearity is mild ($20\%$, not a factor of two). Quoting the narrower
interval alone would understate the uncertainty, and quoting only one of the two
hides the check.

---

## ★★★7 — Acquisition for $\pm 10\%$ at 30–50 m

**Array.** A **dipole–dipole** or **pole–dipole** configuration: it gives the
best lateral and vertical resolution per electrode for a horizontally layered
target, and its sensitivity kernel is concentrated where the two dipoles'
geometry places it, which can be tuned. Wenner would need a much larger spread
for the same investigation depth because its DOI is only about $a/2$.

**Spacing and spread.** To place the 50%-sensitivity spacing beyond 50 m, the
smallest dipole separation needs to be around $10\ \mathrm{m}$ and the maximum
separation around $60$–$80\ \mathrm{m}$, giving a maximum spread of
$n \times a$ with $n \approx 6$–8 separations. That means a **spread of
$500$–$700\ \mathrm{m}$** end to end for a 50 m target — the standard rule of
thumb that a resistivity survey needs a spread of roughly ten times the target
depth.

**Electrodes.** With a 10 m takeout and a 600 m spread: **about 60 electrodes**,
plus a multichannel resistivity meter and a switch box. That electrode count is
the cost driver: acquisition time scales with the number of quadrupoles
(roughly $n^{2}$ combinations), and cable and takeout installation dominates the
field day.

**Expected depth of investigation.** $50$–$80\ \mathrm{m}$ by the sensitivity
criterion, comfortably including the 30–50 m target.

**The failure test, run before reporting.** Three checks:

1. **Sensitivity check.** Compute the normalised sensitivity of $\rho_a$ to the
   target layer's resistivity against spacing; if it does not reach half its
   maximum within the acquired spacings, the requirement is unmet.
2. **Synthetic recovery.** Invert a synthetic model with the same geometry and
   noise level, and measure the recovered thickness and its $\pm 10\%$ interval;
   if the synthetic interval is wider than $\pm 10\%$, the field result cannot be
   better.
3. **Profile-likelihood check on the real data.** Report the $\Delta\chi^{2}=1$
   interval for the target depth; if it exceeds $\pm 10\%$, say so rather than
   quoting the best fit.

**Cost driver.** Electrode count and spread length (cable, labour, and the
$n^{2}$ scaling of quadrupole measurements), followed by the inversion and
reporting effort. Spending on *spread* rather than on *electrode density* is the
usual correct trade for a depth requirement.
