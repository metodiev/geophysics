# Solutions — 22-07-04 Benchmarking, Performance Tracking and Documentation Tests

> Read after attempting. Numbers are computed here with the same closed form and noise model
> as the lesson's SYNTHETIC simulation. Lesson:
> [04 Benchmarking, Performance Tracking and Documentation Tests](../04-benchmarking-and-docs.md).

---

## ★1 — The three quantities

(i) **The effect** to be detected (a percentage change in runtime, memory or operations);
(ii) **the noise** (run-to-run variance of the measurement on that machine);
(iii) **the decision rule** (threshold and number of repeats, with the false-alarm rate and
power they imply). The noise is the one usually left unmeasured — teams record times and
thresholds and never measure the spread the machine produces when nothing changes.

## ★2 — A benchmark with 6 % noise

(a) $n = (2.487 \times 0.06/0.10)^2 = 2.23 \to 3$ repeats.

(b) $n = (2.487 \times 0.06/0.03)^2 = 24.8 \to 25$ repeats.

(c) The repeat count scales with $\sigma^2$: halving the noise quarters both numbers — 3 → 1
(well, $n=1$ suffices for the 10 % effect) and 25 → 7. This is the quantitative reason to pin
a core and take the best of a few runs rather than repeat hundreds of times on a busy
machine.

## ★3 — Documentation examples

**Catches**: (i) a renamed, moved or deleted function used in an example; (ii) a changed
signature (argument order, a new required argument); (iii) a changed default value that the
example prints; (iv) behaviour change on the documented path, if the example asserts on
output.
**Cannot catch**: whether the prose is accurate; whether the parameter description matches
the behaviour; whether the physics is implemented correctly; anything about the 66 % of the
API with no example.

## ★★4 — One measurement per push, 4 % threshold

(a) $P(\text{false alarm}) = P(\mathcal{N}(0, 0.07) > 0.04) = 0.284$. Comparisons
$= 18 \times 230 = 4\,140$, so the expected false alarms are
$4\,140 \times 0.284 \approx 1\,175$ per year — more than three a day.

(b) The median of 9 runs has standard deviation $1.2533\,\sigma/\sqrt{9} = 0.0292$, so
$P(\text{alarm}) = P(\mathcal{N}(0, 0.0292) > 0.04) = 0.086$, giving about
$4\,140 \times 0.086 \approx 355$ alarms a year — a three-fold improvement, still one a day.

(c) Requires **three consecutive comparisons** above the threshold rather than one:
$P = 0.284^3 = 0.0229$ per comparison in the "third in a row" sense, i.e. about **95** such
events a year, a 12-fold reduction — while a *real* regression of more than 4 % exceeds the
threshold on every comparison and is therefore still detected, on the third point (one extra
push of latency). Note the ordering: reduce noise first (b), then change the rule (c). A
median of 9 runs plus the three-point rule gives about
$0.0857^3 \times 4\,140 \approx 2.6$ alarms a year.

## ★★5 — Operation counts

