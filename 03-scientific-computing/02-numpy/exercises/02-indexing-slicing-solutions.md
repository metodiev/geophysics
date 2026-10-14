# Solutions — 03-02-02 Indexing, Slicing, Views vs Copies and Fancy Indexing

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values attributed to a verified snippet were
> produced with the project interpreter (NumPy 2.5.4).

---

## ★1 — View or copy

Taking `a = np.arange(12, dtype=np.float64).reshape(3, 4)` as the test array:

| expression | verdict | proof |
|---|---|---|
| (a) `a[1:]` | **view** | `np.shares_memory(a, a[1:])` → `True` |
| (b) `a[:, 1:3]` | **view** | `np.shares_memory(a, a[:, 1:3])` → `True` |
| (c) `a[1:, ::2]` | **view** | strides `(32, 16)`, shares → `True` |
| (d) `a[[0, 2]]` | **copy** | shares → `False` |
| (e) `a[a > 5]` | **copy** | shares → `False` (and the result is 1-D) |
| (f) `a.reshape(-1)` | **view** | contiguous input, so no copy is needed |
| (g) `a.T.reshape(-1)` | **copy** | shares → `False`; the transpose is not C-contiguous |
| (h) `a + 0` | **copy** | it is an arithmetic operation, not an index expression |
| (i) `a[...]` | **view** | `Ellipsis` is basic indexing |
| (j) `np.asarray(a)` | **view** | returns `a` itself when dtype and layout already match |

All ten verdicts were confirmed with `np.shares_memory` on the interpreter.

---

## ★2 — Three demean functions

```python
def demean_copy(rec):
    out = rec.copy()
    out -= out.mean(axis=1, keepdims=True)
    return out

def demean_astype(rec):
    out = rec.astype(np.float64)
    out -= out.mean(axis=1, keepdims=True)
    return out

def demean_newarray(rec):
    out = np.array(rec, dtype=np.float64, copy=True)
    out -= out.mean(axis=1, keepdims=True)
    return out
```

All three were verified to leave the caller's array unchanged and to return the
same values. When the input is already `float64`, the copy made by `astype` is
**still necessary** — `astype` with an identical dtype still copies unless
`copy=False` is passed, and `copy=False` would reintroduce the bug. The demo's
repair table reports exactly this:

```
  repair [rec.copy()                ] caller unchanged = True, output == result: True
  repair [rec.astype(float64)       ] caller unchanged = True, output == result: True
  repair [np.array(rec, copy=True)  ] caller unchanged = True, output == result: True
```

---

## ★3 — Repeated indices in an augmented assignment

**(a)** `array([0., 5., 5., 0.])` — verified.

**(b)** `c[[1, 1, 2]] += 5` is evaluated as
`c.__setitem__([1,1,2], c.__getitem__([1,1,2]) + 5)`: the gather produces a
*copy* of the three values, the addition modifies that copy, and the scatter then
writes index 1 twice, the second write overwriting the first. The gathered value
is `[0, 0, 0]`, so `+5` gives `[5, 5, 5]` and index 1 receives `5` twice.

**(c)** `np.add.at(c, [1, 1, 2], 5)` → `array([ 0., 10., 5., 0.])` — verified. The
ufunc method is *unbuffered*: it performs each element update in turn on the
destination.

**(d)** Gridding scattered station measurements onto a bin index (duplicate
stations in a cell), and accumulating a stack of traces that share a bin in a
common-midpoint or common-reflection-point gather. Bootstrap resampling with
replacement is the third, statistical, case.

---

## ★4 — Masked assignment against masked selection

```python
rec[rec > threshold] = 0.0     # in place: shape preserved, no allocation
rec = rec[rec > threshold]     # new 1-D array: geometry discarded, copy made
```

`rec[mask] = 0.0` is a `__setitem__` on `rec`: it writes into the existing array,
so the shape and strides of `rec` are untouched, and no temporary is allocated
beyond the `bool` mask itself. `rec = rec[mask]` rebinds the name to a *new* 1-D
array containing only the selected values; the grid structure is gone and any
coordinate arrays that described it no longer correspond.

**The first preserves the survey geometry.** Use `np.where(mask, 0.0, rec)` when a
new array with the same shape is wanted, and a masked array
(`np.ma.masked_array`) when the missing values must be tracked rather than
replaced.

---

## ★5 — Reporting the demo

**(a)**

```
np.shares_memory(rec, sub) = True
sub.base is None (owns data) = False
sub.flags['OWNDATA']       = False
```

**(b)** `elements of rec changed    = [[1, 2]]`, with
`value written back into rec= -999.0`.

**(c)** `max |caller_array - original| = 135.0   <- not zero!`, and the three
repairs all report `caller unchanged = True, output == result: True`.

**(d)** `views: 7   copies: 5`.

The corruption magnitude deserves a comment: $135.0 = 999.0 - 864.0$, where
$864.0$ is the value the demean step wrote at `[1, 3]` — the spike minus the row's
mean. The corrupted element is the *spike*, which is precisely the element a
downstream amplitude analysis cares about most.

---

## ★6 — Gather operations

Let `g` have shape `(ntrace, nsample)` and dtype `float32`.

