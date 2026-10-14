# Exercises — 04-03-03 Radiometric Dating Methods and Their Assumptions

Attempt these **closed-book** before opening the
[solutions](./03-radiometric-dating-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/03-radiometric_dating_demo.py`](../code/03-radiometric_dating_demo.py)
require you to run it and report its actual output.

**Constants.** Use $\lambda_{238} = 1.551\,25 \times 10^{-10}$ a$^{-1}$,
$\lambda_{235} = 9.8485 \times 10^{-10}$ a$^{-1}$ and
$\lambda_{\mathrm{Rb}} = 1.42 \times 10^{-11}$ a$^{-1}$. These are **tabulated
values that differ between compilations**; state in every answer that the age is
tied to this set.

---

## ★ Foundational

**★1.** Compute, for $t = 2000$ Ma,

(a) $^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U}$;
(b) $^{207}\mathrm{Pb}^{*}/^{235}\mathrm{U}$;
(c) the ratio $^{207}\mathrm{Pb}/^{206}\mathrm{Pb}$;
(d) state why the ratio in (c) changes slowly with age for young rocks and
rapidly for old ones.

---

**★2.** An analysis gives $^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U} = 0.20$.

(a) Compute the apparent age.
(b) Compute the age the same analysis would give if the ratio were lower by
0.001.
(c) State why the sensitivity of the age to a *constant* offset in the ratio is
larger for young rocks than for old ones.

---

**★3.** Define concordant and discordant. State for each whether a single age
explains the measurement, and name the diagram used to display the two ratios
together.

---

## ★★ Applied

**★★4.** A U–Pb analysis of $^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U} = 0.0806$
at 500 Ma is contaminated by uncorrected common Pb that adds 0.005 to the ratio.

(a) Compute the apparent age.
(b) Compute the error in Ma and as a fraction of the true age.
(c) Compute the same for a 100 Ma analysis with the same offset of 0.005, given
$^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U} = 0.0156$.
(d) State which of the two is more seriously affected, relative to its age, and
why.

---

**★★5.** Run
[`../code/03-radiometric_dating_demo.py`](../code/03-radiometric_dating_demo.py).

(a) Report the true age and the disturbance age used in the discordia section.
(b) Report the fitted chord coefficients and the maximum chord residual.
(c) Report both intercepts and the error of each against the input.
(d) Report the mean and spread of the seven single-chain ages and the error of
that mean, and explain why the spread, not the mean, is the diagnostic.

---

**★★6.** A three-point Rb–Sr data set defines a line of slope 0.07.

(a) Compute the "age" implied by that slope with the stated decay constant.
(b) A second data set, known to be a two-component mixing array between
compositions $(^{87}\mathrm{Rb}/^{86}\mathrm{Sr}, ^{87}\mathrm{Sr}/^{86}\mathrm{Sr})
= (0.20, 0.7110)$ and $(0.90, 0.7600)$, gives a slope of 0.07 as well. Compute
the intercept and state why it should not be interpreted as an initial ratio.
(c) List three tests that would distinguish the two data sets.
(d) Explain why $r^2$ is not one of the tests.

---

**★★7.** A sample gives a single $^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U}$ ratio
and no second chain.

(a) State what must be assumed to convert the ratio into an age.
(b) Compute the age error produced by an assumed common-Pb offset of 0.002 on a
1000 Ma analysis.
(c) State the difference between this and an isochron age, in one sentence.

---

## ★★★ Research-oriented

**★★★8.** Derive, from the two-stage history described in
[04-03-03 §4](../03-radiometric-dating.md), the relation

$$x_{\text{now}} = x_1 - f\left(x_1 - x_2\right),$$

stating carefully where the uranium decay between $t_1$ and $t_2$ enters. Then

(a) show that the family of discordant points lies on the chord between the
concordia points at $t_1$ and $t_2$;
(b) verify numerically that a synthetic set with $t_1 = 2000$ Ma,
$t_2 = 400$ Ma and $f \in \{0, 0.25, 0.5, 0.75, 1\}$ is collinear to machine
precision;
(c) report the chord residual and the two intercepts recovered by intersecting
the chord with concordia.

---

**★★★9.** Distinguish an episode of radiogenic-Pb **loss** from an episode of
**U loss** in a U–Pb data set.

(a) State on which side of concordia each places the analyses, and why.
(b) Compute the sign and size of the displacement for a synthetic sample that
loses 3 per cent of its $^{238}\mathrm{U}$ at 300 Ma, evaluated at the present
day, using a crystallisation age of 1500 Ma.
(c) State the additional observation that distinguishes a two-stage history from
a multi-stage one.
(d) State what the analysis cannot determine at all, and why a stated
interpretation is required.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
