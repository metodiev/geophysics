# Exercises — 18-06-05 Visualising and Communicating Uncertainty

Lesson: [05 Visualising and Communicating Uncertainty](../05-uncertainty-visualisation.md).
Attempt these before reading the [solutions](./05-uncertainty-visualisation-solutions.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Define pointwise coverage and simultaneous coverage of a credible band in
one sentence each.

**★2.** A pointwise $95\%$ band has half-width $1.959963984540054\,\sigma$. From the
demonstration's measured simultaneous factor of $2.651$, compute the simultaneous
half-width and the percentage increase.

**★3.** The demonstration measures a pointwise coverage of $95.23\%$ and a
whole-curve coverage of $74.25\%$ for the same $95\%$ band. Explain in two sentences
why the second number is lower and what it means for a reader.

## ★★ Applied

**★★4.** For the strongly skewed travel-time example, the mean is $0.9246$ s and
the standard deviation is $0.6082$ s. Compute mean $-2$ s.d. and state the physical
objection to plotting it.

**★★5.** The demonstration reports equal-tailed and HPD intervals for the skewed case
with widths $2.2660$ s and $1.9591$ s. Compute the ratio and state which interval you
would put on a figure if the caption must be short, and why.

**★★6.** Two models' $95\%$ bands overlap at $100\%$ of depths, and a $\log_{10}$
Bayes factor of $3.86$ favours one of them. Convert the Bayes factor to a posterior
probability under equal model priors and state the conclusion a figure alone could
not support.

**★★7.** A figure shows a $95\%$ band but the caption says only "uncertainty in the
velocity model". List the four pieces of information that must be added for the
figure to be auditable.

## ★★★ Research-oriented

**★★★8.** Design a figure (no code required) that communicates a posterior with a
strong skew and a strong correlation between two parameters, to a reader who will look
at it for five seconds. State the panels, the encodings, the caption, and what you
deliberately omit.
