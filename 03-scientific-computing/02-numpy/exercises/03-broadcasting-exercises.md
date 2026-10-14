# Exercises — 03-02-03 Broadcasting Rules and Vectorised Thinking

Attempt these **closed-book** before opening the
[solutions](./03-broadcasting-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/broadcasting_demo.py`](../code/broadcasting_demo.py) require you to run
it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/broadcasting_demo.py
```

For every shape question, give the result shape **and** the reasoning (which axes
pair, which ones are stretched).

---

## ★ Foundational

**★1.** Give the result shape, or state that it raises, for each pair:

(a) `(64, 1) + (1, 32)`
(b) `(64, 32) + (64,)`
(c) `(64, 32) + (32,)`
(d) `(3, 1, 5) * (1, 4, 1)`
(e) `(8,) - (8, 1)`
(f) `(10, 20, 30) + (30,)`

---

**★2.** A trace array `data` has shape `(48, 2000)` — 48 channels, 2000 samples —
and `offsets` has shape `(48,)`, one source–receiver offset per channel.

(a) Write the expression that divides every trace by the absolute value of the
offset of that channel (assume no zero offsets).
(b) State the shape of the intermediate that broadcasting creates, and the shape
of the result.
(c) Rewrite the operation as a loop over channels and state which array shapes the
loop avoids allocating.
(d) State what `offsets` must be reshaped to if the array were stored
`(nsample, nchannel)` instead.

---

**★3.** A station coordinate array `xy` has shape `(500, 2)`.

(a) Write the expression for the full $500 \times 500$ distance matrix, using
`np.hypot`.
(b) Compute the memory of the result in `float64`.
(c) Compute the memory for `n = 5000` and `n = 50 000`.
(d) State the number of distance evaluations in each case, and the ratio to the
number of *independent* pairs.

---

**★4.** Explain in one sentence each:

(a) Why `mean[:, None]` is needed for a station mean but `mean[None, :]` is needed
for a sample mean.
(b) Why broadcasting does not make `np.tile` obsolete.
(c) Why `a[:, None] * b[None, :]` is called an outer product.
(d) Why `(n,) - (n,)` is not an outer product.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) The `ValueError` text for the naive demean, and the subsequent
`max |station mean after|`.
(b) The three checks on the distance matrix (`broadcast == loop`,
`max |bcast - loop|`, `diagonal is zero`).
(c) The two distance-matrix sizes for `n = 2000` and `n = 20000`.
(d) The `MB` column of the memory table, and the shape of the largest case.
(e) The bytes of the `(12,)` mean and of the demeaned array.

---

**★★6.** A gravity forward model has $n_{\text{obs}}$ observations and
$n_{\text{src}}$ sources and a kernel that decays as $1/r^2$, with
$r \ge r_{\min}$.

(a) Compute the memory of the full kernel matrix for
$n_{\text{obs}} = n_{\text{src}} = 8000$ in `float64`.
(b) Reparameterise with a block size of 500 observations. Compute the memory of
the largest intermediate and the number of blocks.
(c) State the total time *work* in kernel evaluations for both forms and explain
why they are equal.
(d) State one physical property of the kernel that could be used to truncate it
and reduce the cost below $O(n_{\text{obs}} n_{\text{src}})$.

---

**★★7.** The broadcast of a per-station scalar over traces can be written four
ways. For each, state the shape of the intermediate and whether the *result* is a
copy of `data`:

(a) `data - mean[:, None]`
(b) `data - mean.reshape(-1, 1)`
(c) `data - np.expand_dims(mean, 1)`
(d) `data -= mean[:, None]`

---

## ★★★ Research-oriented

**★★★8.** A "station-mean" subtraction is intended to remove an instrument DC
offset. Write down the model being assumed —
$\text{data}_{ij} = s_{ij} + c_i + \epsilon_{ij}$ — and answer:

(a) What is the estimator of $c_i$ that the subtraction uses?
(b) Under what condition on the signal $s$ is that estimator unbiased?
(c) Give a geophysical example where the condition fails and the subtraction
removes a real signal.
(d) Give the broadcast expression for the case where the offset is a *linear*
function of sample index, $c_i + g_i t_j$, and state the shapes involved.

---

**★★★9.** Broadcasting can silently change the *meaning* of an expression
without changing its shape. Construct an example with an array of shape
`(100, 100)` and two different arrays of shape `(100,)` such that
`a - u[:, None]` and `a - u[None, :]` have the same shape and give results that
differ. State the check that distinguishes them in a test suite, and the
invariant that must hold for the difference to be *semantically* meaningful.
