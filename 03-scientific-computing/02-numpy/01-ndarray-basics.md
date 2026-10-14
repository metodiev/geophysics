---
id: 03-02-01
title: "ndarray Creation, dtypes, Shapes and Strides"
level: beginner
prereqs: ["03-01-04", "03-01-05"]
estimated_minutes: 75
tags: [numpy, ndarray, dtype, strides, memory]
---

# ndarray Creation, dtypes, Shapes and Strides

A gravity survey is not a list of numbers. It is a *field* — a quantity defined
at every station of a grid — and the natural representation of a field is an
array whose axes carry the geometry. Once you accept that, everything else in
this module follows: the shape is the geometry, the dtype is the precision of
the instrument that produced the numbers, and the strides are the route the
processor takes through memory to reach them.

NumPy's `ndarray` is a **single block of memory plus a description of how to
interpret it**. That description is four things: a shape (how many elements
along each axis), a dtype (how the bytes of one element are interpreted), a set
of strides (how many bytes to step to move one position along each axis), and an
offset (where the first element starts inside the block). Nothing else. A
`(100, 80)` gravity grid of `float64` and a `(100, 80)` grid of `float32` differ
only in the second item; a transposed grid differs only in the third. Two of the
three most consequential NumPy behaviours — views (lesson
[02](./02-indexing-slicing.md)) and cache performance (lesson
[07](./07-memory-performance.md)) — are direct consequences of this model, so it
is worth doing properly rather than learning as syntax.

## Learning objectives

By the end of this lesson you will be able to:

1. **Create** arrays for a 2-D survey grid and a 3-D model cube with
   `zeros`, `ones`, `empty`, `arange`, `linspace` and `meshgrid`, and explain
   when each is the right tool.
2. **Read** an array's metadata — `shape`, `size`, `ndim`, `dtype`, `itemsize`,
   `nbytes`, `strides` — and state in words what each one means physically.
3. **Choose a dtype** from a stated precision requirement, and compute the
   memory that a $10^8$-cell model occupies in each candidate dtype.
4. **Predict** the memory footprint of a model before allocating it, and explain
   why `float32` halves both the footprint and the memory traffic.
5. **Explain** what a stride is, predict the strides of a C-ordered and an
   F-ordered array, and say which axis is traversed contiguously.
6. **State** the axis-order convention of your own code and recognise the
   `(z, y, x)` versus `(x, y, z)` mismatch as a silent transposition.
7. **Recognise** the two dtype traps that produce wrong answers rather than
   errors: silent integer overflow and `float32` accumulation error.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — arrays are passed by reference; you need the function-call model first.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — a list of stations is the object an array replaces.

## 1. Why arrays, and not lists

A list of $80 \times 100 = 8000$ readings occupies several hundred kilobytes of
scattered objects: 8000 Python objects, each with a type pointer and a reference
count, plus a list of 8000 pointers to them. An array of the same readings
occupies 64 000 bytes of contiguous `float64` — one object, one header, one
buffer. The demo prints exactly this:

```
gz.shape      = (100, 80), gz.dtype = float64
gz.nbytes     = 64000 bytes = 0.0640 MB
gz.itemsize   = 8 bytes per element
```

Three consequences follow, and they are the reason geophysics is written in
NumPy:

- **Arithmetic is whole-array.** `gz_mgal = gz * 1e5` multiplies every element,
  in compiled code, in one statement.
- **Memory is predictable.** `shape` and `dtype` determine `nbytes`. You can
  size a job before submitting it (lesson
  [07](./07-memory-performance.md)).
- **The geometry is preserved.** A `(100, 80)` array is a grid, not a bag of
  numbers. The row index is a north coordinate and the column index is an east
  coordinate — provided *you* say so and never forget it.

## 2. Creating arrays

The creation functions fall into three groups.

**Filled arrays — the destination of a computation.**

```python
import numpy as np

grid = np.zeros((100, 80), dtype=np.float64)   # zeros
mask = np.ones((100, 80), dtype=bool)          # ones
cube = np.empty((40, 60, 60), dtype=np.float32)  # uninitialised, fastest
```

