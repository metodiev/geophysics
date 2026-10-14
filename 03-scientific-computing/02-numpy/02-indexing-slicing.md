---
id: 03-02-02
title: "Indexing, Slicing, Views vs Copies and Fancy Indexing"
level: beginner
prereqs: ["03-02-01"]
estimated_minutes: 75
tags: [numpy, indexing, views, copies, aliasing]
---

# Indexing, Slicing, Views vs Copies and Fancy Indexing

This lesson exists because of one sentence: **a slice does not copy**. Every
other fact about NumPy indexing is a corollary. A basic slice — `arr[1:4, 2:5]`,
`arr[::2]`, `arr[:, None]` — returns a *view*: a new array object with a
different shape, strides and offset that points at the same memory. Writing to
the view writes to the original. Reading the view reads the original. Nothing in
the syntax says so, nothing warns you, and the resulting bug appears as a
plausible number in a plot three modules downstream.

The counterweight is that *fancy* indexing — `arr[[0, 2, 5]]` or
`arr[arr > 40]` — copies, and `arr[i] = v` is a write into `arr`. So an
expression's aliasing behaviour depends on which of the two index kinds appears
inside the brackets. This lesson is a systematic account of that split, with a
reproducible demonstration of the failure and three repairs.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** any indexing expression as a view or a copy, and **verify** the
   classification with `np.shares_memory` rather than by reasoning about names.
2. **Reproduce** the silent-corruption bug in which a function that was meant to
   return a modified copy destructively modifies its caller's array, and
   **measure** the corruption.
3. **Repair** that class of bug with `copy`, `astype` or `np.array(..., copy=True)`,
   and **state** which is appropriate when.
4. **Use** fancy indexing and boolean masks correctly, including the pairwise
   (not Cartesian) semantics of `arr[i, j]` with two index arrays, and the
   `np.ix_` idiom for a true Cartesian selection.
5. **Use** masked assignment `arr[mask] = value` and explain why it writes to the
   original while `arr[mask]` on the right-hand side does not.
6. **Predict** whether `reshape`, `transpose` and `ravel` return views, and
   explain the role of contiguity in `ravel`.
7. **Recognise** the buffered-assignment trap in `a[idx] += 1` for repeated
   indices, and use `np.add.at` when duplicate contributions must accumulate.

## Prerequisites

- [01 ndarray Creation, dtypes, Shapes and Strides](./01-ndarray-basics.md) — the
  shape/strides/offset model that makes views possible.
- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](../01-python-fundamentals/03-control-flow.md)
  — the loop that a mask replaces.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](../01-python-fundamentals/09-iterators-generators.md)
  — the same "reference to live data" idea in the Python data model.

## 1. The two indexing grammars

NumPy distinguishes two kinds of index expression.

**Basic indexing** uses integers, slices, `Ellipsis` (`...`), `None`/`newaxis`
and `np.newaxis`. It **always returns a view**. These are all basic:

```python
arr[1:4]            # slice
arr[2:, 1:3]        # two slices
arr[:, 0]           # slice plus integer
arr[::2, ::-1]      # strided slice
arr[:, None]        # newaxis
arr[...]            # ellipsis
```

**Advanced indexing** uses an integer array, a boolean array, or a list. It
**always returns a copy**:

```python
arr[[0, 2, 5]]                 # integer array index
arr[np.array([0, 2, 5])]       # the same, explicitly
idx = np.array([True, False, True]); arr[idx]   # boolean mask
arr[arr > 40]                  # boolean mask from a comparison
```

Mixing them in one expression — `arr[1:4, [0, 2]]` — gives a copy, because
advanced indexing anywhere in the index forces one.

## 2. The demonstration: a slice that silently modified the original

The demo builds a synthetic `(6, 8)` station-by-sample record and takes a
sub-block:

```
sub = rec[1:4, 2:5] =
 [[ 10. 999.  12.]
 [ 18.  19.  20.]
 [ 26.  27.  28.]]
np.shares_memory(rec, sub) = True
sub.base is None (owns data) = False
sub.flags['OWNDATA']       = False

after sub[0, 0] = -999.0:
elements of rec changed    = [[1, 2]]
value written back into rec= -999.0
```

