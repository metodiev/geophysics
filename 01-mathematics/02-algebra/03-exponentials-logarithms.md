---
id: 01-02-03
title: "Exponentials, Logarithms and Decay Laws in Earth Science"
level: beginner
prereqs: ["01-02-02"]
estimated_minutes: 75
tags: [exponential, logarithm, decay, half-life, attenuation]
---

# Exponentials, Logarithms and Decay Laws in Earth Science

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** any decay or growth process in each of its three equivalent forms —
   base $e$, base 2, and e-folding time.
2. **Convert** between decay constant, half-life and mean life, and say which one
   a given problem wants.
3. **Apply** the laws of logarithms to linearise an exponential relation, and read
   the parameters off the intercept and slope.
4. **Invert** an exponential law for time or for a rate, including the
   radiometric age equation and Newton's cooling law.
5. **Distinguish** an exponential from a power law, and state what a straight line
   on a semilog plot does and does not prove.

## Prerequisites

[01-02-02 Functions, Graphs and Transformations](./02-functions-and-graphs.md) for
the exponential family and inverses, and
[01-02-01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
Section 3.4 for solving for a variable in an exponent.

## 1. Intuition: the difference between adding and multiplying

Linear processes add a fixed amount per unit time. Exponential processes multiply
by a fixed factor per unit time. Almost every *rate* law in the Earth sciences is
of the second kind, because a rate is usually proportional to how much of
something is left:

- a radioactive parent decays at a rate proportional to the number of nuclei
  present;
- seismic energy is lost at a rate proportional to the energy in the wave;
- a cooling body loses heat at a rate proportional to its temperature excess;
- a chemical species reacting in a pore water is consumed at a rate proportional
  to its concentration.

When "rate proportional to amount" is written down and solved (a differential
equation, in
[01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)),
the answer is always the same shape:

$$N(t) = N_0 e^{-\lambda t}.$$

That is why one function dominates the subject, and why the logarithm — its
inverse — is the standard tool for extracting rates from data.

## 2. Definitions

### 2.1 The exponential function

For a real constant $k$, the function

$$f(t) = A e^{kt}, \qquad A > 0,$$

is an exponential with **initial value** $A$ (i.e. $f(0) = A$) and **rate
constant** $k$. If $k > 0$ the function grows; if $k < 0$ it decays; if $k = 0$ it
is constant and carries no information about $t$.

Its distinguishing property is that the **relative** rate of change is constant:

$$\frac{1}{f}\frac{df}{dt} = k.$$

No polynomial has this property, and that is why exponentials cannot be replaced
by polynomials in a physical model, however high the degree.

### 2.2 Three ways to write the same decay

| parameter | definition | appears in |
|---|---|---|
| decay constant $\lambda$ | $\lambda = -\dot N/N$, units 1/time | the differential equation and the Laplace transform |
| half-life $T_{1/2}$ | time for $N$ to halve | decay-series tables, radiometric dating |
| mean life $\tau$ | $\tau = 1/\lambda$ | the e-folding vocabulary, filters and time constants |

For $N(t) = N_0e^{-\lambda t}$ the half-life follows from $N(T_{1/2}) = N_0/2$:

$$e^{-\lambda T_{1/2}} = \frac{1}{2}
\;\Longrightarrow\;
\lambda T_{1/2} = \ln 2
\;\Longrightarrow\;
T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693147\ldots}{\lambda}.$$

Equivalently $N(t) = N_0 2^{-t/T_{1/2}}$, which is the same function written in a
form that makes the half-life explicit. The demonstration prints all three for
$^{14}$C with the conventional $T_{1/2} = 5730$ yr:

$$\lambda = 1.209681\times10^{-4}\ \mathrm{yr^{-1}}, \qquad
\tau = 8266.6\ \mathrm{yr}.$$

**Note on the constants.** $^{14}$C is conventionally quoted as
$5730 \pm 40$ yr; the older Libby value of 5568 yr still appears in some
literature. Which one is used changes ages by about 3%, and published
radiocarbon ages should state it.

### 2.3 The logarithm

The natural logarithm is the inverse of the exponential:

$$y = e^{x} \iff x = \ln y, \qquad y > 0.$$

The laws follow directly:

$$\ln(ab) = \ln a + \ln b, \qquad
\ln\frac{a}{b} = \ln a - \ln b, \qquad
\ln a^{p} = p\ln a, \qquad
\log_{10}x = \frac{\ln x}{\ln 10}.$$

Two properties do most of the work in this module:

- **Products become sums.** A product of many attenuation factors becomes a sum
  of exponents, which is why attenuation is measured in decibels (a logarithmic
  unit).
- **Multiplicative change becomes linear.** Taking logarithms of $N = N_0e^{-\lambda
  t}$ gives $\ln N = \ln N_0 - \lambda t$: a **straight line** in $t$.

