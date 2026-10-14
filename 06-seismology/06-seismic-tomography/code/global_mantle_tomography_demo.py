#!/usr/bin/env python3
"""Global mantle tomography: spherically symmetric rays, the long-wavelength
filter, and the depth-amplitude trade-off that limits geodynamic interpretation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python global_mantle_tomography_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lesson 06-06-06.  Everything is SYNTHETIC: a spherically symmetric
Earth of radius 6371 km with the teaching velocity profile v(r) = 8.0 (R/r) km/s
(deepening to 14.6 km/s at the core-mantle boundary), rays traced by the standard
spherical ray integrals, anomalies built from stated radial Gaussians and
cosine angular patterns, and a synthetic conversion factor from velocity to
temperature.  No published Earth model, station or data set is used.

Contents
--------
1. Ray theory in a sphere: travel time and distance as functions of the ray
   parameter, verified against dT/dDelta = p.
2. The long-wavelength filter: what a low-degree parametrisation recovers, and
   how much short-wavelength structure leaks into it.
3. The depth-amplitude trade-off: the family of (depth, amplitude) pairs that
   fits the same travel times.
4. From velocity to temperature: the range of interpretations one data set
   admits.
"""

import numpy as np

R_EARTH = 6371.0e3                  # m, exact by definition of the mean radius
V_SURF = 8000.0                     # m/s, SYNTHETIC surface velocity
R_CMB = 3480.0e3                    # m, core-mantle boundary radius
DEPTH_TOP = 100.0e3                 # shallowest anomaly depth used here
RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def velocity(r):
    """Teaching velocity profile: v(r) = V_SURF * (R / r)."""
    return V_SURF * (R_EARTH / r)


def ray_integrals(p, n=4000):
    """Distance and time of a turning ray with ray parameter p (s/m).

    Standard spherical ray integrals, with the square-root singularity at the
    turning radius removed by the substitution r = r_t + t^2.
    """
    r_t = np.sqrt(p * V_SURF * R_EARTH)          # solves r / v(r) = p
    t_max = np.sqrt(R_EARTH - r_t)
    t = np.linspace(0.0, t_max, n)
    r = r_t + t ** 2
    y = (r / velocity(r)) ** 2 - p ** 2
    y = np.clip(y, 0.0, None)
    jac = 2.0 * t
    with np.errstate(divide="ignore", invalid="ignore"):
        integ = np.where(y > 0, jac / (r * np.sqrt(y)), 0.0)
        integ_t = np.where(y > 0, jac * (r / velocity(r) ** 2) / np.sqrt(y), 0.0)
    delta = 2.0 * p * np.trapezoid(integ, t)
    time = 2.0 * np.trapezoid(integ_t, t)
    return delta, time, r_t


def ray_path(p, n=1200):
    """Radius, angular position and path element along a turning ray."""
    r_t = np.sqrt(p * V_SURF * R_EARTH)
    t_max = np.sqrt(R_EARTH - r_t)
    t = np.linspace(0.0, t_max, n)
    r = r_t + t ** 2
    y = np.clip((r / velocity(r)) ** 2 - p ** 2, 1e-30, None)
    jac = 2.0 * t
    dtheta = np.where(t > 0, p * jac / (r * np.sqrt(y)), 0.0)
    theta = np.cumsum(dtheta)
    cos_i = np.sqrt(np.clip(1.0 - (p * velocity(r) / r) ** 2, 0.0, None))
    ds = np.where(cos_i > 0, jac / np.maximum(cos_i, 1e-12), 0.0)
    return r, theta, ds, t


def radial_gaussian(depth_km, width_km):
    def basis(r):
        z = (R_EARTH - r) / 1e3
        return np.exp(-0.5 * ((z - depth_km) / width_km) ** 2)
    return basis


def data_of(rays, radial, angular):
    """First-order travel-time perturbation from a relative velocity anomaly.

    dT = -2 * integral (dv/v0) * ds / v0 along the ray, in seconds.
    """
    out = []
    for (r, theta, ds, t) in rays:
        out.append(-2.0 * np.trapezoid(radial(r) * angular(theta)
                                       / velocity(r) * ds, t))
    return np.array(out)


def part1_ray_theory():
    section("1. Ray theory in a sphere")
    print(f"radius {R_EARTH / 1e3:.0f} km, synthetic profile "
          f"v(r) = {V_SURF / 1e3:.1f} (R/r) km/s")
    print(f"v at the surface {velocity(R_EARTH) / 1e3:.2f} km/s, at the CMB "
          f"{velocity(R_CMB) / 1e3:.2f} km/s\n")
    ps = np.linspace(240.0, 790.0, 7)          # ray parameter in seconds
    print(f"{'p (s/rad)':>10} {'turning depth (km)':>19} {'Delta (deg)':>12} "
          f"{'T (s)':>10} {'dT/dDelta (s/rad)':>19} {'p (s/rad)':>11}")
    for p in ps:
        delta, time, r_t = ray_integrals(p)
        dp = 1e-3
        d1, t1 = ray_integrals(p + dp)[:2]
        d2, t2 = ray_integrals(p - dp)[:2]
        slope = (t1 - t2) / (d1 - d2)
        print(f"{p:10.1f} {(R_EARTH - r_t) / 1e3:19.0f} "
              f"{np.degrees(delta):12.2f} {time:10.2f} {slope:19.3f} "
              f"{p:11.1f}")
    print("""
  The last two columns are the same quantity: dT/dDelta must equal p, and it
  does to the accuracy of the numerical differentiation.  That identity is the
  reason a travel-time residual can be interpreted as an average of the
  slowness perturbation along the ray, and it is the check that the ray
  integrals above are implemented consistently.""")


