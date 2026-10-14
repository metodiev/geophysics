# Exercises — 15-02-07 Marine CSEM and EM for Gas Hydrates

> **All models and data in this module are SYNTHETIC.** Resistivities, thicknesses
> and frequencies here are teaching values. Constants used:
> $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ exactly;

Lesson: [07 Marine CSEM and EM](../07-marine-csem-em.md).
Solutions: [07 solutions](07-marine-csem-em-solutions.md).

$$\delta = \sqrt{\frac{2\rho}{\mu_0\omega}} = 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m},
\qquad \text{one-way loss} = 8.686\,\frac{d}{\delta}\ \mathrm{dB}.$$

---

## ★ Foundational

**★1.** Skin depth, two frequencies

Compute the skin depth for

**(a)** seawater, $\rho = 0.30\ \Omega\,\mathrm{m}$, at $f = 0.25\ \mathrm{Hz}$ and
$f = 4\ \mathrm{Hz}$;
**(b)** sediment, $\rho = 2.0\ \Omega\,\mathrm{m}$, at the same two frequencies;
**(c)** the ratio of (b) to (a) at each frequency, and why it is the same ratio at
both.

**★2.** Water-column attenuation and the usable band

A survey has $2000\ \mathrm{m}$ of seawater at $0.30\ \Omega\,\mathrm{m}$.

**(a)** Compute the one-way and two-way attenuation through the water column at
$0.1\ \mathrm{Hz}$ and at $1\ \mathrm{Hz}$.
**(b)** A receiver has $110\ \mathrm{dB}$ of dynamic range. Which of the two
frequencies is usable, and what fraction of the range is left for the
sub-seafloor?
**(c)** Find the frequency at which the *two-way* water loss alone equals the whole
$110\ \mathrm{dB}$, and state the consequence for the survey's frequency band.

---

## ★★ Applied

**★3.** Choosing the band for a target

A resistive target lies $300\ \mathrm{m}$ below the seafloor in sediment of
$1.5\ \Omega\,\mathrm{m}$.

**(a)** Taking the best-response criterion $\delta \approx 2d$ and then
$\delta \approx 3d$ (where $d$ is the target depth), compute the two frequencies.
**(b)** State the band you would acquire, and the reason it is a band rather than
one frequency.
**(c)** The target is $20\ \Omega\,\mathrm{m}$ and $50\ \mathrm{m}$ thick. Estimate
its anomaly size from the transverse-resistance argument and say whether it is a
strong or a marginal target.

**★4.** Testing the transverse-resistance rule

The demonstration compares five models with the same $\rho h = 10\,000\
\Omega\,\mathrm{m^{2}}$ (a buried $300\ \mathrm{m}$ deep layer in
$1.0\ \Omega\,\mathrm{m}$ sediment) and finds peak anomalies of $8.52$, $16.88$,
$33.42$, $64.15$ and $114.34$ per cent, with curves deviating from the
$(100, 100)$ reference by up to $99.01\,\%$.

**(a)** For each model, compute the ratio $h/\delta_{\text{layer}}$ at the listed
peak frequency ($0.562$, $0.422$, $0.422$, $0.316$, $0.237\ \mathrm{Hz}$) and state
whether the layer is thin or thick compared with the skin depth *inside* it.
**(b)** The demonstration's controlled test at $0.422\ \mathrm{Hz}$ puts the layer at
the seafloor: $h = 100\ \mathrm{m}$ with $\rho = 10$, $100$, $1000\
\Omega\,\mathrm{m}$ gives $\rho_a = 1.2588$, $1.2882$, $1.2911\
\Omega\,\mathrm{m}$, while $\rho h = 10\,000$ with $h = 100$, $10$, $1\
\mathrm{m}$ gives $1.2882$, $1.0261$, $1.0026\ \Omega\,\mathrm{m}$. State which of
$\rho$, $h$ and $\rho h$ the response is a function of, and support the statement
with the ratios you compute.
**(c)** Starting from $\rho k\tanh(kh) \approx \rho k^{2}h$ for
$h \ll \delta_{\text{layer}}$, derive the thin-layer prediction
$\rho_a = \omega\mu_0(\delta^{2}/2 + \delta h + h^{2})$ and check it against the
$h = 100\ \mathrm{m}$ numbers above.
**(d)** Compute the frequency at which $h = \delta_{\text{layer}}$ for
$\rho = 100\ \Omega\,\mathrm{m}$, $h = 100\ \mathrm{m}$, and state the consequence
for a CSEM survey of a hydrated layer.

**★5.** Why the plane-wave response fails

The demonstration's plane-wave seafloor response is between $0.116$ and
$0.198\ \Omega\,\mathrm{m}$ at every frequency, while the sediment beneath is
$1.00\ \Omega\,\mathrm{m}$ and the target is $100\ \Omega\,\mathrm{m}$.

**(a)** Compute the conductance (thickness/resistivity) of the $1500\ \mathrm{m}$
water column and of the $900\ \mathrm{m}$ of sediment.
**(b)** State, in one sentence, why the water's conductance decides the result.
**(c)** State the geometric change that makes the sediment visible, and why it
works in terms of the *path* the fields take.

---

## ★★★ Research-oriented

**★6.** Design a survey

You are asked to detect a $200\ \mathrm{m}$ thick layer of $50\ \Omega\,\mathrm{m}$
at $250\ \mathrm{m}$ below the seafloor, beneath $1500\ \mathrm{m}$ of seawater at
$0.30\ \Omega\,\mathrm{m}$, in sediment of $1.0\ \Omega\,\mathrm{m}$.

Specify, with arithmetic where possible:

**(a)** the source–receiver offset range and why long offsets help;
**(b)** the frequency band you would acquire, with the reason for each end;
**(c)** the array geometry (number of receivers, spacing) and how it bears on
non-uniqueness;
**(d)** the four largest terms in the error budget, ranked;
**(e)** what the survey's deliverable is, and what it is *not*, in one sentence
each.

**★7.** When is the anomaly not the target?

A $10\,\%$ apparent-resistivity anomaly is measured in the middle of a band and
is interpreted as a gas-hydrate layer by the interpreter of one contractor and as
an artefact by another.

**(a)** List four *physical* causes other than a resistive layer that can produce a
band-limited positive anomaly in the seafloor response.
**(b)** For each, state the independent information that would discriminate it.
**(c)** State the prior information you would insist on before accepting the
hydrate interpretation, and why each item is necessary.

---

## Answers

Full worked solutions, with the arithmetic shown, are in
[07-marine-csem-em-solutions.md](07-marine-csem-em-solutions.md).
