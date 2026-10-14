"""Indexing, slicing, views versus copies, and fancy indexing.

Run:  .venv/bin/python indexing_slicing_demo.py
Requires: numpy only.

Companion to lesson 03-02-02. The record is SYNTHETIC: a (station, sample)
array built from a deterministic analytic signal plus a fixed pattern, so that
the before/after differences printed below are reproducible exactly.

This is the module's bug-hunting script. It reproduces, on purpose, the silent
corruption that a slice-as-copy assumption causes, then fixes it three ways.

The script:

1. Shows that basic slicing returns a VIEW and that writing to the slice writes
   to the original -- the silent-bug demonstration.
2. Reproduces a realistic "demean the traces" function that corrupts its input,
   measures the corruption, then repairs it with .copy().
3. Shows that fancy indexing and boolean masking return COPIES.
4. Shows reshape/transpose/ravel view-versus-copy behaviour.
5. Quantifies how many of a set of derived arrays alias the original, using
   np.shares_memory.
"""

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


NSTA, NSAMP = 6, 8


def make_record():
    """SYNTHETIC (station, sample) record: one spike per station."""
    rec = np.arange(NSTA * NSAMP, dtype=np.float64).reshape(NSTA, NSAMP)
    rec[1, 3] = 999.0
    return rec


def raw_snapshot(rec):
    return rec.copy()


# --------------------------------------------------------------------------
# 1. The slice is a view
# --------------------------------------------------------------------------

def part1_view():
    section("1. A basic slice is a VIEW: writing to it writes to the original")

    rec = make_record()
    before = raw_snapshot(rec)
    print("original rec =\n", rec)

    sub = rec[1:4, 2:5]                 # basic slicing -> view
    print("\nsub = rec[1:4, 2:5] =\n", sub)
    print("np.shares_memory(rec, sub) =", np.shares_memory(rec, sub))
    print("sub.base is None (owns data) =", sub.base is None)
    print("sub.flags['OWNDATA']       =", sub.flags["OWNDATA"])

    sub[0, 0] = -999.0                  # innocuous-looking assignment
    print("\nafter sub[0, 0] = -999.0:")
    print("rec =\n", rec)
    changed = np.argwhere(rec != before)
    print("elements of rec changed    =", changed.tolist())
    print("value written back into rec=", rec[1, 2])
    print("\n  Nothing was returned by assignment; `rec` changed because `sub`")
    print("  is the same 8*6 buffer with a different (shape, strides, offset).")


# --------------------------------------------------------------------------
# 2. The realistic corruption, and three repairs
# --------------------------------------------------------------------------

def demean_inplace_broken(rec):
    """Intended: return a demeaned COPY. Actually destroys the caller's data."""
    out = rec[:, :]                     # NOT a copy -- a view
    out -= out.mean(axis=1, keepdims=True)
    return out


def demean_copy(rec):
    out = rec.copy()
    out -= out.mean(axis=1, keepdims=True)
    return out


def demean_astype(rec):
    out = rec.astype(np.float64)        # same dtype here, but always a copy
    out -= out.mean(axis=1, keepdims=True)
    return out


def demean_newarray(rec):
    out = np.array(rec, dtype=np.float64, copy=True)
    out -= out.mean(axis=1, keepdims=True)
    return out


def part2_silent_bug():
    section("2. A demean function that silently modifies its input")

    original = make_record()
    print("original (SYNTHETIC) =\n", original)

    work = original.copy()              # keep the original for comparison
    result = demean_inplace_broken(work)
    corruption = np.abs(work - original).max()
    print("\nreturned 'copy' =\n", result)
    print("caller's array after the call =\n", work)
    print(f"max |caller_array - original| = {corruption}   <- not zero!")
    print("caller's array was supposed to be untouched.")

    for name, fn in (("rec.copy()", demean_copy),
                     ("rec.astype(float64)", demean_astype),
                     ("np.array(rec, copy=True)", demean_newarray)):
        work = original.copy()
        got = fn(work)
        same = np.array_equal(work, original)
        print(f"\n  repair [{name:<26}] caller unchanged = {same}, "
              f"output == result: {np.allclose(got, result)}")
    print("\n  All three repairs agree numerically; copy() is the cheapest to")
    print("  read. The lesson rule: any function that writes into an array it")
    print("  did not create must document whether it copies.")


# --------------------------------------------------------------------------
# 3. Fancy indexing and boolean masks copy
# --------------------------------------------------------------------------

