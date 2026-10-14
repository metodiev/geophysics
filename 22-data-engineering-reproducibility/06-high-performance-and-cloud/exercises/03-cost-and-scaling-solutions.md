# Solutions — 22-06-03 Cost, Scaling and Practical Efficiency

> Read after attempting. Numbers use the lesson's SYNTHETIC teaching rates
> (0.05 per core-hour, 20 per TB-month, 90 per TB egress). Lesson:
> [03 Cost, Scaling and Practical Efficiency](../03-cost-and-scaling.md).

---

## ★1 — The three terms

$$C_{\text{compute}} = n\,T(n)\,c_h, \qquad
C_{\text{storage}} = V_{\text{stored}}\,m\,c_s, \qquad
C_{\text{egress}} = V_{\text{out}}\,c_e.$$

Compute is proportional to **core-hours consumed** (cores × wall time); storage to
**volume-months kept** (volume × months of retention); egress to the **volume transferred
out** per pass. The asymmetry that matters: compute is consumed once, storage is billed
for as long as the data exists, and egress is charged again on every pass over the data.

## ★2 — 128 cores, 6 hours, 1 TB for 18 months

(a) compute $= 128 \times 6 \times 0.05 = 38.4$; storage $= 1 \times 18 \times 20 = 360.0$;
egress $= 1 \times 90 = 90.0$; total $= 488.4$ units.

(b) storage + egress $= 450.0$, so $450.0/488.4 = 92.1\ \%$.

(c) The retention decision. Halving the retention to nine months saves
$1 \times 9 \times 20 = 180$ units, which is the largest single saving available; halving
the cores would save nothing if the deadline then slipped, and deleting the egress pass
would require co-locating compute and data. Note that if the data is re-downloadable, the
honest alternative is to keep the identifier and the recipe rather than the bytes.

## ★3 — Rising cost per unit of work

The cost per unit of work is (cost of the whole run) / (units of work). Under weak scaling
the *work per core* is held constant, so a perfectly efficient run has constant cost per
unit. Real runs do not, because at larger core counts: (i) **communication** and
synchronisation grow with the number of participants; (ii) **load imbalance** grows — the
slowest rank sets the wall time; and additionally (iii) **I/O contention** on a shared
filesystem grows and can become the serial bottleneck. All of these increase core-hours
for the same work, hence a rising cost per unit.

## ★★4 — 300 TB per year, kept five years

(a) A cohort of raw data is kept for 5 years, the next for 4, … so the total is
$300 \times (5+4+3+2+1) = 4\,500$ TB-months, at 20 units each $= 90\,000$ units over five
years, i.e. 18 000 units per year in steady state ($300 \times 5 \times 20 = 30\,000$ for
the five-year cohorts alone; the arithmetic above is the five-year total).

(b) Keeping one year: at steady state $300 \times 1 \times 20 = 6\,000$ units per year of
raw storage, plus $10 \times 2 \times 20 = 400$ units per year for two years of derived
products $= 6\,400$ units per year, against 18 000 — a saving of 11 600 units per year
(64 %).

(c) The risk is that a later analysis needs a **different reduction** of the raw data, or
needs to re-verify a published result, and the raw data no longer exists — the
irreversibility warning of
[22-03-05](../../03-data-formats-and-engineering/05-data-quality-control.md) §8. Mitigations:
keep the raw data where the provider still has it and record the exact version identifier
and access recipe; keep a cheap, lossless subset (e.g. a decimated but uninterpreted
archive) with a documented decimation; and make the deletion a recorded decision
([22-05-04](../../05-collaboration-and-project-management/04-research-data-management-plan.md)).

## ★★5 — 10 hours at 128 cores, $p = 0.06$

(a) $T(n) = 10 \times (0.06 + 0.94 \times 128/n)$.

- $n = 128$: $T = 10 \times 1.0 = 10.00$ h; cost $= 128 \times 10 \times 0.05 = 64.0$.
- $n = 512$: $T = 10 \times (0.06 + 0.235) = 2.95$ h; cost $= 512 \times 2.95 \times 0.05 = 75.5$.
- $n = 2\,048$: $T = 10 \times (0.06 + 0.05875) = 1.19$ h; cost $= 2\,048 \times 1.19 \times 0.05 = 121.6$.

Core-hours rise from 1 280 to 1 510 to 2 432; the last doubling buys 0.68 h for 46.1 units.

(b) Need $T \le 4$: try $n = 256$: $T = 10 \times (0.06 + 0.47) = 5.30$ h (no);
$n = 512$: 2.95 h (yes). So **512 cores**, cost 75.5 units, using 1 510 core-hours.

(c) The serial floor is $10 \times 0.06 = 0.60$ h, so a 30-minute deadline is **not
reachable at any core count**; changing the deadline, the algorithm or the serial part is
the only route.

## ★★6 — A 1 000-unit bill

(a) compute $= 350$, raw storage $= 250$, derived storage $= 100$, egress $= 200$,
recomputation $= 100$ units.

(b) Compute becomes $350 \times 0.70 = 245$, so the bill is
$245 + 250 + 100 + 200 + 100 = 895$ units: a saving of 105 units, **10.5 %**.

