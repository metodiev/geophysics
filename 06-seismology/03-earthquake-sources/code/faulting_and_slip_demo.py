"""Faulting, slip and the elastic rebound cycle: what can be computed.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python faulting_and_slip_demo.py
Requires: numpy.

Companion to lesson 06-03-01.

Five computed quantities, all from a single block-slider fault model:

1. Stress accumulation at a plate rate on a fault of finite brittle width,
   and the recurrence interval it implies.  The measured interval is compared
   with the analytic expression, and the agreement is reported.
2. The slip deficit accumulated between events, and the check that the slip
   released in an event equals the plate rate times the interval.
3. The seismic moment of the event and the moment *rate* of the fault.  The
   moment rate computed two ways -- from the long-term fault parameters and
   from the event moment divided by the interval -- must agree.
4. The static stress drop, and how the ratio of stress drop to the ambient
   stress difference controls whether the fault is nearly periodic or not.
5. Coulomb failure: how a pore-pressure change moves a fault towards or away
   from failure, in the effective-stress formulation.

Every scenario parameter is SYNTHETIC and stated.  No real earthquake, slip
rate, stress drop or recurrence interval is quoted.
"""

import numpy as np

MU = 3.0e10          # Pa, shear modulus, NOMINAL for crustal rock
V_PLATE = 35.0e-3    # m/a, NOMINAL relative plate rate (35 mm/a)
W_BRITTLE = 12.0e3   # m, NOMINAL seismogenic thickness
A_FAULT = 40.0e3 * 12.0e3   # m^2, rupture area: 40 km along strike x 12 km wide
DTAU = 3.0e6         # Pa, SYNTHETIC static stress drop (3 MPa)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. The loading cycle: numeric integration against a closed form
# --------------------------------------------------------------------------

def part1_recurrence():
    section("1. Stress accumulation and the recurrence interval")
    YEAR = 365.25 * 24 * 3600.0
    tau_dot = MU * V_PLATE / W_BRITTLE          # Pa/a
    interval_analytic = DTAU / tau_dot          # a
    print("  SYNTHETIC fault model")
    print(f"    shear modulus mu            = {MU:.3e} Pa")
    print(f"    relative plate rate V       = {V_PLATE*1e3:.1f} mm/a"
          f" = {V_PLATE:.3e} m/a")
    print(f"    brittle (seismogenic) width = {W_BRITTLE/1e3:.1f} km")
    print(f"    area A = 40 km x 12 km      = {A_FAULT:.3e} m^2")
    print(f"    static stress drop dtau     = {DTAU/1e6:.1f} MPa (SYNTHETIC)")
    print()
    print(f"  loading rate dtau/dt = mu V / W = {tau_dot:.4e} Pa/a"
          f" = {tau_dot/YEAR:.4e} Pa/s")
    print(f"  analytic interval dtau / (dtau/dt) = {interval_analytic:.2f} a")

    # Numeric integration: accumulate stress, drop it when it reaches DTAU.
    dt = 0.01 * interval_analytic
    tau = 0.0
    t = 0.0
    events = []
    for step in range(2_000_000):
        tau += tau_dot * dt
        t += dt
        if tau >= DTAU:
            events.append(t)
            tau -= DTAU
        if len(events) == 3:
            break
    intervals = np.diff([0.0] + events)
    measured = float(np.mean(intervals))
    print(f"  numeric integration ({step+1} steps, dt = {dt:.3e} a):")
    print(f"    event times (a)          = {', '.join(f'{e:.2f}' for e in events)}")
    print(f"    measured mean interval   = {measured:.2f} a")
    print(f"    relative difference from the closed form = "
          f"{abs(measured-interval_analytic)/interval_analytic:.2e}")
    return interval_analytic


# --------------------------------------------------------------------------
# 2. Slip deficit and slip per event
# --------------------------------------------------------------------------

def part2_slip(interval):
    section("2. Slip deficit and coseismic slip")
    slip_deficit = V_PLATE * interval
    slip_from_drop = DTAU * W_BRITTLE / MU
    print(f"  slip deficit accumulated in one interval, V * T = {slip_deficit:.3f} m")
    print(f"  slip released if dtau = mu D / W:  D = dtau W / mu = "
          f"{slip_from_drop:.3f} m")
    print(f"  relative difference = "
          f"{abs(slip_deficit-slip_from_drop)/slip_deficit:.2e}")
    print()
    print("  The two expressions are the same statement: a stress drop dtau on a")
    print("  fault of width W corresponds to a slip D = dtau W / mu, and the slip")
    print("  that accumulates between events is V * T.  Their equality is what")
    print("  fixes T once dtau, W, mu and V are chosen.")
    return slip_deficit


