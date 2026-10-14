# Solutions — 06-04-03 Relative Location: Master-Event, Double-Difference, HypoDD

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [03 Relative Location](../03-relative-location.md).

---

## ★1 — Noise of a difference

$$
\sigma_{\Delta} = \sqrt{20^{2} + 20^{2}} = 28.3\ \mathrm{ms}.
$$

Differencing two independent picks *increases* the noise by 41 per cent.

---

## ★2 — The equation

$$
t_{ij}^{\text{obs}} - t_{i0}^{\text{obs}}
= \big(t_{0j} - t_{00}\big) + \big(T_{ij} - T_{i0}\big) .
$$

The station delay $\tau_i$ is present in both observed times with the same value
and cancels; it never appears in the right-hand side.

---

## ★3 — One sentence

A station delay looks like a source displacement to the whole array, so an
absolute inversion can reduce the residual by moving the event, while a
difference between two events at the same station is insensitive to it because
the delay is shared.

---

## ★4 — Improvement factors

Measured difference over pick difference:

$$
1870.2/78.2 = 23.9 .
$$

Measured difference over absolute offsets:

$$
1594.3/78.2 = 20.4 .
$$

Both are of the order of the precision ratio
$\sigma_{\text{pick}}/\sigma_{\text{dd}} = 20/2 = 10$, with the extra factor
coming from how the noise propagates through the pairwise trade-off.

---

## ★5 — Mean of the delays

From the rounded values,

$$
\frac{67 - 132 + 141 - 52 - 136 - 70 + 69 + 42}{8}
= \frac{-71}{8} = -8.875\ \mathrm{ms},
$$

against the printed $-8.95\ \mathrm{ms}$. The discrepancy is rounding: the
demonstration prints the delays to the nearest millisecond but computes with the
full-precision values, and the sum of eight rounded numbers differs from the
rounded sum by up to 0.5 ms. A worked number should never be reconstructed from
printed digits when more precision was available.

---

## ★6 — Norm of the projection

$$
\sqrt{869.7^{2} + 266.1^{2} + 1016.5^{2}}
= \sqrt{7.563\times10^{5} + 7.081\times10^{4} + 1.033\times10^{6}}
= \sqrt{1.860\times10^{6}} = 1363\ \mathrm{m}.
$$

The measured bias norm is

$$
\sqrt{867.2^{2} + 210.0^{2} + 810.0^{2}}
= \sqrt{7.520\times10^{5} + 4.410\times10^{4} + 6.561\times10^{5}}
= \sqrt{1.452\times10^{6}} = 1205\ \mathrm{m}.
$$

The two differ by about 13 per cent because the measured mean bias averages over
ten events with slightly different geometries, while the projection is evaluated
at the master alone. The agreement of the direction and the order of magnitude is
the point.

---

## ★7 — Reducing $\sigma_{\text{dd}}$ to 0.5 ms

Preprocessing: band-pass to the signal band (failure: removing the high
frequencies removes the timing information); window around the first arrival with
a taper (failure: a window shorter than the wavelet biases the delay); whiten
before correlating (failure: whitening amplifies incoherent noise in similarity
bands); resample for sub-sample interpolation; use the phase of the cross-spectrum
(failure: cycle skipping when the initial alignment is worse than half a period).

Prediction: the offset error scales with the input timing precision, so reducing
$\sigma_{\text{dd}}$ by a factor of 4 should reduce the 78.2 m of the
demonstration to roughly 20 m, provided nothing else in the error budget
dominates. If the measured curve flattens before that, something else — the
velocity cancellation, or the linearisation — has become the limiting term.

---

## ★8 — Measuring the separation limit

**Design:** fix the network and the picking precision; take a master event and
place a second event at separations 0.1, 0.3, 1, 3, 10 and 20 km; generate
differential times through a model perturbed by a fixed uniform 3 per cent, and
locate relatively with the unperturbed model; record for each separation the
error in the *offset* vector relative to that of a control run with no velocity
error.

**Expected shape:** the offset error grows approximately linearly with
separation (the leading term is proportional to the differential travel time, as
in Section 3.3), starting near zero.

**Falsification:** if the error is flat in separation, the cancellation is not
first order and the argument of Section 3.3 is wrong; if it grows faster than
linearly, a second-order term dominates and the linearisation — not the
differencing — is the culprit.
