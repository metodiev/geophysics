"""SYNTHETIC earthquake-catalogue builder shared by the pandas module demos.

**Everything this module returns is SYNTHETIC.**  The events are generated from
``numpy.random.default_rng`` with a fixed seed and a simple statistical model
(a Gutenberg-Richter magnitude distribution with a specified b-value, a
per-region rate and a log-normal depth distribution).  None of it is an
observation of the Earth, none of it is the USGS catalogue, and no number
derived from it -- including any b-value -- is a geophysical result.

The point of the generator is that it has a **known input**, so a lesson can
check that pandas recovers what was put in, and can label that recovery as a
software check rather than a finding.

The four region names (Northvale, Eastmere, Southgate, Westhold) and the
network codes (SYN-NET1, SYN-NET2) are invented for this module.  They are not
real places and not real networks.

Contents
--------
``raw_catalog()``        -- the catalogue *with* the defects a real catalogue has:
                            missing values, duplicate reports, sentinel outliers.
``clean_catalog()``      -- the same catalogue after the documented cleaning
                            policy in lesson 03 has been applied.
``station_table()``      -- a synthetic station metadata table.
``daily_event_counts()`` -- an irregular daily series (missing days).
``groundwater_series()`` -- an irregular series sampled every few days.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Fixed parameters of the SYNTHETIC generator
# --------------------------------------------------------------------------

SEED = 20261014

#: b-value *built into the generator*.  Any b-value recovered by a lesson is an
#: estimate of this number, and is illustrative only.
B_VALUE_INPUT = 1.05

#: Magnitude of completeness built into the generator (all events have M >= this).
M_MIN = 2.0

REGIONS = ("Northvale", "Eastmere", "Southgate", "Westhold")

#: Per-region rate (fraction of all events) and depth model (log-normal).
REGION_META = {
    "Northvale": dict(lat0=41.05, lon0=-121.40, rate=0.34, depth_mu=8.5,
                      depth_sigma=0.42),
    "Eastmere": dict(lat0=38.42, lon0=-122.85, rate=0.28, depth_mu=42.0,
                     depth_sigma=0.35),
    "Southgate": dict(lat0=35.12, lon0=-118.30, rate=0.22, depth_mu=12.0,
                      depth_sigma=0.45),
    "Westhold": dict(lat0=43.70, lon0=-124.10, rate=0.16, depth_mu=21.0,
                     depth_sigma=0.40),
}

#: Sentinel value written into the depth column to stand in for "no depth
#: solution was determined".  999 is *not* a depth; treating it as one is the
#: outlier bug that lesson 03 is built around.
SENTINEL_DEPTH = 999.0

AGENCY_PRIORITY = ("SYN-NET1", "SYN-NET2")

T0 = pd.Timestamp("2010-01-01")
T1 = pd.Timestamp("2019-12-31 23:59:59")


def _magnitudes(rng: np.random.Generator, n: int) -> np.ndarray:
    """Draw n magnitudes from a Gutenberg-Richter law above ``M_MIN``.

    With U uniform on (0, 1], ``M = M_MIN - log10(U)/b`` has
    ``P(M >= m) = 10^{-b (m - M_MIN)}``, i.e. exactly the GR form.
    """
    u = rng.random(n) + 1e-12          # avoid log10(0)
    return M_MIN - np.log10(u) / B_VALUE_INPUT


def _region_events(rng: np.random.Generator, region: str, n: int) -> pd.DataFrame:
    meta = REGION_META[region]
    depth = rng.lognormal(mean=np.log(meta["depth_mu"]),
                          sigma=meta["depth_sigma"], size=n)
    mag = np.round(_magnitudes(rng, n), 1)
    span_s = (T1 - T0).total_seconds()
    times = T0 + pd.to_timedelta(np.sort(rng.random(n) * span_s), unit="s")
    return pd.DataFrame(
        {
            "origin_time": times,
            "latitude": np.round(meta["lat0"] + rng.normal(0.0, 0.35, n), 4),
            "longitude": np.round(meta["lon0"] + rng.normal(0.0, 0.42, n), 4),
            "depth_km": np.round(depth, 2),
            "mw": mag,
            "mag_type": np.where(rng.random(n) < 0.8, "Mw", "mb"),
            "region": region,
            "agency": np.where(rng.random(n) < 0.65, "SYN-NET1", "SYN-NET2"),
        }
    )


def _base_catalog(n_events: int = 400, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    counts = np.floor(np.array([REGION_META[r]["rate"] for r in REGIONS]) * n_events)
    counts = counts.astype(int)
    counts[-1] += n_events - counts.sum()      # make the total exact
    parts = [_region_events(rng, region, int(k))
             for region, k in zip(REGIONS, counts)]
    df = pd.concat(parts, ignore_index=True)
    df = df.sort_values("origin_time").reset_index(drop=True)
    df.insert(0, "event_id",
              [f"S{i:04d}" for i in range(1, len(df) + 1)])
    df["n_stations"] = np.maximum(
        3, np.round(4 + 3.5 * (df["mw"] - M_MIN) + rng.normal(0, 1.5, len(df)))
    ).astype("int64")
    df["rms_s"] = np.round(rng.gamma(2.0, 0.06, len(df)), 3)
    return df


def with_defects(df: pd.DataFrame, seed: int = SEED) -> pd.DataFrame:
    """Return a copy of ``df`` with the three defect classes lesson 03 addresses.

    1. **Missing values** -- ~5 per cent of depths and ~1.5 per cent of
       magnitudes are set to NaN (no solution reported).
    2. **Sentinel outliers** -- two depths are set to ``999`` / a negative value
       and one magnitude to ``-1.0``; these are error codes, not measurements.
    3. **Duplicate reports** -- eight events are reported a second time by
       ``SYN-NET2`` under the *same* ``event_id``, so the catalogue has repeated
       rows that any per-event statistic will double-count.
    """
    rng = np.random.default_rng(seed + 7)
    out = df.copy()
    n = len(out)

    idx = rng.choice(n, size=int(0.05 * n), replace=False)
    out.loc[idx, "depth_km"] = np.nan
    idx = rng.choice(n, size=int(0.015 * n), replace=False)
    out.loc[idx, "mw"] = np.nan

    out.loc[0, "depth_km"] = SENTINEL_DEPTH
    out.loc[1, "depth_km"] = -3.0
    out.loc[2, "mw"] = -1.0

    dup = out.iloc[rng.choice(n, size=8, replace=False)].copy()
    # The second report comes from the *other* network and is a re-analysis,
    # so it differs slightly -- as real duplicate solutions do.  That is what
    # makes a stated "keep the preferred network" rule consequential.
    dup["agency"] = np.where(dup["agency"] == "SYN-NET1", "SYN-NET2", "SYN-NET1")
    dup["depth_km"] = np.round(dup["depth_km"] * 1.04 + 0.6, 2)
    dup["rms_s"] = np.round(dup["rms_s"] * 1.15, 3)
    out = pd.concat([out, dup], ignore_index=True)
    return out.sort_values("origin_time").reset_index(drop=True)


def raw_catalog(n_events: int = 400, seed: int = SEED) -> pd.DataFrame:
    """The SYNTHETIC catalogue as an analyst would receive it, defects included."""
    return with_defects(_base_catalog(n_events=n_events, seed=seed), seed=seed)


# --------------------------------------------------------------------------
# The documented cleaning policy (lesson 03 applies this step by step)
# --------------------------------------------------------------------------

def clean_catalog(n_events: int = 400, seed: int = SEED) -> pd.DataFrame:
    """The SYNTHETIC catalogue after the lesson-03 cleaning policy.

    Policy (each step is *stated* before it is applied):

    1. Drop sentinel depths (``depth_km`` outside ``[0, 700]``).  A depth of
       999 km or -3 km is a code, not a measurement.
    2. Drop events with a missing magnitude.  Magnitude is the analysis
       variable for the magnitude-frequency work, so imputing it would
       manufacture the very distribution being measured.
    3. Impute a missing *depth* with the median depth of its region.  Depth is a
       supporting variable here, and the regional median is a stated,
       conservative choice; the imputation count is reported so a reader can
       judge it.
    4. Drop duplicate ``event_id`` reports, keeping the row from the
       higher-priority network in ``AGENCY_PRIORITY``.
    """
    df = raw_catalog(n_events=n_events, seed=seed)

    df = df[df["depth_km"].isna() | df["depth_km"].between(0.0, 700.0)]
    df = df[df["mw"].notna()]
    df = df[(df["mw"] >= M_MIN) & (df["mw"] <= 9.0)]

    df = df.copy()
    for region, group in df.groupby("region", observed=True):
        df.loc[group.index[group["depth_km"].isna()], "depth_km"] = (
            group["depth_km"].median()
        )

    df["_prio"] = df["agency"].map(
        {name: i for i, name in enumerate(AGENCY_PRIORITY)}
    ).fillna(len(AGENCY_PRIORITY))
    df = df.sort_values("_prio").drop_duplicates("event_id", keep="first")
    df = df.drop(columns="_prio").sort_values("origin_time").reset_index(drop=True)
    return df


# --------------------------------------------------------------------------
# Station metadata and irregular time series
# --------------------------------------------------------------------------

def station_table() -> pd.DataFrame:
    """SYNTHETIC station metadata.  ``region`` is deliberately NON-unique.

    Fourteen stations are shared across four regions, so joining events to
    stations on ``region`` multiplies rows; lesson 05 measures that explosion.
    ``Outerisle`` is a station whose region has no events, which makes an outer
    join produce NaN on the event side.
    """
    rows = [
        ("SYN-A01", "Northvale", 41.10, -121.35, 210.0, 2008, 2024, 3),
        ("SYN-A02", "Northvale", 41.02, -121.52, 95.0, 2009, 2024, 3),
        ("SYN-A03", "Northvale", 40.94, -121.28, 640.0, 2007, 2024, 6),
        ("SYN-B01", "Eastmere", 38.45, -122.80, 55.0, 2006, 2024, 3),
        ("SYN-B02", "Eastmere", 38.38, -122.92, 120.0, 2010, 2024, 3),
        ("SYN-B03", "Eastmere", 38.51, -122.74, 30.0, 2011, 2024, 6),
        ("SYN-B04", "Eastmere", 38.30, -122.99, 410.0, 2005, 2023, 3),
        ("SYN-C01", "Southgate", 35.18, -118.24, 780.0, 2004, 2024, 3),
        ("SYN-C02", "Southgate", 35.06, -118.36, 320.0, 2009, 2024, 3),
        ("SYN-C03", "Southgate", 35.15, -118.19, 150.0, 2012, 2024, 6),
        ("SYN-D01", "Westhold", 43.74, -124.06, 25.0, 2013, 2024, 3),
        ("SYN-D02", "Westhold", 43.66, -124.15, 88.0, 2014, 2024, 3),
        ("SYN-D03", "Outerisle", 44.90, -125.40, 15.0, 2015, 2024, 3),
        ("SYN-D04", "Outerisle", 44.85, -125.31, 40.0, 2016, 2024, 3),
    ]
    return pd.DataFrame(
        rows,
        columns=["station_id", "region", "latitude", "longitude",
                 "elevation_m", "start_year", "end_year", "n_channels"],
    )


def daily_event_counts(seed: int = SEED, start: str = "2014-01-01",
                       days: int = 730) -> pd.Series:
    """SYNTHETIC daily event counts with **missing days** (irregular series).

    Roughly 8 per cent of calendar days are absent, as they would be if the
    series came from a detection process that stops on holidays or during
    outages.  The index is therefore irregular and the gaps are real gaps, not
    zeros.
    """
    rng = np.random.default_rng(seed + 11)
    full = pd.date_range(start, periods=days, freq="D")
    counts = rng.poisson(0.7, days)
    series = pd.Series(counts, index=full, name="n_events")
    keep = rng.random(days) > 0.08
    return series[keep]


def groundwater_series(seed: int = SEED, start: str = "2014-01-01",
                       days: int = 730) -> pd.Series:
    """SYNTHETIC groundwater level in metres, sampled every 3 days on average.

    The sampling interval is jittered by +/- 1 day, so the two series in lesson
    05 do not share a single timestamp and must be aligned rather than
    concatenated.
    """
    rng = np.random.default_rng(seed + 13)
    offsets = np.cumsum(rng.integers(2, 5, size=days // 3))
    idx = pd.Timestamp(start) + pd.to_timedelta(offsets, unit="D")
    idx = idx[idx < pd.Timestamp(start) + pd.Timedelta(days=days)]
    t = np.arange(len(idx)) / 365.25
    annual = 0.9 * np.sin(2 * np.pi * t - 1.1)
    trend = -0.35 * t
    level = 12.0 + trend + annual + rng.normal(0.0, 0.18, len(idx))
    return pd.Series(np.round(level, 3), index=idx, name="head_m")


def mag_to_energy_j(mw) -> float:
    """Gutenberg-Richter energy relation log10(E) = 1.5 M + 4.8 (Joules).

    Stated here because lesson 04 aggregates energy as well as counts.  It is a
    standard empirical relation, applied to SYNTHETIC magnitudes.
    """
    return np.power(10.0, 1.5 * mw + 4.8)