## 3. Linearising an exponential

Equation $\ln N = \ln N_0 - \lambda t$ has the form $y = b + mt$ with

$$y = \ln N, \qquad b = \ln N_0, \qquad m = -\lambda.$$

So a straight line on **semilog** axes gives you the decay constant as minus the
slope and the initial value as $\exp(\text{intercept})$.

The demonstration fits a synthetic counting series exactly: for
$T_{1/2} = 14$ days, $\lambda = 0.049511\ \mathrm{day^{-1}}$, data generated from
$N(t) = 10000\,e^{-\lambda t}$ at $t = 0, 2, \dots, 18$ days, the least-squares
fit of $\ln N$ against $t$ returns

$$\text{slope} = -0.049511\ \mathrm{day^{-1}}, \qquad
\text{intercept} = 9.210340,$$

so $\lambda = 0.049511$ and $T_{1/2} = 14.0000$ days, with
$N_0 = e^{9.210340} = 10000.00$ counts. Exact recovery is expected because the
data are exact; with real counts the scatter in $\ln N$ would widen the confidence
interval on the slope. (Note also the *asymmetry*: fitting in log space treats
small counts as heavily as large ones, so counting data are usually weighted.)

## 4. What a straight line does and does not prove

A straight line on a semilog plot is evidence for exponential behaviour *only
within the plotted range*. Two traps:

1. **A power law on log–log axes is also straight.** $y = ax^{p}$ gives
   $\ln y = \ln a + p\ln x$, a straight line against $\ln x$, not against $x$.
   The way to tell them apart is to test which transformation straightens the data.
2. **Most real decay is a sum of exponentials.** A mixture of decay constants
   plots as a curve that only *looks* straight over a couple of decades. Fitting a
   single exponential to a mixture gives a decay constant that is a weighted
   average of the components — a systematic, not a random, error.

## 5. Worked derivations

### 5.1 From the decay law to the age equation

Let a parent nuclide $P$ decay with constant $\lambda$ and let all of it become
daughter $D^{*}$. If no daughter was present initially, then at time $t$,

$$P(t) = P_0e^{-\lambda t}, \qquad D^{*}(t) = P_0 - P(t)
= P_0\left(1 - e^{-\lambda t}\right).$$

Dividing eliminates the unknown initial amount $P_0$:

$$\frac{D^{*}}{P} = \frac{1 - e^{-\lambda t}}{e^{-\lambda t}}
= e^{\lambda t} - 1.$$

This is the **isochron equation**. Inverting it:

$$e^{\lambda t} = 1 + \frac{D^{*}}{P}
\qquad\Longrightarrow\qquad
t = \frac{1}{\lambda}\ln\!\left(1 + \frac{D^{*}}{P}\right).$$

The logarithm is doing the essential work: it turns a *ratio* into a *time*.

**Numbers.** For $^{238}$U $\to$ $^{206}$Pb, using the commonly quoted
$T_{1/2} = 4.468\times10^{9}$ yr, $\lambda = \ln2/T_{1/2}
= 1.551359\times10^{-10}\ \mathrm{yr^{-1}}$:

| $^{206}$Pb$^{*}$/$^{238}$U | age (Ma) |
|---|---|
| $0.10$ | $614.4$ |
| $0.50$ | $2613.6$ |
| $1.00$ | $4468.0$ |
| $2.00$ | $7081.6$ |
| $4.00$ | $10374.4$ |

Read the first and last rows together: quadrupling the daughter/parent ratio does
not quadruple the age, because the parent is being depleted as the daughter grows.
The ratio $1.00$ gives exactly one half-life, as it must, since half the parent has
decayed.

**Assumptions, stated.** No initial daughter; a closed system (no gain or loss of
either nuclide); a constant decay constant (safe for these nuclides on these time
scales). Each violated assumption biases the age, and each has its own community
of corrections — that is why dating is a science and not an arithmetic exercise.

### 5.2 Seismic attenuation and the quality factor

For a wave of frequency $f$ travelling distance $x$ in a medium of speed $v$ and
quality factor $Q$, the amplitude decays as

$$A(x) = A_0e^{-\alpha x}, \qquad
\alpha = \frac{\pi f}{Qv}.$$

**Derivation of the shape.** Energy loss per cycle is $2\pi/Q$ of the stored
energy, so the fractional energy loss per unit distance is $2\pi f/(Qv)$, and
since energy goes as the square of amplitude, the amplitude decays with rate
$2\pi f/(2Qv) = \pi f/(Qv)$. (This is the standard constant-$Q$ attenuation
model; the factor of two is the one that is most often dropped.)

**Numbers.** With $f = 20$ Hz, $v = 3500$ m/s and $Q = 100$:

