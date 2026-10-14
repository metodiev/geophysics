# Solutions — 09-01-02 Archie's Law, Porosity and Saturation

> **Read after attempting the exercises.** Lesson:
> [02 Archie's Law, Porosity and Saturation](../02-archies-law.md).

---

## ★1 — Formation factor and saturated resistivity

$$F = a\phi^{-m} = 1\times0.30^{-2.1} = 12.46, \qquad
\rho_0 = F\rho_w = 12.46\times0.5 = 6.23\ \Omega\,\mathrm{m}.$$

Note $0.30^{-2.1} = \exp(2.1\times1.20397) = \exp(2.5283) = 12.53$; the two
figures differ by rounding, so use one consistent route: $F = 12.53$ and
$\rho_0 = 6.27\ \Omega\,\mathrm{m}$.

---

## ★2 — Saturation

$$\rho_t = \rho_0S_w^{-n} = 6.27\times0.5^{-2} = 6.27\times4
= 25.07\ \Omega\,\mathrm{m}.$$

---

## ★3 — Porosity from $F$

$$\phi = F^{-1/m} = 40^{-1/2} = 0.1581.$$

---

## ★4 — Two points give $(m, a)$

$$m = \frac{\ln(F_2/F_1)}{\ln(\phi_1/\phi_2)}
= \frac{\ln(12/32)}{\ln(0.18/0.30)}
= \frac{\ln 0.375}{\ln 0.60}
= \frac{-0.98083}{-0.51083} = 1.9201,$$

$$a = F_1\phi_1^{m} = 32\times0.18^{1.9201}
= 32\times\exp(1.9201\times(-1.71480)) = 32\times0.03724 = 1.1917.$$

Check with the second point:
$1.1917\times0.30^{-1.9201} = 1.1917\times10.070 = 12.00$ ✔.

---

## ★5 — Error in $\phi$ from an error in $F$

$$\frac{\delta\phi}{\phi} = -\frac{1}{m}\frac{\delta F}{F}.$$

For $m = 2.0$ and $\delta F/F = +0.10$: $-5.0\%$. For $m = 2.5$: $-4.0\%$.

The *larger* exponent is the more forgiving for a given error in $F$ — this is
the counterpart of the lesson's statement that a larger exponent is *less*
forgiving when the exponent itself is wrong (a 25% error in $m$ moved $\phi$ by
more than 30%). Two different sensitivities; do not confuse them.

---

## ★6 — Saturation uncertainty

$$\frac{\delta S}{S} = -\frac{1}{n}\frac{\delta\rho_t}{\rho_t}
= \frac{0.03}{2.2} = 1.36\%, \qquad
\delta S = 0.35\times0.0136 = 0.0048.$$

The target $\pm0.05$ is met with a factor ten to spare — **provided $n$ is
right**. A 10% error in $n$ would produce
$0.35\times(1-1/2.2\times0.909)$-style shifts of order 0.015, i.e. three times
the measurement-driven uncertainty. The measurement is not the limit; the
calibration is.

---

## ★7 — Tortuosity and the exponent

From $F = \tau/\phi$ and $F = a\phi^{-m}$: $\tau = a\phi^{1-m}$. With $a = 1$,
$\tau = \phi^{1-m}$, which is constant only if $m = 1$.

For $m = 2$: $\tau = \phi^{-1}$, so $\tau(0.35) = 2.857$ and
$\tau(0.08) = 12.5$.

Is that defensible? Partly: lower porosity does mean longer, more tortuous paths,
and a pore-scale model with narrow throats does predict a rising tortuosity. But
$\tau = 1/\phi$ is a *specific* functional form with no independent support, and
at $\phi = 0.08$ the implied tortuosity exceeds the value usually associated with
even tight rocks. The defensible statement is that $m$ is an empirical exponent
that *absorbs* the tortuosity variation; treating the implied $\tau$ as a
measurement is an over-interpretation.

---

## ★8 — A calibration programme (specification)

1. **Samples:** at least three porosity levels per rock type, three cores each
   (nine samples), so that sample-to-sample scatter can be separated from the
   porosity trend.
2. **Measurements:** porosity (helium or mercury porosimetry), $\rho_w$ on the
   actual equilibrating brine (not a chart value), and $R$ on each sample at
   several brine salinities to separate $\rho_w$ from the rock term.
3. **$m$:** regress $\log F$ on $\log\phi$; report the confidence interval on
   the slope and intercept, not just the best fit.
4. **$n$:** desaturate one sample stepwise (porous plate or centrifuge), measure
   $S_w$ gravimetrically and $R$ at each step; regress $\log\rho_t$ on
   $\log S_w$.
5. **Model test:** plot residuals against $\phi$ and $S_w$. A systematic
   curvature or a fan-shaped residual pattern shows that a single power law is
   the wrong model for that sample; a clay-rich sample will show it as a
   non-zero intercept in $\log\rho_t$ versus $\log S_w$ (the surface-conduction
   term of [03](03-conduction-mechanisms-solutions.md) and
   [04](04-clay-and-surface-conduction-solutions.md)).
