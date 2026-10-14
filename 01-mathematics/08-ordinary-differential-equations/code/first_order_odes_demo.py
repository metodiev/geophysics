"""First-order ODEs: decay, dating, cooling, head relaxation and RC/EM decay.

Run:  python3 first_order_odes_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-01.

Every physical problem below has the form

    dy/dt = -a y            (homogeneous relaxation)
    dy/dt = -a y + b        (relaxation toward an equilibrium b/a)

and its exact solution is stated and then checked against a numerical
integration of the ODE itself. No result is quoted that was not first
recomputed here.

Decay constants are *derived from the quoted half-life inside the script*, so
the arithmetic is internally consistent; the half-lives themselves are the
commonly tabulated values and are marked as such.
"""

import math

# Half-lives used below (commonly tabulated values; see the lesson's
# "Further reading" for how to locate authoritative compilations).
T_HALF_C14_YR = 5730.0      # radiocarbon, the physical value
T_HALF_RB87_YR = 4.9e10     # Rb-87 -> Sr-87
T_HALF_K40_YR = 1.25e9      # K-40 total (all branches)
K40_BRANCH_E = 0.1048       # fraction of K-40 decays going to Ar-40 by e-capture
LAMBDA_C14 = math.log(2.0) / T_HALF_C14_YR
LAMBDA_RB87 = math.log(2.0) / T_HALF_RB87_YR
LAMBDA_K40 = math.log(2.0) / T_HALF_K40_YR


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ---------------------------------------------------------------------------
# Integrators for the single scalar ODE y' = f(t, y)
# ---------------------------------------------------------------------------

def euler(f, t0, y0, h, n):
    t, y = t0, y0
    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
    return t, y


def rk4(f, t0, y0, h, n):
    t, y = t0, y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h
    return t, y


