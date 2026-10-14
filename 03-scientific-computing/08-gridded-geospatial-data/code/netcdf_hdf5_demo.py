"""NetCDF/HDF5: what the file is, what packing costs, what it saves.

All data in this demo are SYNTHETIC: a Gaussian gravity anomaly on a regular
lon/lat grid plus a small linear trend and seeded noise. No file is downloaded
and no real dataset is read. Every file written by the demo goes into a
throw-away directory inside this module and is deleted on exit.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python netcdf_hdf5_demo.py
Requires: numpy, netCDF4, xarray, h5py.
"""

from __future__ import annotations

import atexit
import tempfile
import warnings
from pathlib import Path

import h5py
import netCDF4 as nc
import numpy as np
import xarray as xr

# netCDF4 1.7 sets ``array.shape`` internally, which NumPy 2.5 deprecates. The
# warning comes from inside the library and says nothing about this demo.
warnings.filterwarnings("ignore", category=DeprecationWarning)

HERE = Path(__file__).resolve().parent
_SCRATCH = tempfile.TemporaryDirectory(prefix="_demo_nc_", dir=HERE)
atexit.register(_SCRATCH.cleanup)
WORK = Path(_SCRATCH.name)

RNG = np.random.default_rng(20260801)
N_LON, N_LAT, N_TIME = 161, 121, 24
LON = np.linspace(-120.0, -100.0, N_LON)   # degrees_east,  0.125 deg spacing
LAT = np.linspace(30.0, 45.0, N_LAT)       # degrees_north, 0.125 deg spacing


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def synthetic_anomaly() -> np.ndarray:
    """Gravity anomaly in mGal on (time, lat, lon), SYNTHETIC."""
    lon2d, lat2d = np.meshgrid(LON, LAT)
    gauss = 28.0 * np.exp(-(((lon2d + 110.0) / 1.4) ** 2 + ((lat2d - 37.5) / 0.9) ** 2))
    trend = 0.35 * (lat2d - 37.5) - 0.12 * (lon2d + 110.0)
    seasonal = 0.4 * np.sin(2.0 * np.pi * np.arange(N_TIME) / 12.0)
    noise = RNG.normal(0.0, 0.05, size=(N_TIME, N_LAT, N_LON))
    return (gauss[None, :, :] + trend[None, :, :] + seasonal[:, None, None] + noise)


def write_netcdf(path: Path, field: np.ndarray, *, zlib: bool,
                 complevel: int = 4, chunksizes=None,
                 packing: str | None = None,
                 fill: float | None = None) -> None:
    """Write the CF-shaped file.

    ``packing`` controls how the anomaly variable is stored:

    ``None``      float64, one value per number;
    ``"codes"``   int16 raw codes written with auto-scaling OFF, so that
                  ``scale_factor``/``add_offset`` remain pure metadata (CF);
    ``"values"``  float values written with auto-scaling ON, letting the
                  library do the packing;
    ``"double"``  int16 codes written with auto-scaling ON -- the double-packing
                  bug, included so that its cost can be measured.
    """
    ds = nc.Dataset(path, "w", format="NETCDF4")
    ds.Conventions = "CF-1.11"
    ds.title = "SYNTHETIC gravity anomaly grid (geophysics curriculum demo)"
    ds.institution = "synthetic; not an observation of the Earth"
    ds.createDimension("time", N_TIME)
    ds.createDimension("lat", N_LAT)
    ds.createDimension("lon", N_LON)

    v_lon = ds.createVariable("lon", "f8", ("lon",))
    v_lon.units, v_lon.standard_name, v_lon.axis = "degrees_east", "longitude", "X"
    v_lon[:] = LON
    v_lat = ds.createVariable("lat", "f8", ("lat",))
    v_lat.units, v_lat.standard_name, v_lat.axis = "degrees_north", "latitude", "Y"
    v_lat[:] = LAT
    t = ds.createVariable("time", "f8", ("time",))
    t.units = "days since 2020-01-01 00:00:00"
    t.calendar = "standard"
    t.axis = "T"
    t[:] = np.arange(N_TIME) * 30.4375

    kwargs = {"zlib": zlib, "complevel": complevel}
    if chunksizes is not None:
        kwargs["chunksizes"] = chunksizes
    if packing is not None:
        scale, offset = 0.01, 20.0
        v = ds.createVariable("anomaly", "i2", ("time", "lat", "lon"),
                              fill_value=np.int16(-32767), **kwargs)
        v.scale_factor = scale
        v.add_offset = offset
        if packing == "codes":
            v.set_auto_scale(False)
    else:
        v = ds.createVariable("anomaly", "f8", ("time", "lat", "lon"),
                              fill_value=None if fill is None else float(fill),
                              **kwargs)
    v.units = "mGal"
    v.standard_name = "gravity_anomaly"
    v.long_name = "SYNTHETIC free-air gravity anomaly"
    v.coordinates = "lat lon"

    data = field.copy()
    if fill is not None:
        # A synthetic "no data" block: the ocean corner of the grid.
        data[:, :20, :30] = fill
    if packing in ("codes", "double"):
        scale, offset = 0.01, 20.0
        v[:] = np.round((data - offset) / scale).astype(np.int16)
    else:
        v[:] = data
    ds.close()


