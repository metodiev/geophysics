#!/usr/bin/env python3
"""Linear time-invariant systems: superposition, time-invariance, the impulse
response, causality, BIBO stability, the step response and the eigenfunction
property -- each one measured rather than asserted.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lti_systems_demo.py

All models and data in this module are SYNTHETIC.  The systems below are chosen
teaching examples with known analytic answers, so every measured number has an
exact value to compare against.

Contents
--------
1.  A candidate system tested for linearity and time-invariance.
2.  The impulse response, and reconstruction of the output by superposition.
3.  A nonlinear system that fails the same tests, with the size of the failure.
4.  Causality, and BIBO stability from the absolute sum of the impulse response.
5.  Step response and DC gain.
6.  The eigenfunction property: complex exponentials pass through with a
    multiplicative gain H(e^{i w}).
7.  Group delay of a causal moving average.
8.  Convolution of two boxcars, against the exact triangular result.
"""

import numpy as np
from scipy import signal as sps

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC systems (chosen teaching models) ------------------------------
H_MA = np.ones(5) / 5.0             # 5-point moving average, FIR
A_IIR = 0.9                         # one-pole recursive system, stable
A_UNSTABLE = 1.1                    # same form, unstable


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def iir_impulse(a, n=64):
    """Impulse response a^n u[n] of y[n] = a y[n-1] + x[n]."""
    return a ** np.arange(n)


def apply_iir(x, a):
    """Direct recursion y[n] = a y[n-1] + x[n]; x is 1-D."""
    y = np.zeros_like(x, dtype=float)
    prev = 0.0
    for n, xn in enumerate(x):
        prev = a * prev + xn
        y[n] = prev
    return y