`zeros` and `ones` allocate and fill. `empty` allocates and fills with whatever
was in memory — it exists because a common pattern is to allocate a destination
and then write every element of it, so zeroing is wasted work. It is a bug to
read from an `empty` array before writing to it.

**Coordinate arrays — the independent variables.**

```python
east = np.arange(80) * 25.0            # 0, 25, ..., 1975 m
north = np.arange(100) * 25.0          # 0, 25, ..., 2475 m
E, N = np.meshgrid(east, north, indexing="xy")
```

`arange` is start-stop-step on integers or floats; `linspace` takes a *count*
instead of a step and is safer when the endpoint must be exact.
`np.linspace(0, 1975, 80)` guarantees the last value is 1975.0, while
`np.arange(80) * 25.0` can drift by one unit in the last place. For a survey
grid, either is fine; for a coordinate that will be differenced, prefer
`linspace`.

`meshgrid` fans the two 1-D coordinate vectors out to the full grid. With
`indexing="xy"` the result has shape `(len(north), len(east))`, so `E[j, i]` is
the easting of the station at row `j`, column `i`, and the printed pair
`E[:2, :3]` and `N[:2, :3]` shows `E` varying along columns and `N` along rows —
the usual convention for a map. The default `indexing="ij"` reverses that
meaning, and mixing the two silently transposes every field you build from the
coordinates.

**Arrays from a rule.** `np.fromfunction` evaluates a function of the indices;
`np.geomspace` gives geometric spacing; `np.eye` gives an identity matrix. All of
them are conveniences over the two groups above.

## 3. dtypes: the choice that decides whether a model fits

A dtype is both a memory and a precision decision. The demo's table gives the
size of the model that matters — a $10^8$-cell cube:

| dtype | bytes/elem | MB for $10^8$ cells | use |
|---|---|---|---|
| `bool` | 1 | 100 | flag, mask |
| `int8` | 1 | 100 | 8-bit index |
| `int16` | 2 | 200 | seismic sample |
| `int32` | 4 | 400 | default integer |
| `int64` | 8 | 800 | 64-bit counter |
| `float32` | 4 | 400 | single-precision model |
| `float64` | 8 | 800 | default float |
| `complex128` | 16 | 1600 | complex spectrum |

The rule of thumb for a $10^8$-cell velocity or density model is therefore:
**`float32` is 400 MB, `float64` is 800 MB, and a transient `float64` temporary
of the same shape doubles the cost again.** On a 16 GB laptop only the first is
comfortable once you also hold a gradient, a step length and a conjugate-gradient
vector, which is why production modelling codes use `float32` for the model and
promote only the reduction.

The cost of `float32` is precision: 24 bits of significand, so
$\epsilon = 1.19 \times 10^{-7}$ and about 7 decimal digits of relative precision
— NumPy reports the more conservative `np.finfo(np.float32).precision = 6`, meaning
six digits that can be *preserved* through a rounding. `float64` has 53 bits,
$\epsilon = 2.22 \times 10^{-16}$ and `np.finfo(np.float64).precision = 15`. The demo makes the difference concrete by summing $10^7$
values of `0.1`:

```
    exact                = 1000000.0
    sum(float32)         = 1000000.125   (error 0.125)
    sum(float32, dtype=f8)= 1000000.0149011612  (error 0.0149012)
    sum(float64)         = 1000000.0   (error 0)
```

Two lessons are in that block. First, the `float32` total is wrong in the third
decimal place of a sum that is exactly $10^6$; a survey-wide total or a mean
computed in `float32` carries that error into every downstream number. Second,
passing `dtype=np.float64` to `np.sum` recovers most of the accuracy without
storing the array in double precision — the accumulator dtype is a separate
decision from the storage dtype, and it is usually the right one to make.

Choosing a dtype is an engineering decision with a documented answer:

- **Physical measurements** (magnetic field in nT, gravity in mGal, seismic
  amplitudes in ADC counts) are usually best stored in `float64` because they
  are already fewer than $10^8$ values, and the storage saving of `float32` is
  not worth the precision loss in a difference of two nearby numbers.
- **Model parameters on a large grid** (velocity, density, susceptibility) are
  best stored in `float32` once the physics has been validated in `float64`,
  and the validation run is part of the workflow, not an optional extra.
