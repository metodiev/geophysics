"""Elastic moduli, their interrelations, and the P/S velocity ratio.

Run:  python3 elastic_moduli_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-04. A granite-like model (rho = 2700 kg/m^3,
lambda = 25 GPa, mu = 30 GPa) is used throughout; the numbers are a consistent
model, not a measurement of any particular rock.

The script:

1. Computes E, nu, K, M, v_p, v_s and v_p/v_s from lambda, mu, rho.
2. Verifies every interrelation numerically, and checks the 6x6 compliance
   built from E and nu against the stiffness built from lambda and mu - an
   independent route that would expose any algebraic slip.
3. Tabulates v_p/v_s against Poisson's ratio and shows the minimum at
   nu = 0 where the ratio is sqrt(2).
4. Does a Gassmann fluid substitution on a synthetic sandstone, showing that
   saturating a gas sand with water raises v_p and lowers v_s, and states the
   regime in which that statement holds.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


RHO, LAMBDA, MU = 2700.0, 25.0e9, 30.0e9


def part1_moduli():
    section("1. From lambda, mu, rho to every other constant")
    E = MU * (3.0 * LAMBDA + 2.0 * MU) / (LAMBDA + MU)
    nu = LAMBDA / (2.0 * (LAMBDA + MU))
    K = LAMBDA + 2.0 * MU / 3.0
    M = LAMBDA + 2.0 * MU
    vp = math.sqrt(M / RHO)
    vs = math.sqrt(MU / RHO)
    print(f"input model: rho = {RHO:.0f} kg/m^3, lambda = {LAMBDA / 1e9:.3f} GPa, "
          f"mu = {MU / 1e9:.3f} GPa")
    print(f"E = mu (3 lambda + 2 mu)/(lambda + mu) = {E / 1e9:.6f} GPa")
    print(f"nu = lambda / (2 (lambda + mu))       = {nu:.9f}")
    print(f"K = lambda + 2 mu/3                   = {K / 1e9:.6f} GPa")
    print(f"M = lambda + 2 mu (= K + 4 mu/3)      = {M / 1e9:.6f} GPa")
    print(f"v_p = sqrt((lambda + 2 mu)/rho)       = {vp:.6f} m/s")
    print(f"v_s = sqrt(mu/rho)                    = {vs:.6f} m/s")
    print(f"v_p/v_s                               = {vp / vs:.9f}")
    print()
    print("  Independent routes to the same numbers:")
    print(f"    E from 9 K G /(3K + G) = "
          f"{9 * K * MU / (3 * K + MU) / 1e9:.6f} GPa")
    print(f"    nu from (3K - 2G)/(2(3K + G)) = {(3 * K - 2 * MU) / (2 * (3 * K + MU)):.9f}")
    print(f"    M from K + 4 mu/3      = {(K + 4 * MU / 3) / 1e9:.6f} GPa")
    print(f"    K from E/(3(1 - 2 nu)) = {E / (3 * (1 - 2 * nu)) / 1e9:.6f} GPa")
    print(f"    mu from E/(2(1 + nu))  = {E / (2 * (1 + nu)) / 1e9:.6f} GPa")
    print(f"    v_p/v_s from sqrt(2(1 - nu)/(1 - 2 nu)) = "
          f"{math.sqrt(2 * (1 - nu) / (1 - 2 * nu)):.9f}")
    print()
    print("  For this model Poisson's ratio is 0.2273 and v_p/v_s is 1.6833. A rock")
    print("  with nu = 0.25 would give exactly sqrt(3) = 1.732, which is why")
    print("  sqrt(3) is the value usually quoted for a 'Poisson solid'.")


def stiffness_from_lambda_mu(lam, mu):
    c11 = lam + 2.0 * mu
    c12 = lam
    c44 = mu
    return [[c11, c12, c12, 0.0, 0.0, 0.0],
            [c12, c11, c12, 0.0, 0.0, 0.0],
            [c12, c12, c11, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, c44, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, c44, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, c44]]


def stiffness_from_E_nu(E, nu):
    lam = E * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
    mu = E / (2.0 * (1.0 + nu))
    return stiffness_from_lambda_mu(lam, mu)


def part2_consistency():
    section("2. Two independent constructions of the stiffness matrix")
    E = MU * (3.0 * LAMBDA + 2.0 * MU) / (LAMBDA + MU)
    nu = LAMBDA / (2.0 * (LAMBDA + MU))
    a = stiffness_from_lambda_mu(LAMBDA, MU)
    b = stiffness_from_E_nu(E, nu)
    worst = max(abs(a[i][j] - b[i][j]) for i in range(6) for j in range(6))
    print(f"E = {E / 1e9:.6f} GPa, nu = {nu:.9f}")
    print(f"max |C(lambda, mu) - C(E, nu)| over 36 entries = {worst:.3e} Pa")
    print()
    print("  Uniaxial stress test, using the compliance directly:")
    # compliance from E, nu
    S = [[0.0] * 6 for _ in range(6)]
    for i in range(3):
        for j in range(3):
            S[i][j] = -nu / E if i != j else 1.0 / E
    for i in range(3):
        S[i + 3][i + 3] = 2.0 * (1.0 + nu) / E
    sigma0 = 10.0e6
    strain = [sum(S[i][j] * (sigma0 if j == 0 else 0.0) for j in range(6))
              for i in range(6)]
    print(f"    applied sigma_11 = {sigma0 / 1e6:.3f} MPa")
    print(f"    eps_11 = {strain[0]:.9e}  vs sigma_11/E = {sigma0 / E:.9e}")
    print(f"    eps_22 = {strain[1]:.9e}  vs -nu sigma_11/E = "
          f"{-nu * sigma0 / E:.9e}")
    print(f"    eps_33 = {strain[2]:.9e}, shear strains "
          f"{strain[3]:.1e}, {strain[4]:.1e}, {strain[5]:.1e}")
    print(f"    implied axial-extension ratio -eps_22/eps_11 = "
          f"{-strain[1] / strain[0]:.9f} (Poisson's ratio)")
    print()
    print("  The uniaxial test is what a rock-physics laboratory actually measures:")
    print("  it applies one stress and reads three strains, recovering E from the")
    print("  axial strain and nu from the ratio of lateral to axial strain.")


def part3_ratio():
    section("3. v_p/v_s against Poisson's ratio, and the exact bounds")
    print(f"{'nu':>8} {'lambda/mu':>11} {'v_p/v_s':>10} "
          f"{'sqrt(K/mu + 4/3)':>18}")
    for nu in (-0.9, -0.5, -0.2, 0.0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.45, 0.49):
        lam_over_mu = 2.0 * nu / (1.0 - 2.0 * nu) if nu != 0.5 else float("inf")
        ratio = math.sqrt(2.0 * (1.0 - nu) / (1.0 - 2.0 * nu))
        # the same ratio written through K = lambda + 2 mu/3
        k_over_mu = lam_over_mu + 2.0 / 3.0
        print(f"{nu:8.2f} {lam_over_mu:11.5f} {ratio:10.6f} "
              f"{math.sqrt(k_over_mu + 4.0 / 3.0):18.6f}")
    print()
    print("  Two bounds, of different strength, must be kept apart:")
    print(f"   * stability alone (K > 0, mu > 0) gives v_p/v_s = sqrt(K/mu + 4/3)")
    print(f"     > 2/sqrt(3) = {2.0 / math.sqrt(3.0):.6f}, approached as nu -> -1.")
    print(f"   * if lambda >= 0, i.e. nu >= 0, then v_p/v_s >= sqrt(2) = "
          f"{math.sqrt(2.0):.6f}, with")
    print(f"     equality at nu = 0. The familiar 'sqrt(2) minimum' is therefore a")
    print(f"     statement about non-negative lambda, not a universal bound, and")
    print(f"     negative lambda is physically allowed in principle (auxetic media).")
    print(f"   * nu -> 1/2 means K -> infinity: the material becomes incompressible,")
    print(f"     v_p diverges and v_s stays finite, and v_p/v_s grows without bound.")
    print(f"  The one unconditional statement is v_p > v_s: it follows from")
    print(f"  lambda + 2 mu - mu = lambda + mu = K + mu/3 > 0, which holds for every")
    print(f"  stable isotropic solid and never depends on the sign of lambda.")


def part4_fluid_substitution():
    section("4. Gassmann fluid substitution: gas to water in a sandstone")
    phi = 0.20
    K_min, G = 36.0e9, 10.0e9          # quartz mineral modulus, frame shear
    K_dry = 10.0e9                     # dry frame bulk modulus (model value)
    rho_min, rho_w, rho_g = 2650.0, 1000.0, 1.2
    K_w, K_g = 2.2e9, 1.0e7             # water and gas bulk moduli (model values)
    rho_dry = (1.0 - phi) * rho_min

    def fluid_modulus(sw):
        return 1.0 / (sw / K_w + (1.0 - sw) / K_g)      # Wood (Reuss) average

    def density(sw):
        return rho_dry + phi * (sw * rho_w + (1.0 - sw) * rho_g)

    def gassmann_k(sw):
        k_fl = fluid_modulus(sw)
        numerator = (1.0 - K_dry / K_min) ** 2
        denominator = phi / k_fl + (1.0 - phi) / K_min - K_dry / K_min ** 2
        return K_dry + numerator / denominator

    def vp(k_bulk, rho):
        return math.sqrt((k_bulk + 4.0 * G / 3.0) / rho)

    print(f"phi = {phi:.2f}, K_min = {K_min / 1e9:.1f} GPa, G = {G / 1e9:.1f} GPa, "
          f"K_dry = {K_dry / 1e9:.1f} GPa")
    print(f"K_water = {K_w / 1e9:.2f} GPa, K_gas = {K_g / 1e6:.1f} MPa, "
          f"rho_matrix = {rho_min:.0f} kg/m^3")
    print("K_patchy is the Reuss (harmonic) average of the fully gas-saturated and")
    print("fully water-saturated bulk moduli, the standard patchy-saturation bound.")
    print(f"{'Sw':>5} {'K_fl (GPa)':>11} {'rho':>8} {'K_sat (GPa)':>12} "
          f"{'v_p (m/s)':>10} {'v_s (m/s)':>10} {'v_p patchy':>11}")
    for sw in (0.0, 0.2, 0.5, 0.8, 0.9, 0.95, 0.99, 1.0):
        k_fl = fluid_modulus(sw)
        rho = density(sw)
        k_sat = gassmann_k(sw)
        k_patchy = 1.0 / (sw / gassmann_k(1.0) + (1.0 - sw) / gassmann_k(0.0))
        print(f"{sw:5.2f} {k_fl / 1e9:11.4f} {rho:8.1f} {k_sat / 1e9:12.4f} "
              f"{vp(k_sat, rho):10.4f} {math.sqrt(G / rho):10.4f} "
              f"{vp(k_patchy, rho):11.4f}")
    vp_dry = vp(gassmann_k(0.0), density(0.0))
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if vp(gassmann_k(mid), density(mid)) < vp_dry:
            lo = mid
        else:
            hi = mid
    print(f"Gassmann v_p at Sw = 0 is {vp_dry:.4f} m/s and returns to that value")
    print(f"  at Sw = {0.5 * (lo + hi):.4f}; in between v_p is LOWER than dry.")
    print(f"the minimum of the Gassmann curve is "
          f"{min(vp(gassmann_k(0.01 * i), density(0.01 * i)) for i in range(101)):.4f} m/s")
    print()
    print("  Shear modulus is unchanged by the fluid (a fluid cannot support shear),")
    print("  so v_s changes only through the density: adding fluid lowers v_s")
    print("  monotonically, whatever the fluid and however it is distributed.")
    print("  The bulk modulus rises only when the pore fluid becomes much stiffer")
    print("  than gas, and Wood's average makes that happen only near Sw = 1, so")
    print("  the uniform-saturation Gassmann curve for a gas sand dips before it")
    print("  rises - the classic result that stops v_p alone from determining")
    print("  saturation. Patchy saturation (gas pockets larger than the diffusion")
    print("  length) gives a bulk modulus that is the harmonic average of the two")
    print("  endpoints, hence v_p higher than Gassmann at every intermediate Sw.")
    print()
    print("  Regime of validity, and what breaks: Gassmann assumes a")
    print("  homogeneous pore fluid, frequencies low enough for the pore pressure")
    print("  to equilibrate, and no chemical interaction with the frame. In the")
    print("  squirt-flow regime, laboratory measurements often show v_p falling at")
    print("  the first few per cent of saturation instead. Which applies depends on")
    print("  the frequency and the fluid distribution and must be established by")
    print("  measurement; the shear statement above is the robust one.")


if __name__ == "__main__":
    part1_moduli()
    part2_consistency()
    part3_ratio()
    part4_fluid_substitution()
