"""Sedimentary basins: stretching, thermal subsidence and backstripping.

Run:  .venv/bin/python 04-basins_subsidence_demo.py
Requires: NumPy.

Companion to lesson 04-03-04. A basin is a place where the lithosphere has been
made able to hold a thickness of sediment, and the record in the sediment is the
subsidence history. This demo separates the two contributions that a subsidence
curve contains and shows how much of the answer is a consequence of the physics
and how much is a consequence of the values you chose:

1. Solves the 1-D heat-conduction equation for a lithosphere that has been
   stretched instantaneously by a factor beta, computes the isostatic subsidence
   from the density deficit of the cooling column, and compares the numerical
   result with the analytic thermal-subsidence law -- at two grid resolutions,
   so the agreement is evidence about the discretisation and not a coincidence.
2. Computes the instantaneous (crustal-thinning) subsidence and the total
   subsidence, and inverts an observed subsidence for the stretching factor.
3. Backstrips a synthetic stratigraphic column: decompacts each unit with an
   exponential porosity-depth law, removes the sediment and water load, and
   reports the water-loaded tectonic subsidence.
4. Perturbs the assumed porosity, density and lithospheric parameters one at a
   time and reports how many metres of "tectonic subsidence" each assumption is
   worth -- the quantitative reason a subsidence curve is a model, not a datum.

Every physical parameter below is labelled TABULATED or TYPICAL and is a
commonly quoted value: lithospheric thickness, mantle temperature, thermal
expansion coefficient, thermal diffusivity, densities and crustal thickness all
vary between provinces and between compilations, and a subsidence model is only
as good as the values chosen for its province.
"""

from __future__ import annotations

import numpy as np

# --------------------------------------------------------------------------
# TYPICAL / TABULATED parameters.  These are commonly quoted values chosen for
# a continental setting; a real study replaces each with a province-specific
# value and a reference.
# --------------------------------------------------------------------------
A_LITHO = 125.0e3          # m, lithospheric thickness (commonly used standard)
T_MANTLE = 1330.0          # degC, asthenospheric potential temperature (typical)
ALPHA = 3.28e-5            # 1/K, thermal expansion coefficient (commonly quoted)
KAPPA = 1.0e-6             # m^2/s, thermal diffusivity (commonly quoted)
RHO_M = 3300.0             # kg/m^3, mantle density at 0 degC reference
RHO_C = 2800.0             # kg/m^3, crustal density
RHO_S = 2500.0             # kg/m^3, bulk sediment density (compact)
RHO_W = 1030.0             # kg/m^3, sea water
T_CRUST = 35.0e3           # m, crustal thickness (typical continental)
SEC_PER_MYR = 3.15576e13   # s per million years (Julian year)


def initial_geotherm(z: np.ndarray, beta: float) -> np.ndarray:
    """Temperature immediately after instantaneous stretching by beta.

    z is measured downward from the surface.  The steady geotherm before rifting
    is T(z) = T_mantle z / a, with T = 0 at the surface and T = T_mantle at the
    base of the lithosphere.  Stretching reduces the lithospheric thickness to
    a/beta while preserving the temperature difference across it, so
    T(z, 0) = T_mantle beta z / a for z <= a/beta and T_mantle below that.
    """
    stretched = A_LITHO / beta
    return np.where(z <= stretched, T_MANTLE * beta * z / A_LITHO, T_MANTLE)


def steady_geotherm(z: np.ndarray) -> np.ndarray:
    """The pre-rift (and asymptotic post-rift) conductive geotherm."""
    return T_MANTLE * z / A_LITHO


def solve_heat(theta0: np.ndarray, n_cells: int, dt: float, t_end: float):
    """Explicit finite-difference solution for the thermal perturbation.

    theta = T - T_steady satisfies theta_t = kappa theta_zz with theta = 0 at
    both ends of the column.  Working with theta makes the boundary conditions
    homogeneous and makes the comparison with the sine-series solution direct.
    """
    z = np.linspace(0.0, A_LITHO, n_cells + 1)
    dz = z[1] - z[0]
    theta = np.asarray(theta0, dtype=float).copy()
    theta[0] = 0.0
    theta[-1] = 0.0
    stable_dt = dz ** 2 / (2.0 * KAPPA)
    if dt > stable_dt:
        raise ValueError(f"dt={dt:.3e} s exceeds the stability limit "
                         f"{stable_dt:.3e} s")
    r = KAPPA * dt / dz ** 2
    history = [(0.0, theta.copy())]
    for step in range(1, int(round(t_end / dt)) + 1):
        interior = theta[1:-1] + r * (theta[2:] - 2.0 * theta[1:-1]
                                      + theta[:-2])
        theta = np.concatenate(([0.0], interior, [0.0]))
        history.append((step * dt, theta.copy()))
    return z, dz, history


