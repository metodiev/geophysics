---
id: 06-08-02
title: "H-K Stacking and Crustal Thickness Estimation"
level: graduate
prereqs: ["06-08-01", "06-02-03"]
tags: [seismology, receiver-functions, h-k-stacking, moho, crustal-thickness]
---

# H-K Stacking and Crustal Thickness Estimation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the three receiver-function arrival times $t_{Ps}$, $t_{PpPs}$ and
   $t_{PpSs+PsPs}$ from the legs each phase travels inside the layer.
2. **Explain** why the multiples are not noise to be removed but the
   measurements that break the $H$–$k$ degeneracy.
3. **Construct** the H-k stacking objective, including the sign of the third
   term, and evaluate it on a grid.
4. **Read** the trade-off surface as a ridge, not a point, and extract the
   admitted range of $H$ from a stated threshold.
5. **Estimate** the uncertainty in $H$ from repeated noisy realisations and
   state what limits it.
6. **State** the assumptions on which the method depends, and how each one
   biases the answer.

## Prerequisites

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md) —
  the delay time, the ray parameter and the deconvolution.
- [06-02-03 Tau-p and the Radon Transform](../02-ray-theory-and-travel-times/03-tau-p.md) —
  slowness-domain thinking.

## 1. Intuition: one number is not enough, so collect three

The previous lesson left a hard fact: a single Ps delay cannot give both the
crustal thickness $H$ and the ratio $k=v_p/v_s$. But the receiver function
contains more than one Ps arrival. Besides the direct conversion, the layer
traps energy that bounces between the surface and the Moho before escaping.
These **multiples** arrive at different times, and — crucially — their times
depend on $H$ and $k$ in *different combinations*.

The analogy is surveying with three independent measurements instead of one.
Each measurement alone leaves a curve of possibilities; the curves cross at a
point. H-k stacking is the systematic exploitation of that crossing: predict the
three times for every candidate $(H,k)$, look up the receiver-function amplitude
at those predicted times, and score how well the triplet fits. The best score
wins.

## 2. Precise definitions

For a single layer of thickness $H$ over a half-space, with vertical slownesses
$q_p$ and $q_s$ at ray parameter $p$, and $k=v_p/v_s$:

$$q_p = \sqrt{v_p^{-2}-p^{2}}, \qquad q_s=\sqrt{v_s^{-2}-p^{2}}
= \sqrt{k^{2}v_p^{-2}-p^{2}}.$$

The three delays relative to the direct P arrival are

$$
t_{Ps} = H\left(q_s-q_p\right), \qquad
t_{PpPs} = H\left(q_s+q_p\right), \qquad
t_{PpSs+PsPs} = 2H\,q_s .
$$

Notice the structural relation: $t_{PpPs}=t_{Ps}+2Hq_p$ and
$t_{PpSs}=t_{Ps}+t_{PpPs}$. The three times are not independent, but they depend
on $(H,k)$ differently, which is all that matters.

## 3. Derivations

### 3.1 Leg counting: where the three times come from

Every leg inside the layer costs either $H q_p$ (a P leg) or $H q_s$ (an S leg),
because $q$ is the vertical slowness — the travel time per unit depth at that
angle. The reference is the direct P that traverses the layer down and up as P,
of duration $2Hq_p$. Each multiple is built from the same interface and the free
surface.

| Phase | P legs | S legs | total time | time relative to $2Hq_p$ |
|---|---|---|---|---|
| P (reference) | 2 | 0 | $2Hq_p$ | $0$ |
| Ps | 1 | 1 | $Hq_p+Hq_s$ | $H(q_s-q_p)$ |
| PpPs | 3 | 1 | $3Hq_p+Hq_s$ | $H(q_s+q_p)$ |
| PpSs + PsPs | 2 | 2 | $2Hq_p+2Hq_s$ | $2Hq_s$ |

The three results follow directly.

*Numerical check (SYNTHETIC).* With $H=30.0\ \mathrm{km}$,
$v_p=6.30\ \mathrm{km\,s^{-1}}$, $k=1.726$ ($v_s=3.650\ \mathrm{km\,s^{-1}}$)
and $p=0.030\ \mathrm{s\,km^{-1}}$:

$$q_p = \sqrt{0.025194-0.000900}=0.155944,$$
$$q_s = \sqrt{0.075061-0.000900}=0.272305,$$
$$t_{Ps}=30(0.272305-0.155944)=3.491\ \mathrm{s},$$
$$t_{PpPs}=30(0.272305+0.155944)=12.847\ \mathrm{s},$$
$$t_{PpSs}=2(30)(0.272305)=16.338\ \mathrm{s}.$$

