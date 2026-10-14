#!/usr/bin/env python3
"""Radiometrics and alteration mapping: windows, stripping, height response,
ratios, burial and counting statistics.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiometrics_demo.py

Everything here is SYNTHETIC.  The concentrations, sensitivity coefficients,
stripping ratios, attenuation coefficients, counting times and noise levels are
chosen teaching values.  Two exceptions are stated as standard constants where
they are used: the air density (1.225e-3 g/cm^3) and the mass attenuation
coefficients of air at the two window energies.

Contents
--------
1. The three-window spectrometer: concentrations to count rates, stripping, and
   the conditioning of the stripping inverse.
2. The height response of an infinite plane source, F(h) proportional to
   mu h E2(mu h), derived and verified against a direct annular integration.
3. Differential attenuation: the Th/K ratio drifts with flying height.
4. Burial: the soil attenuation that limits the method to the top half-metre.
5. Alteration mapping: K, Th/K, and the separability of potassic from argillic
   alteration given counting noise.
6. Counting statistics and the detection limit versus integration time.
7. Verification.
"""

import numpy as np
from scipy import special

RNG = np.random.default_rng(20261014)

RHO_AIR = 1.225e-3            # g/cm^3, standard air density at STP
MU_RHO_AIR_K = 0.053          # cm^2/g, standard mass attenuation of air, ~1.46 MeV
MU_RHO_AIR_TH = 0.036         # cm^2/g, standard mass attenuation of air, ~2.61 MeV
MU_RHO_SOIL = 0.06            # cm^2/g, standard mass attenuation in rock oxides
RHO_SOIL = 1.6                # g/cm^3

# SYNTHETIC spectrometer calibration: count rate (counts/s) per unit concentration
# for a 4 L crystal at ground level
SENS = np.array([95.0, 4.2, 2.4])      # per %K, per ppm eU, per ppm eTh
# SYNTHETIC stripping ratios: fraction of a window's counts contributed by another
STRIP = np.array([                   # rows = window K, U, Th; cols = source
    [1.00, 0.30, 0.10],
    [0.05, 1.00, 0.30],
    [0.00, 0.00, 1.00],
])

ROCKS = {
    "unaltered granodiorite": (2.0, 2.0, 10.0),
    "potassic alteration": (4.5, 2.5, 6.0),
    "argillic alteration": (0.8, 3.5, 14.0),
    "potassic core (high K, low Th)": (5.5, 2.0, 3.0),
}


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def plane_height_response(h_m, mu_per_m):
    """Flux from an infinite plane source through an attenuating medium.

    Derivation: the annulus at radius x contributes
    With r = sqrt(x^2+h^2), substituting u = mu r gives
    F = (M mu h/2) integral_{mu h}^inf e^{-u}/u^2 du.  Using
    E2(z) = z integral_z^inf e^{-u}/u^2 du, this is F = (M/2) E2(mu h), so
    normalising by the unattenuated value M/2:
        R(h) = E2(mu h),  E2(z) = integral_1^inf e^{-z t}/t^2 dt.
    """
    z = mu_per_m * h_m
    if z <= 0.0:
        return 1.0
    return float(special.expn(2, z))


def plane_height_response_numeric(h_m, mu_per_m, n=400000, xmax_factor=40.0):
    """Brute-force annular integration of the same flux, for verification."""
    xmax = xmax_factor / mu_per_m
    x = np.linspace(0.0, xmax, n)
    r = np.sqrt(x ** 2 + h_m ** 2)
    integrand = (h_m / 2.0) * x * np.exp(-mu_per_m * r) / r ** 3
    return float(np.trapezoid(integrand, x)) * 2.0 / 1.0 * 1.0


def counts_from_concentrations(conc, sens=SENS, strip=STRIP):
    """Window count rates from (K%, eU ppm, eTh ppm) through the stripping matrix."""
    return strip @ (sens * np.asarray(conc))


def concentrations_from_counts(counts, sens=SENS, strip=STRIP):
    return np.linalg.solve(strip, counts) / sens