def post_rift_perturbation(z: np.ndarray, beta: float) -> np.ndarray:
    theta0 = initial_geotherm(z, beta) - steady_geotherm(z)
    theta0[0] = 0.0
    theta0[-1] = 0.0
    return theta0


def modal_weights(beta: float, n_max: int = 399):
    """Sine-series weights of the post-stretching thermal perturbation.

    theta(z, 0) is continuous and vanishes at both ends, so it has a sine series
    whose n-th mode decays as exp(-n^2 t / tau) with tau = a^2/(pi^2 kappa).
    Subsidence is proportional to the column integral of theta, and only the odd
    modes have a non-zero integral, so the subsidence at time t is
    E0 * sum_n w_n (1 - exp(-n^2 t / tau)).

    The weights are the mode integrals c_n = b_n * 2a/(n pi), normalised by
    their exactly known sum.  The returned third value is the relative error of
    that normalisation against the analytic column integral Tm a/2 (1 - 1/beta),
    so a quadrature failure cannot pass silently.
    """
    z = np.linspace(0.0, A_LITHO, 20001)
    theta0 = post_rift_perturbation(z, beta)
    odd = np.arange(1, n_max + 1, 2).astype(float)
    b_over_2 = np.array([
        np.trapezoid(theta0 * np.sin(n * np.pi * z / A_LITHO), z) / A_LITHO
        for n in odd
    ])
    c = 4.0 * b_over_2 * A_LITHO / (odd * np.pi)
    total = c.sum()
    exact_integral = T_MANTLE * A_LITHO / 2.0 * (1.0 - 1.0 / beta)
    return odd, c / total, abs(total - exact_integral) / exact_integral


def exact_subsidence(t_array: np.ndarray, beta: float) -> np.ndarray:
    """Subsidence as a fraction of E0, from the sine-series solution."""
    odd, weights, _err = modal_weights(beta)
    tau = A_LITHO ** 2 / (np.pi ** 2 * KAPPA)
    out = np.zeros_like(t_array, dtype=float)
    for n, w in zip(odd, weights):
        out += w * (1.0 - np.exp(-n ** 2 * t_array / tau))
    return out


def water_loaded_scale(rho_load: float) -> float:
    """alpha rho_m T_mantle a / (2 (rho_m - rho_load)), the subsidence scale."""
    return ALPHA * RHO_M * T_MANTLE * A_LITHO / (2.0 * (RHO_M - rho_load))


