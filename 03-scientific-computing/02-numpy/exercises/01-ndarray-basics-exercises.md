# Exercises — 03-02-01 ndarray Creation, dtypes, Shapes and Strides

Attempt these **closed-book** before opening the
[solutions](./01-ndarray-basics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked "run the demo" refer to
[`../code/ndarray_basics_demo.py`](../code/ndarray_basics_demo.py); run it with
the project interpreter and report its **actual** output rather than a
recollection of it:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/ndarray_basics_demo.py
```

Every memory answer in this set must be given in **decimal megabytes**
($10^6$ bytes), with the arithmetic shown.

---

## ★ Foundational

**★1.** A gravity grid has 2000 stations along east and 3000 along north, stored
as `float64`.

(a) State its shape in the `(north, east)` convention.
(b) Compute its `size` and its `nbytes` in bytes and in megabytes.
(c) Compute the same two quantities if the grid is stored as `float32`.
(d) Compute the memory of the same grid stored in `int16` (raw digitiser
counts), and state whether that representation is appropriate for a *processed*
gravity field.

---

**★2.** Give the strides of each array, in bytes, with no measurement:

(a) `np.zeros((100, 80), dtype=np.float64)`.
(b) `np.zeros((5, 4, 3), dtype=np.int16)`.
(c) `np.zeros((40, 60, 60), dtype=np.float32)`.
(d) State which axis is traversed contiguously in each case.

---

**★3.** A survey occupies $2 \times 10^3$ by $3 \times 10^3$ stations with 4096
samples per station.

(a) Compute the number of values.
(b) Compute the storage in `float64`, `float32` and `int16`.
(c) State the dtype you would choose for the *acquired* data and the dtype you
would choose for the *final processed stack*, and why they differ.
(d) Compute the relative precision of `float32` from its machine epsilon
$1.192 \times 10^{-7}$ in decimal digits, using
$\log_{10}(1/\epsilon)$.

---

**★4.** A colleague sums a `float32` array of $10^8$ values equal to `0.1`.

(a) State the exact mathematical sum.
(b) Explain why the `float32` result cannot be exact, in terms of the binary
representation of `0.1`.
(c) The demo reports a `float32` sum of `1000000.125` for a mathematically exact
$10^6$. Give a one-line fix that keeps the array in `float32` but recovers full
precision in the *sum*, and state which part of the error that fix cannot remove.
(d) State the dtype of the result of `np.sum(np.array([1, 2, 3], dtype=np.int8))`
and explain the promotion.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) `gz.nbytes`, `gz.itemsize` and `gz.strides` from Section 1.
(b) `cube.size`, `cube.nbytes` and `cube.strides` from Section 3.
(c) The `float32` and `float64` machine epsilons printed in Section 2.
(d) The C-order and F-order strides of the `(4, 5)` array in Section 5.
(e) The measured `sum(float32)` and `sum(float64)` for the $10^7$ samples of
`0.1` in Section 4, with the two errors.

---

**★★6.** Build a survey grid with 20 east stations, 10 north stations, easting
starting at 1000 m and northing at 2000 m, both spaced 50 m.

(a) Construct `east` and `north` with `arange`, and `E`, `N` with
`meshgrid(..., indexing="xy")`, and give the shape of `E`.
(b) State the value of `E[0, :3]` and of `N[:3, 0]`.
(c) Repeat with `indexing="ij"` and state what changed.
(d) Explain why the difference is invisible for a square grid and why that makes
it dangerous.

---

**★★7.** A 3-D velocity model has $600 \times 600 \times 400$ cells.

(a) Compute the memory in `float32` and in `float64`.
(b) A finite-difference solver needs the model plus four `float64` wavefield
arrays of the same shape. Compute the peak memory.
(c) State which dtype you would use for each and justify the choice from the
number of digits required to represent a velocity in m s⁻¹.
(d) Compute how many $(1000 \times 1000 \times 1000)$ `float32` models fit in
16 GB of RAM alongside a 2 GB operating system and the four wavefields of part (b).

---

## ★★★ Research-oriented

**★★★8.** Write down a rule that, given (i) the physical precision of the
measurement, (ii) the number of operations to be applied, and (iii) the available
memory, chooses a storage dtype. State the rule so that it can be checked: name
the quantity that must be estimated and the formula that gives the accumulated
relative error after $N$ operations. Then apply it to decide between `float32` and
`float64` for a $10^8$-cell model subjected to a $10^5$-step time integration.

---

**★★★9.** Endianness and file interchange. A legacy binary file of 4096 `int16`
samples was written on a big-endian machine.

(a) State how `np.dtype` encodes byte order and what the `'<'`, `'>'` and `'='`
prefixes mean.
(b) Describe how to read the file with `np.fromfile` and convert the byte order.
(c) Explain why `arr.byteswap()` alone does not change the values you compute with
until you also change the dtype.
(d) State the check that tells you whether the order is right, using a physical
property of the data rather than a guess.
