"""Chunked (dask-backed) arrays: laziness, task graphs, out-of-core reduction.

The demo measures task counts and chunk footprints rather than wall-clock times,
so the numbers are machine-independent. All fields are SYNTHETIC. The one large
computation is built lazily from coordinate arrays, so the 512 MB array is never
materialised in full.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dask_chunking_demo.py
Requires: numpy, xarray, dask.
"""

from __future__ import annotations

import numpy as np
import xarray as xr
import dask.array as dsa

def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ntasks(*arrays) -> int:
    """Number of tasks in the merged graph of one or more dask collections."""
    merged: dict = {}
    for arr in arrays:
        merged.update(dict(arr.__dask_graph__()))
    return len(merged)


def main() -> None:
    section("1. A dask array is a recipe, not an array of numbers")
    a = dsa.random.default_rng(20260804).normal(size=(2000, 2000), chunks=(500, 500))
    print(f"  shape = {a.shape}, dtype = {a.dtype}, nbytes = {a.nbytes:,} bytes")
    print(f"  chunks = {a.chunks[0]} along axis 0, {a.chunks[1]} along axis 1")
    print(f"  npartitions = {a.npartitions}, chunk footprint = "
          f"{a.chunksize[0] * a.chunksize[1] * a.dtype.itemsize:,} bytes")
    print(f"  tasks in the graph for the source array itself = {ntasks(a)}")
    print(f"  the array has not been read: no computation has happened yet")
    total = a.sum()
    print(f"  tasks for the sum of all cells = {ntasks(total)} "
          f"(16 source chunks -> 15 partial sums -> 1 final accumulation)")
    print(f"  computed sum = {float(total.compute()):.6f} "
          f"(a dimensionless sum of standard normals)")

    section("2. Task count versus chunk size")
    print("  chunk     chunks   tasks(sum)   chunk bytes")
    for c in (2000, 1000, 500, 250, 100):
        x = dsa.zeros((2000, 2000), chunks=(c, c), dtype="float64")
        n_ch = x.npartitions
        print(f"  {c:5d}   {n_ch:6d}   {ntasks(x.sum()):9d}   "
              f"{c * c * 8:11,d}")
    print("  Total data volume is constant at 32,000,000 bytes. More chunks means")
    print("  more tasks (more Python overhead) but a smaller working set.")

    section("3. Chunk size does NOT change a deterministic reduction")
    lat = dsa.linspace(-89.0, 89.0, 800, chunks=200)
    lon = dsa.linspace(-179.0, 179.0, 500, chunks=250)
    field_det = (dsa.cos(dsa.deg2rad(lat))[:, None] ** 2
                 + 0.1 * dsa.sin(dsa.deg2rad(lon))[None, :])
    base = float(field_det.mean().compute())
    print(f"  deterministic field: mean = {base:.15f} (dimensionless)")
    for chunks in ((100, 100), (50, 50), (400, 500)):
        re = field_det.rechunk(chunks)
        value = float(re.mean().compute())
        print(f"  rechunked to {chunks}: mean = {value:.15f}, "
              f"difference = {abs(value - base):.3e}")

    section("4. ... but it DOES change dask's random numbers")
    print("  dask.random draws per chunk from a seed mixed with the chunk index,")
    print("  so the numbers themselves depend on the chunking:")
    for chunks in ((100, 100), (50, 50), (200, 200)):
        r = dsa.random.default_rng(7).normal(size=(200, 200), chunks=chunks)
        print(f"    chunks={str(chunks):12s} mean = {float(r.mean().compute()):+.12f}, "
              f"tasks = {ntasks(r)}")
    a1 = dsa.random.default_rng(7).normal(size=(200, 200), chunks=(100, 100)).compute()
    a2 = dsa.random.default_rng(7).normal(size=(200, 200), chunks=(50, 50)).compute()
    print(f"  max absolute difference between two chunkings = {np.abs(a1 - a2).max():.4f}")
    print("  Rule: generate with numpy under a fixed seed, then chunk. Never seed")
    print("  a dask generator and expect a reproducible array.")

    section("5. xarray hides the chunking until you compute")
    ts = np.arange(240)
    data = (np.cos(2 * np.pi * ts / 12.0)[:, None, None]
            + 0.5 * RNG_LAT[:, :, None].transpose(2, 0, 1))
    da = xr.DataArray(data, dims=("time", "lat", "lon"),
                      coords={"time": ts, "lat": np.arange(60), "lon": np.arange(80)},
                      name="temp", attrs={"units": "K"})
    chunked = da.chunk({"time": 60, "lat": 30, "lon": 40})
    print(f"  numpy-backed: type(da.data) = {type(da.data).__name__}, "
          f"nbytes = {da.nbytes:,}")
    print(f"  .chunk({{'time':60,'lat':30,'lon':40}}): type = "
          f"{type(chunked.data).__name__}")
    print(f"  npartitions = {chunked.data.npartitions}, "
          f"chunk footprint = {chunked.data.chunksize[0] * chunked.data.chunksize[1] * chunked.data.chunksize[2] * 8:,} bytes")
    print(f"  tasks = {ntasks(chunked.data)}")
    mean_lazy = chunked.mean()
    print(f"  lazy mean: {type(mean_lazy.data).__name__}, tasks = "
          f"{ntasks(mean_lazy.data)}")
    eager = chunked.compute()
    print(f"  after .compute(): type = {type(eager.data).__name__}, "
          f"mean = {float(eager.mean()):.6f} K")
    print(f"  same value as the numpy original: "
          f"{bool(np.isclose(float(eager.mean()), float(da.mean())))}")

    section("6. Out-of-core: a 512 MB array reduced in 8 MB pieces")
    n = 8000
    big_lat = dsa.linspace(-89.0, 89.0, n, chunks=1000)
    big_lon = dsa.linspace(-179.0, 179.0, n, chunks=1000)
    big = (dsa.cos(dsa.deg2rad(big_lat))[:, None] ** 2
           + 0.25 * dsa.sin(dsa.deg2rad(big_lon))[None, :] ** 2)
    print(f"  shape = {big.shape}, dtype = {big.dtype}, "
          f"nbytes = {big.nbytes:,} bytes = {big.nbytes / 2**20:.1f} MiB")
    print(f"  chunks = {big.chunksize}, chunk footprint = "
          f"{big.chunksize[0] * big.chunksize[1] * 8:,} bytes = "
          f"{big.chunksize[0] * big.chunksize[1] * 8 / 2**20:.1f} MiB")
    print(f"  ratio full array / chunk = {big.nbytes / (big.chunksize[0] * big.chunksize[1] * 8):.0f}x")
    stats = {"mean": big.mean(), "std": big.std(), "min": big.min(), "max": big.max()}
    print(f"  tasks for mean/std/min/max together = {ntasks(*stats.values())}")
    for name, value in stats.items():
        print(f"  {name:4s} = {float(value.compute()):.12f} (dimensionless)")
    zonal = big.mean(axis=1)
    print(f"  zonal mean over longitude: shape {zonal.shape}, "
          f"tasks = {ntasks(zonal)}, first 3 values = "
          f"{np.round(zonal[:3].compute(), 6)}")
    print("  Only one 1000 x 1000 chunk plus its partial result is resident at a")
    print("  time; the full 512 MB array never exists in memory.")

    section("6b. The same reduction on the whole array with numpy would need")
    print(f"  {big.nbytes / 2**20:.0f} MiB of RAM for the array alone, plus "
          f"{big.nbytes / 2**20:.0f} MiB for any temporary formed from it.")

    section("7. Neighbouring chunks: why diff() and rolling() cost more")
    c = dsa.zeros((1000, 1000), chunks=(250, 250))
    print(f"  source tasks = {ntasks(c)}")
    print(f"  c - c.mean() tasks = {ntasks(c - c.mean())} "
          f"(the scalar must be broadcast into every chunk)")
    print(f"  dask.roll(c, 3, axis=1) tasks = {ntasks(dsa.roll(c, 3, axis=1))}")
    print(f"  map_overlap(depth=2) tasks = "
          f"{ntasks(dsa.map_overlap(lambda b: b * 2, c, depth=2, boundary='reflect'))}")
    print("  An operation that needs neighbours must receive each chunk together")
    print("  with a halo of its neighbours, so the graph grows and each task reads")
    print("  more than its own slice.")
    x = xr.DataArray(dsa.random.default_rng(11).normal(size=(600,)),
                     dims=("t",), coords={"t": np.arange(600)}).chunk({"t": 100})
    print(f"  on a 600-point series in 6 chunks of 100:")
    print(f"    lazy .diff('t') tasks = {ntasks(x.diff('t').data)}")
    print(f"    lazy .rolling(t=11).mean() tasks = "
          f"{ntasks(x.rolling(t=11).mean().data)}")
    print(f"    rolling(t=11) drops {(11 - 1) // 2} samples at each end, i.e. "
          f"{int(x.rolling(t=11).mean().isnull().sum().compute())} NaN in total, "
          f"and the halo crosses chunk boundaries")

    section("8. Chunk layout matters for the reduction you actually need")
    t = np.arange(365)
    grid = np.cos(2 * np.pi * t / 365.0)[:, None, None] * RNG_LAT[None, :, :]
    cube = xr.DataArray(grid, dims=("time", "lat", "lon"),
                        coords={"time": t, "lat": np.arange(60), "lon": np.arange(80)})
    for chunks in ({"time": 1, "lat": 60, "lon": 80},
                   {"time": 10, "lat": 20, "lon": 20},
                   {"time": 365, "lat": 20, "lon": 20}):
        c = cube.chunk(chunks)
        footprint = c.data.chunksize[0] * c.data.chunksize[1] * c.data.chunksize[2] * 8
        trend = c.polyfit("time", 1)          # lazy: a Dataset with a new dim
        print(f"  chunks {chunks}: npartitions = {c.data.npartitions:5d}, "
              f"max chunk = {footprint:>9,} bytes, "
              f"nbytes = {c.nbytes:>9,}, "
              f"tasks for polyfit('time') = "
              f"{ntasks(*(v.data for v in trend.data_vars.values())):5d}")
    print("  Chunking along time keeps each spatial point's whole series in one")
    print("  chunk, so a per-pixel time regression needs no cross-chunk traffic.")
    print("  Chunking across time forces every chunk to be gathered.")

    section("9. dtype is a chunk-size decision too")
    f64 = cube.chunk({"time": 30, "lat": 30, "lon": 40})
    f32 = f64.astype("float32")
    foot64 = f64.data.chunksize[0] * f64.data.chunksize[1] * f64.data.chunksize[2] * 8
    foot32 = foot64 // 2
    print(f"  float64 chunk footprint = {foot64:,} bytes")
    print(f"  float32 chunk footprint = {foot32:,} bytes ({foot32 / 2**20:.2f} MiB)")
    print(f"  full array: {f64.nbytes:,} bytes (float64) -> "
          f"{f64.nbytes // 2:,} bytes (float32)")
    print(f"  float32 relative precision 2^-24 = {2 ** -24:.3e}, i.e. about 7")
    print("  significant decimal digits -- plenty for a temperature in kelvin, not")
    print("  enough for a gravity difference of 1 part in 10^8.")

    section("10. A practical rule, stated with measurements")
    for target_mib in (10, 50, 100):
        cells = int(target_mib * 2**20 / 8)
        side = int(np.sqrt(cells))
        print(f"  a {target_mib:3d} MiB float64 chunk holds {cells:,} cells, e.g. "
              f"{side} x {side}")
    print(f"  the demo's 512 MB field needs "
          f"{big.nbytes / (1000 * 1000 * 8):.0f} chunks of 1000 x 1000; "
          f"the reduction touches each one exactly once.")


RNG_LAT = np.random.default_rng(20260805).normal(size=(60, 80))

if __name__ == "__main__":
    main()