$$\alpha = \frac{\pi \times 20}{100 \times 3500} = 1.795\times10^{-4}\ \mathrm{m^{-1}},
\qquad \frac{1}{\alpha} = 5570.4\ \mathrm{m}.$$

So the amplitude falls by a factor $e$ every 5.57 km. Over 100 m,
$A/A_0 = 0.9822$; over 1000 m, $0.8357$.

**Inverting for $Q$.** Measuring the ratio at two distances and taking logarithms:

$$\ln\frac{A(x_2)}{A(x_1)} = -\frac{\pi f}{Qv}(x_2 - x_1)
\qquad\Longrightarrow\qquad
Q = -\frac{\pi f (x_2-x_1)}{v\,\ln\!\big(A(x_2)/A(x_1)\big)}.$$

With the synthetic values above, feeding back
$A(200)/A(100) = 0.982208$ returns $Q = 100.0$ exactly — the cancellation of the
forward and inverse operations. In real data $Q$ estimation is harder, mainly
because the geometric spreading and scattering must be removed first, and because
the logarithm of a ratio of noisy amplitudes is a noisy quantity.

### 5.3 Newton cooling of a shallow intrusion

A body embedded in a medium of different temperature relaxes towards the ambient
temperature with a fixed time constant:

$$T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}.$$

Solving for the time at which a threshold temperature is reached:

$$t = -\tau\ln\!\left(\frac{T - T_\infty}{T_0 - T_\infty}\right).$$

**Numbers.** With $T_\infty = 10\,^\circ$C, $T_0 = 900\,^\circ$C, $\tau = 4$ days
and a threshold of $100\,^\circ$C:

$$t = -4\ln\!\left(\frac{90}{890}\right) = 9.166\ \text{days}.$$

The demonstration's check, $T(9.166) = 100.000000\,^\circ$C, confirms it. The
temperature excess decays by a factor $e$ every 4 days: 890, 539.81, 327.41,
120.45 and 16.30 °C after 0, 2, 4, 8 and 16 days.

**Caveat that matters.** This is the law for a body whose internal temperature is
uniform and whose exchange with the surroundings is proportional to the excess —
a lumped-parameter model. A real intrusion cools by conduction, with a
temperature profile that is not uniform, and the appropriate solution is not
exponential (it involves the error function). The exponential is the correct
0th-order model, and it is an approximation, not a result.

### 5.4 The continuous-compounding limit

If a quantity grows by a factor $(1 + r/n)$ in each of $n$ intervals per unit time,
then after unit time it has grown by

$$\left(1 + \frac{r}{n}\right)^{n} \xrightarrow[n\to\infty]{} e^{r},$$

the limit verified numerically in
[01-02-02](./02-functions-and-graphs.md), Section 7.5. This is why $e$ appears in
every continuous rate law: it is the result of compounding a growth rate
infinitely often and in infinitely small pieces.

## 6. Python demonstration

```bash
python3 code/exponential_decay_demo.py
```

The script `code/exponential_decay_demo.py` uses only the standard library. It
covers: the three parameterisations of the decay law; conventional $^{14}$C ages
from activity ratios; the $^{238}$U–$^{206}$Pb isochron equation; exact recovery
of a decay constant by log-linear least squares on synthetic counts; seismic
attenuation and the recovery of $Q$; and Newton cooling with the threshold-time
inversion.

Observed output worth dwelling on:

```text
      N/N0    conventional age (yr)
     0.500                     5730
     0.100                    19035
     0.010                    38069
```

```text
f = 20 Hz, v = 3500 m/s, Q = 100
attenuation coefficient alpha = pi f / (Q v) = 1.795e-04 /m
skin depth 1/alpha = 5570.4 m
```

| Observation | Consequence in geophysics |
|---|---|
| ratio 0.5 gives exactly one half-life | the half-life is the natural unit; ages are often quoted in half-lives |
| 1% of the parent left gives 38 069 yr | the practical limit of $^{14}$C dating is set by measurement, not by the arithmetic |
| $\alpha$ for 20 Hz at $Q=100$ is $1.8\times10^{-4}$ m⁻¹ | attenuation is negligible over 10 m and dominant over 10 km |
| log-linear fit recovers $\lambda$ exactly for exact data | the *method* is unbiased; noise is a separate question |
| $Q$ recovered as 100.0 from two amplitudes | consistency checks are free when you control the model |

## 7. Exercises

Ten graded exercises with full worked solutions are in
[`exercises/03-exponentials-logarithms-exercises.md`](./exercises/03-exponentials-logarithms-exercises.md)
and
[`exercises/03-exponentials-logarithms-solutions.md`](./exercises/03-exponentials-logarithms-solutions.md).

**★1.** Convert: (a) $T_{1/2} = 5730$ yr to $\lambda$ in yr⁻¹; (b) $\lambda = 0.05$
day⁻¹ to a half-life in days; (c) $N(t) = 100e^{-0.3t}$ to the form
$N_0 2^{-t/T_{1/2}}$.

