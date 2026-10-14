#!/usr/bin/env python3
"""Targeting strategy: which method can see a given target, and what it costs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python targeting_strategy_demo.py

Everything here is SYNTHETIC.  The target geometry, density and susceptibility
contrasts, resistivities, noise levels, detection threshold, survey costs and
target value are chosen teaching values.  They are not measured properties of any
real deposit and not quotations from any tender, contract or report.

Contents
--------
1. Three synthetic target types and their property contrasts.
2. Gravity and magnetic anomaly of a buried sphere versus depth; measured power
   laws and the depth at which the two signal-to-noise ratios cross.
3. EM response: skin depth, induction number and the frequency optimum.
4. Radiometric depth sensitivity: half-value layer and the 10-HVL soil thickness.
5. Gaussian detection probability versus depth; the P_d = 0.5 depth per method.
6. The crossover: depth AND target type decide the ranking.  A crude
   P_d x value - cost comparison is used here; the proper value-of-information
   treatment is deferred to 11-01-03.
7. Verification: voxel integration against the closed form, skin-depth algebra
   against a numerical wavenumber, and the point-mass limit.
"""

import numpy as np
from scipy import optimize, stats

RNG = np.random.default_rng(20261014)

# --- Physical constants (standard) ------------------------------------------
G_NEWTON = 6.67430e-11        # m^3 kg^-1 s^-2
MU0 = 4.0e-7 * np.pi          # H/m, vacuum permeability
MGAL = 1.0e-5                 # m/s^2 per mGal
NT = 1.0e-9                   # T per nT

# --- SYNTHETIC targets: same geometry, different property contrasts ----------
R_TARGET_M = 150.0            # radius of every target body, m
Z_TARGET_M = 300.0            # depth to the centre, m
T1 = "T1 sulphide (dense, conductive, weakly magnetic)"
T2 = "T2 chromite (dense, resistive, non-magnetic)"
T3 = "T3 magnetite (magnetic, low density contrast)"
TARGETS = {
    # name: density contrast (kg/m^3), susceptibility (SI), target rho (ohm m)
    T1: (400.0, 0.001, 1.0),
    T2: (400.0, 0.000, 5000.0),
    T3: (50.0, 0.100, 5000.0),
}
RHO_HOST = 100.0              # host resistivity, ohm m

# --- SYNTHETIC survey parameters -------------------------------------------
B_FIELD = 50.0e-6             # ambient field, T (Earth's field is 25-65 uT)
F_EM = 100.0                  # EM base frequency, Hz
NOISE = {
    "gravity": 0.02,          # mGal, after correction and levelling
    "magnetics": 0.20,        # nT
    "EM": 0.02,               # dimensionless secondary/primary ratio
}
P_FA = 0.05                   # false-alarm probability of the detector
COST_PER_KM2 = {              # SYNTHETIC survey cost, USD per km^2
    "gravity": 250.0,
    "magnetics": 60.0,
    "EM": 350.0,
    "radiometrics": 25.0,
}
AREA_PER_TARGET_KM2 = 100.0   # area worked per target tested
TARGET_VALUE_MUSD = 500.0     # SYNTHETIC in-ground value of a discovery

MU_RHO_1MEV = 0.06            # cm^2/g, mass attenuation, ~1 MeV in rock oxides
SOIL_DENSITY = 1.6            # g/cm^3
ROCK_DENSITY = 2.70           # g/cm^3


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def sphere_volume(r):
    return 4.0 / 3.0 * np.pi * r ** 3


def gravity_sphere_mgal(drho, r, z):
    """Maximum gravity anomaly of a buried sphere: (4/3) pi G drho R^3 / z^2."""
    return (4.0 / 3.0 * np.pi * G_NEWTON * drho * r ** 3 / z ** 2) / MGAL


def magnetic_sphere_nt(susc, r, z, b_field):
    """Vertical-field anomaly on the axis of an induced dipole, in nT.

    M = kappa H with H = B0/mu0; the dipole moment is m = M V, and the axial
    vertical field of a dipole pointing along that axis is (mu0/4pi) 2m/z^3.
    """
    m = susc * (b_field / MU0) * sphere_volume(r)
    return (MU0 / (4.0 * np.pi)) * 2.0 * m / z ** 3 / NT


