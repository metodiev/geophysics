#!/usr/bin/env python3
"""Graduate project 6: receiver functions and H-K stacking - the trade-off
between crustal thickness and Vp/Vs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python receiver_function_demo.py

Everything here is SYNTHETIC.  The receiver function is constructed as a sum of
Gaussians at the exact ray-theoretical arrival times; no seismogram, no station
and no published H-k result is used.

Sections
--------
1. The crustal model and the three Moho phases.
2. A synthetic receiver function.
3. H-K stacking, and the recovered model.
4. The trade-off: why one phase is not enough.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_TRUE = 35.0            # crustal thickness, km
VP_TRUE = 6.30           # crustal P velocity, km/s
K_TRUE = 1.75            # Vp/Vs
P_RAY = 0.06             # ray parameter, s/km
T_MAX = 30.0             # RF time window, s
DT = 0.05                # s
GAUSS_WIDTH = 0.5        # s
WEIGHTS = (0.5, 0.3, 0.2)   # H-K weights for Ps, PpPs, PpSs+PsPs
H_GRID = np.arange(20.0, 60.0 + 0.25, 0.25)
K_GRID = np.arange(1.60, 2.00 + 0.005, 0.005)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def sq(x):
    return np.sqrt(x)


def phase_times(h, vp, k, p):
    vs = vp / k
    eta_p = sq(vp ** -2 - p ** 2)
    eta_s = sq(vs ** -2 - p ** 2)
    t_ps = h * (eta_s - eta_p)
    t_ppps = h * (eta_s + eta_p)
    t_ppss = 2.0 * h * eta_s
    return t_ps, t_ppps, t_ppss


def rf_amplitudes(t, times, amps=(1.0, 0.5, 0.35)):
    out = np.zeros_like(t)
    for tt, a in zip(times, amps):
        out += a * np.exp(-((t - tt) / GAUSS_WIDTH) ** 2)
    return out


def hk_stack(t, rf):
    stack = np.zeros((H_GRID.size, K_GRID.size))
    for i, h in enumerate(H_GRID):
        for j, k in enumerate(K_GRID):
            times = phase_times(h, VP_TRUE, k, P_RAY)
            val = 0.0
            for w, tt in zip(WEIGHTS, times):
                val += w * float(np.interp(tt, t, rf))
            stack[i, j] = val
    return stack


def main():
    section("1. The crustal model and the Moho phases")
    vs_true = VP_TRUE / K_TRUE
    times = phase_times(H_TRUE, VP_TRUE, K_TRUE, P_RAY)
    print(f"SYNTHETIC crust: H = {H_TRUE:.1f} km, Vp = {VP_TRUE:.2f} km/s, "
          f"Vp/Vs = {K_TRUE:.2f} (Vs = {vs_true:.3f} km/s)")
    print(f"  ray parameter p = {P_RAY:.3f} s/km (a teleseismic P at about "
          f"55 deg)")
    print(f"{'phase':<14}{'expression':<26}{'time (s)':>10}")
    for name, expr, tt in (("Ps", "H(eta_s - eta_p)", times[0]),
                           ("PpPs", "H(eta_s + eta_p)", times[1]),
                           ("PpSs+PsPs", "2 H eta_s", times[2])):
        print(f"{name:<14}{expr:<26}{tt:>10.4f}")
    print(f"  the three phases have DIFFERENT dependencies on H and k, which is")
    print(f"  the entire basis of the H-K method.")

    section("2. A synthetic receiver function")
    t = np.arange(0.0, T_MAX, DT)
    rf = rf_amplitudes(t, times)
    rf += 0.02 * RNG.standard_normal(t.size)
    print(f"  window {T_MAX:.0f} s at {DT:.2f} s sampling "
          f"({t.size} samples); Gaussian half-width {GAUSS_WIDTH:.1f} s")
    print(f"  amplitudes 1.00 (Ps), +0.50 (PpPs), +0.35 (PpSs+PsPs) plus "
          f"2% noise")
    print(f"  (polarity convention: the PpPs phase is negated so that all three")
    print(f"   phases contribute positively to the H-K stack)")
    for label, tt in zip(("Ps", "PpPs", "PpSs+PsPs"), times):
        k = int(np.argmin(np.abs(t - tt)))
        print(f"  around {label:<11} (t = {tt:5.2f} s): "
              f"RF = {rf[k - 1:k + 2].round(3)}")

    section("3. H-K stacking")
    stack = hk_stack(t, rf)
    i, j = np.unravel_index(int(np.argmax(stack)), stack.shape)
    h_est, k_est = H_GRID[i], K_GRID[j]
    print(f"  grid: H {H_GRID[0]:.0f}-{H_GRID[-1]:.0f} km "
          f"({H_GRID.size} values), k {K_GRID[0]:.2f}-{K_GRID[-1]:.2f} "
          f"({K_GRID.size} values)")
    print(f"  peak of the weighted stack = {stack[i, j]:.3f}")
    print(f"  recovered H = {h_est:.2f} km (true {H_TRUE:.1f}, "
          f"error {h_est - H_TRUE:+.2f})")
    print(f"  recovered Vp/Vs = {k_est:.3f} (true {K_TRUE:.3f}, "
          f"error {k_est - K_TRUE:+.3f})")
    half = 0.5 * stack[i, j]
    inside = stack >= half
    h_span = H_GRID[np.any(inside, axis=1)]
    k_span = K_GRID[np.any(inside, axis=0)]
    print(f"  half-maximum region: H {h_span.min():.2f}-{h_span.max():.2f} km, "
          f"Vp/Vs {k_span.min():.3f}-{k_span.max():.3f}")

    section("4. The trade-off, phase by phase")
    print(f"  H-K stacks computed with one phase at a time (peak location):")
    print(f"{'phase':<16}{'H (km)':>10}{'Vp/Vs':>10}{'peak':>10}")
    for name, w in zip(("Ps only", "PpPs only", "PpSs+PsPs only"),
                       ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))):
        st = np.zeros_like(stack)
        for ii, h in enumerate(H_GRID):
            for jj, k in enumerate(K_GRID):
                tt = phase_times(h, VP_TRUE, k, P_RAY)
                st[ii, jj] = sum(ww * float(np.interp(tq, t, rf))
                                 for ww, tq in zip(w, tt))
        a, b = np.unravel_index(int(np.argmax(st)), st.shape)
        print(f"{name:<16}{H_GRID[a]:>10.2f}{K_GRID[b]:>10.3f}{st[a, b]:>10.3f}")
    print("  -> a single phase defines a valley in (H, k), not a point: the")
    print("     H-k trade-off is why all three phases are stacked, and why the")
    print("     result must be quoted as a region, not a pair of numbers.")
    print("  the assumed Vp enters every phase time directly, so an error in Vp")
    print("  maps one-for-one into an error in H and must be reported with it.")


if __name__ == "__main__":
    main()
