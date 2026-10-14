# Exercises — 01-02-03 Exponentials, Logarithms and Decay Laws in Earth Science

Attempt these **closed-book** before opening the
[solutions](./03-exponentials-logarithms-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless a problem says otherwise, quote **conventional** constants and label
synthetic data as such.

---

## ★ Foundational

**★1.** Convert, showing the intermediate step:

(a) $T_{1/2} = 5730$ yr to a decay constant in yr⁻¹.

(b) $\lambda = 0.05$ day⁻¹ to a half-life in days.

(c) $N(t) = 100\,e^{-0.3t}$ to the form $N(t) = N_0 2^{-t/T_{1/2}}$.

(d) $\tau = 8266.6$ yr (the mean life of $^{14}$C) to a half-life.

---

**★2.** For $T_{1/2} = 5730$ yr, how long does it take for only $0.1\%$ of the
parent to remain?

(a) Answer in half-lives first, using logarithms base 2.

(b) Then convert to years.

(c) Comment on why 0.1% is beyond the practical range of radiocarbon dating even
though the arithmetic still works.

---

**★3.** Evaluate, using the laws of logarithms rather than a calculator where
possible:

(a) $\ln e^{3}$
(b) $\ln 1$
(c) $\ln(1/e)$
(d) $\log_{10}1000$
(e) $\ln\!\left(\dfrac{a^{2}b}{c}\right)$ in terms of $\ln a$, $\ln b$, $\ln c$.

---

**★4.** For $N(t) = 100\,e^{-0.3t}$, compute $N$ at $t = 0, 1, 2, 5$ and state
the ratio between successive values at unit time steps. Then state whether the
series is better described by a constant difference or a constant ratio.

---

## ★★ Applied

**★★5.** A $^{14}$C measurement gives $N/N_0 = 0.25$.

(a) Compute the conventional age in years, using $T_{1/2} = 5730$ yr.

(b) Explain, using the properties of $2^{-n}$, why the answer must be an exact
whole number of half-lives, and state how many.

(c) State two corrections that a radiocarbon laboratory would apply before
reporting a calendar age, and say why the number in (a) is not one.

---

**★★6.** This is the isochron derivation. Let a parent nuclide decay with constant
$\lambda$ into a daughter that is retained, with no daughter present initially.

(a) Write $P(t)$ and show that $D^{*}(t) = P_0(1 - e^{-\lambda t})$.

(b) Divide to eliminate $P_0$ and derive the isochron equation
$D^{*}/P = e^{\lambda t} - 1$.

(c) Invert it to obtain
$t = \lambda^{-1}\ln(1 + D^{*}/P)$.

(d) Evaluate the age for $D^{*}/P = 0.5$ with
$T_{1/2} = 4.468\times10^{9}$ yr (commonly quoted for $^{238}$U).

(e) Rewrite the isochron equation in a form that is **linear in $t$**, and
explain why that form is the one a laboratory fits.

(f) State three assumptions of the derivation and, for each, whether violating it
makes the computed age too old or too young. (Reason qualitatively; no
calculation required.)

---

**★★7.** A wave with $f = 20$ Hz travels in a medium with $v = 3500$ m/s and
$Q = 100$.

(a) Compute the amplitude attenuation coefficient $\alpha$ and the skin depth
$1/\alpha$.

(b) Compute $A/A_0$ at $x = 100$ m, $500$ m and $1000$ m.

(c) Given the synthetic amplitude ratio $A(500)/A(100) = 0.930710$, recover $Q$
and compare with 100.

(d) Explain, in one sentence, what the factor of 2 in the derivation of
$\alpha = \pi f/(Qv)$ comes from.

---

**★★8.** A body cools by Newton's law with $T_\infty = 10\,^\circ$C,
$T_0 = 900\,^\circ$C and $\tau = 4$ days.

(a) Write the cooling law and compute $T$ at $t = 0, 4, 8$ days.

(b) Solve for the time at which $T = 200\,^\circ$C and verify by substitution.

(c) Explain what $\tau$ means physically, and why it is not the half-life.

(d) State what physical assumption of the lumped-parameter model is violated by a
real intrusion, and what the correct treatment would involve.

---

## ★★★ Research-oriented

**★★★9.** A single exponential fitted to a **mixture** is biased. Construct a
synthetic two-component series

$$N(t) = 1000\,e^{-\lambda_1 t} + 500\,e^{-\lambda_2 t},$$

with $\lambda_1 = \ln 2/5$ day⁻¹ and $\lambda_2 = \ln 2/100$ day⁻¹.

(a) State the two half-lives and identify which component dominates at
$t \to \infty$.

(b) Fit a single exponential by least squares on $\ln N$ versus $t$ over the
windows $[1, 20]$, $[1, 50]$, $[1, 200]$ and $[1, 1000]$ days. Report the apparent
decay constant, the implied half-life and $R^{2}$ for each window.

(c) Report the trend: does the apparent decay constant approach $\lambda_1$,
$\lambda_2$, or neither?

(d) Explain why the window length becomes the *dominant* control on the answer,
and what that implies for reporting a decay constant fitted to real data.

(e) State the limits of your conclusion: what would change if the mixture ratio
$A/B$ were reversed, or if the components were separated by only a factor of two
in half-life instead of twenty?

---

**★★★10.** Design a test that distinguishes an exponential from a power law.

(a) Generate two synthetic data sets on $t = 1, 2, \dots, 100$:

$$y_{\exp}(t) = 100\,e^{-0.02\,t}, \qquad y_{\text{pow}}(t) = 1000\,(t+1)^{-1.5}.$$

(b) For each data set, compute the coefficient of determination $R^{2}$ of a
straight-line fit to $\ln y$ versus $t$ (semilog) and to $\ln y$ versus $\ln t$
(log–log). Tabulate the four values.

(c) Does the larger $R^{2}$ correctly identify the family in both cases? Compare
the semilog $R^{2}$ for the power-law data with the log–log $R^{2}$ for the
exponential data and comment on how much marginal evidence there is.

(d) State the danger of relying on $R^{2}$ alone for this decision, and give one
additional diagnostic you would compute.

(e) Report the method, results, and the limits of your conclusion (in particular,
the role of the chosen amplitudes and the fitted range).

---

## Extension ideas

- Fit the attenuation law to a synthetic amplitude series with multiplicative
  noise, and compare the bias in $Q$ from a fit in log space with that from a fit
  in linear space.
- Take a real decay series table and reproduce the age calculation for a ratio you
  choose, stating which half-life value you used and why.
- Construct a three-component mixture and show that the apparent decay constant
  fitted over a fixed window depends on all three amplitudes. Explain what this
  means for the interpretation of "the" relaxation time of a natural system.
