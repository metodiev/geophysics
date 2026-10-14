"""Radioactive decay, half-life and dating.

Run:  python3 radioactive_decay_demo.py
Requires: Python standard library only.

Companion to lesson 02-09-02. This is the module's numerical-verification
script: it integrates the decay law with fixed-step Euler and fourth-order
Runge-Kutta schemes and compares both against the closed-form solution, it
locates the half-life by root finding to machine precision, it checks that the
Bateman two-member chain and the secular-equilibrium condition are what the ODE
integration produces, and it recovers a synthetic Rb-Sr isochron age by least
squares.

Half-lives and isotopic abundances are *tabulated* inputs, not derived ones.
Every value used below is printed with the label TABULATED so that the reader
never mistakes it for a computed quantity. Compilations differ in the last
digits of every one of them; lesson 02-09-02 states which compilation a value
must be taken from and why.

The script:

1. Converts a tabulated half-life into a decay constant in s^-1 and a^-1, and
   checks the unit algebra explicitly.
2. Verifies the analytic decay law N(t) = N0 exp(-lambda t) against explicit
   Euler and RK4 integration, reporting the measured convergence order.
3. Locates T1/2 by bisection on N(t)/N0 - 1/2 and reports the residual.
4. Computes specific activities: Bq per gram of a pure nuclide, and Bq per kg of
   rock per ppm (or per %) of an element in secular equilibrium.
5. Integrates a two-member chain and compares it with the exact Bateman
   solution, then integrates 238U -> 234Th to secular equilibrium.
6. Fits a synthetic Rb-Sr isochron and reports the recovered age, the initial
   ratio, and the error made by quoting a single-sample model age.
7. Contrasts the two radiocarbon half-lives and quantifies the age difference.
8. Solves the Dodson closure-temperature equation and shows its dependence on
   cooling rate.
"""

import math

# --------------------------------------------------------------------------
# Tabulated inputs.  LABEL: commonly tabulated values; compilations differ.
# --------------------------------------------------------------------------

YEAR = 3.15576e7            # s, Julian year (365.25 d) -- a definition, exact
DAY = 86400.0

# Half-lives in years (LABELLED AS TABULATED, differ between compilations).
T_HALF_A = {
    "C-14  (Libby, conventional)": 5568.0,     # the value behind "conventional" 14C ages
    "C-14  (Cambridge)": 5730.0,               # the closer-to-physical value
    "K-40": 1.248e9,
    "Rb-87": 4.88e10,
    "U-238": 4.468e9,
    "U-235": 7.038e8,
    "Th-232": 1.405e10,
    "Cs-137": 30.08,
    "Sr-90": 28.79,
    "Ra-226": 1600.0,
    "H-3": 12.32,
}
T_HALF_D = {"Rn-222": 3.8235, "Th-234": 24.10}   # days

# Molar masses in g/mol (IUPAC tabulated).
MOLAR_MASS = {
    "C-14  (Libby, conventional)": 14.003242,
    "C-14  (Cambridge)": 14.003242,
    "K-40": 39.963998,
    "Rb-87": 86.909181,
    "U-238": 238.050788,
    "U-235": 235.043930,
    "Th-232": 232.038055,
    "Cs-137": 136.907090,
    "Sr-90": 89.907738,
    "Ra-226": 226.025410,
    "H-3": 3.016049,
    "Rn-222": 222.017578,
    "Th-234": 234.043601,
}

# Isotopic abundances of naturally occurring elements (TABULATED).
ABUNDANCE_40K = 1.17e-4        # 0.0117 atom-% of natural K
MOLAR_MASS_NAT_K = 39.0983     # g/mol, IUPAC standard atomic weight of K
ABUNDANCE_238U = 0.992745
ABUNDANCE_235U = 0.007200
MOLAR_MASS_NAT_U = 238.02891
MOLAR_MASS_NAT_TH = 232.0377

AVOGADRO = 6.02214076e23       # mol^-1, exact (SI)
LN2 = math.log(2.0)
R_GAS = 8.31446261815324       # J mol^-1 K^-1, exact (SI)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def lam(half_life_s):
    """Decay constant in s^-1 from a half-life in seconds."""
    return LN2 / half_life_s


def order_check(errors, steps):
    """Observed convergence order from successive errors and step sizes."""
    orders = []
    for i in range(1, len(errors)):
        if errors[i] == 0.0 or errors[i - 1] == 0.0:
            orders.append(float("nan"))
            continue
        orders.append(
            math.log(errors[i - 1] / errors[i]) / math.log(steps[i - 1] / steps[i])
        )
    return orders


