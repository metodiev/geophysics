#!/usr/bin/env python3
"""Ground-motion prediction equations: median, aleatory scatter, epistemic
uncertainty, and what happens outside the fitted range.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ground_motion_models_demo.py

Everything is SYNTHETIC.  The relation, its coefficients and the scatter
components are teaching values chosen for arithmetic transparency; they are not
fitted to any real strong-motion dataset and no published coefficient is quoted.

Contents
--------
1. The median relation and its sensitivity to magnitude and distance.
2. Within-event (intra-event) and between-event (inter-event) components of the
   scatter, measured from a synthetic dataset.
3. The lognormal distribution of PGA: mean versus median, and exceedance
   probabilities against the closed form.
4. Aleatory scatter versus epistemic uncertainty of the median: what more records
   can and cannot fix.
5. Extrapolation: two relations that fit the same data equally well and disagree
   by a factor of several outside it.
6. Residual diagnostics: a missing distance term is visible in the residuals.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC ground-motion relation (chosen teaching values) ---------------
C0 = 1.411               # ln(PGA) intercept at m = 6, r = R0_KM
C1 = 1.00                # magnitude scaling per magnitude unit
C2 = 1.30                # geometric spreading coefficient
R0_KM = 5.0              # near-source saturation distance, km
SIGMA_INTRA = 0.500      # within-event standard deviation of ln PGA
SIGMA_INTER = np.sqrt(0.600 ** 2 - 0.500 ** 2)   # between-event s.d., = 0.332
SIGMA_TOTAL = np.sqrt(SIGMA_INTRA ** 2 + SIGMA_INTER ** 2)

M_SCENARIO = 6.5         # scenario magnitude for the scatter study
R_SCENARIO = 15.0        # scenario distance for the scatter study, km
N_EVENTS = 200           # synthetic events in the scatter study
N_RECORDS = 20           # records per synthetic event


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def median_pga(m, r):
    """Median PGA in g: ln PGA = c0 + c1 (m - 6) - c2 ln(r + R0)."""
    return np.exp(C0 + C1 * (np.asarray(m, dtype=float) - 6.0)
                  - C2 * np.log(np.asarray(r, dtype=float) + R0_KM))


def exceedance(z, median, sigma):
    """P(PGA > z) for a lognormal PGA with natural-log scatter sigma, via the
    normal CDF expressed with erfc from the standard library-free identity
    erfc(x) = 1 - erf(x) evaluated by math.erf when scalar."""
    import math
    return 0.5 * math.erfc((math.log(z) - math.log(median)) / (sigma * math.sqrt(2.0)))


def main():
    section("1. The median relation")
    print(f"SYNTHETIC relation: ln PGA(g) = {C0:.3f} + {C1:.2f}(m-6) - "
          f"{C2:.2f} ln(r + {R0_KM:.0f})")
    print(f"total scatter sigma = {SIGMA_TOTAL:.3f} (natural log)")
    print("\nmedian PGA (g):")
    print("      M      r=10 km   r=30 km   r=100 km")
    for m in (5.0, 6.0, 7.0, 8.0):
        print(f"    {m:4.1f}   {median_pga(m, 10.0):9.4f}   "
              f"{median_pga(m, 30.0):9.4f}   {median_pga(m, 100.0):10.4f}")
    print(f"\none magnitude unit multiplies the median by exp({C1:.2f}) = "
          f"{np.exp(C1):.3f}")
    print(f"a factor exp({C2:.2f}) = {np.exp(C2):.3f} in (r + R0) divides it by "
          f"the same factor")
    print(f"the relation is a smooth fit, not a physical law: it is calibrated")
    print(f"on a range of magnitude and distance, and outside that range it")
    print(f"extrapolates even when nothing in the numbers warns you.")

    section("2. Scatter components: within-event and between-event")
    print(f"sigma_intra (record to record, same event) = {SIGMA_INTRA:.3f}")
    print(f"sigma_inter (event to event)               = {SIGMA_INTER:.3f}")
    print(f"sigma_total = sqrt(intra^2 + inter^2)      = {SIGMA_TOTAL:.3f}")
    mu = np.log(median_pga(M_SCENARIO, R_SCENARIO))
    eta = RNG.normal(0.0, SIGMA_INTER, size=N_EVENTS)
    eps = RNG.normal(0.0, SIGMA_INTRA, size=(N_EVENTS, N_RECORDS))
    ln_pga = mu + eta[:, None] + eps
    print(f"\nscenario: M{M_SCENARIO:.1f} at {R_SCENARIO:.0f} km, "
          f"{N_EVENTS:d} events x {N_RECORDS:d} records = "
          f"{N_EVENTS * N_RECORDS:d} records")
    print(f"median of the relation              = {np.exp(mu):.4f} g")
    print(f"measured median of the ln PGA       = {np.exp(np.median(ln_pga)):.4f}"
          f" g")
    print(f"measured s.d. of all ln PGA         = {ln_pga.std(ddof=1):.3f} "
          f"(input {SIGMA_TOTAL:.3f})")
    event_means = ln_pga.mean(axis=1)
    print(f"measured s.d. of EVENT means        = {event_means.std(ddof=1):.3f} "
          f"(input {SIGMA_INTER:.3f})")
    within = ln_pga - event_means[:, None]
    print(f"measured s.d. WITHIN events         = {within.std(ddof=1):.3f} "
          f"(input {SIGMA_INTRA:.3f})")
    print("  the two components are separated by comparing the scatter of event")
    print("  means with the scatter of records inside an event.  If a model has")
    print("  no event term, a single record is still uncertain but the MEDIAN is")
    print("  not: these are different questions with different answers.")

    section("3. Lognormal PGA: mean, median and exceedance probability")
    print(f"for a lognormal variable, mean/median = exp(sigma^2/2) = "
          f"{np.exp(SIGMA_TOTAL ** 2 / 2.0):.4f}")
    med_scen = median_pga(M_SCENARIO, R_SCENARIO)
    print(f"median PGA of the scenario = {med_scen:.4f} g, so the MEAN is")
    print(f"  {med_scen * np.exp(SIGMA_TOTAL ** 2 / 2.0):.4f} g "
          f"({(np.exp(SIGMA_TOTAL ** 2 / 2.0) - 1.0) * 100:.1f} % above the "
          f"median)")
    z_design = 0.4
    p_exact = exceedance(z_design, med_scen, SIGMA_TOTAL)
    p_emp = float(np.mean(np.exp(ln_pga) > z_design))
    print(f"\nP(PGA > {z_design:.1f} g) for this scenario:")
    print(f"  closed form 1 - Phi(ln(z/median)/sigma) = {p_exact:.4f}")
    print(f"  measured over {N_EVENTS * N_RECORDS:d} records       = {p_emp:.4f}")
    print(f"  realised mean of the between-event terms = {eta.mean():+.4f} "
          f"in ln PGA")
    print(f"  its expected standard error              = "
          f"{SIGMA_INTER / np.sqrt(N_EVENTS):+.4f}")
    print("  the measured frequency is below the closed form because the drawn")
    print("  event terms averaged slightly low; a tail probability depends")
    print("  exponentially on the median, so a shift of 0.03 in ln PGA moved it")
    print(f"  by {100.0 * (p_emp / p_exact - 1.0):+.0f} %.  This is the epistemic")
    print("  uncertainty of the median showing up inside an aleatory statistic.")
    for z in (0.2, 0.4, 0.6):
        p = exceedance(z, med_scen, SIGMA_TOTAL)
        print(f"  z = {z:.1f} g: P = {p:.4f}, the level exceeded in 1 event in "
              f"{1.0 / p:.0f}")
    print("  hazard curves integrate this tail over all (m, r); the scatter is")
    print("  not a nuisance to be averaged away, it IS the tail.")

    section("4. Aleatory scatter versus epistemic uncertainty of the median")
    print(f"  estimate the median from n records of the scenario, repeat 4000")
    print("  times; the scatter of the estimate is sigma/sqrt(n):")
    print("      n records   s.d. of the median estimate   sigma/sqrt(n)")
    for n in (5, 20, 100):
        est = np.empty(4000)
        for i in range(4000):
            est[i] = np.mean(mu + RNG.normal(0.0, SIGMA_TOTAL, size=n))
        print(f"      {n:9d}   {est.std(ddof=1):25.4f}   "
              f"{SIGMA_TOTAL / np.sqrt(n):14.4f}")
    print("  more records sharpen the median and leave the scatter untouched.")
    print("  Confusing the two is the classic error: a well-recorded earthquake")
    print("  does not make the ground motion of the next one predictable.")

    section("5. Extrapolation: two fits, same data, different worlds")
    m_data = np.arange(4.5, 6.01, 0.25)
    ln_obs = np.log(median_pga(m_data, 20.0)) + RNG.normal(
        0.0, 0.02, size=m_data.size)
    lin = np.polyfit(m_data, ln_obs, 1)
    logm = np.polyfit(np.log(m_data), ln_obs, 1)
    rms_lin = float(np.sqrt(np.mean((np.polyval(lin, m_data) - ln_obs) ** 2)))
    rms_log = float(np.sqrt(np.mean(
        (np.polyval(logm, np.log(m_data)) - ln_obs) ** 2)))
    print(f"  synthetic data: {m_data.size:d} points, M{m_data[0]:.1f}-"
          f"{m_data[-1]:.1f} at 20 km, noise s.d. 0.02 in ln PGA")
    print(f"  model A, linear in m : ln PGA = {lin[0]:.4f} m + {lin[1]:.4f}, "
          f"in-range RMS = {rms_lin:.4f}")
    print(f"  model B, linear in ln m: ln PGA = {logm[0]:.4f} ln m + "
          f"{logm[1]:.4f}, in-range RMS = {rms_log:.4f}")
    in_range_gap = float(np.max(np.abs(
        np.polyval(lin, m_data) - np.polyval(logm, np.log(m_data)))))
    print(f"  largest disagreement between the two models INSIDE the data range:")
    print(f"    {in_range_gap:.4f} in ln PGA = a factor "
          f"{np.exp(in_range_gap):.3f}, comparable to the noise")
    p_lin = float(np.exp(np.polyval(lin, 8.0)))
    p_log = float(np.exp(np.polyval(logm, np.log(8.0))))
    print(f"\n  prediction at M8.0, 20 km (outside the fitted range):")
    print(f"    model A (linear in m)  : {p_lin:.4f} g")
    print(f"    model B (linear in ln m): {p_log:.4f} g")
    print(f"    ratio                  : {p_lin / p_log:.2f}")
    print("  the data cannot choose between them: inside the range they agree to")
    print("  within the scatter, and outside it they differ by tens of per cent")
    print("  per magnitude unit.  Extrapolated hazard inherits a model choice,")
    print("  and no amount of in-range data removes it.")

    section("6. Residual diagnostics: a missing distance term is visible")
    m_grid = np.arange(4.0, 7.01, 0.25)
    r_grid = np.array([5.0, 8.0, 12.0, 18.0, 25.0, 35.0, 50.0, 70.0, 100.0])
    mm, rr = np.meshgrid(m_grid, r_grid, indexing="ij")
    ln_data = np.log(median_pga(mm.ravel(), rr.ravel())) + RNG.normal(
        0.0, 0.05, size=mm.size)
    ln_r = np.log(rr.ravel() + R0_KM)
    # model A: magnitude only (the distance term is omitted)
    A = np.column_stack([np.ones(ln_data.size), mm.ravel()])
    coef_a, *_ = np.linalg.lstsq(A, ln_data, rcond=None)
    res_a = ln_data - A @ coef_a
    # model B: magnitude plus a free distance coefficient
    Bm = np.column_stack([np.ones(ln_data.size), mm.ravel(), ln_r])
    coef_b, *_ = np.linalg.lstsq(Bm, ln_data, rcond=None)
    res_b = ln_data - Bm @ coef_b
    r_a = float(np.corrcoef(res_a, ln_r)[0, 1])
    r_b = float(np.corrcoef(res_b, ln_r)[0, 1])
    print(f"  {ln_data.size:d} synthetic data points on a (m, r) grid, "
          f"noise s.d. 0.05")
    print("      model                              RMS residual   corr(residual, "
          "ln r)")
    print(f"      magnitude only                     {np.sqrt(np.mean(res_a ** 2)):12.4f}"
          f"   {r_a:18.3f}")
    print(f"      magnitude + free distance term     {np.sqrt(np.mean(res_b ** 2)):12.4f}"
          f"   {r_b:18.3f}")
    print(f"  the fitted distance coefficient is {coef_b[2]:.3f} "
          f"(true -{C2:.2f})")
    print("  a wrong functional form leaves structure in the residuals, and the")
    print("  structure is detectable.  Epistemic uncertainty of a ground-motion")
    print("  model is therefore of two kinds: the part the data can rule out, and")
    print("  the part only extrapolation can reveal.")


if __name__ == "__main__":
    main()
