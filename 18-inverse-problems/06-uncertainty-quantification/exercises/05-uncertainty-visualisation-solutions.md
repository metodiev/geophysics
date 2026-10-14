# Solutions — 18-06-05 Visualising and Communicating Uncertainty

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [05 Visualising and Communicating Uncertainty](../05-uncertainty-visualisation.md).

---

## ★1 — Two kinds of coverage

**Pointwise:** at each location separately, the stated fraction of the probability
lies inside the band; equivalently, for a new draw the band covers that location's
value with the stated probability.

**Simultaneous:** the stated fraction of the probability lies inside the band at
*every* location at once — for a new draw, the whole curve lies inside the band with
the stated probability.

---

## ★2 — Widening for simultaneity

$$
\text{half-width}_{\text{simultaneous}} = 2.651\,\sigma,
\qquad
\text{half-width}_{\text{pointwise}} = 1.959963984540054\,\sigma,
$$

$$
\text{increase} = \frac{2.651}{1.959963984540054} - 1 = 0.3526 = 35.3\% .
$$

---

## ★3 — Why the whole-curve coverage is lower

A pointwise band has to cover a single location, so a $95\%$ band fails at each
location with probability $0.05$. A curve that must lie inside the band at *all*
$120$ locations fails if it leaves the band anywhere, and over a correlated process
those failures accumulate, leaving $74.25\%$. A reader who takes the band as a
statement about the curve is therefore overstating the coverage by $21$ percentage
points.

---

## ★★4 — The impossible lower edge

$$
\text{mean} - 2\,\text{s.d.} = 0.9246 - 2(0.6082) = 0.9246 - 1.2164
= -0.2918\ \mathrm{s}.
$$

A two-way travel time cannot be negative. The bar is not conservative; it reports a
value outside the physically admissible set, which is the signature of a symmetric
summary applied to a skewed posterior.

---

## ★★5 — Which interval for the figure

$$
\frac{2.2660}{1.9591} = 1.157 .
$$

For a short caption put the **HPD** interval on the figure and label it
"$95\%$ highest-posterior-density interval": it is the shortest interval carrying
the stated probability, it is well defined for a skewed posterior, and its endpoints
are where the density is equal rather than at fixed tail masses. If instead the
caption needs to state what fraction of the probability lies below and above the
interval — which is often what a risk audience wants — use the equal-tailed interval
and print both tail masses. Either is defensible; what is not is drawing a symmetric
bar.

---

## ★★6 — Bayes factor to probability

$$
B_{10} = 10^{3.86} = 7244,
\qquad
P(M_1\mid d) = \frac{7244}{7245} = 0.999862 .
$$

So the data favour model 1 with posterior probability $99.986\%$ under equal model
priors. A figure showing the two models' bands overlapping at every depth supports
none of this: overlap is a marginal statement at each depth, while the evidence is a
statement about the joint likelihood of twelve picks. **The conclusion a figure
cannot support is "the two models are indistinguishable"; the number that settles it
is the Bayes factor, or an equivalent likelihood-based comparison.**

---

## ★★7 — What the caption must add

1. Which band it is: pointwise or simultaneous.
2. Which interval definition: equal-tailed or HPD, and the coverage probability.
3. What the ensemble is: posterior samples, prior samples or predictive draws — and
   how many.
4. What model produced it: the prior and the likelihood, at least by reference, and
   any component that is *not* included (model discrepancy, unmodelled correlation,
   surrogate error).

Adding only the first two still leaves the reader unable to judge whether the band is
a statement about the data or about our prior.

---

## ★★8 — A five-second figure for a skewed, correlated posterior

- **Panel 1 (left, larger):** the joint posterior as a filled $50\%$ and $95\%$
  contour over the two parameters, on equal axes, with the posterior median marked.
  Contours, not a scatter of $10^5$ points, because the shape of the ridge is the
  message and a scatter buries it.
- **Panel 2 (top right):** the marginal of the first parameter as a filled density
  with the HPD interval marked and its numerical bounds printed.
- **Panel 3 (bottom right):** the marginal of the second parameter, same treatment.
- **Encoding:** a single sequential, perceptually uniform palette for the contour
  levels; no rainbow; axes labelled with units; both axes on the same scale so that
  the correlation is not distorted by the aspect ratio.
- **Caption:** "Posterior from [model]; joint $50\%$ and $95\%$ credible regions and
  marginals; intervals are HPD; $N$ = 50 000 draws with ESS $\ge$ 2000; model
  discrepancy not included."
- **Deliberately omitted:** the full ensemble, the chain traces, the prior, and the
  correlated pairs other than the one shown. The first three are appendix material,
  and the fourth is only meaningful in a pairs plot, which cannot be read in five
  seconds.
