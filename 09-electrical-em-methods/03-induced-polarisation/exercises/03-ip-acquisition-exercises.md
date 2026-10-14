# Exercises — 09-03-03 IP Acquisition, Chargeability and Phase Units

Attempt these before reading the
[solutions](./03-ip-acquisition-solutions.md). The lesson is
[03 IP Acquisition](../03-ip-acquisition.md). All models are **SYNTHETIC**
teaching values throughout.

## ★ Foundational

**★1.** A phase must be measured to $\sigma_{\varphi} = 2$ mrad when the
amplitude signal-to-noise ratio is $\sigma_n/A = 1/10$. Using
$M = 2\left(\sigma_n/(A\sigma_{\varphi})\right)^{2}$, compute the number of
samples required, and the acquisition time at a $2$ Hz fundamental with
$16$ samples per cycle.

**★2.** A linear drift of $s = 5.0$ mV/s acts over $T = 2.0$ s with
$V_p = 20.0$ V. Compute the bias in the window-integral chargeability, in ms.

**★3.** State the three quantities an IP survey can report, their units, and
which of them depends on the integration window.

## ★★ Applied

**★★4.** Derive $\sigma_{\varphi} = \sigma_n/\left(A\sqrt{M/2}\right)$ from the
two-parameter least-squares estimate, then evaluate it (a) for
$A/\sigma_n = 50$ with $M = 2000$ samples, and (b) for $A/\sigma_n = 20$ with
$M = 32$ samples, comparing (b) with the demonstration's measured
$13.171$ mrad.

**★★5.** A survey reports $M_{\text{int}} = 12.0$ ms and wants a phase estimate.
Using the measured spread of $M/\varphi \in \left[0.540, 6.612\right]$ over
eighteen synthetic models, bound the phase, and state one further measurement
that would narrow the bound.

**★★6.** The demonstration reports $M_{\text{int}}(0\text{–}1\,\mathrm{s}) =
20.690$ ms for a charging time $t_{\text{on}} = 0.50$ s and $72.987$ ms when
fully charged ($\tau = 1.5$ s). Compute the percentage bias and check it against
$\left(1 - e^{-t_{\text{on}}/\tau}\right)$.

## ★★★ Research-oriented

**★★★7.** Design an acquisition for a target whose time constant lies between
$0.5$ and $5$ s and whose chargeability is of order $m = 0.05$, with a budget of
one hour per sounding and a target uncertainty on $m$ of $\pm 20\%$. Choose the
on-time, the window set, the fundamental frequency and the stack count, and show
the arithmetic that connects the budget to the uncertainty.

**★★★8.** The window-change experiment of the lesson fits one Debye to a
two-relaxation truth over two window sets and obtains
$\left(m, \tau\right) = \left(0.111, 1.266\ \mathrm{s}\right)$ and
$\left(0.090, 3.960\ \mathrm{s}\right)$. Explain, using the zero-noise residuals
($-13.89\%$ to $+8.97\%$ across the windows), why this is a *model* failure
rather than a *noise* failure, and state what that implies for reporting IP
results.
