"""Phase, harmonics and superposition.

Run:  python3 harmonics_demo.py
Requires: Python standard library only.

Companion to lesson 01-03-05. Every result here is computed from the series
and formulas in the lesson, so you can compare your own working directly.

Sections
--------
1. Phase form and quadrature form of one sinusoid
2. Superposition, beats and the envelope
3. Harmonic synthesis of a square wave, and the Gibbs overshoot
4. A tidal analogue: M2 plus S2 gives the spring-neap envelope (ILLUSTRATIVE)
5. Two wavenumbers together: phase velocity and group velocity
"""

from __future__ import annotations

import math

TAU = 2.0 * math.pi


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rms(values: list[float]) -> float:
    return math.sqrt(sum(v * v for v in values) / len(values))


def main() -> None:
    section("1. Phase form and quadrature form of one sinusoid")
    A, f, phi = 2.5, 0.4, 0.7
    omega = TAU * f
    print(f"A = {A}, f = {f} Hz, phase phi = {phi} rad")
    print(f"omega = 2 pi f = {omega:.10f} rad/s")
    print(f"period T = 1/f = {1.0 / f:.6f} s")
    # A cos(wt - phi) = (A cos phi) cos(wt) + (A sin phi) sin(wt)
    a_coef = A * math.cos(phi)
    b_coef = A * math.sin(phi)
    print(f"\nA cos(phi) = {a_coef:.10f}   (in-phase amplitude)")
    print(f"A sin(phi) = {b_coef:.10f}   (quadrature amplitude)")
    print(f"hypot(a, b) = {math.hypot(a_coef, b_coef):.10f}   (recovers A)")
    print(f"atan2(b, a) = {math.atan2(b_coef, a_coef):.10f}   (recovers phi)")
    print(f"\n{'t (s)':>8} {'A cos(wt-phi)':>16} {'a cos(wt)+b sin(wt)':>22}")
    for k in range(5):
        t = k * 0.25
        left = A * math.cos(omega * t - phi)
        right = a_coef * math.cos(omega * t) + b_coef * math.sin(omega * t)
        print(f"{t:>8.2f} {left:>16.10f} {right:>22.10f}")
    print("The two columns are the same function written two ways, which is")
    print("why amplitude and phase are all you need to describe a sinusoid.")

    section("2. Superposition, beats and the envelope")
    f1, f2 = 1.0, 1.1
    print(f"f1 = {f1} Hz, f2 = {f2} Hz, equal unit amplitudes")
    print(f"difference frequency |f1 - f2| = {abs(f1 - f2):.6f} Hz")
    print(f"beat period 1/|f1 - f2| = {1.0 / abs(f1 - f2):.6f} s")
    print(f"carrier (mean) frequency = {(f1 + f2) / 2:.6f} Hz")
    print(f"\n{'t (s)':>8} {'cos(2 pi f1 t)':>16} {'cos(2 pi f2 t)':>16} {'sum':>12}"
          f" {'envelope 2cos':>15}")
    for k in range(9):
        t = k * 0.5
        x1 = math.cos(TAU * f1 * t)
        x2 = math.cos(TAU * f2 * t)
        env = 2.0 * abs(math.cos(math.pi * (f1 - f2) * t))
        print(f"{t:>8.2f} {x1:>16.6f} {x2:>16.6f} {x1 + x2:>12.6f} {env:>15.6f}")
    print("\nThe envelope column is the exact identity")
    print("  cos(2 pi f1 t) + cos(2 pi f2 t) = 2 cos(pi (f1-f2) t) cos(pi (f1+f2) t),")
    print("so |sum| never exceeds the envelope. Beat period is 10 s, and the")
    print("sum returns to zero every half of that.")

    section("3. Harmonic synthesis of a square wave, and the Gibbs overshoot")
    # A unit square wave of period 1 s built from odd harmonics of amplitude
    # 4/(pi n). The partial sum is compared with the ideal square wave.
    def square_partial(t: float, n_harm: int) -> float:
        total = 0.0
        for k in range(1, n_harm + 1):
            n = 2 * k - 1
            total += 4.0 / (math.pi * n) * math.sin(TAU * n * t)
        return total

    def ideal_square(t: float) -> float:
        return 1.0 if (t % 1.0) < 0.5 else -1.0

    samples = [i / 2000.0 for i in range(2000)]
    print(f"{'harmonics':>10} {'rms error':>14} {'max |error|':>14}"
          f" {'peak overshoot (percent of jump)':>34}")
    for n_harm in (1, 3, 5, 11, 51, 201):
        approx = [square_partial(t, n_harm) for t in samples]
        err = [a - ideal_square(t) for a, t in zip(approx, samples)]
        # The overshoot peak sits within about 1/N of the discontinuity, so the
        # scan grid must get finer as more harmonics are retained.
        n_scan = max(20_000, 100 * n_harm)
        peak = max(square_partial(j * 0.5 / n_scan, n_harm)
                   for j in range(n_scan + 1))
        print(f"{n_harm:>10} {rms(err):>14.6f} {max(abs(e) for e in err):>14.6f}"
              f" {(peak - 1.0) / 2.0 * 100:>33.3f}")
    print("\nRead the columns together, because each says something different.")
    print("The rms error falls steadily as harmonics are added: the series does")
    print("converge in the mean-square sense. The maximum pointwise error does")
    print("not fall at all - it stays at 1.000000, because the discontinuity")
    print("itself is a jump of 2 and no partial sum can ever cross it. And the")
    print("overshoot adjacent to the jump converges to about 8.95 percent of the")
    print("jump instead of going to zero: 8.949 percent at 201 harmonics, and")
    print("still falling only in the fifth decimal. That is the Gibbs")
    print("phenomenon, and it is why a band-limited version of a sharp arrival")
    print("always rings before the arrival time.")
    print("\nThe n = 1 row deserves a caveat: a single sine has no overshoot to")
    print("speak of, and its 13.7 percent is the peak of the sine itself, not a")
    print("Gibbs oscillation. The phenomenon is asymptotic in n.")

    section("4. A tidal analogue: M2 plus S2, ILLUSTRATIVE")
    # Standard constituent periods. M2 is the principal lunar semidiurnal
    # constituent; S2 is its solar counterpart. These are tabulated
    # astronomical constants, quoted here to 7 significant figures.
    M2_HOURS = 12.4206012
    S2_HOURS = 12.0
    f_m2 = 1.0 / M2_HOURS
    f_s2 = 1.0 / S2_HOURS
    beat_hz = abs(f_s2 - f_m2)
    print(f"M2 period = {M2_HOURS} h  -> frequency = {f_m2:.10f} cycles/h")
    print(f"S2 period = {S2_HOURS} h  -> frequency = {f_s2:.10f} cycles/h")
    print(f"difference frequency = {beat_hz:.10f} cycles/h")
    print(f"spring-neap period = 1/difference = {1.0 / beat_hz:.4f} h "
          f"= {1.0 / beat_hz / 24.0:.4f} days")
    print("\nThe printed spring-neap period is the beat of the two dominant")
    print("semidiurnal constituents. Real tidal records also carry K1, O1 and")
    print("P1, so the observed neap-to-spring interval varies; the value above")
    print("is what the two-constituent model predicts, not a universal constant.")

    section("5. Two wavenumbers together: phase velocity and group velocity")
    # Two unit-amplitude waves of the same amplitude, wavenumbers k0 - dk and
    # k0 + dk, angular frequencies w0 - dw and w0 + dw.
    k0, w0 = 2.0, 6.0     # arbitrary units consistent with c = w0/k0 = 3
    dk, dw = 0.1, 0.35    # dw/dk = 3.5, deliberately different from w0/k0
    print(f"k0 = {k0}, w0 = {w0}   -> phase velocity w0/k0 = {w0 / k0:.6f}")
    print(f"dk = {dk}, dw = {dw}   -> group velocity dw/dk = {dw / dk:.6f}")
    print(f"\n{'x':>8} {'u1 + u2':>14} {'envelope 2cos(dk x - dw t)':>30}")
    t = 0.0
    for k in range(7):
        x = k * 1.0
        u = (math.cos((k0 - dk) * x - (w0 - dw) * t)
             + math.cos((k0 + dk) * x - (w0 + dw) * t))
        env = 2.0 * math.cos(dk * x - dw * t)
        print(f"{x:>8.1f} {u:>14.8f} {env:>30.8f}")
    print("\nThe sum of two nearby wavenumbers factorises into a carrier moving")
    print("at the phase velocity and an envelope moving at the group velocity.")
    print("When those two speeds differ you have dispersion, and dispersion is")
    print("how a seismogram tells you the Earth is not a single-velocity body.")


if __name__ == "__main__":
    main()