(a) Growths: $4.30/2.00 = 2.15$ for a doubling and $9.20/4.30 = 2.14$ for a doubling, so
$\log_2 2.145 = 1.10$. Fitted over the whole range (this is the lesson's demo values):
slope $= 1.1008$, i.e. the kernel behaves as $O(n\log n)$ — a doubling of $n$ multiplies the
work by slightly more than 2, which is exactly what $n\log n$ predicts
($2 \times \log(2n)/\log n = 2.15$ at these sizes).

(b) A quadratic kernel doubles the work fourfold each time, so $\log_2 4 = 2$ and the fitted
slope is 2.000.

(c) At 8 % noise a 3 % change needs
$n = (2.487 \times 0.08/0.03)^2 = 43.7 \to 44$ repeats, and a 10 % change 4 repeats. The
operation count needs **one** run and is exact: an algorithmic change from $n\log n$ to $n^2$
is invisible at one problem size but unmistakable in the slope between two sizes, whereas the
same change in a timing series must be distinguished from 8 % noise. The count is the better
instrument because it measures the thing that changed.

## ★★6 — Changing the estimator

(a) For $\sigma = 0.10$, best-of-5 reports the minimum of 5 draws, whose expectation is
$-1.163\sigma = -0.1163$, i.e. **0.116 below** the true value; best-of-20 gives
$-2.060\sigma = -0.2060$, i.e. **0.206 below**. The switch from 5 to 20 therefore lowers the
reported time by 0.090 — about a **9 % "speedup"** that has nothing to do with the code.

(b) The trend line acquires a step: a level shift of −9 % at the commit that changed the
estimator, followed by a new, flatter noise band (spread falls from 0.0667 at best-of-5 to
roughly 0.040 at best-of-20). A reader of the trend will attribute the step to the code
change in that commit.

(c) Record: the estimator and $N$ in every row of the trend file; a **discontinuity note** at
the change with the old and new estimator, the measured bias of each under the same
conditions (the two minima against a single-run reference), and the date; and keep the old
and new series distinguishable (a separate column or a marker) so that cross-change
comparisons are not made.

## ★★★7 — Performance tracking for 12 kernels on a shared cluster

**Machine and environment control.** A dedicated benchmark partition or an exclusive
allocation; CPU governor set to performance; thread counts pinned via environment variables
and recorded (BLAS threads, OpenMP threads); NUMA binding fixed; the container digest, the
compiler version and the kernel's build flags recorded; benchmark runs at a fixed time slot.
A nightly *noise-floor* job runs the same kernels with no code change and records the spread.

**Estimator and $N$ per kernel.** The median of 9 runs (median rather than best-of, to avoid
the low bias of §6; the bias is small for the median — the median of a normal is unbiased).
$N = 9$ because the noise floor on the controlled machine is expected to be a few per cent,
and 9 runs already reduce the standard error of the median to about
$1.2533\sigma/3 = 0.42\sigma$.

**Effect size to track.** 10 % for runtime by default: at $\sigma = 8$ \% that needs 4 runs
per side, comfortably inside the 9 allotted, so the tracking has 80 % power at the 10 % level
with a 5 % false-alarm rate. Kernels whose cost dominates a workflow (or that are called
millions of times) get a 5 % target and 19 repeats per side, scheduled weekly rather than
nightly.

**Thresholds and alert rule.** Threshold $= 3 \times$ the measured floor for the kernel from
the noise-floor job; alert only on **three consecutive** nightly points beyond the threshold.
With a per-point rate of 0.05, the run-of-three rate is $1.25\times10^{-4}$ per comparison —
a handful of alerts a year against 12 kernels.

**Recorded per run.** Timestamp; commit; kernel name and version; machine and container
digest; thread and governor configuration; estimator and $N$; mean, median and spread; the
floor; the operation count and the achieved rate; the problem size; and a flag for scheduled
maintenance on the machine.

**Discontinuities.** Any change to the machine, the container, the compiler, the thread
configuration, the estimator, $N$, or the problem size. Each is recorded as a line in the
trend file with the old and new value, and the analysis treats the two sides separately.

**Adding a kernel.** Start with 30 nightly runs of the unchanged kernel to measure its floor,
record that as the baseline row, and only then enable alerts — an alert without a measured
floor is a guess.

**When not to alert.** During scheduled maintenance or a co-scheduled large job (the run is
labelled and excluded from the alert statistics but kept in the record); and on a kernel that
is about to be replaced, where the alert would only add noise before the change.

## ★★★8 — Evidence for "30 % faster"

**Benchmark specification.** The exact cases, input sizes and data (or a generator with a
seed); what is timed (which regions, with what warm-up); how the baseline and the method are
made to do the same work — the same output tolerance, the same convergence criterion, the same
stopping rule.

**Machine and environment.** Hardware, CPU model, memory, the load control, the container or
environment digest, compiler and flags, thread counts, and whether the two codes were run in
the same session interleaved (the only way to remove drift).

**Estimator and repeats.** The estimator (median), the number of repeats, and the measured
noise floor — from which the reader can compute the confidence interval for the difference.
For a 30 % effect at even 10 % noise, the measurement is easy; the repeats still must be
stated.

**Effect size and interval.** The mean/median speedup with a confidence interval, reported per
input size; the operation counts per case; and the complexity slopes, since an algorithmic
change scales and a constant-factor change does not.

**Identifiers.** The commit or release of both codes, the container digest, and the data
version or seed, so a reader can rerun the comparison.

**The three ways the claim can be false despite a correct measurement.**

1. **Unfair work.** The "baseline" is not doing the same computation: it converges to a
   tighter tolerance, computes something the method avoids, or is configured with fewer
   threads. A speedup claim requires an equivalence statement.
2. **A favourable input distribution.** The method is 30 % faster on the chosen sizes and
   slower elsewhere; without a size sweep, the claim is an average over an unstated subset.
3. **A hardware-specific constant factor.** The gain comes from using a wider SIMD path or a
   GPU present in the test machine; on the reader's machine the method may be slower. The
   claim must state the platform and the scaling behaviour of the advantage.

## ★★★9 — "100 % of the public API documented"

**What the generator proves.** That every public name has a docstring and that the docstring
is syntactically parseable and renders — a statement about the *API surface*, and nothing
about content.

**Four things it cannot prove.** (i) That the docstring explains anything (a generated stub
that restates the signature is not documentation); (ii) that the description matches the
behaviour; (iii) that the examples run, unless they are executed as tests; (iv) that the
parameter and unit conventions are stated, which is where numerical APIs are usually
incomplete (units, coordinate conventions, index bases, mutability, side effects).

**Documentation tests worth adding, with costs.** (i) Run every docstring example in CI:
136 examples at 0.05 s = 6.8 s, 0.13 % of a 90-minute suite — cheap and high value; (ii) run
the README's quick-start verbatim in a clean environment — seconds, and it is the path every
new user takes; (iii) check that every public docstring has a `Parameters`/`Returns` section
and a unit where a physical quantity is involved — a lint rule, near-zero cost; (iv) check
that the citation and version metadata match
([22-01-05](../../01-research-software-engineering/05-licensing-and-citation.md)).

**Measuring usability rather than presence.** Instrument the documentation site (or count
support questions) and record the time-to-first-result for a new user: give three colleagues
who have not seen the repository the quick-start instructions and time how long until they
produce a correct first output, recording the points where they got stuck. A high-value
alternative is a *task test*: five concrete tasks, timed on a fresh machine, repeated after
each documentation change.

**The measurement that settles whether the documentation helps anyone.** The time-to-first-
result for a new user with the documentation as it stands, against the same measurement with
the documentation removed (or against an earlier version). If the numbers are indistinguishable
and the questions in the support channel do not decrease, the documentation is decorative —
and the deficiency is not a missing docstring.
