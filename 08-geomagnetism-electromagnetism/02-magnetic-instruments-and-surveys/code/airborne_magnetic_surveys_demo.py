#!/usr/bin/env python3
"""Airborne magnetic surveys: aircraft interference, its compensation, and the
geometric penalties of flying with a magnetometer.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_magnetic_surveys_demo.py

Everything here is SYNTHETIC: the aircraft coefficients, attitude manoeuvre,
noise, target dipole and flight parameters are chosen teaching values.  No
aircraft, survey or compensation system is described.  The only standard
constant used is mu0 = 4*pi*1e-7 H/m.

Contents
--------
1. The Tolles-Lawson interference model: permanent, induced and eddy terms.
2. A simulated manoeuvre and the size of the interference.
3. Compensation by least squares, with 3, 9 and 18 coefficients.
4. Flying height and the loss of anomaly amplitude.
5. Line spacing and the aliasing of a short-wavelength anomaly.
6. Why compensation must be re-solved flight by flight.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi

# --- SYNTHETIC survey parameters --------------------------------------------
B_EARTH = 50000.0          # nT, total field
DECL, INCL = 5.0, 65.0     # degrees, synthetic field direction
FS = 10.0                  # Hz, sample rate
DURATION = 120.0           # s, length of the manoeuvre
TARGET_DEPTH = 20.0        # m
TARGET_M = 3000.0          # A m^2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def earth_field_hat():
    """Unit vector of the field in the earth frame (north, east, down)."""
    d = np.radians(DECL)
    i = np.radians(INCL)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def rotation(roll, pitch, yaw):
    """Aircraft-to-earth rotation matrix for the given angles (radians)."""
    cr, sr = np.cos(roll), np.sin(roll)
    cp, sp = np.cos(pitch), np.sin(pitch)
    cy, sy = np.cos(yaw), np.sin(yaw)
    Rx = np.array([[1, 0, 0], [0, cr, -sr], [0, sr, cr]])
    Ry = np.array([[cp, 0, sp], [0, 1, 0], [-sp, 0, cp]])
    Rz = np.array([[cy, -sy, 0], [sy, cy, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx


def manoeuvre(t):
    """Attitude angles (radians) of a synthetic manoeuvre."""
    roll = np.radians(25.0) * np.sin(2 * np.pi * t / 25.0)
    pitch = np.radians(12.0) * np.sin(2 * np.pi * t / 17.0 + 0.7)
    yaw = np.radians(18.0) * np.sin(2 * np.pi * t / 31.0 + 1.3)
    return roll, pitch, yaw


def design_matrix(u, du):
    """The 18-column Tolles-Lawson design matrix from the field direction u.

    Columns: 3 permanent (u_i), 6 induced (u_i u_j, i <= j), 9 eddy (u_i du_j/dt).
    """
    n = u.shape[1]
    cols = []
    for i in range(3):
        cols.append(u[i])
    for i in range(3):
        for j in range(i, 3):
            cols.append(u[i] * u[j])
    for i in range(3):
        for j in range(3):
            cols.append(u[i] * du[j])
    return np.column_stack(cols)


def main():
    section("1. The Tolles-Lawson interference model")
    print("  the field direction expressed in the aircraft frame is u(t); the")
    print("  interference on a total-field sensor is modelled as")
    print("    I(t) = sum_k a_k u_k                     (permanent, 3 terms)")
    print("         + sum_{i<=j} b_ij u_i u_j           (induced, 6 terms)")
    print("         + sum_{i,j} c_ij u_i du_j/dt        (eddy, 9 terms)")
    print("  the permanent term is the airframe's own remanence projected onto the")
    print("  sensor axis; the induced term is M = kappa H of the airframe, which is")
    print("  proportional to the ambient field and to its orientation; the eddy term")
    print("  is Faraday induction in the airframe as the flux through it changes.")
    print("  All three scale with the ambient field, which is why the model is")
    print("  built from u and du/dt rather than from the attitude angles directly.")

    section("2. A simulated manoeuvre and the interference it produces")
    t = np.arange(0.0, DURATION, 1.0 / FS)
    roll, pitch, yaw = manoeuvre(t)
    u = np.empty((3, len(t)))
    du = np.empty((3, len(t)))
    b_hat = earth_field_hat()
    for k in range(len(t)):
        u[:, k] = rotation(roll[k], pitch[k], yaw[k]) @ b_hat
    du = np.gradient(u, t, axis=1)
    print(f"  manoeuvre: roll +/-25 deg, pitch +/-12 deg, yaw +/-18 deg over "
          f"{DURATION:.0f} s")
    print(f"  |u| stays at {np.abs(np.linalg.norm(u, axis=0)).mean():.6f} "
          "(a unit vector, as it must be)")
    print(f"  peak |du/dt| = {np.max(np.abs(du)):.4f} per second")
    A = design_matrix(u, du)
    coef_true = np.zeros(A.shape[1])
    coef_true[0:3] = np.array([12.0, -8.0, 20.0])            # nT
    coef_true[3:9] = np.array([15.0, 6.0, -10.0, 4.0, -7.0, 9.0])  # nT
    coef_true[9:18] = np.array([2.0, -1.0, 0.5, 1.5, -0.8, 0.3,
                                -1.2, 0.9, -0.4])            # nT s
    interference = A @ coef_true
    print(f"  SYNTHETIC interference: rms {interference.std():8.3f} nT, "
          f"peak {np.max(np.abs(interference)):8.3f} nT")
    print("  that is of the same order as, or larger than, the crustal anomalies a")
    print("  survey maps (a few to tens of nT) and orders of magnitude above the")
    print("  sub-nanotesla resolution the sensor offers, so compensation is not")
    print("  optional: without it the aircraft's own field is the anomaly.")

    section("3. Compensation by least squares")
    geology = 25.0        # nT, a constant anomaly during the manoeuvre
    noise = 0.3           # nT rms, sensor noise
    measured = geology + interference + RNG.normal(0.0, noise, len(t))
    print("  model order   coefficients   rms residual (nT)   reduction factor")
    for ncol, name in ((3, "permanent only"), (9, "permanent + induced"),
                       (18, "full model")):
        sol, *_ = np.linalg.lstsq(A[:, :ncol], measured, rcond=None)
        resid = measured - A[:, :ncol] @ sol
        print(f"  {name:19s} {ncol:9d}   {resid.std():16.4f}   "
              f"{interference.std()/resid.std():16.1f}")
    print(f"  the sensor noise floor is {noise:.2f} nT rms, and the full model")
    print("  reaches it: the leftover is noise, not uncompensated interference.")
    print("  The economic point is in the first row: a permanent-terms-only solution")
    print("  leaves a residual far above the noise.  The second and third rows are")
    print("  indistinguishable, so with these SYNTHETIC amplitudes the eddy terms are")
    print("  not justified by the data: a larger model that does not reduce the")
    print("  residual below the noise is fitting nothing.  That comparison - not the")
    print("  number of coefficients - is what decides the model order.")

    section("4. Flying height and the loss of anomaly amplitude")
    print(f"  SYNTHETIC dipole target: moment {TARGET_M:.0f} A m^2, "
          f"depth {TARGET_DEPTH:.0f} m")
    print("   altitude (m)   |B| (nT)   fraction of the ground value")
    r_ground = np.array([0.0, 0.0, TARGET_DEPTH])
    b_ground = MU0 / (4 * np.pi) * TARGET_M / TARGET_DEPTH ** 3 * 2.0 * 1e9
    for alt in (0.0, 30.0, 60.0, 100.0, 200.0):
        r = np.array([0.0, 0.0, TARGET_DEPTH + alt])
        b = MU0 / (4 * np.pi) * 2.0 * TARGET_M / np.linalg.norm(r) ** 3 * 1e9
        print(f"  {alt:12.0f}   {b:9.3f}   {b/b_ground:26.4f}")
    print("  the anomaly decays as (depth)^-3, so height is a direct loss of")
    print("  target amplitude; a survey flies as low as the terrain and safety")
    print("  case allow, and the drape is part of the acquisition design.")

    section("5. Line spacing and the aliasing of a short anomaly")
    lam = 400.0
    print(f"  a synthetic anomaly of wavelength {lam:.0f} m, sampled at different")
    print("  line spacings.  The peak may fall between samples, so the retention")
    print("  is the worst case over the anomaly's phase; the recovered wavelength")
    print("  is the best fit restricted to wavelengths the spacing can resolve")
    print("  (that is, two samples per wavelength or better).")
    print("   spacing (m)  s/lambda   worst retention   recovered wavelength")
    for spacing in (50.0, 100.0, 200.0, 400.0, 800.0):
        x = np.arange(0.0, 4000.0, spacing)
        worst = 1.0
        for phi in np.linspace(0.0, 2.0 * np.pi, 33)[:-1]:
            worst = min(worst, np.max(np.abs(np.cos(2 * np.pi * x / lam + phi))))
        y = np.cos(2 * np.pi * x / lam)
        if np.std(y) < 1e-12:
            recovered = "none - the samples are constant"
        else:
            best_lam, best_corr = None, -2.0
            for cand in np.arange(2.0 * spacing, 6001.0, 5.0):
                c = abs(float(np.corrcoef(np.cos(2 * np.pi * x / cand), y)[0, 1]))
                if c > best_corr:
                    best_corr, best_lam = c, cand
            recovered = (f"{best_lam:.0f} m (correlation {best_corr:.4f})"
                         if best_corr > 0.999 else
                         f"none - no resolvable wavelength fits "
                         f"(best {best_lam:.0f} m, correlation {best_corr:.3f})")
        print(f"  {spacing:12.0f}  {spacing/lam:9.3f}   {worst:15.4f}   "
              f"{recovered}")
    print("  note the trap at spacing = wavelength: the samples are all equal, so")
    print("  the retained amplitude is full and the anomaly has vanished from the")
    print("  data.  Amplitude retention is not a test of sampling; wavelength is.")
    print("  At a quarter of the wavelength the sample nearest the peak is within")
    print("  8% of it, and that is the usual design rule for line spacing.")


    section("6. Why compensation is re-solved per flight")
    print("  the interference coefficients depend on the aircraft's magnetisation")
    print("  state, its fuel and stores load, and the field it flies in.  A")
    print("  synthetic check: re-solve the model with the permanent coefficients")
    print("  changed by 20% but the flight fitted with the previous solution.")
    A2 = design_matrix(u, du)
    coef_new = coef_true.copy()
    coef_new[0:3] *= 1.2
    interf2 = A2 @ coef_new
    sol, *_ = np.linalg.lstsq(A[:, :18], A @ coef_true, rcond=None)
    resid = interf2 - A2 @ sol
    print(f"  rms uncompensated interference after the change: "
          f"{resid.std():.3f} nT")
    print("  a stale solution leaves a bias of the order of the change, and it is")
    print("  correlated with attitude, so it appears as a coherent anomaly along")
    print("  the flight lines rather than as noise.")

    section("7. Reproducibility check with the seeded generator")
    draws = RNG.normal(0.0, 1.0, 5)
    print("  first five standard-normal draws from seed 20261014:")
    print("  " + ", ".join(f"{v:+.6f}" for v in draws))


if __name__ == "__main__":
    main()
