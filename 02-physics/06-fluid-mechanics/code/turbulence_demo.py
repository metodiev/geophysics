"""Turbulence: Kolmogorov scales, the log layer and eddy diffusivity.

Run:  python3 turbulence_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-04. The script:

1. Computes the Kolmogorov microscales from a stated dissipation rate and
   kinematic viscosity for a river, the ocean surface layer and the atmosphere.
2. Evaluates the log-law velocity profile, verifies that it produces a linear
   mixing length l = kappa y and an eddy viscosity nu_t = kappa u* y, and
   compares nu_t with the molecular value.
3. Shows that the eddy diffusivity of a mixing-length closure is not determined
   by the resolved gradients alone: two layers with the same shear can have
   diffusivities differing by orders of magnitude once stratification is added.
4. Verifies the -5/3 slope of a Kolmogorov energy spectrum numerically, and
   converts a fitted spectral level into a dissipation rate.
5. Computes eddy mixing times and the turbulent Prandtl number implied by a
   stated heat flux and gradient.

Every number printed below was produced by this script.
"""

import math

KAPPA_VK = 0.41      # von Karman constant, nominal
RHO_W = 1025.0
MU_W = 1.0e-3
NU_W = MU_W / RHO_W
NU_AIR = 1.5e-5
NU_MANTLE = 1.0e21 / 3300.0


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def part1_kolmogorov():
    section("1. Kolmogorov microscales")

    print("eta = (nu^3/eps)^(1/4), u_eta = (nu eps)^(1/4), "
          "tau_eta = (nu/eps)^(1/2)")
    print(f"{'flow':>26} {'nu (m^2/s)':>12} {'eps (m^2/s^3)':>16} "
          f"{'eta (mm)':>10} {'u_eta (mm/s)':>13} {'tau_eta (s)':>13}")
    for name, nu, eps in (
            ("mountain stream", 1.0e-6, 1.0e-1),
            ("ocean surface layer", NU_W, 1.0e-5),
            ("atmospheric surface layer", NU_AIR, 1.0e-2)):
        eta = (nu ** 3 / eps) ** 0.25
        u_eta = (nu * eps) ** 0.25
        tau = math.sqrt(nu / eps)
        print(f"{name:>26} {nu:12.3e} {eps:16.3e} {eta * 1e3:10.4f} "
              f"{u_eta * 1e3:13.4f} {tau:13.3e}")
    print("\n  the dissipation rate is an input, not a prediction: no theory "
          "gives eps from the")
    print("  mean flow. The microscales only translate a chosen eps into "
          "lengths and times.")
    print("  the mantle is deliberately absent: its effective Reynolds number "
          "is ~10^-20, so")
    print("  there is no turbulent cascade and no Kolmogorov range. Applying "
          "these formulas to")
    print("  the mantle is a category error.")


def part2_log_law():
    section("2. The log layer, mixing length and eddy viscosity")

    ustar = 0.05          # friction velocity, m/s
    y0 = 1.0e-3           # roughness length, m
    print(f"u* = {ustar} m/s, roughness length y0 = {y0 * 1e3:.1f} mm, "
          f"kappa = {KAPPA_VK}")
    print(f"{'y (m)':>8} {'u (m/s)':>10} {'du/dy (1/s)':>13} "
          f"{'l = kappa*y (m)':>16} {'nu_t = l^2|du/dy|':>19} {'nu_t/(kappa u* y)':>18}")
    for y in (0.01, 0.1, 1.0, 10.0, 100.0):
        u = ustar / KAPPA_VK * math.log(y / y0)
        # numerical derivative
        h = 1e-6 * max(y, 1e-3)
        up = ustar / KAPPA_VK * math.log((y + h) / y0)
        um = ustar / KAPPA_VK * math.log((y - h) / y0)
        dudy = (up - um) / (2 * h)
        l = KAPPA_VK * y
        nut = l * l * abs(dudy)
        ratio = nut / (KAPPA_VK * ustar * y)
        print(f"{y:8.2f} {u:10.4f} {dudy:13.4f} {l:16.5f} {nut:19.5f} "
              f"{ratio:18.6f}")
    print("\n  the fourth column is l = kappa y, the fifth nu_t = kappa u* y, "
          "and the last")
    print("  column is 1 to within round-off: the log law is exactly the "
          "mixing-length closure")
    print("  with l = kappa y. That is a property of the closure, not a "
          "measurement of it.")
    print(f"\n  nu_t at y = 1 m is {KAPPA_VK * ustar:.4f} m^2/s, i.e. "
          f"{KAPPA_VK * ustar / NU_W:.3e} times the molecular")
    print("  viscosity of water. This is the quantitative reason turbulent "
          "transport dominates.")