# --------------------------------------------------------------------------
# 1. Half-life to decay constant, with the units shown
# --------------------------------------------------------------------------

def part1_decay_constants():
    section("1. Half-life -> decay constant, and the unit algebra")
    print("  lambda = ln2 / T1/2 .  With T1/2 in s, lambda is in s^-1.")
    print("  (Example of the algebra for U-238 by hand:")
    print(f"    lambda = 0.693147 / {4.468e9 * YEAR:.6e} s = "
          f"{lam(4.468e9 * YEAR):.6e} s^-1 )")
    print()
    print(f"{'nuclide':<28}{'T1/2 (a)':>13}{'lambda (1/s)':>16}"
          f"{'lambda (1/a)':>14}{'mean life (a)':>15}")
    for name, th in T_HALF_A.items():
        l = lam(th * YEAR)
        print(f"{name:<28}{th:>13.6g}{l:>16.6e}{l * YEAR:>14.6e}"
              f"{1.0 / (l * YEAR):>15.4g}")
    for name, th in T_HALF_D.items():
        l = lam(th * DAY)
        print(f"{name + ' (days)':<28}{th / 365.25:>13.6g}{l:>16.6e}"
              f"{l * YEAR:>14.6e}{1.0 / (l * YEAR):>15.4g}")
    print()
    print("  Dimensional check: ln2 is dimensionless and T1/2 has unit s, so")
    print("  lambda has unit s^-1. Multiplying a per-second constant by the")
    print("  year in seconds converts it to a per-year constant, and the two")
    print("  must therefore satisfy (lambda per year) = (lambda per second)")
    print("  x (seconds per year). Check it on U-238 by hand:")
    l238 = lam(T_HALF_A["U-238"] * YEAR)
    print(f"    {l238:.6e} s^-1 x {YEAR:.6e} s/a = {l238 * YEAR:.6e} a^-1")
    print(f"    and ln2 / T1/2[in a] = ln2 / 4.468e9 = "
          f"{LN2 / T_HALF_A['U-238']:.6e} a^-1")
    print("  The mean life is 1/lambda = T1/2/ln2, longer than the half-life")
    print("  by the factor 1.4427; for K-40 that is 1.80 Ga against 1.248 Ga.")


# --------------------------------------------------------------------------
# 2. Verification of dN/dt = -lambda N against Euler and RK4
# --------------------------------------------------------------------------

def part2_verification():
    section("2. The decay law: analytic solution versus numerical integration")
    th = 1.248e9
    l = lam(th * YEAR)
    n0 = 1.0
    t_end = 2.0 * th * YEAR

    def rhs(n):
        return -l * n

    print(f"  Using K-40, tabulated T1/2 = {th:.6g} a, lambda = {l:.6e} s^-1.")
    print(f"  Integrating from t = 0 to t = 2 T1/2 = {t_end:.6e} s.")
    print()
    print(f"{'step (s)':>12}{'steps':>8}{'Euler err':>14}{'order':>8}"
          f"{'RK4 err':>14}{'order':>8}")
    prev = {}
    for steps in (100, 200, 400, 800, 1600, 3200):
        h = t_end / steps
        # Explicit Euler
        n = n0
        for _ in range(steps):
            n += h * rhs(n)
        e_euler = abs(n - n0 * math.exp(-l * t_end))
        # Classical RK4
        n = n0
        for _ in range(steps):
            k1 = rhs(n)
            k2 = rhs(n + 0.5 * h * k1)
            k3 = rhs(n + 0.5 * h * k2)
            k4 = rhs(n + h * k3)
            n += h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        e_rk4 = abs(n - n0 * math.exp(-l * t_end))
        o_euler = o_rk4 = float("nan")
        if "e" in prev and prev["e"] > 0.0 and e_euler > 0.0:
            o_euler = math.log(prev["e"] / e_euler) / math.log(prev["h"] / h)
        if "r" in prev and prev["r"] > 0.0 and e_rk4 > 0.0:
            o_rk4 = math.log(prev["r"] / e_rk4) / math.log(prev["h"] / h)
        print(f"{h:>12.4e}{steps:>8}{e_euler:>14.4e}{o_euler:>8.3f}"
              f"{e_rk4:>14.4e}{o_rk4:>8.3f}")
        prev = {"h": h, "e": e_euler, "r": e_rk4}

    print()
    analytic = n0 * math.exp(-2.0 * LN2)
    print(f"  Analytic N(2 T1/2)/N0 = exp(-2 ln2) = {analytic:.15f} = 1/4 exactly.")
    print(f"  |analytic - 0.25| = {abs(analytic - 0.25):.3e} (round-off only).")
    print("  Euler is first order and RK4 is fourth order: the 'order' columns")
    print("  show that, which is the evidence that both are implemented")
    print("  correctly. The RK4 error at 100 steps is already smaller than the")
    print("  Euler error at 3200 steps.")
    print("  The last RK4 row is the exception that proves the rule: its error")
    print("  has reached the ~1e-16 round-off floor of double precision, so its")
    print("  measured order collapses. Refining a scheme below the round-off")
    print("  floor cannot improve the answer, and reporting an order from such")
    print("  a row would be reporting numerical noise.")


