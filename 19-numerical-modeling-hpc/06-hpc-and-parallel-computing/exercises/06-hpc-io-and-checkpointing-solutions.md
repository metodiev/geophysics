# Solutions — 19-06-06 Parallel I/O, Checkpointing and Job Management

> **Read after attempting the exercises.** Filesystem numbers are measured on the
> machine that ran the demonstration; the MTBF is an **assumed model input**.

Lesson: [06 Parallel I/O, Checkpointing and Job Management](../06-hpc-io-and-checkpointing.md).

---

## ★1 — The restart comparison

The two numbers are $\max|u_{\text{restart}} - u_{\text{uninterrupted}}|$ over the
whole field, at the final step. A lossless checkpoint writing the same arithmetic
path must give exactly $0.000$, because the same operations are applied to the
same operands in the same order after the restart. Any non-zero value is a
serialisation or restart bug — a missed field, a rounded parameter, a boundary
condition reconstructed from state it does not have — and not a rounding effect.

---

## ★2 — Overhead fraction

$$\frac{0.10}{60 + 0.10} = 0.00166 = 0.166\%.$$

The checkpoint cost is added to the interval, not substituted into it, so the
denominator is the wall time actually spent (work plus checkpoint).

---

## ★3 — The two failure modes

- **A torn file:** the checkpoint is half-written when the job dies, so it cannot
  be read at all — the demo reproduces the error
  `EOF: reading magic string, expected 8 bytes got 6`.
- **A destroyed previous checkpoint:** a direct overwrite begins by truncating the
  good file, so the crash leaves neither the new checkpoint nor the old one —
  every step since the previous interval is lost.

The rename pattern prevents both, because the old file remains valid until the
new file is complete and the rename is atomic.

---

## ★4 — The $1\%$ payload

A $30$-minute interval is $1800$ s, and $1\%$ of it is $18$ s of write time (or,
if the overhead is defined against the work time, $18.18$ s; use $18$ s and state
the convention). At $5.03$ GB/s:

$$18\ \text{s} \times 5.03\ \text{GB/s} = 90.5\ \text{GB}.$$

So a $90$ GB checkpoint costs about $1\%$ of a half-hour interval on this
filesystem. Two qualifications belong with the number: real checkpoints are often
written by many ranks at once, so the aggregate rate is not the single-stream
rate; and a $1\%$ decision must be made against the *measured* interval, not a
nominal one.

---

## ★5 — The optimal interval

$$t_{\text{opt}} = \sqrt{2\,t_{\text{ckpt}}\,\text{MTBF}}
= \sqrt{2(0.10)(3.156\times10^{7})} = \sqrt{6.312\times10^{6}}
= 2.512\times10^{3}\ \text{s} \approx 0.70\ \text{h}.$$

Work at risk per failure at that interval: half the interval plus the checkpoint
itself, $1256 + 0.1 \approx 1256$ s, matching the printed $1267$ s to within the
rounding of the interval (the demo uses the unrounded $2.534\times10^{3}$ s).

---

## ★6 — Changing the MTBF

$$\frac{t_{\text{opt}}(3.156\times10^{3})}{t_{\text{opt}}(3.156\times10^{7})}
= \sqrt{\frac{3.156\times10^{3}}{3.156\times10^{7}}} = \sqrt{10^{-4}} = 0.01 .$$

So a one-hour MTBF instead of a one-year MTBF shortens the optimal interval by a
factor of $100$, to about $25$ s. The *rule* is that the interval scales as the
**square root** of both inputs: a factor-of-four change in the MTBF changes the
interval by only a factor of two. That is the stated robustness — and it is worth
being precise about what it buys: a wrong MTBF by a factor of a hundred is wrong
in the interval by a factor of ten, and the flatness of the cost curve near the
optimum means even that is survivable, which is why a campaign can start with a
guessed MTBF and correct it from logs.

---

## ★7 — A safe multi-file checkpoint

Protocol:

1. Write all four parts under temporary names,
   `ckpt.<step>.part{0..3}.tmp`, using `os.replace` semantics never to touch the
   live files.
2. `os.replace` each temporary part into its real name **only after all four are
   complete**.
3. **Write a completion marker last:** a small file `ckpt.<step>.done` containing
   the four part hashes and the step number, written with a temporary name and
   renamed.

Restart protocol:

1. Find the highest step with a `.done` marker.
2. Verify each part's hash against the marker.
3. If any part fails, fall back to the previous step; if none is valid, start
   afresh.
4. Load the four parts and reconstruct the state — including the step number and
   the random-number-generator state.

The **marker is the whole trick**: without it, a crash between parts leaves four
individually valid files from different generations, and a restart can silently
mix them. The marker converts a set of files into a single atomic object, at the
cost of one extra rename. Two generations of the marker make the scheme robust to
a crash during the marker write.

---

## ★8 — Deciding per-rank against aggregated I/O

**Measurement:** write the same total bytes both ways, at the production rank
count and the production amount per rank, on the target filesystem, timing
several repetitions and reporting the best and the median. The demo's code is
the template: build the payload, time $P$ separate `np.save` calls and one
aggregated `np.save`, and compute the ratio, then delete the files.

**Observables that would invert the measured $0.947$:**

- **metadata cost per file:** if creating and closing a file costs milliseconds
  (a heavily loaded metadata server, a network filesystem with per-file locking),
  $P$ files pay $P$ times that cost while the aggregated write pays it once. The
  observable is the write time of a *zero-length* file as a function of $P$.
- **client-side concurrency:** if the filesystem can absorb many simultaneous
  writers (many storage targets, no shared lock), per-rank writes parallelise and
  the aggregate rate rises with $P$; if it cannot, they serialise and the
  aggregated pattern wins. The observable is aggregate throughput as a function
  of the number of concurrent writers.

A third observable worth measuring before the choice: on a shared filesystem, the
per-rank pattern produces a file count that grows with the job size, which becomes
a campaign-level problem (inode quotas, listing times) long before it becomes a
per-write problem.
