"""Fourier series and periodic decomposition, with ocean tides as the example.

Run:  python3 fourier_series_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-01 (Fourier Series and Periodic Decomposition).

The seven tidal *speeds* used below are the conventional tabulated Doodson
speeds (degrees per hour) that tidal analysis has used for a century; they are
physical constants of the Sun-Moon-Earth system and are not invented here.

The tidal *amplitudes and phases* are SYNTHETIC: they were chosen by hand to
make the arithmetic readable, and they are not a fit to any real tide gauge.

Conventions used throughout this module
---------------------------------------
Real signal, one-sided physical model:
    h(t) = sum_i  A_i * cos(omega_i * t - phi_i)        (phi_i = phase lag)
Discrete Fourier transform (analysis / forward), no scaling:
    X[k] = sum_{n=0}^{N-1} x[n] * exp(-2*pi*i*k*n/N)
Inverse transform:
    x[n] = (1/N) * sum_{k=0}^{N-1} X[k] * exp(+2*pi*i*k*n/N)
The forward transform therefore uses the exp(-i*omega*t) kernel.  Sample
spacing dt and sample count N give bin spacing df = 1/(N*dt).
"""

import cmath
import math

# ---------------------------------------------------------------------------
# Tidal constituents: conventional speeds in degrees per hour.
# Period in hours = 360 / speed.
# ---------------------------------------------------------------------------
CONSTITUENTS = (
    # name, speed (deg/hour), amplitude (m) SYNTHETIC, phase lag (deg) SYNTHETIC
    ("M2", 28.9841042, 1.20, 210.0),   # principal lunar semidiurnal
    ("S2", 30.0000000, 0.40, 230.0),   # principal solar semidiurnal
    ("N2", 28.4397295, 0.24, 190.0),   # larger lunar elliptic semidiurnal
    ("K2", 30.0821373, 0.11, 225.0),   # lunisolar semidiurnal
    ("K1", 15.0410686, 0.30, 110.0),   # lunisolar diurnal
    ("O1", 13.9430356, 0.18,  95.0),   # principal lunar diurnal
    ("P1", 14.9589314, 0.10, 105.0),   # principal solar diurnal
)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def speed_cph(deg_per_hour):
    """Cycles per hour."""
    return deg_per_hour / 360.0


def model_h(t_hours, constituents=CONSTITUENTS):
    """Synthesise the water level from the constituent list."""
    total = 0.0
    for _name, speed, amp, phase_deg in constituents:
        omega = 2.0 * math.pi * speed_cph(speed)   # radians per hour
        total += amp * math.cos(omega * t_hours - math.radians(phase_deg))
    return total


def trapz(func, a, b, n):
    """Composite trapezoidal rule on n intervals."""
    h = (b - a) / n
    total = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        total += func(a + i * h)
    return total * h


def dft(x):
    """Forward DFT, X[k] = sum_n x[n] exp(-2*pi*i*k*n/N).  O(N^2)."""
    n = len(x)
    out = []
    for k in range(n):
        acc = 0j
        for index in range(n):
            acc += x[index] * cmath.exp(-2j * math.pi * k * index / n)
        out.append(acc)
    return out