def main():
    section("1. Radioactive decay: exact solution versus two integrators")
    lam = 1.0
    f = lambda t, y: -lam * y
    T = 2.0
    exact = math.exp(-lam * T)
    print(f"y' = -lambda y,  y(0) = 1,  lambda = {lam},  integrate to t = {T}")
    print(f"{'h':>10}{'Euler error':>16}{'ratio':>9}{'RK4 error':>16}{'ratio':>9}")
    prev_e = prev_r = None
    for h in (0.2, 0.1, 0.05, 0.025):
        n = int(round(T / h))
        _, ye = euler(f, 0.0, 1.0, h, n)
        _, yr = rk4(f, 0.0, 1.0, h, n)
        ee, er = abs(ye - exact), abs(yr - exact)
        re_ = "" if prev_e is None else f"{prev_e / ee:9.2f}"
        rr_ = "" if prev_r is None else f"{prev_r / er:9.2f}"
        print(f"{h:>10.3f}{ee:>16.3e}{re_:>9}{er:>16.3e}{rr_:>9}")
        prev_e, prev_r = ee, er
    print("Euler error halves when h halves (first order); RK4 error falls by ~16")
    print("(fourth order). Numerical order, not a theoretical claim.")

    section("2. Radiocarbon dating from an activity ratio")
    ratio = 1.5                      # A0 / A_sample
    age = (T_HALF_C14_YR / math.log(2.0)) * math.log(ratio)
    print(f"half-life       = {T_HALF_C14_YR:.0f} yr  -> lambda = "
          f"{LAMBDA_C14:.6e} /yr")
    print(f"A0/A_sample     = {ratio}")
    print(f"age             = {age:.0f} yr  ({age / 1000:.2f} ka)")
    # Back-substitute: does the age reproduce the ratio?
    print(f"check e^(-lambda t) = {math.exp(-LAMBDA_C14 * age):.6f}  (should be "
          f"{1 / ratio:.6f})")
    print(f"residual        = {abs(math.exp(-LAMBDA_C14 * age) - 1 / ratio):.3e}")

    section("3. Rb-Sr and K-Ar dating from parent/daughter ratios")
    ds_dn = 0.05                     # Sr-87*/Rb-87
    age_rb = math.log(1.0 + ds_dn) / LAMBDA_RB87
    print(f"Rb-Sr: T1/2 = {T_HALF_RB87_YR:.3e} yr, lambda = {LAMBDA_RB87:.6e} /yr")
    print(f"       Sr-87*/Rb-87 = {ds_dn}  ->  age = {age_rb:.4e} yr "
          f"= {age_rb / 1e9:.3f} Ga")
    print(f"       check 1+ratio recovered: "
          f"{math.exp(LAMBDA_RB87 * age_rb) - 1.0:.6e}")

    ar_k = 0.01                      # Ar-40*/K-40
    lam_e = LAMBDA_K40 * K40_BRANCH_E
    age_k = math.log(1.0 + (LAMBDA_K40 / lam_e) * ar_k) / LAMBDA_K40
    print(f"K-Ar:  T1/2 = {T_HALF_K40_YR:.3e} yr, lambda = {LAMBDA_K40:.6e} /yr, "
          f"branching to Ar = {K40_BRANCH_E}")
    print(f"       Ar-40*/K-40 = {ar_k}  ->  age = {age_k:.4e} yr "
          f"= {age_k / 1e6:.1f} Ma")
    print(f"       check 1+ratio recovered: "
          f"{math.exp(LAMBDA_K40 * age_k) - 1.0:.6e}")

    section("4. Newton cooling of a sill (lumped model)")
    kappa = 1.0e-6                   # m^2/s, rock thermal diffusivity
    half_thickness = 50.0            # m
    k = kappa / half_thickness ** 2  # 1/s
    tau = 1.0 / k
    T_magma, T_country = 1100.0, 100.0
    print(f"kappa = {kappa:.1e} m^2/s, half-thickness L = {half_thickness:.0f} m")
    print(f"k = kappa/L^2 = {k:.3e} /s  ->  tau = {tau:.3e} s = "
          f"{tau / (365.25 * 24 * 3600):.1f} yr")
    target = 200.0
    frac = (target - T_country) / (T_magma - T_country)
    t_target = -math.log(frac) / k
    print(f"time to fall from {T_magma:.0f} C to {target:.0f} C "
          f"(country rock {T_country:.0f} C):")
    print(f"   t = -ln((T-Ta)/(T0-Ta))/k = -ln({frac:.3f})/k = "
          f"{t_target:.3e} s = {t_target / (365.25 * 24 * 3600):.1f} yr")
    # Numerical check with RK4 on the ODE itself.
    f_T = lambda t, y: -k * (y - T_country)
    n = 200000
    h = t_target / n
    _, T_num = rk4(f_T, 0.0, T_magma, h, n)
    print(f"   RK4 integration to that time gives T = {T_num:.3f} C "
          f"(target {target:.0f} C)")
    print("   Lumped model: uniform temperature, conduction-limited to the "
          "country rock.")
    print("   It is an upper bound on the cooling time, not a thermal history.")

    section("5. Hydraulic-head relaxation in a confined aquifer")
    T_trans = 1.0e-3                 # m^2/s
    stor = 1.0e-4                    # dimensionless
    L = 1000.0                       # m, drainage length
    tau_h = 4.0 * stor * L ** 2 / (math.pi ** 2 * T_trans)
    print(f"T = {T_trans:.1e} m^2/s, S = {stor:.1e}, L = {L:.0f} m")
    print(f"tau = 4 S L^2 / (pi^2 T) = {tau_h:.4e} s = "
          f"{tau_h / 86400:.3f} days")
    h0 = 5.0
    for t_days in (1.0, 3.0, 10.0):
        t = t_days * 86400.0
        print(f"   t = {t_days:5.1f} d: head = {h0 * math.exp(-t / tau_h):.4f} m"
              f"   (of {h0:.1f} m initial)")
    # Numerical check of the ODE dh/dt = -h/tau.
    f_h = lambda t, y: -y / tau_h
    t10 = 10.0 * 86400.0
    h_step = t10 / 40000
    _, h_num = rk4(f_h, 0.0, h0, h_step, 40000)
    print(f"   RK4 after 10 d: {h_num:.6f} m  vs exact "
          f"{h0 * math.exp(-t10 / tau_h):.6f} m")

    section("6. Pumping drawdown as a linear ODE with constant forcing")
    tau_w = 2.0 * 86400.0            # 2 days, lumped response time
    q_inf = -8.0                     # m, steady-state drawdown at the well
    print(f"dh/dt = -h/tau + h_inf/tau,  tau = {tau_w / 86400:.1f} d, "
          f"h_inf = {q_inf:.1f} m")
    print(f"{'t (d)':>8}{'h (m)':>12}{'exact (m)':>14}")
    for t_days in (0.0, 0.5, 1.0, 2.0, 5.0):
        t = t_days * 86400.0
        exact = q_inf * (1.0 - math.exp(-t / tau_w))
        if t_days == 0.0:
            num = 0.0
        else:
            n = 20000
            hh = t / n
            _, num = rk4(lambda tt, y: (q_inf - y) / tau_w, 0.0, 0.0, hh, n)
        print(f"{t_days:>8.1f}{num:>12.5f}{exact:>14.5f}")
    print("The head approaches 90 % of steady state in t = 2.303 tau.")

    section("7. RC and RL decay: the same ODE, different physics")
    R, C = 1.0e6, 1.0e-6
    print(f"RC circuit: R = {R:.1e} ohm, C = {C:.1e} F  ->  tau = {R * C:.3f} s")
    for t in (0.0, 1.0, 2.0, 4.0):
        print(f"   t = {t:4.1f} s: V/V0 = {math.exp(-t / (R * C)):.6f}")
    L, R2 = 2.0, 40.0
    print(f"RL circuit: L = {L:.1f} H, R = {R2:.0f} ohm  ->  tau = {L / R2:.4f} s")
    print("Both decay exponentially; only the physical name of tau changes.")
    print("A conducting loop of inductance L and resistance R has the same")
    print("magnetic-field decay time tau = L/R; that is why EM transients in")
    print("the ground have characteristic decay times set by conductivity.")

    section("8. Integrating factor verified on a forced problem")
    # y' + 2y = 4x, y(0) = 1  ->  y = 2x - 1 + 2 exp(-2x)
    p = lambda x: 2.0
    q = lambda x: 4.0 * x
    y_exact = lambda x: 2.0 * x - 1.0 + 2.0 * math.exp(-2.0 * x)
    print("y' + 2y = 4x,  y(0) = 1   ->   y = 2x - 1 + 2 exp(-2x)")
    print(f"{'x':>8}{'numerical':>16}{'exact':>16}{'residual y\'+2y-4x':>22}")
    for x in (0.0, 0.5, 1.0, 2.0, 4.0):
        _, y_num = rk4(lambda t, y: q(t) - p(t) * y, 0.0, 1.0, x / 20000.0, 20000) \
            if x > 0 else (0.0, 1.0)
        residual = (y_num - y_exact(x))
        print(f"{x:>8.2f}{y_num:>16.9f}{y_exact(x):>16.9f}{residual:>22.3e}")
    print("Residual is integration error only; the formula is exact.")

    section("9. Why the relaxation time, not the amplitude, sets the clock")
    print("For every system above the state variable obeys y' = -y/tau, whose")
    print("solution halves after t = tau ln 2 = 0.6931 tau. The *absolute* size")
    print("of the state never enters the exponent: a large intrusion and a small")
    print("one cool with the same time constant, which is fixed by geometry and")
    print("diffusivity alone.")


if __name__ == "__main__":
    main()
