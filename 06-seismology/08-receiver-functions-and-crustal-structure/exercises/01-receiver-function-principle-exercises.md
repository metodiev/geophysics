# Exercises — 06-08-01 Receiver Functions: Deconvolution and Ps Conversions

Attempt these before reading the
[solutions](./01-receiver-function-principle-solutions.md). The lesson is
[01 Receiver Functions](../01-receiver-function-principle.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A phase with speed $v = 3.50\ \mathrm{km\,s^{-1}}$ travels at ray
parameter $p = 0.060\ \mathrm{s\,km^{-1}}$. Compute its vertical slowness $q$
and state its unit. Repeat for $v = 6.00\ \mathrm{km\,s^{-1}}$.

**★2.** Using $H = 30\ \mathrm{km}$, $v_p = 6.20\ \mathrm{km\,s^{-1}}$,
$v_s = 3.60\ \mathrm{km\,s^{-1}}$, $p = 0.055\ \mathrm{s\,km^{-1}}$, compute the
Ps delay $\Delta t_{Ps}$. Show the arithmetic for both square roots.

**★3.** State the units of $Hq_s$ and verify by dimensional analysis that it is a
time.

## ★★ Applied

**★★4.** Derive $\mathrm{d}H/\mathrm{d}k|_{\Delta t}$ and evaluate it for the
model of ★2 with $k = v_p/v_s$. By how much does a $4\%$ error in $k$ move the
depth?

**★★5.** In the demonstration, the deconvolution noise gain is $23.8\times$ at
water level $10^{-8}$ and $0.79\times$ at $10^{-1}$, while the pulse FWHM grows
from $0.160$ to $0.260\ \mathrm{s}$. A study must resolve a $0.4\ \mathrm{s}$
pulse and keep the noise gain below $2\times$. Which water level do you choose
and why?

**★★6.** A receiver function shows a peak at $\Delta t = 12.5\ \mathrm{s}$ at
$p = 0.055\ \mathrm{s\,km^{-1}}$. A colleague calls it a deep converter at
roughly $100\ \mathrm{km}$. Using the multiple times of the demonstration model
($H = 30\ \mathrm{km}$, $k = 1.726$), give a better explanation and justify it
with a number.

## ★★★ Research-oriented

**★★★7.** Design an experiment that measures noise gain versus water level for
three different input noise levels (1%, 5%, 20%). State the metric you will use,
predict how the curves will shift, and what conclusion about the choice of water
level you expect. You do not need to run it to specify it, but a specification
that could not be executed is a failed answer.

**★★★8.** The analytic transfer function is
$1 + (a_{Ps}/a_p)\exp(-i\omega\Delta t)$. The demonstration verifies the spectral
ratio against it on the band where $|V|^{2} > 10^{-6}\max|V|^{2}$ (127 of 1001
bins) and finds a maximum deviation of $5.45\times10^{-7}$. Explain why the check
is restricted to that band, and why a deviation of order $10^{-7}$ rather than
$10^{-15}$ is the right thing to expect from a double-precision computation.
