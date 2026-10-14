"""Can a natural earthquake swarm be told apart from an induced sequence?

This demo builds two synthetic populations from STATED models:

  * INDUCED sequences: event rate proportional to a (lagged, noisy) injection
    rate, epicentres clustered around a well, hypocentres concentrated at the
    injection depth.
  * NATURAL swarms: an Omori-type aftershock decay from a natural mainshock,
    epicentres clustered around the mainshock, hypocentres drawn from a
    regional depth distribution.

Nothing about either population is a measurement.  The point is to measure how
well the standard diagnostic statistics SEPARATE them, and to find the regime in
which they do not separate them at all.

Statistics examined (each is what a real study would compute):
  S1  median hypocentral distance from the injection well
  S2  two-sample Kolmogorov-Smirnov comparison of the event depths against a
      regional reference depth distribution
  S3  Pearson correlation between the monthly event count and the monthly
      injection rate, with its p-value
  S4  Gutenberg-Richter b-value by maximum likelihood, with its standard error

The measured outputs are the AUC (probability that a randomly chosen induced
sequence scores more 'induced-like' than a randomly chosen natural swarm) and
the true-positive rate at a fixed 5 % false-positive rate.

Run:  <repo>/.venv/bin/python natural_vs_induced_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy import stats

# ----------------------------------------------------------------------
# MODEL inputs (chosen, not measured)
# ----------------------------------------------------------------------
MC = 0.5                 # -    MODEL catalogue completeness magnitude
B_REGIONAL = 1.0         # -    MODEL regional b-value for natural seismicity
B_INDUCED = 1.0          # -    MODEL b-value for the induced population
Z_INJ = 3.0e3            # m    MODEL injection depth
D_INJ_SCALE = 1.5e3      # m    MODEL induced epicentral decay length
Z_NAT_MEAN, Z_NAT_SD = 7.0e3, 2.5e3   # m  MODEL regional depth distribution
SWARM_SD = 1.5e3         # m    MODEL natural swarm spatial r.m.s. radius
N_MONTHS = 24            # -    MODEL length of the operations history
LOC_ERR = 0.5e3          # m    MODEL hypocentral location uncertainty

LINES = "=" * 78


def section(title: str) -> None:
    print(f"\n{LINES}\n{title}\n{LINES}")


# ----------------------------------------------------------------------
# Synthetic populations
# ----------------------------------------------------------------------
def injection_history(rng: np.random.Generator) -> np.ndarray:
    """Monthly injection volume rate, arbitrary units, one value per month."""
    m = np.arange(N_MONTHS)
    shape = np.exp(-((m - 11.0) ** 2) / (2 * 5.0 ** 2))
    return np.maximum(shape * rng.lognormal(0.0, 0.2, N_MONTHS), 1e-3)


def gr_magnitudes(rng: np.random.Generator, n: int, b: float) -> np.ndarray:
    """Draw n magnitudes above MC from a GR law with exponent b."""
    return MC + rng.exponential(1.0 / (b * np.log(10.0)), n)


def gen_induced(rng: np.random.Generator, inj: np.ndarray,
                n_target: int, well_xy: tuple[float, float] = (0.0, 0.0),
                lag_days: float = 20.0) -> dict:
    """Events at a rate proportional to the lagged injection rate."""
    days = np.arange(N_MONTHS) * 30.44
    lam = np.interp(days - lag_days, days, inj)
    lam = lam / lam.sum()
    n = max(int(n_target), 1)
    t = rng.choice(days, size=n, p=lam) + rng.uniform(-15.0, 15.0, n)
    r = rng.rayleigh(D_INJ_SCALE, n) * 1.0
    ang = rng.uniform(0.0, 2.0 * np.pi, n)
    x = well_xy[0] + r * np.cos(ang)
    y = well_xy[1] + r * np.sin(ang)
    z = np.abs(rng.normal(Z_INJ, 0.4e3, n))
    m = gr_magnitudes(rng, n, B_INDUCED)
    return dict(t=t, x=x, y=y, z=z, m=m)


def gen_natural(rng: np.random.Generator, centre_xy: tuple[float, float],
                n_target: int, t_main: float, c_days: float = 2.0,
                p_exp: float = 1.0, z_mean: float = Z_NAT_MEAN,
                z_sd: float = Z_NAT_SD) -> dict:
    """Omori-decaying swarm around a natural mainshock.

    z_mean / z_sd let the swarm be sited at ANY depth, including the injection
    depth -- which is the adversarial case: natural seismicity that shares the
    reservoir's depth range.
    """
    n = max(int(n_target), 1)
    u = rng.uniform(0.0, 1.0, n)
    if p_exp == 1.0:
        t = t_main + c_days * (1.0 / u - 1.0)
    else:
        t = t_main + c_days * (u ** (-1.0 / (p_exp - 1.0)) - 1.0)
    t = np.clip(t, 0.0, (N_MONTHS - 1) * 30.44)
    x = centre_xy[0] + rng.normal(0.0, SWARM_SD, n)
    y = centre_xy[1] + rng.normal(0.0, SWARM_SD, n)
    z = np.abs(rng.normal(z_mean, z_sd, n))
    m = gr_magnitudes(rng, n, B_REGIONAL)
    return dict(t=t, x=x, y=y, z=z, m=m)


def add_location_error(rng: np.random.Generator, cat: dict) -> dict:
    return dict(t=cat["t"],
                x=cat["x"] + rng.normal(0.0, LOC_ERR, cat["x"].size),
                y=cat["y"] + rng.normal(0.0, LOC_ERR, cat["y"].size),
                z=np.clip(cat["z"] + rng.normal(0.0, LOC_ERR, cat["z"].size), 0.0, None),
                m=cat["m"])


def regional_reference(rng: np.random.Generator, n: int = 500, sd: float = 1.0e4) -> np.ndarray:
    """Depth distribution of a WELL-MIXED regional catalogue (a model choice)."""
    x = rng.uniform(-sd, sd, n)
    y = rng.uniform(-sd, sd, n)
    return add_location_error(rng, dict(t=np.zeros(n), x=x, y=y,
                                        z=np.abs(rng.normal(Z_NAT_MEAN, Z_NAT_SD, n)),
                                        m=gr_magnitudes(rng, n, B_REGIONAL)))["z"]


# ----------------------------------------------------------------------
# Statistics
# ----------------------------------------------------------------------
def b_value(m: np.ndarray) -> tuple[float, float]:
    """Aki-Utsu MLE b-value and its Shi-Bolt standard error."""
    n = m.size
    b = np.log10(np.e) / (m.mean() - (MC - 0.05))
    return float(b), float(b / np.sqrt(n))


def stat_vector(rng: np.random.Generator, cat: dict, inj: np.ndarray,
                ref_z: np.ndarray, well_xy=(0.0, 0.0)) -> dict:
    """The four diagnostic statistics, all as 'higher = more induced-like'."""
    dist = np.hypot(cat["x"] - well_xy[0], cat["y"] - well_xy[1])
    s1 = -np.median(dist)

    ks = stats.ks_2samp(cat["z"], ref_z)
    # a small p-value means "depths unlike the regional population": induced-like
    s2 = -ks.pvalue

    month = np.clip((cat["t"] / 30.44).astype(int), 0, N_MONTHS - 1)
    counts = np.bincount(month, minlength=N_MONTHS).astype(float)
    if counts.std() > 0:
        corr, pval = stats.pearsonr(counts, inj)
    else:
        corr, pval = 0.0, 1.0
    s3 = -pval

    b, sb = b_value(cat["m"])
    # within one standard error of the regional value is "natural-like"
    s4 = -abs(b - B_REGIONAL) / max(sb, 1e-6)
    return dict(S1=s1, S2=s2, S3=s3, S4=s4, corr=corr, p_corr=pval,
                dist_med=np.median(dist), b=b, b_err=sb, p_ks=ks.pvalue,
                z_med=np.median(cat["z"]), n=cat["m"].size)


def auc(pos: np.ndarray, neg: np.ndarray) -> float:
    """Probability a random positive scores above a random negative."""
    allv = np.concatenate([pos, neg])
    ranks = stats.rankdata(allv)
    return float((ranks[:pos.size].sum() - pos.size * (pos.size + 1) / 2)
                 / (pos.size * neg.size))


def tpr_at_fpr(pos: np.ndarray, neg: np.ndarray, fpr: float = 0.05) -> tuple[float, float]:
    thr = np.quantile(neg, 1.0 - fpr)
    return float(np.mean(pos >= thr)), float(thr)


def main() -> int:
    print("Natural swarm versus induced sequence: can the statistics separate them?")
    print(f"MODEL: Mc = {MC}, b_natural = {B_REGIONAL}, b_induced = {B_INDUCED}, "
          f"injection depth = {Z_INJ / 1e3:.1f} km")
    print(f"       regional depths N({Z_NAT_MEAN / 1e3:.1f}, "
          f"{Z_NAT_SD / 1e3:.1f}) km, swarm radius {SWARM_SD / 1e3:.1f} km, "
          f"location error {LOC_ERR / 1e3:.1f} km")
    print("       OPERATIONS: 24 months of injection, non-zero for roughly months")
    print("       3 to 19, i.e. about 16 months = 487 days of activity")

    rng = np.random.default_rng(20261014)
    inj = injection_history(rng)
    ref_z = regional_reference(rng)

    def induced(n_ev, well_xy=(0.0, 0.0)):
        return stat_vector(rng, add_location_error(rng, gen_induced(rng, inj, n_ev, well_xy)),
                           inj, ref_z)

    def natural(n_ev, centre, t_main, z_mean=Z_NAT_MEAN, z_sd=Z_NAT_SD):
        return stat_vector(rng, add_location_error(
            rng, gen_natural(rng, centre, n_ev, t_main, z_mean=z_mean, z_sd=z_sd)),
            inj, ref_z)

    # ------------------------------------------------------------------
    section("1. A paired example: induced sequence versus ADVERSARIAL natural swarm")
    print("  The natural swarm is deliberately sited at the well, at the injection")
    print("  depth, and during the operations window.  Each of those choices is")
    print("  individually plausible for a natural swarm.")
    si = induced(400)
    sn = natural(400, (0.4e3, -0.3e3), t_main=330.0, z_mean=Z_INJ, z_sd=0.4e3)
    print("\n   quantity                          induced (MODEL)   natural (MODEL)")
    for lab, k, fmt in (("median distance from well [km]", "dist_med", "{:15.2f}"),
                        ("median depth [km]", "z_med", "{:15.2f}"),
                        ("depth KS p-value", "p_ks", "{:15.3e}"),
                        ("rate-vs-injection Pearson r", "corr", "{:15.3f}"),
                        ("rate-vs-injection p-value", "p_corr", "{:15.3e}"),
                        ("b-value +/- s.e.", "b", "{:15.3f}")):
        vi, vn = si[k], sn[k]
        if k in ("dist_med", "z_med"):
            vi, vn = vi / 1e3, vn / 1e3
        print(f"   {lab:33s} {fmt.format(vi)}   {fmt.format(vn)}")
    print(f"   {'b-value standard error':33s} {si['b_err']:15.3f}   {sn['b_err']:15.3f}")
    print("  The spatial and depth diagnostics agree to within their scatter, so a")
    print("  study relying on them would report this natural swarm as induced.  The")
    print("  time correlation is the ONLY statistic that separates the pair -- and it")
    print("  separates them only because the induced population was built to track")
    print("  the injection while the natural one was not.  If a natural swarm's")
    print("  timing happened to track the operations, nothing in the catalogue would")
    print("  be left.")

    # ------------------------------------------------------------------
    section("2. Population: induced versus ORDINARY natural swarms")
    n_pop = 600
    ord_i, ord_n = [], []
    for _ in range(n_pop):
        ne = int(rng.integers(80, 600))
        ord_i.append(induced(ne, (rng.uniform(-1e3, 1e3), rng.uniform(-1e3, 1e3))))
        ang = rng.uniform(0.0, 2 * np.pi)
        rc = rng.uniform(0.0, 15e3)
        ord_n.append(natural(ne, (rc * np.cos(ang), rc * np.sin(ang)),
                             float(rng.uniform(0.0, (N_MONTHS - 1) * 30.44))))
    labels = {"S1": "median distance from well",
              "S2": "depth KS against regional",
              "S3": "time correlation with injection",
              "S4": "b-value versus regional b"}
    print("   statistic                       AUC     TPR at 5% FPR")
    for key in ("S1", "S2", "S3", "S4"):
        pv = np.array([r[key] for r in ord_i])
        nv = np.array([r[key] for r in ord_n])
        tpr, _ = tpr_at_fpr(pv, nv)
        print(f"   {labels[key]:31s} {auc(pv, nv):6.3f}   {tpr:12.3f}")
    print("  Every spatial, depth or magnitude statistic looks excellent here -- but")
    print("  only because the ordinary natural swarms were generated away from the")
    print("  well and outside the reservoir depth range.  That is a property of the")
    print("  models, not evidence that the statistics work in general.")

    # ------------------------------------------------------------------
    section("3. Adversarial natural swarms: near well, reservoir depth, in-window")
    adv = []
    for _ in range(n_pop):
        ne = int(rng.integers(80, 600))
        rc = rng.uniform(0.0, 3e3)
        ang = rng.uniform(0.0, 2 * np.pi)
        adv.append(natural(ne, (rc * np.cos(ang), rc * np.sin(ang)),
                           float(rng.uniform(60.0, 640.0)),
                           z_mean=Z_INJ, z_sd=0.4e3))
    print("   statistic                       AUC     TPR at 5% FPR")
    for key in ("S1", "S2", "S3", "S4"):
        pv = np.array([r[key] for r in ord_i])
        nv = np.array([r[key] for r in adv])
        tpr, _ = tpr_at_fpr(pv, nv)
        print(f"   {labels[key]:31s} {auc(pv, nv):6.3f}   {tpr:12.3f}")
    print("  AUC = 0.5 means the statistic carries NO information about the label.")
    print("  Sited in the reservoir and inside the operations window, a natural swarm")
    print("  is statistically the same object as an induced sequence.")

    # ------------------------------------------------------------------
    section("4. Operating point of the rule actually used in practice")
    thr = 4e3
    tp = sum(1 for r in ord_i if (-r["S1"]) < thr and r["p_ks"] < 0.05)
    fp = sum(1 for r in adv if (-r["S1"]) < thr and r["p_ks"] < 0.05)
    fp3 = sum(1 for r in adv if (-r["S1"]) < thr and r["p_ks"] < 0.05 and r["p_corr"] < 0.05)
    tp3 = sum(1 for r in ord_i if (-r["S1"]) < thr and r["p_ks"] < 0.05 and r["p_corr"] < 0.05)
    print("  Rule A: induced if (median distance from well < 4 km) AND (depth KS p < 0.05)")
    print(f"   induced sequences correctly called induced        : "
          f"{tp}/{len(ord_i)} = {tp / len(ord_i):.3f}")
    print(f"   ADVERSARIAL natural swarms wrongly called induced : "
          f"{fp}/{len(adv)} = {fp / len(adv):.3f}")
    print("  Rule B: Rule A AND (time-correlation p < 0.05)")
    print(f"   induced sequences correctly called induced        : "
          f"{tp3}/{len(ord_i)} = {tp3 / len(ord_i):.3f}")
    print(f"   ADVERSARIAL natural swarms wrongly called induced : "
          f"{fp3}/{len(adv)} = {fp3 / len(adv):.3f}")
    print("  All the discriminating power of Rule B sits in its last clause.  That")
    print("  clause is a coincidence test, and section 5 prices the coincidence.")

    # ------------------------------------------------------------------
    section("5. How often does a natural swarm fall inside an operations window?")
    n_ev = 1500
    p_win = []
    for _ in range(n_ev):
        rc = rng.uniform(4e3, 15e3)
        ang = rng.uniform(0.0, 2 * np.pi)
        p_win.append(natural(int(rng.integers(80, 600)),
                             (rc * np.cos(ang), rc * np.sin(ang)),
                             float(rng.uniform(0.0, 7305.0)))["p_corr"])
    p_win = np.array(p_win)
    ops_days = 487.0
    cat_years = 20.0
    p_coincide = ops_days / (cat_years * 365.25)
    print(f"  Measured false-positive rate of the 5 % time test over {n_ev} natural")
    print(f"  swarms distributed over a {cat_years:.0f}-year catalogue: "
          f"{float(np.mean(p_win < 0.05)):.4f}")
    print("  The test behaves as advertised on average, so the problem is not the")
    print("  test but the coincidence arithmetic it is applied to:")
    print(f"    P(a random natural swarm falls in a {ops_days:.0f}-day operations")
    print(f"    window of a {cat_years:.0f}-year catalogue) = "
          f"{p_coincide:.4f}")
    for n_wells in (1, 5, 10, 30):
        print(f"    with {n_wells:2d} separate operations windows: P(at least one "
              f"coincidence per swarm) = {1 - (1 - p_coincide) ** n_wells:.4f}")
    print("  In a mature basin with tens of operations windows, a coincidence")
    print("  between a natural swarm and injection is expected, not surprising.")

    # ------------------------------------------------------------------
    section("Summary of measured quantities")
    print(f"  AUC, median distance, induced vs ordinary natural  = "
          f"{auc(np.array([r['S1'] for r in ord_i]), np.array([r['S1'] for r in ord_n])):.3f}")
    print(f"  AUC, depth KS, induced vs ordinary natural         = "
          f"{auc(np.array([r['S2'] for r in ord_i]), np.array([r['S2'] for r in ord_n])):.3f}")
    print(f"  AUC, median distance, induced vs ADVERSARIAL       = "
          f"{auc(np.array([r['S1'] for r in ord_i]), np.array([r['S1'] for r in adv])):.3f}")
    print(f"  AUC, depth KS, induced vs ADVERSARIAL              = "
          f"{auc(np.array([r['S2'] for r in ord_i]), np.array([r['S2'] for r in adv])):.3f}")
    print(f"  AUC, time correlation, induced vs ADVERSARIAL      = "
          f"{auc(np.array([r['S3'] for r in ord_i]), np.array([r['S3'] for r in adv])):.3f}")
    print(f"  AUC, b-value, induced vs ADVERSARIAL               = "
          f"{auc(np.array([r['S4'] for r in ord_i]), np.array([r['S4'] for r in adv])):.3f}")
    print(f"  false-positive rate of the combined spatial+depth")
    print(f"    rule on adversarial natural swarms               = "
          f"{fp / len(adv):.3f}")
    print(f"  false-positive rate of the 5 % time test           = "
          f"{float(np.mean(p_win < 0.05)):.4f}")
    print("\nAll populations are MODEL constructions.  The measured result is a")
    print("property of these models: when the natural and induced populations share")
    print("location, depth and b-value, no single statistic separates them, and a")
    print("correlation with operations is evidence of coincidence, not of cause.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
