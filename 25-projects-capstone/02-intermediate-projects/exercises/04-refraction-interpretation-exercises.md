# Exercises — 25-02-04 Project: Interpreting a Refraction Survey

Attempt these before reading the
[solutions](./04-refraction-interpretation-solutions.md). The project is
[04 Refraction Interpretation](../04-refraction-interpretation.md). Values
printed by
[`code/refraction_interpretation_demo.py`](../code/refraction_interpretation_demo.py):

| Quantity | Model A | Model B |
|---|---|---|
| $v_1$ (km s⁻¹) | 0.40 | 1.00 |
| $v_2$ (km s⁻¹) | 1.60 | 1.50 (hidden) |
| $v_3$ (km s⁻¹) | 4.00 | 5.00 |
| $h_1$ / $h_2$ (m) | 3.0 / 8.0 | 2.0 / 2.0 |
| critical angles | $14.5°$, $5.7°$ | — |
| crossovers (m) | 8.0, 26.0 | 9.0 would be, 7.5 is |
| inverted $v_2$ / $v_3$ | $1.600$ / $4.001$ | — |
| inverted $h_1$ / $h_2$ | $3.00$ / $8.00$ | — |
| apparent depth (2-layer) | — | $3.30$ vs true $4.00$ |

Picks: 59 offsets, 1 to 60 m, first arrivals, Gaussian noise 1.5 ms.
Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** For model A, compute the critical angle for refraction along the top of
layer 2 and along the top of layer 3, and state which interface produces the
first arrival at 40 m.

**★2.** Compute the crossover offset between the direct wave and the head wave
along layer 2 for $v_1 = 0.50\ \mathrm{km\,s^{-1}}$,
$v_2 = 2.00\ \mathrm{km\,s^{-1}}$ and $h_1 = 4.0\ \mathrm{m}$.

**★3.** Using the intercepts $a_2 = 14.522115\ \mathrm{s}$ and
$a_3 = 24.091503\ \mathrm{s}$ with $v_1 = 0.40$, $v_2 = 1.600$ and
$v_3 = 4.001\ \mathrm{km\,s^{-1}}$ (SI: $v_1 = 400$, $v_2 = 1600$,
$v_3 = 4001\ \mathrm{m\,s^{-1}}$), compute $h_1$ from the branch-2 intercept and
state its unit.

## ★★ Applied

**★★4.** Using the $h_1$ from ★3, compute $h_2$ from the branch-3 intercept with
the formula of §5 of the lesson, and compare with the true 8.0 m.

**★★5.** For model B, show that the crossover from branch 1 to branch 2 would be
at 9.0 m, that the crossover from branch 2 to branch 3 is at 7.5 m, and hence
that branch 2 is never the first arrival. State the general condition this
illustrates.

**★★6.** For model B, compute the two-layer apparent depth from the branch-3
intercept, compare it with $h_1 + h_2 = 4.00\ \mathrm{m}$, and express the error
as a percentage and as a number of pick standard deviations (pick
$\sigma = 1.5\ \mathrm{ms}$, and the observed branch spans 35 m at
$5.0\ \mathrm{km\,s^{-1}}$).

## ★★★ Research-oriented

**★★★7.** Design an acquisition and interpretation that removes the hidden-layer
ambiguity at a site where a 2 m layer of $1.5\ \mathrm{km\,s^{-1}}$ may lie
between a $1.0\ \mathrm{km\,s^{-1}}$ surface layer and a
$5.0\ \mathrm{km\,s^{-1}}$ bedrock. State the added method, what it measures,
why it is sensitive where first arrivals are not, the depth resolution you expect,
and the cost. A design that cannot detect the layer is a failed answer.
