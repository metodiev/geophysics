#!/usr/bin/env python3
"""MT inversion: a 1-D Occam inversion of synthetic data, the trade-off between
misfit and model roughness, and the effect of a static shift.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_inversion_demo.py

Everything here is SYNTHETIC.  The layered model, the noise level and the
regularisation range are chosen teaching values, not field data.

Contents
--------
1. A synthetic layered model and its apparent resistivity and phase.
2. A 1-D Occam inversion: misfit versus roughness, and the recovered model.
3. Resolution: a thin layer is smeared, and its conductance is what survives.
4. A static shift applied to the data, and the model it produces.
5. Summary for the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KM = 1.0e3
PERIODS = np.logspace(-2, 3, 24)          # 0.01 to 1000 s
NOISE = 0.02                              # 2% noise on |Z| and on the phase


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mt_1d_Z(periods, rho, thick):
    out = np.zeros(periods.size, dtype=complex)
    for ip, T in enumerate(periods):
        omega = 2 * np.pi / T
        k = np.sqrt(1j * omega * MU0 / np.asarray(rho, float))
        eta = 1j * omega * MU0 / k
        Z = eta[-1]
        for i in range(len(rho) - 2, -1, -1):
            th = np.tanh(k[i] * thick[i])
            Z = eta[i] * (Z + eta[i] * th) / (eta[i] + Z * th)
        out[ip] = Z
    return out


def forward(periods, log_rho_layers, thickness):
    """Model parametrised as N log10 resistivities in equal-thickness layers."""
    rho = 10.0 ** log_rho_layers
    rho_full = list(rho) + [rho[-1]]
    return mt_1d_Z(periods, rho_full, list(thickness) + [0.0])


def data_vector(Z):
    return np.concatenate([np.log(np.abs(Z)), np.angle(Z)])


def occam(periods, thick, dobs, n_layers, roughness_weight=1.0, n_iter=60):
    """Occam inversion: minimise mean squared misfit + mu * model roughness.

    Gauss-Newton with a line search, and the model bounded in log10 rho.
    """
    LOG_LO, LOG_HI = np.log10(0.1), np.log10(1.0e6)
    D = np.zeros((n_layers - 1, n_layers))
    for i in range(n_layers - 1):
        D[i, i] = 1.0
        D[i, i + 1] = -1.0
    nd = dobs.size
    m = np.full(n_layers, np.log10(100.0))

    def objective(mv):
        pred = data_vector(forward(periods, mv, thick))
        return (np.mean((dobs - pred) ** 2)
                + roughness_weight * np.sum((D @ mv) ** 2))

    for _ in range(n_iter):
        pred = data_vector(forward(periods, m, thick))
        r = dobs - pred
        J = np.zeros((nd, n_layers))
        for j in range(n_layers):
            dm = np.zeros(n_layers)
            dm[j] = 1e-6
            J[:, j] = (data_vector(forward(periods, m + dm, thick)) - pred) / 1e-6
        A = np.vstack([J / np.sqrt(nd), np.sqrt(roughness_weight) * D])
        b = np.concatenate([r / np.sqrt(nd),
                            -np.sqrt(roughness_weight) * (D @ m)])
        step, *_ = np.linalg.lstsq(A, b, rcond=None)
        o0 = objective(m)
        alpha = 1.0
        accepted = False
        for _ in range(12):
            cand = np.clip(m + alpha * step, LOG_LO, LOG_HI)
            if objective(cand) < o0:
                m = cand
                accepted = True
                break
            alpha *= 0.5
        if not accepted:
            m = np.clip(m + 0.05 * step, LOG_LO, LOG_HI)
    Z = forward(periods, m, thick)
    misfit = np.sqrt(np.mean((dobs - data_vector(Z)) ** 2))
    rough = np.linalg.norm(D @ m)
    return m, Z, misfit, rough


def main():
    section("1. A synthetic layered model and its response")
    rho_true = np.array([200.0, 20.0, 400.0, 50.0])       # Ohm m
    thick_true = np.array([1.0, 2.0, 5.0]) * KM           # above the half-space
    print("SYNTHETIC model (Ohm m and km above the last entry, the half-space):")
    print("   200 for 1 km, 20 for 2 km, 400 for 5 km, then 50")
    Z_true = mt_1d_Z(PERIODS, list(rho_true), list(thick_true))
    rho_a = np.abs(Z_true) ** 2 / (2 * np.pi / PERIODS * MU0)
    phase = np.degrees(np.angle(Z_true))
    print("   period (s)   rho_a (Ohm m)   phase (deg)")
    for i in range(0, PERIODS.size, 4):
        print(f"   {PERIODS[i]:10.4f}   {rho_a[i]:13.3f}   {phase[i]:11.3f}")
    dobs = data_vector(Z_true)
    sigma = NOISE * np.std(dobs)
    dobs = dobs + sigma * RNG.standard_normal(dobs.size)
    print(f"data: {PERIODS.size} periods, log-amplitude and phase, each datum has")
    print(f"Gaussian noise of sigma = {sigma:.5f} = {NOISE * 100:.0f}% of the spread")
    print(f"the thin 20 Ohm m layer occupies 2 km out of 8 km: the question is whether")
    print("the data can resolve it as a layer or only as a conductance")

    section("2. A 1-D Occam inversion")
    n_layers = 14
    thick_inv = np.full(n_layers, 0.8 * KM)
    print("   mu        rms misfit   model roughness   conductance of the layer (S)")
    results = []
    for mu in (1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0):
        m, Z, mis, rough = occam(PERIODS, thick_inv, dobs, n_layers, mu)
        rho_model = 10.0 ** m
        seg = (np.arange(n_layers) >= 1) & (np.arange(n_layers) <= 3)
        cond = np.sum(thick_inv[seg] / rho_model[seg])
        print(f"   {mu:8.0e}   {mis:11.5f}   {rough:15.4f}   {cond:24.2f}")
        results.append((mu, mis, m, Z, rough))
    # Occam's choice: take the SMOOTHEST model whose misfit is within 10% of the
    # best achieved.  Models inside that band are indistinguishable at this noise.
    mis_min = min(r[1] for r in results)
    acceptable = [r for r in results if r[1] <= 1.10 * mis_min]
    mu_best, mis_best, m_best, Z_best, rough_best = max(acceptable, key=lambda r: r[0])
    print(f"   the noise sigma is {sigma:.5f}; the smallest misfit achieved is {mis_min:.5f}")
    print(f"   models within 10% of that are indistinguishable at this noise; taking")
    print(f"   the smoothest of them (the Occam choice) gives mu = {mu_best:g}")
    rho_best = 10.0 ** m_best
    print("   recovered resistivity by layer (Ohm m):")
    print("   " + ", ".join(f"{v:.1f}" for v in rho_best))
    print(f"   true top layers were {rho_true[0]:.0f}, {rho_true[1]:.0f}, "
          f"{rho_true[2]:.0f} Ohm m")
    cond_true = thick_true[1] / rho_true[1]
    cond_rec = np.sum(thick_inv[1:4] / rho_best[1:4])
    print(f"   conductance of the conductive layer: true {cond_true:.2f} S, "
          f"recovered {cond_rec:.2f} S ({cond_rec / cond_true * 100:.1f}%)")

    section("3. Resolution and equivalence")
    print("the same data were fitted by two models with the same conductance")
    print("   model                         rms misfit   conductance (S)")
    for name, rr, th in (
        ("true  20 Ohm m over 2 km", [200.0, 20.0, 400.0, 50.0],
         np.array([1.0, 2.0, 5.0]) * KM),
        ("same conductance: 10 Ohm m over 1 km", [200.0, 10.0, 400.0, 50.0],
         np.array([1.0, 1.0, 5.0]) * KM),
        ("same conductance: 40 Ohm m over 4 km", [200.0, 40.0, 400.0, 50.0],
         np.array([1.0, 4.0, 5.0]) * KM),
    ):
        Zc = mt_1d_Z(PERIODS, rr, list(th))
        res = np.sqrt(np.mean((dobs - data_vector(Zc)) ** 2))
        print(f"   {name:34s} {res:11.5f}   {th[1] / rr[1]:15.2f}")
    print("   three different Earths with the same conductance S = h/rho fit the same")
    print("   data: with a thin layer the data constrain S, not h and rho separately.")

    section("4. A static shift")
    shift = 1.6
    Z_shift = shift * Z_true
    dobs_s = data_vector(Z_shift) + NOISE * np.std(dobs) * RNG.standard_normal(dobs.size)
    m_s, Z_s, mis_s, rough_s = occam(PERIODS, thick_inv, dobs_s, n_layers, mu_best)
    rho_s = 10.0 ** m_s
    print(f"the impedance is multiplied by {shift:.1f} (a near-surface galvanic")
    print("distortion of the electric field; the phase is untouched):")
    print(f"   rho_a at the longest period: {rho_a[-1]:.2f} -> "
          f"{np.abs(Z_shift[-1]) ** 2 / (2 * np.pi / PERIODS[-1] * MU0):.2f} Ohm m")
    print(f"   phase at the longest period: {phase[-1]:.3f} -> "
          f"{np.degrees(np.angle(Z_shift[-1])):.3f} deg")
    print(f"   inversion of the shifted data: rms misfit {mis_s:.5f}, top layer "
          f"{rho_s[0]:.1f} Ohm m (true {rho_true[0]:.0f}),")
    print(f"   layer 2 {rho_s[1]:.1f} Ohm m (true {rho_true[1]:.0f})")
    print("   the misfit is just as good and every resistivity has moved: a static")
    print("   shift is absorbed by the model, which is why it must be removed or")
    print("   jointly inverted with a priori information.")

    section("5. Summary for the lesson")
    print(f"  noise sigma {sigma:.5f}; best mu {mu_best:g} gives rms {mis_best:.5f}")
    print(f"  the conductive layer is smeared over several 0.8 km layers, but its")
    print(f"  conductance is recovered to {cond_rec / cond_true * 100:.1f}%")
    print(f"  a static shift of {shift:.1f} is absorbed into the model and leaves the")
    print("  misfit unchanged: amplitude alone cannot distinguish it from structure")


if __name__ == "__main__":
    main()
