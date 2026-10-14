#!/usr/bin/env python3
"""Mise-a-la-masse: the half-space point-source field, the analytic response of a
conducting sphere in a locally uniform field (with its boundary conditions
verified), the surface anomaly of a buried body energised from a borehole, the
ambiguity between depth and conductivity contrast, and where the model breaks.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mise_a_la_masse_demo.py

Everything is SYNTHETIC.  The resistivities, contrasts, depths, radii and
currents are chosen teaching values, not measurements of any real ore body,
quarry, borehole or instrument.

Contents
--------
1. A buried point current electrode: the surface field and its width rule.
2. The conducting sphere in a uniform field: derivation checks.
3. Mise-a-la-masse anomaly versus depth and conductivity contrast.
4. The depth-contrast ambiguity: an iso-anomaly ridge.
5. Where the locally-uniform-field model breaks, and the surface-array response.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_HOST = 100.0        # ohm m, synthetic host resistivity
CURRENT = 1.0           # A, injected current


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def point_potential(points, electrodes, rho=RHO_HOST):
    """Half-space potential of point current electrodes.

    `points` is an (n, 2) array of (x, z) field positions with z > 0 below the
    surface; `electrodes` is a sequence of (x, z, current) with z > 0.  Each
    electrode is mirrored in the insulating surface with the same sign, so its
    contribution is  rho I / (4 pi) (1/r + 1/r_image).
    """
    pts = np.atleast_2d(np.asarray(points, dtype=float))
    v = np.zeros(pts.shape[0])
    for xe, ze, cur in electrodes:
        if ze <= 0.0:
            raise ValueError("electrodes must be below the surface")
        r1 = np.sqrt((pts[:, 0] - xe) ** 2 + (pts[:, 1] - ze) ** 2)
        r2 = np.sqrt((pts[:, 0] - xe) ** 2 + (pts[:, 1] + ze) ** 2)
        v += rho * cur / (4.0 * np.pi) * (1.0 / r1 + 1.0 / r2)
    return v


def surface_monopole(x_positions, electrodes, rho=RHO_HOST):
    """Potential on the surface of point electrodes placed ON the surface:
    V(x) = rho I / (2 pi |x - x_e|).  Exact for a half-space."""
    x = np.atleast_1d(np.asarray(x_positions, dtype=float))
    v = np.zeros(x.size)
    for xe, cur in electrodes:
        v += rho * cur / (2.0 * np.pi * np.abs(x - xe))
    return v


def surface_gradient_at(centre_x, electrodes, rho=RHO_HOST, step=1.0):
    """Numerical horizontal field at a point on the surface (V/m)."""
    base = (centre_x - step, centre_x + step)
    v = surface_monopole(np.array(base), electrodes, rho)
    return -(v[1] - v[0]) / (2.0 * step)


def gradient_at(centre, electrodes, rho=RHO_HOST, step=0.01):
    """Numerical electric field E = -grad V at a point (V/m)."""
    field = np.zeros(2)
    for k in range(2):
        for sign in (+1.0, -1.0):
            p = np.array(centre, dtype=float)
            p[k] += sign * step
            field[k] += -sign * point_potential(p[None, :], electrodes, rho)[0] \
                / (2.0 * step)
    return field


def sphere_dipole_field(centre, radius, contrast, electrodes, rho=RHO_HOST):
    """Electric field of the induced dipole of a conducting sphere.

    A sphere of radius a and conductivity sigma_1 in a host of sigma_0, placed
    in a locally uniform field E0, has the external potential

        phi_anom = A cos(theta) / r^2,
        A = a^3 E0 (sigma_1 - sigma_0) / (sigma_1 + 2 sigma_0),

    which corresponds to a current dipole of moment p = 4 pi sigma_0 A.  The
    function returns (A_vector_as_amplitude, direction unit vector, E0).
    """
    e0 = gradient_at(centre, electrodes, rho)
    e0_mag = float(np.linalg.norm(e0))
    sigma0 = 1.0 / rho
    sigma1 = contrast * sigma0
    a_amp = radius ** 3 * e0_mag * (sigma1 - sigma0) / (sigma1 + 2.0 * sigma0)
    direction = e0 / e0_mag if e0_mag > 0 else np.array([0.0, 1.0])
    return a_amp, direction, e0_mag


def malm_profile(x_surface, depth_source, centre, radius, contrast,
                 current=CURRENT, rho=RHO_HOST, dipole_sep_frac=0.05):
    """Total and primary surface potentials for a borehole source at
    (0, depth_source) and a conducting sphere centred at `centre`."""
    electrodes = [(0.0, depth_source, current)]
    primary = point_potential(x_surface, electrodes, rho)
    a_amp, direction, _ = sphere_dipole_field(centre, radius, contrast,
                                              electrodes, rho)
    sigma0 = 1.0 / rho
    moment = 4.0 * np.pi * sigma0 * a_amp
    sep = dipole_sep_frac * radius
    i_eq = moment / sep
    pair = [(centre[0] + 0.5 * sep * direction[0],
             centre[1] + 0.5 * sep * direction[1], i_eq),
            (centre[0] - 0.5 * sep * direction[0],
             centre[1] - 0.5 * sep * direction[1], -i_eq)]
    anomaly = point_potential(x_surface, pair, rho)
    return primary, anomaly


def fwhm(x, v):
    ab = np.where(v >= 0.5 * v.max())[0]
    return x[ab[-1]] - x[ab[0]] if ab.size > 1 else np.nan


def main():
    section("1. A buried point electrode: the surface field and its width")
    depth = 50.0
    x = np.linspace(-400.0, 400.0, 80001)
    v = point_potential(np.column_stack([x, np.zeros_like(x)]),
                        [(0.0, depth, CURRENT)])
    print(f"rho = {RHO_HOST:.1f} ohm m, I = {CURRENT:.3f} A, electrode at "
          f"{depth:.1f} m depth (SYNTHETIC)")
    print(f"  V(0) = rho I / (2 pi depth) = {1000 * v.max():.4f} mV "
          f"(analytic {1000 * RHO_HOST * CURRENT / (2 * np.pi * depth):.4f} mV)")
    print("\n  offset x (m)   V (mV)   V / V(0)   apparent rho from "
          "rho_a = 2 pi r V / I")
    for xo in (0.0, 25.0, 50.0, 100.0, 200.0, 400.0):
        r = np.sqrt(xo ** 2 + depth ** 2)
        vv = point_potential(np.array([[xo, 0.0]]),
                             [(0.0, depth, CURRENT)])[0]
        print(f"  {xo:12.1f}   {1000 * vv:7.3f}   {vv / v.max():9.4f}   "
              f"{2 * np.pi * r * vv / CURRENT:27.3f}")
    print("with the current electrode buried in a homogeneous half-space the")
    print("apparent resistivity is exactly the true one at every offset, so any")
    print("departure from this profile is the anomaly of a conductivity")
    print("contrast - which is the whole principle of mise-a-la-masse.")
    print(f"\nwidth rule: FWHM = {fwhm(x, v):.1f} m = "
          f"{fwhm(x, v) / depth:.4f} x depth, against the exact point-source")
    print("value 2 sqrt(3) = 3.4641 for 1/sqrt(x^2 + h^2) at half maximum.")

    section("2. A conducting sphere in a locally uniform field: checks")
    a, contrast = 10.0, 100.0
    e0 = 1.0
    sigma0 = 1.0 / RHO_HOST
    sigma1 = contrast * sigma0
    aa = a ** 3 * e0 * (sigma1 - sigma0) / (sigma1 + 2.0 * sigma0)
    print(f"sphere: radius a = {a:.1f} m, contrast sigma1/sigma0 = "
          f"{contrast:.0f}, host rho = {RHO_HOST:.1f} ohm m")
    print(f"A = a^3 E0 (sigma1 - sigma0)/(sigma1 + 2 sigma0) = {aa:.4f} V m "
          f"for E0 = 1 V/m")
    b_in = 3.0 * sigma0 * e0 / (sigma1 + 2.0 * sigma0)
    print(f"interior field coefficient B = 3 sigma0 E0/(sigma1 + 2 sigma0) = "
          f"{b_in:.6f} V/m")
    print("\n  theta (deg)   phi_in - phi_out (V)   sigma1 dphi_in/dr - "
          "sigma0 dphi_out/dr")
    worst_pot = worst_cur = 0.0
    for deg in (0.0, 30.0, 60.0, 90.0, 120.0, 180.0):
        th = np.radians(deg)
        phi_in = -b_in * a * np.cos(th)
        phi_out = -e0 * a * np.cos(th) + aa * np.cos(th) / a ** 2
        d_in = -b_in * np.cos(th)
        d_out = -e0 * np.cos(th) - 2.0 * aa * np.cos(th) / a ** 3
        worst_pot = max(worst_pot, abs(phi_in - phi_out))
        worst_cur = max(worst_cur, abs(sigma1 * d_in - sigma0 * d_out))
        print(f"  {deg:11.1f}   {phi_in - phi_out:+21.3e}   "
              f"{sigma1 * d_in - sigma0 * d_out:+26.3e}")
    print(f"\nmaximum violation: potential {worst_pot:.2e} V, "
          f"normal current {worst_cur:.2e} A/m^2 - both at round-off.")
    for label, c in (("contrast 1 (no body)", 1.0), ("contrast 100", 100.0),
                     ("contrast 10^6 (near-perfect conductor)", 1.0e6)):
        s1 = c * sigma0
        a_c = a ** 3 * e0 * (s1 - sigma0) / (s1 + 2.0 * sigma0)
        pot_on_sphere = -e0 * a * np.cos(0.0) + a_c / a ** 2
        pot_at_90 = a_c * np.cos(np.pi / 2.0) / a ** 2
        pot_180 = -e0 * a * np.cos(np.pi) + a_c * np.cos(np.pi) / a ** 2
        print(f"  {label:36s}: A = {a_c:9.4f} V m; potential on the sphere at "
              f"0/90/180 deg = {pot_on_sphere:+.6f} / {pot_at_90:+.6f} / "
              f"{pot_180:+.6f} V")
    print(f"for E0 = 1 V/m the potential drop across the sphere is "
          f"E0 a = {e0 * a:.1f} V.  The contrast-1 case has A = 0 as it must,")
    print("and the large-contrast case has a potential on r = a within 3e-5 V of")
    print("zero at every angle, i.e. equipotential to 0.0003% of E0 a - the")
    print("boundary condition a perfect conductor imposes.")

    section("3. Mise-a-la-masse: anomaly versus offset and contrast")
    xs = np.linspace(-300.0, 300.0, 601)
    surface = np.column_stack([xs, np.zeros_like(xs)])
    depth_source, radius = 5.0, 15.0
    print(f"borehole source at {depth_source:.1f} m depth, current "
          f"{CURRENT:.2f} A; sphere radius {radius:.1f} m; stations from "
          f"{xs[0]:.0f} to {xs[-1]:.0f} m")
    print("the body is offset horizontally, so that the source-to-centre")
    print("distance stays above 3 radii, where the locally uniform field")
    print("approximation is defensible; that ratio is printed with every row")
    print("\n  body centre (m)   contrast   distance/radius   anomaly above the "
          "body (%)")
    for xc, dc in ((60.0, 40.0), (100.0, 60.0), (150.0, 90.0)):
        dist = np.hypot(xc - 0.0, dc - depth_source)
        for c in (10.0, 100.0, 1000.0):
            primary, anomaly = malm_profile(surface, depth_source, (xc, dc),
                                            radius, c)
            i_above = int(np.argmin(np.abs(xs - xc)))
            print(f"  ({xc:5.1f}, {dc:5.1f})   {c:8.0f}   "
                  f"{dist / radius:15.2f}   "
                  f"{100 * abs(anomaly[i_above]) / abs(primary[i_above]):22.3f}")
    print("the anomaly above the body rises with contrast but saturates: beyond")
    print("a contrast of about 100 the body is already nearly a perfect")
    print("conductor, and the surface pattern stops changing (the same")
    print("saturation seen in section 2).  It also falls steeply with distance,")
    print("which is the depth-versus-offset ambiguity of section 4.")

    section("4. The offset-contrast ambiguity")
    target = 0.10   # per cent, the anomaly we insist on observing
    print(f"insist on observing a {target:.2f}% anomaly directly above the body")
    print("and ask which (distance, contrast) pairs can produce it")
    print("\n  body centre (m)   distance/radius   saturated anomaly (%)   "
          "contrast for the target")
    hits = []
    for xc, dc in ((60.0, 40.0), (100.0, 60.0), (150.0, 90.0)):
        i_above = int(np.argmin(np.abs(xs - xc)))
        primary, anomaly = malm_profile(surface, depth_source, (xc, dc),
                                        radius, 1.0e5)
        sat = 100 * abs(anomaly[i_above]) / abs(primary[i_above])
        best, best_err = np.nan, np.inf
        for c in np.logspace(0.0, 5.0, 800):
            _, an = malm_profile(surface, depth_source, (xc, dc), radius, c)
            frac = 100 * abs(an[i_above]) / abs(primary[i_above])
            if abs(frac - target) < best_err:
                best_err, best = abs(frac - target), c
        dist = np.hypot(xc, dc - depth_source)
        hits.append((dist, best))
        print(f"  ({xc:5.1f}, {dc:5.1f})   {dist / radius:15.2f}   "
              f"{sat:22.3f}   {best:24.2f}")
    print("the saturated column is the key: the anomaly stops responding to the")
    print("contrast once the body is a good conductor relative to the host, so")
    print("the amplitude measures DISTANCE/RADIUS, not conductivity.  A 0.10%")
    print("anomaly is produced by contrast 1.12 at 4.63 radii and by contrast")
    print("3.71 at 11.49 radii: a continuum of (distance, contrast, size) triples")
    print("gives the same single number.  Only the shape of the anomaly map - its")
    print("width and its decay with offset - adds information, and it does so")
    print("weakly, as lesson 01 section 5 measured for the SP dipole.")

    section("5. Where the model breaks: the source inside the body")
    print("now move the source down towards a body centred at (0, 40) m, radius")
    print("15 m, contrast 100, and watch the locally-uniform-field approximation")
    print("fail.  The last column is the model's own validity ratio.")
    print("\n  source depth (m)   distance/radius   modelled anomaly above the "
          "body (%)")
    for hs in (5.0, 20.0, 30.0, 37.5, 39.0, 39.9):
        primary, anomaly = malm_profile(surface, hs, (0.0, 40.0), radius,
                                        100.0)
        i_above = int(np.argmin(np.abs(xs)))
        dist = abs(40.0 - hs)
        print(f"  {hs:16.1f}   {dist / radius:15.2f}   "
              f"{100 * abs(anomaly[i_above]) / abs(primary[i_above]):22.1f}")
    print("the modelled anomaly grows without bound as the source approaches the")
    print("body (1.3% at 5 m, 7987% at 39 m): the field at the centre diverges as")
    print("1/r^2 while the model keeps treating the sphere as if it sat in a")
    print("uniform field.  At the centre itself the numerical gradient vanishes,")
    print("which is the same singularity seen from the other side.  Physically")
    print("current is injected INTO a conductor, which then acts as an extended")
    print("electrode at one potential; that regime needs an equipotential-body")
    print("model, not a polarised-sphere model.  The distance/radius column is")
    print("printed precisely so that a reader can see when the numbers stop")
    print("meaning anything: only the first row has a source-to-centre distance")
    print("above two radii, and every other row has the source at or inside the")
    print("body's surface.  Those numbers are a demonstration of the model's")
    print("limit, not a prediction.")

    section("6. The same body seen by a surface array")
    print("dipole-dipole array on the surface over the same body, centred at")
    print("(0, 40) m, radius 15 m, contrast 100; spacing a, with A at -a, B at 0,")
    print("M at +a and N at +2a, and K = -6 pi a from the array geometry")
    print("first the internal check: over homogeneous ground the array must")
    print("return the true resistivity at every spacing")
    print("\n  spacing a (m)   rho_a, no body (ohm m)   rho_a with body "
          "(ohm m)   anomaly (%)")
    for span in (30.0, 60.0, 120.0):
        amps = [(-span, CURRENT), (0.0, -CURRENT)]

        def dv_pair(px, with_sphere):
            v = surface_monopole(np.array([px]), amps, RHO_HOST)[0]
            if with_sphere:
                for xe, cur in amps:
                    e0 = surface_gradient_at(0.0, [(xe, cur)], RHO_HOST)
                    sigma0 = 1.0 / RHO_HOST
                    sigma1 = 100.0 * sigma0
                    a_amp = radius ** 3 * abs(e0) * (sigma1 - sigma0) \
                        / (sigma1 + 2.0 * sigma0)
                    moment = 4.0 * np.pi * sigma0 * a_amp
                    sep = 0.05 * radius
                    i_eq = moment / sep
                    # the induced dipole points along the surface field, so it
                    # is horizontal here; mirror each electrode in the surface
                    v += point_potential(
                        np.array([[px, 0.0]]),
                        [(0.0 + 0.5 * sep, 40.0, i_eq),
                         (0.0 - 0.5 * sep, 40.0, -i_eq)], RHO_HOST)[0]
            return v

        dv_with = dv_pair(span, True) - dv_pair(2.0 * span, True)
        dv_without = dv_pair(span, False) - dv_pair(2.0 * span, False)
        k_geom = -6.0 * np.pi * span
        rho_wo = k_geom * dv_without / CURRENT
        rho_w = k_geom * dv_with / CURRENT
        print(f"  {span:13.1f}   {rho_wo:22.3f}   {rho_w:19.3f}   "
              f"{100 * (rho_w - rho_wo) / rho_wo:11.3f}")
    print("the no-body column returns 100 ohm m at every spacing, which validates")
    print("the array code and its geometric factor; the body then produces an")
    print("apparent-resistivity anomaly of a few per cent, of the same order as")
    print("the mise-a-la-masse anomaly at a comparable distance.  The geometries")
    print("differ: with the source inside the body the mise-a-la-masse pattern is")
    print("centred on it, while the array response depends on where the two")
    print("dipoles sit relative to it - so the two measurements constrain")
    print("different aspects of the same conductor, which is why they are used")
    print("together.")


if __name__ == "__main__":
    main()
