"""Heat conduction, Fourier's law and thermal diffusivity.

Run:  python3 heat_conduction_demo.py
Requires: Python standard library only.

Companion to lesson 02-05-04. This is the numerical-verification script for the
module: it solves the 1-D diffusion equation explicitly and compares the result
against the analytic error-function solution, reporting the measured
discrepancy.

Material properties are nominal (k = 2.5 W m^-1 K^-1, rho = 2700 kg m^-3,
c_p = 800 J kg^-1 K^-1 for "rock"), chosen to be internally consistent.

The script:

1. Tabulates thermal diffusivity kappa = k/(rho c_p) and contrasts it with
   thermal conductivity, which differs by a factor of ~10^6.
2. Computes the diffusion time for L = 10 m, 100 m, 1 km and 10 km, under two
   explicit conventions, and the diffusion length sqrt(kappa t).
3. Solves the half-space step-change problem by finite differences and compares
   it with T(z,t) = dT erfc(z / 2 sqrt(kappa t)): profile error, surface-flux
   error, and an observed convergence order.
4. Computes the penetration of periodic surface temperature variations
   (diurnal and annual skin depths).
"""

import math

YEAR = 3.15576e7            # s, Julian year (365.25 d)

# Nominal properties.
ROCK = {"k": 2.5, "rho": 2700.0, "c": 800.0}
OCEANIC = {"k": 3.2, "rho": 3300.0, "c": 1250.0}
WATER = {"k": 0.60, "rho": 1000.0, "c": 4186.0}
AIR = {"k": 0.026, "rho": 1.225, "c": 1005.0}


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def kappa(m):
    return m["k"] / (m["rho"] * m["c"])


def part1_diffusivity_table():
    section("1. Thermal conductivity versus thermal diffusivity")
    print("  kappa = k / (rho c_p)   -- these differ by a factor ~1e6 in rock")
    print(f"{'medium':<14}{'k (W/m/K)':>12}{'rho (kg/m3)':>13}"
          f"{'c_p (J/kg/K)':>14}{'kappa (m2/s)':>16}")
    for name, m in (("rock", ROCK), ("oceanic", OCEANIC), ("water", WATER),
                    ("air", AIR)):
        print(f"{name:<14}{m['k']:>12.3f}{m['rho']:>13.1f}{m['c']:>14.1f}"
              f"{kappa(m):>16.6e}")
    print()
    kr, kw = ROCK["k"], WATER["k"]
    print(f"  Rock conducts heat {kr / kw:.2f} times better than water AND")
    print(f"  diffuses temperature {kappa(ROCK) / kappa(WATER):.3f} times faster,")
    print("  because water's much larger volumetric heat capacity more than")
    print("  offsets its low conductivity. The two ratios are not equal, and")
    print("  neither one can be inferred from the other:")
    print("  conductivity limits the FLUX; diffusivity limits the SPEED.")
    print("  Confusing the two is the commonest error in this subject.")


def part2_timescales():
    section("2. Diffusion timescale tau = L^2 / kappa")
    kap = kappa(ROCK)
    print(f"  Using kappa = {kap:.6e} m2/s (rock)")
    print(f"{'L':>10}{'L (m)':>10}{'tau = L^2/kappa':>18}{'tau (a)':>12}"
          f"{'t(10% of dT) (a)':>20}")
    for L in (10.0, 100.0, 1.0e3, 1.0e4):
        tau = L * L / kap
        # erfc(x) = 0.10 -> x = 0.9061938, so t = L^2/(4 x^2 kappa)
        x = 0.9061938024
        t10 = L * L / (4.0 * x * x * kap)
        print(f"{L:>10.0f}{L:>10.0f}{tau:>18.4e}{tau / YEAR:>12.1f}"
              f"{t10 / YEAR:>20.1f}")
    print()
    print("  Two conventions, both used in the literature:")
    print("    tau = L^2/kappa is the order-of-magnitude diffusion time;")
    print("    t(10%) is the time for a step change to register 10 per cent of")
    print("    its amplitude at depth L.")
    print()
    print("  A surface temperature change reaches 100 m on a timescale of")
    print(f"  {100.0 ** 2 / kap / YEAR:.0f} years and 1 km on a timescale of")
    print(f"  {1000.0 ** 2 / kap / YEAR:.0f} years. That ratio of 100 is the")
    print("  L^2 law, and it is the entire basis of borehole palaeoclimatology:")
    print("  the shallow record is a centuries-long thermometer, the 1 km record")
    print("  a glacial-cycle one, and nothing deeper is recoverable because")
    print("  sediment blanketing and advection corrupt the signal.")
    print()
    print(f"  Diffusion length sqrt(kappa t) in 1 ka = "
          f"{math.sqrt(kap * 1000.0 * YEAR):.2f} m;")
    print(f"  in 1 Ma = {math.sqrt(kap * 1e6 * YEAR):.1f} m;")
    print(f"  in 1 Ga = {math.sqrt(kap * 1e9 * YEAR) / 1e3:.1f} km.")
    print("  Over the age of the Earth, conduction alone moves heat roughly a")
    print("  couple of hundred kilometres — and in practice far less, because")
    print("  the mantle convects.")


