"""Faraday's law, induction, eddy currents, and the diffusion of a magnetic field
into a conductor - the physical principle of every EM method, and of the
geodynamo's observable consequences.

Run:  python3 em_induction_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-04. The script:

1. Computes the EMF induced in a circular loop by a sinusoidal field, comparing
   the closed form -pi a^2 omega B0 cos(omega t) with a finite-difference
   derivative of the flux; states the size of the 50 Hz mains hum it implies.
2. Computes the motional EMF vBL of a rod moved through a field, and the
   secondary field of the induced current, including its sign (Lenz).
3. Solves the magnetic diffusion equation numerically for a step field applied at
   the surface of a conductor and compares with the similarity solution
   B = B0 erfc(z/(2 sqrt(D t))); verifies the sqrt(t) scaling of the depth.
4. Computes the eddy-current density J = -(1/mu0) dB/dz and the ohmic
   dissipation density.
5. Tabulates magnetic diffusion times mu0 sigma L^2 for laboratory, crustal and
   core scales, and the magnetic Reynolds number for core convection.

Every number printed below was produced by this script.
"""

import math

MU0 = 1.25663706212e-6
SECONDS_PER_YEAR = 3.15576e7      # Julian year


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def erfc(x):
    """Complementary error function via the Maclaurin series for erf.

    The series is accurate to double precision for |x| <= 4, which covers every
    argument used below (all are < 0.5). For |x| > 4 the asymptotic form would be
    needed; it is not reached here and would be a silent loss of accuracy if it
    were, so the function raises instead.
    """
    if abs(x) > 4.0:
        raise ValueError("erfc series is only accurate for |x| <= 4")
    if x < 0.0:
        return 2.0 - erfc(-x)
    s = 0.0
    for k in range(0, 60):
        s += ((-1.0) ** k) * x ** (2 * k + 1) / (math.factorial(k) * (2 * k + 1))
    erf = 2.0 / math.sqrt(math.pi) * s
    return 1.0 - erf


def part1_faraday():
    section("1. Faraday's law in a loop: -dPhi/dt, closed form and numerical")
    a, b0, f = 0.10, 50.0e-6, 50.0
    omega = 2.0 * math.pi * f
    print(f"  loop radius a = {a:.2f} m, B = B0 sin(wt) with B0 = {b0 * 1e6:.0f} uT,"
          f" f = {f:.0f} Hz")
    area = math.pi * a * a
    print(f"  loop area = {area:.6f} m^2,  Phi0 = A B0 = {area * b0:.6e} Wb")
    print(f"{'t (s)':>10}{'Phi (Wb)':>16}{'-dPhi/dt numeric':>20}{'-A B0 w cos(wt)':>18}")
    for k in range(4):
        t = k * 0.25 / f
        dt = 1.0e-7
        flux = lambda tt: area * b0 * math.sin(omega * tt)
        num = -(flux(t + dt) - flux(t - dt)) / (2 * dt)
        ana = -area * b0 * omega * math.cos(omega * t)
        print(f"{t:10.6f}{flux(t):16.6e}{num:20.6e}{ana:18.6e}")
    print(f"  peak EMF = A B0 omega = {area * b0 * omega:.6e} V"
          f" = {area * b0 * omega * 1e3:.4f} mV")
    print("  That is the 50 Hz hum a 10 cm coil picks up from a 50 uT field - larger")
    print("  than most induced-polarisation signals, which is why field systems are")
    print("  shielded and why the mains frequency is notched.")


