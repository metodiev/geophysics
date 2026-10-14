# Exercises — 25-04-05 Project: Joint Gravity-Seismic Inversion

Attempt these before reading the
[solutions](./05-joint-inversion-project-solutions.md). The project is
[05 Joint Inversion](../05-joint-inversion-project.md). Values printed by
[`code/joint_inversion_demo.py`](../code/joint_inversion_demo.py):

| Dataset | $\chi^2$/datum | mean 1σ (kg m⁻³) | mean error | $\operatorname{tr}R$ |
|---|---|---|---|---|
| gravity only | 0.9617 | 14.56 | 22.36 | 19.23 / 32 |
| seismic only | 0.8767 | 56.51 | 29.08 | 5.04 / 32 |
| joint | 0.7697 | 14.23 | 21.09 | 19.65 / 32 |
| link doubled | — | — | change 268.0 | misfit 0.7462 |
| link reversed | — | — | change 40.0 | misfit 6262.7 |

Model: 8 blocks × 4 layers (32 parameters); 20 gravity stations (0.05 mGal);
24 paths (0.05 s); link $v = 4500 + 0.4(\rho - 2500)$ m/s.
Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Write the gravity kernel and the travel-time kernel per unit density, with
units, and state why the travel-time kernel is sparse while the gravity kernel is
not.

**★2.** A path of 40 km at $v = 4500\ \mathrm{m\,s^{-1}}$ crosses a block whose
density rises by $250\ \mathrm{kg\,m^{-3}}$. Using the link, compute the change in
$v$, the fractional change, and the change in travel time. Compare with the stated
noise of $0.05\ \mathrm{s}$.

**★3.** Compute the ratio of the joint mean uncertainty to the gravity-only mean
uncertainty, and of the joint mean model error to the gravity-only error. State
what each ratio measures.

## ★★ Applied

**★★4.** The joint resolution trace is 19.65 of 32 against 19.23 for gravity alone.
Compute the number of *additional* resolved parameters, and the number of
additional data (24 paths). State the cost–benefit in one sentence.

**★★5.** The link's slope is doubled with no change in misfit. Explain in two
sentences, in terms of the product that enters the travel time, why the data cannot
detect it, and state what additional information would.

**★★6.** Gravity-only resolves 19.23 of 32 parameters and the joint inversion
19.65. Estimate the fraction of the model that remains unresolved in each case, and
state which parameter group (shallow or deep) the remaining null space most likely
occupies, using the layer-by-layer errors (13.13 / 19.66 for gravity; 10.91 / 22.23
for joint) as evidence.

## ★★★ Research-oriented

**★★★7.** Design a joint inversion that can *constrain* the petrophysical link
rather than assume it. State the parameterisation (including the link's
parameters), why the link becomes identifiable in your design when it is not in a
linear one, the independent data that pin the link's scale, the resolution
statement you would report for the link itself, and the synthetic test that would
prove the link is recovered. A design whose link remains degenerate is a failed
answer.
