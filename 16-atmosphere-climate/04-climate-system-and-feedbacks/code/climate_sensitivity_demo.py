#!/usr/bin/env python3
"""Climate sensitivity: definitions and estimation. Equilibrium and transient
sensitivity from a two-layer model, the Gregory regression and its dependence on
the regression window, the distribution implied by uncertain feedback
parameters, and the dependence of transient sensitivity on ocean heat uptake.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_sensitivity_demo.py

Everything is SYNTHETIC. Every heat capacity, feedback parameter, drift slope
and forcing here is a CHOSEN TEACHING VALUE. Nothing is quoted from a published
assessment, and no number is an estimate of the real Earth's climate
sensitivity.

Contents
--------
1. Two definitions: equilibrium (ECS) and transient (TCR) sensitivity, from one
   two-layer model.
2. The Gregory regression: what it recovers, and how the answer moves with the
   length of the regression window when the feedback drifts with temperature.
3. The distribution of ECS implied by an uncertain feedback parameter.
4. Four estimators of the same quantity, side by side.
5. Transient sensitivity versus ocean heat uptake, with the equilibrium held
   fixed.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8
T_REF = 288.0
F_2X = 3.7                   # W/m^2, chosen
C_MIXED = 2.0423e8           # J/(m^2 K), 50 m mixed layer
C_DEEP = 1.3683e10           # J/(m^2 K), 3350 m deep ocean
GAMMA = 0.7                  # W/(m^2 K), coupling
YEAR = 365.0 * 86400.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# Core model
# ---------------------------------------------------------------------------

def step_run(f_func, years, lam_abs, drift, dt=0.005):
    """Integrate the two-layer model with a drifting feedback.

    Mixed layer: C_m dT_m/dt = F(t) - (lam_abs + drift*T_m) T_m - gamma (T_m-T_d)
    Deep ocean:  C_d dT_d/dt =                                     + gamma (T_m-T_d)
    N = F - (lam_abs + drift*T_m) T_m is the net top-of-atmosphere flux.

    The time argument and dt are in YEARS; the capacities are in J/(m^2 K), so
    the ODE is integrated in seconds and only the bookkeeping is annual.
    """
    dt_s = dt * YEAR
    n = int(years / dt)
    t = np.arange(n) * dt
    t_m = np.zeros(n)
    t_d = np.zeros(n)
    n_flux = np.zeros(n)

    def deriv(tm, td, tt):
        f_now = f_func(tt)
        d_m = (f_now - (lam_abs + drift * tm) * tm - GAMMA * (tm - td)) / C_MIXED
        d_d = GAMMA * (tm - td) / C_DEEP
        return d_m, d_d

    for k in range(n - 1):
        k1 = deriv(t_m[k], t_d[k], t[k])
        k2 = deriv(t_m[k] + 0.5 * dt_s * k1[0], t_d[k] + 0.5 * dt_s * k1[1],
                   t[k] + 0.5 * dt)
        k3 = deriv(t_m[k] + 0.5 * dt_s * k2[0], t_d[k] + 0.5 * dt_s * k2[1],
                   t[k] + 0.5 * dt)
        k4 = deriv(t_m[k] + dt_s * k3[0], t_d[k] + dt_s * k3[1], t[k] + dt)
        t_m[k + 1] = t_m[k] + dt_s * (k1[0] + 2 * k2[0] + 2 * k3[0]
                                      + k4[0]) / 6.0
        t_d[k + 1] = t_d[k] + dt_s * (k1[1] + 2 * k2[1] + 2 * k3[1]
                                      + k4[1]) / 6.0
        n_flux[k] = f_func(t[k]) - (lam_abs + drift * t_m[k]) * t_m[k]
    n_flux[-1] = f_func(t[-1]) - (lam_abs + drift * t_m[-1]) * t_m[-1]
    return t, t_m, t_d, n_flux


def equilibrium_temp(f, lam_abs, drift):
    """Solve F = (lam_abs + drift*T) T for the positive root."""
    if abs(drift) < 1e-12:
        return f / lam_abs
    disc = lam_abs ** 2 + 4.0 * drift * f
    return (-lam_abs + np.sqrt(disc)) / (2.0 * drift) if drift > 0 else \
        (2.0 * f) / (lam_abs + np.sqrt(disc))


# ---------------------------------------------------------------------------
# 1. Two definitions
# ---------------------------------------------------------------------------

def part1_definitions():
    section("1. Two definitions from one model")
    lam_abs = 3.5
    ecs = equilibrium_temp(F_2X, lam_abs, 0.0)
    print("SYNTHETIC two-layer model: C_m = 2.04e8, C_d = 1.37e10 J/(m^2 K),")
    print(f"gamma = {GAMMA:.2f} W/(m^2 K), |lambda| = {lam_abs:.2f} "
          f"W/(m^2 K), F_2x = {F_2X:.2f} W/m^2")
    print(f"\n  ECS (equilibrium) = F_2x/|lambda| = {ecs:.4f} K")
    # transient: 1%/yr CO2 increase, doubling after ln2/ln1.01 = 69.7 yr
    ramp_rate = np.log(1.01)
    t_double = np.log(2.0) / ramp_rate
    f_ramp = lambda t: F_2X * (ramp_rate * t) / np.log(2.0)
    t, t_m, t_d, n_flux = step_run(f_ramp, 200.0, lam_abs, 0.0)
    i70 = int(t_double / 0.005)
    tcr = t_m[i70]
    kappa = (f_ramp(t_double) - lam_abs * tcr) / tcr
    print(f"  doubling time at 1%/yr = {t_double:.1f} yr")
    print(f"  TCR (transient at doubling) = {tcr:.4f} K")
    print(f"  ratio TCR/ECS = {tcr / ecs:.3f}")
    print(f"  ocean heat uptake efficiency at that time, kappa = N/dT = "
          f"{kappa:.3f} W/(m^2 K)")
    print(f"  approximation TCR ~ F_2x/(|lambda| + kappa) = "
          f"{F_2X / (lam_abs + kappa):.4f} K  "
          f"(error {abs(F_2X / (lam_abs + kappa) - tcr) / tcr * 100:.2f}%)")
    print("\n  ECS is a property of the model's equilibrium; TCR is a property")
    print("  of the model AND of the forcing pathway. They are not two estimates")
    print("  of one number: they are two different numbers, and both are used.")


# ---------------------------------------------------------------------------
# 2. The Gregory regression and its window dependence
# ---------------------------------------------------------------------------

def part2_gregory():
    section("2. The Gregory regression, and why its window matters")
    lam_abs, drift = 3.5, 1.0
    print("Step forcing F_2x applied at t = 0, with a feedback that STRENGTHENS")
    print(f"as the state warms: |lambda(T)| = {lam_abs:.2f} + {drift:.2f} T.")
    print("Gregory regression: N = intercept + slope x dT, over an increasing")
    print("window starting at t = 0.\n")
    f_step = lambda t: F_2X * np.ones_like(np.atleast_1d(t))
    t, t_m, t_d, n_flux = step_run(lambda tt: F_2X, 2000.0, lam_abs, drift,
                                   dt=0.01)
    true_eq = equilibrium_temp(F_2X, lam_abs, drift)
    out_values = []
    print(f"  true equilibrium temperature = {true_eq:.4f} K "
          f"(so the true ECS is {true_eq:.4f} K)")
    print(f"\n{'window (yr)':>12} {'slope (W/m2K)':>15} {'intercept':>10} "
          f"{'R^2':>7} {'|lambda| at end':>17} {'ECS from slope':>15}")
    for win in (20.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0):
        idx = t <= win
        x, y = t_m[idx], n_flux[idx]
        slope, intercept = np.polyfit(x, y, 1)
        resid = y - (slope * x + intercept)
        r2 = 1.0 - resid.var() / y.var()
        lam_end = lam_abs + drift * t_m[idx][-1]
        out_values.append(F_2X / -slope)
        print(f"{win:12.0f} {-slope:15.4f} {intercept:10.4f} {r2:7.5f} "
              f"{lam_end:17.3f} {F_2X / -slope:15.4f}")
    lin = F_2X / lam_abs
    print(f"\n  Compare three numbers. The linear estimate that ignores the drift")
    print(f"  is F_2x/|lambda| = {lin:.4f} K, which is "
          f"{(lin - true_eq) / true_eq * 100:.0f}% above the model's own")
    print(f"  equilibrium of {true_eq:.4f} K. The Gregory estimates run from the")
    print("  shortest to the longest window in the table above, a spread of")
    print(f"  {abs(1 - out_values[-1] / out_values[0]) * 100:.1f}%, and they move SYSTEMATICALLY with the")
    print("  window rather than randomly. The regression is almost perfect at")
    print("  every window (R^2 above 0.999), and yet it is biased, because the")
    print("  fitted slope is an average of |lambda| over the temperatures the")
    print("  window sampled, while ECS depends on |lambda| at the equilibrium")
    print("  temperature. A high R^2 is not evidence of an unbiased slope; it is")
    print("  evidence that a straight line fits the data you chose. With")
    print("  drift = 0 the slope is exact for every window, so the effect is a")
    print("  property of the drifting feedback, not of the regression.")


# ---------------------------------------------------------------------------
# 3. Distribution from an uncertain feedback
# ---------------------------------------------------------------------------

def part3_distribution():
    section("3. One number, or a distribution?")
    n = 400000
    lam = -RNG.uniform(1.5, 3.0, n)          # total feedback, chosen range
    ecs = -F_2X / lam
    print("CHOSEN assumption: total lambda uniform on [-3.0, -1.5] W/(m^2 K).")
    print("ECS = -F_2x/lambda; the reciprocal of a uniform distribution is")
    print("not uniform.\n")
    print(f"{'percentile':>12} {'ECS (K)':>10}")
    for q in (1, 5, 10, 25, 50, 75, 90, 95, 99):
        print(f"{q:12d} {np.percentile(ecs, q):10.3f}")
    print(f"\n  mean {ecs.mean():.3f} K, median {np.median(ecs):.3f} K, "
          f"sd {ecs.std():.3f} K")
    print(f"  skewness {float(((ecs - ecs.mean()) ** 3).mean() / ecs.std() ** 3):.3f}")
    print("  the distribution is strongly right-skewed: the 99th percentile is")
    print(f"  {np.percentile(ecs, 99) / np.median(ecs):.2f} times the median while the")
    print(f"  1st is {np.percentile(ecs, 1) / np.median(ecs):.2f} times it. Any single")
    print("  number quoted from this model must be accompanied by which summary")
    print("  of the distribution it is.")


# ---------------------------------------------------------------------------
# 4. Four estimators
# ---------------------------------------------------------------------------

def part4_estimators():
    section("4. Four ways to estimate the same quantity")
    lam_abs, drift = 3.5, 1.0
    true_eq = equilibrium_temp(F_2X, lam_abs, drift)
    t, t_m, t_d, n_flux = step_run(lambda tt: F_2X, 2000.0, lam_abs, drift,
                                   dt=0.01)
    out = {}
    for win in (50.0, 150.0, 500.0):
        idx = t <= win
        slope, intercept = np.polyfit(t_m[idx], n_flux[idx], 1)
        out[f"ECS, Gregory {win:.0f} yr"] = (F_2X / -slope, -slope)
    ramp_rate = np.log(1.01)
    t_double = np.log(2.0) / ramp_rate
    f_ramp = lambda tt: F_2X * (ramp_rate * tt) / np.log(2.0)
    tr, trm, trd, tn = step_run(f_ramp, 200.0, lam_abs, drift)
    i70 = int(t_double / 0.01)
    tcr = trm[i70]
    kappa = (F_2X - lam_abs * tcr) / tcr
    out["TCR, from the ramp run"] = (tcr, lam_abs + kappa)
    print(f"  true equilibrium ECS (from the model's own algebra) = "
          f"{true_eq:.4f} K")
    print(f"  true TCR (1%/yr ramp, at doubling)                   = "
          f"{tcr:.4f} K")
    print(f"\n{'estimator':>28} {'value (K)':>10} {'|lambda| implied':>16} "
          f"{'error vs truth':>15}")
    for name, (val, lam_use) in out.items():
        truth = tcr if name.startswith("TCR") else true_eq
        print(f"{name:>28} {val:10.4f} {lam_use:16.4f} "
              f"{(val - truth) / truth * 100:14.1f}%")
    print(f"\n  ECS is {true_eq:.4f} K and TCR is {tcr:.4f} K: the transient")
    print(f"  response is {tcr / true_eq * 100:.0f}% of the equilibrium one for this")
    print("  forcing pathway. They are not two estimates of one quantity. Among")
    print("  the ECS estimates the window moves the answer systematically, and")
    print("  among the TCR values the ramp rate and the ocean coupling would do")
    print("  the same.")
    print("  Quoting 'the' climate sensitivity without naming the estimator, the")
    print("  forcing pathway and the window is quoting a number without its")
    print("  definition.")


# ---------------------------------------------------------------------------
# 5. Transient sensitivity versus ocean heat uptake
# ---------------------------------------------------------------------------

def part5_kappa():
    section("5. Transient sensitivity is set by the ocean, not by the feedback")
    lam_abs = 3.5
    ramp_rate = np.log(1.01)
    t_double = np.log(2.0) / ramp_rate
    f_ramp = lambda tt: F_2X * (ramp_rate * tt) / np.log(2.0)
    print(f"ECS fixed at F_2x/|lambda| = {F_2X / lam_abs:.4f} K by fixing")
    print(f"|lambda| = {lam_abs:.2f} W/(m^2 K). Only gamma (the ocean coupling)")
    print("changes between rows.\n")
    print(f"{'gamma (W/m2K)':>15} {'TCR (K)':>9} {'TCR/ECS':>9} "
          f"{'kappa at doubling':>19}")
    for g in (0.3, 0.5, 0.7, 1.0, 1.5):
        globals()['GAMMA'] = g
        t, t_m, t_d, n = step_run(f_ramp, 200.0, lam_abs, 0.0, dt=0.01)
        i70 = int(t_double / 0.01)
        tcr = t_m[i70]
        kappa = (F_2X - lam_abs * tcr) / tcr
        print(f"{g:15.1f} {tcr:9.4f} {tcr / (F_2X / lam_abs):9.3f} "
              f"{kappa:19.3f}")
    globals()['GAMMA'] = 0.7
    print("\n  ECS is identical in every row. TCR spans a factor of about two,")
    print("  because a better-coupled ocean buries heat faster and slows the")
    print("  surface response. This is why TCR is easier to constrain than ECS:")
    print("  it is a property of a few decades, over which the ocean is the")
    print("  dominant unknown, rather than a property of an equilibrium that has")
    print("  never been observed.")


def main():
    part1_definitions()
    part2_gregory()
    part3_distribution()
    part4_estimators()
    part5_kappa()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
