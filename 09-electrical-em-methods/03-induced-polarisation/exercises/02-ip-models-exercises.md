# Exercises — 09-03-02 IP Models: Cole-Cole, Debye, Constant-Phase Element

Attempt these before reading the
[solutions](./02-ip-models-solutions.md). The lesson is
[02 IP Models](../02-ip-models.md). All models are **SYNTHETIC** teaching
values throughout.

## ★ Foundational

**★1.** Compute $\rho$ at $f = 1.00$ Hz for
$\rho_0 = 200\ \Omega\,\mathrm{m}$, $m = 0.05$, $c = 0.50$,
$\tau = 0.20$ s, showing each intermediate complex number
($\lvert z\rvert$, $\arg z$, $z$, $1/(1+z)$, $\rho/\rho_0$), and report
$\lvert\rho\rvert$ and the phase in mrad.

**★2.** For $m = 0.25$, $c = 1.00$ and $\tau = 0.40$ s, compute the peak phase
magnitude and the peak frequency from the analytic formulae.

**★3.** A model has $\rho_0 = 50\ \Omega\,\mathrm{m}$ and $m = 0.20$. State its
DC and high-frequency resistivities and explain in two sentences why those two
numbers cannot constrain $c$.

## ★★ Applied

**★★4.** From the lesson's measured peak-phase table, by what factor does the
peak phase fall between $c = 1.00$ and $c = 0.60$ at $m = 0.10$? Using the fitted
relation $\lvert\varphi_{\max}\rvert = 0.3165\,m^{1.0565}$ rad for $c = 0.60$,
what $m$ would be needed to reproduce the $c = 1.00$ peak phase?

**★★5.** The Kramers-Kronig check reproduces the model phase to within
$2\times10^{-12}$ rad at $0.05$, $1$ and $20$ Hz for $c = 1.00$, $0.60$ and
$0.25$. State what this implies for a survey that measures amplitude only, and
what it does *not* imply.

**★★6.** At $c = 0.10$ the measured phase over two decades is
$4.012$–$4.145$ mrad and the amplitude slope is $-0.0026$. Compute the band
exponent $n_{\text{eff}} = (2/\pi)\lvert\varphi\rvert$ using the mean phase, compare
it with the model's $c$, and state what a survey can and cannot conclude from it.

## ★★★ Research-oriented

**★★★7.** Specify the numerical Kramers-Kronig check: the quadrature, the
integration band, the treatment of the band edges, the expected order of the
residual, and the failure mode of a band that is too narrow. Your specification
must be executable with NumPy and SciPy as used in this module.

**★★★8.** An exact two-relaxation ground has $\tau_1 = 0.30$ s and
$\tau_2 = 6.00$ s. A survey is limited to $0.01$–$100$ Hz and $2$ mrad phase
noise, and a single Cole-Cole fits it with a residual of $2.054$ mrad. Specify
the band extension and the noise level that would identify both time constants,
and state the decision criterion you would use (including the risk you are
accepting).