The demonstration reports $3.494$, $12.846$ and $16.339\ \mathrm{s}$ at
$p=0.030$; the small differences are rounding in the hand arithmetic.

### 3.2 Moveout of each phase — and why it matters

Differentiating with respect to $p^{2}$:

$$\frac{\partial t_{Ps}}{\partial p^{2}}
= -\frac{H}{2}\left(\frac{1}{q_s}-\frac{1}{q_p}\right),$$

$$\frac{\partial t_{PpPs}}{\partial p^{2}}
= -\frac{H}{2}\left(\frac{1}{q_s}+\frac{1}{q_p}\right), \qquad
\frac{\partial t_{PpSs}}{\partial p^{2}} = -H\frac{1}{q_s}.$$

Because $q_s<q_p$ for $v_s<v_p$, the first expression is **positive** and the
others are **negative**. This is the diagnostic promised in lesson 01: the
primary conversion moves one way with slowness and the multiples move the other.
The demonstration measures $+45.7$, $-160.2$ and $-114.5\ \mathrm{s}$ per
$(\mathrm{s\,km^{-1}})^{2}$.

### 3.3 The H-k stacking objective

Let $A(t,p)$ be the receiver function (amplitude versus delay time) at ray
parameter $p$. Define the stacked score

$$s(H,k) = \sum_{i=1}^{N_p}\Big[
w_1 A\big(t_{Ps}(H,k,p_i),p_i\big)
+ w_2 A\big(t_{PpPs}(H,k,p_i),p_i\big)
- w_3 A\big(t_{PpSs}(H,k,p_i),p_i\big)\Big].$$

The weights $(w_1,w_2,w_3)$ trade the reliability of the three phases;
the demonstration uses $(0.7,0.2,0.1)$ as a CHOSEN, stated set. The **minus sign
on the third term** is required by the polarity of PpSs conversions, which
arrive with opposite sign to Ps under the standard normalisation. The best
$(H,k)$ maximises $s$.

### 3.4 Resolution: the surface is a ridge

Two mechanisms widen the solution. First, the trade-off of lesson 01 survives in
modified form: for fixed $H$ there is a $k$ that keeps $t_{Ps}$ right, and the
multiples only *partially* remove the degeneracy. Second, the finite bandwidth of
the receiver function means each amplitude sample is a pulse of finite width, so
times within roughly one pulse width are indistinguishable.

The right way to report H-k results is therefore not a single number. It is the
best point **plus the set of models that fit comparably well**. The demonstration
computes that set as all grid cells with $s \ge 0.95\,s_{\max}$.

*Numerical check.* On a $45\times27$ grid ($1215$ cells), the noise-free maximum
is at $H=30.00\ \mathrm{km}$, $k=1.730$ against a true $(30.00,1.726)$. The 95%
set contains $15$ cells: $H\in[29.25,30.75]$ (span $1.50\ \mathrm{km}$),
$k\in[1.700,1.750]$ (span $0.050$). Along the trade-off ridge, $H=27\ \mathrm{km}$
is best fitted by $k=1.810$ at $85.8\%$ of the peak, and $H=31\ \mathrm{km}$ by
$k=1.700$ at $93.8\%$ — a 1 km change in $H$ is traded against a 0.03 change in
$k$ for a small change in score.

### 3.5 Why the multiples break the degeneracy, algebraically

Write the two constraints as functions of the two unknowns. The Ps constraint
gives a curve $k_{Ps}(H)$; the PpPs constraint gives a second curve. Expanding
$t_{Ps}$ and $t_{PpPs}$ for small $p$ (which is adequate to see the structure):

$$t_{Ps} \approx H\left(\frac{1}{v_s}-\frac{1}{v_p}\right)
- \frac{Hp^{2}}{2}(v_s-v_p),$$

$$t_{PpPs} \approx H\left(\frac{1}{v_s}+\frac{1}{v_p}\right)
- \frac{Hp^{2}}{2}(v_s+v_p).$$

The leading coefficients differ: $t_{Ps}$ measures the *difference* of the
reciprocal speeds, $t_{PpPs}$ their *sum*. Suppose a trial $(H',k')$ reproduces
$t_{Ps}$ but errs on $H$. Then the sum term moves in a direction that cannot be
cancelled by the same error, because the ratio of the two coefficients is not
one for any $v_s \ne 0$. That mismatch is exactly the extra information. The
PpSs term adds a third combination, $2H/v_s$, which is sensitive to $v_s$ alone.
Three measurements, three independent combinations — but only if the data
actually resolve the three arrival times, which brings back the bandwidth caveat.

