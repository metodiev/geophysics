"""Performance, dtypes and when to leave pandas.

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/performance_dtypes_demo.py
Requires: pandas and numpy (installed in the project venv).

Companion to lesson 03-04-07.  The table is SYNTHETIC (see
``synthetic_catalog.py`` for the generator used by the other lessons; this demo
builds a larger table with the same columns by the same rules).

**Timings are machine- and load-dependent.**  The ratios between the two arms of
each comparison are the lesson; the absolute milliseconds are not, and no timing
below should be quoted as a property of pandas.

Demonstrates:

1. Where the memory actually goes: a per-column, deep memory table.
2. Text -> ``category``, and the measured saving.
3. Downcasting floats, and the precision cost that comes with it.
4. A Python loop versus a vectorised mask on the same task.
5. Leaving pandas for NumPy (a moving average) and for a database (a filtered
   aggregate), with the measured difference and the reason.
"""

from __future__ import annotations

import sqlite3
import time

import numpy as np
import pandas as pd

N_ROWS = 600_000
SEED = 20261014


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def best_of(fn, repeats=3):
    """Return (best_seconds, result) over ``repeats`` calls of ``fn``."""
    times = []
    result = None
    for _ in range(repeats):
        t0 = time.perf_counter()
        result = fn()
        times.append(time.perf_counter() - t0)
    return min(times), result