def gauss_solve(a, b):
    """Solve a . x = b by Gaussian elimination with partial pivoting."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[pivot] = m[pivot], m[col]
        pv = m[col][col]
        for r in range(col + 1, n):
            factor = m[r][col] / pv
            if factor == 0.0:
                continue
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))
        x[r] = s / m[r][r]
    return x


def amp_sigma(ata, coeffs, j, sigma):
    """First-order standard error of constituent j's amplitude.

    With X the design matrix, Cov(coeffs) = sigma^2 (X^T X)^-1.  Writing the
    fitted cos and sin coefficients as a and b, A = hypot(a, b), and the delta
    method gives

        Var(A) = (a^2 d11 + 2 a b d12 + b^2 d22) / (a^2 + b^2),

    where d are the entries of sigma^2 (X^T X)^-1 for that (a, b) pair.  The
    cross term matters: the cos and sin coefficients of one constituent are not
    equally well determined on a finite record, so Var(A) is not simply
    d11 + d22.
    """
    size = len(ata)
    i1, i2 = 1 + 2 * j, 2 + 2 * j
    col1 = gauss_solve(ata, [1.0 if i == i1 else 0.0 for i in range(size)])
    col2 = gauss_solve(ata, [1.0 if i == i2 else 0.0 for i in range(size)])
    d11 = col1[i1] * sigma ** 2
    d12 = col2[i1] * sigma ** 2
    d22 = col2[i2] * sigma ** 2
    a, b = coeffs[i1], coeffs[i2]
    return math.sqrt((a * a * d11 + 2.0 * a * b * d12 + b * b * d22) / (a * a + b * b))


class Lcg:
    """Minimal reproducible pseudo-random source (no third-party dependency)."""

    def __init__(self, seed=20261014):
        self.state = seed % (2 ** 31)

    def uniform(self):
        self.state = (1103515245 * self.state + 12345) % (2 ** 31)
        return self.state / float(2 ** 31)

    def normal(self):
        """Sum of 12 uniforms minus 6: mean 0, standard deviation exactly 1."""
        return sum(self.uniform() for _ in range(12)) - 6.0


def harmonic_fit(series, dt_hours, constituents):
    """Least-squares fit of mean + cos/sin at the given constituent speeds.

    Returns (mean, [(name, amplitude, phase_lag_deg), ...]).
    The basis {1, cos(omega_i t), sin(omega_i t)} is *not* orthogonal over a
    finite record, which is exactly why the normal equations have to be solved
    rather than each constituent projected out independently.
    """
    n = len(series)
    speeds = [speed_cph(c[1]) for c in constituents]
    columns = [lambda i: 1.0]
    for f in speeds:
        columns.append(lambda i, f=f: math.cos(2.0 * math.pi * f * i * dt_hours))
        columns.append(lambda i, f=f: math.sin(2.0 * math.pi * f * i * dt_hours))

    size = len(columns)
    ata = [[0.0] * size for _ in range(size)]
    atb = [0.0] * size
    basis = [[col(i) for i in range(n)] for col in columns]
    for r in range(size):
        atb[r] = sum(basis[r][i] * series[i] for i in range(n))
        for c in range(r, size):
            val = sum(basis[r][i] * basis[c][i] for i in range(n))
            ata[r][c] = val
            ata[c][r] = val
    coeffs = gauss_solve(ata, atb)

    results = []
    for j, (name, _speed, _amp, _phase) in enumerate(constituents):
        a = coeffs[1 + 2 * j]
        b = coeffs[2 + 2 * j]
        phase = math.degrees(math.atan2(b, a)) % 360.0
        results.append((name, math.hypot(a, b), phase))
    return coeffs[0], results, ata, coeffs


def main():
    section("0. Constituent speeds, periods and the resolution they demand")
    print(f"{'name':>4} {'speed':>12} {'period (h)':>11} {'period (d)':>11}"
          f" {'freq (cyc/h)':>13}")
    for name, speed, _amp, _phase in CONSTITUENTS:
        freq = speed_cph(speed)
        print(f"{name:>4} {speed:>12.7f} {360.0 / speed:>11.5f}"
              f" {360.0 / speed / 24.0:>11.5f} {freq:>13.8f}")

    m2 = speed_cph(CONSTITUENTS[0][1])
    s2 = speed_cph(CONSTITUENTS[1][1])
    n2 = speed_cph(CONSTITUENTS[2][1])
    k2 = speed_cph(CONSTITUENTS[3][1])
    k1 = speed_cph(CONSTITUENTS[4][1])
    o1 = speed_cph(CONSTITUENTS[5][1])
    p1 = speed_cph(CONSTITUENTS[6][1])
    print("\nFrequency separations and the record length they require")
    print("(Rayleigh criterion: T > 1 / |f1 - f2|).")
    pairs = (("M2", m2, "S2", s2), ("M2", m2, "N2", n2),
             ("K1", k1, "O1", o1), ("M2", m2, "K2", k2), ("O1", o1, "P1", p1))
    for na, fa, nb, fb in pairs:
        sep = abs(fa - fb)
        print(f"  {na}-{nb}: |df| = {sep:.8f} cyc/h -> T > {1.0 / sep:8.2f} h"
              f" = {1.0 / sep / 24.0:6.3f} d")

    section("1. Orthogonality of cos and sin on one period")
    print("Numeric integrals over [0, 2*pi] with 20000 intervals:")
    for m, n_ in ((3, 3), (3, 5), (0, 0), (2, 2), (4, 7)):
        cm = trapz(lambda x: math.cos(m * x) * math.cos(n_ * x), 0.0, 2 * math.pi, 20000)
        sm = trapz(lambda x: math.sin(m * x) * math.sin(n_ * x), 0.0, 2 * math.pi, 20000)
        cs = trapz(lambda x: math.cos(m * x) * math.sin(n_ * x), 0.0, 2 * math.pi, 20000)
        print(f"  m = {m}, n = {n_}:  <cos,cos> = {cm: .6f}   <sin,sin> = {sm: .6f}"
              f"   <cos,sin> = {cs: .2e}")

    section("2. Square wave: coefficients 1/n and the Gibbs overshoot")
    print("f(t) = sign(sin t) = (4/pi) * sum_{odd n} sin(n t)/n")
    for terms in (1, 3, 9, 25, 99, 199):
        peak = 0.0
        step = 2.0 * math.pi / 200001
        for i in range(200001):
            t = i * step
            s = 0.0
            for n_ in range(1, terms + 1, 2):
                s += math.sin(n_ * t) / n_
            peak = max(peak, 4.0 / math.pi * s)
        print(f"  odd harmonics through n = {terms:>3}: max partial sum = {peak:.6f}"
              f"  overshoot = {peak - 1.0:+.6f}"
              f" = {100.0 * (peak - 1.0) / 2.0:6.3f}% of the jump (jump = 2)")
    print("  The overshoot does not shrink with more terms: it converges to a")
    print("  constant fraction of the jump (the Gibbs phenomenon).")

    section("3. A SYNTHETIC tide record: sampled hourly")
    dt = 1.0                       # hours
    for days in (14.0, 30.0, 60.0):
        n = int(days * 24.0)
        series = [model_h(i * dt) for i in range(n)]
        rng = max(series) - min(series)
        print(f"  {days:5.1f} d = {n:5d} samples: range = {rng:.3f} m,"
              f" df = 1/(N dt) = {1.0 / (n * dt):.8f} cyc/h"
              f"  (= 1/{n * dt:.1f} h)")

    days = 60.0
    n = int(days * 24.0)
    series = [model_h(i * dt) for i in range(n)]
    spectrum = dft(series)
    df = 1.0 / (n * dt)
    print(f"\n  Highest resolved frequency (Nyquist) = {1.0 / (2.0 * dt):.4f} cyc/h"
          f"  (period {2.0 * dt:.1f} h).")
    print("  Bin amplitudes 2|X[k]|/N nearest each constituent, 60-day record:")
    print(f"  {'name':>4} {'true f':>12} {'nearest bin':>12} {'|f - bin|':>12}"
          f" {'2|X|/N':>9} {'true A':>8}")
    for name, speed, amp, _phase in CONSTITUENTS:
        f0 = speed_cph(speed)
        kb = min(int(round(f0 / df)), n // 2)
        ampl = 2.0 * abs(spectrum[kb]) / n
        print(f"  {name:>4} {f0:>12.8f} {kb * df:>12.8f} {abs(f0 - kb * df):>12.8f}"
              f" {ampl:>9.4f} {amp:>8.3f}")
    print("  Where the constituent sits far from a bin, the bin amplitude is")
    print("  meaningless: the energy has leaked into neighbouring bins.")

    section("4. Least-squares harmonic analysis at the exact speeds")
    print("4a. Noise-free synthetic data (the model IS the data):")
    print(f"  {'record':>8} {'name':>4} {'true A':>8} {'fit A':>9} {'err':>9}"
          f" {'true phi':>9} {'fit phi':>9}")
    for days in (14.0, 60.0):
        n = int(days * 24.0)
        rec = [model_h(i * dt) for i in range(n)]
        _mean, fit, _ata, _c = harmonic_fit(rec, dt, CONSTITUENTS)
        for (name, amp, phase), (_n, _s, amp_t, phase_t) in zip(fit, CONSTITUENTS):
            print(f"  {days:>6.0f} d {name:>4} {amp_t:>8.3f} {amp:>9.4f}"
                  f" {abs(amp - amp_t):>9.5f} {phase_t:>9.1f} {phase:>9.2f}")
    print("  With no noise and an exactly invertible system, even a 14-day record")
    print("  recovers every constituent exactly.  Resolution is therefore NOT a")
    print("  statement about invertibility; it is a statement about noise gain.")
    print("  Note the phases are reported on [0, 360): -150 deg and 210 deg are the")
    print("  same angle, and tidal phases are conventionally quoted mod 360.")

    print("\n4b. Noise gain: formal standard error of each amplitude")
    print("  (white measurement noise with sigma = 0.0200 m; coefficient covariance")
    print("   sigma^2 * (A^T A)^-1 from the same normal matrix.  'Rayleigh' is the")
    print("   record length 1/|df| needed to separate that constituent from its")
    print("   nearest neighbour in the table.)")
    sigma = 0.02
    labels = ("14 d", "30 d", "60 d", "365 d")
    lengths = (14.0, 30.0, 60.0, 365.0)
    table = {}
    rayleigh = {}
    for days in lengths:
        n = int(days * 24.0)
        rec = [model_h(i * dt) for i in range(n)]
        _mean, _fit, ata, coeffs = harmonic_fit(rec, dt, CONSTITUENTS)
        table[days] = [amp_sigma(ata, coeffs, j, sigma)
                       for j in range(len(CONSTITUENTS))]
    for j, (name, speed, _a, _p) in enumerate(CONSTITUENTS):
        fj = speed_cph(speed)
        others = [abs(fj - speed_cph(c[1])) for k, c in enumerate(CONSTITUENTS) if k != j]
        rayleigh[name] = 1.0 / min(others) / 24.0
    header = f"  {'name':>4} {'A (m)':>7} {'Rayleigh d':>11}"
    for lab in labels:
        header += f" {lab + ' (mm)':>10}"
    print(header)
    for j, (name, _speed, amp, _p) in enumerate(CONSTITUENTS):
        row = f"  {name:>4} {amp:>7.3f} {rayleigh[name]:>11.1f}"
        for days in lengths:
            row += f" {1000.0 * table[days][j]:>10.2f}"
        print(row)
    print("  Relative to the constituent's own amplitude (per cent):")
    for j, (name, _speed, amp, _p) in enumerate(CONSTITUENTS):
        row = f"  {name:>4} {amp:>7.3f} {rayleigh[name]:>11.1f}"
        for days in lengths:
            row += f" {100.0 * table[days][j] / amp:>10.2f}"
        print(row)
    print("  The pattern follows the nearest-neighbour separation, not the size of")
    print("  the constituent: S2 and K2 differ by 0.082 deg/h (a 183-day beat), and")
    print("  K1 and P1 by the same amount, so those pairs dominate the uncertainty")
    print("  on any short record, while well-separated M2 and O1 are already good at")
    print("  14 days.  Rayleigh's 1/|df| is a convenient threshold, not a cliff; the")
    print("  exact quantity is the noise gain read off (A^T A)^-1.")

    print("\n4c. Monte-Carlo check of the prediction (24 noise realisations)")
    print("  The RMS of 24 samples carries its own ~14% random error, so ratios")
    print("  scattered about 1.0 by +/-30% are agreement; a systematic factor would")
    print("  mean the model of the noise or of the estimator was wrong.")
    print(f"  {'record':>8} {'name':>4} {'predicted':>10} {'observed':>10} {'ratio':>8}")
    for days, seed0 in ((14.0, 5000), (60.0, 7000)):
        n = int(days * 24.0)
        clean = [model_h(i * dt) for i in range(n)]
        _mean, _fit, ata, coeffs = harmonic_fit(clean, dt, CONSTITUENTS)
        predicted = [amp_sigma(ata, coeffs, j, sigma)
                     for j in range(len(CONSTITUENTS))]
        sums = [0.0] * len(CONSTITUENTS)
        trials = 24
        for t in range(trials):
            rng = Lcg(seed=seed0 + t)
            noisy = [clean[i] + sigma * rng.normal() for i in range(n)]
            _m2, fit, _ata2, _c2 = harmonic_fit(noisy, dt, CONSTITUENTS)
            for j, (_name, amp, _p) in enumerate(fit):
                sums[j] += (amp - CONSTITUENTS[j][2]) ** 2
        for j in range(len(CONSTITUENTS)):
            obs = math.sqrt(sums[j] / trials)
            print(f"  {days:>6.0f} d {CONSTITUENTS[j][0]:>4} {predicted[j]:>10.4f}"
                  f" {obs:>10.4f} {obs / predicted[j]:>8.2f}")
    print("  The prediction from the normal matrix reproduces the observed scatter,")
    print("  so the Rayleigh criterion and the noise gain can be used quantitatively")
    print("  in survey design rather than as a rule of thumb.")

    section("5. Spring-neap beat of M2 + S2")
    synodic_s2 = 1.0 / abs(m2 - s2)
    anomalistic = 1.0 / abs(m2 - n2)
    diurnal = 1.0 / abs(o1 - p1)
    print(f"  M2/S2 synodic (spring-neap) period = 1/{abs(m2 - s2):.8f}"
          f" = {synodic_s2:.2f} h = {synodic_s2 / 24.0:.3f} d")
    print(f"  M2/N2 anomalistic period            = {anomalistic:.2f} h"
          f" = {anomalistic / 24.0:.3f} d")
    print(f"  O1/P1 diurnal inequality period     = {diurnal:.2f} h"
          f" = {diurnal / 24.0:.3f} d")

    (n1, s1, a1, p1_) = CONSTITUENTS[0]
    (n2_, s2_, a2, p2_) = CONSTITUENTS[1]
    w1 = 2.0 * math.pi * speed_cph(s1)
    w2 = 2.0 * math.pi * speed_cph(s2_)
    ph1 = math.radians(p1_)
    ph2 = math.radians(p2_)

    def envelope(t):
        re = a1 * math.cos(w1 * t - ph1) + a2 * math.cos(w2 * t - ph2)
        im = a1 * math.sin(w1 * t - ph1) + a2 * math.sin(w2 * t - ph2)
        return math.hypot(re, im)

    step = 0.5
    span = 3.0 * synodic_s2
    total = int(span / step)
    env = [envelope(i * step) for i in range(total)]
    highs = [i for i in range(1, total - 1) if env[i] > env[i - 1] and env[i] >= env[i + 1]]
    print(f"  Envelope |A1 e^(i(w1 t - phi1)) + A2 e^(i(w2 t - phi2))|, step {step} h:")
    for i in highs[:5]:
        print(f"    t = {i * step:8.1f} h = {i * step / 24.0:6.3f} d   envelope = {env[i]:.4f} m")
    gaps = [highs[i + 1] * step - highs[i] * step for i in range(len(highs) - 1)]
    if gaps:
        mean_gap = sum(gaps) / len(gaps)
        print(f"  Mean gap between envelope maxima = {mean_gap:.3f} h"
              f" = {mean_gap / 24.0:.3f} d  (theory {synodic_s2 / 24.0:.3f} d)")
        print(f"  Envelope range = {min(env):.4f} to {max(env):.4f} m; the two")
        print(f"  predicted extremes are |A1 - A2| = {abs(a1 - a2):.3f} m and"
              f" A1 + A2 = {a1 + a2:.3f} m.")


if __name__ == "__main__":
    main()
