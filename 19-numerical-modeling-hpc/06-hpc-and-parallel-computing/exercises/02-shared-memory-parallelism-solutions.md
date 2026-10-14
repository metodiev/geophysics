# Solutions — 19-06-02 Shared-Memory Parallelism: OpenMP and Threading

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs; timings are machine-dependent.

Lesson: [02 Shared-Memory Parallelism: OpenMP and Threading](../02-shared-memory-parallelism.md).

---

## ★1 — Below one

CPython holds the global interpreter lock for the duration of a bytecode
instruction, so the four threads execute the Python loop **serially** while the
interpreter still pays for creating and scheduling them. The measured $0.930\times$
is the ideal $1\times$ minus that scheduling cost: the work is unchanged, and the
overhead is added.

---

## ★2 — Efficiency

$$\text{efficiency} = \frac{3.746}{4} = 0.9365 = 93.6\%,$$

matching the printed $93.6\%$. The $6.4\%$ shortfall is cache and memory-system
contention between four sorting arrays plus thread start-up.

---

## ★3 — Race and deadlock

- **Race condition:** two threads access the same location concurrently, at least
  one writes, and the result depends on the interleaving — measured here as $578$
  lost updates of $800$.
- **Deadlock:** two or more threads each wait for a resource the other holds, so
  no progress is possible at all — the program stops rather than producing a wrong
  answer.

---

## ★4 — The model without contention

$$\frac{29.021}{4} + 4 = 7.255 + 4 = 11.255\ \text{ms},$$

a predicted speedup of $29.021/11.255 = 2.58\times$. Measured: $95.888$ ms, a
speedup of $0.303\times$. The model fails by $95.888/11.255 = 8.5\times$, and the
missing term is contention — for the GIL between calls and for the memory system
throughout.

---

## ★5 — The static bound

The makespan of a static schedule is at least the largest block:
$33$ units against an ideal of $108/4 = 27$, so the bound is
$33/27 = 1.222$. The measured ratio static/dynamic is $1.116$, which is *below*
the bound because the dynamic schedule also pays queue-locking overhead and
because the largest single item ($8$ units) still bounds it from below at
$8/27 = 0.296$ — the measured value lies between the two limits, as it must.

---

## ★6 — The rule and the invalid test

**Rule:** the digest depends on the decomposition (chunk boundaries and merge
order) and not on the number of workers executing it, provided the decomposition
is held fixed.

The chunk-count experiment is not a reproducibility test because it *changes the
arithmetic*: each chunk is summed internally by numpy's pairwise routine, so
different boundaries produce different roundings. A test that varies the thing the
claim depends on cannot verify the claim; it can only measure its sensitivity.
The valid test is: same decomposition, different pool size or machine size, same
digest.

---

## ★7 — GIL contention or memory contention?

Two experiments with distinct observables:

- **GIL contention:** replace the numpy work with a *compute-bound* kernel of the
  same duration (e.g. the sort of Section 3) and repeat. If the compute-bound
  version scales but the streaming version does not, the difference is not the GIL
  (both release it) but the memory system. Observable: speedup versus kernel type
  at fixed serial duration.
- **Memory contention:** run the streaming kernel with one thread but on four
  separate arrays of one quarter the size, so the memory footprint and traffic are
  unchanged while the concurrency is one. Observable: bandwidth at the same total
  bytes with and without concurrency.

The measured evidence already available points to memory: the single thread
reaches $92.50$ GB/s, close to the plateau measured in
[01 §2](../01-hpc-architecture.md), so there is little headroom for a second
thread to claim. If the GIL were the cause, the compute-bound sort — which also
releases the GIL and also contends for it between calls — would fail in the same
way, and it achieved $3.746\times$.

---

## ★8 — Static or dynamic?

Total work $= 2.5\ \mathrm{ns} \times 4\times10^{6} = 10$ ms; ideal per-thread
time at $P = 4$ is $2.5$ ms.

Decision rule used: **dynamic only when the imbalance it removes exceeds the
queue overhead**, and a queue acquisition costs of the order of $100$ ns. With
$4\times10^{6}$ points split into, say, $4\times10^{4}$ chunks of $100$ points,
each chunk is $250$ ns of work — the same order as the queue overhead, so dynamic
scheduling would spend a comparable amount acquiring work as doing it.

**Choose `schedule(static)`** with a fine enough split, e.g. $100$ chunks,
which bounds the imbalance at one chunk ($0.25$ ms) — $10\%$ of the ideal
$2.5$ ms — while paying no queue overhead. Dynamic becomes worthwhile when the
per-iteration cost varies by more than the chunk time, which for this stencil
would require a heterogeneity of order $100$ ns per point.