- **Acquired time series** are best stored in the acquisition integer format
  (`int16` or `int32`) with the scale factor and offset recorded beside them,
  because converting to `float64` at read time costs memory you do not need and
  loses the provenance of the raw counts.
- **Masks and flags** are `bool`, which is 1 byte, not 1 bit. A `(10^8,)` boolean
  mask is 100 MB — often larger than the array it indexes. `np.packbits` exists
  for the cases where that matters.

## 4. Shape, size and axis order

`shape` is a tuple, one entry per axis; `size` is the product; `ndim` is
`len(shape)`. The demo's cube is

```
cube.shape    = (40, 60, 60)  (depth, north, east)
cube.size     = 144000 cells
cube.strides  = (14400, 240, 4) bytes
```

Note the arithmetic of the strides: `4` bytes is one `float32` element, `240` is
`60 × 4` (one row of the cube), and `14400` is `60 × 60 × 4` (one depth slice).
Every stride is the product of the itemsize and the lengths of all *faster*
axes. You should be able to reconstruct strides from shape and dtype by hand;
this is the single most useful habit for reading NumPy code you did not write.

The axis-order convention is a naming decision, and it must be written down.
This module uses `(z, y, x)` for model cubes so that `cube[k]` is a horizontal
depth slice, matching most modelling codes. Other conventions in wide use are
`(x, y, z)` in GIS-derived data and `(time, channel, sample)` in seismic
recordings. A mismatch is a silent transposition: the physics runs, the numbers
look plausible, and the answer is wrong. The defence is to name your axes in the
docstring and to assert shapes at every function boundary.

## 5. Strides, C order and Fortran order

Strides are the honest interface to the machine. In the demo, the same logical
`(4, 5)` array stored two ways gives

```
C-order  strides = (40, 8) bytes = (5*8, 8)
F-order  strides = (8, 32) bytes = (8, 4*8)
c.ravel() is a view : True
f.ravel() is a copy : True
c[2:, 1:3].strides  = (40, 8)
c[:, ::2].strides   = (40, 16)   (stride 16, not 8)
```

Read the last two lines carefully. A slice `c[2:, 1:3]` has the *same strides* as
`c`, with a different shape and starting offset: no data moved. A slice
`c[:, ::2]` has a stride of 16 bytes along the second axis instead of 8 — the
elements are the same memory, taken every other one. That is what "a slice is a
view" means at the byte level, and it is why a strided slice can be many times
slower than a contiguous one (lesson [07](./07-memory-performance.md)).

C order (row-major) means the last axis is contiguous; Fortran order means the
first is. `c.ravel()` returns a view because reading C-order-contiguous memory
in index order is a relabelling; `f.ravel()` must copy because the memory order
of `f` is not the order of the flattened index. `np.shares_memory` is the only
reliable test of which happened — never infer it from the name of the operation.

## 6. Physical interpretation

The metadata has a physical reading that is worth keeping in mind:

- **shape** is the geometry of the experiment: how many stations east and north,
  how many depth layers. If the shape is wrong, the experiment described is not
  the experiment performed.
- **dtype** is the instrument: `float64` is a 16-digit voltmeter, `float32` a
  7-digit one, `int16` a 16-bit digitiser whose whole range is 65536 counts.
  A measurement cannot be more precise than the instrument, and storing a
  `float32` result in `float64` does not add information.
- **strides** are the route through memory. They are invisible in the physics
  and dominant in the runtime.
- **nbytes** is the cost. A gravity survey of 8000 stations is negligible;
  a $10^8$-cell inversion model is the whole job.

## 7. Assumptions and regime of validity

- **`float64` is not exact.** It is a 53-bit binary significand, so `0.1` is not
  representable and `0.1 + 0.2 != 0.3` exactly. Its machine epsilon is
  $2.22 \times 10^{-16}$; `float32`'s is $1.19 \times 10^{-7}$. Every claim of the
  form "the residual is zero" in this module means "below the tolerance stated".
- **`arange` with a float step accumulates error**; use `linspace` when the
  endpoint matters.
- **`empty` may contain anything**, including NaN bit patterns. Reading before
  writing is undefined behaviour, not merely garbage.