# --------------------------------------------------------------------------
# 3. Half-life by root finding
# --------------------------------------------------------------------------

def part3_root_finding():
    section("3. Locating T1/2 by bisection, to machine precision")
    for th in (5568.0, 4.468e9, 30.08):
        l = lam(th * YEAR)
        f = lambda t: math.exp(-l * t) - 0.5
        lo, hi = 0.0, 4.0 * th * YEAR
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if f(lo) * f(mid) <= 0.0:
                hi = mid
            else:
                lo = mid
        root = 0.5 * (lo + hi)
        print(f"  T1/2 tabulated = {th:>10.6g} a   located root = "
              f"{root / YEAR:>18.12f} a   residual |N/N0 - 1/2| = "
              f"{abs(f(root)):.3e}")
    print()
    print("  The residual is 0.0 at double precision: bisection converges onto")
    print("  the tabulated number itself, exactly. All the uncertainty in a")
    print("  decay constant therefore comes from the tabulated half-life and")
    print("  never from the arithmetic, which is why the half-life you quote")
    print("  must be the one you actually looked up, with its compilation.")


# --------------------------------------------------------------------------
# 4. Specific activities
# --------------------------------------------------------------------------

def part4_specific_activity():
    section("4. Specific activity: pure nuclide, and per ppm in rock")
    print("  For a pure nuclide, A_s = lambda N_A / M  (Bq per gram, M in g/mol).")
    print()
    print(f"{'nuclide':<28}{'A_s (Bq/g)':>16}{'A_s (Bq/kg)':>16}")
    for name in ("C-14  (Cambridge)", "K-40", "Rb-87", "U-238", "U-235",
                 "Th-232", "Cs-137", "Ra-226"):
        l = lam(T_HALF_A[name] * YEAR)
        a_s = l * AVOGADRO / MOLAR_MASS[name]
        print(f"{name:<28}{a_s:>16.6e}{a_s * 1000.0:>16.6e}")

    print()
    print("  Element concentrations in rock, assuming secular equilibrium.")
    print("  Number of atoms per kg of rock: N = w * N_A / M  (w = mass fraction)")
    print()
    rows = (
        ("238U, 1 ppm", ABUNDANCE_238U * 1e-6, MOLAR_MASS_NAT_U,
         T_HALF_A["U-238"]),
        ("235U, 1 ppm natural U", ABUNDANCE_235U * 1e-6, MOLAR_MASS_NAT_U,
         T_HALF_A["U-235"]),
        ("232Th, 1 ppm", 1e-6, MOLAR_MASS_NAT_TH, T_HALF_A["Th-232"]),
        ("40K, 1 % natural K", ABUNDANCE_40K * 1e-2, MOLAR_MASS_NAT_K,
         T_HALF_A["K-40"]),
    )
    print(f"{'concentration':<24}{'N (atoms/kg)':>16}{'lambda (1/s)':>14}"
          f"{'A (Bq/kg)':>14}")
    for label, w, m, th in rows:
        n = w * AVOGADRO * 1000.0 / m
        l = lam(th * YEAR)
        print(f"{label:<24}{n:>16.6e}{l:>14.6e}{l * n:>14.4f}")

    print()
    n_u = ABUNDANCE_238U * 1e-6 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_U
    n_th = 1e-6 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_TH
    n_k = ABUNDANCE_40K * 1e-2 * AVOGADRO * 1000.0 / MOLAR_MASS_NAT_K
    a_u = lam(T_HALF_A["U-238"] * YEAR) * n_u
    a_th = lam(T_HALF_A["Th-232"] * YEAR) * n_th
    a_k = lam(T_HALF_A["K-40"] * YEAR) * n_k
    print("  The numbers quoted in the textbook literature are 12.4 Bq/kg for")
    print(f"  1 ppm U, 4.1 Bq/kg for 1 ppm Th and 313 Bq/kg for 1 % K. This")
    print(f"  script, with the tabulated inputs listed at the top, gives "
          f"{a_u:.2f}, {a_th:.2f}")
    print(f"  and {a_k:.1f} Bq/kg. The differences are 1-2 per cent and come")
    print("  entirely from the choice of tabulated half-life and abundance:")
    print("  this is the concrete reason a conversion factor copied from a")
    print("  paper must be recomputed from the compilation that paper used.")

    print()
    ratio = (lam(T_HALF_A["U-235"] * YEAR) * ABUNDANCE_235U /
             (lam(T_HALF_A["U-238"] * YEAR) * ABUNDANCE_238U))
    print(f"  Activity ratio 235U/238U in natural uranium = {ratio:.6f}, i.e.")
    print(f"  1/{1.0 / ratio:.3f}. It is not 1/137.9 (the abundance ratio) and")
    print("  not 1: the two isotopes have different decay constants, and")
    print("  gamma spectrometry of natural uranium always sees the 235U line")
    print("  at 185.7 keV riding on the 238U series.")