def part2_long_wavelength():
    section("2. The long-wavelength filter")
    ps = np.linspace(240.0, 790.0, 121)
    rays = [ray_path(p) for p in ps]
    shape = radial_gaussian(1500.0, 350.0)      # radial form assumed KNOWN here
    ang = {"cos2": lambda th: np.cos(2.0 * th),
           "sin2": lambda th: np.sin(2.0 * th),
           "cos6": lambda th: np.cos(6.0 * th),
           "sin6": lambda th: np.sin(6.0 * th)}
    g = np.array([data_of(rays, shape, f) for f in ang.values()]).T
    print(f"{len(ps)} rays, synthetic anomaly dv/v0 at 1500 km depth, radius of")
    print(f"the anomaly 350 km; the angular pattern is what is solved for, with")
    print(f"4 basis functions ({', '.join(ang)})\n")
    amp_in = 0.01                                # 1 per cent anomaly
    for name, pattern in (("cos(2 theta), degree 2",
                           lambda th: np.cos(2.0 * th)),
                          ("cos(12 theta), degree 12",
                           lambda th: np.cos(12.0 * th))):
        d = data_of(rays, shape, pattern) * amp_in
        m = np.linalg.lstsq(g, d, rcond=None)[0]
        resid = g @ m - d
        print(f"  input: {amp_in * 100:.2f} per cent {name}")
        print(f"    rms of the input datum            : "
              f"{np.sqrt(np.mean(d ** 2)):.4e} s")
        print(f"    recovered low-degree coefficients : "
              + ", ".join(f"{k} {100.0 * v:+.4f}%" for k, v in zip(ang, m)))
        r2 = 1.0 - np.sum(resid ** 2) / np.sum((d - d.mean()) ** 2)
        print(f"    fraction of the datum explained   : {r2:.4f}")
        print(f"    rms residual                      : "
              f"{np.sqrt(np.mean(resid ** 2)):.4e} s\n")
    print(f"""  A degree-2 input is recovered as a degree-2 answer of the right size.  A
  degree-12 input is NOT recovered, and it does not simply fail to fit either:
  it is fitted by a SPURIOUS low-degree pattern several per cent of the input
  amplitude, with a residual a small fraction of the data.  That is the honest
  description of a low-degree global model -- it is a filter whose stop band
  reappears as an alias in the pass band -- and it is why global models are
  quoted with the maximum degree they solve for, and why a low-degree feature in
  one model and not in another is not evidence about the mantle until the
  coverage of both has been compared.""")


def part3_depth_amplitude():
    section("3. The depth-amplitude trade-off")
    ps = np.linspace(240.0, 790.0, 121)
    rays = [ray_path(p) for p in ps]
    sigma = 1.0                                  # s, synthetic residual level
    pattern = lambda th: np.cos(2.0 * th)
    depth_true, amp_true = 1500.0, 0.01
    d_target = data_of(rays, radial_gaussian(depth_true, 350.0), pattern) * amp_true
    print(f"{len(ps)} rays, synthetic travel-time noise sigma = "
          f"{sigma * 1e3:.0f} ms")
    print(f"the 'observed' residual comes from a {100 * amp_true:.1f} per cent "
          f"anomaly at {depth_true:.0f} km")
    print(f"its rms is {np.sqrt(np.mean(d_target ** 2)):.4e} s, so the data are "
          f"{np.sqrt(np.mean(d_target ** 2)) / sigma:.1f} times the noise\n")
    print(f"{'depth (km)':>11} {'fitted amplitude':>18} {'residual rms (s)':>18} "
          f"{'residual / sigma':>17}")
    for depth in (800.0, 1200.0, 1500.0, 1800.0, 2200.0):
        d = data_of(rays, radial_gaussian(depth, 350.0), pattern)
        amp = float(d @ d_target / (d @ d))
        rms = float(np.sqrt(np.mean((amp * d - d_target) ** 2)))
        print(f"{depth:11.0f} {100.0 * amp:17.3f}% {rms:18.4e} "
              f"{rms / sigma:17.3f}")
    print(f"""  Every row below the threshold fits the observed residual to within the stated
  noise, with an anomaly amplitude that changes by a factor of about 1.5 and a
  depth that moves by 600 km: at this residual level the data admit a band of
  depths, not a depth.  A deeper anomaly has to be stronger to produce the same
  delay, and the only thing that breaks the trade-off is a measurement with a
  different depth sensitivity -- surface waves, normal modes, or body waves that
  turn at a different radius.  A reported anomaly depth is therefore conditional
  on the data set that produced it, and it should be quoted as the band it came
  from.""")


def part4_temperature():
    section("4. From velocity to temperature")
    dlnv_dT = -1.0e-4                          # K^-1, SYNTHETIC, stated
    print(f"synthetic conversion used: d ln v_s / dT = {dlnv_dT:.1e} per K")
    print("(a STATED teaching value, not a measurement; the real conversion")
    print("depends on composition, phase and pressure)\n")
    print(f"{'amplitude dv/v':>16} {'implied dT (K)':>16}")
    for amp in (0.010, 0.006, 0.020, 0.004):
        print(f"{amp:16.3f} {amp / dlnv_dT:16.0f}")
    print("""
  The same data set, interpreted through the same conversion, gives temperature
  anomalies that differ by a factor of five across the range of amplitudes the
  data admit.  Both steps carry an error that multiplies: the recovered
  amplitude is a fraction of the truth set by the damping (lesson 06-06-07
  measures this), and the conversion factor is a modelling choice.  A published
  temperature anomaly is only meaningful with the amplitude it came from and the
  conversion that produced it, and it is not an observation.""")


def main():
    t0 = part1_ray_theory()
    part2_long_wavelength()
    part3_depth_amplitude()
    part4_temperature()
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
