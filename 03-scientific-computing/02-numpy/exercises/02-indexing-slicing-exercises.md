# Exercises — 03-02-02 Indexing, Slicing, Views vs Copies and Fancy Indexing

Attempt these **closed-book** before opening the
[solutions](./02-indexing-slicing-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/indexing_slicing_demo.py`](../code/indexing_slicing_demo.py) require you
to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/indexing_slicing_demo.py
```

Unless a problem says otherwise, write every answer as **Python code plus a
one-sentence statement of whether memory is shared**.

---

## ★ Foundational

**★1.** For each expression, state **view** or **copy**, and give the operation
that would prove it:

(a) `a[1:]`
(b) `a[:, 1:3]`
(c) `a[1:, ::2]`
(d) `a[[0, 2]]`
(e) `a[a > 5]`
(f) `a.reshape(-1)`
(g) `a.T.reshape(-1)`
(h) `a + 0`
(i) `a[...]`
(j) `np.asarray(a)`

---

**★2.** Write the function

```python
def demean(rec):
    """Return a demeaned copy of rec, leaving rec unchanged."""
```

three ways (using `copy`, `astype` and `np.array`), and state which of the three
copies is *necessary* when the input dtype is already `float64`.

---

**★3.** Consider

```python
c = np.zeros(4)
c[[1, 1, 2]] += 5
```

(a) Give the resulting array.
(b) Explain, in one sentence, why the repeated index is lost.
(c) Give the replacement that accumulates correctly and state its result.
(d) Name two geophysical operations where duplicate indices are the norm rather
than the exception.

---

**★4.** Explain the difference between

```python
rec[rec > threshold] = 0.0
rec = rec[rec > threshold]
```

in terms of shape, memory and intent. State which one preserves the survey
geometry.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) `np.shares_memory(rec, sub)`, `sub.base is None` and `sub.flags['OWNDATA']` for
`sub = rec[1:4, 2:5]`.
(b) The list of elements of `rec` that changed after `sub[0, 0] = -999.0`.
(c) The value of `max |caller_array - original|` after the broken demean, and the
three repair routes with their `caller unchanged` verdicts.
(d) The line reporting the number of views and copies in the alias audit.

---

**★★6.** A seismic gather is stored as a `(ntrace, nsample)` `float32` array
`g`. Write, without running anything, the expression for each operation, and state
whether the result is a view or a copy:

(a) The first 100 samples of every trace.
(b) Every second trace.
(c) The traces whose maximum absolute amplitude exceeds `2.0`.
(d) A run of samples, `g[10:20, 100:200]`, with an amplitude of exactly `0.0`.
(e) The gather with traces 3 and 7 exchanged, without copying the samples.

---

**★★7.** The demo's broken function is

```python
def demean_inplace_broken(rec):
    out = rec[:, :]
    out -= out.mean(axis=1, keepdims=True)
    return out
```

(a) Give the smallest edit that fixes it, character for character.
(b) Explain why `out = rec` (rather than `rec[:, :]`) fails identically.
(c) Explain why the corruption is invisible if the caller passes a *temporary*,
e.g. `demean_inplace_broken(np.arange(48.0).reshape(6, 8))`.
(d) Add one assertion to the function's *caller* that would catch the bug in a
test suite, and say why an assertion *inside* `demean_inplace_broken` cannot.

---

## ★★★ Research-oriented

**★★★8.** Derive the number of elements of a `(n0, n1, n2)` `float64` C-ordered
array that a single cache line (128 bytes) can supply under three traversals:
along the last axis, along the first axis, and along `a[:, :, ::8]`. State the
ratio of useful elements per cache line to the ideal case, and use it to predict
which of the three the measured strided penalty (17.8–23.9×) corresponds to.

---

**★★★9.** Design a test that distinguishes "this function copies its input" from
"this function writes into its input" without inspecting its source, and that
works for an input whose shape and dtype make it hard to guess. State:

(a) the observable that distinguishes the two cases;
(b) the statistical confidence you have in the verdict after one call;
(c) the failure mode of your test when the function happens to write the *same*
value that was already there.