A quantitative measure of "how much the multiples help" is the *conditioning* of
the map $(H,k)\mapsto(t_{Ps},t_{PpPs},t_{PpSs})$. Its Jacobian is

$$J = \begin{pmatrix}
q_s-q_p & H\,\dfrac{k}{v_p^{2}q_s}\\[2mm]
q_s+q_p & H\,\dfrac{k}{v_p^{2}q_s}\\[2mm]
2q_s & 2H\,\dfrac{k}{v_p^{2}q_s}
\end{pmatrix},$$

where the first column is $\partial t_i/\partial H$ and the second is
$\partial t_i/\partial k$. If only the first row is used, $J$ has rank one and
the two unknowns cannot be separated. Adding the second row makes the rank two,
and the third row makes the system overdetermined — one more reason to include
PpSs even though its weight is small.

### 3.6 Choosing the weights

The weights are not free parameters of the physics; they are a statement about
relative reliability. A defensible choice has three ingredients:

1. **Noise level per phase.** Later arrivals sit in a noisier part of the
   receiver function, where source coda and deeper structure dominate. Smaller
   weight for later phases follows.
2. **Polarity and amplitude.** PpSs has opposite polarity and, for a given
   contrast, a different amplitude; the negative sign is mandatory and the
   magnitude should be checked on synthetic data for the velocity range of
   interest.
3. **Sensitivity of the score to the weights.** Run the stack for several weight
   sets and report whether the best $(H,k)$ moves. If it does, the result is
   weight-dependent and must be said so. The demonstration's $(0.7,0.2,0.1)$ set
   is a **stated** choice, not a universal recommendation.

## 4. Physical interpretation

- The multiples are *internal resonances of the crust*. Their delay times grow
  with both $H$ and $v_s$, while $t_{Ps}$ grows with $H$ and the *difference*
  $v_s - v_p$. The differing dependence is the information.
- Because the multiples arrive late ($12$–$18\ \mathrm{s}$ in the demonstration),
  they are the part of the receiver function most easily contaminated by
  deeper structure and by other multiples. That is why their weights are small.
- A ridge in the surface is not a failure of the method; it is an honest
  statement that the data constrain one combination of $H$ and $k$ much better
  than the other. Reporting the ridge is more informative than reporting its
  highest point.

### 4.1 What the ridge means in practice

Suppose a regional study reports "Moho depth $32\ \mathrm{km}$" from H-k
stacking. The defensible statement is narrower: "the receiver functions admit
$H\in[29.3,30.8]\ \mathrm{km}$ at 95% confidence for the assumed single-layer
model, with $k$ free." If a colleague then quotes the depth in a comparison with
a refraction profile, the comparison is only meaningful if both estimates carry
their admitted ranges and both adopt comparable velocity assumptions. A
$1.5\ \mathrm{km}$ range is small compared with the real variation of crustal
thickness across a continent, so H-k stacking is genuinely useful — but it is not
a point measurement, and treating it as one overstates what the data support.

There is also a subtle coupling to the *forward model*. A deeper Moho in a
region of high $v_p$ and a shallower Moho in a region of low $v_p$ can produce
near-identical receiver functions. Since $v_p$ is usually assumed from a
regional model rather than measured at the station, the resulting map inherits
the assumed model's errors. The honest framing of a crustal-thickness map is
"Moho depth under the assumed $v_p$ model", and a sensitivity test in which
$v_p$ is varied by a stated amount should accompany it.

## 5. Assumptions

1. A **single** layer over a half-space. Real crust has internal contrasts, and
   a strong mid-crustal converter produces its own multiples that can be
   mistaken for Moho multiples.
2. Horizontal, isotropic layering. Dip and anisotropy shift and rotate the
   azimuthal pattern.
3. The correct polarity convention is used when summing the third term.
4. The ray parameter of each receiver function is known well enough; the
   moveout is evaluated with it.
5. The amplitude of the receiver function is preserved (not arbitrarily scaled
   between events) if the weights are to mean anything.

### 5.1 Sensitivity of the answer to the weight set

Because the weights are a stated choice, the result must be tested against them.
A cheap and convincing test is to rerun the grid search for three weight sets —
for example $(0.8,0.2,0.1)$, $(0.7,0.2,0.1)$ and $(0.5,0.3,0.2)$ — and report
whether the best $(H,k)$ moves by more than the 95% set width. If it does, the
conclusion is weight-dependent and the paper must say so. If it does not, the
ridge is robust to the weighting, and the admitted range from Section 3.4 can be
quoted with more confidence. This single test distinguishes a result from an
artefact of one's own choices, and it costs only a few minutes of computation.