def main():
    n = 64
    impulse = np.zeros(n)
    impulse[0] = 1.0

    section("1. Linearity and time-invariance of y = x convolved with [1, .5, .25]")
    h = np.array([1.0, 0.5, 0.25])

    def system(x):
        return np.convolve(x, h)[: len(x)]

    x1 = RNG.normal(0.0, 1.0, n)
    x2 = RNG.normal(0.0, 1.0, n)
    alpha, beta = 2.5, -1.25
    lhs = system(alpha * x1 + beta * x2)
    rhs = alpha * system(x1) + beta * system(x2)
    print(f"superposition error max|H[a x1 + b x2] - aH[x1] - bH[x2]| = "
          f"{np.max(np.abs(lhs - rhs)):.3e} (arbitrary units)")

    shift = 7
    x1_shift = np.zeros(n)
    x1_shift[shift:] = x1[: n - shift]
    y_shift = system(x1_shift)
    y_expected = np.zeros(n)
    y_expected[shift:] = system(x1)[: n - shift]
    print(f"time-invariance error max|H[x shifted] - H[x] shifted| = "
          f"{np.max(np.abs(y_shift - y_expected)):.3e}")

    section("2. The impulse response and superposition")
    h_measured = system(impulse)
    print(f"measured impulse response (first 6 samples) = "
          f"{np.array2string(h_measured[:6], precision=6)}")
    print(f"the system's declared h                       = {h}")
    print(f"max difference                               = "
          f"{np.max(np.abs(h_measured[:3] - h)):.3e}")
    y_direct = system(x1)
    y_super = np.zeros(n)
    for k in range(n):
        y_super[k:] += x1[k] * h_measured[: n - k]
    print(f"superposition reconstruction max error       = "
          f"{np.max(np.abs(y_direct - y_super)):.3e}")

    section("3. A nonlinear system fails the same tests")
    print("candidate: Q{x} = x^2")
    lhs_q = (alpha * x1 + beta * x2) ** 2
    rhs_q = alpha * x1 ** 2 + beta * x2 ** 2
    print(f"H[a x1 + b x2] - (aH[x1] + bH[x2]) rms = "
          f"{np.sqrt(np.mean((lhs_q - rhs_q) ** 2)):.4f}")
    print(f"rms of the output itself               = "
          f"{np.sqrt(np.mean(lhs_q ** 2)):.4f}")
    print(f"relative failure of superposition      = "
          f"{np.sqrt(np.mean((lhs_q - rhs_q) ** 2)) / np.sqrt(np.mean(lhs_q ** 2)):.4f}"
          f"  (systematically nonzero: the system is nonlinear)")

    section("4. Causality and BIBO stability")
    h_stable = iir_impulse(A_IIR, 200)
    h_unstable = iir_impulse(A_UNSTABLE, 60)
    print("BIBO stability criterion: a causal LTI system is stable iff "
          "sum |h[n]| < infinity")
    for name, a, hh in (("a = 0.9  (stable)", A_IIR, h_stable),
                        ("a = 1.1  (unstable)", A_UNSTABLE, h_unstable)):
        print(f"  {name}: sum |h[n]| = {np.sum(np.abs(hh)):.6f} "
              f"(exact 1/(1-a) = {1.0 / (1.0 - a):.6f} truncated)"
              if a < 1 else
              f"  {name}: sum |h[n]| = {np.sum(np.abs(hh)):.6f} over 60 samples, "
              f"exact 1/(1-a) does not exist")
    print(f"h[n] for a = 0.9 is exactly a^n u[n]: max error vs a**n = "
          f"{np.max(np.abs(apply_iir(impulse, A_IIR) - iir_impulse(A_IIR, n))):.3e}")

    section("5. Step response and DC gain")
    step = np.ones(n)
    y_step_iir = apply_iir(step, A_IIR)
    y_step_ma = np.convolve(step, H_MA, mode="full")
    print(f"one-pole a = 0.9: y_step[10] = {y_step_iir[10]:.6f}, "
          f"y_step[63] = {y_step_iir[63]:.6f}  (limit 1/(1-a) = "
          f"{1.0 / (1.0 - A_IIR):.6f})")
    print(f"5-point moving average: y_step[3] = {y_step_ma[3]:.6f} "
          f"(= 4/5 = {4 / 5:.6f}), y_step[20] = {y_step_ma[20]:.6f} (limit 1)")
    print("so the DC gain is the sum of the impulse response: "
          f"{np.sum(H_MA):.6f} for the moving average")

    section("6. Eigenfunction property: complex exponentials")
    w = 0.7                                  # rad/sample
    x_exp = np.exp(1j * w * np.arange(n))
    y_exp = np.convolve(x_exp, H_MA)[:n]
    H_analytic = np.sum(H_MA * np.exp(-1j * w * np.arange(len(H_MA))))
    H_numeric = y_exp[40] / x_exp[40]
    print(f"H(e^(i w)) from the definition  = {H_numeric.real:+.10f} "
          f"{H_numeric.imag:+.10f}j")
    print(f"H(e^(i w)) by summing h[n]e^(-iwn) = {H_analytic.real:+.10f} "
          f"{H_analytic.imag:+.10f}j")
    print(f"max relative error over the whole record = "
          f"{np.max(np.abs(y_exp[20:] - H_analytic * x_exp[20:])):.3e}")
    w_freqz, H_freqz = sps.freqz(H_MA, worN=[w])
    print(f"scipy.signal.freqz at w = {w} gives {H_freqz[0].real:+.10f} "
          f"{H_freqz[0].imag:+.10f}j")

    section("7. Group delay of a causal moving average")
    x_pulse = np.zeros(200)
    x_pulse[50] = 1.0
    y_pulse = np.convolve(x_pulse, H_MA, mode="full")
    onset = int(np.argmax(y_pulse > 1e-12))
    idx = np.arange(len(y_pulse))
    centroid = np.sum(idx * y_pulse) / np.sum(y_pulse)
    print(f"impulse at sample 50 -> output starts at sample {onset} and its "
          f"centroid is at sample {centroid:.6f}")
    print(f"   so the delay measured from the centroid = "
          f"{centroid - 50:.6f} samples")
    print(f"group delay of a symmetric length-M FIR: (M-1)/2 = "
          f"{(len(H_MA) - 1) / 2:.1f} samples")
    w_grid = np.linspace(0.05, 1.15, 400)   # below the first null at 2*pi/5
    _, Hw = sps.freqz(H_MA, worN=w_grid)
    phase = np.unwrap(np.angle(Hw))
    gd = -np.gradient(phase, w_grid)
    print(f"group delay from the unwrapped phase slope on 0.05 <= w <= 1.15 rad "
          f"(first null at 2*pi/5 = {2 * np.pi / 5:.4f} rad):")
    print(f"   mean = {gd.mean():.6f} samples, max deviation from 2 = "
          f"{np.max(np.abs(gd - 2.0)):.3e} samples")

    section("8. Convolution of two boxcars is a triangle")
    b1 = np.ones(4)
    b2 = np.ones(4)
    conv = np.convolve(b1, b2)
    exact = np.array([1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0])
    print(f"boxcar(4) * boxcar(4) = {conv}")
    print(f"exact triangular result = {exact}")
    print(f"max difference = {np.max(np.abs(conv - exact)):.3e}; "
          f"output length {len(conv)} = N1 + N2 - 1 = {len(b1) + len(b2) - 1}")


if __name__ == "__main__":
    main()
