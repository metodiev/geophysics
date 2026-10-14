# Exercises — 20-01-02 Linear Time-Invariant Systems and Impulse Response

Attempt these before reading the
[solutions](./02-lti-systems-solutions.md). The lesson is
[02 LTI Systems](../02-lti-systems.md). **All models and data in this module
are SYNTHETIC** teaching examples.

## ★ Foundational

**★1.** State whether each system is (i) linear, (ii) time-invariant, and give
the impulse response where it exists:

  (a) $y[n] = 3x[n] - x[n-1]$;
  (b) $y[n] = x^{2}[n]$;
  (c) $y[n] = x[n/2]$ for even $n$, $0$ otherwise (a decimator);
  (d) $y[n] = n\,x[n]$;
  (e) $y[n] = 0.5\,y[n-1] + x[n]$, with $y[-1] = 0$.

**★2.** Convolve $x = [2, -1, 3]$ with $h = [1, 0.5]$ by hand and verify with
$\sum_n y[n] = \left(\sum_n x[n]\right)\left(\sum_n h[n]\right)$.

**★3.** For the one-pole system $y[n] = 0.7\,y[n-1] + x[n]$, write down $h[n]$,
$\sum_{n}\lvert h[n]\rvert$, the DC gain, and the value of the step response at
$n = 5$. State whether the system is BIBO-stable and why.

## ★★ Applied

**★★4.** A synthetic system's measured impulse response is
$h = [1, 0.8, 0.6, 0.4, 0.2]$ (samples at $1\ \mathrm{kHz}$).
Compute (a) the DC gain, (b) the response to a unit step, (c) the group delay if
the phase is exactly linear, and (d) the response to $x[n] = 1$ for
$0\le n \le 4$ and $0$ otherwise. Check (d) two ways.

**★★5.** Show that a system satisfying the linearity axiom must satisfy
$\mathcal H\{0\} = 0$, and explain why this matters for a sensor that reports a
constant $2.5\ \mathrm{V}$ offset when its input is zero. Then show that
$y[n] = \lvert x[n]\rvert$ is not linear, by exhibiting two inputs and two
scalars for which superposition fails.

**★★6.** A causal system has $h[n] = 0.5^{n}u[n]$. Another is cascaded with it:
$h_2[n] = \delta[n] - 0.25\,\delta[n-1]$. Find the combined impulse response by
hand (use associativity), give the DC gain of the cascade, and state which of the
two systems is a high-pass and which a low-pass by comparing their gains at
$\omega = 0$ and $\omega = \pi$.

## ★★★ Research-oriented

**★★★7.** A digitised seismic channel shows a small dependence of its
sensitivity on the ambient temperature, of order $0.05\%$ per kelvin, and daily
temperature excursions of $5\ \mathrm{K}$. Design a test that distinguishes
"the channel is LTI with a drifting gain" from "the channel is not LTI", stating
the input, the statistic, the resolution of that statistic, and the expected
signature of each hypothesis. Then state what you would do to the data if the
drift hypothesis is supported.

**★★★8.** The demonstration measures the group delay of a symmetric FIR two ways
(the phase slope and the centroid of the impulse response) and notes that the
*onset* is not delayed. Construct a synthetic example in which the onset-based
delay and the centroid-based delay differ by more than one sample, explain which
one a first-break picker effectively measures, and state the sign and size of the
bias you would expect in an arrival time estimated from a pick on a
low-pass-filtered record.