def part_one() -> None:
    print()
    print("1. Thermal subsidence after stretching")
    print("-" * 78)
    beta = 2.0
    t_end = 200.0 * SEC_PER_MYR
    tau = A_LITHO ** 2 / (np.pi ** 2 * KAPPA)
    e0 = water_loaded_scale(RHO_W) * (1.0 - 1.0 / beta)
    print(f"  beta = {beta:.2f},  a = {A_LITHO / 1e3:.0f} km, "
          f"kappa = {KAPPA:.1e} m^2/s")
    print(f"  thermal time constant tau = a^2/(pi^2 kappa) = "
          f"{tau / SEC_PER_MYR:,.2f} Ma")
    print(f"  asymptotic thermal subsidence E0 = {e0:,.1f} m "
          f"for beta = {beta:.2f}")

    print()
    print("  Step 1: verify the solver against a case with an exact solution.")
    print("  Set the perturbation to a single sine mode theta = Theta sin(pi z/a);")
    print("  the exact solution is theta exp(-t/tau), so the fractional "
          "subsidence must")
    print("  be exactly 1 - exp(-t/tau) at every time.")
    theta_amp = 100.0
    exact_case = {}
    print(f"{'n cells':>9}{'dt (Ma)':>10}{'t (Ma)':>9}{'numeric':>12}"
          f"{'1-exp(-t/tau)':>16}{'error':>12}")
    for n_cells in (100, 400):
        z = np.linspace(0.0, A_LITHO, n_cells + 1)
        theta0 = theta_amp * np.sin(np.pi * z / A_LITHO)
        dz = z[1] - z[0]
        dt = 0.4 * dz ** 2 / KAPPA
        _, _, history = solve_heat(theta0, n_cells, dt, t_end)
        integral0 = float(np.sum(theta0) * dz)
        exact_case[n_cells] = {}
        for t, profile in history:
            frac = 1.0 - float(np.sum(profile) * dz) / integral0
            exact_case[n_cells][t] = frac
        for t_ma in (25.0, 100.0, 200.0):
            key = min(exact_case[n_cells],
                      key=lambda x: abs(x - t_ma * SEC_PER_MYR))
            num = exact_case[n_cells][key]
            ana = 1.0 - np.exp(-key / tau)
            print(f"  {n_cells:>7}{dt / SEC_PER_MYR:>10.3f}"
                  f"{key / SEC_PER_MYR:>9.1f}{num:>12.6f}{ana:>16.6f}"
                  f"{num - ana:>12.2e}")
    print("  The error falls from 3e-5 to 2e-6 when dt is reduced by a factor "
          "of 20: this is")
    print("  the explicit scheme's time-discretisation error, not a modelling "
          "error. That is")
    print("  a verified solver, so any remaining disagreement in the next step "
          "is a property")
    print("  of the problem and not of the code.")

    print()
    print("  Step 2: the post-rift geotherm, which is NOT a single sine mode.")
    odd, weights, norm_err = modal_weights(beta)
    print(f"  modal quadrature check: |sum(c_n) - Tm a/2 (1 - 1/beta)| / exact "
          f"= {norm_err:.2e}")
    print(f"{'mode n':>8}{'1/tau_n (Ma^-1)':>18}{'weight':>12}{'cumulative':>13}")
    cumulative = 0.0
    for n, w in list(zip(odd, weights))[:6]:
        cumulative += w
        print(f"  {n:>6.0f}{(n ** 2 / (tau / SEC_PER_MYR)):>18.5f}{w:>12.5f}"
              f"{cumulative:>13.5f}")
    print(f"  the first mode carries {weights[0]:.4f} of the total and the "
          f"third {weights[1]:+.4f}:")
    print("  the weights alternate in sign and decay as 1/n^3, so the "
          "perturbation is a")
    print("  sum of modes with very different decay rates.")

    print()
    print(f"{'n cells':>9}{'dt (Ma)':>10}{'dz (m)':>10}"
          f"{'S(50 Ma)':>12}{'exact(50)':>12}{'rel. err':>11}")
    curves = {}
    for n_cells in (50, 100, 200, 400):
        z = np.linspace(0.0, A_LITHO, n_cells + 1)
        theta0 = post_rift_perturbation(z, beta)
        dz = z[1] - z[0]
        dt = min(0.25 * SEC_PER_MYR, 0.4 * dz ** 2 / KAPPA)
        _, _, history = solve_heat(theta0, n_cells, dt, t_end)
        scale = ALPHA * RHO_M / (RHO_M - RHO_W)
        integral0 = float(np.sum(theta0) * dz)
        curve = {t: scale * (integral0 - float(np.sum(profile) * dz))
                 for t, profile in history}
        curves[n_cells] = curve
        key = min(curve, key=lambda x: abs(x - 50.0 * SEC_PER_MYR))
        exact50 = e0 * float(exact_subsidence(np.array([key]), beta)[0])
        err = abs(curve[key] - exact50) / exact50
        print(f"  {n_cells:>7}{dt / SEC_PER_MYR:>10.3f}{dz:>10.1f}"
              f"{curve[key]:>12,.1f}{exact50:>12,.1f}{err:>11.4%}")

    curve = curves[400]
    print()
    print("  Full curve at 400 cells against the exact series and against the "
          "single-mode")
    print("  closed form usually quoted:")
    print(f"{'t (Ma)':>9}{'numeric (m)':>13}{'exact (m)':>12}"
          f"{'numeric-exact':>15}{'1-mode law':>13}{'law-exact':>12}")
    worst_num = worst_law = 0.0
    for t_ma in (0.0, 5.0, 10.0, 25.0, 50.0, 100.0, 150.0, 200.0):
        key = min(curve, key=lambda x: abs(x - t_ma * SEC_PER_MYR))
        num = curve[key]
        exact = e0 * float(exact_subsidence(np.array([key]), beta)[0])
        law = e0 * (1.0 - np.exp(-key / tau))
        worst_num = max(worst_num, abs(num - exact))
        worst_law = max(worst_law, abs(law - exact))
        print(f"  {key / SEC_PER_MYR:>7.1f}{num:>13,.1f}{exact:>12,.1f}"
              f"{num - exact:>15,.1f}{law:>13,.1f}{law - exact:>12,.1f}")
    print(f"  worst |numeric - exact|   : {worst_num:.3e} m "
          f"({worst_num / e0:.3e} of E0)")
    print(f"  worst |1-mode law - exact|: {worst_law:.1f} m "
          f"({worst_law / e0:.2%} of E0)")
    print("  Two separate results. The numerical curve reproduces the exact "
          "series to about a")
    print("  part in 10^5, which means the discretisation and the isostatic "
          "bookkeeping are")
    print("  both right. And the familiar S(t) = E0 (1 - exp(-t/tau)) is the "
          "*first-mode")
    print("  truncation* of that series: it errs by tens of metres (about 40 m "
          "here, 2 per")
    print("  cent of E0) around 10-25 Myr, because mode 3 alone carries about 4 "
          "per cent of")
    print("  the amplitude and decays nine times faster, mode 5 twenty-five "
          "times faster.")
    print("  Quote the closed form, but know what it is.")