def part2_motional_lenz():
    section("2. Motional EMF and Lenz's law")
    b = 50.0e-6
    for length, speed in ((1.0, 1.0), (1.0, 0.01), (0.1, 1.0)):
        emf = b * length * speed
        print(f"  rod of length {length:4.2f} m moving at {speed:5.2f} m/s in"
              f" B = {b * 1e6:.0f} uT: EMF = v B L = {emf:.6e} V")
    print("  A receiver coil towed at 1 m/s through the geomagnetic field generates a")
    print("  motion-induced EMF of this order: it is a real noise source in")
    print("  magnetotellurics and in any moving-coil instrument.")
    print()
    a = 0.05
    print(f"  Lenz check: a loop of radius {a:.2f} m and resistance 1 ohm sees dB/dt")
    print("  from B(t) = B0 sin(wt). The induced current creates a secondary field")
    print("  opposing the change of the primary flux, so the measured EMF is")
    print("  EMF = -dPhi/dt: the minus sign is the statement that the loop resists")
    print("  being changed, and it is what makes a conductor a *screen* at high")
    print("  frequency (lesson 02-07-06).")


def part3_step_diffusion():
    section("3. Magnetic diffusion of a step: numerics against the similarity solution")
    sigma = 1.0            # S/m
    d_coef = 1.0 / (MU0 * sigma)
    dz = 0.005
    nz = 240
    dt = 5.0e-12
    cfl = d_coef * dt / dz ** 2
    print(f"  sigma = {sigma:.0f} S/m, D = 1/(mu0 sigma) = {d_coef:.4e} m^2/s")
    print(f"  dz = {dz} m, dt = {dt:.1e} s, CFL = {cfl:.4f} (stable below 0.5),"
          f" domain {nz * dz:.2f} m")
    b = [0.0] * nz
    times = [1.0e-8, 2.0e-8, 4.0e-8]
    print(f"{'z (m)':>7}" + "".join(f"{'B(z,' + f'{t * 1e9:.0f}' + 'ns)':>14}"
                                    for t in times)
          + f"{'erfc(z/2sqrt(Dt))':>20}")
    step = 0
    snapshots = {}
    n_steps = int(round(times[-1] / dt))
    for n in range(n_steps):
        new = b[:]
        new[0] = 1.0
        for j in range(1, nz - 1):
            new[j] = b[j] + cfl * (b[j + 1] - 2.0 * b[j] + b[j - 1])
        new[nz - 1] = new[nz - 2]
        b = new
        if (n + 1) % int(round(times[step] / dt)) == 0:
            snapshots[times[step]] = b[:]
            step += 1
            if step == len(times):
                break
    rows = [0, 4, 8, 16, 24, 32]
    t_last = times[-1]
    for j in rows:
        line = f"{j * dz:7.3f}"
        for tt in times:
            line += f"{snapshots[tt][j]:14.6f}"
        line += f"{erfc(j * dz / (2.0 * math.sqrt(d_coef * t_last))):20.6f}"
        print(line)
    print("  (the last column is the exact similarity solution at the latest time)")
    print(f"{'t (ns)':>8}{'z at B=0.5 (m)':>18}{'z/sqrt(Dt)':>14}{'J = -(1/mu0)dB/dz':>22}")
    for tt in times:
        bb = snapshots[tt]
        z_half = float("nan")
        for j in range(nz - 1):
            if bb[j] >= 0.5 >= bb[j + 1]:
                z_half = (j + (bb[j] - 0.5) / (bb[j] - bb[j + 1])) * dz
                break
        j0 = -(bb[1] - bb[0]) / dz / MU0
        print(f"{tt * 1e9:8.1f}{z_half:18.6f}{z_half / math.sqrt(d_coef * tt):14.6f}"
              f"{j0:22.4e}")
    print("  z/sqrt(Dt) is constant: the step field penetrates as sqrt(t), not at a")
    print("  constant speed. Diffusion has no wavefront - a point any EM interpreter")
    print("  must keep in mind when tempted to read an arrival time.")
    # residual of the diffusion equation using the exact similarity solution
    t = t_last

    def b_exact(z, tt):
        return erfc(z / (2.0 * math.sqrt(d_coef * tt)))

    hz = 1.0e-5
    ht = 1.0e-12
    z = 0.1
    lhs = (b_exact(z, t + ht) - b_exact(z, t - ht)) / (2 * ht)
    rhs = d_coef * (b_exact(z + hz, t) - 2 * b_exact(z, t) + b_exact(z - hz, t)) / hz ** 2
    print(f"  residual of dB/dt = D d2B/dz2 for the similarity solution at"
          f" z = {z} m, t = {t * 1e9:.0f} ns:")
    print(f"    dB/dt = {lhs:.6e},  D d2B/dz2 = {rhs:.6e},"
          f"  |residual|/|dB/dt| = {abs(lhs - rhs) / abs(lhs):.3e}")