- **`int` overflow is silent for arrays.** The demo shows
  `np.array([127], dtype=np.int8) + np.int8(1)` returning `[-128]` and
  `np.array([2^31-1], dtype=int32) + 1` returning `[-2147483648]`. NumPy emits a
  `RuntimeWarning` for the equivalent *scalar* addition, which is why the array
  case is easy to miss: the operation in a grid loop is the silent one.
- **The strides model assumes a dense buffer.** A view always has a base array
  that keeps the buffer alive; a slice of a 2 GB array keeps 2 GB alive even if
  the slice is tiny. `arr.base` and `arr.flags['OWNDATA']` are the diagnostics.
- **Memory sizes quoted here are decimal megabytes** ($10^6$ bytes), matching
  NumPy's `nbytes / 1e6`. A "400 MB" array is 381 MiB.

## 8. Python demonstration

The script is [`code/ndarray_basics_demo.py`](./code/ndarray_basics_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/ndarray_basics_demo.py
```

It builds a synthetic 2-D gravity grid and a synthetic 3-D density cube,
tabulates the dtype catalogue, and prints the stride tables. The grid and the
cube are SYNTHETIC: the anomaly is an analytic Gaussian in the station
coordinates and the cube is a linear depth trend plus a buried block, so nothing
here is an observation and the script needs no data file.

Key output (this machine, NumPy 2.5.4):

```
east  (m)     : [ 0. 25. 50. 75.] ... 1975
north (m)     : [ 0. 25. 50. 75.] ... 2475
E.shape       = (100, 80)   -> (north, east) = (100, 80)
E[:2, :3] =
[[ 0. 25. 50.]
 [ 0. 25. 50.]]
N[:2, :3] =
[[ 0.  0.  0.]
 [25. 25. 25.]]
gz.shape      = (100, 80), gz.dtype = float64
gz range      = 0.0002 .. 5.0000 mGal (synthetic)
gz.nbytes     = 64000 bytes = 0.0640 MB
gz.strides    = (640, 8) bytes = (80 columns, 1 column)
C-contiguous  = True, F-contiguous = False
```

and the cube:

```
cube.shape    = (40, 60, 60)  (depth, north, east)
cube.size     = 144000 cells
cube.dtype    = float32, itemsize = 4
cube.nbytes   = 576000 bytes = 0.576000 MB
cube[0, 0, :3] = [2400. 2400. 2400.]
cube[-1, 0, :3] = [2413.65 2413.65 2413.65]
total mass    = 0.000650 1e15 kg (cells of 25 m x 25 m x 3 m)
```

The last line is the synthetic cube's mass in units of $10^{15}$ kg, computed
with a `float64` accumulator over a `float32` array — the pattern recommended in
§3.

### What to observe

1. `E` is constant down its columns and `N` is constant along its rows: the
   `indexing="xy"` convention makes the last axis east, and this is the fact
   that every subsequent reduction in lesson [04](./04-ufuncs-reductions.md) must
   respect.
2. `gz.strides = (640, 8)`: 640 bytes to move one station north, 8 bytes to move
   one station east. The ratio is the number of columns, which is checkable by
   hand.
3. The cube is 144 000 `float32` cells and 576 000 bytes; the same cube in
   `float64` would be 1 152 000 bytes. Scale by $694$ to reach $10^8$ cells and
   you get the 400 MB and 800 MB of the dtype table.
4. `f.ravel() is a copy : True` — the *only* thing that changed between the two
   ravel calls is the memory layout, and the operation's semantics changed with
   it.

## 9. Common mistakes

1. **Assuming `arange` gives the endpoint.** `np.arange(0, 1, 0.1)` has 10
   elements and ends at 0.9; `np.linspace(0, 1, 11)` ends at 1.0.
2. **Using `empty` and reading it.** The values are whatever the allocator had.
3. **Integer division and overflow in index arithmetic.** `n // 2` is
   floor-division for integers but produces NaN for `np.nan`; `int8` counters
   wrap at 127.
4. **Mixing `meshgrid` conventions.** `indexing="ij"` and `indexing="xy"` give
   transposed grids with the same shape for square grids — an error that only
   shows up on non-square data.
5. **Trusting a `float32` sum.** Accumulate in `float64` with `dtype=` when the
   total itself is the answer.
6. **Forgetting that a view keeps the whole base alive.** Retaining a 100-element
   slice of a 1 GB array retains 1 GB.
7. **Assuming `float64` is exact for money-like decimal quantities.** It is not;
   `0.1` has no finite binary representation.
8. **Stating the axis order only in your head.** Write `(depth, north, east)` in
   the docstring of every function that takes the cube.

## 10. Real-world applications

- **Seismic data volumes** are stored as `(inline, crossline, time)` cubes of
  `float32`; a 1000 × 1000 × 2000 survey is $2 \times 10^9$ samples, 8 GB in
  `float32` and 16 GB in `float64`. The dtype decision is what makes the
  difference between processing in memory and processing in tiles.
- **Gravity and magnetic surveys** are `(station)` or `(line, station)` arrays of
  `float64`, small enough that precision is never the constraint and the grid
  geometry is the whole problem.
- **Finite-difference wavefield modelling** keeps three or four
  `(nx, ny, nz)`-shaped arrays live at once; the memory budget is set by shape
  and dtype before a single line of physics is written.
- **Satellite gravity (GRACE) and altimetry** arrive as `(time, latitude,
  longitude)` cubes; the time axis is the one that is reduced, and the shape of
  the reduction must match the shape of the time coordinate exactly.
- **Machine-learning geophysics** feeds `(batch, channel, sample)` tensors whose
  memory is governed by the same arithmetic; a factor of two in dtype is a
  factor of two in batch size.

## 11. Further reading

- **Harris, C. R., et al. "Array programming with NumPy." *Nature* 585,
  357–362 (2020).** The reference description of the ndarray data model,
  including the buffer/strides design used here. DOI 10.1038/s41586-020-2649-2.
  Level: intermediate.
- **NumPy documentation, "Array creation" and "Data type objects (dtype)".**
  [https://numpy.org](https://numpy.org) — the authoritative pages for
  `arange`/`linspace` behaviour and for the promotion rules not covered here.
  Level: beginner.
- **Oliphant, T. E. *A Guide to NumPy* (Trelgol Publishing, 2006).** The original
  book-length treatment; Chapters 3–4 cover the memory model as it is still
  implemented today. Level: intermediate.
- **van der Walt, S., Colbert, S. C., & Varoquaux, G. "The NumPy array: a
  structure for efficient numerical computation." *Computing in Science &
  Engineering* 13(2), 22–30 (2011).** A short, clear account of why strides and
  views exist. DOI 10.1109/MCSE.2011.37. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02 Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md)
  — the consequences of the view model.
- [07 Memory Layout, Strides and Cache-Aware Performance](./07-memory-performance.md)
  — the runtime consequences of stride.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — what a list costs by comparison.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md)
  — the mathematical object the 2-D array represents.
