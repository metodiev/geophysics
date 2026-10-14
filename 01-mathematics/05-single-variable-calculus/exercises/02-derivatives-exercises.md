# Exercises — 01-05-02 Derivatives and Rates of Change

Attempt these **closed-book** before opening the
[solutions](./02-derivatives-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Differentiate from first principles, showing the limit of the difference
quotient at each step:

(a) $f(x) = 3x^{2} - 5x$
(b) $f(x) = \dfrac{1}{x+2}$
(c) $f(t) = \sqrt{t}$ (for $t>0$)

---

**★2.** State the units of each derivative and check the expression dimensionally:

(a) $dv/dz$ for $v$ in km/s and $z$ in km
(b) $dT/dz$ for $T$ in K and $z$ in m
(c) $dg/dz$ for $g$ in m/s² and $z$ in m
(d) $dP/dt$ for $P$ in Pa and $t$ in yr

---

**★3.** Write down the forward and central difference approximations to $f'(x)$,
state the order of the truncation error of each, and explain which one you would
use when function evaluations are expensive.

---

## ★★ Applied

**★★4.** A velocity model is $v(z) = 1500 + 0.5z\ \mathrm{m\,s^{-1}}$ with $z$ in
metres.

(a) Compute $dv/dz$ analytically.
(b) Estimate $dv/dz$ at $z = 3000$ m by a central difference with $h = 100$ m and
with $h = 1$ m.
(c) The demonstration reports an error of `1.26e-08` for $h = 10^{-5}$ m. Explain
why a smaller step is *worse*, naming the numerical mechanism.
(d) State the value of $h$ at which you would stop refining for data known to
$0.1$ m/s.

---

**★★5.** A borehole records 22.0 °C at the surface and 91.0 °C at 2000 m depth.

(a) Compute the geothermal gradient in K/km and K/m.
(b) Estimate the heat flux for $k = 2.4\ \mathrm{W\,m^{-1}\,K^{-1}}$, in
W/m² and mW/m².
(c) State two physically distinct reasons why this gradient may differ from the
true steady-state gradient of the region.

---

**★★6.** Relative motion of 35 mm/yr occurs across a 60 km wide shear zone.

(a) Compute the strain rate in $\mathrm{yr^{-1}}$ and $\mathrm{s^{-1}}$
(use 1 yr = 3.156 × 10⁷ s).
(b) Compute the time to accumulate unit strain, in years and in Myr.
(c) Show that the time to accumulate unit strain equals $W/v$, and evaluate it for
the values here. Then explain why a study that reports only the velocity across a
zone cannot be compared with one that reports a strain rate unless the zone width
is also stated.

---

## ★★★ Research-oriented

**★★★7.** Repeat the demonstration's noise experiment for a **second** derivative,
using the central second difference

$$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^{2}} .$$

Take $f(x) = x$ plus Gaussian noise with $\sigma = 10$ m/s (the true second
derivative is zero), and measure the mean absolute value of the estimate for
$h = 500, 100, 20$ m with at least 200 samples each.

(a) Derive the standard deviation of the noise in the estimate in terms of
$\sigma$ and $h$, using the fact that the three noise samples are independent.
(b) Fit the empirical exponent of $h$ and compare with your prediction.
(c) State the limits of your conclusion: what depends on the noise model, and what
depends only on the differencing weights?

---

**★★★8.** A gravimeter's height above the reference datum is uncertain by ±3 mm.
Using the free-air gradient derived in the lesson, compute the resulting
uncertainty in the gravity value in µGal. Then state the smallest real gravity
change that is *observable* given a repeatability of 5 µGal, and explain what the
difference between the two numbers means for the design of a monitoring survey.

---

## Extension ideas

- Repeat ★2 for the second derivative $d^{2}T/dz^{2}$ and state its units. Why is it
  awkward to measure directly?
- Write a function `central_difference(f, x, h)` that returns the estimate *and* the
  interval that would be optimal for a stated noise level
  $\sigma$: $h_{\text{opt}} \approx (\sigma/\sigma_{3})^{1/3}$ with
  $\sigma_{3}$ an estimate of $\lvert f'''\rvert$. Test it on $f(x)=\sin x$.
- The lesson's strain rate used 50 mm/yr over 100 km. Produce a table of strain
  rates for 10, 20, 50 and 100 mm/yr across zone widths of 10, 50 and 200 km, and
  identify which combinations give strain rates below $10^{-14}\ \mathrm{s^{-1}}$.
