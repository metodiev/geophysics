# Exercises — 03-02-08 Replacing Loops: Vectorisation Patterns and Traps

Attempt these **closed-book** before opening the
[solutions](./08-vectorisation-patterns-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/vectorisation_demo.py`](../code/vectorisation_demo.py) require you to run
it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/vectorisation_demo.py
```

**Every performance claim must be reported with an operation count, an element
count, or a peak allocation**, not only a wall-clock ratio, and every
transformation must be accompanied by a correctness check.

---

## ★ Foundational

**★1.** State whether each form is fused or materialises an intermediate, and give
the number of full-size passes over memory:

(a) `(x * x).sum()`
(b) `np.dot(x, x)`
(c) `np.sum(np.abs(x))`
(d) `np.add(x, y, out=z)`
(e) `np.where(x > 0, x, 0.0).sum()`

---

**★2.** For a loop that appends one element at a time to an array of final length
$m$:

(a) Write the number of element copies performed, as a function of $m$.
(b) Evaluate it for $m = 20\,000$.
(c) Give two patterns that avoid the quadratic growth.
(d) State the complexity class of `np.append` used inside a loop.

---

**★3.** Answer in one or two sentences each.

(a) Why is `np.vectorize` not a performance tool?
(b) Why can a broadcast be slower than the loop it replaced?
(c) What is the difference between "vectorised" and "fused"?
(d) Why must a speed-up claim be accompanied by a correctness check?

---

**★4.** For each pattern, name the dedicated NumPy kernel:

(a) Summing weights into integer bins indexed by an array.
(b) Reducing contiguous but unequal-length segments of an array.
(c) Accumulating into a destination where duplicate indices must all contribute.
(d) A multi-index contraction that neither `@` nor broadcasting expresses
cleanly.
(e) Writing a ufunc result into a preallocated array.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) `nobs`, `nsrc`, `pairs`, the loop and broadcast times, the speed-up, the
maximum difference and the agreement verdict.
(b) The `(x * x).sum()` and `np.dot(x, x)` times and *peak traced memory*.
(c) The three `np.vectorize` timings and the ratio.
(d) The `np.append` and preallocated times, the ratio, and the stated element-copy
count.
(e) The two runs of the broadcast and of the row loop, the two time ratios, the
peak-memory ratio and the stated robust result.

---

**★★6.** A pairwise-comparison step computes, for $n = 12\,000$ receivers, an
$n \times n$ matrix of delay times.

(a) Compute the memory of the matrix in `float32`.
(b) State the number of matrix elements and the ratio to the number of
independent receiver pairs.
(c) Propose a blocked implementation with block size $B = 500$ and compute the
largest intermediate.
(d) State the total number of delay evaluations in both forms and explain why
blocking does not change it.
(e) State the case where the correct answer is neither form, and what to use
instead.

---

**★★7.** A code sums $10^6$ weighted samples into 1000 spatial bins.

(a) Write the three candidate implementations: masked accumulation,
`np.add.at`, and `np.bincount`.
(b) State which of them is silently incorrect and why.
(c) State which has a dedicated kernel and why that matters for clarity.
(d) Given that the demo measured `np.add.at` and `np.bincount` to be within a
factor of about two of each other on a similar problem, state the criterion you
would use to choose between them.

---

## ★★★ Research-oriented

**★★★8.** A convolution of a 1-second wavelet with a 60-second trace at 1 ms
sampling is currently implemented as a double loop over $60\,000 \times 1000$
samples.

(a) Compute the number of multiply-adds.
(b) State the algorithmic change that reduces the cost asymptotically, and the
new operation count for a transform of length 65536.
(c) State the memory cost of the transform and compare it with the direct form.
(d) State the condition on the wavelet length for the transform to win, and
justify it from the operation counts.
(e) State the physical property of the convolution that the transform exploits,
and one situation in geophysics where it does not hold.

---

**★★★9.** A Monte Carlo study reports a speed-up of "40×" for a vectorised
implementation of an inversion step.

(a) List the five facts a reviewer needs in order to judge the claim.
(b) State what a speed-up measured on a *small* test problem usually
overestimates, and why.
(c) State the two independent measurements that distinguish "the CPU work was
reduced" from "the memory traffic was reduced", and say which is more likely for
a large array.
(d) State the reproducibility criterion for the claim, and the one that is
achievable when the timing cannot be reproduced.
