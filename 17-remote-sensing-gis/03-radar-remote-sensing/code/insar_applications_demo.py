#!/usr/bin/env python3
"""InSAR applications: a verified elastic dislocation model, a synthetic
interferogram and its aliasing limit, the ascending/descending decomposition,
a volcanic source, a seasonal subsidence, and a landslide gradient budget.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_applications_demo.py

Everything is SYNTHETIC: the slip, source depths, volumes, rates and scene
geometries are teaching values generated here.  No real earthquake, volcano,
subsidence field or landslide is modelled, and no measured displacement appears.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0                 # m/s
LAM = C / 5.300e9                 # m   teaching carrier


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def strike_slip_profile(x, d, slip):
    """Surface fault-parallel displacement of a long strike-slip fault.

    Standard antiplane (mode III), 2-D, homogeneous elastic half-space model:
    uniform slip b on the fault below the locking depth d, giving

        u(x) = (b / pi) arctan(x / d),

    a monotone profile with u -> +-b/2 at infinity (total offset b), maximum
    surface shear strain b/(pi d) at the trace, and u(d) = b/4.
    """
    return slip / np.pi * np.arctan(x / d)


def los_unit(heading_deg, inc_deg):
    """Line-of-sight unit vector (ground to satellite) in (E, N, U)."""
    alpha = np.radians(heading_deg)
    th = np.radians(inc_deg)
    return np.array([np.sin(th) * np.cos(alpha), -np.sin(th) * np.sin(alpha),
                     np.cos(th)])


def main():
    section("1. The strike-slip model, verified rather than asserted")
    slip = 2.0                 # m of strike-slip, SYNTHETIC
    depth = 4000.0             # m, locking depth of the fault
    x = np.linspace(-60000.0, 60000.0, 6001)   # 20 m grid = one pixel
    u = strike_slip_profile(x, depth, slip)
    print(f"SYNTHETIC long strike-slip fault: slip b = {slip:.1f} m, "
          f"locking depth d = {depth/1000:.1f} km")
    print("model: 2-D antiplane (mode III) homogeneous elastic half-space, uniform")
    print("slip below depth d, so u(x) = (b/pi) arctan(x/d).  The model is a stated")
    print("assumption; what the demo does is verify its consequences.\n")
    u_inf = slip / 2.0
    print(f"  (a) far-field limits: u(-1 Mm) = {u[0]:+.6f} m, "
          f"u(+1 Mm) = {u[-1]:+.6f} m")
    print(f"      against +-b/2 = +-{u_inf:.6f} m: reached to "
          f"{abs(u[-1])/u_inf*100:.4f}%")
    win = np.abs(x) <= 5.0 * depth
    off = u[win][-1] - u[win][0]
    print(f"  (b) offset over a +-5d window ({np.ptp(x[win])/1000:.0f} km): "
          f"{off:+.4f} m = {off/slip*100:.1f}% of b")
    i0 = np.argmin(np.abs(x))
    grad_num = (u[i0 + 1] - u[i0 - 1]) / (2.0 * (x[1] - x[0]))
    print(f"  (c) peak surface shear strain at the trace: numerical "
          f"{grad_num:.6e}, closed form")
    print(f"      b/(pi d) = {slip/(np.pi*depth):.6e}  (ratio "
          f"{grad_num/(slip/(np.pi*depth)):.6f})")
    print(f"  (d) u(d) = {strike_slip_profile(np.array([depth]), depth, slip)[0]:.6f} "
          f"m = {strike_slip_profile(np.array([depth]), depth, slip)[0]/slip*100:.1f}% of b")
    print(f"      so the locking depth is the distance at which one quarter of the")
    print(f"      far-field offset has accumulated: depth is measurable, not decorative")
    u2 = strike_slip_profile(x, depth, 2.0 * slip)
    print(f"  (e) linearity: doubling b multiplies the peak offset by "
          f"{np.max(np.abs(u2))/np.max(np.abs(u)):.6f}")
    print("\n  for a *buried* dislocation the surface trace is continuous: the offset")
    print("  accumulates over a zone of width ~d.  There is no surface rupture and no")
    print("  data gap at x = 0, which is what makes this the standard model for")
    print("  moderate strike-slip earthquakes.")

    section("2. A synthetic interferogram and its gradient budget")
    heading, inc = 8.0, 35.0
    unit = los_unit(heading, inc)
    print(f"  view: heading {heading:.0f} deg, incidence {inc:.0f} deg; LOS unit "
          f"vector (ground to satellite)")
    print(f"  in (east, north, up) = ({unit[0]:+.4f}, {unit[1]:+.4f}, {unit[2]:+.4f})")
    print(f"  the sensitivity to northward motion, |{unit[1]:.4f}|, is a factor")
    print(f"  {abs(unit[0]/unit[1]):.2f} below the eastward sensitivity: a")
    print("  strike-slip fault is the worst case for a polar-orbiting radar, and the")
    print("  inferred slip depends on the projection that is assumed.\n")
    for name, strike_dir in (("north-south", np.array([0.0, 1.0, 0.0])),
                             ("east-west", np.array([1.0, 0.0, 0.0]))):
        proj = unit @ strike_dir
        los_1d = proj * u
        wrapped = (4.0 * np.pi * los_1d / LAM + np.pi) % (2.0 * np.pi) - np.pi
        peak = np.abs(los_1d).max()
        res_m = x[1] - x[0]
        dmax = np.abs(np.diff(los_1d)).max()
        print(f"  {name} fault: projection coefficient {proj:+.4f}")
        print(f"    peak LOS displacement {peak*100:.4f} cm = "
              f"{peak*2/(LAM/2.0):.3f} fringes "
              f"(one fringe = {LAM/2*100:.4f} cm)")
        print(f"    largest LOS change per {res_m:.0f} m pixel: {dmax*1000:.4f} mm "
              f"against the lam/4 limit of {LAM/4*1000:.4f} mm -> "
              f"{'unwrappable' if dmax < LAM/4 else 'ALIASED'}")
    print("\n  the gradient budget is the right way to ask whether a fault is")
    print("  measurable: the peak strain is b/(pi d), so a shallower locking depth or")
    print("  a larger slip moves the fringes together until the per-pixel change")
    print(f"  exceeds lam/4 = {LAM/4*1000:.4f} mm and the near field aliases.  With")
    print(f"  b = {slip:.1f} m and d = {depth/1000:.1f} km the margin is comfortable;")
    print("  halve d and the per-pixel change doubles.")

    section("3. Ascending and descending: decomposing the look directions")
    print("  a single pass measures one projection; two passes with different")
    print("  headings give two equations in three unknowns, so the standard")
    print("  assumption is that the north-south component is negligible.\n")
    asc = los_unit(8.0, 35.0)
    desc = los_unit(188.0, 39.0)
    print("   component   ascending coefficient   descending coefficient")
    for k, nm in enumerate(("east", "north", "up")):
        print(f"   {nm:9s}   {asc[k]:21.4f}   {desc[k]:22.4f}")
    print("\n  the north coefficient is smaller than the east one by a factor:")
    print(f"    ascending: |{asc[0]:.3f}| / |{asc[1]:.3f}| = "
          f"{abs(asc[0]/asc[1]):.2f};  descending: {abs(desc[0]/desc[1]):.2f}")
    truth = np.array([0.020, 0.0, -0.030])      # 2 cm east, 3 cm subsidence
    obs = np.array([asc @ truth, desc @ truth])
    a_mat = np.array([[asc[0], asc[2]], [desc[0], desc[2]]])
    est = np.linalg.solve(a_mat, obs)
    print(f"\n  SYNTHETIC truth: east {truth[0]*100:+.2f} cm, up {truth[2]*100:+.2f} cm")
    print(f"  observed LOS: ascending {obs[0]*100:+.4f} cm, "
          f"descending {obs[1]*100:+.4f} cm")
    print(f"  recovered (assuming no N-S motion): east {est[0]*100:+.4f} cm, "
          f"up {est[1]*100:+.4f} cm")
    print(f"  errors: {abs(est[0]-truth[0])*1000:.4f} mm east, "
          f"{abs(est[1]-truth[2])*1000:.4f} mm up")
    biased = np.array([0.020, 0.010, -0.030])   # 1 cm of northward motion
    obs_b = np.array([asc @ biased, desc @ biased])
    est_b = np.linalg.solve(a_mat, obs_b)
    print(f"\n  now give the same ground 10 mm of northward motion as well:")
    print(f"  recovered (still assuming no N-S): east {est_b[0]*100:+.4f} cm, "
          f"up {est_b[1]*100:+.4f} cm")
    print(f"  the north component leaks entirely into the east estimate "
          f"({(est_b[0]-biased[0])*1000:+.2f} mm) and leaves the vertical")
    print(f"  estimate unchanged ({abs(est_b[1]-biased[2])*1000:.2f} mm error), because with both")
    print("  passes sharing the same angle to north the north term is proportional to")
    print("  the east term with the same ratio in both equations: the two are not")
    print("  separable, and the assumption decides which one absorbs the signal.")
    print("  For a mostly strike-slip earthquake this is the dominant error term.")

    section("4. A volcanic source: a Gaussian uplift and its volume")
    sigma = 2000.0      # m
    ampl = 0.060        # m
    r = np.linspace(-12000.0, 12000.0, 1201)
    up = ampl * np.exp(-(r ** 2) / (2.0 * sigma ** 2))
    volume = 2.0 * np.pi * sigma ** 2 * ampl
    print(f"  teaching source: vertical uplift {ampl*100:.1f} cm, Gaussian radius")
    print(f"  sigma = {sigma/1000:.1f} km")
    print(f"  its integral (the volume change of the teaching model) is")
    print(f"    dV = 2 pi sigma^2 * A = {volume/1e6:.4f} x 10^6 m^3 "
          f"= {volume/1e6:.4f} Mm^3")
    print(f"  that formula is exact for a Gaussian, so the volume needs no")
    print(f"  assumption about the source geometry - only the shape assumption.")
    d_los_v = np.cos(np.radians(35.0)) * up
    print(f"\n  on the line of sight at 35 deg the peak signal is "
          f"{d_los_v.max()*100:.3f} cm = "
          f"{d_los_v.max()*2/(LAM/2.0):.3f} fringes")
    for frac in (0.10, 0.25, 0.50):
        rr = sigma * np.sqrt(-2.0 * np.log(frac))
        print(f"    at {frac*100:3.0f}% of the peak, radius = {rr/1000:6.3f} km, "
              f"uplift {up[np.argmin(abs(r-rr))]*100:6.3f} cm")
    print("  the deformation falls off on the source scale; a satellite image with")
    print("  a 5 x 20 m pixel and a 100 km frame resolves this pattern easily, which")
    print("  is why volcanic deformation is the most photogenic InSAR target.")

    section("5. Subsidence: a linear trend with a seasonal term")
    t = np.linspace(0.0, 3.0, 40)
    rate = -14.0            # mm/yr (subsidence)
    seas = 6.0              # mm
    d = rate * t + seas * np.sin(2.0 * np.pi * (t - 0.4))
    fit2 = np.polyfit(t, d, 1)
    print(f"  SYNTHETIC truth: rate {rate:.1f} mm/yr, seasonal amplitude "
          f"{seas:.1f} mm")
    print(f"  a straight-line fit alone gives {fit2[0]:.4f} mm/yr "
          f"(bias {fit2[0]-rate:+.4f} mm/yr)")
    season = np.sin(2.0 * np.pi * t)
    cosay = np.cos(2.0 * np.pi * t)
    a_mat = np.column_stack([t, season, cosay, np.ones_like(t)])
    coef, *_ = np.linalg.lstsq(a_mat, d, rcond=None)
    amp = np.hypot(coef[1], coef[2])
    phase = np.arctan2(coef[2], coef[1])
    print(f"  a fit with rate, annual sine and cosine, and a constant gives")
    print(f"    rate {coef[0]:.6f} mm/yr (bias {coef[0]-rate:+.2e} mm/yr)")
    print(f"    seasonal amplitude {amp:.4f} mm, phase {phase:.4f} rad")
    print(f"  recovering the season requires enough samples per cycle: with")
    print(f"  {t.size} dates over {t[-1]:.1f} yr that is "
          f"{t.size/t[-1]:.1f} dates/yr, and the seasonal term is resolved.")
    print("  the subsidence signal itself ("
          f"{abs(rate)*t[-1]:.1f} mm over the record) is "
          f"{abs(rate)*t[-1]/(LAM/2*1000)*100:.1f}% of one fringe in total, so")
    print("  the discrimination is entirely in the time series, not in any single")
    print("  fringe: this is the case that motivates the network of lesson 03.")

    section("6. A landslide: the gradient budget")
    print("  a moving mass with a smooth velocity field and a sharp toe\n")
    res_m = 20.0
    limit_cm = LAM / 4.0 * 100.0
    print(f"  aliasing limit: |change of LOS displacement| < lam/4 = "
          f"{limit_cm:.4f} cm per pixel = "
          f"{limit_cm/100.0/res_m*1000:.4f} mm per metre of ground")
    print("\n   rate (mm/yr)   width (m)   gradient after 1 yr (mm/m)   "
          "unwrappable?")
    for rate_mm_yr, width_m in ((50.0, 200.0), (50.0, 100.0), (200.0, 100.0),
                                (500.0, 50.0)):
        grad = (rate_mm_yr * 1.0) / width_m     # mm/yr per m, for one year of motion
        wrap = grad * 1.0 / (limit_cm * 10.0 / res_m)
        print(f"   {rate_mm_yr:11.0f}   {width_m:9.0f}   {grad:26.4f}   "
              f"{'yes' if wrap < 1 else 'NO (aliased)'}")
    print("\n  (the comparison uses one year of accumulated motion against the")
    print("  per-pixel limit; the margin shrinks linearly with the time between")
    print("  acquisitions, which is why slow landslides need short revisit and fast")
    print("  ones need either a shorter revisit or a phase-unwrapping-independent")
    print("  method.  The classic remedy is a network of nearby pairs plus an")
    print("  external constraint at the toe.)")


if __name__ == "__main__":
    main()
