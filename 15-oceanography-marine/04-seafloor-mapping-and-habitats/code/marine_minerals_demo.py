#!/usr/bin/env python3
"""Marine minerals and deep-sea mining geophysics: the scale of the physical
anomalies a deposit produces, the electromagnetic depth of investigation in
seawater, the geostatistics of nodule abundance, and the resource arithmetic.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_minerals_demo.py

Everything here is SYNTHETIC.  The deposit, the abundance field and the grades are
teaching models with the stated model constants.  No real mine site, licence area,
deposit, cruise or survey is referenced, and no number is quoted from a published
measurement.

Contents
--------
1. Scale of the anomalies: gravity and magnetic effects of a model massive
   sulphide body, and the skin depth of seawater.
2. Electromagnetic depth of investigation: frequency, water-column attenuation
   and the detection limit at a stated noise level.
3. Geostatistics: a synthetic nodule-abundance field, its variogram, the fitted
   model, ordinary kriging and the kriging variance.
4. Resource arithmetic: tonnage, metal, the sample count for a target accuracy,
   and the sensitivity that dominates the answer.
5. Worked examples used in the lesson.
"""

import numpy as np
from scipy.optimize import curve_fit

RNG = np.random.default_rng(20261014)

G_NEWTON = 6.67430e-11     # m^3 kg^-1 s^-2 (standard constant)
MU0 = 4.0e-7 * np.pi       # H/m
M_GAL = 1.0e-5             # m/s^2 per mGal (exact definition)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sphere_gravity(rho_contrast, radius_m, depth_m):
    """Maximum vertical gravity anomaly of a buried sphere, in m/s^2."""
    return 4.0 / 3.0 * np.pi * G_NEWTON * rho_contrast * radius_m ** 3 / \
        depth_m ** 2


def dipole_field(moment_A_m2, distance_m):
    """Equatorial field of a dipole in T; on-axis is twice this value."""
    return MU0 / (4.0 * np.pi) * moment_A_m2 / distance_m ** 3


def skin_depth(rho_ohm_m, freq_hz):
    """Plane-wave skin depth in a conductor, m: delta = 503.29 sqrt(rho/f)."""
    return 503.29 * np.sqrt(rho_ohm_m / freq_hz)


def exp_variogram(h, nugget, sill_partial, rng_len):
    return nugget + sill_partial * (1.0 - np.exp(-h / rng_len))


def generate_field(n, dx, corr_len, nugget_sd, field_sd):
    """2-D field with exponential covariance plus an independent nugget."""
    kx = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(kx, kx)
    K2 = KX ** 2 + KY ** 2
    # spectral density of the exponential covariance: ~ 1/(1 + k^2 L^2)^(3/2)
    S = 1.0 / (1.0 + K2 * corr_len ** 2) ** 1.5
    noise = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    field = np.real(np.fft.ifft2(np.fft.fft2(noise) * np.sqrt(S)))
    field = field / field.std() * field_sd
    return field + RNG.normal(0.0, nugget_sd, field.shape)


def krige_ok(cov, x_obs, y_obs, x_target, y_target, variance, corr_len):
    """Ordinary kriging with an exponential covariance; returns (est, var)."""
    n = x_obs.size
    d_obs = np.hypot(x_obs[:, None] - x_obs[None, :],
                     y_obs[:, None] - y_obs[None, :])
    Cov = variance * np.exp(-d_obs / corr_len)
    np.fill_diagonal(Cov, variance)
    A = np.zeros((n + 1, n + 1))
    A[:n, :n] = Cov
    A[:n, n] = 1.0
    A[n, :n] = 1.0
    d_t = np.hypot(x_obs - x_target, y_obs - y_target)
    b = np.zeros(n + 1)
    b[:n] = variance * np.exp(-d_t / corr_len)
    b[n] = 1.0
    w = np.linalg.solve(A, b)
    est = float(np.dot(w[:n], cov))
    var = float(variance - np.dot(w, b))
    return est, var