def solve_halfspace(kap, t_end, Lmax, dz, r, T_s=1.0):
    """Explicit finite-difference solution of the 1-D diffusion equation.

    Domain 0 <= z <= Lmax, T(z,0) = 0, T(0,t) = T_s, T(Lmax,t) = 0.
    Stability requires r = kappa dt / dz^2 <= 0.5.
    """
    dt = r * dz * dz / kap
    nsteps = int(round(t_end / dt))
    dt = t_end / nsteps
    r_eff = kap * dt / (dz * dz)
    n = int(round(Lmax / dz)) + 1
    T = [0.0] * n
    T[0] = T_s
    for _ in range(nsteps):
        prev = T[0]
        for i in range(1, n - 1):
            cur = T[i]
            T[i] = cur + r_eff * (prev - 2.0 * cur + T[i + 1])
            prev = cur
        T[0] = T_s
        T[-1] = 0.0
    return T, dt, nsteps, r_eff


def part3_fd_vs_erfc():
    section("3. Finite differences versus the error-function solution")
    kap = kappa(ROCK)
    k, dT = ROCK["k"], 10.0                       # K
    t_end = 2500.0 * YEAR
    Lmax = 3000.0
    dz, r = 5.0, 0.4
    T, dt, nsteps, r_eff = solve_halfspace(kap, t_end, Lmax, dz, r, 1.0)
    print(f"  kappa = {kap:.6e} m2/s, t = 2500 a = {t_end:.4e} s, "
          f"dz = {dz:.1f} m, r = {r_eff:.4f}, steps = {nsteps}")
    print(f"  analytic: T(z,t) = dT erfc(z / (2 sqrt(kappa t))), "
          f"2 sqrt(kappa t) = {2 * math.sqrt(kap * t_end):.2f} m")
    print()
    print(f"{'z (m)':>8}{'T_num/dT':>12}{'T_erfc/dT':>12}{'abs err':>12}"
          f"{'rel err':>12}")
    max_abs = 0.0
    ss_err = 0.0
    count = 0
    for z in (0.0, 50.0, 100.0, 200.0, 300.0, 400.0, 600.0, 800.0, 1000.0):
        i = int(round(z / dz))
        num = T[i]
        an = math.erfc(z / (2.0 * math.sqrt(kap * t_end)))
        err = abs(num - an)
        rel = err / an if an > 1e-12 else 0.0
        max_abs = max(max_abs, err)
        if an > 1e-6:
            ss_err += err * err
            count += 1
        print(f"{z:>8.0f}{num:>12.6f}{an:>12.6f}{err:>12.3e}{rel:>12.3e}")
    rms = math.sqrt(ss_err / count)
    print()
    print(f"  max |T_num - T_erfc| = {max_abs:.4e}  (in units of dT)")
    print(f"  rms error over points with signal = {rms:.4e}  (in units of dT)")
    print(f"  i.e. a worst-case temperature error of {max_abs * dT:.4e} K "
          f"for a {dT:.0f} K step,")
    print(f"  or {100.0 * max_abs:.4f} per cent of the step amplitude.")
    print()
    an_flux = k * dT / math.sqrt(math.pi * kap * t_end)
    num_flux = k * dT * (T[0] - T[1]) / dz          # upward surface flux
    print(f"  surface flux, analytic k dT/sqrt(pi kappa t) = "
          f"{an_flux:.6f} W/m2 ({an_flux * 1e3:.4f} mW/m2)")
    print(f"  surface flux, finite difference k (T0-T1)/dz  = "
          f"{num_flux:.6f} W/m2 ({num_flux * 1e3:.4f} mW/m2)")
    print(f"  relative difference = "
          f"{abs(num_flux - an_flux) / an_flux:.4e}")
    print()
    print("  A 10 K surface step 2500 years ago still contributes tens of")
    print("  milliwatts per square metre at the surface — a real perturbation")
    print("  in a heat-flow measurement, which is why borehole heat-flow series")
    print("  must be corrected for surface temperature history.")
    return kap, t_end