# --------------------------------------------------------------------------
# 3. Seismic moment and moment rate
# --------------------------------------------------------------------------

def part3_moment(interval, slip):
    section("3. Seismic moment and moment rate")
    m0 = MU * A_FAULT * slip
    m0_rate_fault = MU * A_FAULT * V_PLATE
    m0_rate_events = m0 / interval
    print(f"  M0 = mu A D = {MU:.3e} x {A_FAULT:.3e} x {slip:.3f} = {m0:.4e} N m")
    print(f"  moment rate from fault parameters, mu A V = {m0_rate_fault:.4e} N m/a")
    print(f"  moment rate from events, M0 / T          = {m0_rate_events:.4e} N m/a")
    print(f"  relative difference = "
          f"{abs(m0_rate_events-m0_rate_fault)/m0_rate_fault:.2e}")
    print()
    print("  The long-term moment rate is fixed by A and V, not by how the slip is")
    print("  parcelled out.  Many small events and one large event release the same")
    print("  moment per unit time; they differ in how the moment is distributed in")
    print("  magnitude, which is the content of 06-11.")
    return m0


# --------------------------------------------------------------------------
# 4. Stress drop versus ambient stress difference
# --------------------------------------------------------------------------

def part4_stress_drop():
    section("4. Stress drop against the ambient stress difference")
    depth_km = 10.0
    rho = 2700.0
    g = 9.80665
    sigma_v = rho * g * depth_km * 1e3
    print(f"  at {depth_km:.0f} km, lithostatic vertical stress rho g z = "
          f"{sigma_v/1e6:.1f} MPa  (rho = {rho:.0f} kg/m^3, NOMINAL)")
    print(f"  SYNTHETIC stress drop dtau = {DTAU/1e6:.1f} MPa")
    print(f"  dtau / sigma_v = {DTAU/sigma_v:.4f}")
    print("  Order 1e-2: earthquake stress drops are a small fraction of the")
    print("  ambient stress, which is why one fault can host a long sequence of")
    print("  similar events with a nearly constant dtau -- the 'constant stress")
    print("  drop' observation, which is an empirical regularity, not a law.")
    print()
    print("  With dtau constant, D = dtau W / mu is constant, so the scaling")
    print("  M0 = mu A D is controlled by area ALONE.  That is the geometric")
    print("  statement behind self-similarity, quantified in lesson 06-03-06.")


# --------------------------------------------------------------------------
# 5. Coulomb failure and pore pressure
# --------------------------------------------------------------------------

def part5_coulomb():
    section("5. Coulomb failure under a pore-pressure change")
    print("  The Coulomb failure function is  CFF = tau - mu_s (sigma_n - p),")
    print("  equivalently  CFF = tau - mu_s sigma_n_eff.  A pore-pressure change")
    print("  dp changes CFF by  + mu_s dp.")
    mu_s = 0.6
    print(f"  friction coefficient mu_s = {mu_s:.2f}  (SYNTHETIC, laboratory range)")
    print()
    print("     dp (MPa)   dCFF (MPa)   dCFF/dtau = 1 MPa")
    for dp_mpa in (0.0, 0.5, 1.0, 2.0, 5.0):
        dcff = mu_s * dp_mpa
        print(f"   {dp_mpa:9.2f}   {dcff:10.3f}   {dcff/1.0:14.3f}")
    print()
    print("  A 1 MPa pore-pressure increase is worth 0.6 MPa of added shear stress.")
    print("  Reset: a stress drop of 3 MPa therefore needs only a 5 MPa pore")
    print(f"  pressure rise to be triggered, since {DTAU/1e6:.1f} / {mu_s:.2f} = "
          f"{DTAU/1e6/mu_s:.2f} MPa.")


def main():
    print("Faulting, slip and the elastic rebound cycle -- computed quantities")
    print(f"numpy {np.__version__}")
    interval = part1_recurrence()
    slip = part2_slip(interval)
    part3_moment(interval, slip)
    part4_stress_drop()
    part5_coulomb()
    print()
    print("=" * 72)
    print("Summary of the checks performed in this script:")
    print("  * measured recurrence interval vs dtau / (mu V / W): see part 1")
    print("  * slip from V * T vs slip from dtau W / mu:          see part 2")
    print("  * moment rate from fault parameters vs from events:  see part 3")
    print("  * dtau / rho g z as a dimensionless stress ratio:    see part 4")
    print("Every input is printed with its units and labelled SYNTHETIC or")
    print("NOMINAL.  No real event, catalogue or measured constant is quoted.")
    print("=" * 72)


if __name__ == "__main__":
    main()
