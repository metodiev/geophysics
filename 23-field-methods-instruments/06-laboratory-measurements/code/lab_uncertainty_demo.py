"""Laboratory uncertainty budgets and reporting: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (the GUM-style combination of Type A and
Type B uncertainties, rectangular and expanded-certificate conversions, the
Welch-Satterthwaite effective degrees of freedom, the En score, a variance
components model).  No laboratory standard, certificate or measured value is
reproduced.
"""

import math

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "A budget: Type A and Type B terms combined")
    print(f"  {'term':<34}{'type':>6}{'standard u':>13}{'variance share':>16}")
    terms = [
        ("repeatability (s = 0.45, n = 6)", "A", 0.45 / math.sqrt(6.0), 5),
        ("calibration certificate (U = 0.60, k = 2)", "B", 0.60 / 2.0, None),
        ("resolution 0.1 (rectangular)", "B", 0.1 / (2.0 * math.sqrt(3.0)), None),
        ("temperature +-0.05 (rectangular)", "B", 0.05 / math.sqrt(3.0), None),
        ("drift since calibration 0.08 (rect.)", "B", 0.08 / math.sqrt(3.0), None),
    ]
    var = [u ** 2 for _, _, u, _ in terms]
    tot = sum(var)
    for (name, typ, u, dof), v in zip(terms, var):
        print(f"  {name:<34}{typ:>6}{u:13.5f}{v/tot*100:15.2f} %")
    uc = math.sqrt(tot)
    print(f"  combined standard uncertainty u_c = {uc:.5f}")
    nu_a = 5
    nu_eff = uc ** 4 / (var[0] ** 2 / nu_a)
    print(f"  Welch-Satterthwaite effective dof = {nu_eff:.1f}")
    for k in (1.0, 2.0, 1.99):
        print(f"  coverage factor k = {k:.2f} -> expanded U = {k*uc:.5f}")
    print("  -> with nu_eff = {:.0f} the k = 2 factor is the t-factor to within".format(nu_eff))
    print("     1 %, so the small-sample correction does not matter here; with")
    print("     n = 3 it would.")


def section_2():
    banner(2, "Why a small repeat count changes the coverage factor")
    print(f"  {'n repeats':>10}{'dof':>5}{'t(95 %)':>10}{'U/u_c':>8}")
    for n in (2, 3, 4, 6, 10, 20):
        dof = n - 1
        t = {1: 12.71, 2: 4.303, 3: 3.182, 5: 2.571, 9: 2.262, 19: 2.093}[dof]
        print(f"  {n:10d}{dof:5d}{t:10.3f}{t:8.3f}")
    print("  -> with n = 3 the coverage factor is 4.3, not 2: an uncertainty quoted")
    print("     as 'k = 2' from three repeats understates the interval by a factor")
    print("     of two.")


def section_3():
    banner(3, "Budget for a derived property: porosity from a mass difference")
    dm, dm_u = 6.90, 0.020
    v_bulk, v_u = 32.60, 0.050
    rho_w, rho_u = 0.998, 0.0005
    phi = dm / (rho_w * v_bulk)
    terms = [("mass difference", dm_u / dm, dm_u / dm),
             ("bulk volume", v_u / v_bulk, v_u / v_bulk),
             ("fluid density", rho_u / rho_w, rho_u / rho_w)]
    tot = sum(t[1] ** 2 for t in terms)
    print(f"  d_mass = {dm:.2f} +- {dm_u:.3f} g, V_bulk = {v_bulk:.2f} +- {v_u:.3f} cm3, "
          f"rho_w = {rho_w:.3f} +- {rho_u:.4f}")
    print(f"  porosity = d_mass / (rho_w V_bulk) = {phi*100:.4f} %")
    print(f"  {'term':<20}{'relative u':>13}{'variance share':>16}")
    for name, rel, _ in terms:
        print(f"  {name:<20}{rel*100:12.4f} %{(rel**2/tot)*100:15.2f} %")
    u_rel = math.sqrt(tot)
    print(f"  combined relative u = {u_rel*100:.4f} %  -> u = {phi*u_rel*100:.4f} "
          f"porosity points")
    print(f"  expanded U (k = 2) = {2*phi*u_rel*100:.4f} points")
    print("  -> the mass difference dominates: improving the volume measurement")
    print("     would change nothing, and the balance resolution is the lever.")