The assignment `sub[0, 0] = -999.0` reached into `rec[1, 2]`. There is no return
value to notice, no exception, and no warning. Notice also the diagnostics:
`np.shares_memory` is `True`, `sub` does not own its data, and `sub.base` is not
`None`. These three are the checks you should reach for whenever aliasing is in
doubt.

`sub.base is rec` is `False` here — `sub.base` is the underlying buffer, not the
array object — which is exactly why "check `.base is` the other array" is a
weaker test than `np.shares_memory`. Use the explicit function.

## 3. The realistic version, and three repairs

The demo's second part reproduces the bug in the form it actually occurs. A
helper is supposed to return a demeaned copy of the traces:

```python
def demean_inplace_broken(rec):
    out = rec[:, :]                 # assumed to be a copy; it is a view
    out -= out.mean(axis=1, keepdims=True)
    return out
```

Running it gives

```
max |caller_array - original| = 135.0   <- not zero!
caller's array was supposed to be untouched.
```

The caller's data has been centred in place. The function returned the right
answer *and* destroyed its input, so the failure shows up later, when some other
routine uses the raw record and finds it already demeaned. In a processing
pipeline the symptom is a factor-of-two error in an amplitude, or a double
demean that removes a genuine long-period signal.

Three repairs, all of which the demo verifies to give identical numerical output:

```python
out = rec.copy()                              # clearest intent
out = rec.astype(np.float64)                  # a copy because dtype is set
out = np.array(rec, dtype=np.float64, copy=True)
```

`rec.copy()` is the one to use unless the dtype change is also wanted. The rule
to adopt permanently: **any function that writes into an array it did not
create must say in its docstring whether it copies the input.** If it does not
copy, name it with a verb that warns the reader — `_inplace_`, or the convention
that the first argument is modified and returned.

## 4. Fancy indexing and boolean masks

Both copy. The demo:

```
np.shares_memory(rec, rec[idx])       = False
picked.base is None (owns its data)   = True
after picked[0, 0] = -1.0: rec[0, 0] = 0.0 (unchanged)

rec > 40 gives 8 selected values
selected = [999.  41.  42.  43.  44.  45.  46.  47.]
```

So `picked` is safe to modify. Two subtleties are worth more than the main fact.

**Two index arrays are pairwise, not Cartesian.** Verified directly:

```python
>>> c = np.arange(6).reshape(2, 3)
>>> c[[0, 1], [0, 2]]
array([0, 5])
```

That selects `c[0, 0]` and `c[1, 2]` — the two pairs, not the four combinations.
For the Cartesian selection use `np.ix_`:

```python
>>> c[np.ix_([0, 1], [0, 2])]
array([[0, 2],
       [3, 5]])
```

This trap matters most in practice for picking a sub-list of rows and a
sub-list of columns from a data matrix.

**Masked assignment writes; masked selection does not.**

```
row assignments through a mask DO reach the original -- the mask is
a copy but `rec[mask] = value` is a setitem on rec
```

`rec[rec > 40] = 0.0` is a single operation that zeroes every value above 40,
in place, without materialising an index list. `rec = rec[rec > 40]` discards
the geometry — the result is 1-D — and is almost never what a grid workflow
wants; if you need the geometry, use `np.where` or a masked array.

**Buffered assignment with repeated indices.** The single most surprising
behaviour in this lesson is

```python
>>> a = np.zeros(5)
>>> a[[0, 0, 2]] += 1
array([1., 0., 1., 0., 0.])
```

The increment was applied once, not twice, because `a[[0, 0, 2]] += 1` is
`a.__setitem__([0,0,2], a.__getitem__([0,0,2]) + 1)`: the gather produces a copy,
the add modifies the copy, and the scatter writes each destination once. When
duplicate contributions must accumulate, use the unbuffered ufunc method:

```python
>>> b = np.zeros(5)
>>> np.add.at(b, [0, 0, 2], 1)
array([2., 0., 1., 0., 0.])
```

This is the scatter-accumulation pattern behind gridding, binned statistics and
spatial joining, and lesson [08](./08-vectorisation-patterns.md) returns to it
with measurements.

## 5. reshape, transpose and ravel

The demo prints the aliasing status of each:

```
a.reshape(2, 3, 4) shares memory: True
a.T                shares memory: True
a.ravel()          shares memory: True
a.T.reshape(-1)    shares memory: False
a.T is C-contiguous: False
b = a3x4.T, b.flags['C_CONTIGUOUS'] = False
b.reshape(-1) shares memory with b: False
```

`reshape` is a view **when the requested shape is compatible with the existing
memory order** and a copy when it is not. For a C-contiguous array,
`reshape(-1)` reinterprets the flat buffer and is free; for a transposed array
the flat index order does not correspond to memory order, so NumPy copies
silently. The demo confirms with

```
after a.T[0, 0] = -7.0, a[0, 0] = -7.0   (transpose is a view)
after a.ravel()[1] = -8.0, a[0, 1] = -8.0
```

The practical consequences: use `ravel()` for speed when you truly need a flat
view and do not care about the order; use `reshape(-1)` when the order matters
and you accept that it may copy; call `np.ascontiguousarray` explicitly when you
want the copy to be visible in the profile rather than hidden inside `reshape`.

### 5.1 Which aliasing check to use, and what it costs

Two functions answer the question, and they differ in exactly one respect: speed
against certainty.

```python
np.shares_memory(a, b)       # exact; may be slow (it does a full bounds check)
np.may_share_memory(a, b)    # fast and conservative; may return True wrongly
```

`may_share_memory` uses only the bounds of the two arrays' memory regions and is
therefore fast *and* conservative: it can return `True` for arrays that in fact
overlap nowhere, because it ignores the strides that decide which bytes are
actually visited. It is the right first filter when you need to *scan* a list of
arrays inside a hot loop; it is the wrong final answer. `shares_memory` is exact
and is correspondingly slower, which is the version to use in a test or an
assertion, where being wrong is worse than being slow.

A third check is cheap and often enough:

```python
arr.flags["OWNDATA"]      # False for every view
arr.base is not None      # True for every view, but not only for views of arr
```

`OWNDATA` answers "does this array own its buffer?" — which is precisely the
question "is this a view?" — without touching the base array at all. It is an
*O(1)* attribute read, and it is the check to use when the cost of the aliasing
test matters. The demo's alias audit prints both columns side by side, and they
agree on all twelve expressions:

```
rec[1:4]                          True     False
rec[[0, 1]]                      False      True
```

The first row is a view (shared memory, does not own its data); the second is a
copy (no shared memory, owns its data). For every array in this audit the two
columns agree, which makes `OWNDATA` a reliable *and* cheap proxy for "is this a
view of its base array" — one of the few places in NumPy where the cheap test is
also the right one.

The one case where the cheap test is not enough is the one this lesson started
with: an array can be a view of *another* array that is itself a view, and
`OWNDATA` tells you only that it is a view of something. To find out whether two
names you hold refer to overlapping buffers, `shares_memory` is the answer.

## 6. An alias audit

The demo ends by classifying twelve expressions. The result:

```
expression               shares memory   OWNDATA
rec[1:4]                          True     False
rec[1:4, 2:5]                     True     False
rec[:, ::2]                       True     False
rec[...]                          True     False
rec.ravel()                       True     False
rec.T                             True     False
rec.reshape(48)                   True     False
rec[[0, 1]]                      False      True
rec[rec > 10]                    False      True
rec.copy()                       False      True
rec + 0                          False      True
rec.astype(np.float32)           False      True

views: 7   copies: 5
```

Read the last five rows as a rule: **anything that changes the dtype or gathers
scattered indices copies; anything that changes only shape, strides or offset is
a view.** `rec + 0` copies because it is a computation, not an index expression
— the fact that adding zero is arithmetically an identity does not make it
memory-identity.

## 7. Physical interpretation

The mental model that keeps this straight: an array is a *window onto a
recording*. `rec[1:4, 2:5]` is a smaller window onto the same recording — you
have not made a new recording, and anything you write on the window is on the
recording. `rec.copy()` is a duplicate recording, with its own file. A boolean
mask is a list of page numbers you have written down on a separate sheet: the
sheet is new, the pages are the same.

