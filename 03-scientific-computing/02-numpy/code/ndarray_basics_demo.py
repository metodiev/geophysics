"""ndarray creation, dtypes, shapes and strides.

Run:  .venv/bin/python ndarray_basics_demo.py
Requires: numpy only.

Companion to lesson 03-02-01. Every array in this script is SYNTHETIC: the
gravity grid is an analytic bell-shaped anomaly generated from the coordinates,
the density cube is filled with a deterministic rule, and no observed dataset is
read. Timings are absent from this script by design -- it reports only sizes,
strides and dtypes, which are machine-independent facts.

The script:

1. Builds a 2-D gravity survey grid and prints its shape, strides and flags.
2. Tabulates the NumPy dtypes used in field data and the memory a 10^8-cell
   model occupies in each.
3. Measures the memory of a small 3-D density cube and extrapolates to the
   sizes that actually matter.
4. Demonstrates two dtype traps: silent integer overflow and float32
   accumulation error.
5. Shows what ``strides`` mean by building the same logical array in C and
   Fortran order.
"""

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. A gravity survey grid is an ndarray, and shape encodes geometry
# --------------------------------------------------------------------------

def part1_survey_grid():
    section("1. A 2-D gravity survey grid")

    n_east, n_north = 80, 100            # stations
    d_east = d_north = 25.0              # m, station spacing
    east = np.arange(n_east) * d_east
    north = np.arange(n_north) * d_north

    # meshgrid returns both axes on the full grid; indexing="xy" keeps the
    # conventional (east, north) reading order.
    E, N = np.meshgrid(east, north, indexing="xy")

    print(f"east  (m)     : {east[:4]} ... {east[-1]:.0f}")
    print(f"north (m)     : {north[:4]} ... {north[-1]:.0f}")
    print(f"E.shape       = {E.shape}   -> (north, east) = (100, 80)")
    print(f"N.shape       = {N.shape}")
    print(f"E[:2, :3] =\n{E[:2, :3]}")
    print(f"N[:2, :3] =\n{N[:2, :3]}")

    # SYNTHETIC gravity anomaly: one Gaussian source of 5 mGal amplitude.
    amp, e0, n0, sigma = 5.0, 1000.0, 1500.0, 400.0
    gz = amp * np.exp(-((E - e0) ** 2 + (N - n0) ** 2) / (2.0 * sigma ** 2))

    print(f"\ngz.shape      = {gz.shape}, gz.dtype = {gz.dtype}")
    print(f"gz range      = {gz.min():.4f} .. {gz.max():.4f} mGal (synthetic)")
    print(f"gz.nbytes     = {gz.nbytes} bytes = {gz.nbytes / 1e6:.4f} MB")
    print(f"gz.itemsize   = {gz.itemsize} bytes per element")
    print(f"gz.strides    = {gz.strides} bytes = "
          f"({gz.strides[0] // 8} columns, {gz.strides[1] // 8} column)")
    print(f"C-contiguous  = {gz.flags['C_CONTIGUOUS']}, "
          f"F-contiguous = {gz.flags['F_CONTIGUOUS']}")
    print("\n  Reading of the strides: moving one row down costs "
          f"{gz.strides[0]} bytes,")
    print(f"  moving one column right costs {gz.strides[1]} bytes. Row-major"
          " order is why")
    print("  traversing along the last axis is the cache-friendly direction"
          " (lesson 07).")


# --------------------------------------------------------------------------
# 2. dtypes: the choice that decides whether a model fits in RAM
# --------------------------------------------------------------------------

def part2_dtypes():
    section("2. dtype catalogue and the memory of a 10^8-cell model")

    dtypes = (
        (np.bool_, "flag / mask"),
        (np.int8, "8-bit index"),
        (np.int16, "seismic int16 sample"),
        (np.int32, "default integer"),
        (np.int64, "64-bit counter"),
        (np.float32, "single-precision model"),
        (np.float64, "default float"),
        (np.complex128, "complex spectrum"),
    )
    cells = 10 ** 8
    print(f"{'dtype':<11}{'bytes/elem':>11}{'MB for 1e8 cells':>19}"
          f"{'max representable':>34}   use")
    for dt, use in dtypes:
        info = np.iinfo(dt) if np.issubdtype(dt, np.integer) else None
        top = "" if info is None else f"{info.max}"
        print(f"{np.dtype(dt).name:<11}{np.dtype(dt).itemsize:>11}"
              f"{np.dtype(dt).itemsize * cells / 1e6:>19.1f}{top:>34}   {use}")

    print("\n  A 10^8-cell model: 800 MB in float64, 400 MB in float32.")
    print("  Single precision halves the footprint AND the memory traffic,")
    print("  which matters more than the arithmetic speed on modern CPUs.")
    print(f"  float32 eps = {np.finfo(np.float32).eps:.3e} "
          f"(precision {np.finfo(np.float32).precision} digits)")
    print(f"  float64 eps = {np.finfo(np.float64).eps:.3e} "
          f"(precision {np.finfo(np.float64).precision} digits)")
    print("  Choose float32 only when every operation you will apply keeps")
    print("  more digits than the answer needs.")


