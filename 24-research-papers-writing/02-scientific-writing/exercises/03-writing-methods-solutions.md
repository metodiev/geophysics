# Solutions — 24-02-03 Writing Methods Sections That Can Be Reproduced

> Read after attempting. Numbers computed. Lesson:
> [03 Writing Methods](../03-writing-methods.md).

---

## ★1 — Elevation correction at $+10\%$

$$d = (0, 0, 0, 0, 0, 0.10), \qquad
\sum_i e_i d_i = 0.60 \times 0.10 = 0.060,$$
$$y = 100\exp(0.060) = 100 \times 1.06184 = 106.18,$$

a change of $+6.18\%$ — the largest of the six parameters at this deviation, and
the value printed in the lesson's sensitivity table.

---

## ★2 — Taper length at $+50\%$

$$d = (0, 0.50, 0, 0, 0, 0), \qquad
\sum_i e_i d_i = 0.45 \times 0.50 = 0.225,$$
$$y = 100\exp(0.225) = 100 \times 1.25232 = 125.23,$$

a change of $+25.2\%$. Units: the deviation $d$ is dimensionless (fraction of the
half-range), the elasticity is dimensionless, so $y$ carries the same unit as the
published quantity ($100$ units of whatever is being reported — here per cent of a
reference value).

---

## ★3 — Log-deviation standard deviation for two unknown parameters

$$\operatorname{SD}(S) = \sqrt{\frac{1}{12}\left(0.60^{2} + 0.45^{2}\right)}
= \sqrt{\frac{0.36 + 0.2025}{12}}
= \sqrt{0.046875} = 0.2165 .$$

The $90\%$ interval for the reader's reproduction is
$100\exp(\pm 1.645 \times 0.2165) = 100\exp(\pm 0.3561)$:

$$y \in [70.0,\ 142.8].$$

Two unknown high-elasticity parameters leave a range spanning a factor of $2.04$,
so no tolerance below about $40\%$ could be met.

---

## ★4 — Variance removed by one reported parameter

All free: $\sum e_i^2 = 0.825$. With the elevation correction reported,
$\sum e_i^2 = 0.825 - 0.36 = 0.465$. The variance fraction removed is

$$1 - \frac{0.465}{0.825} = 1 - 0.5636 = 0.4364 \approx 43.6\%.$$

The remaining standard deviation is
$\sqrt{0.465/12} = \sqrt{0.03875} = 0.1969$, so the $90\%$ interval is

$$100\exp(\pm 1.645\times 0.1969) = 100\exp(\pm 0.3239)
\;\Rightarrow\; y \in [72.3,\ 138.2],$$

as printed in the lesson. Reporting the single most influential parameter removes
$43.6\%$ of the inherited variance; reporting the least influential one
(elasticity $0.10$) removes only
$1 - (0.825 - 0.01)/0.825 = 1.2\%$.

---

## ★5 — Is the $5\%$ reproduction claim supported?

Five of six reported leaves the elevation correction free, so

$$\operatorname{SD}(S) = \sqrt{\frac{0.36}{12}} = \sqrt{0.03} = 0.1732,$$

and the $90\%$ interval is

$$100\exp(\pm 1.645\times 0.1732) = 100\exp(\pm 0.2849)
\;\Rightarrow\; y \in [75.2,\ 133.0].$$

The interval spans $+33\%$ and $-25\%$ around the published value, so a claim of
reproduction within $5\%$ is **not supported**: a reader who guesses the unreported
parameter within $\pm 50\%$ of its plausible range will miss the published number
by up to a third. The claim would be supportable if the omitted parameter's
plausible range were at most $\pm 3\%$ of the half-range
($0.05/0.60 \approx 0.083$ of the half-range for the $90\%$ bound at $1.645$), which
is a testable statement about how tightly the parameter is constrained in practice.

---

## ★6 — Word budget for the three most influential decisions

Three decisions at $25$ words each $= 75$ words. Against the mean Methods length of
$1417$ words,

$$\frac{75}{1417} = 5.3\%\ \text{of the section}.$$

Five per cent of the Methods budget buys defensible statements about influence for
the three parameters that together carry $0.36 + 0.2025 + 0.1225 = 0.685$ of the
total $0.825$ — $83\%$ of the parameter-driven variance. This is the argument for
sensitivity statements: they cost a twentieth of the section and they remove most of
the reproduction uncertainty.

---

## ★7 — Sensitivity experiment for a real chain

**Output metric.** Choose one scalar and state it: for example the root-mean-square
misfit of the processed result against a reference, in the same units as the data,
plus a second structural metric (a peak amplitude or a picked onset time). One
metric is not enough: parameters often trade a better fit for a biased feature.

**Parameter set and ranges.** Every parameter you can actually vary, with a range
justified physically or empirically — filters bounded by Nyquist, velocity bounded
by the plausible geology, and taper lengths bounded by the window. Ranges must be
defensible in the paper, because they set the answer.

**Design.** One-parameter-at-a-time is adequate for a first ranking when the chain
is nearly linear over the ranges; for anything else use a variance-based
decomposition (a Sobol' or Morris design) over the joint range. Budget the runs:
one-at-a-time at $10$ values for $6$ parameters is $60$ runs; a Sobol' design for
the same problem needs of order $10^{3}$ runs to separate main effects from
interactions with useful precision.

**The question one-at-a-time cannot answer.** Interaction: whether two parameters
matter only in combination. A velocity step and a damping factor, for example, may
each be harmless while together producing a systematically biased amplitude.
Without a joint design, the paper reports a ranking that holds only along the axes
you happened to sample.

---

## ★8 — How much variability comes from unreported parameters?

**Unit of analysis.** One published result number per paper, paired with a set of
reproduction runs of that paper's own code.

**Outcome.** The fraction of the variance of the reproduced result that is
explained by varying unreported parameters within their documented plausible
ranges, decomposed (variance ratio) against the variance explained by everything
reported. Report the ratio with a bootstrap interval over papers.

**Recovering parameters.** Identify the unreported choices from the code and its
defaults, define the plausible range from documented practice (library defaults,
domain conventions) rather than from taste, and pre-register both the list and the
ranges before running. Without this step the study can always produce the result it
wants by widening a range after the fact.

**Selection bias.** Papers with archived, runnable code and data are a biased
subset: methods papers, well-funded groups, and authors already attentive to
reproducibility. Their unreported-parameter variability is likely *smaller* than the
field's, because they had a rehearsal. The measured fraction is therefore a lower
bound, and the report must present the selection flow — how many papers were
contacted, how many archived anything usable, how many ran — as the primary
evidence about what remains unknown.
