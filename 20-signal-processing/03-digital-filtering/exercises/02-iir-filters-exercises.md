# Exercises — 20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic

Attempt these before reading the
[solutions](./02-iir-filters-solutions.md). The lesson is
[02 IIR Filter Design](../02-iir-filters.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** Write the magnitude-squared response of the Butterworth lowpass and state
the value of $|H|$ at $\Omega = \Omega_c$ for any order.

**★2.** An IIR filter has denominator coefficients $a = [1, -1.2, 0.5]$. Find its
poles and state whether it is stable.

**★3.** State the bilinear-transform mapping from $s$ to $z$ and the frequency
warping relation it implies.

## ★★ Applied

**★★4.** Compute the order a Butterworth filter needs for $f_s = 100$ Hz,
passband to 10 Hz, stopband from 20 Hz, $R_p = 3$ dB, $R_s = 40$ dB, using the
closed-form order formula with the cutoff at the passband edge.

**★★5.** For the same specification, state how many orders an elliptic design
needs, and explain the direction of the difference from your answer to ★★4.

**★★6.** The demo measures a passband group delay that rises from 10.155 samples
at 5 Hz to 17.395 samples at 55 Hz for a 6th-order Butterworth. Compute the
differential delay between a 10 Hz and a 50 Hz component in milliseconds at
$f_s = 1000$ Hz.

## ★★★ Research-oriented

**★★★7.** Show that a Butterworth filter's $-\!3$ dB frequency and its passband
edge are different quantities, and derive the relation between them for order $M$.

**★★★8.** Cascade three identical 2nd-order sections and compare the group-delay
variation with a single 6th-order direct-form design of the same coefficients.
State which is more dispersive and why the pole locations are the same.