# --------------------------------------------------------------------------
# 5. Chains: Bateman and secular equilibrium
# --------------------------------------------------------------------------

def rk4_system(rhs, y0, t_end, steps):
    y = list(y0)
    h = t_end / steps
    for _ in range(steps):
        k1 = rhs(y)
        y2 = [y[i] + 0.5 * h * k1[i] for i in range(len(y))]
        k2 = rhs(y2)
        y3 = [y[i] + 0.5 * h * k2[i] for i in range(len(y))]
        k3 = rhs(y3)
        y4 = [y[i] + h * k3[i] for i in range(len(y))]
        k4 = rhs(y4)
        y = [y[i] + h * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
             for i in range(len(y))]
    return y


def part5_chains():
    section("5. Parent-daughter chains: Bateman, and secular equilibrium")
    # A generic parent/daughter pair with convenient half-lives, so that the
    # ODE integration and the closed form can be compared directly.
    t_p, t_d = 10.0 * YEAR, 1.0 * YEAR
    lp, ld = lam(t_p), lam(t_d)
    n0 = 1.0

    def rhs(y):
        return [-lp * y[0], lp * y[0] - ld * y[1]]

    bateman = lambda t: (n0 * lp / (ld - lp) * (math.exp(-lp * t)
                                                - math.exp(-ld * t)))
    print(f"  Generic pair: T1/2(parent) = 10 a, T1/2(daughter) = 1 a.")
    print(f"{'t (a)':>8}{'N_d numeric':>16}{'Bateman closed form':>22}"
          f"{'rel diff':>12}")
    for t in (0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0):
        ts = t * YEAR
        num = rk4_system(rhs, [n0, 0.0], ts, 20000)[1]
        exact = bateman(ts)
        print(f"{t:>8.2f}{num:>16.9e}{exact:>22.9e}"
              f"{abs(num - exact) / max(exact, 1e-300):>12.3e}")
    print()
    print("  Equal activities require lambda_p N_p = lambda_d N_d. Near secular")
    print("  equilibrium the daughter's activity settles to the parent's, which")
    print("  is why a gamma-ray spectrometer counting a 238U-series line sees")
    print("  the whole series at one activity.")

    print()
    print("  Now the real top of the 238U series: 238U -> 234Th -> 234Pa ...")
    l_238 = lam(T_HALF_A["U-238"] * YEAR)
    l_234th = lam(T_HALF_D["Th-234"] * DAY)
    t_end = 365.0 * DAY

    def rhs_u(y):
        return [-l_238 * y[0], l_238 * y[0] - l_234th * y[1]]

    y0 = [1.0, 0.0]
    print(f"{'t (d)':>8}{'A(238U)':>16}{'A(234Th)':>16}{'ratio Th/U':>14}")
    last = None
    for t_d in (1.0, 10.0, 30.0, 100.0, 365.0):
        y = rk4_system(rhs_u, y0, t_d * DAY, 200000)
        a1, a2 = l_238 * y[0], l_234th * y[1]
        last = a2 / a1
        print(f"{t_d:>8.1f}{a1:>16.9e}{a2:>16.9e}{last:>14.6f}")
    print()
    print("  After one year the activity ratio is")
    print(f"  {last:.6f}, i.e. within {abs(1.0 - last):.1e} of unity, so 234Th")
    print("  is in secular equilibrium with 238U to better than 0.003 per")
    print("  cent. The whole of that deficit is explained analytically: one")
    n_hl = 365.0 / T_HALF_D["Th-234"]
    print(f"  year is {n_hl:.2f} half-lives of 234Th, so the un-built daughter")
    print(f"  is 2^-{n_hl:.2f} = {2.0 ** -n_hl:.3e} of the equilibrium value,")
    print(f"  against the measured {abs(1.0 - last):.3e}: the two agree to")
    print("  three significant figures, which is the check that the model in")
    print("  the code is the model in the equation. The parent, meanwhile, has")
    print(f"  decayed by {100.0 * (1.0 - math.exp(-l_238 * 365.0 * DAY)):.2e}")
    print("  per cent in the same year: this ratio of timescales, 24 days")
    print("  against 4.468 Ga, is what 'secular' means quantitatively.")