In geophysical terms, the corruption in §3 is the difference between *"I applied
a filter to my traces"* and *"I applied a filter to the raw field records and
also to my working copy"*. Both produce a filtered section; only one leaves the
raw data intact for re-processing. Raw data is expensive (a field campaign) and
the working copy is cheap, so the rule is always to view, and to copy
deliberately.

## 8. Assumptions and regime of validity

- **Views keep the base alive.** A 100-element view of a 2 GB array retains the
  2 GB. `arr.base` is the pointer to check; `arr.flags['OWNDATA']` is `False`
  for a view.
- **`np.shares_memory` is exact**, and may be slow for large arrays because it
  does a thorough bounds check. `np.may_share_memory` is a fast conservative
  test that returns `True` for `c` and `c.T` — useful as a first filter, not as a
  proof.
- **Two arrays can share memory without any obvious relation.** `np.shares_memory`
  on arrays of a sliced view chain reports `True` for objects that never
  mentioned each other; this is the mechanism behind bugs that survive review.
- **A masked that selects nothing still copies** (to an empty array), and a mask
  of the wrong shape raises `IndexError` — the error surfaces only at run time.
- **`arr[i] = v` broadcasting** applies `v` across the selection; `arr[i] += v`
  with repeated indices drops duplicates (§4). The two lines look equally
  innocuous and are not.
- **Integer arrays of dtype `bool` are masks; lists are promoted to arrays.**
  `arr[[True, False]]` is a mask, `arr[[1, 0]]` is a gather of rows 1 and 0.
  A list of booleans and a list of integers do different things with identical
  syntax.
- **Copies are not free.** A `rec[rec > 40]` on a large 2-D grid allocates half
  the array. In a loop over 10 000 traces the allocation dominates the run time;
  prefer masked assignment.

## 9. Python demonstration