def section_4():
    banner(4, "Reporting: significant digits and what the interval says")
    u = 0.0035714        # dimensionless; 0.3571 % of the value
    phi = 0.212081
    print(f"  value = {phi*100:.4f} % with u = {u*100:.4f} % (dimensionless {u:.7f})")
    for k in (1.0, 2.0):
        U = k * u
        print(f"  u = {u:.6f} -> U(k={k:.0f}) = {U:.6f}; "
              f"reported: {phi*100:.2f} % +- {U*100:.2f} %")
    print(f"  over-rounded: {phi*100:.4f} % +- {U*100:.1f} % (interval too coarse)")
    print(f"  under-rounded: {phi*100:.6f} % +- {U*100:.5f} % (false precision)")
    print("  -> two significant digits for the uncertainty and the value rounded")
    print("     to the same place: 21.21 % +- 0.71 % (k = 2).")


def section_5():
    banner(5, "Comparing with another laboratory: the En score")
    x_lab, u_lab = 21.35, 0.10
    x_ref, u_ref = 21.10, 0.07
    en = abs(x_lab - x_ref) / math.sqrt(u_lab ** 2 + u_ref ** 2)
    print(f"  laboratory {x_lab:.2f} +- {u_lab:.2f}, reference {x_ref:.2f} "
          f"+- {u_ref:.2f} (porosity points)")
    print(f"  difference = {x_lab-x_ref:+.2f} points, ratio = "
          f"{x_lab/x_ref:.4f} ({100*(x_lab/x_ref-1):+.2f} %)")
    print(f"  En = |x - x_ref| / sqrt(u^2 + u_ref^2) = {en:.4f}")
    print(f"  {'case':<34}{'difference':>11}{'u combined':>12}{'En':>8}")
    for name, d, ul, ur in (("consistent, tight budgets", 0.10, 0.10, 0.07),
                            ("inconsistent (this case)", 0.25, 0.10, 0.07),
                            ("large difference, large budgets", 0.25, 0.30, 0.20),
                            ("small difference, tiny budgets", 0.05, 0.02, 0.01)):
        e = abs(d) / math.sqrt(ul ** 2 + ur ** 2)
        print(f"  {name:<34}{d:11.2f}{math.sqrt(ul**2+ur**2):12.4f}{e:8.3f}")
    print("  -> En < 1 is consistent, En > 1 is not: the score compares the")
    print("     difference with the *combined* uncertainty, so a large difference")
    print("     can be consistent when the budgets are large and vice versa.")


def section_6():
    banner(6, "Repeatability versus reproducibility: where the variance lives")
    s_repeat, s_between = 0.08, 0.35
    s_repro = math.sqrt(s_repeat ** 2 + s_between ** 2)
    print(f"  within-laboratory repeatability s_r = {s_repeat:.2f} points")
    print(f"  between-specimen sd              s_L = {s_between:.2f} points")
    print(f"  reproducibility sd = sqrt(s_r^2 + s_L^2) = {s_repro:.4f} points")
    print(f"  variance share: within {100*s_repeat**2/s_repro**2:.2f} %, "
          f"between {100*s_between**2/s_repro**2:.2f} %")
    print(f"  {'n repeats':>10}{'se of mean':>13}{'95 % half-width':>17}")
    for n in (1, 2, 3, 6, 12):
        se = s_repro / math.sqrt(n)
        print(f"  {n:10d}{se:13.4f}{1.96*se:17.4f}")
    n_needed = (1.96 * s_repro / 0.10) ** 2
    print(f"  to reach a 0.10-point half-width: n = (1.96 s / t)^2 = {n_needed:.0f}")
    print("  -> the between-specimen term dominates, so repeating one specimen")
    print("     buys nothing: the count that matters is the number of specimens.")


def main():
    print()
    banner(0, "LABORATORY UNCERTAINTY AND REPORTING: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no certificate,")
    print("laboratory standard or measured value is reproduced.")


if __name__ == "__main__":
    main()