## 6. Units and dimensional analysis

| Quantity | Unit | Note |
|---|---|---|
| $H$ | km | depth/thickness |
| $v_p, v_s$ | $\mathrm{km\,s^{-1}}$ | |
| $p$ | $\mathrm{s\,km^{-1}}$ | ray parameter |
| $q_p, q_s$ | $\mathrm{s\,km^{-1}}$ | $\sqrt{\mathrm{s^2\,km^{-2}}}$ |
| $t_i$ | s | $\mathrm{km}\times\mathrm{s\,km^{-1}}$ |
| $k$ | dimensionless | $v_p/v_s$ |
| $A$ | same unit as the RF | arbitrary; weights dimensionless |

The score $s$ has the units of the receiver function. Only its *shape* in
$(H,k)$ is interpreted.

## 7. Worked examples

### Example 1 — predict the triplet

For $H=25\ \mathrm{km}$, $v_p=6.0\ \mathrm{km\,s^{-1}}$, $k=1.80$
($v_s=3.333$), $p=0.05\ \mathrm{s\,km^{-1}}$:

$$q_p=\sqrt{0.027778-0.0025}=0.159036,\quad
q_s=\sqrt{0.090000-0.0025}=0.295804,$$
$$t_{Ps}=25(0.136768)=3.419\ \mathrm{s},$$
$$t_{PpPs}=25(0.454840)=11.371\ \mathrm{s},\quad
t_{PpSs}=2(25)(0.295804)=14.790\ \mathrm{s}.$$

### Example 2 — how far apart are competing models?

Using the ridge from the demonstration, two models $(H,k) = (30,1.730)$ and
$(32,1.680)$ score $9.708$ and $8.445$. The ratio is $0.870$, i.e. the second is
$13\%$ lower. For a stack of many receiver functions the log-likelihood
difference matters; with a single trace, a $13\%$ score difference is rarely
decisive. **Report both.**

### Example 3 — a two-cell hand search

Take a $2\times2$ grid around the demonstration's answer:
$(H,k) \in \{29.75,30.00\}\times\{1.725,1.730\}$. The synthetic field has
Gaussian pulses of half-width $\approx 0.20$–$0.30\ \mathrm{s}$. The delay
$t_{Ps}(H,k)$ changes between adjacent cells by

$$\Delta t_{Ps} \approx \frac{\partial t_{Ps}}{\partial H}\,\Delta H
= (q_s-q_p)(0.25\ \mathrm{km}) = 0.124 \times 0.25
= 0.031\ \mathrm{s},$$

which is far smaller than the pulse width. Every cell in this block therefore
attracts nearly the same score, which is why the 95% set is a contiguous
blob rather than an isolated cell. The practical rule: **the grid spacing should
be finer than the resolution, not finer than the data.** Reporting an answer to
$0.01\ \mathrm{km}$ when the pulse width corresponds to $\sim 1.5\ \mathrm{km}$
is false precision.

### Example 4 — uncertainty from repeated noisy realisations

The demonstration adds noise at $16\%$ of the field rms and repeats the whole
stack 60 times. It recovers $H = 30.02 \pm 0.14\ \mathrm{km}$ and
$k = 1.727 \pm 0.005$, against a truth of $(30.00, 1.726)$. The bias is
$+0.02\ \mathrm{km}$ on $H$; the scatter ($0.14\ \mathrm{km}$) is much smaller
than the 95% set width ($1.50\ \mathrm{km}$). At this noise level the **ridge
limits the answer, not the noise** — a distinction that a single stack cannot
reveal.

## 8. Python demonstration

`code/hk_stacking_demo.py`:

1. builds $t_{Ps}$, $t_{PpPs}$, $t_{PpSs}$ for the true model and tabulates
   their moveout;
2. synthesises a receiver-function field as Gaussians at those times, with
   amplitudes that vary with $p$;
3. grid-searches $H\in[25,36]\ \mathrm{km}$ and $k\in[1.60,1.86]$ and reports the
   maximum against the truth;
4. measures the 95% set and prints the trade-off ridge;
5. repeats the entire stack over 60 noise realisations and reports the mean and
   standard deviation of $H$ and $k$.

The demo prints the grid size ($1215$ cells), the peak score, the median of the
surface, and the admitted ranges, so every number quoted above can be
reproduced.

