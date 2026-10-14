# Exercises — 11-02-06 IP for Disseminated Sulphides and Porphyry Systems

Attempt these before reading the
[solutions](./06-ip-for-minerals-solutions.md). The lesson is
[06 IP for Minerals](../06-ip-for-minerals.md). All Cole-Cole parameters, circuit
resistances, volume fractions, windows and noise levels are **SYNTHETIC** teaching
values.

Useful: $Z(\omega) = R_0[1-m(1-\frac{1}{1+(i\omega\tau)^c})]$,
$m = (R_0-R_\infty)/R_0$,
$\phi_{\text{corner}}(c=1) = \arctan(m/(2-m))$,
$(2/\pi)\int\phi\,\mathrm{d}\ln\omega = -\ln(1-m)$,
$M(t_1,t_2) = m\tau(e^{-t_1/\tau}-e^{-t_2/\tau})/(t_2-t_1)$,
$m_{\text{mix}} = \phi R_b/(R+\phi R_b)$.

## ★ Foundational

**★1.** A sample has $R_0 = 180\ \Omega\,\mathrm{m}$ and $R_\infty = 162\
\Omega\,\mathrm{m}$. Compute its intrinsic chargeability, and state the phase at
the corner frequency for the Debye case.

**★2.** For the same sample with $\tau = 0.25\ \mathrm{s}$ and $c = 1$, compute
$|Z|$ and the phase at $f = 0.1$, $0.64$ and $4.0\ \mathrm{Hz}$.

**★3.** Compute $-\ln(1-m)$ for $m = 0.25$ and state the error introduced by
reporting the phase area as the chargeability.

**★4.** Using the mixture model with $R_b/R = 6$, compute the measured
chargeability for blocked fractions $\phi = 0.01$, $0.05$ and $0.20$, and state
whether the relation is linear.

## ★★ Applied

**★★5.** A rock shows $m = 0.30$ in a mixture model with $R_b/R = 12$. Compute the
blocked fraction, then compute the measured chargeability if a connected sulphide
path of $R_s = R/15$ exists in parallel. State the physical interpretation of the
change.

**★★6.** A time-domain survey with a $200$–$800\ \mathrm{ms}$ window reports
$45\ \mathrm{mV/V}$. Compute the chargeability the same rock would give in a
$100$–$300\ \mathrm{ms}$ window and in an $800$–$2400\ \mathrm{ms}$ window, for
$\tau = 0.5$ and $\tau = 2.0\ \mathrm{s}$, and state the ratio of the widest spread
you find.

**★★7.** For the lesson's SYNTHETIC sample ($m = 0.2$, $\tau = 1\ \mathrm{s}$,
$c = 0.6$), compute the phase at $0.05$, $0.5$ and $5\ \mathrm{Hz}$, then compute
$\phi(0.16\ \mathrm{Hz})$ for $c = 0.4$, $0.6$ and $1.0$ at the same $m$. State
what the $c$ dependence implies for the reliability of an $m$ inverted from a
narrow-band survey.

**★★8.** A clay with $m = 0.18$, $\tau = 0.01\ \mathrm{s}$, $c = 0.9$ and a
sulphide with $m = 0.18$, $\tau = 1.5\ \mathrm{s}$, $c = 0.6$ both produce a
chargeability. Compute each one's peak phase and peak frequency, and compute the
chargeabilities in a $100$–$500\ \mathrm{ms}$ window. Which observable separates
them, and by how much?

## ★★★ Research-oriented

**★★★9.** Design an IP program to distinguish disseminated sulphide from clay in a
terrain where both are present, stating the frequency band, the number of
frequencies (or the time-domain window set), the observable you would fit, and the
decision rule. Support the design with a computed separability: use the two
models above and show the misfit that would arise if the wrong model were fitted.

**★★★10.** EM coupling contaminates IP. Model a spurious coupling response as an
additional term proportional to $\omega^{1/2}$ with a stated coefficient, add it
to the Cole-Cole phase, and compute the bias it introduces into an inverted $m$
and $\tau$ over a two-decade and a half-decade band. State the array geometry
change that would reduce the bias, and why the bias is worse for a resistive
ground.

**★★★11.** The blocked-path model is a lumped circuit. Construct a numerical
experiment on a 2-D resistor network (say $40\times40$ nodes) in which a fraction
$\phi$ of the bonds is replaced by a series RC element, and measure $m$ versus
$\phi$. Compare the measured curve with the closed form
$\phi R_b/(R+\phi R_b)$ and report where and why they diverge.
