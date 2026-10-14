#!/usr/bin/env python3
"""Abrupt climate change and tipping elements: a two-box ocean circulation with
freshwater forcing (showing a fold and hysteresis), and a zero-dimensional
energy-balance model with an ice-albedo threshold (showing multiple equilibria).

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python abrupt_climate_change_demo.py

All models and data in this file are SYNTHETIC.  The box model and the
energy-balance model are chosen teaching constructions; the tipping thresholds
computed here are properties of these models, not estimates of any real
threshold.  The standard constants used (solar constant, Stefan-Boltzmann
constant via a linear OLR fit) are stated in the code.

Contents
--------
1. Two-box circulation: time integration under a ramped freshwater forcing,
   forward and backward, and the resulting hysteresis loop.
2. The fold: the range of freshwater forcing with three steady solutions, and
   the two stable ones inside it.
3. Ice-albedo bistability in a zero-dimensional energy-balance model.
4. The sensitivity of the thresholds to the closure: structural uncertainty.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC two-box parameters -------------------------------------------
GAMMA_T = 1.0           # temperature relaxation rate, per unit time (fast)
T_POLAR_STAR = 5.0      # reference polar temperature, degC
T_EQUATOR_STAR = 25.0   # reference equatorial temperature, degC
DT_REF = 20.0           # temperature scale, K
DS_REF = 2.0            # salinity scale, psu
DT = 0.02               # time step
SPINUP_TIME = 200.0     # time units at each forcing value
H_FORWARD = np.linspace(0.0, 1.2, 49)
H_BACKWARD = H_FORWARD[::-1]

# --- SYNTHETIC energy-balance parameters ------------------------------------
SOLAR_CONSTANT_W_M2 = 1361.0
OLR_A_W_M2 = 210.0
OLR_B_W_M2_K = 2.0
ALBEDO_WARM = 0.30
ALBEDO_COLD = 0.62
ICE_THRESHOLD_C = -10.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def circulation(t_polar, t_equator, s_polar, s_equator):
    """Dimensionless circulation index: positive means thermal dominance.

    The polar box is dense when it is cold (thermal term) and light when it is
    fresh (haline term); q is the difference of those two contributions.
    """
    return (t_equator - t_polar) / DT_REF - (s_equator - s_polar) / DS_REF


def step(state, freshwater):
    """One explicit Euler step of the two-box model.

    Temperature relaxes to its reference; salinity has no restoring term, so
    the salinity difference is set by the balance between salt transport by the
    circulation and the freshwater flux.  This is the classic Stommel closure.
    """
    t_polar, t_equator, s_polar, s_equator = state
    q_magnitude = abs(circulation(t_polar, t_equator, s_polar, s_equator))
    dt_polar = GAMMA_T * (T_POLAR_STAR - t_polar) \
        + q_magnitude * (t_equator - t_polar)
    dt_equator = GAMMA_T * (T_EQUATOR_STAR - t_equator) \
        + q_magnitude * (t_polar - t_equator)
    ds_polar = q_magnitude * (s_equator - s_polar) - freshwater
    ds_equator = q_magnitude * (s_polar - s_equator) + freshwater
    return np.array([t_polar + DT * dt_polar,
                     t_equator + DT * dt_equator,
                     s_polar + DT * ds_polar,
                     s_equator + DT * ds_equator])


def saturate(state, freshwater):
    for _ in range(int(SPINUP_TIME / DT)):
        state = step(state, freshwater)
    return state


def sweep(h_values, start_state):
    entries = []
    state = start_state
    for freshwater in h_values:
        state = saturate(state, freshwater)
        entries.append((freshwater, circulation(*state),
                        state[1] - state[0], state[3] - state[2]))
    return entries, state


def steady_state_branches(h_values):
    """Solve the steady-state relation q = G(|q|) for each freshwater forcing.

    With q the circulation index, the steady state satisfies
        dT = gamma_T*(T*_e - T*_p) / (gamma_T + 2|q|)
        dS = H / |q|
    and q = dT/DT_REF - dS/DS_REF.  Roots are found by scanning q and refining
    each sign change by bisection.  The salinity relation is singular at q = 0,
    so |q| < 0.02 is excluded from the scan.
    """
    def residual(q, freshwater):
        magnitude = abs(q)
        delta_t = GAMMA_T * (T_EQUATOR_STAR - T_POLAR_STAR) \
            / (GAMMA_T + 2.0 * magnitude)
        delta_s = freshwater / magnitude
        return q - (delta_t / DT_REF - delta_s / DS_REF)

    solutions = []
    for freshwater in h_values:
        grid = np.concatenate([
            -np.linspace(6.0, 0.02, 6000), np.linspace(0.02, 6.0, 6000)])
        values = np.array([residual(q, freshwater) for q in grid])
        roots = []
        for i in range(len(grid) - 1):
            if values[i] * values[i + 1] < 0:
                low, high = grid[i], grid[i + 1]
                for _ in range(80):
                    mid = 0.5 * (low + high)
                    if residual(low, freshwater) * residual(mid, freshwater) <= 0.0:
                        high = mid
                    else:
                        low = mid
                roots.append(round(0.5 * (low + high), 6))
        solutions.append((freshwater, sorted(set(roots))))
    return solutions


def main():
    section("1. Two-box circulation under a ramped freshwater forcing")
    start = np.array([T_POLAR_STAR, T_EQUATOR_STAR, 25.0, 25.0])
    forward, end_state = sweep(H_FORWARD, start)
    backward, _ = sweep(H_BACKWARD, end_state)
    backward_lookup = {round(entry[0], 6): entry for entry in backward}
    print(f"  temperature relaxation rate gamma_T = {GAMMA_T:.2f} per unit time")
    print(f"  circulation index q = (T_e - T_p)/{DT_REF:.0f} K - "
          f"(S_e - S_p)/{DS_REF:.0f} psu")
    print(f"  salinity has no restoring term: it is set by transport against the")
    print(f"  freshwater flux (the classic Stommel closure)")
    print(f"  freshwater forcing H ramped from {H_FORWARD[0]:.2f} to "
          f"{H_FORWARD[-1]:.2f} then back, in psu per unit time")
    print(f"  {'H':>7s} {'q forward':>11s} {'q backward':>11s} "
          f"{'dT (K)':>8s} {'dS (psu)':>9s}")
    for index, (hf, qf, dtf, dsf) in enumerate(forward):
        if index % 5 == 0:
            qb = backward_lookup[round(hf, 6)][1]
            print(f"  {hf:7.3f} {qf:11.4f} {qb:11.4f} {dtf:8.3f} {dsf:9.4f}")
    forward_q = np.array([entry[1] for entry in forward])
    backward_q = np.array([backward_lookup[round(entry[0], 6)][1]
                           for entry in forward])
    gap = forward_q - backward_q
    bistable = H_FORWARD[np.abs(gap) > 0.05]
    print(f"  largest forward-minus-backward difference in q = "
          f"{np.max(np.abs(gap)):.4f}")
    if len(bistable):
        print(f"  forcing range where the two branches differ (|dq| > 0.05): "
              f"{bistable.min():.3f} to {bistable.max():.3f}")
    print("  Over that range the state depends on the history of the forcing, not")
    print("  only on its current value: that is hysteresis. It is why the")
    print("  transition is abrupt and why returning the forcing to the value at")
    print("  which the circulation collapsed does not restore it.")

    section("2. The fold: multiple steady states")
    h_values = np.linspace(0.0, 0.9, 19)
    branches = steady_state_branches(h_values)
    multiple = [(h, roots) for h, roots in branches if len(roots) >= 3]
    print(f"  steady states of q = G(|q|) found by root finding on a grid")
    print(f"  {'H':>7s} {'number of solutions':>20s} {'solutions (q)':>34s}")
    for index, (h, roots) in enumerate(branches):
        if index % 3 == 0 or len(roots) >= 3:
            print(f"  {h:7.3f} {len(roots):20d} "
                  f"{', '.join(f'{r:+.4f}' for r in roots):>34s}")
    if multiple:
        h_lo = min(item[0] for item in multiple)
        h_hi = max(item[0] for item in multiple)
        print(f"  three steady states exist for H in about [{h_lo:.3f}, "
              f"{h_hi:.3f}]")
        h_mid, roots_mid = multiple[len(multiple) // 2]
        print(f"  at H = {h_mid:.3f} the solutions are q = "
              f"{', '.join(f'{r:+.4f}' for r in roots_mid)}")
        print("  The middle one is unstable; the outer two are the two climate")
        print("  states the system can occupy. Which one is found depends on the")
        print("  initial condition, so an abrupt transition is a property of the")
        print("  system, not of the forcing alone.")
    else:
        print("  no forcing value in this range produced three solutions; the")
        print("  fold is outside the sampled range for these parameters.")

    section("3. Ice-albedo bistability in a zero-dimensional EBM")
    q_values = np.linspace(200.0, 900.0, 1401)
    warm_branch = (q_values * (1.0 - ALBEDO_WARM) - OLR_A_W_M2) / OLR_B_W_M2_K
    cold_branch = (q_values * (1.0 - ALBEDO_COLD) - OLR_A_W_M2) / OLR_B_W_M2_K
    both = (warm_branch > ICE_THRESHOLD_C) & (cold_branch < ICE_THRESHOLD_C)
    q_lo = float(q_values[both].min())
    q_hi = float(q_values[both].max())
    q_earth = SOLAR_CONSTANT_W_M2 / 4.0
    print(f"  warm branch T = (Q*(1 - {ALBEDO_WARM:.2f}) - {OLR_A_W_M2:.0f})/"
          f"{OLR_B_W_M2_K:.0f}, valid while T > {ICE_THRESHOLD_C:.0f} degC")
    print(f"  cold branch T = (Q*(1 - {ALBEDO_COLD:.2f}) - {OLR_A_W_M2:.0f})/"
          f"{OLR_B_W_M2_K:.0f}, valid while T < {ICE_THRESHOLD_C:.0f} degC")
    print(f"  both branches self-consistent for Q in [{q_lo:.1f}, {q_hi:.1f}] "
          f"W/m^2")
    print(f"  present-day absorbed-flux equivalent Q = S/4 = {q_earth:.2f} W/m^2")
    print(f"  at that Q: warm branch T = "
          f"{(q_earth * (1 - ALBEDO_WARM) - OLR_A_W_M2) / OLR_B_W_M2_K:.2f} degC, "
          f"cold branch T = "
          f"{(q_earth * (1 - ALBEDO_COLD) - OLR_A_W_M2) / OLR_B_W_M2_K:.2f} degC")
    print("  Two stable temperatures exist for the same solar forcing, with an")
    print("  unstable intermediate solution between them: the classic snowball")
    print("  bistability. With these chosen parameters the present-day value sits")
    print("  inside the bistable range. That is a statement about the model, not")
    print("  about the Earth: it has no clouds, no ocean and no ice flow.")

    section("4. Thresholds depend on the closure (structural uncertainty)")
    print(f"  {'ice albedo':>11s} {'Q at warm-branch end':>21s} "
          f"{'Q at cold-branch end':>21s} {'width':>8s}")
    for albedo_cold in (0.50, 0.62, 0.72):
        warm = (q_values * (1.0 - ALBEDO_WARM) - OLR_A_W_M2) / OLR_B_W_M2_K
        cold = (q_values * (1.0 - albedo_cold) - OLR_A_W_M2) / OLR_B_W_M2_K
        mask = (warm > ICE_THRESHOLD_C) & (cold < ICE_THRESHOLD_C)
        lo = float(q_values[mask].min())
        hi = float(q_values[mask].max())
        print(f"  {albedo_cold:11.2f} {lo:21.1f} {hi:21.1f} {hi - lo:8.1f}")
    print("  Changing one closure parameter moves both ends of the bistable range.")
    print("  Tipping-point estimates from simple models are conditional on closures")
    print("  of exactly this kind, which is why they are reported as ranges under")
    print("  stated assumptions rather than as numbers.")


if __name__ == "__main__":
    main()
