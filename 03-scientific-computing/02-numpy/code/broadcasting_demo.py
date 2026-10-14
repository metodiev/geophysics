"""Broadcasting rules and vectorised thinking.

Run:  .venv/bin/python broadcasting_demo.py
Requires: numpy only.

Companion to lesson 03-02-03. All data SYNTHETIC: the traces are drawn from a
seeded generator, the station coordinates are on a regular synthetic grid.

The script:

1. Subtracts a station mean from every trace of a (station, sample) array --
   the canonical broadcasting operation -- and shows the shape bookkeeping.
2. Prints the ValueError that the naive (no-newaxis) version raises, so the
   shape-mismatch message is available verbatim.
3. Builds ann x n distance matrix in one expression and compares it with the
   double Python loop, checking they agree exactly (on values, not on timing).
4. Shows the outer-product idiom and the four broadcast-compatible shape pairs.
5. Quantifies the memory a broadcast result needs, which is the reason
   broadcasting a distance matrix does not scale to a whole survey.
"""

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


NSTA, NSAMP = 12, 500
SEED = 20261014


def part1_demean():
    section("1. Subtract the station mean from every trace")

    rng = np.random.default_rng(SEED)
    data = rng.normal(loc=0.0, scale=1.0, size=(NSTA, NSAMP))
    data += np.linspace(-3.0, 3.0, NSTA)[:, None]      # station DC offsets
    print(f"data.shape = {data.shape}  (station, sample)")
    print(f"station means (shape {data.mean(axis=1).shape}): "
          f"{np.round(data.mean(axis=1), 4)}")

    mean = data.mean(axis=1)                # shape (12,)
    print(f"mean.shape = {mean.shape} -> cannot broadcast directly against "
          f"{data.shape}")
    try:
        data - mean
    except ValueError as exc:
        print(f"ValueError: {exc}")

    demeaned = data - mean[:, np.newaxis]    # (12, 1) broadcasts against (12, 500)
    print(f"\nmean[:, None].shape = {mean[:, np.newaxis].shape}")
    print(f"demeaned.shape      = {demeaned.shape}")
    print(f"max |station mean after| = {np.abs(demeaned.mean(axis=1)).max():.3e}"
          " (float rounding only)")

    demeaned2 = data - mean.reshape(-1, 1)
    demeaned3 = data - np.expand_dims(mean, 1)
    print(f"newaxis, reshape and expand_dims agree: "
          f"{np.array_equal(demeaned, demeaned2) and np.array_equal(demeaned, demeaned3)}")
    print(f"`mean[:, None]` costs {mean.nbytes} bytes; the broadcast result "
          f"costs {demeaned.nbytes} bytes.")
    print("  Broadcasting never materialises the (12, 500) copy of `mean`;")
    print("  the subtraction reads one scalar per row.")


def part2_rules():
    section("2. The broadcasting rules, exercised")

    cases = [
        ((3, 4), (4,)),
        ((3, 4), (3, 1)),
        ((3, 1), (1, 4)),
        ((5, 1, 3), (4, 1)),
        ((2, 3, 4), (3, 1)),
        ((2, 3, 4), (4, 3)),
    ]
    for a, b in cases:
        try:
            out = np.empty(a) + np.empty(b)
            verdict = f"ok -> {out.shape}"
        except ValueError as exc:
            verdict = f"ValueError: {exc}"
        print(f"  {str(a):<12} + {str(b):<12} : {verdict}")

    print("\n  Align the shapes from the RIGHT. Each pair of axes must be equal")
    print("  or one of them must be 1. Missing leading axes are treated as 1.")
    print("  (4, 3) against (2, 3, 4) is the exception of the list: the last")
    print("  axes 4 and 3 disagree and the whole operation is rejected.")


def part3_distance_matrix():
    section("3. A distance matrix without a single Python loop")

    n = 200
    rng = np.random.default_rng(SEED + 1)
    xy = rng.uniform(0.0, 5000.0, size=(n, 2))    # SYNTHETIC station positions, m

    dx = xy[:, None, 0] - xy[None, :, 0]          # (200, 1) - (1, 200) -> (200, 200)
    dy = xy[:, None, 1] - xy[None, :, 1]
    d_bcast = np.hypot(dx, dy)
    print(f"xy.shape            = {xy.shape}")
    print(f"dx.shape            = {dx.shape}")
    print(f"d_bcast.shape       = {d_bcast.shape}")
    print(f"d_bcast.nbytes      = {d_bcast.nbytes} bytes "
          f"({d_bcast.nbytes / 1e6:.4f} MB for n = {n})")

    d_loop = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            d_loop[i, j] = float(np.hypot(xy[i, 0] - xy[j, 0],
                                          xy[i, 1] - xy[j, 1]))
    print(f"broadcast == loop   = {np.array_equal(d_bcast, d_loop)}")
    print(f"max |bcast - loop|  = {np.abs(d_bcast - d_loop).max()}")
    print(f"diagonal is zero     = {np.allclose(np.diag(d_bcast), 0.0)}")
    print(f"matrix is symmetric  = {np.allclose(d_bcast, d_bcast.T)}")

    for n_big in (2000, 20000):
        mb = n_big * n_big * 8 / 1e6
        print(f"  n = {n_big:>6}: distance matrix would need {mb / 1000:>7.2f} GB")
    print("  Broadcasting removed the loop but not the O(n^2) memory. For a")
    print("  real survey, tile the computation or use a KD-tree (lesson 08).")


def part4_outer():
    section("4. The outer-product idiom")

    depth = np.array([2.0, 4.0, 6.0, 8.0, 10.0])         # km
    slowness = np.array([0.20, 0.15, 0.12, 0.10])        # s/km
    t = depth[:, None] * slowness[None, :]               # (5, 1) * (1, 4)
    print(f"depth.shape {depth.shape} x slowness.shape {slowness.shape} "
          f"-> t.shape {t.shape}")
    print("travel-time matrix (s):\n", np.round(t, 3))
    print(f"np.outer agrees: {np.array_equal(t, np.outer(depth, slowness))}")
    print("\n  `a[:, None] * b[None, :]` is the general outer product; np.outer")
    print("  is the 1-D convenience wrapper and flattens its arguments.")


def part5_memory():
    section("5. What broadcasting costs in memory")

    print(f"{'operation':<46}{'result shape':>14}{'MB':>10}")
    rows = [
        ("(4000, 1) + (1, 4000)", (4000, 1), (1, 4000)),
        ("(4000, 1, 1) * (1, 2000, 4000)", (4000, 1, 1), (1, 2000, 4000)),
        ("gravity forward: (nobs, 1) - (1, nsrc)", (20000, 1), (1, 5000)),
    ]
    for label, a, b in rows:
        shape = np.broadcast_shapes(a, b)
        size = int(np.prod(shape))
        print(f"{label:<46}{str(shape):>14}{size * 8 / 1e6:>10.1f}")
    print("\n  The intermediate array, not the inputs, is what exhausts memory.")
    print("  The transpose trick avoids moving data, but the mask, the distance")
    print("  matrix and the design matrix are all real allocations.")


def main():
    print("NumPy broadcasting -- companion to lesson 03-02-03")
    print(f"numpy version: {np.__version__}, SEED = {SEED}")
    part1_demean()
    part2_rules()
    part3_distance_matrix()
    part4_outer()
    part5_memory()


if __name__ == "__main__":
    main()