## 9. Exercises

Full sets are in
[`exercises/02-h-k-stacking-exercises.md`](./exercises/02-h-k-stacking-exercises.md)
and
[`exercises/02-h-k-stacking-solutions.md`](./exercises/02-h-k-stacking-solutions.md).

- **★** Compute the triplet for $H=35$ km, $k=1.70$, $p=0.06\ \mathrm{s\,km^{-1}}$
  with $v_p=6.2\ \mathrm{km\,s^{-1}}$.
- **★★** Derive $\partial t_{PpPs}/\partial p^{2}$ and confirm its sign.
- **★★** Explain why the third weight is negative, and what error appears if it
  is taken positive.
- **★★★** The 95% set spans 1.5 km in $H$. Propose and compute an experiment
  that narrows it, and state the cost.

## 10. Common mistakes

1. **Reporting the grid maximum as "the" thickness.** The grid spacing bounds
   the answer; report the admitted set.
2. **Using the wrong polarity for the third term.** Summing PpSs with a positive
   weight biases $H$ and $k$ in a coupled way.
3. **Assuming the multiples are Moho multiples.** A strong mid-crustal converter
   produces similar-looking multiples at different times.
4. **Ignoring the ray-parameter distribution.** A narrow $p$ range weakens the
   moveout discrimination and broadens the ridge.
5. **Comparing scores across different normalisations.** If each receiver
   function is normalised independently, the total score's absolute value is not
   comparable between data sets.
6. **Ignoring the grid's resolution.** A grid finer than the pulse width produces
   a smooth, tempting maximum with many nearly equal neighbours; a grid coarser
   than the pulse width can miss the maximum entirely. Report the step and the
   admitted set together.

## 11. Real-world applications

- **Continental crustal-thickness maps.** H-k stacking of large temporary arrays
  (USArray and its successors) produced the community reference maps of Moho
  depth.
- **Reservoir and basin studies.** The same method gives depth to a shallow
  basement or a strong intra-sedimentary contrast, with the caveat of poorer
  separation of the multiples.
- **Planetary seismology.** Single-station H-k logic is applied to Mars and Moon
  data, where arrays do not exist; the ridge is correspondingly more important
  to report.
- **Instrument and network design.** The value of a station for crustal studies
  depends on its back-azimuthal and distance coverage, which controls the
  slowness range available for stacking.
- **Teaching the difference between detection and resolution.** H-k stacking is
  a clean example of a method that *detects* a Moho robustly (the peak is
  unmistakable) while *resolving* its depth only within a ridge. Forced analogy
  with thin-bed seismic detection in
  [06-09-07 Seismic Attributes and Quantitative Interpretation](../09-reflection-seismology/07-seismic-attributes.md)
  is deliberate: the same distinction recurs throughout geophysics and is the
  subject of
  [05-01-03 The Resolution–Depth Trade-off](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md).

## 12. Further reading

- **Zhu, L., & Kanamori, H. (2000). Moho depth variation in southern California
  from teleseismic receiver functions. *Journal of Geophysical Research*,
  105(B2), 2969–2980.** Level: research. The paper that defined the three-phase
  stacking used here.
- **Ammon, C. J., Randall, G. E., & Zandt, G. (1990). On the non-uniqueness of
  receiver function inversions. *Journal of Geophysical Research*, 95(B10),
  15303–15315.** Level: research. The trade-off studied in this lesson.
- **ObsPy TauP documentation.** <https://docs.obspy.org/packages/obspy.taup.html> —
  Level: reference. Computing ray parameters and travel times offline.
- **FDSN web services specification.** <https://www.fdsn.org/webservices/> —
  Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md) —
  where the trade-off is derived.
- [03 Moho Discontinuity Depth and Sharpness](03-moho-interface.md) — what the
  amplitudes add.
- [05 Joint Inversion of Receiver Functions and Surface Waves](05-joint-inversion-rf.md) —
  the alternative that breaks the trade-off with an independent measurement.
- [06-09-03 Velocity Analysis and Moveout Interpretation](../09-reflection-seismology/03-velocity-analysis.md) —
  the same moveout-as-information idea in exploration seismology.

## 14. Self-assessment checklist

- [ ] I can derive all three delays by leg counting.
- [ ] I can explain why the multiple moveout has the opposite sign.
- [ ] I can build the stacking objective and state why the third term is negative.
- [ ] I can extract a 95% admitted set from a grid search.
- [ ] I can distinguish resolution-limited from noise-limited uncertainty.
- [ ] I can list three assumptions and the bias each one causes if violated.
