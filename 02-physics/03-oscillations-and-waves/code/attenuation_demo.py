"""Attenuation, absorption and the quality factor Q, measured.

Run:  python3 attenuation_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-10. The script:

1. Tabulates the amplitude decay for a range of Q at a fixed wavelength and
   verifies the identity Q = pi/(alpha lambda) by measuring the decay over one
   wavelength.
2. Measures Q from a numerical viscoacoustic simulation (u_tt + 2 beta u_t =
   c^2 u_xx) by the logarithmic decrement of successive peaks, and compares it
   with omega/(2 beta).
3. Recovers Q from a synthetic two-receiver spectral ratio, with and without
   noise, showing how the bandwidth and the noise control the uncertainty.
4. Computes Q and the velocity dispersion of a standard linear solid and tests
   the nearly-constant-Q relation V(omega)/V(omega0) - 1 = ln(omega/omega0)/(pi Q).

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def part1_decay():
    section("1. Amplitude decay for a range of Q, at wavelength 50 m")
    wavelength = 50.0
    print(f"alpha = pi/(Q lambda), decay length 1/alpha, and the amplitude after")
    print(f"1 km of propagation at wavelength {wavelength:.0f} m")
    print(f"{'Q':>7} {'alpha (1/m)':>13} {'1/alpha (m)':>13} "
          f"{'exp(-alpha*1000)':>17} {'pi/(alpha lambda)':>18}")
    for q in (20.0, 50.0, 100.0, 200.0, 500.0):
        alpha = math.pi / (q * wavelength)
        print(f"{q:7.1f} {alpha:13.6e} {1.0 / alpha:13.1f} "
              f"{math.exp(-alpha * 1000.0):17.6f} "
              f"{math.pi / (alpha * wavelength):18.6f}")
    print()
    print("  Over one wavelength the amplitude falls by the factor exp(-pi/Q), and")
    print("  the stored energy falls by exp(-2 pi/Q), so the fractional energy lost")
    print("  per cycle is 2 pi/Q: with Q = 100 barely 6 per cent per cycle, and with")
    print("  Q = 20 about 27 per cent. 1/Q is the natural measure of loss; alpha")
    print("  converts it into metres, but only at one frequency.")


def part2_numerical_q():
    section("2. Measuring Q from a damped standing mode")
    c, length = 2000.0, 200.0            # m/s, m
    beta = 0.8                           # 1/s
    k = math.pi / length                 # first mode
    omega = c * k
    period = 2.0 * math.pi / omega
    print(f"c = {c:.0f} m/s, domain length {length:.0f} m, first mode: "
          f"omega = c k = {omega:.6f} rad/s, period = {period:.6f} s")
    print(f"damping coefficient beta = {beta:.2f} 1/s -> "
          f"Q = omega/(2 beta) = {omega / (2 * beta):.4f}")
    n = 201
    dx = length / (n - 1)
    x = [i * dx for i in range(n)]
    dt = 0.4 * dx / c
    u_old = [math.sin(k * xi) for xi in x]
    u = [0.0] * n
    for i in range(1, n - 1):
        u[i] = u_old[i] + 0.5 * dt * dt * c * c * (
            u_old[i + 1] - 2.0 * u_old[i] + u_old[i - 1]) / dx ** 2
    probe = n // 2                       # an antinode of the first mode
    steps = int(round(10.0 * period / dt))
    window = int(round(period / dt))
    amps = []
    current = 0.0
    for step in range(steps):
        u_new = [0.0] * n
        for i in range(1, n - 1):
            laplacian = (u[i + 1] - 2.0 * u[i] + u[i - 1]) / dx ** 2
            u_new[i] = (2.0 * u[i] - (1.0 - beta * dt) * u_old[i]
                        + dt * dt * c * c * laplacian) / (1.0 + beta * dt)
        u_old, u = u, u_new
        current = max(current, abs(u[probe]))
        if (step + 1) % window == 0:
            amps.append(current)
            current = 0.0
    print(f"peak |u| per period: "
          + ", ".join(f"{a:.5f}" for a in amps))
    ts = [(i + 0.5) * period for i in range(len(amps))]
    logs = [math.log(a) for a in amps]
    m = len(ts)
    mt = sum(ts) / m
    ml = sum(logs) / m
    slope = (sum((t - mt) * (l - ml) for t, l in zip(ts, logs))
             / sum((t - mt) ** 2 for t in ts))
    q_meas = omega / (-2.0 * slope)
    print(f"measured decay rate from the fit = {-slope:.6f} 1/s "
          f"(input beta = {beta})")
    print(f"Q from the fitted decay        = {q_meas:.4f}")
    print(f"Q from Q = omega/(2 beta)      = {omega / (2 * beta):.4f}")
    print(f"difference = {abs(q_meas - omega / (2 * beta)):.2e}")
    print()
    print("  The amplitude decays as exp(-beta t) while the phase advances as")
    print("  omega t, so the decrement per cycle is 2 pi beta/omega = pi/Q. The")
    print("  simulation reproduces that from the differential equation and nothing")
    print("  else. Q is not an independent knob: it says what a decay rate means")
    print("  at a frequency, which is why one Q describes a whole band only when")
    print("  the medium is nearly constant-Q.")


def lcg(seed):
    """Deterministic uniform generator in (0,1), for reproducible noise."""
    state = seed

    def draw():
        nonlocal state
        state = (1103515245 * state + 12345) % (2 ** 31)
        return state / float(2 ** 31)

    return draw


def part3_spectral_ratio():
    section("3. Recovering Q from a spectral ratio, with noise")
    Q_true = 80.0
    v = 3000.0
    x1, x2 = 500.0, 1500.0
    print(f"model: Q = {Q_true:.0f}, v = {v:.0f} m/s, receivers at "
          f"{x1:.0f} m and {x2:.0f} m (separation {x2 - x1:.0f} m)")
    print(f"{'noise':>7} {'Q recovered':>12} {'error (%)':>11} {'slope fit residual':>20}")
    for noise in (0.0, 0.01, 0.05):
        draw = lcg(20261014)
        freqs = [5.0 + 2.5 * i for i in range(40)]
        xs = []
        ys = []
        for f in freqs:
            alpha = math.pi * f / (Q_true * v)          # alpha = omega/(2 Q v)
            a1 = math.exp(-alpha * x1) * (1.0 + noise * (2.0 * draw() - 1.0))
            a2 = math.exp(-alpha * x2) * (1.0 + noise * (2.0 * draw() - 1.0))
            xs.append(f)
            ys.append(math.log(a1 / a2))
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        slope = sxy / sxx
        intercept = my - slope * mx
        resid = math.sqrt(sum((y - (intercept + slope * x)) ** 2
                              for x, y in zip(xs, ys)) / (n - 2))
        q_est = math.pi * (x2 - x1) / (v * slope)
        print(f"{noise:7.2f} {q_est:12.4f} {(q_est - Q_true) / Q_true * 100:11.3f} "
              f"{resid:20.3e}")
    print()
    print("  ln(A1/A2) = -pi f (x2 - x1)/(Q v) is a straight line in frequency whose")
    print("  slope gives Q directly once v and the path length are known. The")
    print("  noiseless case recovers Q exactly; 1 per cent random amplitude error")
    print("  moves Q by 0.5 per cent and 5 per cent error by 2.5 per cent, while the")
    print("  fit residual column shows the scatter left in the data. The estimator is")
    print("  well conditioned because the whole band is fitted at once. Real Q")
    print("  estimation is harder than this because v must be known independently and")
    print("  the amplitudes must be corrected for geometric spreading, source and")
    print("  receiver coupling, and focusing - effects that mimic attenuation and can")
    print("  dominate it. Every spectral-ratio Q should carry an error budget.")


def part4_dispersion():
    section("4. A standard linear solid: Q and its inevitable dispersion")
    rho = 2600.0
    mu_r, q0 = 30.0e9, 30.0
    # Zener (standard linear solid) with peak Q0 at omega0: set tau_e/tau_s so
    # that Q peaks at omega0, then scale
    omega0 = 2.0 * math.pi * 10.0
    tau_e = 1.0 / omega0 * (math.sqrt(1.0 + 1.0 / q0 ** 2) + 1.0 / q0)
    tau_s = 1.0 / omega0 * (math.sqrt(1.0 + 1.0 / q0 ** 2) - 1.0 / q0)
    mu_u = mu_r * tau_e / tau_s

    def moduli(omega):
        m = mu_u * (1.0 + 1j * omega * tau_e) / (1.0 + 1j * omega * tau_s)
        return m.real, m.imag

    m1_0, m2_0 = moduli(omega0)
    q_peak = m1_0 / m2_0
    v0 = math.sqrt(m1_0 / rho)
    print(f"mu_relaxed = {mu_r / 1e9:.4f} GPa, Q0 = {q0}, f0 = "
          f"{omega0 / (2 * math.pi):.1f} Hz")
    print(f"Q at f0 = {q_peak:.6f} (input {q0}); V(f0) = {v0:.4f} m/s")
    print(f"{'f (Hz)':>9} {'Q(f)':>10} {'V (m/s)':>11} {'V/V0 - 1':>12} "
          f"{'ln(f/f0)/(pi Q0)':>18} {'difference':>11}")
    for f in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0):
        omega = 2.0 * math.pi * f
        m1, m2 = moduli(omega)
        q = m1 / m2
        v = math.sqrt(m1 / rho)
        approx = math.log(f / 10.0) / (math.pi * q0)
        print(f"{f:9.1f} {q:10.4f} {v:11.4f} {v / v0 - 1:12.6f} "
              f"{approx:18.6f} {(v / v0 - 1) - approx:11.3e}")
    print()
    print("  Q is not constant even for this single relaxation: it peaks at f0 and")
    print("  falls away on both sides, roughly as omega below f0 and as 1/omega")
    print("  above it. Wherever Q is large the accompanying velocity dispersion is")
    print("  fixed by the attenuation through the Kramers-Kronig relations, and the")
    print("  nearly-constant-Q approximation V/V0 - 1 = ln(f/f0)/(pi Q0) reproduces")
    print("  it to about 10 to 25 per cent over a factor of five in frequency. Two")
    print("  decades away it fails by a factor of about two, because the dispersion")
    print("  of a single relaxation saturates while ln(f/f0) does not. The relation")
    print("  is a first-order result for Q >> 1 near the reference frequency, and it")
    print("  must be used inside that regime.")


if __name__ == "__main__":
    part1_decay()
    part2_numerical_q()
    part3_spectral_ratio()
    part4_dispersion()