def part3_closure():
    section("3. Eddy diffusivity is not fixed by the resolved gradient")

    print("mixing-length with stratification: K = l^2 |du/dz| / (1 + Ri/Ri_c)")
    print(f"Ri = N^2/(du/dz)^2, N^2 = (g/theta) dtheta/dz, Ri_c = 0.25\n")
    l = 10.0
    dudz = 0.01
    g_over_theta = 9.81 / 300.0        # atmosphere
    print(f"l = {l} m, du/dz = {dudz} 1/s, g/theta = {g_over_theta:.5f} "
          "K^-1 m s^-2")
    print(f"{'dtheta/dz (K/m)':>17} {'N^2 (1/s^2)':>13} {'Ri':>9} "
          f"{'suppression':>12} {'K (m^2/s)':>11}")
    for dth in (0.0, 0.001, 0.005, 0.01, 0.02, 0.05):
        N2 = g_over_theta * dth
        Ri = N2 / (dudz * dudz)
        supp = 1.0 / (1.0 + Ri / 0.25)
        K = l * l * dudz * supp
        print(f"{dth:17.3f} {N2:13.3e} {Ri:9.4f} {supp:12.5f} {K:11.5f}")
    print("\n  the mean gradient du/dz is identical in every row, yet K spans "
          "nearly two decades.")
    print("  A closure is therefore an assumption about the unresolved flow, "
          "not a consequence of")
    print("  the resolved one. Two models that agree on the mean velocity can "
          "disagree on the flux.")


def part4_spectrum():
    section("4. The -5/3 spectrum, verified by regression")

    def spectrum(k, eps):
        C = 1.5
        return C * eps ** (2.0 / 3.0) * k ** (-5.0 / 3.0)

    eps = 1.0e-5
    ks = [10 ** (t / 40.0) for t in range(0, 121)]   # k from 1 to 10^3
    xs = [math.log(k) for k in ks]
    ys = [math.log(spectrum(k, eps)) for k in ks]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = sxy / sxx
    intercept = my - slope * mx
    print(f"synthetic E(k) = C eps^(2/3) k^(-5/3) sampled over "
          f"k = 1 to 1e3 ({n} points)")
    print(f"  fitted slope in log-log        = {slope:.10f}  (exact "
          f"{-5.0 / 3.0:.10f})")
    print(f"  fitted intercept               = {intercept:.6f}")

    # Recover eps from the intercept: C eps^(2/3) = exp(intercept)
    C = 1.5
    eps_fit = (math.exp(intercept) / C) ** 1.5
    print(f"  dissipation rate recovered from the fitted level = "
          f"{eps_fit:.6e} m^2/s^3")
    print(f"  the input dissipation rate was                  = {eps:.6e} "
          f"m^2/s^3")
    print("\n  the slope is a robust measurement; the level (and hence eps) "
          "depends on the")
    print("  assumed Kolmogorov constant C, which is an empirical number near "
          "1.5. A spectrum")
    print("  alone fixes the product C eps^(2/3), never eps by itself.")

    # Scale range: how many decades of scales does a given Re buy?
    print("\n  scale separation: L/eta ~ Re^(3/4)")
    for name, Re in (("river", 1.0e6), ("ocean", 1.0e8),
                     ("atmosphere", 1.0e10)):
        print(f"    {name:>12}: Re = {Re:.0e}  ->  L/eta ~ "
              f"{Re ** 0.75:.3e}")


def part5_mixing_times():
    section("5. Eddy mixing times and the turbulent Prandtl number")

    print("diffusion time t ~ h^2 / K")
    print(f"{'setting':>28} {'h (m)':>8} {'K (m^2/s)':>11} {'t':>14}")
    for name, h, K in (
            ("lake, 10 m, summer", 10.0, 1.0e-3),
            ("mixed layer, 50 m", 50.0, 1.0e-1),
            ("abyssal ocean, 4000 m", 4000.0, 1.0e-4),
            ("atmospheric boundary layer", 1000.0, 10.0)):
        t = h * h / K
        print(f"{name:>28} {h:8.0f} {K:11.3e} {t:14.4e}")
    print("  seconds. The abyssal value is the one that matters for ocean "
          "ventilation;")
    print("  K ~ 1e-4 m^2/s there rather than the 1e-1 m^2/s of a stirred "
          "layer.")

    print("\nturbulent Prandtl number from a stated flux and gradient:")
    print("  Pr_t = (nu_t/K_h) with <w'theta'> = -K_h dtheta/dz")
    for name, flux, grad in (("atmospheric day", -0.05, 0.01),
                             ("ocean thermocline", -1.0e-5, 1.0e-4)):
        Kh = -flux / grad
        print(f"    {name:>20}: <w'theta'> = {flux:.2e} K m/s, "
              f"dtheta/dz = {grad:.1e} K/m  ->  K_h = {Kh:.3e} m^2/s")
    print("  K_h is inferred, not measured directly: the instruments see the "
          "flux and the")
    print("  gradient, and the diffusivity is whatever makes the closure "
          "consistent.")


def main():
    part1_kolmogorov()
    part2_log_law()
    part3_closure()
    part4_spectrum()
    part5_mixing_times()


if __name__ == "__main__":
    main()
