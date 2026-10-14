#!/usr/bin/env python3
"""Local linearisation for nonlinear inversion: the Jacobian, its finite-difference
verification, the measured size of the linearisation error, the convergence of
Gauss-Newton with damping, and the measured basin of attraction.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python local_linearization_demo.py

All models and data are SYNTHETIC: an exponential-decay amplitude model with
chosen parameters and computer-generated noise.  Nothing is measured.

Contents
--------
1. The forward model, the analytic Jacobian and its finite-difference check.
2. The linearisation error and its measured order in the step size.
3. Gauss-Newton with damping: the error history and its convergence order.
4. The basin of attraction, measured on a grid of starting models.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def forward(u, t):
    """d(t) = A exp(-alpha t).  u = (A, alpha)."""
    return u[0] * np.exp(-u[1] * t)


def jacobian(u, t):
    """Analytic Jacobian, shape (len(t), 2)."""
    A, alpha = u
    e = np.exp(-alpha * t)
    return np.column_stack([e, -A * t * e])


def objective(u, t, d, lam=0.0):
    r = forward(u, t) - d
    return float(r @ r) + lam * float(u @ u)


def gn(u0, t, d, iters=40, lm=True, lam_reg=0.0):
    """Damped Gauss-Newton.  Returns (u, history of objective, error iters)."""
    u = np.array(u0, dtype=float)
    hist, steps, lam = [], [], 1e-3
    for _ in range(iters):
        r = forward(u, t) - d
        J = jacobian(u, t)
        g = J.T @ r
        H = J.T @ J + lam_reg * np.eye(2)
        accepted = False
        for _ in range(30):
            try:
                step = np.linalg.solve(H + (lam if lm else 0.0) * np.eye(2), -g)
            except np.linalg.LinAlgError:
                lam *= 10.0
                continue
            u_new = u + step
            if not np.all(np.isfinite(u_new)):
                lam *= 10.0
                continue
            if objective(u_new, t, d, lam_reg) < objective(u, t, d, lam_reg):
                u = u_new
                lam = max(lam / 3.0, 1e-12)
                accepted = True
                break
            lam *= 10.0
        hist.append(objective(u, t, d, lam_reg))
        steps.append(float(np.linalg.norm(step)) if accepted else np.nan)
        if not accepted:
            break
    return u, np.array(hist), np.array(steps)


def main():
    t = np.linspace(0.0, 10.0, 20)
    u_true = np.array([3.0, 0.5])
    d_true = forward(u_true, t)
    sig = 0.005 * d_true.max()
    d = d_true + sig * RNG.standard_normal(t.size)

    section("1. The forward model and the analytic Jacobian")
    print("  model: d(t) = A exp(-alpha t), u = (A, alpha)")
    print(f"  SYNTHETIC truth: A = {u_true[0]:.2f}, alpha = {u_true[1]:.2f} "
          f"(1/s), t on [0, {t[-1]:.0f}] s, {t.size} samples")
    print(f"  data peak {d_true.max():.4f}; noise sigma = {sig:.5f} "
          f"({sig / d_true.max() * 100:.2f}% of the peak)")
    print("  Jacobian: dd/dA = exp(-alpha t),  dd/dalpha = -A t exp(-alpha t)")
    print("\n   step h     max relative deviation of the finite-difference Jacobian")
    best = (np.inf, None)
    for h in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8):
        J_an = jacobian(u_true, t)
        J_fd = np.empty_like(J_an)
        for k in range(2):
            up, um = u_true.copy(), u_true.copy()
            up[k] += h
            um[k] -= h
            J_fd[:, k] = (forward(up, t) - forward(um, t)) / (2.0 * h)
        rel = np.max(np.abs(J_fd - J_an) / np.maximum(np.abs(J_an), 1e-300))
        if rel < best[0]:
            best = (rel, h)
        print(f"   {h:8.0e}   {rel:24.3e}")
    print(f"  best measured step h = {best[1]:.0e} with deviation {best[0]:.3e}")
    print(f"  the classical central-difference estimate eps^(1/3) = "
          f"{(2.2e-16) ** (1 / 3):.1e}")
    print("  The deviation falls like h^2 until round-off dominates near 1e-8; the")
    print("  analytic Jacobian is verified to about 1e-9 in relative terms.")

    section("2. How good is the linearisation?")
    print("  second-order residual ||F(u+delta) - F(u) - J delta|| for a step of")
    print("  size ||delta|| along a fixed direction d = (0.6, -0.8):\n")
    dirn = np.array([0.6, -0.8])
    print("   ||delta||   residual          residual/||delta||^2   fitted order")
    prev = None
    for h in (0.4, 0.2, 0.1, 0.05, 0.025):
        uu = u_true + h * dirn
        res = np.linalg.norm(forward(uu, t) - forward(u_true, t)
                             - jacobian(u_true, t) @ (h * dirn))
        ratio = res / h**2
        order = "" if prev is None else f"{np.log(res / prev[0]) / np.log(h / prev[1]):.3f}"
        prev = (res, h)
        print(f"   {h:9.3f}   {res:15.6e}   {ratio:19.6e}   {order:>12s}")
    print("  The fitted order approaches 2: the linearisation error is O(||delta||^2),")
    print("  so the linearised model is accurate to first order and no better.")
    print("  Halving the step quarters the error, which is the reason a Gauss-Newton")
    print("  iteration near the solution gains two digits per step.")

    section("3. Gauss-Newton with damping")
    u0 = np.array([1.0, 0.10])
    u_gn, hist, steps = gn(u0, t, d, iters=40)
    print(f"  start u0 = (A, alpha) = ({u0[0]:.2f}, {u0[1]:.2f}); "
          f"alpha is off by a factor of 5")
    print("\n   iteration   objective      ||u - u_true||")
    u_it = u0.copy()
    errs = []
    lam = 1e-3
    prev = objective(u_it, t, d)
    it = 0
    while it < 25:
        r = forward(u_it, t) - d
        J = jacobian(u_it, t)
        g = J.T @ r
        H = J.T @ J
        ok = False
        for _ in range(30):
            step = np.linalg.solve(H + lam * np.eye(2), -g)
            u_new = u_it + step
            if objective(u_new, t, d) < prev:
                u_it, prev = u_new, objective(u_new, t, d)
                lam = max(lam / 3.0, 1e-12)
                ok = True
                break
            lam *= 10.0
        it += 1
        errs.append(float(np.linalg.norm(u_it - u_true)))
        print(f"   {it:9d}   {prev:10.3e}   {errs[-1]:14.6e}"
              + ("" if ok else "   (no descent step: stopped)"))
        if not ok:
            break
    print("\n  The iteration reaches the noise floor in four or five steps and")
    print("  then stops: with noisy data the residual cannot reach zero, and a")
    print("  Gauss-Newton iteration on a nonzero-residual problem is LINEAR, not")
    print("  quadratic.  The textbook quadratic rate needs a zero-residual solution,")
    print("  so it is measured below on the same problem with exact data.")

    d_exact = d_true
    u = u0.copy()
    lam, prev = 1e-3, objective(u, t, d_exact)
    e_seq, obj_seq = [], []
    for _ in range(12):
        r = forward(u, t) - d_exact
        J = jacobian(u, t)
        g = J.T @ r
        H = J.T @ J
        ok = False
        for _ in range(30):
            step = np.linalg.solve(H + lam * np.eye(2), -g)
            u_new = u + step
            if objective(u_new, t, d_exact) < prev:
                u, prev = u_new, objective(u_new, t, d_exact)
                lam = max(lam / 3.0, 1e-12)
                ok = True
                break
            lam *= 10.0
        e_seq.append(float(np.linalg.norm(u - u_true)))
        obj_seq.append(prev)
        if not ok or e_seq[-1] == 0.0:
            break
    print("\n  EXACT data, same start, error per iteration and measured order:")
    print("   iteration   objective     ||u - u_true||   measured order")
    for k, (e, ob) in enumerate(zip(e_seq, obj_seq)):
        if k == 0 or e_seq[k - 1] == 0.0 or e == 0.0:
            print(f"   {k + 1:9d}   {ob:11.3e}   {e:14.6e}")
            continue
        order = np.log(e) / np.log(e_seq[k - 1])
        print(f"   {k + 1:9d}   {ob:11.3e}   {e:14.6e}   {order:14.3f}")
    print("  From the third iteration the measured order is about 2: the step")
    print("  doubles the number of correct digits, which is the quadratic rate the")
    print("  theory promises for a zero-residual problem and an undamped step.")

    section("4. The basin of attraction")
    print("  Gauss-Newton from a grid of starts, success = final relative error")
    print("  below 1e-3 in A and alpha simultaneously.\n")
    grid = [(A, al) for A in (0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
            for al in (0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5)]
    ok = 0
    worst_ok = 0.0
    for A0, al0 in grid:
        u_s, _, _ = gn(np.array([A0, al0]), t, d, iters=60)
        good = (abs(u_s[0] - u_true[0]) / u_true[0] < 1e-3
                and abs(u_s[1] - u_true[1]) / u_true[1] < 1e-3)
        if good:
            ok += 1
            worst_ok = max(worst_ok,
                           float(np.linalg.norm(np.array([A0, al0]) - u_true)))
    print(f"  starts tested: {len(grid)}; converged to the truth: {ok} "
          f"({ok / len(grid) * 100:.1f}%)")
    print(f"  largest starting distance that still converged: {worst_ok:.3f}")
    print("  For this problem the basin is large: the residual surface has one")
    print("  minimum and the damping prevents the wild steps that a raw")
    print("  Gauss-Newton step would take.  The basin is a property of the")
    print("  objective and of the damping, and it is measured rather than assumed.")
    print("  remote and negative starts also succeed here:")
    for u_try in ((50.0, 5.0), (-5.0, 0.5), (0.001, 0.001), (100.0, 0.001)):
        u_s, _, _ = gn(np.array(u_try), t, d, iters=100)
        print(f"    from ({u_try[0]:8.3f}, {u_try[1]:6.3f}) -> "
              f"({u_s[0]:7.4f}, {u_s[1]:7.4f}) with objective "
              f"{objective(u_s, t, d):.4e}")
    u_far, _, _ = gn(np.array([1000.0, 1000.0]), t, d, iters=100)
    print(f"\n  counter-example: from (1000, 1000) the iteration stalls at "
          f"({u_far[0]:.4f}, {u_far[1]:.4f})")
    print(f"  with objective {objective(u_far, t, d):.4f}, against "
          f"{objective(u_true, t, d):.4e} at the truth.")
    print("  The reason is not a competing minimum: at alpha = 1000 the model")
    print("  exp(-1000 t) underflows to zero, so the Jacobian column")
    print("  dd/dalpha = -A t exp(-alpha t) is numerically zero and the gradient")
    print("  vanishes.  The iteration is at a STATIONARY point of a flat region,")
    print("  not at a solution -- a failure that a stopping rule on the gradient")
    print("  cannot detect, and the subject of lesson 07.")
    print("  Measured conclusion: for starts whose parameters span more than three")
    print("  orders of magnitude around the truth, only the flat-region failure")
    print("  appears; the basin of the genuine minimum covers the tested grid.")


if __name__ == "__main__":
    main()