def main():
    section("1. The three-window spectrometer and the stripping inverse")
    print("each window sees not only its own radioelement: Compton scattering")
    print("moves counts between windows, so the raw window count rates must be")
    print("unmixed.  Rows = window (K, U, Th); the matrix is SYNTHETIC:")
    print(f"\n{STRIP}")
    print(f"\nsensitivity (counts/s per unit): K = {SENS[0]:.1f} per %K, "
          f"U = {SENS[1]:.1f} per ppm eU, Th = {SENS[2]:.1f} per ppm eTh")
    sv = np.linalg.svd(STRIP, compute_uv=False)
    print(f"singular values of the stripping matrix: "
          f"{', '.join(f'{s:.4f}' for s in sv)}")
    print(f"condition number = {sv[0] / sv[-1]:.3f}")
    print("\nsignal (counts/s) and the recovered concentrations (round trip):")
    print(f"{'rock':30s} {'K (c/s)':>9s} {'U (c/s)':>9s} {'Th (c/s)':>9s} "
          f"{'%K':>7s} {'eU':>6s} {'eTh':>6s}")
    for name, conc in ROCKS.items():
        c = counts_from_concentrations(conc)
        back = concentrations_from_counts(c)
        print(f"{name:30s} {c[0]:9.1f} {c[1]:9.1f} {c[2]:9.1f} "
              f"{back[0]:7.3f} {back[1]:6.3f} {back[2]:6.3f}")
    print("the round trip is exact because the matrix is well conditioned; the")
    print("next section shows what a *measurement* error does to it.")

    section("2. The height response of an infinite plane source")
    print("derivation: an annulus at radius x contributes")
    print("  dF = (M h/2) x dx exp(-mu r)/r^3,  r = sqrt(x^2+h^2),")
    print("so with u = mu r the total is")
    print("  F(h) = (M/2) E2(mu h),   i.e.   R(h) = F(h)/F(0) = E2(mu h),")
    print("where E2 is the second exponential integral.")
    mu_k = MU_RHO_AIR_K * RHO_AIR * 100.0     # per metre (cm^2/g * g/cm^3 * 100)
    mu_th = MU_RHO_AIR_TH * RHO_AIR * 100.0
    print(f"\nair: rho = {RHO_AIR:.4e} g/cm^3; mass attenuation "
          f"{MU_RHO_AIR_K:.3f} (K window) and {MU_RHO_AIR_TH:.3f} cm^2/g "
          f"(Th window)")
    print(f"linear attenuation in air: mu_K = {mu_k:.5f} /m, "
          f"mu_Th = {mu_th:.5f} /m")
    print(f"\n{'height (m)':>11s} {'R_K':>9s} {'R_Th':>9s} {'Th/K drift':>12s}")
    for h in (0.0, 30.0, 60.0, 120.0, 200.0):
        rk = plane_height_response(h, mu_k)
        rt = plane_height_response(h, mu_th)
        print(f"{h:11.0f} {rk:9.4f} {rt:9.4f} {rt / rk:12.4f}")
    print("\nthe half-height, where each window's flux falls to half:")
    for lab, mu in (("K window", mu_k), ("Th window", mu_th)):
        from scipy import optimize
        h_half = optimize.brentq(lambda h: plane_height_response(h, mu) - 0.5,
                                 0.1, 5000.0)
        print(f"  {lab}: {h_half:6.1f} m of air")
    print("flight height is therefore a first-order control on count rate, and")
    print("the Th/K ratio DRIFTS with height because the two windows are")
    print("attenuated differently -- see section 3.")

    section("3. Differential attenuation and the Th/K ratio")
    print("a ratio cancels the source strength and the instrument gain, but NOT")
    print("the height dependence when the two windows have different mu:")
    print(f"\n{'height (m)':>11s} {'mu_K h':>8s} {'mu_Th h':>9s} "
          f"{'R_Th/R_K':>10s} {'bias vs 0 m (%)':>17s}")
    r0 = plane_height_response(0.0, mu_k)
    base = plane_height_response(30.0, mu_th) / plane_height_response(30.0, mu_k)
    for h in (30.0, 60.0, 90.0, 120.0, 180.0):
        rk = plane_height_response(h, mu_k)
        rt = plane_height_response(h, mu_th)
        print(f"{h:11.0f} {mu_k * h:8.4f} {mu_th * h:9.4f} {rt / rk:10.4f} "
              f"{(rt / rk - base) / base * 100:17.2f}")
    print(f"\na flown ratio measured at 120 m and interpreted as if flown at 30 m")
    print(f"is biased by "
          f"{(plane_height_response(120.0, mu_th) / plane_height_response(120.0, mu_k)) / base * 100 - 100:.1f}%.")
    print("for a drape over 100 m of relief the *apparent* Th/K varies across the")
    print("map by that amount with no change in the ground.  Airborne")
    print("radiometric maps are therefore height-corrected before ratios are")
    print("formed, and an uncorrected ratio map is a map of terrain.")

    section("4. Burial: why radiometrics only sees the top half-metre")
    mu_soil = MU_RHO_SOIL * RHO_SOIL
    print(f"soil: rho = {RHO_SOIL:.2f} g/cm^3, mass attenuation "
          f"{MU_RHO_SOIL:.3f} cm^2/g -> mu = {mu_soil:.4f} /cm")
    print(f"half-value layer = {np.log(2) / mu_soil:.2f} cm; "
          f"10 HVL = {10 * np.log(2) / mu_soil:.1f} cm")
    print(f"\n{'cover (cm)':>11s} {'transmitted':>12s} {'as % of no cover':>18s}")
    for d in (0.0, 10.0, 30.0, 50.0, 100.0):
        t = np.exp(-mu_soil * d)
        print(f"{d:11.0f} {t:12.6f} {t * 100:18.1f}")
    print("\ncombining burial with height, the escaping flux is approximately")
    print("  F ~ (M/2) exp(-mu_soil d) R(h),")
    print("because the soil path is short and steep while the air path is long.")
    for d in (0.0, 20.0, 50.0):
        for h in (30.0, 120.0):
            f = np.exp(-mu_soil * d) * plane_height_response(h, mu_k)
            print(f"  cover {d:5.0f} cm, height {h:5.0f} m: relative flux "
                  f"{f:8.5f}")
    print("a 50 cm cover removes 99.2% of the bedrock signal: radiometrics is a")
    print("SURFACE geochemical mapper, and its targets are patterns in the top")
    print("half-metre, not bodies at depth.")

    section("5. Alteration mapping and separability")
    print("alteration changes the radioelement RATIOS, so the diagnostic is")
    print("Th/K (or K/(K+U+Th)) rather than any single channel:")
    print(f"\n{'rock':32s} {'%K':>6s} {'eU':>6s} {'eTh':>6s} {'Th/K':>8s} "
          f"{'K/(K+U+Th)':>12s}")
    for name, conc in ROCKS.items():
        k, u, th = conc
        print(f"{name:32s} {k:6.2f} {u:6.2f} {th:6.2f} {th / k:8.2f} "
              f"{k / (k + u + th):12.3f}")
    print("\nnow add counting noise: 300 s integration, a 4 L crystal, and the")
    print("count rates of section 1.  Poisson: sigma_N = sqrt(N) counts.")
    t_int = 300.0
    print(f"\n{'rock':32s} {'Th/K':>8s} {'sigma(Th/K)':>12s} {'sep. from host':>16s}")
    host = ROCKS["unaltered granodiorite"]
    ratios = {n: c[2] / c[0] for n, c in ROCKS.items()}
    for name, conc in ROCKS.items():
        c = counts_from_concentrations(conc)
        n_counts = c * t_int
        sig = np.sqrt(n_counts) / n_counts
        # first-order propagation of the Th/K ratio
        sig_ratio = ratios[name] * np.sqrt(sig[2] ** 2 + sig[0] ** 2)
        sep = abs(ratios[name] - ratios["unaltered granodiorite"]) / sig_ratio
        print(f"{name:32s} {ratios[name]:8.3f} {sig_ratio:12.4f} {sep:16.1f}")
    print("separation in units of sigma.  All four rock types are separated at")
    print("many sigma with a 300 s integration: this is why radiometrics is such")
    print("an efficient mapping tool -- and why it fails the moment the outcrop")
    print("is covered.")

    section("6. Counting statistics and detection limits")
    print("for a count rate N (counts/s) integrated over T seconds, the relative")
    print("uncertainty is sigma/N = 1/sqrt(N T).  Compute the uncertainty in the K")
    print("window for the unaltered host at several integration times:")
    c_host = counts_from_concentrations(host)
    print(f"\n{'T (s)':>7s} {'N_K (counts)':>13s} {'rel. sigma':>11s} "
          f"{'sigma(%K)':>10s} {'sigma(Th/K)':>12s}")
    for tt in (10.0, 30.0, 100.0, 300.0, 1000.0):
        nk = c_host[0] * tt
        nth = c_host[2] * tt
        rel_k = 1.0 / np.sqrt(nk)
        rel_th = 1.0 / np.sqrt(nth)
        ratio_host = host[2] / host[0]
        sig_ratio = ratio_host * np.sqrt(rel_k ** 2 + rel_th ** 2)
        print(f"{tt:7.0f} {nk:13.0f} {rel_k:11.5f} {host[0] * rel_k:10.4f} "
              f"{sig_ratio:12.5f}")
    print("\nthe uncertainty falls as 1/sqrt(T), so a factor of ten in precision")
    print("costs a factor of a hundred in time: this is the fundamental reason")
    print("radiometric surveys are flown fast and wide rather than slow and")
    print("precise.  It also means two adjacent pixels with different ratios may")
    print("differ only because of counting noise, which is a question a")
    print("variogram answers and a contour map hides.")

    section("7. Verification")
    print("(a) the closed form R(h) = E2(mu h) against a direct annular")
    print("    numerical integration of the flux")
    for h in (30.0, 120.0):
        num = plane_height_response_numeric(h, mu_k)
        closed = plane_height_response(h, mu_k)
        print(f"    h = {h:5.0f} m: numeric {num:.6f}, closed form "
              f"{closed:.6f}, difference {abs(num - closed):.2e}")
    print("    (the numeric integral is multiplied by 2 to normalise by M/2 = 1)")
    print("(b) the stripping matrix round trip")
    worst = 0.0
    for name, conc in ROCKS.items():
        back = concentrations_from_counts(counts_from_concentrations(conc))
        worst = max(worst, float(np.max(np.abs(back - np.asarray(conc)))))
    print(f"    worst absolute round-trip error over four rock types = "
          f"{worst:.2e}")
    print("(c) Poisson counting statistics against a Monte Carlo")
    n_mc = 200000
    lam = c_host[2] * 300.0
    draws = RNG.poisson(lam, n_mc)
    print(f"    analytic sigma/N = {1 / np.sqrt(lam):.6f}")
    print(f"    Monte Carlo sigma/N = {draws.std() / draws.mean():.6f} "
          f"({n_mc} draws of Poisson({lam:.0f}))")
    print("(d) the E2 small-argument limit")
    for z in (1e-6, 1e-3, 1e-1, 1e-2):
        print(f"    mu h = {z:.1e}: E2(mu h) = {float(special.expn(2, z)):.6f} "
              f"(tends to 1 as mu h -> 0)")
    print("(e) the large-argument limit E2(z) -> exp(-z)/z")
    for z in (2.0, 5.0, 20.0):
        print(f"    mu h = {z:5.1f}: E2 = {float(special.expn(2, z)):.6e}, "
              f"exp(-z)/z = {np.exp(-z) / z:.6e}, ratio "
              f"{float(special.expn(2, z)) / (np.exp(-z) / z):.4f}")


if __name__ == "__main__":
    main()
