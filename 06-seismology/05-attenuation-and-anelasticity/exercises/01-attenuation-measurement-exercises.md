# Exercises — 06-05-01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods

Attempt these before reading the
[solutions](./01-attenuation-measurement-solutions.md). The lesson is
[01 Measuring Q](../01-attenuation-measurement.md). All models are
**SYNTHETIC** teaching values; work to three significant figures unless a
question says otherwise.

## ★ Foundational

**★1.** A medium has $v = 3500\ \mathrm{m\,s^{-1}}$ and $Q = 150$ at
$f = 2\ \mathrm{Hz}$. Compute $\alpha$ and $1/\alpha$. State the unit of each,
and explain in one sentence why $1/\alpha$ is not the wavelength (compute the
wavelength too).

**★2.** The same medium is recorded at $x_1 = 30\ \mathrm{km}$ and
$x_2 = 130\ \mathrm{km}$ from a common source. Write down $\ln(A_1/A_2)$ as a
function of $f$ for the ideal case, including the geometric-spreading term for
$1/x$ spreading. Evaluate the expression at $f = 5\ \mathrm{Hz}$.

**★3.** A spectral-ratio fit over $[1, 20]\ \mathrm{Hz}$ returns a slope
$m = 0.1132\ \mathrm{Hz^{-1}}$ for the receivers and velocity of ★2. Compute the
implied $Q$ and state the units of $m$.

## ★★ Applied

**★★4.** For ★2's geometry, the log-amplitude difference has noise of standard
deviation $\sigma_y = \sqrt{2}$ (unit noise on each log amplitude) and $N = 150$
frequencies uniformly spaced over $[0.5, 8]\ \mathrm{Hz}$. Compute
$\sigma_m$ and the fractional error $\sigma_Q/Q$ predicted from the fit
geometry. Would a $1.5\%$ answer be possible in this band?

**★★5.** A source at one station produces arrivals at two distances with
travel times $\tau_r = 12.0\ \mathrm{s}$ and $\tau_r = 30.0\ \mathrm{s}$. The
measured pulse widths (FWHM) are $0.311\ \mathrm{s}$ and $0.761\ \mathrm{s}$.
Using the rise-time relation, find $Q$ from the slope, and check the answer
against the assumption of a single source width. Comment on why the *slope*
rather than either intercept is the measurement.

**★★6.** A colleague reports "this path has $Q = 90$" from a fit over
$[0.5, 2]\ \mathrm{Hz}$. Using the demonstration's single-relaxation model
($f_0 = 1\ \mathrm{Hz}$, $D = 0.020$, so $1/Q(f) = D(f/f_0)/(1+(f/f_0)^{2})$),
compute the band average $\langle 1/Q\rangle$ over that band and the implied
band-$Q$. Compare with $Q(f_0) = 100$ and state what the colleague should add to
the claim to make it reproducible.

## ★★★ Research-oriented

**★★★7.** Design a measurement plan that obtains $Q$ to $2\%$ or better on a
$60\ \mathrm{km}$ path with $v = 3200\ \mathrm{m\,s^{-1}}$, given that the usable
band is $[0.8, 6]\ \mathrm{Hz}$ and each log-amplitude measurement has
$\sigma = 0.05$. State the estimator, the number of independent paths you need,
and show the arithmetic for each step. A plan that could not be executed is a
failed answer.

**★★★8.** Attenuation and dispersion are two faces of one transfer function.
A study measures a spectral-ratio $Q = 200$ over $[1, 10]\ \mathrm{Hz}$ on a path
with $\tau_r = 24.0\ \mathrm{s}$, and separately measures a differential travel
time between $1\ \mathrm{Hz}$ and $10\ \mathrm{Hz}$ of $0.010\ \mathrm{s}$.
Compute the $Q$ implied by the dispersion measurement with the
nearly-constant-$Q$ law and state whether the two are consistent. Then state
which of the two measurements you would trust for a $1\%$ velocity correction and
why.