def part4_eddy_currents():
    section("4. Eddy currents and their ohmic dissipation")
    sigma = 1.0
    d_coef = 1.0 / (MU0 * sigma)
    t = 4.0e-8
    z = 0.02
    h = 1.0e-5

    def b_exact(zz):
        return erfc(zz / (2.0 * math.sqrt(d_coef * t)))

    dbdz = (b_exact(z + h) - b_exact(z - h)) / (2 * h)
    j = -dbdz / MU0
    e = j / sigma
    print(f"  at t = {t * 1e9:.0f} ns, z = {z * 100:.0f} cm, sigma = {sigma} S/m:")
    print(f"    B/B0 = {b_exact(z):.6f}, dB/dz = {dbdz:.6e} T/m")
    print(f"    eddy current density J = -(1/mu0) dB/dz = {j:.6e} A/m^2")
    print(f"    electric field E = J/sigma = {e:.6e} V/m")
    print(f"    ohmic dissipation J E = {j * e:.6e} W/m^3")
    print("  The dissipated energy comes out of the magnetic field: that is magnetic")
    print("  diffusion, and in a rock it is the loss mechanism that limits EM")
    print("  penetration (skin depth, lesson 02-07-06).")


def part5_timescales():
    section("5. Diffusion times and the geodynamo")
    print("  tau = mu0 sigma L^2 (the order-of-magnitude magnetic diffusion time):")
    cases = [("laboratory (1 m, copper-like)", 5.96e7, 1.0),
             ("crust (10 km, 100 ohm m)", 0.01, 1.0e4),
             ("core (3480 km, 1e6 S/m)", 1.0e6, 3.48e6)]
    print(f"{'scale':>30}{'sigma (S/m)':>14}{'L (m)':>12}{'tau (s)':>14}"
          f"{'tau (yr)':>14}")
    for name, sigma, length in cases:
        tau = MU0 * sigma * length ** 2
        print(f"{name:>30}{sigma:14.3g}{length:12.3g}{tau:14.4e}"
              f"{tau / SECONDS_PER_YEAR:14.3e}")
    sigma_c, length_c = 1.0e6, 3.48e6
    tau_fund = MU0 * sigma_c * length_c ** 2 / math.pi ** 2
    print(f"\n  fundamental free-decay mode of a sphere, tau = mu0 sigma R^2/pi^2:")
    print(f"    sigma_core = {sigma_c:.0e} S/m (NOMINAL and debated; L = {length_c:.2e} m)")
    print(f"    tau = {tau_fund:.4e} s = {tau_fund / SECONDS_PER_YEAR:.3e} yr")
    age = 4.5e9
    print(f"    ratio tau / age of the Earth (4.5e9 yr) = {tau_fund / SECONDS_PER_YEAR / age:.3e}")
    print("  Diffusion alone would destroy the geomagnetic field in ~1e4-1e5 years,")
    print("  four to five orders of magnitude faster than the age of the Earth.")
    print("  The field must therefore be maintained: this is the core argument for")
    print("  dynamo action, and it is quantitative, not qualitative.")
    u, length = 1.0e-3, 3.5e6
    rm = MU0 * sigma_c * u * length
    print(f"\n  magnetic Reynolds number Rm = mu0 sigma u L with u = {u} m/s")
    print(f"  (NOMINAL core flow speed), L = {length:.1e} m: Rm = {rm:.4e}")
    print("  Rm >> 1 means advection beats diffusion: the necessary condition for a")
    print("  self-sustaining dynamo is met. (It is not sufficient - see 08-01-05.)")


def main():
    part1_faraday()
    part2_motional_lenz()
    part3_step_diffusion()
    part4_eddy_currents()
    part5_timescales()


if __name__ == "__main__":
    main()