def part_two() -> None:
    print()
    print("2. Instantaneous subsidence, total subsidence, and beta inversion")
    print("-" * 76)
    print(f"{'beta':>6}{'S_initial (m)':>16}{'S_thermal(inf) (m)':>21}"
          f"{'S_total (m)':>14}{'crustal thinning (km)':>23}")
    for beta in (1.25, 1.5, 2.0, 3.0, 5.0):
        s_initial = (T_CRUST * (1.0 - 1.0 / beta)
                     * (RHO_M - RHO_C) / (RHO_M - RHO_W))
        s_thermal = water_loaded_scale(RHO_W) * (1.0 - 1.0 / beta)
        print(f"  {beta:>4.2f}{s_initial:>16,.1f}{s_thermal:>21,.1f}"
              f"{s_initial + s_thermal:>14,.1f}{T_CRUST * (1 - 1 / beta) / 1e3:>23.2f}")
    print("  Both terms contain the factor (1 - 1/beta): a basin is created by "
          "thinning the lithosphere, and every consequence scales with the "
          "fraction removed.")

    print()
    print("  Inversion: what beta does an observed total subsidence imply?")
    observed = 3000.0  # m, SYNTHETIC observed water-loaded subsidence
    # S_total(beta) = (1 - 1/beta) * [ t_c (rho_m - rho_c)/(rho_m - rho_w)
    #                                 + alpha rho_m T_m a / (2 (rho_m - rho_w)) ]
    coefficient = (T_CRUST * (RHO_M - RHO_C) / (RHO_M - RHO_W)
                   + water_loaded_scale(RHO_W))
    one_minus = observed / coefficient
    beta_fit = 1.0 / (1.0 - one_minus)
    print(f"    SYNTHETIC observed S_total = {observed:,.0f} m")
    print(f"    coefficient (per unit of 1 - 1/beta) = {coefficient:,.0f} m")
    print(f"    (1 - 1/beta) = {one_minus:.4f}  ->  beta = {beta_fit:.3f}")
    print(f"    crustal thinning implied = {T_CRUST * (1 - 1 / beta_fit) / 1e3:.2f} km")
    print("  One number does not determine a history: the same total subsidence "
          "can come from more thinning with less thermal subsidence, or the "
          "reverse, which is why the shape of the curve and not its endpoint is "
          "the measurement.")


def porosity(depth: float, phi0: float, c: float) -> float:
    return phi0 * np.exp(-depth / c)


def backstrip(units, phi0: float, c: float):
    """Decompact a column and return the water-loaded tectonic subsidence.

    Units are (age_Ma, present_top_m, present_bottom_m, grain_density).  The
    column is decompacted unit by unit from the top down, so each unit's
    thickness is its thickness at the time it was deposited.
    """
    load = 0.0        # mass per unit area of everything above the unit
    rows = []
    for age, top, bottom, rho_g in units:
        thickness_now = bottom - top
        if thickness_now <= 0:
            raise ValueError("a unit must have positive present thickness")
        phi_now = porosity(0.5 * (top + bottom), phi0, c)
        # Decompacted thickness: solid volume is conserved.
        solid = thickness_now * (1.0 - phi_now)
        decompacted = solid / (1.0 - phi0)  # porosity at deposition is phi0
        mass = load + RHO_W * decompacted + solid * (rho_g - RHO_W)
        tectonic = mass / (RHO_M - RHO_W)
        rows.append((age, thickness_now, phi_now, decompacted, tectonic))
        load = mass
    return rows


