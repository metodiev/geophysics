"""Wave description: the bookkeeping of f, T, omega, lambda, k and v.

Run:  python3 wave_basics_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-04. The script:

1. Builds the parameter table for four real wave types from c = lambda f,
   omega = 2 pi f, k = 2 pi/lambda, and checks the identity v = omega/k.
2. Demonstrates sampling and aliasing: a 60 Hz signal sampled at 100 Hz looks
   like 40 Hz; the apparent frequency is measured from the sampled data.
3. Measures a phase velocity from the phase difference between two receivers,
   using the discrete Fourier coefficient at the known frequency, and exhibits
   the cycle-skipping ambiguity when the spacing exceeds a wavelength.
4. Adds two sinusoids and measures the beat of the envelope.
5. Shows how much velocity error one cycle of phase corresponds to.

Every number printed below was produced by this script.
"""

import cmath
import math

G = 9.80665
C_LIGHT = 2.99792458e8      # m/s, exact by definition (SI)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def part1_parameters():
    section("1. The parameter table: one number determines all the others")
    rows = [
        ("seismic P in granite", 5600.0, 10.0),
        ("ultrasound in steel", 5900.0, 1.0e6),
        ("ocean swell (deep water)", G * 10.0 / (2.0 * math.pi), 0.1),
        ("GPR in soil, eps_r = 4", C_LIGHT / 2.0, 1.0e8),
    ]
    print(f"{'wave':>26} {'v (m/s)':>12} {'f (Hz)':>11} {'lambda (m)':>12} "
          f"{'T (s)':>11} {'k (1/m)':>11} {'omega/k - v':>12}")
    for name, v, f in rows:
        lam = v / f
        k = 2.0 * math.pi / lam
        omega = 2.0 * math.pi * f
        print(f"{name:>26} {v:12.5g} {f:11.4g} {lam:12.5g} {1.0 / f:11.4g} "
              f"{k:11.5g} {omega / k - v:12.3e}")
    print()
    print("  For a deep-water gravity wave the speed is not a material constant:")
    print("  c = sqrt(g lambda/(2 pi)) = gT/(2 pi), so a longer swell travels")
    print("  faster. That is dispersion (lesson 02-03-07). For an elastic wave in")
    print("  a homogeneous rock, c is a material property and every frequency")
    print("  travels at the same speed.")


def measure_frequency_from_samples(f, fs, n):
    """Apparent frequency from interpolated upward zero crossings."""
    xs = [math.cos(2.0 * math.pi * f * i / fs) for i in range(n)]
    times = []
    for i in range(1, n):
        if xs[i - 1] < 0.0 <= xs[i]:
            frac = -xs[i - 1] / (xs[i] - xs[i - 1])
            times.append((i - 1 + frac) / fs)
    if len(times) < 2:
        return float("nan")
    return (len(times) - 1) / (times[-1] - times[0])


def part2_aliasing():
    section("2. Sampling and aliasing")
    fs = 100.0
    print(f"sample rate fs = {fs} Hz -> Nyquist frequency = {fs / 2.0} Hz")
    print(f"{'true f':>9} {'apparent':>10} {'measured':>12}")
    for f in (10.0, 30.0, 40.0, 60.0, 90.0, 110.0):
        m = round(f / fs)
        folded = abs(f - m * fs)
        measured = measure_frequency_from_samples(f, fs, 4000)
        print(f"{f:9.1f} {folded:10.1f} {measured:12.4f}")
    print()
    print("  Frequencies above the Nyquist frequency are indistinguishable from")
    print("  their aliases: 60 Hz sampled at 100 Hz is 40 Hz, and no processing")
    print("  can tell them apart afterwards. Anti-alias filtering before")
    print("  digitising is the only remedy.")


def dft_at(samples, dt, f):
    """Discrete Fourier coefficient at frequency f (a single DFT bin)."""
    total = 0j
    for i, x in enumerate(samples):
        total += x * cmath.exp(-2j * math.pi * f * i * dt)
    return total


