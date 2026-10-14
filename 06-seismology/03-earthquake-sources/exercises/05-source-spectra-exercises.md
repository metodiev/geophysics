# Exercises — 06-03-05 Source Spectra, Corner Frequency and Stress Drop

Attempt these before reading the
[solutions](./05-source-spectra-solutions.md). The lesson is
[05 Source Spectra, Corner Frequency and Stress Drop](../05-source-spectra.md)
and the demonstration is
[`../code/source_spectra_demo.py`](../code/source_spectra_demo.py). All values are
**SYNTHETIC**. Use $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $k = 0.37$ unless told otherwise, and

$$\Omega(f) = \frac{\Omega_0}{1+(f/f_c)^{2}},\qquad
M_0 = \frac{16}{7}\Delta\sigma a^{3},\qquad f_c = \frac{k\beta}{a}.$$

## ★ Foundational

**★1.** A SYNTHETIC event has $M_0 = 1.0\times10^{20}\ \mathrm{N\,m}$ and
$\Delta\sigma = 5.0\ \mathrm{MPa}$. Compute the source radius $a$ and the corner
frequency $f_c$, showing the cube root explicitly.

**★2.** Using the $f_c$ from ★1, compute $\Omega(2f_c)/\Omega_0$ and
$\Omega(f_c/2)/\Omega_0$ from the model formula, and state the two asymptotic
slopes of $\log\Omega$ versus $\log f$ on either side of $f_c$.

**★3.** Invert the ★1 pair $(M_0, f_c)$ back to a stress drop with the formula
$\Delta\sigma = \tfrac{7}{16}M_0(f_c/(k\beta))^{3}$ and verify that you recover
$5.0\ \mathrm{MPa}$.

## ★★ Applied

**★★4.** The data of ★1 were built with $k = 0.37$. Invert them with $k = 0.20$
and with $k = 0.50$, and report the two stress drops and the ratio between them.
State whether the $M_0$ recovered from the plateau changes.

**★★5.** Compute the mean slip of the ★1 event using
$\bar D = \tfrac{16}{7\pi}(\Delta\sigma/\mu)a$, and check it against
$M_0 = \mu\pi a^{2}\bar D$.

**★★6.** Using the demo's constant-stress-drop family, take $a = 50\ \mathrm{m}$
($f_c = 25.9\ \mathrm{Hz}$, $M_0 = 8.5714\times10^{11}\ \mathrm{N\,m}$) and
$a = 5000\ \mathrm{m}$ ($f_c = 0.259\ \mathrm{Hz}$,
$M_0 = 8.5714\times10^{17}\ \mathrm{N\,m}$). Compute the exponent
$p$ in $M_0\propto f_c^{p}$ from these two points and state what it implies for
the slip.

**★★7.** From the demo's saturation table, estimate the exponent of the
band-limited amplitude with respect to $M_0$ for (a) the band
$10^{-4}$–$10^{-3}\ \mathrm{Hz}$ and (b) the band $2$–$10\ \mathrm{Hz}$, using the
$M_0 = 10^{18}$ and $M_0 = 10^{23}$ rows. Compare with the demo's fitted
$0.999089$ and $0.333771$ and explain the sign of any difference.

## ★★★ Research-oriented

**★★★8.** Design a study to test whether stress drop varies systematically with
depth, given that $k$ is unknown and cannot be measured. Specify what you would
hold fixed, what you would compare (a robust *relative* statistic, not an absolute
stress drop), the data you would need, and the model-dependence that remains after
your design. A specification that could not be executed is a failed answer.

**★★★9.** The $\omega^{-2}$ shape is assumed. Design a test of that assumption
using many events at one station, specifying the observable, the competing models
(e.g. different high-frequency decay exponents), the fit statistic, and the
degeneracy with attenuation that you must break.

**★★★10.** Using the relations of the lesson, show that if every event in a
population shares the same, unknown $k$, then *ratios* of stress drops within the
population are independent of $k$ even though absolute values are not. Then state
one observational requirement that this conclusion needs, and one way it can
fail.