**(a)** `g[:, :100]` — **view**. A slice of the last axis, itemsize 4.
**(b)** `g[::2]` — **view**. A step of 2 along axis 0.
**(c)** `g[np.abs(g).max(axis=1) > 2.0]` — **copy**. Advanced indexing.
**(d)** `g[10:20, 100:200] = 0.0` — not a new array at all; an in-place write into
the original through a view, shape `(10, 100)`.
**(e)** `g[[3, 7]] = g[[7, 3]]` — the right-hand side is a copy (fancy indexing),
so the exchange is safe. Writing `g[[3, 7]] = g[[7, 3]]` without the intermediate
copy would also work *because* of the gather-then-scatter buffering, but relying
on that is exactly the `c[[1, 1, 2]] += 5` trap in a different guise; be explicit
with a temporary when the indices overlap.

---

## ★7 — Fixing the broken demean

**(a)** The smallest edit is to change `rec[:, :]` to `rec[:, :].copy()`, or
equivalently `rec.copy()`. Both leave the rest of the function untouched.

**(b)** `out = rec` binds a second name to the *same array object*. `out -= ...`
is then `rec -= ...`; the failure is identical, and it is even more confusing
because `out is rec` is `True` and could in principle be checked.

**(c)** When the caller passes a temporary — an expression like
`np.arange(48.0).reshape(6, 8)` — there is no other reference to the array, so
corrupting it is harmless, *and the function appears to work*. This is why the bug
survives unit tests written with literals and temporaries, and appears only when a
named array is passed. Good tests pass named arrays and check them afterwards.

**(d)** In the caller:

```python
record = load_raw()                 # a named array
before = record.copy()
traces = demean_inplace_broken(record)
assert np.array_equal(record, before), "demean modified its input"
```

An assertion *inside* the function cannot catch it, because the function cannot
know whether its caller still holds a reference to the buffer, and comparing the
input with itself would always pass — the corruption is performed by the function
itself, so by the time the assertion runs, "before" no longer exists. The defect
is about the *boundary*, so the test must be at the boundary.

---

## ★★8 — Useful elements per cache line

Let the last axis have stride $s_2$, the first $s_0$, and the line size be
$L = 128$ bytes.

**Along the last axis:** stride 8 bytes (one `float64`), so a line supplies
$L / 8 = 16$ useful elements. This is the ideal case, ratio 1.

**Along the first axis:** the stride is $n_1 n_2 \times 8$ bytes, which for any
array of more than 16 elements per row exceeds the line length. Every step lands
on a different line, so a line supplies **1** useful element. Ratio $1/16$.

**Along `a[:, :, ::8]`:** the last-axis stride is $8 \times 8 = 64$ bytes, so a
128-byte line supplies **2** useful elements. Ratio $2/16 = 1/8$.

The measured penalty in the demo was **17.8×** (17.8–23.9× across runs), corresponding to a traversal
stride of 128 bytes:

```
arr[:, ::16].shape = (3000, 188), strides = (24000, 128)
```

i.e. the last axis was decimated by 16, giving a stride of $16 \times 8 = 128$
bytes = exactly one line. So a line supplies 1 useful element and the ideal is 16
— a naive bandwidth-ratio prediction of **16×**. The measured 17.8× is *larger*
than 16× because the prediction ignores the extra address arithmetic, the loss of
hardware prefetching and the fact that both a read and a write of the line occur
for an in-place add. The prediction of the *mechanism* is right; the exact ratio
requires the measurement.

---

## ★★★9 — A black-box aliasing test

**(a)** The observable is **the identity and content of the caller's object after
the call**:

```python
def writes_into_input(fn, *args, **kwargs):
    inputs = [a for a in args if isinstance(a, np.ndarray)]
    before = [a.copy() for a in inputs]
    fn(*args, **kwargs)
    return [not np.array_equal(a, b) for a, b in zip(inputs, before)]
```

Returning `True` for any input means the function wrote into it. A weaker but
complementary test is `np.shares_memory(result, input)` on the return value: a
shared-memory result means the function returned a view (and therefore may also
have written through it).

**(b)** **One call gives a definitive verdict for content changes, not a
statistical one.** If the input changed, the function writes into its input — no
uncertainty. If it did not change, the function might still write *sometimes* (on
a branch not taken, for a different shape, for a non-contiguous input), so the
negative verdict is only as strong as the coverage of the arguments you passed.
There is no confidence level to quote; there is coverage. Test with a contiguous
and a transposed input, with an empty selection and a full selection, and with the
shape that triggers the branch.

**(c)** The failure mode is a function that writes the *same value* it read — for
instance one that recomputes a quantity that is already correct, or that writes
zeros into a region that is already zero. The content comparison cannot see it,
and `np.shares_memory` on the *inputs* is not applicable. Two mitigations: (i)
pass inputs that are deliberately *not* fixed points of the operation (a random
array rather than a zeros array, with a seed so the test is reproducible), and
(ii) if the function's contract matters, read the source or test with an
instrumented subclass of `ndarray` that records `__setitem__` calls. The practical
rule is to test with random data, never with zeros or arange — a lesson worth
generalising to every behavioural test in a numerical code.