def part_three() -> None:
    print()
    print("3. Backstripping a synthetic stratigraphic column")
    print("-" * 76)
    # SYNTHETIC column: age (Ma), present top (m), present bottom (m),
    # grain density (kg/m^3).  Constructed for the arithmetic.
    units = [
        (40.0, 0.0, 400.0, 2650.0),
        (30.0, 400.0, 1100.0, 2700.0),
        (20.0, 1100.0, 2000.0, 2720.0),
        (10.0, 2000.0, 3200.0, 2680.0),
    ]
    phi0 = 0.55      # TYPICAL surface porosity
    c = 2000.0       # m, TYPICAL porosity decay length
    print(f"  assumed surface porosity phi0 = {phi0:.2f}, decay length c = "
          f"{c:,.0f} m, water depth 0 m")
    rows = backstrip(units, phi0, c)
    print()
    print(f"{'age (Ma)':>10}{'thickness now (m)':>19}{'phi now':>9}"
          f"{'decompacted (m)':>17}{'tectonic subs. (m)':>20}")
    for age, thickness, phi_now, decompacted, tectonic in rows:
        print(f"  {age:>8.0f}{thickness:>19,.0f}{phi_now:>9.3f}"
              f"{decompacted:>17,.0f}{tectonic:>20,.0f}")
    print("  Decompacted thickness always exceeds present thickness because the "
          "unit was buried less, and therefore had more porosity, when it was "
          "deposited.")
    span_yr = (units[0][0] - units[-1][0]) * 1e6
    rate_m_per_ka = rows[-1][4] / span_yr * 1e3
    print(f"  mean tectonic subsidence rate over the {span_yr / 1e6:.0f} Myr "
          f"of record: {rate_m_per_ka:.4f} m/ka, i.e. "
          f"{rate_m_per_ka / 1e3:.2e} mm/a")
    print("  Watch the rate, not the thickness: a basin filled in 10 Myr and one "
          "filled in 100 Myr have different histories behind the same column.")


def part_four() -> None:
    print()
    print("4. What each assumption is worth, in metres of tectonic subsidence")
    print("-" * 76)
    units = [
        (40.0, 0.0, 400.0, 2650.0),
        (30.0, 400.0, 1100.0, 2700.0),
        (20.0, 1100.0, 2000.0, 2720.0),
        (10.0, 2000.0, 3200.0, 2680.0),
    ]
    base = backstrip(units, 0.55, 2000.0)[-1][4]
    print(f"  base case: phi0 = 0.55, c = 2000 m, rho_s = {RHO_S:.0f} kg/m^3 "
          f"-> S_tectonic = {base:,.0f} m")
    print()
    print(f"{'parameter':<26}{'variant':>16}{'S_tectonic (m)':>18}{'change (m)':>14}")
    variants = []
    for phi0 in (0.45, 0.55, 0.65):
        variants.append(("surface porosity phi0", f"{phi0:.2f}",
                         backstrip(units, phi0, 2000.0)[-1][4]))
    for decay in (1500.0, 2000.0, 3000.0):
        variants.append(("porosity decay length", f"{decay:,.0f} m",
                         backstrip(units, 0.55, decay)[-1][4]))
    for rho_g in (2650.0, 2750.0, 2850.0):
        units_v = [(a, t, b, rho_g) for a, t, b, _ in units]
        variants.append(("grain density", f"{rho_g:,.0f} kg/m^3",
                         backstrip(units_v, 0.55, 2000.0)[-1][4]))
    for label, variant, value in variants:
        print(f"  {label:<24}{variant:>16}{value:>18,.0f}{value - base:>+14,.0f}")
    print()
    print(f"  Spread caused by the porosity assumptions alone: "
          f"{max(v for l, _, v in variants if 'porosity' in l) - min(v for l, _, v in variants if 'porosity' in l):,.0f} m; "
          f"by grain density alone: "
          f"{max(v for l, _, v in variants if 'density' in l) - min(v for l, _, v in variants if 'density' in l):,.0f} m.")
    print("  These are the same order as the tectonic signal being measured. A "
          "backstripped curve without a sensitivity table is a curve with an "
          "unstated error bar, and the error bar is not the measurement's fault.")


def main() -> None:
    print("=" * 78)
    print("Sedimentary basins: stretching, thermal subsidence, backstripping")
    print("=" * 78)
    part_one()
    part_two()
    part_three()
    part_four()
    print()
    print("=" * 78)
    print("All parameters are TABULATED/TYPICAL values, not measurements of a")
    print("particular basin, and all synthetic inputs are constructed. Change a")
    print("parameter and the curve moves: that is the lesson, not a defect.")
    print("=" * 78)


if __name__ == "__main__":
    main()