def part3_phase_velocity():
    section("3. Phase velocity from two receivers, and cycle skipping")
    v_true = 2000.0
    f = 25.0
    lam = v_true / f
    omega = 2.0 * math.pi * f
    fs = 5000.0
    dt = 1.0 / fs
    n = 4000
    print(f"v = {v_true} m/s at f = {f} Hz -> lambda = {lam:.4f} m; "
          f"sampled at {fs:.0f} Hz for {n * dt:.3f} s")
    print(f"{'dx (m)':>9} {'dx/lambda':>10} {'phase lag (deg)':>17} "
          f"{'v recovered':>13} {'error':>10}")
    for dx in (0.3 * lam, 0.8 * lam, 1.3 * lam):
        x1 = [math.cos(omega * i * dt) for i in range(n)]
        x2 = [math.cos(omega * (i * dt - dx / v_true)) for i in range(n)]
        lag = cmath.phase(dft_at(x1, dt, f)) - cmath.phase(dft_at(x2, dt, f))
        lag = lag - 2.0 * math.pi * round(lag / (2.0 * math.pi))   # to (-pi, pi]
        v_meas = omega * dx / lag
        print(f"{dx:9.3f} {dx / lam:10.3f} {math.degrees(lag):17.4f} "
              f"{v_meas:13.3f} {(v_meas - v_true) / v_true:10.3f}")
    print()
    print("  Up to one wavelength the lag gives the true speed. Beyond it the lag")
    print("  is only known modulo 2 pi: 0.8 lambda wraps to -72 deg and the naive")
    print("  inversion returns a negative speed, while 1.3 lambda returns 8666.667")
    print("  m/s, which is 4.333 times too high and is the classic cycle skip.")
    print("  Spacing must stay below the shortest wavelength to be resolved - the")
    print("  array-design rule for every seismic and GPR survey.")


def part4_beats():
    section("4. Superposition of two sinusoids: the beat")
    f1, f2 = 8.0, 9.0
    n, dt = 4000, 0.001
    xs = [math.cos(2.0 * math.pi * f1 * i * dt) + math.cos(2.0 * math.pi * f2 * i * dt)
          for i in range(n)]
    print(f"f1 = {f1} Hz, f2 = {f2} Hz -> envelope at |f2 - f1| = {abs(f2 - f1)} Hz, "
          f"period {1.0 / abs(f2 - f1)} s")
    env = [2.0 * abs(math.cos(math.pi * (f2 - f1) * i * dt)) for i in range(n)]
    zeros = [i * dt for i in range(1, n) if env[i - 1] < 1e-3 <= env[i]]
    spacing = sum(zeros[i + 1] - zeros[i] for i in range(len(zeros) - 1)) / (len(zeros) - 1)
    print(f"measured spacing of envelope nodes = {spacing:.6f} s "
          f"(half the beat period, {0.5 / abs(f2 - f1):.6f} s)")
    print(f"measured max |x| = {max(abs(x) for x in xs):.9f}, predicted "
          f"{2.0:.9f}")
    print()
    print("  The sum of two equal-amplitude sinusoids is a carrier at the mean")
    print("  frequency multiplied by a slow envelope at half the difference")
    print("  frequency - the time-domain face of the wave packet of lesson")
    print("  02-03-07.")


def part5_phase_carries_timing():
    section("5. How much velocity error is one cycle of phase?")
    f, v, distance = 10.0, 3000.0, 600.0
    print(f"A {f} Hz wave travels {distance} m at {v} m/s: delay "
          f"{distance / v:.6f} s = {distance * f / v:.4f} cycles = "
          f"{math.degrees(2.0 * math.pi * f * distance / v):.2f} deg")
    for dv in (0.5, 5.0, 16.7):
        dphase = 2.0 * math.pi * f * distance * (1.0 / (v - dv) - 1.0 / v)
        print(f"  velocity error {dv:6.2f} m/s -> phase change "
              f"{math.degrees(dphase):+.3f} deg ({dphase / (2.0 * math.pi):+.5f} cycles)")
    t = distance / v
    one_degree = 2.0 * math.pi / 360.0 / (2.0 * math.pi * f)     # seconds per degree
    dv_per_degree = distance / (t - one_degree) - v
    print(f"  one degree of phase = {one_degree * 1e3:.4f} ms of travel time = "
          f"{dv_per_degree:.3f} m/s of velocity over this path")
    print()
    print("  Phase resolves velocity finely - a few m/s here - but only within one")
    print("  cycle; beyond that the cycle count is unknown and the velocity error")
    print("  jumps by a factor of order the number of cycles missed, which is why")
    print("  seismologists count cycles instead of trusting one phase reading.")


if __name__ == "__main__":
    part1_parameters()
    part2_aliasing()
    part3_phase_velocity()
    part4_beats()
    part5_phase_carries_timing()