def part3_fancy():
    section("3. Fancy indexing and boolean masking COPY")

    rec = make_record()
    idx = np.array([0, 2, 2, 5])
    picked = rec[idx]
    print(f"rec.shape = {rec.shape}, idx = {idx}")
    print("rec[idx] =\n", picked)
    print("np.shares_memory(rec, rec[idx])       =",
          np.shares_memory(rec, rec[idx]))
    print("picked.base is None (owns its data)   =", picked.base is None)

    picked[0, 0] = -1.0
    print("after picked[0, 0] = -1.0: rec[0, 0] =", rec[0, 0], "(unchanged)")

    mask = rec > 40.0
    selected = rec[mask]
    print(f"\nrec > 40 gives {int(mask.sum())} selected values")
    print(f"selected = {selected}")
    print(f"np.shares_memory(rec, rec[mask]) = {np.shares_memory(rec, rec[mask])}")

    rec[mask] = 0.0
    print("\nrow assignments through a mask DO reach the original -- the mask is")
    print("a copy but `rec[mask] = value` is a setitem on rec:")
    print("rec =\n", rec)
    print("\n  Rule: `x[i] = v` writes to x. `x[i]` on the right-hand side")
    print("  creates a new array. `rec[rec > 40] = 0` is one operation and is")
    print("  fast; `rec = rec[rec > 40]` throws away the geometry.")


# --------------------------------------------------------------------------
# 4. reshape, transpose, ravel
# --------------------------------------------------------------------------

def part4_reshaping():
    section("4. reshape, transpose and ravel: which are views?")

    a = np.arange(24, dtype=np.float64).reshape(4, 6)
    print(f"a.shape = {a.shape}, contiguous = {a.flags['C_CONTIGUOUS']}")

    rs = a.reshape(2, 3, 4)
    tp = a.T
    rv = a.ravel()
    cs = a.reshape(4, 6).T.reshape(-1)
    print(f"a.reshape(2, 3, 4) shares memory: {np.shares_memory(a, rs)}")
    print(f"a.T                shares memory: {np.shares_memory(a, tp)}")
    print(f"a.ravel()          shares memory: {np.shares_memory(a, rv)}")
    print(f"a.T.reshape(-1)    shares memory: {np.shares_memory(a, cs)}")
    print(f"a.T is C-contiguous: {tp.flags['C_CONTIGUOUS']}")

    tp[0, 0] = -7.0
    print(f"\nafter a.T[0, 0] = -7.0, a[0, 0] = {a[0, 0]}   (transpose is a view)")
    rv[1] = -8.0
    print(f"after a.ravel()[1] = -8.0, a[0, 1] = {a[0, 1]}")

    b = np.arange(12, dtype=np.float64).reshape(3, 4).T
    print(f"\nb = a3x4.T, b.flags['C_CONTIGUOUS'] = {b.flags['C_CONTIGUOUS']}")
    print(f"b.reshape(-1) shares memory with b: "
          f"{np.shares_memory(b, b.reshape(-1))}")
    print("  A non-contiguous array cannot always be reshaped without a copy;")
    print("  NumPy silently copies in that case. `np.shares_memory` is the")
    print("  only reliable test, never the type of the operation.")


# --------------------------------------------------------------------------
# 5. Audit: which derived arrays alias?
# --------------------------------------------------------------------------

def part5_alias_audit():
    section("5. An alias audit over a set of derived arrays")

    rec = make_record()
    derived = {
        "rec[1:4]": rec[1:4],
        "rec[1:4, 2:5]": rec[1:4, 2:5],
        "rec[:, ::2]": rec[:, ::2],
        "rec[...] ": rec[...],
        "rec.ravel()": rec.ravel(),
        "rec.T": rec.T,
        "rec.reshape(48)": rec.reshape(48),
        "rec[[0, 1]]": rec[[0, 1]],
        "rec[rec > 10]": rec[rec > 10],
        "rec.copy()": rec.copy(),
        "rec + 0": rec + 0,
        "rec.astype(np.float32)": rec.astype(np.float32),
    }
    n_view = n_copy = 0
    print(f"{'expression':<24}{'shares memory':>14}{'OWNDATA':>10}")
    for name, arr in derived.items():
        shares = np.shares_memory(rec, arr)
        n_view += shares
        n_copy += not shares
        print(f"{name:<24}{str(shares):>14}{str(arr.flags['OWNDATA']):>10}")
    print(f"\nviews: {n_view}   copies: {n_copy}")
    print("  Every operation that changes dtype or gathers scattered indices")
    print("  copies. Every operation that only changes shape, strides or the")
    print("  starting offset is a view. Knowing which is which is the whole of")
    print("  this lesson.")


def main():
    print("NumPy indexing and slicing -- companion to lesson 03-02-02")
    print(f"numpy version: {np.__version__}")
    part1_view()
    part2_silent_bug()
    part3_fancy()
    part4_reshaping()
    part5_alias_audit()


if __name__ == "__main__":
    main()