**★★2.** For a decay law with $T_{1/2} = 5730$ yr, how long until 0.1% of the
parent remains? Answer it in half-lives first, then numerically.

**★★★3.** Design and run an experiment that shows where a single-exponential fit
breaks down for a two-component decay. Construct a synthetic series
$N(t) = A e^{-\lambda_1 t} + B e^{-\lambda_2 t}$, fit a single slope by least
squares over different time windows, and report how the fitted apparent decay
constant depends on the window and on the mixture ratio. State the limits of your
conclusion.

## 8. Common mistakes

1. **Dropping the factor of 2 in the attenuation exponent.** Energy loss per cycle
   is $2\pi/Q$; the *amplitude* decays at half that rate. Getting it wrong doubles
   or halves every $Q$ you report.
2. **Confusing mean life with half-life.** $\tau = 1/\lambda = T_{1/2}/\ln 2$, so
   $\tau$ is about 44% larger than $T_{1/2}$; the two are not interchangeable.
3. **Using a log axis and calling the result a proof.** A power law is also
   straight on log–log axes.
4. **Forgetting that a logarithm needs a positive argument.** A negative
   amplitude, a zero count or a negative ratio has no logarithm, and the code will
   either error or return a NaN.
5. **Taking logarithms of raw counts without weighting.** The log transform makes
   the error distribution asymmetric; small counts dominate an unweighted fit.
6. **Quoting an age without its model.** Every age is the output of a model with
   assumptions; state them, or the number is not reproducible.
7. **Treating a lumped-parameter exponential as exact physics.** Newton cooling
   assumes a uniform temperature; conduction does not give an exponential.

## 9. Real-world applications

- **Geochronology.** U–Pb, Rb–Sr, K–Ar and radiocarbon dating are all inversions
  of the isochron or decay equation; the differences between them are in the
  chemistry and the corrections, not the algebra.
- **Seismic and ultrasonic attenuation.** $Q$ estimates from amplitude decay,
  spectral ratios and rise-time methods; all require the logarithmic relation
  above.
- **Ground-penetrating radar and electromagnetic methods.** Skin depth
  $\delta = 1/\alpha$ sets the investigation depth, and it depends on frequency
  and conductivity in exactly the exponential way.
- **Thermal and hydrologic transients.** Time constants of borehole temperature
  recovery, groundwater recession curves, and the response of a catchment to
  rainfall are modelled as exponential relaxations.
- **Radioactive waste and heat production.** Radiogenic heat production decays
  exponentially; the present-day budget reflects the integrated decay history of
  the isotopes involved.
- **Anomaly decay with depth.** The far-field behaviour of potential fields is a
  power law, not an exponential — a useful reminder that not every "decay" is
  exponential, and that the distinction is testable on a log–log plot.

## 10. Further reading

- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd
  ed.). Wiley.** Sections on exponential and logarithmic functions and on
  first-order rate processes. Level: beginner to intermediate.
- **Turcotte, D. L., & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Chapters on heat transfer and on radioactive decay and
  radiogenic heating. Level: intermediate. Standard for the physics behind the
  laws used here.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Chapter on attenuation and anelasticity. Level:
  advanced. The source of the constant-$Q$ model in Section 5.2.
- **Stewart, J. *Calculus: Early Transcendentals* (current edition).** Chapter on
  exponential and logarithmic functions. Level: beginner.
- **Dickin, A. P. (2005). *Radiogenic Isotope Geology* (2nd ed.). Cambridge
  University Press.** Level: intermediate to advanced. For the assumptions behind
  every dating equation, and how they are tested.

> Note on citations: bibliographic details are given so you can locate the works;
> editions and page numbers vary, and this repository does not reproduce
> copyrighted text.

## 11. Related lessons

- [02 Functions, Graphs and Transformations](./02-functions-and-graphs.md) —
  Sections 3.3 and 7.5 are the prequel to this lesson.
- [01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
  — Section 3.4, solving for a variable inside an exponential.
- [04 Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md) —
  the other half of the "which model fits?" question.
- [01-08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
  — why exponential solutions appear whenever a rate is proportional to a
  quantity.
- [01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md)
  — fitting these laws to noisy data, with confidence intervals.

## Self-assessment checklist

- [ ] I can convert freely between $\lambda$, $T_{1/2}$ and $\tau$.
- [ ] I can linearise an exponential relation and read the parameters from slope
      and intercept.
- [ ] I can derive the isochron equation and invert it for an age.
- [ ] I can state the constant-$Q$ attenuation relation with the correct factor.
- [ ] I can explain why $e$ appears in continuous rate laws.
- [ ] I can say what a straight line on a semilog plot does *not* prove.