The script is
[`code/indexing_slicing_demo.py`](./code/indexing_slicing_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/indexing_slicing_demo.py
```

The record is SYNTHETIC and deterministic — `np.arange(48).reshape(6, 8)` with a
spike at `[1, 3]` — so every before/after pair printed below is reproducible
exactly, with no random seed involved.

Key output (this machine, NumPy 2.5.4):

```
sub = rec[1:4, 2:5] =
 [[ 10. 999.  12.]
 [ 18.  19.  20.]
 [ 26.  27.  28.]]
np.shares_memory(rec, sub) = True
sub.base is None (owns data) = False
sub.flags['OWNDATA']       = False
```

```
max |caller_array - original| = 135.0   <- not zero!

  repair [rec.copy()                ] caller unchanged = True, output == result: True
  repair [rec.astype(float64)       ] caller unchanged = True, output == result: True
  repair [np.array(rec, copy=True)  ] caller unchanged = True, output == result: True
```

```
rec > 40 gives 8 selected values
np.shares_memory(rec, rec[mask]) = False
```

```
a.reshape(2, 3, 4) shares memory: True
a.T                shares memory: True
a.ravel()          shares memory: True
a.T.reshape(-1)    shares memory: False
```

```
views: 7   copies: 5
```

### What to observe

1. The corruption magnitude 135.0 is exactly the spike value 999.0 minus the
   demeaned value it was replaced by — which is the point: the corruption is
   large, silent, and would survive any check that only looked at the returned
   array.
2. `135.0` appears in the *caller's* array, so an assertion inside the helper
   would not have caught it. The assertion has to be at the boundary: check the
   input is unchanged after the call, or copy at the top of the helper.
3. All three repairs produce output equal to the broken version's output, which
   confirms that the bug is purely about memory, not about arithmetic. Fixing
   one of these fixes the numerical result without changing a single numeric
   operation.
4. The alias audit's `views: 7   copies: 5` is a compact statement of the whole
   lesson; reproduce it on your own arrays when you inherit unfamiliar code.

## 10. Common mistakes

1. **`out = arr`** instead of `out = arr.copy()`. The most common form of the
   bug in §3, and the hardest to see, because the two lines look like a
   legitimate alias.
2. **`out = arr[:]`**, `out = arr[:, :]` or `out = arr.reshape(arr.shape)` —
   three different-looking copies that are three different-looking views.
3. **`arr[idx] += 1` with repeated `idx`.** Increments are dropped (§4).
4. **`arr[rows, cols]` expecting a Cartesian submatrix.** It is pairwise; use
   `np.ix_`.
5. **`arr[arr > threshold]` inside a loop** when masked assignment would do the
   same work without allocating.
6. **Assuming `ravel` copies because you called `.T`.** It is `reshape`'s
   compatibility rule that decides, not the history of the array.
7. **Keeping a small view and wondering why memory is not released.** The base
   array is retained.
8. **Using a list of integers where a boolean mask was meant** (or the reverse).
   `[0, 1]` means two rows; `[False, True]` means a mask of length 2.

## 11. Real-world applications

- **Trace editing.** Blanking a noisy window is `data[t0:t1, :] = 0.0` — an
  in-place write through a view, which is what you want: it edits the record,
  not a copy.
- **Amplitude normalisation.** Dividing each trace by its maximum must not write
  into the raw record; the pervasive bug in student processing codes is
  normalising in place and then re-normalising in a later step.
- **Gravity and magnetic grids.** Masking a survey polygon is
  `grid[mask] = np.nan`; extracting the interior is `inside = grid[mask]`, and
  the two are different by design.
- **Seismic gathers.** Sorting a sorted gather by offset uses fancy indexing and
  therefore produces a new array — a necessary copy, since the sort permutation
  is not a stride pattern.
- **Inversion.** A model update on a subset of cells where bounds are inactive is
  `m[active] += dm[active]`; if `active` contains a repeated index the update is
  silently wrong, which is why bound-constrained solvers use `np.add.at`
  or a projection step.
- **Machine learning pipelines.** A batch is often a view into a large tensor;
  normalising it in place corrupts the dataset for the next epoch. This is the
  same bug, at scale.

## 12. Further reading

- **NumPy documentation, "Indexing on ndarrays" and "Copies and views".**
  [https://numpy.org](https://numpy.org) — the authoritative statement of the
  basic/advanced split reproduced here, including the buffering rule for
  augmented assignment. Level: beginner.
- **NumPy documentation, "Broadcasting" and `np.shares_memory` reference.**
  [https://numpy.org](https://numpy.org) — the exact definitions, including the
  conservative nature of `np.may_share_memory`. Level: beginner.
- **Harris, C. R., et al. "Array programming with NumPy." *Nature* 585, 357–362
  (2020).** Section on views and memory. DOI 10.1038/s41586-020-2649-2. Level:
  intermediate.
- **van der Walt, S., Colbert, S. C., & Varoquaux, G. "The NumPy array: a
  structure for efficient numerical computation." *Computing in Science &
  Engineering* 13(2), 22–30 (2011).** DOI 10.1109/MCSE.2011.37. Level:
  intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 ndarray Creation, dtypes, Shapes and Strides](./01-ndarray-basics.md) — the
  stride model that makes a slice free and a gather expensive.
- [03 Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) — views
  created by `None`/`newaxis`, which are the ones that catch people out.
- [08 Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md)
  — `np.add.at`, scatter accumulations and binned reductions.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](../01-python-fundamentals/09-iterators-generators.md)
  — the reference-versus-value distinction in the Python data model.
- [22-data-engineering-reproducibility/…](../../22-data-engineering-reproducibility/README.md)
  — why raw data must remain immutable through a pipeline.

Exercises:
[`exercises/02-indexing-slicing-exercises.md`](./exercises/02-indexing-slicing-exercises.md)
and
[`exercises/02-indexing-slicing-solutions.md`](./exercises/02-indexing-slicing-solutions.md).

## Self-assessment checklist

- [ ] I can classify ten indexing expressions as view or copy without running
      them, and check my answers with `np.shares_memory`. (§1, §6)
- [ ] I can write a function that demeans traces without modifying its input, and
      say in the docstring that it copies. (§3)
- [ ] I can state why `rec[:, :]` is not a copy, and name three expressions that
      are. (§1, §6)
- [ ] I can explain the pairwise semantics of `arr[rows, cols]` and the `np.ix_`
      repair. (§4)
- [ ] I can explain why `a[[0, 0]] += 1` increments once and what to use
      instead. (§4)
- [ ] I can predict when `reshape(-1)` on a transposed array will copy. (§5)
- [ ] I can describe a bug in my own past code that this lesson would have
      caught. (§10)
