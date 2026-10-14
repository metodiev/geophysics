# Exercises — 10-01-03 Attenuation, Penetration Depth and Frequency Trade-Offs

Attempt before the [solutions](./03-gpr-attenuation-penetration-solutions.md).
Lesson: [03 Attenuation, Penetration and Frequency](../03-gpr-attenuation-penetration.md).
All models **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $\alpha$ in $\mathrm{m^{-1}}$ and $\mathrm{dB\,m^{-1}}$ for
$\sigma = 2\times10^{-3}\ \mathrm{S\,m^{-1}}$ and $\varepsilon_r = 9$, and give
the skin depth.

**★2.** Compute the two-way loss in dB at $3.0\ \mathrm{m}$ depth for
$\alpha = 0.1\ \mathrm{m^{-1}}$.

**★3.** For $v = 0.075\ \mathrm{m\,ns^{-1}}$ and $Q = 20$, compute
$\alpha_Q$ at $100$ and $400\ \mathrm{MHz}$.

## ★★ Applied

**★★4.** With $\alpha_{\mathrm{cond}} = 0.0471\ \mathrm{m^{-1}}$, $Q = 12$ and
$v = 0.07495\ \mathrm{m\,ns^{-1}}$, compute the total $\alpha$ at $200\
\mathrm{MHz}$ and the fractional contribution of conduction loss.

**★★5.** A spectral ratio of two reflections $1.5\ \mathrm{m}$ apart has
intercept $0.15$ and slope $1.2\times10^{-8}\ \mathrm{s}$. Compute
$\alpha_{\mathrm{cond}}$ and $Q$ for $v = 0.075\ \mathrm{m\,ns^{-1}}$.

**★★6.** Using the budget $A/A_{\mathrm{ref}} = R\,r_{\mathrm{ref}}
e^{-2\alpha d}/(2d)$, find the depth at which a $-70\ \mathrm{dB}$ threshold is
crossed for $|R| = 0.2$, $\alpha = 0.3\ \mathrm{m^{-1}}$.

## ★★★ Research-oriented

**★★★7.** The centroid estimator returned $Q = 61.15$ for a model $Q = 60$ at a
path difference of $13.34\ \mathrm{ns}$ and a $2.74\%$ centroid shift. Estimate
the error this estimator would show if the path difference were tripled, and
state the assumption that breaks.

**★★★8.** Design a frequency choice for a survey that must reach $4\ \mathrm{m}$
in a medium with $\alpha(t) = 0.0471 + \pi f/(vQ)$ at $Q = 20$ and a $-75\
\mathrm{dB}$ budget. State the answer in MHz with your assumptions listed.