def main():
    section("1. Scale of the physical anomalies of a model deposit")
    rho_c, radius, depth = 1500.0, 100.0, 1000.0
    dg = sphere_gravity(rho_c, radius, depth)
    print("  model massive-sulphide body: density contrast "
          f"{rho_c:.0f} kg/m^3, radius {radius:.0f} m, top at {depth:.0f} m")
    print(f"  gravity anomaly of an equivalent sphere:")
    print(f"    g = 4/3 pi G rho a^3 / z^2 = {dg:.4e} m/s^2 "
          f"= {dg / M_GAL:.4f} mGal")
    print(f"  (1 mGal = 1e-5 m/s^2, exactly)")
    print("  for comparison, shipborne gravity is repeatable to about a tenth of a")
    print("  mGal and seafloor gravimetry to a few hundredths: a single mound is at")
    print("  or below the detection limit of both.")
    print("\n  the same effect from a flat layer, for scale:")
    print("   thickness (m)   slab anomaly (mGal) for d(rho) = 1500 kg/m^3")
    for t in (10.0, 50.0, 100.0, 500.0):
        g = 2.0 * np.pi * G_NEWTON * rho_c * t / M_GAL
        print(f"   {t:13.0f}   {g:33.3f}")
    print("  a few tens of metres of altered crust or sediment is therefore easily")
    print("  visible; the ore body itself is not.")

    J_model, vol = 2.0, 4.0 / 3.0 * np.pi * radius ** 3
    m_dip = J_model * vol
    b = dipole_field(m_dip, depth)
    print(f"\n  magnetic effect of the same body with J = {J_model:.1f} A/m:")
    print(f"    volume = {vol:.3e} m^3, moment = {m_dip:.3e} A m^2")
    print(f"    equatorial field = {b * 1e9:.2f} nT (on-axis twice this)")
    print("  1 nT is at the level of a careful marine magnetometer survey, and the")
    print("  body is a 200 m sphere: magnetics maps the volcanic and alteration")
    print("  setting, not the deposit.")
    print(f"\n  skin depth of seawater (rho = 0.25 ohm m):")
    for f in (0.1, 1.0, 10.0, 100.0):
        print(f"    f = {f:6.1f} Hz: delta = {skin_depth(0.25, f):7.1f} m")
    for h in (200.0, 2000.0):
        att = 20.0 / np.log(10.0) * (-h / skin_depth(0.25, 1.0))
        print(f"  attenuation through {h:.0f} m of seawater at 1 Hz: "
              f"{att:.1f} dB (factor {10 ** (att / 20.0):.1e})")

    section("2. Electromagnetic depth of investigation")
    print("  a plane wave travelling down through the water to a seafloor system")
    print("  is attenuated as exp(-h/delta) with delta = 503.29 sqrt(rho/f):")
    print("\n   frequency (Hz)   delta(seawater)   loss over 2000 m   delta(1 ohm m crust)")
    for f in (0.1, 0.5, 1.0, 5.0, 25.0):
        ds = skin_depth(0.25, f)
        loss = 20.0 / np.log(10.0) * (-2000.0 / ds)
        print(f"   {f:14.1f}   {ds:15.1f}   {loss:16.1f}   "
              f"{skin_depth(1.0, f):20.1f}")
    f_needed = (503.29 * np.sqrt(0.25) / (2000.0 / np.log(100.0))) ** 2
    print(f"\n  to keep the water-column loss under 1% (20 dB) over 2000 m the")
    print(f"  frequency must fall to {f_needed:.3f} Hz, at which the skin depth in a")
    print(f" 1 ohm m crust is {skin_depth(1.0, f_needed):.0f} m: a frequency that")
    print("  reaches the seafloor resolves almost nothing beneath it.")
    print("  This is why marine EM is towed close to the seafloor: at 50 m")
    print(f"  altitude the loss at 1 Hz is "
          f"{20.0 / np.log(10.0) * (-50.0 / skin_depth(0.25, 1.0)):.1f} dB instead "
          f"of {20.0 / np.log(10.0) * (-2000.0 / skin_depth(0.25, 1.0)):.1f} dB.")
    noise_frac = 0.05
    print(f"\n  depth of investigation for a target whose response decays as")
    print(f"  exp(-z/delta) and a noise floor of {noise_frac * 100:.0f}% of the primary:")
    print("   frequency (Hz)   delta (1 ohm m)   max depth (m)")
    for f in (0.1, 1.0, 10.0, 100.0):
        dc = skin_depth(1.0, f)
        z_max = dc * np.log(1.0 / noise_frac)
        print(f"   {f:14.1f}   {dc:15.1f}   {z_max:13.0f}")
    print("  the model is a teaching approximation: it treats the target response as")
    print("  a diffusive decay rather than solving the scattering problem, so it")
    print("  gives the order of the depth, not a resolution.")

    section("3. Geostatistics of nodule abundance")
    n, dx, L, nug, sd, mean_ab = 400, 50.0, 2000.0, 1.5, 4.0, 15.0
    field = generate_field(n, dx, L, nug, sd) + mean_ab
    print(f"  synthetic abundance field: {n} x {n} cells at {dx:.0f} m "
          f"({n * dx / 1e3:.0f} km x {n * dx / 1e3:.0f} km)")
    print(f"  correlation length {L:.0f} m, field sd {sd:.2f} kg/m^2, nugget sd "
          f"{nug:.2f} kg/m^2, mean {mean_ab:.1f} kg/m^2")
    print(f"  realised field: mean {field.mean():.2f}, sd {field.std():.2f} "
          f"kg/m^2")

    def sample_grid(spacing_m):
        """Regular sample grid of the given spacing over the field."""
        step = int(round(spacing_m / dx))
        idx = np.arange(step // 2, n, step)
        return idx * dx, idx

    def variogram_from(xs, ys, z, lags, win):
        gamma = []
        for h in lags:
            vals = []
            for i in range(xs.size):
                d = np.hypot(xs[i:] - xs[i], ys[i:] - ys[i])
                sel = (np.abs(d - h) < win) & (d > 0)
                vals.extend(0.5 * (z[i] - z[i:])[sel] ** 2)
            gamma.append(np.mean(vals) if len(vals) >= 10 else np.nan)
        return np.array(gamma)

    sx, ix_s = sample_grid(1000.0)
    XS, YS = np.meshgrid(sx, sx)
    ZS = field[np.ix_(ix_s, ix_s)]
    xs, ys, zs = XS.ravel(), YS.ravel(), ZS.ravel()
    print(f"\n  a survey-style sampling grid at 1 km spacing gives {zs.size} "
          f"samples")
    lags = np.arange(250.0, 8000.0, 250.0)
    gamma = variogram_from(xs, ys, zs, lags, 100.0)
    ok = ~np.isnan(gamma)
    popt, _ = curve_fit(exp_variogram, lags[ok], gamma[ok],
                        p0=[nug ** 2, sd ** 2, L], maxfev=40000,
                        bounds=([0.0, 0.0, 50.0], [100.0, 400.0, 20000.0]))
    print("   lag (m)   gamma (kg/m^2)^2   fitted model")
    for h, g in zip(lags[::4], gamma[::4]):
        print(f"   {h:7.0f}   {g:17.2f}   {exp_variogram(h, *popt):12.2f}")
    print(f"  fitted: nugget {popt[0]:.2f}, partial sill {popt[1]:.2f}, range "
          f"{popt[2]:.0f} m")
    print(f"  true:   nugget {nug ** 2:.2f}, partial sill {sd ** 2:.2f}, range "
          f"{L:.0f} m")
    print("  the nugget is the intercept at zero lag: the variance that closer")
    print("  sampling cannot resolve.  Note the shortest populated lag is 250 m,")
    print("  which is why the nugget is only weakly constrained.")

    print("\n  estimator variance of the fitted range, five field realisations per")
    print("  sampling density (true range 2000 m):")
    print("   spacing (m)   samples   mean range (m)   sd of range (m)")
    for s_g in (500.0, 1000.0, 2000.0, 4000.0):
        rr = []
        for _ in range(5):
            f2 = generate_field(n, dx, L, nug, sd) + mean_ab
            x2, i2 = sample_grid(s_g)
            X2, Y2 = np.meshgrid(x2, x2)
            g2 = variogram_from(X2.ravel(), Y2.ravel(),
                                f2[np.ix_(i2, i2)].ravel(), lags, 100.0)
            m2 = ~np.isnan(g2)
            try:
                pt, _ = curve_fit(exp_variogram, lags[m2], g2[m2],
                                  p0=[nug ** 2, sd ** 2, L], maxfev=40000,
                                  bounds=([0.0, 0.0, 50.0],
                                          [100.0, 400.0, 20000.0]))
                rr.append(pt[2])
            except RuntimeError:
                continue
        rr = np.array(rr)
        print(f"   {s_g:12.0f}   {i2.size ** 2:7d}   {rr.mean():15.0f}   "
              f"{rr.std(ddof=1):15.0f}")
    print("  the range is identifiable to within a factor of about two at a 1 km")
    print("  spacing and becomes unreliable when the grid approaches the range.")

    print("\n  ordinary kriging at 60 validation cells, using the FITTED")
    print("  parameters and every second sample:")
    vx = RNG.integers(0, n, 60)
    vy = RNG.integers(0, n, 60)
    xk, yk, zk = xs[::2], ys[::2], zs[::2]
    errs, sds = [], []
    vc = max(popt[0] + popt[1], 1e-6)
    for a, b_ in zip(vx, vy):
        est, var = krige_ok(zk, xk, yk, a * dx, b_ * dx, vc, max(popt[2], 1.0))
        errs.append(est - field[a, b_])
        sds.append(np.sqrt(max(var, 0.0)))
    rms = np.sqrt(np.mean(np.square(errs)))
    print(f"    RMS error = {rms:.2f} kg/m^2")
    print(f"    mean kriging sd = {np.mean(sds):.2f} kg/m^2, ratio "
          f"{rms / np.mean(sds):.2f}")
    print("  the two should agree if the variogram is right; the ratio says how")
    print("  much the kriging variance under- or over-states the true error.")

    print("\n  how many samples for the AREA MEAN?  Monte-Carlo experiment over")
    print("  25 realisations: sample a regular grid and measure the spread of the")
    print("  estimated mean of the whole 400 km^2 area (true mean 15.0 kg/m^2):")
    print("   spacing (km)   samples   measured sd of mean   naive sigma/sqrt(n)")
    for s_km in (0.5, 1.0, 2.0, 4.0, 8.0):
        s_m = s_km * 1000.0
        step = int(round(s_m / dx))
        idxs = np.arange(step // 2, n, step)
        ests = []
        for _ in range(25):
            f2 = generate_field(n, dx, L, nug, sd) + mean_ab
            ests.append(f2[np.ix_(idxs, idxs)].mean())
        ests = np.array(ests)
        n_s = idxs.size ** 2
        print(f"   {s_km:13.1f}   {n_s:7d}   {ests.std(ddof=1):19.3f}   "
              f"{field.std() / np.sqrt(n_s):19.3f}")
    print("  at every spacing finer than the range the measured spread is much")
    print("  larger than the independent-sample formula (by 5-9x), and it stops")
    print("  improving once the grid is finer than the")
    print("  range: beyond that point the error is the difference between the")
    print("  area's own mean and the regional mean, which no denser sampling of")
    print("  the same area can remove.")

    section("4. Resource arithmetic")
    area_km2, abundance, grade_ni, grade_cu = 400.0, float(zs.mean()), 0.013, 0.011
    area = area_km2 * 1e6
    tonnage = area * abundance * 1e3 / 1e3      # kg -> t: 1 kg/m^2 x m^2 = t/1000
    tonnage = area * abundance / 1e3            # wet tonnes
    print(f"  area {area_km2:.0f} km^2, mean abundance {abundance:.1f} kg/m^2 "
          f"(wet)")
    print(f"  tonnage = A x abundance = {tonnage:.3e} t = {tonnage / 1e6:.1f} "
          f"Mt (wet)")
    ni = tonnage * grade_ni
    cu = tonnage * grade_cu
    print(f"  at grades Ni {grade_ni * 100:.2f}% and Cu {grade_cu * 100:.2f}% "
          f"(model values):")
    print(f"    contained Ni = {ni:.3e} t, contained Cu = {cu:.3e} t")
    print("  sensitivity of contained metal to the three inputs:")
    print("   abundance (kg/m^2)   tonnage (Mt)   Ni (10^3 t)   Cu (10^3 t)")
    for ab in (5.0, 10.0, 15.0, 20.0, 30.0):
        t2 = area * ab / 1e3
        print(f"   {ab:18.1f}   {t2 / 1e6:12.1f}   {t2 * grade_ni / 1e3:13.1f}   "
              f"{t2 * grade_cu / 1e3:13.1f}")
    print(f"  abundance, grade and area each enter linearly, so a factor of two in")
    print(f"  any one is a factor of two in the metal.")

    cv = 0.5
    print(f"\n  sample count for a relative error of 10% at 95% confidence")
    print(f"  (n = (1.96 cv / eps)^2) for a coefficient of variation cv:")
    print("   cv     samples for eps = 10%   for eps = 20%   for eps = 30%")
    for cv_i in (0.2, 0.5, 1.0, 1.5):
        print(f"   {cv_i:4.1f}   {int(np.ceil((1.96 * cv_i / 0.10) ** 2)):20d}   "
              f"{int(np.ceil((1.96 * cv_i / 0.20) ** 2)):13d}   "
              f"{int(np.ceil((1.96 * cv_i / 0.30) ** 2)):13d}")
    print(f"  with cv = {cv} (a moderate value for nodule abundance) a 10% resource")
    print(f"  figure needs {int(np.ceil((1.96 * cv / 0.10) ** 2))} independent box-core")
    print("  samples taking into account the correlation length, and the samples must")
    print("  be spaced further apart than the range or they count as one.")

    section("5. Worked examples used in the lesson")
    print(f"(a) sphere gravity anomaly = {dg / M_GAL:.4f} mGal for a "
          f"{2 * radius:.0f} m body at {depth:.0f} m")
    print(f"(b) dipole field at {depth:.0f} m = {b * 1e9:.2f} nT")
    print(f"(c) seawater skin depth at 1 Hz = {skin_depth(0.25, 1.0):.0f} m; "
          f"loss over 2000 m = "
          f"{20.0 / np.log(10.0) * (-2000.0 / skin_depth(0.25, 1.0)):.1f} dB")
    print(f"(d) fitted variogram: nugget {popt[0]:.2f}, partial sill "
          f"{popt[1]:.2f}, range {popt[2]:.0f} m; kriging RMS "
          f"{np.sqrt(np.mean(np.square(errs))):.2f} kg/m^2 against a mean kriging "
          f"sd of {np.mean(sds):.2f}")
    print(f"(e) tonnage {tonnage / 1e6:.1f} Mt wet, contained Ni "
          f"{ni / 1e3:.1f} x 10^3 t")
    print(f"(f) samples for a 10% abundance estimate at cv = {cv}: "
          f"{int(np.ceil((1.96 * cv / 0.10) ** 2))}")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
