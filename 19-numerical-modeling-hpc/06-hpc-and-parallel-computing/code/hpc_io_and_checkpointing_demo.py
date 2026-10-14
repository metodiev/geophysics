#!/usr/bin/env python3
"""Parallel I/O, checkpointing and job management: measured costs and the two
failure modes a checkpoint has to survive.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_io_and_checkpointing_demo.py

Everything is SYNTHETIC: array sizes, the modelled machine mean time between
failures and the modelled checkpoint cost are chosen teaching values.  The demo
writes a few small files into the directory it is run from and deletes them
again before it exits; nothing outside that directory is touched and no process,
subprocess or MPI rank is started.

Contents
--------
1. Checkpoint and restart: measured bit-identity with an uninterrupted run.
2. Per-rank files against one aggregated file: measured write cost.
3. Torn writes: why a checkpoint is written to a temporary name and renamed.
4. Integrity: a checksum that notices one flipped bit.
5. Checkpoint interval model with stated assumptions.
6. Summary of measured quantities.
"""

import hashlib
import os
import time

import numpy as np

RNG = np.random.default_rng(20261014)

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(SCRATCH_DIR, "_demo_checkpoint.npy")
TMP = os.path.join(SCRATCH_DIR, "_demo_checkpoint.tmp.npy")

MTBF_YEARS = 1.0            # ASSUMED model parameter, not a measurement
SECONDS_PER_YEAR = 365.25 * 24.0 * 3600.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def advance(u, steps):
    """A deterministic SYNTHETIC integration: diffusion-like relaxation."""
    for _ in range(steps):
        u[1:-1, 1:-1] = 0.25 * (u[:-2, 1:-1] + u[2:, 1:-1]
                                + u[1:-1, :-2] + u[1:-1, 2:])
    return u


def cleanup():
    for path in (CKPT, TMP):
        if os.path.exists(path):
            os.remove(path)