(c) Derived-product storage halves ($100 \to 50$) and recomputation halves
($100 \to 50$): the bill becomes $350 + 250 + 50 + 200 + 50 = 900$ units, a saving of 100
units, **10.0 %**. The two interventions are comparable in size, and that is the lesson:
a 30 % solver speed-up buys about the same as deleting half the regenerable intermediates
and half the reruns — while the solver change needed a code effort and the housekeeping did
not. Note the implied decomposition of recomputation: the failure line is charged at the
full unit cost of the work, so halving the *failure rate* and halving the *retry cost* are
interchangeable.

## ★★★7 — A 10 000-realisations forecast

**Work units.** 10 000 realisations, 3 core-hours each, 40 GB each.

1. **Compute.** $10\,000 \times 3 \times 0.05 = 1\,500$ units, plus a setup/merge stage —
   assume 100 units — so 1 600 units.
2. **Raw/input storage.** Assume inputs are shared and stored once: state the volume and
   retention explicitly (say 500 TB for one year $= 500 \times 12 \times 20 = 120\,000$
   units) — this is where the honest answer usually shows the model was never about the
   realisations.
3. **Derived storage.** $10\,000 \times 40\ \text{GB} = 400$ TB, kept 24 months
   $= 400 \times 24 \times 20 = 192\,000$ units. For the *result* set alone, that is the
   dominant term by two orders of magnitude over the compute.
4. **Movement.** One pass of the 400 TB out of the compute region $= 36\,000$ units; each
   additional pass adds the same.
5. **Failure line.** 5 % failure with one retry $= 0.05 \times 1\,600 \times 2 \approx 160$
   units of compute — small for compute, but the recomputation also re-writes the derived
   volume it had already produced, so the storage and movement lines are effectively paid
   once more: $0.05 \times 192\,000 \approx 9\,600$ units.

**Dominant term**: derived-product storage (192 000 units), then input storage. The
compute is under 1 % of the total — the numbers make this blatant.

**First measurement**: the per-realisations output *size*, and whether the full-precision
volume is needed at publication time or can be reduced once and stored in the reduced form
only. That single decision moves the largest line.

## ★★★8 — Measuring a real cost per unit of work

**Per-run record.** Timestamp and project/account tag; core or instance count and wall
time (hence core-hours); the machine or instance type and its rate at the time; input
volume read and the storage tier it came from; output volume written; bytes transferred
in and out with the destination; peak and total memory (for right-sizing); exit status and
whether the run was retried; and the run's work-unit count (realisations, events, tiles)
so the denominator is honest. Record the identifier of the code version and container so
the run can be attributed to a result.

**Attributing shared infrastructure.** Allocate shared filesystem, licences, database
instances and staff time by a stated rule — usage-based where possible (bytes stored per
month, licence seats), equally divided otherwise, with the rule written down. Report
"direct" and "allocated" numbers separately; the direct number is the one that changes
when the code changes, and the allocated number is the one the finance office uses.

**Three naive uses that mislead.**

1. **Comparing cost per unit across projects** — the work units are not comparable
   (one "realisation" is not another's "tile"), so the ratio is meaningless.
2. **Treating storage as a one-off** — it recurs monthly and appears small per run; a
   project that looks cheap per run can be dominated by data it never deletes.
3. **Ignoring retries and failed runs** — if failed runs are excluded from the record,
   the measured cost per unit is a lower bound, and precisely the failures the forecast
   needs to price are invisible.

## ★★★9 — "Double the cores, halve the deadline"

**When it is right.** In the low-$n$ regime where efficiency is still high: the
demonstration's table halves 12.0 h to 3.45 h going from 64 to 256 cores (a 3.5× speedup
for 4× the cores), so for a *doubling* of cores in that regime the wall time does fall
nearly by half — the first halving is roughly attainable.

**When the floor forbids it.** Once $T(n)$ approaches $T_{64}\,p$, each doubling yields
less, and below the floor no core count reaches the deadline. At $p = 0.05$ the floor is
0.60 h; a 0.5-hour deadline is infeasible for any $n$ (Table 3).

**Marginal cost of the last halving.** Core-hours: 768 (12 h) → 883 (6 h) → 1 037 (3 h) →
1 344 (1.5 h). The increments are +115, +154, +307 — the third halving costs twice the
second. So "just double again" is a request to buy the most expensive increment yet.

**Evidence required before approving the spend.** The measured wall time at a *pilot*
problem size across several core counts (at least the current and proposed counts, each
repeated); the per-instance activity showing the work actually distributes; the estimated
serial fraction with its measurement size stated; the forecast cost of the new run against
the current one; and the checkpoint/restart plan, since a shorter deadline is worthless if
the run restarts from scratch.

**The non-cost reason a shorter deadline can still be worth it.** A deadline that fits
inside a maintenance window, a conference or a field campaign turns an experiment that
could not be run into one that can; the second-order effect is that faster loops mean more
model variants tested per unit of researcher time, which is often the real constraint. The
decision is then "is the extra cost smaller than the value of the additional iterations?",
which is a scientific question, not a cost-model one.
