"""Landslides, slope stability and what geophysics adds.

Run:  .venv/bin/python landslides_demo.py
Requires: numpy.

Companion to lesson 04-07-03.

The stability arithmetic here is the standard infinite-slope and sliding-block
analysis, derived in the lesson; the geophysical part is the conversion of a
measured seismic velocity or permittivity into a water content and a stiffness,
which is what a geophysical survey contributes that a slope map cannot.

1. Infinite-slope factor of safety with pore pressure, and the pore-pressure
   ratio at failure.
2. The critical (Newmark) acceleration, derived exactly and against the
   small-slope approximation that is usually quoted.
3. The sliding-block displacement, integrated numerically and checked against
   the closed-form solution for a rectangular acceleration pulse.
4. Refraction for the depth of a failure surface, from the intercept time.
5. Water content from a GPR velocity, by inverting a stated mixing model.
6. The strain dependence of shear modulus and what it does to Vs.

All soil parameters are NOMINAL textbook ranges, labelled.  No landslide is
attributed a volume, a date or an acceleration record.
"""

import math

import numpy as np

G = 9.80665
GAMMA_W = 9810.0    # N/m^3, unit weight of water


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Infinite slope
# --------------------------------------------------------------------------

def fs_infinite(beta_deg, z, gamma, c_prime, phi_deg, u):
    """Factor of safety of an infinite slope with a slip plane at depth z.

    sigma_n = gamma z cos^2 beta,  tau = gamma z sin beta cos beta,
    FS = [c' + (sigma_n - u) tan phi'] / tau
    """
    b = math.radians(beta_deg)
    p = math.radians(phi_deg)
    sigma_n = gamma * z * math.cos(b) ** 2
    tau = gamma * z * math.sin(b) * math.cos(b)
    return (c_prime + (sigma_n - u) * math.tan(p)) / tau


def part1():
    section("1. Infinite slope: the factor of safety and the water table")
    gamma = 18000.0     # N/m^3, moist unit weight (NOMINAL, 16-20 kN/m^3)
    c_prime = 0.0       # Pa, cohesionless, so the derivation is transparent
    phi = 32.0          # degrees, NOMINAL clean sand
    z = 3.0             # m, slip-plane depth
    print(f"  gamma = {gamma/1000:.1f} kN/m^3, c' = {c_prime:.0f} Pa, "
          f"phi' = {phi:.0f} deg, z = {z:.1f} m  (NOMINAL)")
    print()
    print("  dry slope (u = 0):")
    print("     beta (deg)   FS      note")
    for beta in (10.0, 15.0, 20.0, 25.0, 30.0, 32.0, 35.0):
        f = fs_infinite(beta, z, gamma, c_prime, phi, 0.0)
        note = "dry, cohesionless FS = tan phi / tan beta" if abs(beta - 32.0) < 1e-9 else ""
        print(f"  {beta:10.1f}   {f:6.4f}   {note}")
    print()
    print(f"  At 32 deg with c' = 0 the dry FS is exactly tan(32)/tan(32) = 1.0000,")
    print(f"  the textbook statement that a dry cohesionless slope fails at")
    print(f"  beta = phi'.")
    print()
    print("  saturated slope: pore pressure ratio r_u = u / (gamma z)")
    print(f"  a water table at the ground surface gives r_u = gamma_w/gamma = "
          f"{GAMMA_W/gamma:.4f}")
    print()
    print(f"     beta (deg)   FS (r_u = {GAMMA_W/gamma:.4f})   r_u at FS = 1")
    for beta in (10.0, 15.0, 20.0, 25.0, 30.0):
        u_sat = (GAMMA_W / gamma) * gamma * z
        f_sat = fs_infinite(beta, z, gamma, c_prime, phi, u_sat)
        b = math.radians(beta)
        p = math.radians(phi)
        r_u_crit = math.cos(b) ** 2 * (1.0 - math.tan(b) / math.tan(p))
        print(f"  {beta:10.1f}   {f_sat:15.4f}   {r_u_crit:12.4f}")
    print()
    print("  r_u at failure for c' = 0 is cos^2(beta)(1 - tan beta / tan phi'),")
    print("  derived by setting FS = 1.  Compare each value with the fully")
    print("  saturated 0.5450: at 10 deg failure needs r_u = 0.696, more than")
    print("  saturation can supply, so that slope cannot fail by pore pressure")
    print("  alone; at 15 deg the required 0.533 is just below saturation, and")
    print("  at 20 deg it is far below.  The geophysical measurement that")
    print("  matters is therefore the water table and the water content, not the")
    print("  slope angle alone.")


# --------------------------------------------------------------------------
# 2. Critical acceleration
# --------------------------------------------------------------------------