- [05-plotting-and-visualisation/01 Matplotlib Basics](../05-plotting-and-visualisation/01-matplotlib-basics.md)
  — how the shape of an array becomes the axes of a plot.

Exercises:
[`exercises/01-ndarray-basics-exercises.md`](./exercises/01-ndarray-basics-exercises.md)
and
[`exercises/01-ndarray-basics-solutions.md`](./exercises/01-ndarray-basics-solutions.md).

## Self-assessment checklist

- [ ] I can create a `(north, east)` coordinate pair with `meshgrid` and state
      the meaning of `E[j, i]`. (§2)
- [ ] I can compute `nbytes` from `shape` and `dtype` without running the code,
      and name the dtype whose $10^8$-cell model is 400 MB. (§3)
- [ ] I can explain why `float32` storage with a `float64` accumulator is often
      the right combination. (§3)
- [ ] I can reconstruct the strides of a C-ordered array from its shape and
      itemsize. (§4)
- [ ] I can predict whether `ravel` on a transposed array copies. (§5)
- [ ] I can state the axis order of my 3-D model cube in a docstring, and say
      what breaks when someone assumes the other order. (§4)
- [ ] I can describe both silent dtype traps and the check that catches each.
      (§7, §9)
- [ ] I can quote the memory of a $10^8$-cell model in `float32` and in
      `float64`. (§3)
