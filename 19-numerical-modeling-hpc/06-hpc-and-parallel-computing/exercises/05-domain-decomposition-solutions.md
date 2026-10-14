# Solutions — 19-06-05 Domain Decomposition and Load Balancing

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs.

Lesson: [05 Domain Decomposition and Load Balancing](../05-domain-decomposition.md).

---

## ★1 — Halo fractions

- **$16$ bands** on a $1024\times1024$ grid: band height $b = 1024/16 = 64$, width
  $n = 1024$, halo fraction $2n/(nb) = 2/64 = 3.125\%$.
- **$4\times4$ blocks**: block side $s = 1024/4 = 256$, halo fraction
  $4s/s^{2} = 4/256 = 1.5625\%$.

The block layout halves the halo fraction at $16$ ranks — the surface-to-volume
advantage — and pays for it with diagonal neighbours in the communication graph.

---

## ★2 — The two bounds

- **Static contiguous blocks:** the makespan is at least the largest block's work,
  because a rank cannot finish before it has done its own work and cannot help
  another rank.
- **Dynamic work queue:** the makespan is at least the largest *single item's*
  work, because items are indivisible; with fine-enough items this bound
  approaches the ideal.

---

## ★3 — The cost range

With $v \in [1.200, 2.800]$, the cost $1/v$ ranges over
$[1/2.800, 1/1.200] = [0.3571, 0.8333]$. The ratio of the cost extremes is
$0.8333/0.3571 = 2.333$, the same as $v_{\max}/v_{\min} = 2.800/1.200 = 2.333$,
because $1/v$ is monotone and the extremes swap ends rather than changing
magnitude.

---

## ★4 — The imbalance and its penalty

Mean $= (51.6 + 51.52 + 88.16 + 87.99)/4 = 279.27/4 = 69.82$. Maximum $= 88.16$.

$$\max/\text{mean} = \frac{88.16}{69.82} = 1.263,$$

and since the makespan is proportional to the maximum, the largest rank runs
$26.3\%$ longer than a perfectly balanced rank would — the penalty is the same
$26.3\%$, because the ideal makespan is the mean by definition of the total work
divided by the number of ranks.

---

## ★5 — Why the balanced partition has unequal counts

The work per column is not proportional to its width: columns where $v$ is small
cost more. The greedy balancer therefore assigns **more columns** to ranks whose
columns are cheap and **fewer** to ranks containing the slow patch, equalising
work at the price of unequal cell counts: $[157, 154, 95, 106]$.

The cost is real and must be paid:

- the partition is no longer a uniform band, so a code that assumed
  $\text{rows} = N/p$ must be generalised to variable extents;
- moving from one decomposition to another requires data motion (a repartition),
  whose cost must be less than the imbalance removed;
- a variable-extent decomposition complicates the neighbour logic and any
  indexing arithmetic that was previously uniform.

---

## ★6 — Where Amdahl efficiency crosses $50\%$

$$S(p) = \frac{1}{f + (1-f)/p}, \qquad \frac{S}{p} = \frac{1}{pf + (1-f)}
= 0.5 \;\Rightarrow\; pf + 1 - f = 2 .$$

$$\Rightarrow p = \frac{1 + f}{f} = \frac{1.0551}{0.0551} = 19.15 .$$

So the efficiency passes below $50\%$ between $p = 19$ and $p = 20$; at
$p = 32$ it is $1/(32(0.0551) + 0.9449) = 1/2.708 = 36.9\%$ and the ceiling
speedup is $11.8\times$ against an ideal $32\times$.

---

## ★7 — Removing the granularity bound

The bound in the lesson's Section 8 came from item granularity: four columns,
one per rank, so the largest single weight ($0.83$) is the floor for the
makespan. Refining the decomposition means splitting each column into several
sub-domains that can be assigned independently — in $2$-D, splitting the slow
patch into $2\times2$ tiles instead of leaving it as two whole bands.

**Cost:** the halo fraction rises. A band split into two halves has twice the
internal boundary, so the halo fraction doubles if the split is along the halo
direction; if it is along the non-halo direction (splitting in $y$ while halos
are in $z$) the halo count also doubles because the two sub-domains each need
their own neighbour rows. The messages per rank roughly double, so at
$\alpha = 5\ \mu\mathrm{s}$ the communication cost per swing rises from about
$10\ \mu\mathrm{s}$ to about $20\ \mu\mathrm{s}$ — which is small only if the
sub-domain's compute time is large compared with that.

The trade is therefore: granularity improvement versus halo and message growth,
and it is decided by numbers of exactly the kind tabulated in the lesson.

---

## ★8 — Why the measured ratio exceeds the prediction

Measured $1.336$, predicted $1.256$; the gap is $6.4\%$ of the prediction. Two
effects:

1. **The balanced run has more total work per rank.** The emulation's unit counts
   are the weights rounded up with `max(1, ...)`, so the balanced partition's
   four ranks are not exactly equal in *executed* units; this inflates the
   denominator's time.
2. **Thread scheduling noise in the emulation.** Four threads sharing a machine
   with other work are subject to the operating system's scheduling, and the
   makespan of a $13$–$18$ ms run is sensitive to it.

Effect 2 is the artefact of the emulation: real MPI ranks on dedicated cores do
not have it, and a network adds effects the emulation lacks entirely. Effect 1 is
a property of the demo's tuning and would be absent in a solver whose work per
rank is exactly proportional to its weights. The honest statement is that the
prediction is an arithmetic bound on the ratio and the emulation lands $6\%$ above
it, which is the accuracy an in-process emulation can be trusted to.