def part2():
    section("2. Critical acceleration: exact and approximate")
    phi = 32.0
    p = math.radians(phi)
    print(f"  cohesionless infinite slope, phi' = {phi:.0f} deg")
    print()
    print("  With a horizontal pseudo-static coefficient k_h, the normal stress")
    print("  falls to W(cos b - k_h sin b) and the driving shear rises to")
    print("  W(sin b + k_h cos b).  Setting FS = 1 and using")
    print("  FS0 = tan phi / tan beta for the static slope gives")
    print("    k_h(exact) = tan b (FS0 - 1) / (1 + FS0 tan^2 b),")
    print("  against the usual small-slope approximation (FS0 - 1) tan b.")
    print()
    print("     beta (deg)   FS0     k_h exact   k_h approx   ratio")
    for beta in (5.0, 10.0, 15.0, 20.0, 25.0):
        b = math.radians(beta)
        fs0 = math.tan(p) / math.tan(b)
        k_exact = math.tan(b) * (fs0 - 1.0) / (1.0 + fs0 * math.tan(b) ** 2)
        k_approx = (fs0 - 1.0) * math.tan(b)
        print(f"  {beta:10.1f}   {fs0:6.3f}   {k_exact:10.4f}   {k_approx:10.4f}"
              f"   {k_exact/k_approx:8.4f}")
    print()
    print("  The approximation is high by 6 per cent at 5 deg, 23 per cent at")
    print("  20 deg and 29 per cent at 25 deg, because it drops the term")
    print("  FS0 tan^2 b in the denominator.  An over-estimate of the critical")
    print("  acceleration means an UNDER-estimate of the sliding displacement,")
    print("  which is the non-conservative direction for a hazard assessment.")


# --------------------------------------------------------------------------
# 3. Sliding-block displacement
# --------------------------------------------------------------------------

def newmark_displacement(dt, accel, a_c):
    """Integrate the sliding-block ODE: s'' = a(t) - a_c while sliding.

    Sliding starts when |a| first exceeds a_c and stops when the relative
    velocity returns to zero.  Returns total displacement.
    """
    v = 0.0
    s = 0.0
    sliding = False
    for a in accel:
        if not sliding and a > a_c:
            sliding = True
        if sliding:
            v_new = v + (a - a_c) * dt
            if v_new <= 0.0 and v > 0.0:
                sliding = False
                v = 0.0
                continue
            s += v * dt
            v = max(v_new, 0.0)
    return s


def part3():
    section("3. Sliding-block displacement: integrator versus closed form")
    dt = 1.0e-5
    a_c = 1.0
    print(f"  rectangular acceleration pulse, amplitude a = 2 m/s^2,")
    print(f"  critical acceleration a_c = {a_c:.1f} m/s^2")
    print()
    print("  closed form for a rectangular pulse of duration t0 and a > a_c:")
    print("     d = a t0^2 (a - a_c) / (2 a_c),")
    print("  which is the sum of the displacement during the pulse,")
    print("  (1/2)(a - a_c)t0^2, and the displacement while decelerating at a_c,")
    print("  (a - a_c)^2 t0^2 / (2 a_c).  The record below therefore includes")
    print("  4 t0 of zero acceleration after the pulse, so that the decelerating")
    print("  part is actually integrated.")
    print()
    print("    t0 (s)   numeric d (m)   closed form (m)   rel. diff")
    for t0 in (0.1, 0.2, 0.5, 1.0):
        n = int(round(t0 / dt))
        accel = np.concatenate([np.full(n, 2.0), np.zeros(4 * n)])
        num = newmark_displacement(dt, accel, a_c)
        closed = 2.0 * t0 ** 2 * (2.0 - a_c) / (2.0 * a_c)
        print(f"  {t0:8.2f}   {num:14.6f}   {closed:15.6f}   "
              f"{abs(num-closed)/closed:.2e}")
    print()
    print("  The displacement is quadratic in both pulse duration and the")
    print("  excess acceleration, which is why a factor of two in a_c is worth")
    print("  much more than a factor of two in the ground motion: it enters")
    print("  twice, inside a quadratic.")


# --------------------------------------------------------------------------
# 4. Refraction depth
# --------------------------------------------------------------------------

def part4():
    section("4. Seismic refraction: depth to the failure surface")
    print("Two-layer refraction, critical refraction at the interface:")
    print("  t_i = 2 z sqrt(v2^2 - v1^2) / (v1 v2)")
    print("  z   = t_i v1 v2 / (2 sqrt(v2^2 - v1^2))")
    print()
    v1 = 600.0     # m/s, NOMINAL dry soil
    print(f"  v1 = {v1:.0f} m/s, tabulated against t_i:")
    print()
    print("     v2 (m/s)   t_i (ms)   z (m)")
    for v2 in (1800.0, 2200.0, 3000.0):
        for ti_ms in (10.0, 12.5, 15.0):
            ti = ti_ms / 1000.0
            z = ti * v1 * v2 / (2.0 * math.sqrt(v2 ** 2 - v1 ** 2))
            print(f"  {v2:10.0f}   {ti_ms:9.1f}   {z:6.3f}")
    print()
    print("  A 12.5 ms intercept on a 600/2200 m/s section puts the refractor at")
    ti = 0.0125
    z = ti * v1 * 2200.0 / (2.0 * math.sqrt(2200.0 ** 2 - v1 ** 2))
    print(f"  z = {z:.3f} m.  The intercept depends on BOTH velocities, and the")
    print("  depth is proportional to the intercept: a 10 per cent velocity")
    print("  error moves the depth by roughly the same fraction.")
    print()
    print("  What the survey cannot see: a velocity contrast is not a strength,")
    print("  and a clay layer that is weaker than the surrounding soil may have")
    print("  a LOWER velocity, in which case it is a hidden layer and the")
    print("  refractor picked is the top of the stronger material beneath it.")