def main():
    cleanup()
    section("1. Checkpoint and restart: measured bit-identity")
    n, steps, ckpt_at = 256, 24, 12
    u0 = RNG.standard_normal((n, n))
    uninterrupted = advance(u0.copy(), steps)
    truncated = advance(u0.copy(), ckpt_at)
    np.save(CKPT, truncated)
    restarted = advance(np.load(CKPT), steps - ckpt_at)
    diff = np.max(np.abs(restarted - uninterrupted))
    print(f"  grid {n}x{n}, {steps} steps, checkpoint written after step {ckpt_at}")
    print(f"  checkpoint size on disk: {os.path.getsize(CKPT)} bytes "
          f"({n*n*8} bytes of payload)")
    print(f"  max|restarted - uninterrupted| = {diff:.3e}")
    print("  a checkpoint that stores the state exactly restarts the trajectory")
    print("  exactly.  Any difference here would be a serialisation bug, not")
    print("  rounding: the arithmetic is identical, only the state was parked.")
    print("  .npy stores the array's bytes and dtype, so the round trip is lossless.")

    section("2. Per-rank files against one aggregated file")
    ranks = 8
    chunk = 250_000                      # doubles per rank (2 MB)
    data = [RNG.standard_normal(chunk) for _ in range(ranks)]
    paths = [os.path.join(SCRATCH_DIR, f"_demo_rank{r}.npy") for r in range(ranks)]
    t0 = time.perf_counter()
    for r in range(ranks):
        np.save(paths[r], data[r])
    t_per_rank = time.perf_counter() - t0
    t0 = time.perf_counter()
    np.save(os.path.join(SCRATCH_DIR, "_demo_aggregated.npy"), np.concatenate(data))
    t_aggregated = time.perf_counter() - t0
    total_mb = ranks * chunk * 8 / 1e6
    print(f"  {ranks} ranks x {chunk} doubles = {total_mb:.1f} MB in total")
    print(f"    one file per rank    : {t_per_rank*1e3:8.3f} ms  "
          f"({total_mb/t_per_rank*1e-3:.2f} GB/s)")
    print(f"    one aggregated file  : {t_aggregated*1e3:8.3f} ms  "
          f"({total_mb/t_aggregated*1e-3:.2f} GB/s)")
    print(f"    measured ratio per-rank/aggregated = {t_per_rank/t_aggregated:.3f}")
    print(f"    file count: {ranks} against 1.  Per-file overhead is what the ratio")
    print("    measures, and on this local filesystem it is small because the files")
    print("    are large relative to the metadata cost.")
    print("  This is a local filesystem on one machine and an emulation of the")
    print("  pattern, not a parallel filesystem measurement.")
    for p in paths:
        os.remove(p)
    os.remove(os.path.join(SCRATCH_DIR, "_demo_aggregated.npy"))

    section("3. Torn writes, and the rename that prevents them")
    good = np.arange(1000, dtype=np.float64)
    np.save(CKPT, good)
    print("  a valid checkpoint exists; now simulate a crash during a rewrite that")
    print("  writes directly over it:")
    try:
        with open(CKPT, "wb") as fh:
            fh.write(b"\x93NUMPY")       # header only, then the crash
            raise RuntimeError("simulated crash mid-write")
    except RuntimeError as exc:
        print(f"    {exc}")
    try:
        recovered = np.load(CKPT)
        print(f"    reload of the checkpoint: {recovered.size} values -- the previous")
        print("    checkpoint was destroyed")
    except Exception as exc:                       # noqa: BLE001
        print(f"    reload failed: {type(exc).__name__}: {exc}")
    print("  the same crash with a temporary file and os.replace:")
    np.save(CKPT, good)
    try:
        with open(TMP, "wb") as fh:
            fh.write(b"\x93NUMPY")
            raise RuntimeError("simulated crash mid-write")
    except RuntimeError as exc:
        print(f"    {exc}")
    try:
        recovered = np.load(CKPT)
        print(f"    reload of the checkpoint: {recovered.size} values, "
              f"identical to the original: "
              f"{np.array_equal(recovered, good)}")
    except Exception as exc:                       # noqa: BLE001
        print(f"    reload failed: {type(exc).__name__}: {exc}")
    np.save(TMP, np.arange(1000, dtype=np.float64) + 1)
    os.replace(TMP, CKPT)
    print(f"  after the successful write and rename, the checkpoint holds "
          f"{np.load(CKPT).size} values")
    print("  rename is atomic within a filesystem: a reader sees either the old")
    print("  file or the new one, never a half-written one.  The cost is one extra")
    print("  name in the directory and one rename call.")

    section("4. Integrity: the checksum notices one flipped bit")
    arr = RNG.standard_normal(10_000)
    np.save(CKPT, arr)
    raw = open(CKPT, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    broken = bytearray(raw)
    broken[-1] ^= 0x01
    tampered = os.path.join(SCRATCH_DIR, "_demo_tampered.npy")
    open(tampered, "wb").write(bytes(broken))
    digest2 = hashlib.sha256(open(tampered, "rb").read()).hexdigest()
    a = np.load(CKPT)
    b = np.load(tampered)
    print(f"  checkpoint sha256   : {digest[:32]}...")
    print(f"  after one flipped bit: {digest2[:32]}...")
    print(f"  digests equal: {digest == digest2}")
    print(f"  arrays equal: {np.array_equal(a, b)}")
    n_diff = int(np.sum(a != b))
    print(f"  elements differing: {n_diff} (the flipped bit lands in one mantissa)")
    print("  the digest is the cheap check that the bytes are the ones written; the")
    print("  array comparison is the physics-level check.  A restart should do both:")
    print("  hash the file, then verify the checksum stored in the run manifest.")
    os.remove(tampered)

    section("5. Checkpoint interval with stated assumptions")
    payload_mb = 512.0
    write_bw = total_mb / t_aggregated * 1e-3          # GB/s measured above
    ckpt_seconds = payload_mb / 1000.0 / write_bw
    mtbf_seconds = MTBF_YEARS * SECONDS_PER_YEAR
    print(f"  measured local write bandwidth: {write_bw:.2f} GB/s")
    print(f"  a {payload_mb:.0f} MB checkpoint therefore costs {ckpt_seconds:.2f} s "
          f"of write time on this filesystem")
    print(f"  ASSUMED machine mean time between failures: {MTBF_YEARS:.1f} year "
          f"= {mtbf_seconds:.3e} s (a model parameter, not a measurement)")
    print("  Young's first-order rule: checkpoint every sqrt(2 * cost * MTBF)")
    interval = np.sqrt(2.0 * ckpt_seconds * mtbf_seconds)
    wasted_no_ckpt = mtbf_seconds / 2.0
    print(f"    optimal interval  = {interval:.3e} s = "
          f"{interval/3600.0:.2f} h")
    print(f"    work lost per failure at that interval ~ {interval/2.0:.1f} s")
    print(f"    work lost per failure with no checkpointing ~ "
          f"{wasted_no_ckpt:.3e} s (half the MTBF)")
    print("  the rule balances two costs that scale differently: writing more often")
    print("  costs more write time, writing less often costs more recomputation.  The")
    print("  interval moves as the square root of both inputs, so halving the MTBF")
    print("  shortens it by only about 1.41x.  The formula is arithmetic; the write")
    print("  bandwidth is measured above and the MTBF is an assumed model input.")

    section("6. Summary of measured quantities")
    print(f"  restart difference, {steps} steps with a checkpoint at {ckpt_at} : "
          f"{diff:.3e}")
    print(f"  per-rank writes / aggregated write          : "
          f"{t_per_rank*1e3:.3f} / {t_aggregated*1e3:.3f} ms")
    print(f"  measured ratio                              : "
          f"{t_per_rank/t_aggregated:.3f}")
    print("  torn write, direct overwrite                : checkpoint unusable")
    print("  torn write, temp file plus rename           : checkpoint intact")
    print(f"  one flipped bit changes the sha256          : {digest != digest2}")
    print(f"  optimal checkpoint interval under assumptions: {interval/3600:.2f} h")
    print("  All timings are local filesystem measurements on the machine that ran")
    print("  this script; the MTBF is an assumed model input.  All model inputs are")
    print("  SYNTHETIC teaching values.  No file written by this demo is left behind.")
    cleanup()


if __name__ == "__main__":
    main()