# --------------------------------------------------------------------------
# 3. A 3-D model cube
# --------------------------------------------------------------------------

def part3_model_cube():
    section("3. A 3-D density cube")

    nz, ny, nx = 40, 60, 60
    cube = np.empty((nz, ny, nx), dtype=np.float32)
    # Deterministic SYNTHETIC density: a linear depth trend plus a buried block.
    z = np.arange(nz, dtype=np.float32)[:, None, None]
    cube[...] = 2400.0 + 0.35 * z
    cube[20:24, 25:35, 25:35] = 2900.0          # dense body, 4x10x10 cells

    print(f"cube.shape    = {cube.shape}  (depth, north, east)")
    print(f"cube.size     = {cube.size} cells")
    print(f"cube.dtype    = {cube.dtype}, itemsize = {cube.itemsize}")
    print(f"cube.nbytes   = {cube.nbytes} bytes = {cube.nbytes / 1e6:.6f} MB")
    print(f"cube.strides  = {cube.strides} bytes")
    print(f"cube[0, 0, :3] = {cube[0, 0, :3]}")
    print(f"cube[-1, 0, :3] = {cube[-1, 0, :3]}")
    print(f"total mass    = {cube.sum(dtype=np.float64) * 25.0 ** 2 * 3.0 / 1e15:.6f}"
          " 1e15 kg (cells of 25 m x 25 m x 3 m)")
    print("\n  Axis order is a convention, not a law. This cube uses (z, y, x),")
    print("  the convention of most seismic and gravity modelling codes, so")
    print("  that cube[k] is a horizontal depth slice. State your convention in")
    print("  every function docstring; mismatch between (x, y, z) and (z, y, x)")
    print("  silently transposes a model and produces a plausible wrong answer.")


# --------------------------------------------------------------------------
# 4. Two dtype traps
# --------------------------------------------------------------------------

def part4_dtype_traps():
    section("4. dtype traps")

    print("(a) integer overflow is silent")
    i8 = np.array([127], dtype=np.int8)
    i32 = np.array([2 ** 31 - 1], dtype=np.int32)
    print(f"    np.array([127], dtype=int8) + int8(1)          = "
          f"{i8 + np.int8(1)}")
    print(f"    np.array([2^31-1], dtype=int32) + int32(1)     = "
          f"{i32 + np.int32(1)}")
    print(f"    int8  wraps to {np.iinfo(np.int8).min}, "
          f"int32 wraps to {np.iinfo(np.int32).min}")
    print("    No exception and no warning on the array path. NumPy emits a")
    print("    RuntimeWarning for the equivalent SCALAR addition, which is why")
    print("    the warning is so easy to miss: the operation that occurs in a")
    print("    grid loop is the silent array one.")
    print("    Use a wider dtype, or compare against np.iinfo(dt).max before")
    print("    an increment that could cross the bound.")

    print("\n(b) float32 accumulation error")
    x32 = np.full(10 ** 7, 0.1, dtype=np.float32)
    x64 = np.full(10 ** 7, 0.1, dtype=np.float64)
    s32 = float(np.sum(x32))
    s32d64 = float(np.sum(x32, dtype=np.float64))
    s64 = float(np.sum(x64))
    exact = 10 ** 7 * 0.1
    print(f"    exact                = {exact}")
    print(f"    sum(float32)         = {s32!r}   (error {abs(s32 - exact):.6g})")
    print(f"    sum(float32, dtype=f8)= {s32d64!r}  (error"
          f" {abs(s32d64 - exact):.6g})")
    print(f"    sum(float64)         = {s64!r}   (error {abs(s64 - exact):.6g})")
    print("    NumPy sums in pairs, so the error is far below the naive")
    print("    1e7 * eps32 bound; the accumulator dtype still decides the floor.")


# --------------------------------------------------------------------------
# 5. Strides, C order and Fortran order
# --------------------------------------------------------------------------

def part5_strides():
    section("5. The same array in C order and Fortran order")

    c = np.arange(20, dtype=np.float64).reshape(4, 5)
    f = np.asfortranarray(c)
    print(f"C-order  strides = {c.strides} bytes = (5*8, 8)")
    print(f"F-order  strides = {f.strides} bytes = (8, 4*8)")
    print(f"c.ravel() is a view : {c.ravel().base is not None}")
    print(f"f.ravel() is a copy : {f.ravel().base is None}")
    print(f"c[2:, 1:3].strides  = {c[2:, 1:3].strides}")
    print(f"c[:, ::2].strides   = {c[:, ::2].strides}   (stride 16, not 8)")
    print("\n  A stride is the byte step to the next element along an axis.")
    print("  Slicing never copies: it returns a new (shape, strides, offset)")
    print("  triple over the same buffer. That is the subject of lesson 02.")


def main():
    print("NumPy ndarray basics -- companion to lesson 03-02-01")
    print(f"numpy version: {np.__version__}")
    part1_survey_grid()
    part2_dtypes()
    part3_model_cube()
    part4_dtype_traps()
    part5_strides()


if __name__ == "__main__":
    main()
