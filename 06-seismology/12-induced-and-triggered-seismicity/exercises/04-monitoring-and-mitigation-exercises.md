# Exercises — 06-12-04 Traffic-Light Protocols, Monitoring and Mitigation

Attempt these before reading the
[solutions](./04-monitoring-and-mitigation-solutions.md). The lesson is
[04 Traffic-Light Protocols, Monitoring and Mitigation](../04-monitoring-and-mitigation.md);
all numbers are printed by
[`../code/traffic_light_demo.py`](../code/traffic_light_demo.py). All models are
**SYNTHETIC** teaching values; no real project, protocol or regulation is
described.

## ★ Foundational

**★1.** With $M_c = 1.0$, $b = 1.00$ and $n_0 = 100$ events/yr at or above
$M_c$, compute the rate $n_0 10^{-b(M_t-M_c)}$ and the probability of at least one
event in one year, $1 - e^{-\text{rate}}$, for $M_t = 3.0$ and $M_t = 4.0$.
Compare with the demonstration's $1.0000$ and $0.6321$ (at $M_t = 3.0$) and
$0.0952$ (at $M_t = 4.0$).

**★2.** Compute the expected number of threshold crossings in a 10-year programme
at one site and at 20 sites for $M_t = 2.0$ and $M_t = 3.0$, and state the
functional dependence on the number of sites.

**★3.** Using $E[M_{\max}] = M_c + (\ln N + \gamma_E)/(b\ln 10)$ with
$\gamma_E = 0.5772$, compute the expected maximum magnitude for $N = 1000$ and
compare with the demonstration's model column ($4.251$).

## ★★ Applied

**★★4.** The demonstration computes the number of events needed for a 50% chance
of exceeding $M_t$ as approximately $0.693\times10^{b(M_t-M_c)}$. Verify the
$M_t = 5.0$ entry ($6930$) and explain why the number grows only as
$10^{b\Delta M}$ — i.e. why halving a magnitude increment does not halve the
number of events.

**★★5.** The demonstration reports 5–95% spreads of $1.696$, $1.765$, $1.771$ and
$1.746$ magnitude units for $N = 10, 100, 1000, 10000$, and the asymptotic Gumbel
spread $\frac{1}{b\ln 10}\ln\!\left(\frac{\ln 0.05}{\ln 0.95}\right) = 1.766$.
Compute the Gumbel value and state what its constancy in $N$ means for a
traffic-light protocol that "waits for more data".

**★★6.** The demonstration reports a naive formula $\log_{10}N/b$ that
underestimates the mean by $0.251$ magnitude units for $b = 1$. Reproduce that
offset from the two formulas and state which term is being dropped.

## ★★★ Research-oriented

**★★★7.** Using the demonstration's toy cost model
$\text{cost}(M_t) = c_{\text{trip}}\,\text{rate}(M_t) + c_{\text{dmg}}\,
\text{rate}(M_{\text{dmg}})e^{-\text{rate}(M_t)W}$, derive the condition for an
interior optimum, and state for which of the demonstration's five
$(c_{\text{trip}}, c_{\text{dmg}})$ pairs the optimum is at a boundary and why.

**★★★8.** Derive the Gumbel distribution of the maximum of $N$ independent
Gutenberg-Richter magnitudes and hence the asymptotic 5–95% spread
$\frac{1}{b\ln 10}\ln(\ln 0.05/\ln 0.95)$. State the two approximations made in
taking the limit.

**★★★9.** A regulator asks you to certify that a project "cannot produce an event
above magnitude 4". Using only the demonstration's arithmetic, write the three
statements you can honestly make, the one you cannot, and the observation that
would falsify your certification.