def skin_depth(rho_ohm_m, freq_hz):
    """Plane-wave skin depth delta = sqrt(2 / (mu0 sigma omega)) in metres."""
    sigma = 1.0 / rho_ohm_m
    return np.sqrt(2.0 / (MU0 * sigma * 2.0 * np.pi * freq_hz))


def induction_factor(freq_hz, r, rho_target):
    """Simple induction-number response omega*tau / sqrt(1 + (omega*tau)^2).

    tau = mu0 sigma a^2 / pi^2 is the decay time constant of a conducting sphere.
    This is a one-parameter circuit response, not the exact solution of the full
    Maxwell problem for a sphere; it has the correct resistive-limit growth
    (proportional to frequency) and saturates at high frequency.
    """
    tau = MU0 * (1.0 / rho_target) * r ** 2 / np.pi ** 2
    wt = 2.0 * np.pi * freq_hz * tau
    return wt / np.sqrt(1.0 + wt ** 2)


def em_index(freq_hz, r, z, rho_t, rho_h):
    """EM coupling index: geometric coupling x host attenuation x induction.

    Geometric part: the secondary field of a buried conductor behaves as a
    dipole, so its amplitude at the surface falls as (a/z)^3.  Host part: the
    primary field in a conducting half-space decays as exp(-z/delta), and the
    coupling is two-way, hence exp(-2z/delta).  This is an INDEX, not a forward
    model; the quantitative treatment is in 11-02-04 and 08-05.
    """
    delta = skin_depth(rho_h, freq_hz)
    return ((r / z) ** 3 * np.exp(-2.0 * z / delta)
            * induction_factor(freq_hz, r, rho_t))


def detection_probability(signal, noise, p_fa=P_FA):
    """Gaussian detection: P_d = Q(Q^-1(P_fa) - d') with d' = signal/noise."""
    d_prime = signal / noise
    threshold = stats.norm.isf(p_fa)       # Q^-1(P_fa)
    return float(stats.norm.sf(threshold - d_prime))


def prob_half_depth(signal_fn, noise, z_lo=50.0, z_hi=20000.0):
    """Depth at which P_d falls through 0.5, by bisection."""
    f = lambda z: detection_probability(signal_fn(z), noise) - 0.5
    if f(z_lo) < 0.0:
        return np.nan
    return optimize.brentq(f, z_lo, z_hi)


