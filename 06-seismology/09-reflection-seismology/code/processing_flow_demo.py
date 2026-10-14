#!/usr/bin/env python3
"""The reflection processing flow: NMO, stack, and what stacking does to random
versus coherent noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python processing_flow_demo.py

SYNTHETIC throughout.  All velocities, offsets and noise levels are CHOSEN.

Contents
--------
1. Exact two-layer travel time versus the hyperbolic NMO approximation; error
   versus offset is measured.
2. An NMO-corrected and stacked CMP gather.
3. Random noise: measured stack improvement versus fold, against sqrt(N).
4. Coherent noise: a second event with the wrong moveout is NOT attenuated.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker_n(t, t0, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * (t - t0) ** 2) * np.exp(-a * (t - t0) ** 2)


# --- SYNTHETIC layered model over a half-space -------------------------------
# (thickness m, vp m/s)
MODEL = [(500.0, 2200.0), (700.0, 2800.0), (800.0, 3400.0)]
V_HALF = 4000.0


def exact_tt_offset(p):
    """Exact (x, t) for the reflection from the base of the layered stack.

    For horizontal layers, sin(theta_i) = p*v_i, and the downgoing plus upgoing
    path gives x = 2*sum(h tan theta) and t = 2*sum(h/(v cos theta)).
    """
    x = 0.0
    t = 0.0
    for h, v in MODEL:
        s = p * v
        if s >= 1.0:
            return None, None
        cos = np.sqrt(1.0 - s ** 2)
        x += 2.0 * h * (s / cos)
        t += 2.0 * h / (v * cos)
    return x, t


def main():
    section("1. Exact travel time versus the hyperbolic NMO approximation")
    # build exact t(x) by ray tracing and interpolating
    v_max = max(v for _, v in MODEL)
    ps = np.linspace(0.0, 0.95 / v_max, 600)
    xs, ts = [], []
    for p in ps:
        x, t = exact_tt_offset(p)
        if x is None:
            continue
        xs.append(x)
        ts.append(t)
    xs = np.array(xs)
    ts = np.array(ts)
    order = np.argsort(xs)
    xs, ts = xs[order], ts[order]

    # RMS velocity and t0 (two-way, normal incidence)
    dt_i = np.array([2.0 * h / v for h, v in MODEL])
    v_rms = np.sqrt(np.sum(dt_i * np.array([v for _, v in MODEL]) ** 2) / dt_i.sum())
    t0 = dt_i.sum()
    print(f"  model: {len(MODEL)} layers, half-space v = {V_HALF:.0f} m/s")
    print(f"  t0 (two-way) = {t0:.4f} s, v_rms = {v_rms:.1f} m/s")
    print("   offset (m)   exact t (s)   hyperbolic t (s)   error (ms)")
    hyper = np.sqrt(t0 ** 2 + xs ** 2 / v_rms ** 2)
    err = (hyper - ts) * 1e3
    for o in (0, 500, 1000, 2000, 3000, 4000):
        i = int(np.argmin(np.abs(xs - o)))
        print(f"   {xs[i]:10.0f}   {ts[i]:11.4f}   {hyper[i]:16.4f}   "
              f"{err[i]:+10.3f}")
    print(f"  maximum |error| over the spread = {np.max(np.abs(err)):.2f} ms")
    print("  The hyperbola with v_rms is excellent at small offset and drifts at")
    print("  long offset; the residual is the higher-order (anellipticity) term.")

    section("2-4. CMP gather, NMO, stack, and noise behaviour")
    dt = 0.002
    tt = np.arange(0.0, 3.0, dt)
    offsets = np.arange(0.0, 3000.0 + 1.0, 200.0)   # 16 traces (fold 16)
    f0 = 30.0
    v_stack = v_rms

    def gather(v_nmo, extra=None, noise=0.0):
        G = np.zeros((offsets.size, tt.size))
        for i, x in enumerate(offsets):
            tn = np.sqrt(t0 ** 2 + x ** 2 / v_nmo ** 2)
            G[i] += ricker_n(tt, tn, f0)
        if extra is not None:
            # a coherent event with a DIFFERENT moveout (a multiple-like event)
            v2, t02 = extra
            for i, x in enumerate(offsets):
                tn = np.sqrt(t02 ** 2 + x ** 2 / v2 ** 2)
                G[i] += 0.8 * ricker_n(tt, tn, f0)
        if noise:
            G += noise * RNG.standard_normal(G.shape)
        return G

    def nmo_stack(G, v_nmo):
        out = np.zeros_like(G)
        for i in range(G.shape[0]):
            x = offsets[i]
            for j, t in enumerate(tt):
                arg = t ** 2 - x ** 2 / v_nmo ** 2
                if arg <= 0:
                    continue
                tn = np.sqrt(arg)
                k = int(round(tn / dt))
                if 0 <= k < tt.size:
                    out[i, j] = G[i, k]
        return out.sum(axis=0) / G.shape[0]

    G = gather(v_stack)
    stack = nmo_stack(G, v_stack)
    print(f"  gather: {offsets.size} traces (fold {offsets.size}), "
          f"{tt.size} samples, dt = {dt * 1e3:.0f} ms")
    print(f"  stacked peak at t = {tt[np.argmax(stack)]:.3f} s "
          f"(expected {t0:.3f} s)")

    # (3) random noise versus fold
    print("\n  (3) random noise: stack improvement versus fold")
    noise = 0.30
    trials = 40
    win = np.abs(tt - t0) > 0.25          # excludes the (corrected) primary
    print("       fold   predicted sqrt(N)   measured noise reduction")
    for n in (4, 8, 16):
        ratios = []
        for _ in range(trials):
            Gn = gather(v_stack, noise=noise)
            s_all = nmo_stack(Gn[:n], v_stack)
            s_one = nmo_stack(Gn[:1], v_stack)
            r_one = np.sqrt(np.mean(s_one[win] ** 2))
            r_all = np.sqrt(np.mean(s_all[win] ** 2))
            ratios.append(r_one / r_all)
        print(f"       {n:4d}   {np.sqrt(n):16.2f}   {np.mean(ratios):20.2f}")
    print("  The metric is the noise rms outside the arrival window, single trace")
    print("  divided by N-fold stack.  It tracks sqrt(N): random noise averages")
    print("  down as the square root of the fold.")

    # (4) coherent noise
    print("\n  (4) coherent noise: a second event with a different moveout")
    extra = (v_stack * 0.72, 1.35)     # slower, later: a multiple-like event
    Gc = gather(v_stack, extra=extra)
    sc = nmo_stack(Gc, v_stack)
    s1 = nmo_stack(Gc[:1], v_stack)
    band = (tt > 1.30) & (tt < 1.45)
    prim_ratio = sc[(tt > 1.40) & (tt < 1.43)].max() / np.max(np.abs(sc[band]))
    one_ratio = s1[(tt > 1.40) & (tt < 1.43)].max() / np.max(np.abs(s1[band]))
    print(f"  primary / coherent-event amplitude, single trace : {one_ratio:.3f}")
    print(f"  primary / coherent-event amplitude, 16-fold stack: {prim_ratio:.3f}")
    print("  Stacking barely improves this ratio (no sqrt(N) gain): a coherent")
    print("  event with a different moveout does not average out.  Attenuating it")
    print("  needs a method that exploits its moveout (a Radon transform or SRME),")
    print("  not more stacking.")


if __name__ == "__main__":
    main()
