#!/usr/bin/env python3
"""Geophysical signatures of major deposit types: contrasts, anomalies and
which deposit classes a given method can tell apart.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python deposit_signatures_demo.py

Everything here is SYNTHETIC.  The property contrasts of the deposit classes are
CHOSEN TEACHING VALUES spanning the ranges usually quoted for such classes; they
are not measurements, not averages of any database, and not properties of any
named deposit or district.  The geometry, noise levels and thresholds are
synthetic too.

Contents
--------
1. The synthetic contrast table: density, susceptibility, resistivity,
   chargeability and radioelements for seven deposit classes and one host.
2. Anomaly amplitudes for one common buried-sphere geometry, computed for
   gravity, magnetics and EM.
3. The signature matrix, its singular values and its rank: how many independent
   directions the methods span.
4. Pairwise cosine similarities: which deposit classes are confusable.
5. Pairwise distances, and the two classes a single method cannot separate.
6. Noise-limited classification: how often the two closest classes are confused
   with one method against two methods.
7. Verification: metric axioms, identical-vector cosine, and the depth exponents
   of the anomaly formulas.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_NEWTON = 6.67430e-11        # m^3 kg^-1 s^-2
MU0 = 4.0e-7 * np.pi          # H/m
MGAL = 1.0e-5                 # m/s^2 per mGal
NT = 1.0e-9                   # T per nT

R_TARGET_M = 150.0            # shared radius of every synthetic body model
Z_TARGET_M = 300.0            # shared depth to centre
B_FIELD = 50.0e-6             # ambient field, T
F_EM = 100.0                  # EM frequency, Hz
RHO_HOST = 100.0              # host resistivity, ohm m

# name: drho (kg/m^3), kappa (SI), rho (ohm m), chargeability (mV/V),
#       K (%), eU (ppm), eTh (ppm)
CLASSES = {
    "porphyry Cu (disseminated)": (100.0, 0.010, 20.0, 15.0, 3.0, 3.0, 12.0),
    "IOCG (magnetite-bearing)":   (400.0, 0.350, 5.0, 8.0, 1.5, 2.0, 6.0),
    "VMS (massive sulphide)":     (600.0, 0.050, 0.5, 12.0, 0.5, 1.0, 1.0),
    "magmatic Ni-Cu sulphide":    (450.0, 0.100, 1.0, 10.0, 0.3, 0.5, 1.0),
    "chromite":                   (800.0, 0.005, 2000.0, 1.0, 0.1, 0.2, 0.5),
    "banded iron formation":      (900.0, 0.500, 500.0, 2.0, 0.3, 1.0, 2.0),
    "graphite schist (barren)":   (-50.0, 0.001, 0.2, 3.0, 1.0, 2.0, 8.0),
}
HOST = (0.0, 0.005, RHO_HOST, 1.0, 2.0, 2.0, 10.0)   # unmineralised host

NOISE = {                    # 1-sigma detection noise, in each unit
    "gravity": 0.02,         # mGal
    "magnetics": 0.20,       # nT
    "EM": 0.02,              # dimensionless secondary/primary ratio
    "radiometrics": 5.0,     # percent relative error on a ratio
}
METHODS = ("gravity", "magnetics", "EM", "K", "U", "Th")


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def gravity_sphere_mgal(drho, r=R_TARGET_M, z=Z_TARGET_M):
    return (4.0 / 3.0 * np.pi * G_NEWTON * drho * r ** 3 / z ** 2) / MGAL


def magnetic_sphere_nt(susc, r=R_TARGET_M, z=Z_TARGET_M, b_field=B_FIELD):
    m = susc * (b_field / MU0) * (4.0 / 3.0 * np.pi * r ** 3)
    return (MU0 / (4.0 * np.pi)) * 2.0 * m / z ** 3 / NT


def skin_depth(rho, f=F_EM):
    return np.sqrt(2.0 / (MU0 * (1.0 / rho) * 2.0 * np.pi * f))


def em_index(rho_target, r=R_TARGET_M, z=Z_TARGET_M, rho_host=RHO_HOST, f=F_EM):
    """Geometric coupling x host attenuation x induction number (an index)."""
    tau = MU0 * (1.0 / rho_target) * r ** 2 / np.pi ** 2
    wt = 2.0 * np.pi * f * tau
    return ((r / z) ** 3 * np.exp(-2.0 * z / skin_depth(rho_host, f))
            * wt / np.sqrt(1.0 + wt ** 2))


def signature(vec):
    """Full signature vector of one class given a 7-tuple of properties."""
    drho, susc, rho, charge, k_pct, u_ppm, th_ppm = vec
    hk, hu, hth = HOST[4], HOST[5], HOST[6]
    return np.array([
        gravity_sphere_mgal(drho),
        magnetic_sphere_nt(susc),
        em_index(rho),
        (k_pct - hk) / hk * 100.0,        # relative radioelement contrast, %,
        (u_ppm - hu) / hu * 100.0,        # visible only where the body outcrops
        (th_ppm - hth) / hth * 100.0,
    ])


def main():
    section("1. SYNTHETIC contrast table")
    print(f"shared body model: sphere of radius {R_TARGET_M:.0f} m at "
          f"z = {Z_TARGET_M:.0f} m; ambient field {B_FIELD / 1e-6:.0f} uT; "
          f"EM at {F_EM:.0f} Hz")
    print(f"host: rho = {RHO_HOST:.0f} ohm m, kappa = {HOST[1]:.3f} SI, "
          f"K = {HOST[4]:.1f}%, eU = {HOST[5]:.1f} ppm, eTh = {HOST[6]:.1f} ppm")
    print(f"\n{'deposit class':30s} {'drho':>7s} {'kappa':>7s} {'rho':>8s} "
          f"{'M(mV/V)':>8s} {'K%':>6s} {'eU':>5s} {'eTh':>5s}")
    for name, v in CLASSES.items():
        print(f"{name:30s} {v[0]:7.0f} {v[1]:7.3f} {v[2]:8.1f} {v[3]:8.1f} "
              f"{v[4]:6.1f} {v[5]:5.1f} {v[6]:5.1f}")
    print(f"{'HOST (granodiorite)':30s} {HOST[0]:7.0f} {HOST[1]:7.3f} "
          f"{HOST[2]:8.1f} {HOST[3]:8.1f} {HOST[4]:6.1f} {HOST[5]:5.1f} "
          f"{HOST[6]:5.1f}")
    print("\nthe chargeability column is not used below: it belongs to the IP")
    print("method, which is treated quantitatively in 11-02-06.")

    section("2. Anomaly amplitude for the shared geometry")
    sigs = {name: signature(v) for name, v in CLASSES.items()}
    print(f"{'deposit class':30s} {'dg(mGal)':>9s} {'dB(nT)':>9s} "
          f"{'EM index':>10s} {'dK(%)':>8s} {'dU(%)':>8s} {'dTh(%)':>8s}")
    for name, s in sigs.items():
        print(f"{name:30s} {s[0]:9.3f} {s[1]:9.2f} {s[2]:10.5f} "
              f"{s[3]:8.1f} {s[4]:8.1f} {s[5]:8.1f}")
    print("\nmagnetics separates by two orders of magnitude across classes;")
    print("gravity separates by one; the EM index varies over four orders because")
    print("of the 1/z^3 coupling and the skin-depth term; the radioelement")
    print("contrasts are percentages and only exist where the body outcrops.")

    section("3. The signature matrix: rank and independent directions")
    names = list(sigs)
    M = np.array([sigs[n] for n in names])
    Mn = M / np.linalg.norm(M, axis=1, keepdims=True)     # unit-normalise rows
    sv = np.linalg.svd(Mn, compute_uv=False)
    print(f"signature matrix: {M.shape[0]} classes x {M.shape[1]} quantities, "
          f"rows normalised to unit length")
    print("singular values: " + ", ".join(f"{x:.4f}" for x in sv))
    tol = sv[0] * max(M.shape) * np.finfo(float).eps
    print(f"rank with the usual tolerance {tol:.3e} = {(sv > tol).sum()} "
          f"of {len(sv)}")
    print(f"condition number = {sv[0] / sv[-1]:.2f}")
    print("a rank below the number of columns would mean two quantities carry")
    print("the same information; the condition number measures how nearly so.")
    print(f"\nlargest and smallest singular directions (rows = quantities:")
    print(f"{'  '.join(f'{m:>9s}' for m in METHODS)})")
    U, _, Vt = np.linalg.svd(Mn, full_matrices=False)
    print("  max: " + "  ".join(f"{x:9.4f}" for x in Vt[0]))
    print("  min: " + "  ".join(f"{x:9.4f}" for x in Vt[-1]))
    print("the minimum direction is the combination of measurements along which")
    print("the deposit classes are least separated; the coefficients name the")
    print("trade-off.")

    section("4. Pairwise cosine similarity")
    G = Mn @ Mn.T
    print(f"{'pair of classes':58s} {'cos':>7s}")
    pairs = [(G[i, j], names[i], names[j])
             for i in range(len(names)) for j in range(i + 1, len(names))]
    for c, a, b in sorted(pairs, reverse=True)[:6]:
        print(f"{a + ' / ' + b:58s} {c:7.4f}")
    print("cos = 1 means the two classes produce the same signature pattern and")
    print("can only be told apart by absolute magnitude, which the geology does")
    print("not guarantee.")

    section("5. Distances and the confusable pairs")
    D = np.sqrt(np.maximum(0.0, 2.0 - 2.0 * G))    # Euclidean distance of unit vecs
    dist_pairs = [(D[i, j], names[i], names[j])
                  for i in range(len(names)) for j in range(i + 1, len(names))]
    print(f"{'pair of classes':58s} {'distance':>9s}")
    for d, a, b in sorted(dist_pairs)[:6]:
        print(f"{a + ' / ' + b:58s} {d:9.4f}")
    i_vms = names.index("VMS (massive sulphide)")
    i_gra = names.index("graphite schist (barren)")
    i_ni = names.index("magmatic Ni-Cu sulphide")
    i_iocg = names.index("IOCG (magnetite-bearing)")
    i_bif = names.index("banded iron formation")
    print(f"\nVMS vs graphite schist: cosine {G[i_vms, i_gra]:.4f}, "
          f"distance {D[i_vms, i_gra]:.4f}")
    print("a massive sulphide body and a barren graphite schist are both strong")
    print("conductors with little magnetic or density signature.  That is the")
    print("classic false positive of mineral exploration.")
    print(f"\nIOCG vs banded iron formation: cosine {G[i_iocg, i_bif]:.4f}, "
          f"distance {D[i_iocg, i_bif]:.4f}")
    print("these two have almost the same signature DIRECTION: both are dense and")
    print("strongly magnetic, and differ only in the absolute magnitudes.")

    section("6. What the data can and cannot separate")
    sigma = np.array([NOISE["gravity"], NOISE["magnetics"], NOISE["EM"],
                      NOISE["radiometrics"], NOISE["radiometrics"],
                      NOISE["radiometrics"]])

    def err_known_amplitude(i, j, cols):
        """Both signatures are known: compare the projection with the noise."""
        from scipy import stats
        d_mu = M[i, cols] - M[j, cols]
        var = np.sum(sigma[cols] ** 2 * (d_mu / np.linalg.norm(d_mu)) ** 2)
        return float(stats.norm.cdf(-np.linalg.norm(d_mu) / (2.0 * np.sqrt(var))))

    def err_unknown_amplitude(i, j, a_scale, cols=None):
        """Size and depth unknown: only the signature DIRECTION is observable.

        Both classes share an unknown amplitude A (a common scale factor across
        methods -- an approximation stated in the lesson).  The decision
        boundary between them is the hyperplane perpendicular to
        u_i - u_j, where u are the unit signature directions, so the error is
        P(<x, u_i - u_j> < 0) with x = A s_i + noise.
        """
        from scipy import stats
        cols = list(range(M.shape[1])) if cols is None else cols
        s_i, s_j = M[i, cols], M[j, cols]
        u_i = s_i / np.linalg.norm(s_i)
        u_j = s_j / np.linalg.norm(s_j)
        d = u_i - u_j
        mean = a_scale * float(s_i @ d)
        sd = np.sqrt(np.sum(sigma[cols] ** 2 * d ** 2))
        return float(stats.norm.cdf(-mean / sd)) if sd > 0 else 0.0

    print("(a) amplitudes KNOWN (target model fixes size and depth):")
    print(f"{'pair':58s} {'P(error)':>9s}")
    for lab, i, j in (("VMS / graphite, EM only", i_vms, i_gra),
                      ("VMS / graphite, all methods", i_vms, i_gra),
                      ("IOCG / BIF, all methods", i_iocg, i_bif),
                      ("VMS / Ni-Cu, all methods", i_vms, i_ni)):
        cols = [2] if "EM only" in lab else list(range(6))
        print(f"{lab:58s} {err_known_amplitude(i, j, cols):9.4f}")
    print("\n(b) amplitudes UNKNOWN (reconnaissance: the body's size and depth are")
    print("    not known, so only the direction of the signature is observable):")
    print(f"{'pair':46s} {'cos':>8s} {'P(err) A=1':>11s} {'P(err) A=0.1':>13s}")
    for lab, i, j in (("IOCG / banded iron formation", i_iocg, i_bif),
                      ("VMS / magmatic Ni-Cu", i_vms, i_ni),
                      ("VMS / graphite schist", i_vms, i_gra),
                      ("chromite / porphyry Cu", names.index("chromite"),
                       names.index("porphyry Cu (disseminated)"))):
        print(f"{lab:46s} {G[i, j]:8.4f} {err_unknown_amplitude(i, j, 1.0):11.4f} "
              f"{err_unknown_amplitude(i, j, 0.1):13.4f}")
    print("\n(c) the potential-field channels removed: radioelement ratios only")
    print("    (their contrast is a surface concentration ratio, so it does not")
    print("    scale with the body's depth the way an anomaly amplitude does):")
    print(f"{'pair':46s} {'P(err)':>9s}")
    for lab, i, j in (("IOCG / banded iron formation", i_iocg, i_bif),
                      ("VMS / magmatic Ni-Cu", i_vms, i_ni),
                      ("VMS / graphite schist", i_vms, i_gra),
                      ("chromite / porphyry Cu", names.index("chromite"),
                       names.index("porphyry Cu (disseminated)"))):
        print(f"{lab:46s} {err_unknown_amplitude(i, j, 1.0, [3, 4, 5]):9.4f}")
    print("radiometrics alone separates the two densest, most magnetic classes")
    print("(IOCG and banded iron formation) at a few per cent error, because their")
    print("K/U/Th directions differ strongly.  That is the whole argument for")
    print("airborne radiometrics in these terrains -- and the whole reason it fails")
    print("under cover.")
    print("\nwith the amplitude unknown, what separates two classes is the DIRECTION")
    print("of the signature vector, and the noise that matters is the noise")
    print("PERPENDICULAR to it, divided by the signal magnitude.  Two things")
    print("follow.  First, a class pair separated only by magnitude (cosine close")
    print("to 1) is unresolvable at any budget.  Second, the direction is carried")
    print("by whichever quantity has the largest RELATIVE contrast, so a small")
    print("radioelement contrast can dominate the classification whenever the")
    print("body outcrops, and is invisible when it does not.")
    print("\nThis is the honest limit of anomaly-based targeting: a strong anomaly")
    print("establishes that SOMETHING anomalous is there.  Identifying which class")
    print("it belongs to requires either an amplitude constraint (a known size or")
    print("depth) or a property the classes differ in by direction, not by")
    print("magnitude -- typically the radioelement ratios or the IP response.")

    section("7. Verification")
    print("(a) metric axioms on the distance matrix")
    print(f"    symmetry: max |D - D^T| = {np.max(np.abs(D - D.T)):.2e}")
    tri = max(D[i, k] - (D[i, j] + D[j, k])
              for i in range(len(names)) for j in range(len(names))
              for k in range(len(names)))
    print(f"    triangle inequality: max (D[i,k] - D[i,j] - D[j,k]) = "
          f"{tri:.2e} (must be <= 0)")
    print(f"    diagonal: max D[i,i] = {np.max(np.diag(D)):.2e}")
    print("(b) cosine of a class with itself")
    for n in ("VMS (massive sulphide)", "chromite"):
        k = names.index(n)
        print(f"    {n:30s} self cosine = {G[k, k]:.10f}")
    print("(c) depth exponents of the anomaly formulas")
    zz = np.array([150.0, 300.0, 600.0, 1200.0])
    g = np.array([gravity_sphere_mgal(400.0, 150.0, z) for z in zz])
    b = np.array([magnetic_sphere_nt(0.1, 150.0, z, B_FIELD) for z in zz])
    print(f"    gravity   fitted exponent = "
          f"{np.polyfit(np.log(zz), np.log(g), 1)[0]:.6f} (expect -2)")
    print(f"    magnetics fitted exponent = "
          f"{np.polyfit(np.log(zz), np.log(b), 1)[0]:.6f} (expect -3)")


if __name__ == "__main__":
    main()