# --------------------------------------------------------------------------
# 6. Isochron
# --------------------------------------------------------------------------

def part6_isochron():
    section("6. Rb-Sr isochron: recovering a known age from synthetic data")
    t_half_rb = T_HALF_A["Rb-87"] * YEAR
    l_rb = lam(t_half_rb)
    l_rb_a = LN2 / T_HALF_A["Rb-87"]
    true_age = 350.0e6            # a, the age we build into the synthetic data
    r0 = 0.7065                   # initial 87Sr/86Sr

    # Synthetic whole-rock analyses: x = 87Rb/86Sr, y = 87Sr/86Sr.
    xs = [0.15, 0.42, 0.95, 1.60, 2.45, 3.30, 4.10, 5.20]
    ys = [r0 + (math.exp(l_rb_a * true_age) - 1.0) * x for x in xs]
    # A small, deterministic perturbation so the fit is a fit and not a lookup.
    noise = [2e-4, -3e-4, 1e-4, -2e-4, 3e-4, -1e-4, 2e-4, -3e-4]
    ys = [y + n for y, n in zip(ys, noise)]

    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = my - slope * mx
    resid = [y - (intercept + slope * x) for x, y in zip(xs, ys)]
    syy = sum(r ** 2 for r in resid) / (n - 2)
    sig_slope = math.sqrt(syy / sxx)
    age = math.log1p(slope) / l_rb_a
    sig_age = sig_slope / ((1.0 + slope) * l_rb_a)

    print(f"  TABULATED T1/2(87Rb) = {T_HALF_A['Rb-87']:.6g} a, "
          f"lambda = {l_rb_a:.6e} a^-1")
    print(f"  (lambda = 1.42e-11 a^-1 is the value recommended by the IUGS")
    print(f"  subcommission; {l_rb:.6e} s^-1 is the same constant in SI.)")
    print(f"  True age built into the data: {true_age:.6e} a, "
          f"initial ratio {r0:.4f}")
    print()
    print(f"{'87Rb/86Sr':>12}{'87Sr/86Sr':>14}{'residual':>12}")
    for x, y, r in zip(xs, ys, resid):
        print(f"{x:>12.3f}{y:>14.6f}{r:>12.2e}")
    print()
    print(f"  Least squares slope     = {slope:.6e}  +/- {sig_slope:.2e}")
    print(f"  Least squares intercept = {intercept:.6f}  (true {r0:.4f})")
    print(f"  Recovered age           = {age:.6e} a  +/- {sig_age:.2e}")
    print(f"  Relative error in age   = "
          f"{abs(age - true_age) / true_age:.3e}")

    # The model-age trap: one sample, assuming an initial ratio by fiat.
    x1, y1 = xs[3], ys[3]
    assume = 0.7040
    model_age = math.log1p((y1 - assume) / x1) / l_rb_a
    assume2 = 0.7100
    model_age2 = math.log1p((y1 - assume2) / x1) / l_rb_a
    print()
    print(f"  Model age of the single sample with 87Rb/86Sr = {x1:.2f}:")
    print(f"    assuming initial ratio {assume:.4f} -> {model_age / 1e6:.1f} Ma")
    print(f"    assuming initial ratio {assume2:.4f} -> {model_age2 / 1e6:.1f} Ma")
    print(f"  The isochron age is {age / 1e6:.1f} Ma whatever the initial ratio,")
    print("  because the intercept is fitted, not assumed. A model age is only")
    print("  as good as the assumed initial ratio, and the two numbers above")
    print(f"  differ by {abs(model_age - model_age2) / 1e6:.1f} Ma for a change of")
    print("  0.006 in the assumption.")