def describe(path: Path) -> None:
    ds = nc.Dataset(path)
    print(f"  dims: { {k: len(v) for k, v in ds.dimensions.items()} }")
    for name, var in ds.variables.items():
        print(f"  var {name:8s} {str(var.dtype):5s} dims={var.dimensions} "
              f"attrs={sorted(var.ncattrs())}")
    print(f"  global attrs: {sorted(ds.ncattrs())}")
    ds.close()


def main() -> None:
    field = synthetic_anomaly()

    section("1. The synthetic field (SYNTHETIC data, not an observation)")
    print(f"  grid: {N_LON} lon x {N_LAT} lat x {N_TIME} time "
          f"({N_LON * N_LAT * N_TIME:,} values)")
    print(f"  lon spacing = {LON[1] - LON[0]:.4f} deg, "
          f"lat spacing = {LAT[1] - LAT[0]:.4f} deg")
    print(f"  anomaly range = {field.min():.4f} .. {field.max():.4f} mGal")
    print(f"  in-memory float64 = {field.nbytes:,} bytes")

    plain = WORK / "plain.nc"
    write_netcdf(plain, field, zlib=False)
    section("2. netCDF-4 header: dimensions, variables, attributes")
    describe(plain)
    print(f"  on-disk size, uncompressed float64 = {plain.stat().st_size:,} bytes")

    section("3. A NetCDF-4 file IS an HDF5 file (read the same file with h5py)")
    with h5py.File(plain, "r") as h5:
        print(f"  root group members: {sorted(h5.keys())}")
        print(f"  dataset keys only : {sorted(k for k in h5 if k != 'lon')[:4]} ...")
        dset = h5["anomaly"]
        print(f"  /anomaly  dtype={dset.dtype} shape={dset.shape} "
              f"chunks={dset.chunks} compression={dset.compression}")
        print(f"  /anomaly  attrs={sorted(dset.attrs)}")
        print(f"  HDF5 library version = {h5py.version.hdf5_version}")

    packed = WORK / "packed.nc"
    write_netcdf(packed, field, zlib=False, packing="codes")
    section("4. Packing: int16 + scale_factor/add_offset")
    scale, offset = 0.01, 20.0
    counts = np.round((field - offset) / scale).astype(np.int16)
    decoded = counts.astype(np.float64) * scale + offset
    err = decoded - field
    print(f"  scale_factor = {scale} mGal/count, add_offset = {offset} mGal")
    print(f"  unpack:  value = scale_factor * code + add_offset")
    print(f"  int16 code range used = {counts.min()} .. {counts.max()} "
          f"(int16 limits -32767 .. 32767)")
    print(f"  half a count = {scale / 2:.4f} mGal; ideal rms error for uniform "
          f"rounding = {scale / np.sqrt(12):.5f} mGal")
    print(f"  measured  rms error = {np.sqrt(np.mean(err ** 2)):.5f} mGal")
    print(f"  measured  max error = {np.abs(err).max():.5f} mGal")
    print(f"  on-disk size, packed int16 = {packed.stat().st_size:,} bytes "
          f"({plain.stat().st_size / packed.stat().st_size:.2f}x smaller)")
    with xr.open_dataset(packed) as dsx:
        print(f"  xarray dtype after auto-unpack = {dsx['anomaly'].dtype}, "
              f"encoding scale_factor = {dsx['anomaly'].encoding.get('scale_factor')}")
        diff = float(np.abs(dsx["anomaly"] - xr.DataArray(field,
                                                          dims=("time", "lat", "lon"))).max())
        print(f"  xarray-vs-truth max difference = {diff:.5f} mGal")

    section("4b. Letting the library pack, and what double-packing costs")
    auto = WORK / "autopack.nc"
    write_netcdf(auto, field, zlib=False, packing="values")
    with xr.open_dataset(auto) as dsx:
        err_auto = float(np.abs(dsx["anomaly"] - xr.DataArray(
            field, dims=("time", "lat", "lon"))).max())
    print(f"  writing float values with scale_factor set: max error = "
          f"{err_auto:.5f} mGal, size = {auto.stat().st_size:,} bytes")
    twice = WORK / "doublepacked.nc"
    write_netcdf(twice, field, zlib=False, packing="double")
    with xr.open_dataset(twice) as dsx:
        wrong = dsx["anomaly"].values
        err_twice = float(np.abs(wrong - field).max())
    with nc.Dataset(twice) as ds2:
        ds2.set_auto_scale(False)
        stored = np.asarray(ds2.variables["anomaly"][:]).astype(np.int64)
    outside = ~((stored >= counts.min()) & (stored <= counts.max()))
    print(f"  writing ALREADY-ROUNDED codes with scale_factor set (the bug):")
    print(f"    max error = {err_twice:.2f} mGal vs a 0.005 mGal rounding budget")
    print(f"    stored codes occupied {stored.min()} .. {stored.max()} instead of "
          f"{counts.min()} .. {counts.max()}")
    print(f"    codes outside the correct range = {int(outside.sum()):,} "
          f"({100 * outside.mean():.1f} % of the grid)")
    print("    The library packs on WRITE as well as unpacking on read, so the")
    print("    codes were packed twice. Set auto_scale=False when you store codes.")

    section("5. _FillValue is metadata, not a number")
    filled = WORK / "filled.nc"
    write_netcdf(filled, field, zlib=False, fill=-9999.0)
    with xr.open_dataset(filled) as dsx:
        n_nan = int(dsx["anomaly"].isnull().sum())
        print(f"  values masked as missing = {n_nan:,} "
              f"({100 * n_nan / field.size:.2f} % of the grid)")
        print(f"  masking is ON by default: mask_and_scale="
              f"{dsx['anomaly'].encoding is not None} -> NaN, not -9999")
    with xr.open_dataset(filled, mask_and_scale=False) as dsx:
        print(f"  with mask_and_scale=False the raw sentinel survives: "
              f"min = {float(dsx['anomaly'].min()):.1f}")

    section("6. Compression and on-disk chunking")
    sizes = {
        "none          ": plain.stat().st_size,
    }
    for level in (1, 6):
        p = WORK / f"zl{level}.nc"
        write_netcdf(p, field, zlib=True, complevel=level)
        sizes[f"zlib level {level}  "] = p.stat().st_size
    chunked = WORK / "chunked.nc"
    write_netcdf(chunked, field, zlib=True, complevel=4, chunksizes=(6, 40, 60))
    sizes["chunked 6x40x60"] = chunked.stat().st_size
    for label, size in sizes.items():
        print(f"  {label}: {size:>10,} bytes  "
              f"(ratio {plain.stat().st_size / size:5.2f}x)")
    with h5py.File(chunked, "r") as h5:
        print(f"  on-disk chunk shape = {h5['anomaly'].chunks} "
              f"(chunk bytes = {h5['anomaly'].chunks[0] * h5['anomaly'].chunks[1] * h5['anomaly'].chunks[2] * 8:,})")

    section("7. Reading a hyperslab costs only the slab")
    ds = nc.Dataset(plain)
    slab = ds.variables["anomaly"][0, :, :]
    print(f"  one time step = {slab.shape} = {slab.size:,} values of "
          f"{ds.variables['anomaly'].size:,} total "
          f"({100 * slab.size / ds.variables['anomaly'].size:.2f} %)")
    print(f"  slab mean = {slab.mean():.4f} mGal, slab std = {slab.std():.4f} mGal")
    ds.close()

    section("8. Summary of what the format actually stores")
    print("  netCDF-4 = HDF5 container + CF conventions.")
    print("  Dimensions are named and shared; variables name the dimensions")
    print("  they use; attributes carry units, standard_name and _FillValue.")
    print("  A NetCDF file is self-describing well enough to be plotted")
    print("  correctly by a program that has never seen it before.")


if __name__ == "__main__":
    main()
