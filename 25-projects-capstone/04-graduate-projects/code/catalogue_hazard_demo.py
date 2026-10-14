#!/usr/bin/env python3
"""Graduate project 4: catalogue statistics and hazard inputs - the effects of
declustering and completeness on the recurrence rate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python catalogue_hazard_demo.py

Everything here is SYNTHETIC.  The catalogue is generated from a chosen
Gutenberg-Richter law with chosen aftershock sequences; no real catalogue, no
real earthquake and no published hazard curve is used.

Sections
--------
1. The synthetic catalogue and its magnitude statistics.
2. Gardner-Knopoff declustering.
3. Recurrence rates, and how much declustering and Mc move them.
4. The hazard input: rate, probability and uncertainty.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

YEARS = 50.0
B_TRUE = 1.00
MC = 3.0
N_BACKGROUND = 4000
K_AFTERSHOCK = 10.0 ** 0.8
M_REF = 4.0
OMORI_C = 0.01              # days
N_MAINSHOCK_FRAC = 0.05
BOX_KM = 200.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def magnitudes(n, b, mc):
    """Gutenberg-Richter magnitudes above mc for a given b."""
    return mc + RNG.exponential(1.0 / (b * np.log(10.0)), n)


def make_catalogue():
    t = RNG.uniform(0.0, YEARS * 365.25, N_BACKGROUND)
    m = magnitudes(N_BACKGROUND, B_TRUE, MC)
    x = RNG.uniform(0.0, BOX_KM, N_BACKGROUND)
    y = RNG.uniform(0.0, BOX_KM, N_BACKGROUND)
    order = np.argsort(m)[::-1]
    t, m, x, y = t[order], m[order], x[order], y[order]

    n_main = int(N_MAINSHOCK_FRAC * N_BACKGROUND)
    extra_t, extra_m, extra_x, extra_y = [], [], [], []
    for i in range(n_main):
        n_aft = int(min(K_AFTERSHOCK * 10.0 ** (m[i] - M_REF), 1200))
        if n_aft < 1:
            continue
        dt = OMORI_C * (RNG.random(n_aft) ** (-1.0 / 0.9) - 1.0)
        extra_t.append(t[i] + np.clip(dt, 0.0, 365.25))
        extra_m.append(magnitudes(n_aft, B_TRUE, MC))
        extra_x.append(x[i] + 5.0 * RNG.standard_normal(n_aft))
        extra_y.append(y[i] + 5.0 * RNG.standard_normal(n_aft))
    t_all = np.concatenate([t] + extra_t)
    m_all = np.concatenate([m] + extra_m)
    x_all = np.concatenate([x] + extra_x)
    y_all = np.concatenate([y] + extra_y)
    keep = t_all <= YEARS * 365.25
    return t_all[keep], m_all[keep], x_all[keep], y_all[keep], n_main


def decluster(t, m, x, y):
    """Gardner-Knopoff window declustering in time and epicentral distance."""
    order = np.argsort(m)[::-1]
    keep = np.ones(t.size, dtype=bool)
    for i in order:
        if not keep[i]:
            continue
        dt_win = 10.0 ** (0.1238 * m[i] + 0.983)
        dr_win = 10.0 ** (0.1238 * m[i] + 0.6069)
        close = ((np.abs(t - t[i]) <= dt_win)
                 & (np.hypot(x - x[i], y - y[i]) <= dr_win)
                 & (m <= m[i]) & keep)
        close[i] = False
        keep &= ~close
    return keep


def b_value(m, mc, dm=0.1):
    return float(np.log10(np.e) / (m.mean() - (mc - dm / 2.0)))


def main():
    section("1. The synthetic catalogue")
    t, m, x, y, n_main = make_catalogue()
    print(f"SYNTHETIC catalogue: {t.size} events over {YEARS:.0f} yr, "
          f"b = {B_TRUE:.2f}, Mc = {MC:.1f}")
    print(f"  {N_BACKGROUND} background events plus aftershocks of the "
          f"{n_main} largest events")
    print(f"  magnitude range {m.min():.2f} to {m.max():.2f}; "
          f"{int(np.sum(m >= 5.0))} events M >= 5, "
          f"{int(np.sum(m >= 6.0))} events M >= 6")
    counts = np.bincount(((m - MC) / 0.1).astype(int))
    mc_mode = MC + 0.1 * int(np.argmax(counts))
    print(f"  maximum-curvature Mc = {mc_mode:.1f} (assumed {MC:.1f})")
    print(f"  mean annual rate = {t.size / YEARS:.1f} events/yr above Mc")

    section("2. Gardner-Knopoff declustering")
    keep = decluster(t, m, x, y)
    print(f"  windows: dt = 10^(0.1238M+0.983) days, dr = 10^(0.1238M+0.6069) km")
    print(f"  {t.size} events -> {int(keep.sum())} independent "
          f"({100 * keep.mean():.1f}% retained; "
          f"{100 * (1 - keep.mean()):.1f}% classified as aftershocks)")
    print(f"  M >= 5: {int(np.sum((m >= 5.0) & keep))} of "
          f"{int(np.sum(m >= 5.0))} retained")
    print(f"  M >= 6: {int(np.sum((m >= 6.0) & keep))} of "
          f"{int(np.sum(m >= 6.0))} retained")

    section("3. Recurrence rates")
    for label, sel in (("raw", np.ones(t.size, dtype=bool)), ("declustered", keep)):
        b = b_value(m[sel], MC)
        sigma_b = b / np.sqrt(sel.sum())
        a = np.log10(sel.sum() / YEARS) + b * MC
        rate6 = 10.0 ** (a - b * 6.0)
        print(f"  {label:<12} N = {int(sel.sum()):5d}, b = {b:.4f} "
              f"+/- {sigma_b:.4f}, lambda(M>=6) = {rate6:.5f} /yr "
              f"(1 per {1 / rate6:.1f} yr)")
        if label == "declustered":
            rate6_d = rate6
            b_d, sigma_b_d, a_d = b, sigma_b, a
    for mc_try in (3.0, 3.5, 4.0):
        b_try = b_value(m[keep & (m >= mc_try)], mc_try)
        a_try = np.log10(np.sum(keep & (m >= mc_try)) / YEARS) + b_try * mc_try
        print(f"  Mc = {mc_try:.1f}: N = {int(np.sum(keep & (m >= mc_try))):5d}, "
              f"b = {b_try:.4f}, lambda(M>=6) = {10 ** (a_try - b_try * 6.0):.5f} /yr")
    print("  -> declustering changes the RATE substantially while leaving b nearly")
    print("     unchanged, because aftershocks obey the same GR law as the")
    print("     background; the assumed Mc changes both.  The rate is the input")
    print("     every hazard calculation consumes, so both choices belong in the")
    print("     report.")

    section("4. The hazard input")
    rate_unc = abs(np.log(10.0) * 6.0 * sigma_b_d) * rate6_d
    print(f"  declustered b = {b_d:.4f} +/- {sigma_b_d:.4f}")
    print(f"  lambda(M>=6) = {rate6_d:.5f} +/- {rate_unc:.5f} /yr "
          f"(from sigma_b alone)")
    for mag in (6.0, 7.0):
        rate_m = 10.0 ** (a_d - b_d * mag)
        unc_m = abs(np.log(10.0) * mag * sigma_b_d) * rate_m
        print(f"  lambda(M>={mag:.0f}) = {rate_m:.5f} +/- {unc_m:.5f} /yr "
              f"(1 per {1 / rate_m:.0f} yr)")
        for span in (30.0, 50.0):
            p = 1.0 - np.exp(-rate_m * span)
            p_lo = 1.0 - np.exp(-(rate_m - unc_m) * span)
            p_hi = 1.0 - np.exp(-(rate_m + unc_m) * span)
            print(f"    P(at least one M>={mag:.0f} in {span:.0f} yr) = {p:.4f} "
                  f"({p_lo:.4f} to {p_hi:.4f} from the b uncertainty alone)")
    print("  the Poisson assumption ignores the aftershock clustering that")
    print("  declustering removed from the RATE but not from the PROCESS: a")
    print("  Poisson model is appropriate only for the declustered catalogue.")


if __name__ == "__main__":
    main()