# --------------------------------------------------------------------------
# 5. Water content from a GPR velocity
# --------------------------------------------------------------------------

EPS_W = 80.4      # pure water at ~20 C, tabulated
EPS_S = 5.0       # soil mineral grains, NOMINAL (4-7)
EPS_A = 1.0       # air


def crim_epsilon(theta, phi):
    """Complex Refractive Index Model: sqrt(eps) mixed linearly by volume."""
    return (theta * math.sqrt(EPS_W) + (1.0 - phi) * math.sqrt(EPS_S)
            + (phi - theta) * math.sqrt(EPS_A)) ** 2


def part5():
    section("5. Water content from a GPR velocity")
    c = 299792458.0
    phi = 0.35
    print("The CRIM mixing model is an ASSUMED volumetric model, not a law:")
    print("  sqrt(eps) = theta sqrt(eps_w) + (1-phi) sqrt(eps_s) + (phi-theta)")
    print("It is used here only to show how strongly the velocity depends on")
    print("water content, and therefore why a velocity is a moisture measurement.")
    print()
    print(f"  porosity phi = {phi:.2f}, eps_w = {EPS_W:.1f} (tabulated), "
          f"eps_s = {EPS_S:.1f}, eps_a = 1.0")
    print()
    print("     theta    eps_r    v (m/ns)   v (cm/ns)")
    for theta in (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35):
        eps = crim_epsilon(theta, phi)
        v = c / math.sqrt(eps)
        print(f"  {theta:8.2f}   {eps:7.3f}   {v/1e9:9.4f}   {v/1e7:9.4f}")
    print()
    v_dry = c / math.sqrt(crim_epsilon(0.05, phi))
    v_wet = c / math.sqrt(crim_epsilon(0.30, phi))
    print(f"  from theta = 0.05 to 0.30 the velocity falls from {v_dry/1e9:.4f} to")
    print(f"  {v_wet/1e9:.4f} m/ns, a factor of {v_dry/v_wet:.3f}.")
    dtheta = 0.25 / ((v_dry - v_wet) / 1e9)
    print(f"  Inverting the model, dtheta/dv = {dtheta:.4f} per m/ns, so a")
    print(f"  velocity measured to 0.001 m/ns constrains the water content to")
    print(f"  about {dtheta*1e-3:.4f} of volumetric water content — but only if")
    print("  CRIM is the right model for the soil and the porosity is known.")
    print()
    print("  The relations that are actually used in the field (Topp and its")
    print("  successors) are empirical fits to this inverse problem, with stated")
    print("  soil-type ranges, and they assume the model form is right.")


# --------------------------------------------------------------------------
# 6. Strain-dependent modulus
# --------------------------------------------------------------------------

def part6():
    section("6. Shear modulus degradation, and how little Vs notices")
    gamma_r = 1.0e-4    # reference strain, NOMINAL
    print(f"  assumed hyperbolic model G/Gmax = 1/(1 + gamma/gamma_r),")
    print(f"  gamma_r = {gamma_r:.1e} (a measured fitting parameter)")
    print()
    print("     gamma      G/Gmax    Vs/Vs_max   f0/f0_max")
    for gamma in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
        g = 1.0 / (1.0 + gamma / gamma_r)
        vs = math.sqrt(g)
        print(f"  {gamma:9.1e}   {g:7.4f}   {vs:10.4f}   {vs:10.4f}")
    print()
    print("  A 50 per cent loss of shear modulus is a 29 per cent loss of Vs and")
    print("  a 29 per cent loss of the site's fundamental frequency, because")
    print("  Vs = sqrt(G/rho) and f0 = Vs/(4H).  Vs is the quantity a seismic")
    print("  survey measures, and it is the square root of the quantity the")
    print("  slope-stability calculation wants.  That square root is why the")
    print("  velocity change during a wet season is smaller than the stiffness")
    print("  change, and why Vs alone is a weak constraint on stability.")


def main():
    print("Landslides and slope stability -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    print()
    print("=" * 72)
    print("No landslide volume, date, location or acceleration record appears")
    print("in this script.  All soil parameters are NOMINAL ranges.")
    print("=" * 72)


if __name__ == "__main__":
    main()
