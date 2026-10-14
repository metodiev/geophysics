# Exercises — 02-01-02 Measurement Uncertainty, Significant Figures and Error Bars

Attempt these **closed-book** before opening the
[solutions](./02-measurement-uncertainty-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\,30\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ with relative
uncertainty $2.2\times10^{-5}$, and
$GM_\oplus = 3.986\,004\,418\times10^{14}\ \mathrm{m^3\,s^{-2}}$ (defining).
Unless a problem says otherwise, state your coverage factor.

---

## ★ Foundational

**★1.** Rewrite each result in defensible form: (a) $2.04371 \pm 0.0123$ mGal;
(b) $979\,812.37 \pm 41$ mGal; (c) $5.123456 \pm 0.0004$ km/s;
(d) $1.000000 \pm 0.3$ (dimensionless).

---

**★2.** A gravimeter's display steps by 0.01 mGal. Twenty repeat readings at a
fixed station scatter with a sample standard deviation of 0.046 mGal.
(a) Which number is the resolution, which is the uncertainty? (b) What is the
defensible uncertainty of a **single** reading, and of the **mean** of the
twenty? (c) Why would quoting the resolution be wrong by a factor of about 5?

---

**★3.** Six repeat determinations of a field quantity give
$9.794,\ 9.801,\ 9.789,\ 9.797,\ 9.803,\ 9.792$ (in $10^{-6}\ \mathrm{m\,s^{-2}}$).
Compute (a) the mean, (b) the sample standard deviation $s$, (c) the standard
error of the mean, (d) the defensible report of the mean.

---

**★4.** Propagate the uncertainty in $q = k\,\dfrac{\Delta T}{\Delta z}$, with
$k = 2.5 \pm 0.125\ \mathrm{W\,m^{-1}K^{-1}}$, $\Delta T = 13.5 \pm 0.27$ K and
$\Delta z = 0.30 \pm 0.003$ m. Give $q$ with its relative and absolute
uncertainty, and state which input dominates.

---

## ★★ Applied

**★★5.** An anomaly measurement has four independent contributions:
$0.03$, $0.04$, $0.02$ and $0.01$ mGal. (a) Compute the combined standard
uncertainty. (b) Rank the contributions by their share of the variance.
(c) If you can halve any one of them, which choice reduces the total most, and
by how much?

---

**★★6.** Four determinations of one magnetic anomaly are
$(2.10 \pm 0.06)$, $(2.02 \pm 0.04)$, $(2.15 \pm 0.10)$ and $(2.04 \pm 0.03)$ mGal.
(a) Compute the inverse-variance weighted mean and its uncertainty.
(b) Compute $\chi^{2}$ and $\chi^{2}/\nu$. (c) Compare with the unweighted mean
and comment on whether the quoted uncertainties are credible.

---

**★★7.** An excess mass is inferred from a residual anomaly directly above it:
$M = g_z d^{2}/G$, with $g_z = 5.00 \pm 0.05\ \mu\mathrm{m\,s^{-2}}$ and
$d = 250 \pm 2.5$ m.

(a) Compute $M$.
(b) Compute the relative uncertainty contributed by each input, including $G$
(relative uncertainty $2.2\times10^{-5}$).
(c) Compute the combined relative and absolute uncertainty, and the defensible
report.
(d) Explain why $G$'s 2.2 × 10⁻⁵ matters far more when the Earth's mass is
obtained by dividing a precisely measured $GM_\oplus$ by $G$ than it does here.

---

**★★8.** An instrument's specification says "accuracy ±(0.5% of reading + 3
counts)", with 1 count = 0.001 mGal and a reading of 120.000 mGal. Convert this
to a standard uncertainty, stating the distributional assumption you make, and
explain why the answer is a *type B* uncertainty.

---

## ★★★ Research-oriented

**★★★9.** Design an experiment that reduces the uncertainty of a measured
anomaly by a factor of 4, given that the current uncertainty has a random
component of 0.040 mGal and a systematic component (calibration) of 0.030 mGal.

(a) Show that no amount of repetition achieves the goal, and quantify the limit.
(b) State what must be changed and what the target values would be.
(c) Write the resulting budget as a table with shares.

---

**★★★10.** The ratio of two independent normal variables is used as an estimator
in a geophysical inversion. With numerator $N(1.0,0.5)$ and denominator
$N(1.0,0.5)$: (a) write down the first-order quadrature estimate of the relative
uncertainty of the ratio; (b) explain why the exact ratio distribution has no
finite variance; (c) describe the numerical experiment that demonstrates this,
including what you would plot and what you would expect to see; (d) state the
reporting convention you would adopt for such an estimator.