# --------------------------------------------------------------------------
# 7. Radiocarbon and the half-life choice
# --------------------------------------------------------------------------

def part7_radiocarbon():
    section("7. Radiocarbon: the half-life you choose is part of the answer")
    # Specific activity of modern carbon, from the Cambridge half-life.
    l_cam = LN2 / (5730.0 * YEAR)
    l_lib = LN2 / (5568.0 * YEAR)
    print(f"  TABULATED T1/2(C-14): {5568.0:.0f} a (Libby, used for the")
    print(f"  'conventional radiocarbon age') and {5730.0:.0f} a (Cambridge).")
    print(f"  lambda_libby = {l_lib:.6e} s^-1, lambda_cambridge = {l_cam:.6e} s^-1")
    print()
    print(f"{'measured A/A_modern':>22}{'Libby age (a)':>16}"
          f"{'Cambridge age (a)':>19}{'difference (a)':>16}")
    for ratio in (0.9, 0.75, 0.5, 0.3, 0.1, 0.05):
        t_lib = -math.log(ratio) / l_lib / YEAR
        t_cam = -math.log(ratio) / l_cam / YEAR
        print(f"{ratio:>22.3f}{t_lib:>16.1f}{t_cam:>19.1f}"
              f"{t_cam - t_lib:>16.1f}")
    print()
    print("  The 2.9 per cent difference in half-life is a 2.9 per cent")
    print("  difference in age: at 10 000 a that is about 300 a. That is the")
    print("  entire reason 'conventional radiocarbon ages' are defined with")
    print("  the Libby half-life and then *calibrated* against a measured")
    print("  curve, rather than converted to calendar years by the decay law")
    print("  alone.")


# --------------------------------------------------------------------------
# 8. Closure temperature
# --------------------------------------------------------------------------

def part8_closure_temperature():
    section("8. Closure temperature: Dodson's equation and the cooling rate")
    # Dodson (1973): E/(R Tc) = ln( A R Tc^2 D0 / (E a^2 dT/dt) )
    # Geometry: A = 55 (sphere), 27 (cylinder), 8.7 (plane sheet).
    a_geom = 55.0
    a_size = 0.5e-3            # m, effective diffusion radius of the grain
    e_act = 200e3              # J/mol, illustrative activation energy
    d0 = 1.0e-4                # m^2/s, illustrative frequency factor
    print("  Model parameters used (ILLUSTRATIVE, not measured values):")
    print(f"    activation energy E = {e_act / 1e3:.0f} kJ/mol")
    print(f"    frequency factor D0 = {d0:.1e} m^2/s")
    print(f"    diffusion radius a = {a_size * 1e3:.2f} mm, sphere (A = {a_geom})")
    print()
    print(f"{'cooling rate (K/Ma)':>22}{'Tc (K)':>12}{'Tc (C)':>12}")
    for rate_ma in (1.0, 10.0, 100.0, 1000.0):
        rate = rate_ma / (1e6 * YEAR)     # K/s
        tc = e_act / (R_GAS * 400.0)      # initial guess
        for _ in range(200):
            rhs = math.log(a_geom * R_GAS * tc * tc * d0
                           / (e_act * a_size * a_size * rate))
            tc = e_act / (R_GAS * rhs)
        print(f"{rate_ma:>22.4g}{tc:>12.1f}{tc - 273.15:>12.1f}")
    print()
    print("  Slower cooling gives a lower closure temperature, because the")
    print("  grain has longer to lose its daughter. This is why a 'closure")
    print("  temperature' without a stated cooling rate is not a number: it is")
    print("  the reason different chronometers in the same rock record")
    print("  different ages, and the basis of thermochronology.")


def main():
    part1_decay_constants()
    part2_verification()
    part3_root_finding()
    part4_specific_activity()
    part5_chains()
    part6_isochron()
    part7_radiocarbon()
    part8_closure_temperature()


if __name__ == "__main__":
    main()
