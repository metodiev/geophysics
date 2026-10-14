# Solutions — 09-02-05 Electrical Resistivity Tomography (ERT) Acquisition and Design

> **Read after attempting the exercises.** Lesson:
> [05 ERT Acquisition and Design](../05-ert-tomography.md).

---

## ★1 — Count

Line length $= (64-1)\times3.0 = 189.0$ m.

$n = 1$: aperture index span $= 4+1 = 5$, so
$\text{count} = 64-5+1 = 60$.

$n = 6$: span $= 4+6 = 10$, so $\text{count} = 64-10+1 = 55$.

Total for $n = 1..6$: $60+59+58+57+56+55 = 345$ measurements.

---

## ★2 — Scaling

$\text{DOI}/a = 1.264$ for $n = 4$, so
$\text{DOI} = 4\times1.264 = 5.06$ m.

---

## ★3 — Signal

$|k| = 188.4956\times2 = 376.99$ m, so

$$\Delta V = \frac{\rho I}{|k|} = \frac{100\times0.1}{376.99}
= 0.02653\ \mathrm{V} = 26.5\ \mathrm{mV},$$

matching the lesson's table for $n = 3$.

---

## ★4 — Usable $n$ in different grounds

Required: $\Delta V > 10\times0.5\ \mathrm{mV} = 5.0\ \mathrm{mV}$, i.e.
$\rho I/|k| > 0.005$ V with $I = 0.1$ A and $|k| = 37.70n(n+1)(n+2)$ m
(for $a = 2$ m and the dipole-dipole formula with $|k|/a = 18.85n(n+1)(n+2)$):

$$|k| < \frac{\rho\times0.1}{0.005} = 20\rho.$$

- $\rho = 30\ \Omega\,\mathrm{m}$: $|k| < 600$ m →
  $n(n+1)(n+2) < 600/37.70 = 15.9$. Since
  $3\times4\times5 = 60 > 15.9$ and $2\times3\times4 = 24 > 15.9$ but
  $1\times2\times3 = 6 < 15.9$, only **$n = 1$** is usable.
- $\rho = 300\ \Omega\,\mathrm{m}$: $|k| < 6000$ m →
  $n(n+1)(n+2) < 159$; $4\times5\times6 = 120 < 159$ but
  $5\times6\times7 = 210 > 159$, so **$n \le 4$** is usable.

A factor-10 change in ground resistivity changes the deep reach from $n = 1$ to
$n = 4$.

---

## ★5 — An 8 m, 6 m target in 50 $\Omega\,\mathrm{m}$ ground

1. Spacing: $a = d/(\text{DOI}/a) = 8/1.787 = 4.5$ m.
2. Aperture: $8\times4.5 = 35.8$ m.
3. Footprint: $a\times2.51 = 11.3$ m — larger than the 6 m target.
4. Signal: $|k| = 1055.58\times4.5 = 4750$ m,
   $\Delta V = 50\times0.1/4750 = 1.05\ \mathrm{mV}$, i.e. twice the stated
   0.5 mV floor: thin but workable with stacking.

Verdict: **detected, not resolved.** The target is smaller than the footprint, so
its true size cannot be recovered; only its presence and approximate position.

---

## ★6 — Marginal coverage

Design 1: $2.5/41 = 0.061$ m per measurement. Design 2: $5.3/123 = 0.043$ m per
measurement.

Tripling the measurement count bought a 2.1-fold increase in coverage depth, so
the marginal return has already fallen by 30%. This is the quantitative reason
that adding long offsets to a shallow survey is expensive: the sensitivity mass
per measurement falls faster than the depth grows.

---

## ★7 — Resolving a 3 m layer at 20 m

1. **Spacing.** To reach 20 m with $n = 6$: $a = 20/1.787 = 11.2$ m.
2. **Footprint.** At 20 m depth the 10–90% width is $2.51a = 28.1$ m — larger
   than the desired resolution. So the *depth* requirement and the *resolution*
   requirement conflict: to resolve a 3 m layer you need a footprint well below
   3 m, which is impossible at 20 m depth with any surface array
   (the width/depth ratio is ~1.4 for every $n$ measured in the lesson). **The
   binding constraint is the footprint ratio, and it cannot be met.**
3. Therefore the honest design goal changes: detect the layer at 20 m with
   $a \approx 11$ m and state that its thickness is determined only through its
   conductance, with a factor-of-two (or worse) admitted range from the
   equivalence analysis of [03](03-apparent-resistivity-solutions.md).
4. **Signal and current.** $|k| = 1055.58\times11.2 = 11800$ m;
   $\Delta V = 150\times0.1/11800 = 1.27\ \mathrm{mV}$ — above the 0.5 mV floor.
   With 16-fold stacking the effective noise falls by 4, so $I = 0.1$ A is
   sufficient.
5. **Geometry.** A 200 m line needs $\lceil200/11.2\rceil+1+8 = 27$ electrodes.

The binding constraint is the footprint-to-depth ratio, i.e. the physics, not
the instrumentation.

---

## ★8 — DOI and sign changes

For an array whose $s(z)$ changes sign, the cumulative integral of $s(z)$
(`cumsum`) is non-monotonic: it rises, falls, and can cross a level several
times. The demonstration's table shows this directly — the dipole-dipole
cumulative integral exceeds 1 ($\int_0^{40}|s|\,\mathrm{d}z = 1.0195$) precisely
because it has folded in regions of negative sensitivity.

Consequences:

1. With $|s|$ the median depth is well defined and comparable between arrays;
   the lesson uses it and says so.
2. With the signed $s$ the "depth where half the mass lies" may not exist, or may
   jump discontinuously as the array changes: the same array can appear to
   reach 2 m or 20 m depending on which crossing is chosen.
3. Therefore **a DOI number without its convention (signed or absolute;
   surface step included or not; mean, median or 90% depth) is not a
   measurement.** The lesson's convention is: absolute value, buried half,
   median. Any comparison with a published DOI must first check that the
   conventions match.