def part4_convergence():
    section("4. Observed convergence of the scheme")
    kap = kappa(ROCK)
    t_end = 500.0 * YEAR
    Lmax = 1500.0
    print("  r = kappa dt/dz^2 held at 0.4, so dt ~ dz^2 and the temporal")
    print("  truncation error is O(dt) = O(dz^2).")
    print(f"{'dz (m)':>8}{'dt (s)':>12}{'steps':>10}{'Linf err/dT':>16}"
          f"{'ratio':>10}")
    prev = None
    for dz in (40.0, 20.0, 10.0, 5.0):
        T, dt, nsteps, r_eff = solve_halfspace(kap, t_end, Lmax, dz, 0.4, 1.0)
        worst = 0.0
        for i in range(0, int(round(Lmax / dz)) + 1):
            z = i * dz
            an = math.erfc(z / (2.0 * math.sqrt(kap * t_end)))
            worst = max(worst, abs(T[i] - an))
        ratio = (prev / worst) if prev else float("nan")
        print(f"{dz:>8.1f}{dt:>12.4e}{nsteps:>10d}{worst:>16.4e}"
              f"{ratio:>10.2f}")
        prev = worst
    print()
    print("  The error falls by ~4 each time dz is halved, which is the")
    print("  expected second-order dependence on the grid spacing (we hold the")
    print("  cell Courant number fixed, so refining dz refines dt in step).")
    print("  The scheme is verified against an exact solution, not merely")
    print("  'reasonable-looking'.")


def part5_periodic():
    section("5. Periodic surface forcing: skin depth and attenuation")
    kap = kappa(ROCK)
    print("  For T(0,t) = T0 + dT cos(omega t), the solution is")
    print("  T(z,t) = T0 + dT exp(-z/delta) cos(omega t - z/delta),")
    print("  delta = sqrt(2 kappa / omega), the thermal skin depth.")
    print(f"{'cycle':<10}{'period (s)':>14}{'omega (rad/s)':>16}"
          f"{'delta (m)':>12}{'depth for 1% amp (m)':>22}")
    for name, period in (("diurnal", 86400.0), ("annual", YEAR),
                         ("100 ka", 100.0e3 * YEAR),
                         ("1 Ma", 1.0e6 * YEAR)):
        omega = 2.0 * math.pi / period
        delta = math.sqrt(2.0 * kap / omega)
        depth1 = delta * math.log(100.0)
        print(f"{name:<10}{period:>14.6e}{omega:>16.6e}{delta:>12.4f}"
              f"{depth1:>22.3f}")
    print()
    omega_a = 2.0 * math.pi / YEAR
    delta_a = math.sqrt(2.0 * kap / omega_a)
    for z in (1.0, 3.0, 5.0, 10.0):
        amp = math.exp(-z / delta_a)
        lag_days = (z / delta_a) / omega_a / 86400.0
        print(f"  annual wave at z = {z:>4.1f} m: amplitude {amp:.4f} of surface,"
              f" phase lag {lag_days:>6.1f} days")
    print()
    print("  The diurnal wave is dead by ~0.8 m and the annual wave by ~15 m.")
    print("  Below that, only the glacial-cycle and longer components survive.")
    print("  This is why a borehole temperature log is a low-pass filtered")
    print("  history of surface temperature, with the filter set by kappa.")


if __name__ == "__main__":
    part1_diffusivity_table()
    part2_timescales()
    part3_fd_vs_erfc()
    part4_convergence()
    part5_periodic()