def main():
    section("1. Three synthetic targets and their property contrasts")
    print(f"every body is a sphere of radius R = {R_TARGET_M:.0f} m "
          f"(volume {sphere_volume(R_TARGET_M):.3e} m^3), centred at "
          f"z = {Z_TARGET_M:.0f} m; host resistivity {RHO_HOST:.0f} ohm m")
    print(f"ambient field B0 = {B_FIELD / 1e-6:.0f} uT\n")
    print(f"{'target':50s} {'drho (kg/m3)':>12s} {'kappa (SI)':>11s} "
          f"{'rho (ohm m)':>12s}")
    for name, (drho, susc, rho_t) in TARGETS.items():
        print(f"{name:50s} {drho:12.0f} {susc:11.3f} {rho_t:12.1f}")
    print("\na method can only see a CONTRAST.  A body with no property contrast")
    print("against its host is invisible to that method, whatever its size, so the")
    print("same body is a different target to each tool.")

    section("2. Gravity and magnetic anomaly of the same sphere versus depth")
    drho1, susc1, rho1 = TARGETS[T1]
    print(f"T1: drho = {drho1:.0f} kg/m^3, kappa = {susc1:.3f} SI")
    print(f"{'z (m)':>8s} {'gravity (mGal)':>15s} {'SNR_grav':>9s} "
          f"{'magnetics (nT)':>15s} {'SNR_mag':>8s}")
    for z in (100.0, 200.0, 300.0, 450.0, 600.0, 900.0, 1500.0):
        g = gravity_sphere_mgal(drho1, R_TARGET_M, z)
        b = magnetic_sphere_nt(susc1, R_TARGET_M, z, B_FIELD)
        print(f"{z:8.0f} {g:15.4f} {g / NOISE['gravity']:9.2f} "
              f"{b:15.3f} {b / NOISE['magnetics']:8.2f}")
    zz = np.geomspace(100.0, 1500.0, 6)
    gg = np.array([gravity_sphere_mgal(drho1, R_TARGET_M, z) for z in zz])
    bb = np.array([magnetic_sphere_nt(susc1, R_TARGET_M, z, B_FIELD) for z in zz])
    slope_g = np.polyfit(np.log(zz), np.log(gg), 1)[0]
    slope_b = np.polyfit(np.log(zz), np.log(bb), 1)[0]
    print(f"\nfitted power laws over 100-1500 m: gravity ~ z^{slope_g:.3f}, "
          f"magnetics ~ z^{slope_b:.3f}")
    z_cross = optimize.brentq(
        lambda z: (magnetic_sphere_nt(susc1, R_TARGET_M, z, B_FIELD)
                   / NOISE["magnetics"])
        / (gravity_sphere_mgal(drho1, R_TARGET_M, z) / NOISE["gravity"]) - 1.0,
        50.0, 5000.0)
    print(f"because the exponents differ, the two signal-to-noise ratios must")
    print(f"cross: for this target they are equal at z = {z_cross:.0f} m.  Shallower")
    print("than that, magnetics wins; deeper, gravity wins.  'Which method is")
    print("better' has no depth-free answer.")

    section("3. EM response: skin depth, induction number, frequency optimum")
    print(f"host {RHO_HOST:.0f} ohm m, target {rho1:.1f} ohm m, "
          f"z = {Z_TARGET_M:.0f} m, a = {R_TARGET_M:.0f} m")
    tau = MU0 * (1.0 / rho1) * R_TARGET_M ** 2 / np.pi ** 2
    print(f"sphere time constant tau = mu0 sigma a^2/pi^2 = {tau * 1e3:.3f} ms "
          f"-> induction-number corner near {1.0 / (2 * np.pi * tau):.1f} Hz")
    print(f"\n{'f (Hz)':>8s} {'delta host (m)':>15s} {'induction':>10s} "
          f"{'EM index':>10s} {'SNR':>8s}")
    for f in (10.0, 30.0, 100.0, 300.0, 1000.0, 10000.0):
        idx = em_index(f, R_TARGET_M, Z_TARGET_M, rho1, RHO_HOST)
        print(f"{f:8.0f} {skin_depth(RHO_HOST, f):15.1f} "
              f"{induction_factor(f, R_TARGET_M, rho1):10.4f} {idx:10.5f} "
              f"{idx / NOISE['EM']:8.3f}")
    f_opt = optimize.minimize_scalar(
        lambda f: -em_index(f, R_TARGET_M, Z_TARGET_M, rho1, RHO_HOST),
        bounds=(0.5, 5000.0), method="bounded").x
    print(f"\nthe index peaks near {f_opt:.0f} Hz: too low a frequency induces too")
    print("little current, too high a frequency attenuates the primary before it")
    print("reaches the body.  Frequency is a depth-and-target SELECTOR, and the")
    print("optimum depends on the target's own time constant.")

    section("4. Radiometric depth sensitivity")
    print(f"mass attenuation at ~1 MeV in rock-forming oxides: "
          f"{MU_RHO_1MEV:.2f} cm^2/g (standard tabulated value)")
    for name, dens in (("soil", SOIL_DENSITY), ("rock", ROCK_DENSITY)):
        mu = MU_RHO_1MEV * dens
        print(f"  {name:5s} rho = {dens:.2f} g/cm^3: mu = {mu:.4f} /cm, "
              f"half-value layer = {np.log(2.0) / mu:.2f} cm, "
              f"10 HVL = {10 * np.log(2.0) / mu:.1f} cm")
    print(f"\n{'cover (cm)':>11s} {'fraction transmitted':>21s}")
    for d in (10.0, 30.0, 50.0, 100.0):
        mu = MU_RHO_1MEV * SOIL_DENSITY
        print(f"{d:11.0f} {np.exp(-mu * d):21.6f}")
    print("radiometrics is a SURFACE geochemical mapper: it sees the top ~0.5 m")
    print("of soil, so it can only detect alteration that reaches the surface.")

    section("5. Detection probability versus depth")
    grav_signal = lambda z: gravity_sphere_mgal(drho1, R_TARGET_M, z)
    mag_signal = lambda z: magnetic_sphere_nt(susc1, R_TARGET_M, z, B_FIELD)
    em_signal = lambda z: em_index(F_EM, R_TARGET_M, z, rho1, RHO_HOST)
    print(f"Gaussian detector, false-alarm probability {P_FA:.2f}, "
          f"P_d = Q(Q^-1(P_fa) - d')")
    print(f"{'z (m)':>8s} {'P_d gravity':>12s} {'P_d magnetics':>14s} "
          f"{'P_d EM':>9s}")
    for z in (100.0, 200.0, 300.0, 400.0, 600.0, 800.0, 1200.0):
        print(f"{z:8.0f} "
              f"{detection_probability(grav_signal(z), NOISE['gravity']):12.4f} "
              f"{detection_probability(mag_signal(z), NOISE['magnetics']):14.4f} "
              f"{detection_probability(em_signal(z), NOISE['EM']):9.4f}")
    zg = prob_half_depth(grav_signal, NOISE["gravity"])
    zm = prob_half_depth(mag_signal, NOISE["magnetics"])
    ze = prob_half_depth(em_signal, NOISE["EM"])
    print(f"\ndepth at which P_d falls to 0.50 (target radius "
          f"{R_TARGET_M:.0f} m):")
    print(f"  gravity     {zg:8.0f} m  = {zg / R_TARGET_M:5.1f} radii")
    print(f"  magnetics   {zm:8.0f} m  = {zm / R_TARGET_M:5.1f} radii")
    print(f"  EM {F_EM:.0f} Hz   {ze:8.0f} m  = {ze / R_TARGET_M:5.1f} radii")
    print("the three methods do not fade at the same depth, so a target model is")
    print("required before a method can be ranked.")

    section("6. The crossover: depth AND target type decide the ranking")
    print(f"crude value metric: E[net] = P_d x {TARGET_VALUE_MUSD:.0f} MUSD - cost, "
          f"with cost =")
    print(f"{AREA_PER_TARGET_KM2:.0f} km^2 x (USD/km^2).  This ignores the value of "
          f"a negative")
    print("result; the proper treatment is 11-01-03.")
    print(f"{'method':11s} {'USD/km^2':>9s} {'cost (MUSD)':>12s}")
    for m, c in COST_PER_KM2.items():
        print(f"{m:11s} {c:9.0f} {c * AREA_PER_TARGET_KM2 / 1e6:12.3f}")
    print()
    print(f"{'z (m)':>6s} " + " ".join(
        f"{m:>19s}" for m in ("gravity", "magnetics", "EM")))
    print(f"{'':6s} " + " ".join(f"{'P_d   E[net] MUSD':>19s}" for _ in range(3)))
    for z in (150.0, 300.0, 500.0, 900.0):
        row = []
        for m, sig, nz in (("gravity", grav_signal, NOISE["gravity"]),
                           ("magnetics", mag_signal, NOISE["magnetics"]),
                           ("EM", em_signal, NOISE["EM"])):
            pd = detection_probability(sig(z), nz)
            net = pd * TARGET_VALUE_MUSD - COST_PER_KM2[m] * AREA_PER_TARGET_KM2 / 1e6
            row.append(f"{pd:8.3f} {net:9.1f}")
        print(f"{z:6.0f} " + " ".join(f"{r:>19s}" for r in row))
    print("\nT1: P_d saturates near 1 for gravity and magnetics, so the value")
    print("metric separates only at depth — but by 900 m gravity leads 376.6 to")
    print("95.6 MUSD.  The underlying SNR crossover between the two is at 298 m.")
    print("Now hold depth at 300 m and change the TARGET TYPE:")
    print(f"\n{'target':50s} {'P_d grav':>9s} {'P_d mag':>8s} {'P_d EM':>7s} "
          f"{'winner':>9s}")
    for name, (drho, susc, rho_t) in TARGETS.items():
        s = {
            "gravity": lambda z, d=drho: gravity_sphere_mgal(d, R_TARGET_M, z),
            "magnetics": lambda z, k=susc: magnetic_sphere_nt(
                k, R_TARGET_M, z, B_FIELD),
            "EM": lambda z, r=rho_t: em_index(F_EM, R_TARGET_M, z, r, RHO_HOST),
        }
        pd = {m: detection_probability(s[m](Z_TARGET_M), NOISE[m]) for m in s}
        net = {m: pd[m] * TARGET_VALUE_MUSD
               - COST_PER_KM2[m] * AREA_PER_TARGET_KM2 / 1e6 for m in pd}
        winner = max(net, key=net.get)
        print(f"{name:50s} {pd['gravity']:9.3f} {pd['magnetics']:8.3f} "
              f"{pd['EM']:7.3f} {winner:>9s}")
    print("the winner is a property of the TARGET, not of the tool: T2 is")
    print("invisible to magnetics and to EM because it carries no magnetic or")
    print("conductivity contrast, and no depth would change that.  Method")
    print("selection therefore starts with a target model, and the target model")
    print("is the hypothesis being tested.")

    section("7. Verification")
    n = 61
    ax = np.linspace(-R_TARGET_M, R_TARGET_M, n)
    X, Y, Zl = np.meshgrid(ax, ax, ax, indexing="ij")
    inside = X ** 2 + Y ** 2 + Zl ** 2 <= R_TARGET_M ** 2
    cell = (ax[1] - ax[0]) ** 3
    depth = Zl[inside] + Z_TARGET_M          # depth of each voxel, positive down
    rr = np.sqrt(X[inside] ** 2 + Y[inside] ** 2 + depth ** 2)
    dg_down = np.sum(G_NEWTON * drho1 * cell * depth / rr ** 3)
    analytic = gravity_sphere_mgal(drho1, R_TARGET_M, Z_TARGET_M)
    print(f"(a) voxel sum of the downward acceleration ({n}^3 grid, "
          f"{inside.sum()} cells)")
    print(f"    voxel sum  = {dg_down / MGAL:.6f} mGal")
    print(f"    closed form {analytic:.6f} mGal")
    print(f"    relative difference = "
          f"{abs(dg_down / MGAL - analytic) / analytic * 100:.4f}% "
          f"(voxel approximation of the sphere surface)")
    sig = 1.0 / RHO_HOST
    k = np.sqrt(1j * MU0 * sig * 2.0 * np.pi * F_EM)
    delta_num = 1.0 / k.imag
    print(f"(b) skin depth at {F_EM:.0f} Hz in {RHO_HOST:.0f} ohm m:")
    print(f"    closed form {skin_depth(RHO_HOST, F_EM):.4f} m, from "
          f"1/Im(sqrt(i mu0 sigma omega)) {delta_num:.4f} m, "
          f"difference {abs(delta_num - skin_depth(RHO_HOST, F_EM)):.2e} m")
    print("(c) point-mass limit of the sphere formula:")
    for z in (300.0, 3000.0, 30000.0):
        exact = gravity_sphere_mgal(drho1, R_TARGET_M, z)
        point = (G_NEWTON * drho1 * sphere_volume(R_TARGET_M) / z ** 2) / MGAL
        print(f"    z = {z:7.0f} m: sphere {exact:.6e} mGal, point mass "
              f"{point:.6e} mGal, ratio {exact / point:.6f}")
    print("    at depth the body's SIZE is unobservable: only its total excess")
    print("    mass is constrained, which is the gravity non-uniqueness in embryo.")


if __name__ == "__main__":
    main()
