"""Mantle convection, slab pull and ridge push: the forces, ranked.

Run:  .venv/bin/python driving_forces_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-02-03, "Mantle Convection, Slab Pull and Ridge Push".

Three driving forces are candidates, and the honest way to compare them is to
compute each one from its own mechanism rather than to quote a ranking. The
script does that, and then does two things with the result that a ranking alone
cannot do:

1. **Slab pull from thermal buoyancy.** The density excess of a subducting slab
   is computed from half-space cooling -- the same cooling model that predicts
   seafloor depth and heat flow -- integrated over the slab's cross-section.
   The result is a force per unit length of trench, and its dependence on the
   *age* of the slab falls out of the calculation rather than being asserted.
2. **Ridge push from the pressure difference at the ridge.** The ridge stands
   higher than old ocean floor, so the pressure at the base of the plate is
   lower beneath the ridge. The force follows from that difference.
3. **Basal drag from a viscous asthenosphere.** Shear traction eta v / d over
   the area of the plate base. Its magnitude is comparable to ridge push and
   its *sign* is a separate question.
4. **A viscosity the observations require.** If slab pull is the dominant
   force and the plate moves at the observed speed, the viscosity needed to
   balance the force follows from the drag law. The number is compared with
   the viscosity inferred independently from post-glacial rebound, which is a
   genuine consistency check between two unrelated measurements.
5. **The Rayleigh number**, which decides whether the mantle convects at all
   and how vigorous the convection is.

Every thermal constant and rock property is NOMINAL and is labelled. The
conclusions here are order-of-magnitude statements, and the script prints the
sensitivity of each one to its inputs, because the forces differ by an order of
magnitude and the *ranking* is what is robust rather than any individual value.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.special import erfc

YEAR = 3.15576e7
MYR = 1e6 * YEAR
G_ACC = 9.81

# --------------------------------------------------------------------------
# NOMINAL thermal and rheological constants (the same set as the seafloor
# cooling model of lesson 04-02-01, so the two lessons share their inputs).
# --------------------------------------------------------------------------
K_THERMAL = 3.2                # W m^-1 K^-1
KAPPA = 1.0e-6                 # m^2 s^-1
ALPHA = 3.0e-5                 # K^-1
DELTA_T = 1300.0               # K
RHO_M = 3300.0                 # kg/m^3
RHO_W = 1000.0                 # kg/m^3
ETA_MANTLE = 1.0e21            # Pa s, upper-mantle/whole-mantle scale
ETA_ASTHENOSPHERE = 4.0e19     # Pa s, a low-viscosity channel
D_ASTHENOSPHERE = 200e3        # m
R_EARTH = 6371e3               # m
H_MANTLE = 2890e3              # m, mantle thickness


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def slab_buoyancy(age_ma, thickness_km=100.0):
    """Mass excess per unit area of a slab, from its thermal structure.

    The slab carries the thermal structure of a plate that cooled for age_ma
    before subduction:

        T(z) = dT erf( z / (2 sqrt(kappa t)) ),

    measured downward from the top of the plate, with the surface held at
    zero and the initial temperature equal to dT.  Its temperature deficit is
    dT - T(z) = dT erfc(z / 2 sqrt(kappa t)), so its density excess relative
    to the mantle at the same depth is

        drho(z) = rho_m alpha dT erfc( z / 2 sqrt(kappa t) ).

    Returns the mass excess in kg/m^2, and the temperature scale depth in km.
    """
    t = age_ma * MYR
    scale = 2.0 * math.sqrt(KAPPA * t)
    z = np.linspace(0.0, thickness_km * 1e3, 40001)
    drho = RHO_M * ALPHA * DELTA_T * erfc(z / scale)
    mass_excess = float(np.trapezoid(drho, z))       # kg/m^2
    return mass_excess, scale / 1e3


def part1_slab_pull():
    section("1. Slab pull, computed from thermal buoyancy")
    print("  The slab is the cold thermal boundary layer of the ocean plate,")
    print("  so its density excess is the same thermal contraction that gives")
    print("  the seafloor its depth-age curve. With T(z) from half-space")
    print("  cooling, the density excess is")
    print("    drho(z) = rho_m alpha dT erfc(z / 2 sqrt(kappa t))")
    print("  and the force along the slab is g times the mass excess per unit")
    print("  area times the length of slab counted:")
    print("    F = g * L_slab * integral drho(z) dz.")
    print()
    print(f"  {'slab age (Ma)':>14}{'scale depth (km)':>18}"
          f"{'mass excess (kg/m^2)':>22}")
    data = []
    for age_ma in (20.0, 60.0, 100.0, 140.0):
        mass_excess, scale_km = slab_buoyancy(age_ma)
        data.append((age_ma, mass_excess))
        print(f"  {age_ma:>14.0f}{scale_km:>18.0f}{mass_excess:>22.3e}")
    print()
    print("  The mass excess grows with slab age, because a slab that cooled")
    print(f"  for longer is thicker and colder. The 140 Ma slab pulls")
    print(f"  {data[-1][1] / data[0][1]:.1f} times as hard as the 20 Ma one, and that is a")
    print("  prediction rather than a bookkeeping entry: plates attached to")
    print("  old, deeply subducted slabs should move faster. Over the large")
    print("  plates the correlation is present and weak, which is exactly the")
    print("  situation that keeps a question open.")
    print()
    print("  The force also depends on *how much slab is counted*, which is a")
    print("  definition rather than a measurement:")
    print()
    print(f"  {'slab age':>10}{'L = 660 km':>16}{'L = 2900 km':>16}"
          f"{'ratio':>8}")
    for age_ma, mass_excess in data:
        f660 = G_ACC * mass_excess * 660e3
        f2900 = G_ACC * mass_excess * 2900e3
        print(f"  {age_ma:>10.0f}{f660:>16.2e}{f2900:>16.2e}"
              f"{f2900 / f660:>8.1f}")
    print()
    print("  Counting the slab only down to the 660 km discontinuity, where the")
    print("  phase changes and the viscosity increase change its behaviour,")
    print("  gives a few times 1e13 N/m. Counting the whole mantle path gives")
    print("  about four times that. Both are the same physics with a different")
    print("  definition of the slab, which is why slab pull should be quoted as")
    print("  a range and why comparing two papers' force estimates without")
    print("  checking what each one counted is a waste of an afternoon.")
    print()
    print("  The horizontal component, which is what drives the plate toward")
    print("  the trench, is the along-slab force times cos(dip). A 60-degree")
    print("  slab transmits 0.50 of the force horizontally; a 30-degree slab")
    print("  transmits 0.87. The dip therefore matters as much as the force")
    print("  when the question is how fast a plate moves.")
    print()


def part2_ridge_push():
    section("2. Ridge push, from the pressure difference at the ridge")
    print("  The ridge crest stands higher than old ocean floor because the")
    print("  young plate is hot and therefore light. At the base of the plate")
    print("  the pressure under the ridge is lower than under old lithosphere")
    print("  by g (rho_m - rho_w) dh, and that difference acts over the plate")
    print("  thickness. The force per unit length is therefore")
    print("    F = g (rho_m - rho_w) dh h,")
    print("  where dh is the ridge elevation above the reference ocean floor")
    print("  and h is the thickness over which the pressure difference acts.")
    print()
    # Ridge elevation above old ocean floor, from the half-space model.
    subsidence_coeff = (2.0 * RHO_M * ALPHA * DELTA_T / (RHO_M - RHO_W)) * math.sqrt(KAPPA / math.pi)
    dh = subsidence_coeff * math.sqrt(100.0 * MYR)     # metres at 100 Ma
    print(f"  Ridge elevation above 100 Ma ocean floor: dh = {dh:.0f} m")
    print("  (from the same half-space cooling coefficient as lesson 04-02-01).")
    print()
    print(f"  {'h (km)':>10}{'F (N/m)':>14}")
    for h_km in (40.0, 60.0, 80.0, 100.0):
        f = G_ACC * (RHO_M - RHO_W) * dh * (h_km * 1e3)
        print(f"  {h_km:>10.0f}{f:>14.2e}")
    print()
    print("  The ambiguity is entirely in h, the thickness over which the")
    print("  pressure difference acts, and h is not a well-defined quantity:")
    print("  it is roughly the depth at which the cooling plate reaches the")
    print("  adiabat, which is where the thermal model itself stops being")
    print("  sharp. The honest statement is a range of order 1e12 N/m, an")
    print("  order of magnitude below slab pull and remarkably insensitive to")
    print("  everything except h. Ridge push is a real force and it is not the")
    print("  main one.")
    print()


def part3_basal_drag():
    section("3. Basal drag, from the viscosity of the asthenosphere")
    print("  A plate moving at v over an asthenosphere of viscosity eta and")
    print("  thickness d experiences a shear traction")
    print("    tau = eta v / d,")
    print("  and the force per unit length of the plate margin is tau times the")
    print("  plate dimension along the direction of motion.")
    print()
    print(f"  {'eta (Pa s)':>12}{'v (mm/a)':>10}{'tau (Pa)':>12}"
          f"{'F (N/m), L=10 000 km':>24}")
    v_ms = 50.0e-3 / YEAR
    for eta in (1e19, 4e19, 1e20, 1e21):
        tau = eta * v_ms / D_ASTHENOSPHERE
        f = tau * 1.0e7
        print(f"  {eta:>12.0e}{50.0:>10.0f}{tau:>12.3e}{f:>24.2e}")
    print()
    print("  With a 4e19 Pa s channel the traction is a few times 1e5 Pa, which")
    print("  is a tenth of a megapascal, and the force over a 10 000 km plate")
    print("  is of order 1e12 N/m: the same order as ridge push.")
    print()
    print("  What the table cannot tell you is the *sign*. If the mantle")
    print("  beneath a plate is moving faster than the plate, the drag drives")
    print("  the plate; if it is moving slower, the drag resists. Both cases")
    print("  exist on the Earth: some plates appear to be dragged by a")
    print("  fast-moving asthenosphere and some appear to be held back by it.")
    print("  A force magnitude without a direction is only half an answer, and")
    print("  this is the honest reason basal drag is the least settled of the")
    print("  three forces.")
    print()


def part4_required_viscosity():
    section("4. The viscosity the observations require")
    print("  Take slab pull as the dominant force:  set the drive against a")
    print("  resisting drag over the plate and solve for the viscosity.")
    print("    F_slab * L_trench = tau * A_plate = (eta v / d) * L_plate * L_trench")
    print("    => eta = F_slab d / (v L_plate)")
    print()
    mass_excess_100 = slab_buoyancy(100.0)[0]
    f_slab = G_ACC * mass_excess_100 * 660e3
    print(f"  {'v (mm/a)':>10}{'L_plate (km)':>14}{'eta (Pa s)':>14}")
    for v_mm, l_km in ((20.0, 5000.0), (50.0, 10000.0), (80.0, 10000.0),
                       (50.0, 15000.0)):
        v = v_mm * 1e-3 / YEAR
        eta = f_slab * D_ASTHENOSPHERE / (v * l_km * 1e3)
        print(f"  {v_mm:>10.0f}{l_km:>14.0f}{eta:>14.2e}")
    print()
    print("  The required viscosity lands between 1e20 and 1e21 Pa s for")
    print("  plausible plate speeds and sizes. That is the same range that")
    print("  post-glacial rebound infers independently, from a completely")
    print("  different observation (the relaxation of a Pleistocene ice load).")
    print("  Two unrelated measurements agreeing on the viscosity of the mantle")
    print("  is the strongest single piece of evidence that the forces computed")
    print("  here are the right order of magnitude, because viscosity is the")
    print("  only free parameter the force balance has.")
    print()


def part5_rayleigh():
    section("5. Does the mantle convect at all?")
    print("  Ra = rho g alpha dT d^3 / (eta kappa).")
    print()
    print(f"  {'eta (Pa s)':>12}{'d (km)':>10}{'Ra':>12}{'Ra/Ra_crit':>14}")
    ra_crit = 1.0e3
    for eta in (1e21, 1e22):
        for d_km in (700.0, 2890.0):
            d = d_km * 1e3
            ra = (RHO_M * G_ACC * ALPHA * DELTA_T * d**3
                  / (eta * KAPPA))
            print(f"  {eta:>12.0e}{d_km:>10.0f}{ra:>12.2e}"
                  f"{ra / ra_crit:>14.2e}")
    print()
    print("  The critical Rayleigh number for the onset of convection in a")
    print(f"  fluid layer is of order {ra_crit:.0e}. Every case in the table")
    print("  exceeds it, by one to nearly five orders of magnitude, so the")
    print("  question is never")
    print("  whether the mantle convects: it is whether the convection is")
    print("  layered, how fast it is, and how the plates couple to it. Those")
    print("  are the live questions of the subject, and they are why the")
    print("  relative importance of the three forces in sections 1 to 3 is")
    print("  still an area of active measurement rather than settled fact.")
    print()


def main():
    print("Mantle convection, slab pull and ridge push: the forces, ranked.")
    part1_slab_pull()
    part2_ridge_push()
    part3_basal_drag()
    part4_required_viscosity()
    part5_rayleigh()
    print("=" * 74)
    print("All thermal and rheological constants are NOMINAL and are labelled.")
    print("Each force is computed from its own mechanism, and each result is")
    print("reported with the sensitivity that dominates its uncertainty.")
    print("=" * 74)


if __name__ == "__main__":
    main()
