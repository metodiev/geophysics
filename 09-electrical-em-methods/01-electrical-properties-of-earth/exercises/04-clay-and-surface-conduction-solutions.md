# Solutions — 09-01-04 Clay Effects, CEC and Membrane Polarisation

> **Read after attempting the exercises.** Lesson:
> [04 Clay Effects, CEC and Membrane Polarisation](../04-clay-and-surface-conduction.md).

---

## ★1 — Pore-volume cation excess

$$Q_v = \frac{\mathrm{CEC}}{100}\,\rho_g\,\frac{1-\phi}{\phi}
= \frac{8}{100}\times2.65\times\frac{0.80}{0.20} = 0.08\times10.6
= 0.8480\ \mathrm{eq\,L^{-1}}.$$

---

## ★2 — Surface conductivity

$$\sigma_s = \beta Q_v = 0.10\times0.8480 = 0.08480\ \mathrm{S\,m^{-1}}.$$

---

## ★3 — Chargeability

$$m = \frac{0.025-0.020}{0.025} = 0.2000.$$

---

## ★4 — Saturation with and without the surface term

$$\sigma_w/F = 0.2/0.04 = 5.0\ \mathrm{S\,m^{-1}}$$

using $F = \phi^{-2} = 0.04^{-1} = 25$; more carefully
$F = 1/0.20^{2} = 25$, so
$\sigma_w/F = 0.2/25 = 0.00800\ \mathrm{S\,m^{-1}}$, and

$$\sigma = 0.00800 + 0.08480 = 0.09280\ \mathrm{S\,m^{-1}}
\quad(\text{surface term } 91.4\%).$$

Without correction:

$$S = \left(\frac{0.09280}{0.00800}\right)^{1/2} = 3.406,$$

i.e. 341% — inadmissible.

With correction: $S = \left(\frac{0.09280-0.08480}{0.00800}\right)^{1/2} = 1.000$.

The corrected value is the only admissible one; the uncorrected value violates
the definition of saturation.

---

## ★5 — Why the saturation is invisible

At $S_w = 0.5$, $\sigma_0$ for the electrolytic path falls by the factor
$S^{n} = 0.25$: $0.00800\to0.00200\ \mathrm{S\,m^{-1}}$ (in the notation of
[02](../02-archies-law.md), $\rho_t = \rho_0S^{-n}$ so $\sigma_t = \sigma_0S^{n}$).
The surface term is essentially unchanged:

$$\sigma(0.5) = 0.00200 + 0.08480 = 0.08680\ \mathrm{S\,m^{-1}}
\quad\text{against } 0.09280.$$

A **change of $-6.5\%$** in measured conductivity for a 50% change in
saturation. Without the surface term the change would be $-75\%$ — a factor 11
more visible. So the clay has made the rock nearly blind to its own water
content, and a monitoring survey that promises to map saturation in a
clay-bearing unit is promising something the physics does not deliver.

---

## ★6 — Debye numbers

$$\tau = \frac{1}{2\pi f_c} = \frac{1}{2\pi\times2} = 0.079577\ \mathrm{s}
= 79.577\ \mathrm{ms}.$$

For a Debye, $|\varphi|$ peaks near $f_c$; the lesson's demo prints
$5.2159^\circ$ at $1.8197$ Hz for these parameters (slightly below $f_c$ because
the peak depends on $\sigma_\infty/\sigma_0$).

At $f = 0.01$ Hz, using the lesson's table for the same
$\sigma_\infty/\sigma_0 = 1.2$: phase $\approx 1.0\ \mathrm{mrad}$
($0.0573^\circ$), $|\sigma| = 0.050000\ \mathrm{S\,m^{-1}}$.

A DC resistivity survey needs only the last number: at $f \ll f_c$ the medium is
at its DC conductivity, and the dispersion is invisible. It needs the other two
only to justify *ignoring* them.

---

## ★7 — Phase area versus chargeability

$$-\ln(1-m) = -\ln(1-0.4) = -\ln 0.6 = 0.510826.$$

So the area is $0.511$ against $m = 0.400$: a $27.7\%$ overstatement.

The 10% threshold: solve $-\ln(1-m)/m = 1.10$. For small $m$,
$-\ln(1-m)/m \approx 1 + m/2$, so $m \approx 0.20$ gives
$1 + 0.10 = 1.10$ exactly to first order. Check: $-\ln(0.8)/0.2 = 0.22314/0.2 =
1.1157$, i.e. $11.6\%$ — so the exact threshold is slightly below $m = 0.2$,
about $m = 0.18$ ($-\ln(0.82)/0.18 = 1.104$). **For $m \lesssim 0.18$ the phase
area is within 10% of $m$; beyond that the two must be distinguished.**

---

## ★8 — Separating electrolytic from surface conduction

1. **Samples:** one clay-bearing and one clean sample from the same unit, to give
   a reference with $\sigma_s \approx 0$.
2. **Fluids:** a sequence of at least four NaCl brine concentrations spanning two
   decades (e.g. 0.005 to 0.5 mol/L), prepared by weight, with $\sigma_w$
   *measured* for each.
3. **Measured quantities:** $\sigma$ for each sample at each salinity, and
   porosity by porosimetry.
4. **Plot:** $\sigma$ against $\sigma_w$ at fixed $\phi$. The two-term model
   predicts a **straight line**, because
   $\sigma = \sigma_w/F + \sigma_s$: the slope is $1/F$ and the
   intercept at $\sigma_w = 0$ is $\sigma_s$.
5. **Criterion for success:** the fit must be linear over the full salinity
   range (residuals showing curvature indicate brine-dependent $\sigma_s$ or
   mobility effects), the intercept must be positive and reproducible between
   cores, and the slope must give $F$ consistent with the measured porosity
   through $F = \phi^{-m}$ with $m$ in the range the rock type supports.
6. **Failure signature:** a negative intercept, or an intercept that scales with
   $\sigma_w$, means the model is misspecified — the measurement has not
   separated the mechanisms, and $\sigma_s$ must not be reported.