def build(n: int = N_ROWS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    return pd.DataFrame(
        {
            "event_id": [f"S{i:06d}" for i in range(n)],
            "region": rng.choice(list(("Northvale", "Eastmere", "Southgate",
                                       "Westhold")), n),
            "agency": rng.choice(["SYN-NET1", "SYN-NET2"], n),
            "mag_type": rng.choice(["Mw", "mb"], n),
            "mw": np.round(2.0 - 2.0 * np.log10(rng.random(n)), 2),
            "depth_km": np.round(rng.lognormal(2.5, 0.8, n), 2),
            "n_stations": rng.integers(3, 15, n),
        }
    )


def part1_memory_anatomy():
    section("1. Where the memory goes")
    df = build()
    mb = df.memory_usage(deep=True)
    table = pd.DataFrame({"bytes": mb, "MB": (mb / 1e6).round(1)})
    table["share_%"] = (100 * mb / mb.sum()).round(1)
    print(f"  rows: {len(df):,}")
    print(table.to_string())
    print()
    print(f"  total deep memory: {mb.sum() / 1e6:.1f} MB")
    print("  Four text columns hold most of it. Each Python str is a separate")
    print("  object: an 8-byte pointer in the column plus roughly 50-60 bytes")
    print("  of object overhead and characters. A column of 600,000 short")
    print("  strings costs tens of megabytes to store a handful of distinct")
    print("  values.")


def part2_category():
    section("2. Text -> category: the largest single saving")
    df = build()
    before = df.memory_usage(deep=True)
    for col in ("region", "agency", "mag_type"):
        print(f"  {col}: {df[col].nunique()} distinct values in "
              f"{len(df):,} rows")
    categorised = df.copy()
    for col in ("region", "agency", "mag_type"):
        categorised[col] = categorised[col].astype("category")
    after = categorised.memory_usage(deep=True)
    cmp = pd.DataFrame({
        "before_MB": (before / 1e6).round(2),
        "after_MB": (after / 1e6).round(2),
    })
    cmp["saving"] = (1 - cmp["after_MB"] / cmp["before_MB"]).round(3)
    cmp = cmp.drop(index="Index")
    print()
    print(cmp.to_string())
    print()
    print("  event_id is untouched at 0.000 saving because it has "
          f"{df['event_id'].nunique():,} distinct")
    print("  values -- categorising a high-cardinality identifier would store a")
    print("  label per row and gain nothing. category is for columns whose")
    print("  distinct-value count is small and repeated.")
    print()
    total_before, total_after = before.sum(), after.sum()
    print(f"  total: {total_before / 1e6:.1f} MB -> "
          f"{total_after / 1e6:.1f} MB  "
          f"({total_before / total_after:.2f}x smaller)")
    print()
    print("  A category stores each distinct label ONCE and keeps a small")
    print("  integer code per row. The cost is that the label set is fixed at")
    print("  conversion time: adding a new category later requires")
    print("  .cat.add_categories(), and operations that produce new labels")
    print("  between categories raise rather than silently widen the set.")
    print()
    print("  category dtype codes:")
    print(categorised["region"].cat.codes.head(5).to_string())
    print(f"  categories of region: {list(categorised['region'].cat.categories)}")
    print()
    print("  Note that text is stored as the dedicated 'str' dtype in pandas 3")
    print(f"  (not 'object'): df['region'].dtype -> {df['region'].dtype!r}")
    print("  Tutorials written for pandas 1.x will show 'object' here.")


def part3_downcast():
    section("3. Downcasting: less memory, less precision")
    df = build()
    dtype_map = {"mw": "float32", "depth_km": "float32"}
    small = df.astype({k: v for k, v in dtype_map.items() if k in df.columns})
    before = df.memory_usage(deep=True)
    after = small.memory_usage(deep=True)
    cmp = pd.DataFrame({
        "dtype_before": df.dtypes.astype(str),
        "dtype_after": small.dtypes.astype(str),
        "before_MB": (before / 1e6).round(2),
        "after_MB": (after / 1e6).round(2),
    }).drop(index="Index")
    print(cmp.to_string())
    print()
    print(f"  total: {before.sum() / 1e6:.1f} MB -> "
          f"{after.sum() / 1e6:.1f} MB  "
          f"({before.sum() / after.sum():.2f}x smaller)")
    print()
    print("  The precision cost, measured on the magnitude column:")
    diff = (small["mw"].astype("float64") - df["mw"]).abs()
    print(f"    largest absolute change   : {diff.max():.3e} magnitudes")
    print(f"    rows changed at all       : {int((diff > 0).sum()):,} of "
          f"{len(df):,}")
    exact = bool((small["mw"] == df["mw"]).all())
    print(f"    exact equality preserved  : {exact}")
    print()
    print("  float32 carries about 7 significant decimal digits, so a")
    print("  magnitude rounded to 0.1 is represented with error around 1e-7.")
    print("  That is harmless for plotting and fatal for code that groups by")
    print("  exact float equality, which is why binning must go through")
    print("  pd.cut or a rounded integer key rather than ==.")


def part4_loop_versus_vectorised():
    section("4. A Python loop versus a vectorised mask")
    df = build()
    depths = df["depth_km"].to_numpy()

    def loop_way():
        total = 0.0
        for d in depths:
            if d > 30.0:
                total += d
        return total

    def vector_way():
        mask = df["depth_km"] > 30.0
        return df.loc[mask, "depth_km"].sum()

    def apply_way():
        return df["region"].apply(len)

    def str_way():
        return df["region"].str.len()

    t_loop, v_loop = best_of(loop_way)
    t_vec, v_vec = best_of(vector_way)
    print(f"  both compute the sum of depths above 30 km over {len(df):,} rows")
    print(f"    Python loop, iterating  : {t_loop * 1e3:8.2f} ms")
    print(f"    pandas boolean mask     : {t_vec * 1e3:8.2f} ms")
    print(f"    ratio                   : {t_loop / t_vec:8.2f}x")
    print()
    print(f"    loop result   : {v_loop!r}")
    print(f"    vector result : {v_vec!r}")
    print(f"    absolute difference : {abs(v_loop - v_vec):.3e}")
    print(f"    relative difference : {abs(v_loop - v_vec) / abs(v_vec):.3e}")
    print()
    print("  Equal to about 15 significant figures, and not bit-for-bit equal:")
    print("  the loop adds one number at a time, the mask sums in a different")
    print("  order, and floating-point addition is not associative. That is a")
    print("  property of the arithmetic, not an error in either arm, and it is")
    print("  why comparisons of floats use a tolerance rather than ==.")
    print()
    print("  The loop does the same arithmetic one element at a time in the")
    print("  interpreter. The mask pushes the whole comparison into compiled")
    print("  code over a contiguous buffer. Neither is 'more correct'; one is")
    print("  simply doing per-element work that does not need to be done per")
    print("  element.")
    print()
    print("  The same rule inside pandas -- prefer the specialised accessor:")
    t_apply, v_apply = best_of(apply_way)
    t_str, v_str = best_of(str_way)
    print(f"    Series.apply(len)  : {t_apply * 1e3:8.2f} ms")
    print(f"    Series.str.len()   : {t_str * 1e3:8.2f} ms")
    print(f"    ratio              : {t_apply / t_str:8.2f}x   "
          f"over {len(df):,} strings")
    print(f"    results identical  : {bool((v_apply == v_str).all())}")
    print("  apply() calls back into Python once per element; the .str accessor")
    print("  runs the loop in its own compiled layer. Same answer, fewer trips")
    print("  across the interpreter boundary.")
    print()
    print("  Not every accessor wins on every task, though: measured on this")
    print("  machine and this pandas build, .str.upper() was actually slower")
    print("  than .apply(str.upper) for these short repeated labels, because")
    print("  upper() has to build a new string object either way. The rule is")
    print("  'measure the operation you have', not 'the accessor is always")
    print("  faster'.")


def part5_leave_for_numpy():
    section("5. Leaving pandas for NumPy: a moving average")
    df = build()
    window = 200
    depths = df["depth_km"].to_numpy()

    def pandas_way():
        return df["depth_km"].rolling(window).mean().to_numpy()

    def convolve_way():
        kernel = np.ones(window) / window
        return np.convolve(depths, kernel, mode="valid")

    def cumsum_way():
        cum = np.cumsum(np.insert(depths, 0, 0.0))
        return (cum[window:] - cum[:-window]) / window

    t_pd, v_pd = best_of(pandas_way)
    t_cv, v_cv = best_of(convolve_way)
    t_cs, v_cs = best_of(cumsum_way)
    print(f"  {window}-point moving average of depth, {len(df):,} points")
    print(f"    Series.rolling({window}).mean()      : {t_pd * 1e3:8.2f} ms   "
          "O(n) running sum")
    print(f"    numpy.convolve(depths, ones/{window}) : {t_cv * 1e3:8.2f} ms   "
          "O(n*window) dot products")
    print(f"    numpy cumsum difference           : {t_cs * 1e3:8.2f} ms   "
          "O(n) running sum")
    print()
    pd_tail = v_pd[window - 1:]
    print(f"    rolling vs convolve, max |diff| : "
          f"{float(np.nanmax(np.abs(pd_tail - v_cv))):.3e} km")
    print(f"    rolling vs cumsum,   max |diff| : "
          f"{float(np.nanmax(np.abs(pd_tail - v_cs))):.3e} km")
    print(f"    windows compared                : {len(v_cv):,}")
    print()
    print("  The result that matters here is the one that contradicts the")
    print("  folklore. The *naive* NumPy route is the slowest of the three,")
    print("  because convolve evaluates a 200-point dot product at every one of")
    print(f"  {len(depths):,} positions -- about "
          f"{len(depths) * window / 1e9:.1f} G multiply-adds.")
    print("  pandas' rolling uses a running sum, so it is O(n), and it beats")
    print("  convolve. Matching that algorithm in NumPy with a cumulative sum")
    print("  is again the fastest of the three.")
    print()
    print("  So the lesson is not 'NumPy is faster than pandas'. It is: the")
    print("  algorithm dominates, the library is second-order, and a claimed")
    print("  speed-up must be measured on the task you actually have. The")
    print("  differences between these three arms are far larger than the")
    print("  differences between the two libraries running the same algorithm.")


def part6_leave_for_database():
    section("6. Leaving pandas for a database: a filtered aggregate")
    df = build()
    con = sqlite3.connect(":memory:")
    df.to_sql("events", con, index=False)

    def pandas_way():
        return (df[df["depth_km"] > 30.0]
                .groupby("region", observed=True)["mw"]
                .agg(["count", "mean"]))

    def sql_way():
        cur = con.execute(
            "SELECT region, COUNT(*) AS n, AVG(mw) AS mean_mw "
            "FROM events WHERE depth_km > 30.0 GROUP BY region"
        )
        return pd.DataFrame(cur.fetchall(),
                            columns=["region", "n", "mean_mw"])

    t_pd, v_pd = best_of(pandas_way)
    t_sql, v_sql = best_of(sql_way)
    print(f"  table: {len(df):,} rows loaded into an in-memory SQLite database")
    print(f"    pandas mask + groupby  : {t_pd * 1e3:8.2f} ms")
    print(f"    SQL GROUP BY (fetch)   : {t_sql * 1e3:8.2f} ms")
    print()
    print("  SQL result:")
    print(v_sql.round(4).to_string(index=False))
    print()
    print("  pandas result:")
    print(v_pd.round(4).to_string())
    print()
    print("  On a table this size the two are comparable and the")
    print("  implementation detail decides. The argument for the database is")
    print("  not this benchmark; it is that the filter and the aggregate happen")
    print("  inside the engine, so a table of 10^9 rows never has to be brought")
    print("  into memory and a query over it touches only the columns it names.")
    print("  When the data no longer fit in RAM, that is the moment pandas")
    print("  stops being the right tool -- not a moment earlier.")
    con.close()


def part7_rules():
    section("7. Working rules")
    rules = [
        "Measure before you optimise: memory_usage(deep=True) and a best-of-three, not a guess.",
        "Convert low-cardinality text columns to category, and state that the label set is fixed.",
        "Keep the dtype that preserves the measurement; check what a downcast does to equality first.",
        "Replace per-row Python loops with masks, group-by and vectorised string/date methods.",
        "Drop to NumPy when the output is a raw array and the index is not part of the question.",
        "Keep pandas when alignment, NaN semantics or a time index are part of the question.",
        "Move to a database or a chunked reader when the data stop fitting in memory.",
    ]
    for r in rules:
        print("  - " + r)


if __name__ == "__main__":
    print("SYNTHETIC table: generated in-code, not an observation of the Earth")
    print("and not the USGS catalogue.  Timings are machine-dependent; only")
    print("their ratios are meaningful.")
    part1_memory_anatomy()
    part2_category()
    part3_downcast()
    part4_loop_versus_vectorised()
    part5_leave_for_numpy()
    part6_leave_for_database()
    part7_rules()
