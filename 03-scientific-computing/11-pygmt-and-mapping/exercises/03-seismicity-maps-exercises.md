# Exercises — 03-11-03 Plotting Seismicity, Focal Mechanisms and Plate Boundaries

> Solutions are in
> [`03-seismicity-maps-solutions.md`](./03-seismicity-maps-solutions.md).

---

## ★ Foundational

**★1.** Convert to $M_w$: (a) $M_0 = 10^{16}$ N·m, (b) $M_0 = 10^{20}$ N·m,
(c) $M_0 = 5\times10^{18}$ N·m.

**★2.** For $b = 1.0$ and $M_c = 2.0$, how many events of $M \ge 5.0$ does a
catalogue of 10 000 events predict?

**★3.** State two ways a real catalogue is a biased sample of what the Earth did.

**★4.** What do strike, dip and rake describe?

**★5.** Write down the Aki–Utsu estimator and identify the term that differs
between the two estimators the lesson compares.

---

## ★★ Applied

**★★6.** Reproduce the $b$-value measurement for $n = 500$ and $n = 20\,000$
events with the same seed, and report both estimates and their standard errors.
State how the estimator disagreement scales with $n$.

**★★7.** Fit the binned slope with and without the empty bins and report both
slopes. Explain which you would quote.

**★★8.** Build the same map with a logarithmic size column,
$s = 0.02 + 0.05\log_{10}(M - M_c + 1)$, and report the size range. State which
encoding you would use and why.

**★★9.** Replace the four-vertex trench with a 100-vertex polyline interpolated
along the same path, and report the change in the fraction of events within 50 km.
State whether the change is what you expected.

**★★10.** Compute the $b$-value for a catalogue with $M_c = 3.0$ instead of 2.5
from the same generated events (i.e. discarding the events below 3.0) and report
the bias relative to 1.0. Explain the direction of the bias.

---

## ★★★ Research-oriented

**★★★11.** Design a completeness test. Using your synthetic catalogue, compute
(a) the maximum curvature of the magnitude–frequency distribution and (b) the
goodness-of-fit test of the GR fit as a function of a trial $M_c$, and report the
$M_c$ each method returns against the input of 2.5. State which you would trust on
a real catalogue and what would change if the magnitude rounding interval differed
from the one you used.

**★★★12.** Quantify the symbol-size distortion. For a magnitude range
$M_c$–$M_c+4$, compute the marker area, radius and ratio to the smallest event
under (a) area proportional to $M - M_c$ and (b) area proportional to $10^{M}$
(energy-like). Report the two dynamic ranges and state which encoding a reader is
more likely to interpret correctly, citing whatever evidence you can find — and
say plainly if you cannot find any.
