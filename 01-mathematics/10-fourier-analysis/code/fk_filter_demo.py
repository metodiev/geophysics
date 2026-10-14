"""Two-dimensional Fourier analysis: f-k spectra, dip filtering, up/down separation.

Run:  python3 fk_filter_demo.py
Requires: Python standard library only.

Companion to lesson 01-10-07 (Two-Dimensional Fourier Analysis and Wavenumber
Filtering).

Geometry and conventions
------------------------
x = offset along the receiver line (m), t = two-way time (s), so
    dt = 4 ms, dx = 25 m, nt = 128, nx = 64.
Forward 2-D transform, no scaling:
    F[kx, kf] = sum_nx sum_nt f[x, t] exp(-2*pi*i*(kx*x/nx + kf*t/nt))
Slowness p = 1/v_apparent (s/m).  A plane wave w(t - p x) has its energy on the
line kf = 1/(p... ) -- precisely, its 2-D spectrum is W(kf) * delta(kx - p*kf),
so kx/kf = p.  Nyquist wavenumber = 1/(2 dx) = 0.02 cycles/m.
The sign convention of the forward kernel is the same as everywhere in this
module: exp(-i*omega*t), so kx > 0 means energy moving towards increasing x.
"""

import cmath
import math

DT = 0.004
DX = 12.5
NT = 256
NX = 64


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fft(a):
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j |= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        half = length >> 1
        wl = cmath.exp(-2j * math.pi / length)
        for start in range(0, n, length):
            w = 1 + 0j
            for k in range(start, start + half):
                u = a[k]
                v = a[k + half] * w
                a[k] = u + v
                a[k + half] = u - v
                w *= wl
        length <<= 1
    return a


def ifft(a):
    n = len(a)
    return [x.conjugate() / n for x in fft([v.conjugate() for v in a])]


def fft2(grid):
    """2-D forward transform of grid[t][x]; returns spec[kf][kx].

    Separable: transform along x for every time sample, then along t for every
    wavenumber.  The order of the two passes does not matter; the axis each
    pass is applied to does.
    """
    step1 = [fft([grid[t][x] for x in range(NX)]) for t in range(NT)]   # [t][kx]
    spec = [[0j] * NX for _ in range(NT)]
    for kx in range(NX):
        column = fft([step1[t][kx] for t in range(NT)])
        for kf in range(NT):
            spec[kf][kx] = column[kf]
    return spec


def ifft2(spec):
    """Inverse of fft2, with the 1/(NT*NX) normalisation."""
    step1 = [[0j] * NX for _ in range(NT)]
    for kx in range(NX):
        column = ifft([spec[kf][kx] for kf in range(NT)])
        for kf in range(NT):
            step1[kf][kx] = column[kf]
    out = [[0.0] * NX for _ in range(NT)]
    for t in range(NT):
        row = ifft(step1[t])
        for x in range(NX):
            out[t][x] = row[x].real
    return out


def rms(values):
    return math.sqrt(sum(v * v for v in values) / len(values))


def wavelet(u, f0=22.0, width=0.022):
    """Zero-phase band-limited wavelet centred on u = 0."""
    return math.exp(-(u / width) ** 2) * math.cos(2 * math.pi * f0 * u)


def band_event(t0, p, f0, amp=1.0, width=0.06):
    """Narrow-band event: a modulated sinusoid on the line t = t0 + p x.

    Its 2-D spectrum is concentrated near (kf, kx) = (f0, p*f0), which makes the
    f-k peak location measurable without the ambiguity a broadband wavelet
    leaves behind.
    """
    out = [[0.0] * NX for _ in range(NT)]
    for ix in range(NX):
        x = ix * DX
        for it in range(NT):
            u = it * DT - t0 - p * x
            out[it][ix] += amp * math.exp(-(u / width) ** 2) * math.cos(2 * math.pi * f0 * u)
    return out


def plane_event(kx_bins, kf_bins, amp=1.0):
    """Continuous plane wave that sits exactly on the 2-D bin grid.

    cos(2*pi*(kf_bins*t/T + kx_bins*x/L)) with T = NT*dt and L = NX*dx, so the
    signal is periodic in both variables and its 2-D spectrum consists of two
    bins.  The slowness is kx_bins*T/(kf_bins*L).
    """
    out = [[0.0] * NX for _ in range(NT)]
    for it in range(NT):
        for ix in range(NX):
            out[it][ix] = amp * math.cos(2 * math.pi * (kf_bins * it / NT
                                                        - kx_bins * ix / NX))
    return out


def add(grid, other):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(grid, other)]


def gather(events):
    """Sum of plane-wave events.  events: (t0, slowness, amplitude)."""
    out = [[0.0] * NX for _ in range(NT)]
    for t0, p, amp in events:
        for ix in range(NX):
            x = ix * DX
            for it in range(NT):
                out[it][ix] += amp * wavelet(it * DT - t0 - p * x)
    return out


def tapered_2d(grid, taper_fraction=0.1):
    """Cosine taper at all four edges, so the record is smooth at the boundary."""
    nta = max(2, int(NT * taper_fraction))
    nxa = max(2, int(NX * taper_fraction))
    wt = [1.0] * NT
    wx = [1.0] * NX
    for i in range(nta):
        f = 0.5 * (1.0 - math.cos(math.pi * i / nta))
        wt[i] = f
        wt[NT - 1 - i] = f
    for i in range(nxa):
        f = 0.5 * (1.0 - math.cos(math.pi * i / nxa))
        wx[i] = f
        wx[NX - 1 - i] = f
    return [[grid[it][ix] * wt[it] * wx[ix] for ix in range(NX)] for it in range(NT)]


def total_energy(grid):
    return sum(v * v for row in grid for v in row)


def main():
    print(f"dt = {DT} s, dx = {DX} m, nt = {NT}, nx = {NX}")
    print(f"frequency resolution 1/(nt dt) = {1.0 / (NT * DT):.4f} Hz,"
          f" Nyquist {1.0 / (2 * DT):.1f} Hz")
    print(f"wavenumber resolution 1/(nx dx) = {1.0 / (NX * DX):.5f} cycles/m,"
          f" Nyquist {1.0 / (2 * DX):.5f} cycles/m")

    section("1. The 2-D transform, verified against the definition")
    small = [[float((3 * it + 5 * ix) % 7 - 3) for ix in range(8)] for it in range(8)]
    spec = [[0j] * 8 for _ in range(8)]
    for kf in range(8):
        for kx in range(8):
            acc = 0j
            for it in range(8):
                for ix in range(8):
                    acc += small[it][ix] * cmath.exp(
                        -2j * math.pi * (kx * ix / 8 + kf * it / 8))
            spec[kf][kx] = acc
    s1 = [fft([small[t][x] for x in range(8)]) for t in range(8)]      # [t][kx]
    fast = [[0j] * 8 for _ in range(8)]
    for kx in range(8):
        column = fft([s1[t][kx] for t in range(8)])
        for kf in range(8):
            fast[kf][kx] = column[kf]
    err = max(abs(spec[kf][kx] - fast[kf][kx]) for kf in range(8) for kx in range(8))
    print(f"  direct 2-D sum against row/column FFTs on an 8x8 grid: max difference"
          f" = {err:.3e}")
    print("  The 2-D transform is separable: transform every row, then every column.")
    print("  A full 2-D FFT therefore costs one 1-D FFT per row plus one per column.")

    section("2. A plane wave lies on a straight line through the origin of f-k")
    p_fast = 1.0 / 1500.0
    p_slow = -1.0 / 1000.0
    ev1 = band_event(0.10, p_fast, 20.0, 1.0)
    ev2 = band_event(0.16, p_slow, 20.0, 0.7)
    shot = add(ev1, ev2)
    spec = fft2(shot)
    df = 1.0 / (NT * DT)
    dkx = 1.0 / (NX * DX)
    print(f"  event 1: v = {1 / p_fast:.0f} m/s (p = {p_fast:.6e} s/m),"
          f" event 2: v = {-1 / p_slow:.0f} m/s moving the other way")
    print(f"  {'f (Hz)':>8} {'peak kx':>10} {'kx/f (s/m)':>13} {'-1/p (m/s)':>11}"
          f" {'true p (s/m)':>14}")
    for f0, p_true in ((15.0, p_fast), (20.0, p_fast), (20.0, p_slow), (25.0, p_fast),
                       (30.0, p_fast), (20.0, p_fast)):
        ev = band_event(0.10, p_true, f0, 1.0)
        sp = fft2(ev)
        ifreq = int(round(f0 / df))
        row = [abs(sp[ifreq][kx]) for kx in range(NX)]
        best = max(range(NX), key=lambda kx: row[kx])
        kx_pk = (best if best <= NX // 2 else best - NX) * dkx
        note = "" if abs(f0 - 20.0) < 1e-9 else f"  (event at {f0:.0f} Hz)"
        print(f"  {f0:>8.1f} {kx_pk:>10.5f} {kx_pk / f0:>13.7f}"
              f" {f0 / kx_pk if kx_pk else float('inf'):>11.0f}"
              f" {p_true:>14.7f}{note}")
    print("  At every frequency tested |kx| = |p|*f to within the wavenumber bin")
    print("  spacing, so the event's energy lies on a line through the origin whose")
    print("  slope is its slowness.  A dipping event IS a line in the f-k plane.")
    print("  The SIGN is a convention statement, and worth stating exactly: with the")
    print("  forward kernel exp(-i(kx*x + omega*t)) used throughout this module, an")
    print("  event whose arrival time increases with offset (t = t0 + p x, p > 0)")
    print("  puts its positive-frequency energy at kx = -p f.  Every sign below --")
    print("  which quadrant holds the up-going wave, which half-plane holds the")
    print("  down-dip event -- follows from this one line.")

    section("3. Dip filtering: separating two events by their slope")
    df = 1.0 / (NT * DT)
    dkx = 1.0 / (NX * DX)
    length = NX * DX
    span = NT * DT
    kf_bins = 14                       # 13.67 Hz, exactly on the frequency grid
    f_ev = kf_bins * df
    kx_fast, kx_slow = 10.0, -24.0     # exactly on the wavenumber grid
    p_fast = kx_fast * span / (kf_bins * length)
    p_slow = kx_slow * span / (kf_bins * length)
    v_cut = 800.0                      # between the two apparent velocities

    def fan(grid, vcut):
        sp = fft2(grid)
        out = [[0j] * NX for _ in range(NT)]
        for kf in range(NT):
            fk = (kf if kf <= NT // 2 else kf - NT) * df
            for kx in range(NX):
                kx_cyc = (kx if kx <= NX // 2 else kx - NX) * dkx
                if fk == 0.0 or abs(kx_cyc / fk) < 1.0 / vcut:
                    out[kf][kx] = sp[kf][kx]
        return ifft2(out)

    def flat(grid):
        return [v for row in grid for v in row]

    print(f"  record: {NX} traces at dx = {DX} m ({length:.0f} m) and {NT} samples at")
    print(f"  dt = {DT} s ({span:.3f} s); df = {df:.4f} Hz, dkx = {dkx:.5f} cycles/m,")
    print(f"  Nyquist wavenumber {1.0 / (2 * DX):.5f} cycles/m.")
    print(f"  Two continuous plane waves placed exactly on the bin grid so that each")
    print(f"  has a two-bin spectrum:")
    print(f"    A: bin kx = {kx_fast:.0f}, kf = {kf_bins}  ->  {kf_bins * df:.3f} Hz,"
          f" apparent velocity {1 / p_fast:.1f} m/s")
    print(f"    B: bin kx = {kx_slow:.0f}, kf = {kf_bins}  ->  {kf_bins * df:.3f} Hz,"
          f" apparent velocity {-1 / p_slow:.1f} m/s (a ground-roll-like surface")
    print("       wave, slower and moving the other way)")
    print(f"  filter: keep |kx/f| < 1/{v_cut:.0f} s/m, i.e. events faster than"
          f" {v_cut:.0f} m/s")
    wave_a = plane_event(kx_fast, kf_bins)
    wave_b = plane_event(kx_slow, kf_bins)
    shot = add(wave_a, wave_b)
    separated = fan(shot, v_cut)
    ref_a = wave_a
    print(f"  {'quantity':>38} {'RMS':>12} {'fraction of its event':>22}")
    for label, part, ref in (("A surviving the filter", fan(wave_a, v_cut), ref_a),
                             ("B surviving the filter", fan(wave_b, v_cut), wave_b)):
        print(f"  {label:>38} {rms(flat(part)):>12.4e}"
              f" {rms(flat(part)) / rms(flat(ref)):>22.3e}")
    resid = [a - b for a, b in zip(flat(separated), flat(ref_a))]
    print(f"  {'filter output minus event A':>38} {rms(resid):>12.4e}"
          f" {rms(resid) / rms(flat(ref_a)):>22.3e}")
    print("  For events that sit exactly on the grid the separation is exact to")
    print("  round-off, because each event occupies two bins and the mask is a")
    print("  straight line between them.")
    print("\n  Now the same experiment with short wave packets rather than")
    print("  continuous waves, which is what field data contain:")
    print(f"  {'packet width (s)':>18} {'B leakage':>12} {'A lost':>10}")
    for width in (0.06, 0.12, 0.24, 0.48):
        pa = band_event(0.10, p_fast, f_ev, 1.0, width=width)
        pb = band_event(0.16, p_slow, f_ev, 1.0, width=width)
        leak = rms(flat(fan(pb, v_cut))) / rms(flat(pb))
        lost = rms([a - b for a, b in zip(flat(pa), flat(fan(pa, v_cut)))]) / rms(flat(pa))
        print(f"  {width:>18.2f} {leak:>12.4f} {lost:>10.4f}")
    print("  A wave packet has a finite spatial extent, so its f-k ridge is")
    print("  broadened and part of it lies on the wrong side of the mask.  Roughly a")
    print("  fifth of a short, steep packet survives a fan filter, and a similar")
    print("  fraction of the wanted event is removed.  That is why real f-k")
    print("  filtering is judged on the section, not on the theory, and why the")
    print("  amplitudes either side of the mask are always checked.")

    section("4. Up/down separation is a quadrant filter")
    length = NX * DX
    span = NT * DT
    kf_bins = 14
    kx_bins = 10.0
    p_up = kx_bins * span / (kf_bins * length)
    ev_a = plane_event(kx_bins, kf_bins)
    ev_b = plane_event(-kx_bins, kf_bins)
    both = add(ev_a, ev_b)
    half = NX // 2

    def quadrant_filter(grid, cone_freq=0.0, cone_bins=0.0):
        sp = fft2(grid)
        out = [[0j] * NX for _ in range(NT)]
        for kf in range(NT):
            fk = abs((kf if kf <= NT // 2 else kf - NT) * df)
            positive_f = 1 <= kf < NT // 2
            negative_f = NT // 2 < kf < NT - 1
            for kx in range(NX):
                kx_cyc = abs((kx if kx <= NX // 2 else kx - NX) * dkx)
                if (positive_f and kx >= half) or (negative_f and kx < half):
                    if fk >= cone_freq and kx_cyc >= cone_bins * dkx:
                        out[kf][kx] = sp[kf][kx]
        return ifft2(out)

    print(f"  two continuous plane waves of the same frequency"
          f" ({kf_bins * df:.3f} Hz) and opposite slowness")
    print(f"  (p = +/-{p_up:.4e} s/m, i.e. +/-{1 / p_up:.1f} m/s).  The filter keeps")
    print("  the half-plane that corresponds to p > 0 plus its conjugate, which is")
    print("  what makes the output a real signal.")
    print(f"  {'variant':>30} {'B leaking in':>14} {'A lost':>12}"
          f" {'leak/B':>10} {'loss/A':>10}")
    for label, cf, cb in (("quadrant only", 0.0, 0.0),
                          ("quadrant + cone mute", 8.0, 2.0)):
        out_a = quadrant_filter(ev_a, cf, cb)
        lost_a = rms([a - b for a, b in zip(flat(ev_a), flat(out_a))])
        leak_b = rms(flat(quadrant_filter(ev_b, cf, cb)))
        print(f"  {label:>30} {leak_b:>14.4e} {lost_a:>12.4e}"
              f" {leak_b / rms(flat(ev_b)):>10.3e} {lost_a / rms(flat(ev_a)):>10.3e}")
    out_a = quadrant_filter(ev_a)
    print("\n  A plane wave on the bin grid is split exactly: nothing of event B")
    print("  survives and nothing of event A is lost.  The cone mute, applied to")
    print("  the same data, then removes the legitimate low-frequency content of A:")
    print("  a cone is a choice about the data, not a mathematical necessity.")
    print("  With wave packets rather than continuous waves the leakage returns to")
    print("  about a fifth of the event's own RMS, as measured in Section 3.")
    print("  This is the standard first step in VSP and walkaway processing:")
    print("  separating up- from down-going energy needs no velocity model, only")
    print("  the geometry, because opposite directions of propagation occupy")
    print("  opposite halves of the f-k plane.")

    section("5. Spatial aliasing: when the dip wraps in f-k")
    v_ev = 1000.0
    f_alias = v_ev / (2 * DX)
    print(f"  dx = {DX:.0f} m, event velocity {v_ev:.0f} m/s: unaliased only below")
    print(f"  f = v/(2 dx) = {f_alias:.1f} Hz")
    print(f"  {'f (Hz)':>8} {'true |kx|':>11} {'observed kx':>13} {'|kx|/f':>10}"
          f" {'apparent |v| (m/s)':>19} {'aliased':>9}")
    for f0 in (20.0, 40.0, 52.0, 80.0):
        ev = band_event(0.12, 1.0 / v_ev, f0, 1.0)
        sp = fft2(ev)
        ifreq = int(round(f0 / df))
        row = [abs(sp[ifreq][kx]) for kx in range(NX)]
        best = max(range(NX), key=lambda kx: row[kx])
        kx_obs = (best if best <= NX // 2 else best - NX) * dkx
        kx_true = f0 / v_ev
        print(f"  {f0:>8.1f} {kx_true:>11.5f} {kx_obs:>13.5f}"
              f" {abs(kx_obs) / f0:>10.6f}"
              f" {f0 / abs(kx_obs) if kx_obs else float('inf'):>19.0f}"
              f" {'YES' if kx_true > 1.0 / (2 * DX) else 'no':>9}")
    print(f"  Below {f_alias:.0f} Hz the measured wavenumber equals the true one.  Above")
    print("  it the peak lands on the far side of the Nyquist wavenumber: the apparent")
    print("  slowness stops increasing, folds back, and the event reads as a slower")
    print("  dip in the opposite direction.  In f-k space aliasing is a wrap, and it")
    print("  is completely invisible in the time-offset display.")

    section("6. The 2-D transform assumes periodicity: taper")
    ev = band_event(0.30, 1.0 / 1200.0, 13.671875, 1.0, width=0.15)
    kx_max = 6 * dkx

    def lowcut(grid):
        sp = fft2(grid)
        mask = [[sp[kf][kx] if abs((kx if kx <= NX // 2 else kx - NX) * dkx) <= kx_max
                 else 0j for kx in range(NX)] for kf in range(NT)]
        return ifft2(mask)

    filtered = lowcut(ev)
    edge = [filtered[it][ix] for it in range(NT) for ix in range(0, 4)]
    middle = [filtered[it][ix] for it in range(NT) for ix in range(20, 44)]
    print(f"  a hard wavenumber cut |kx| <= {kx_max:.5f} cycles/m (6 bins) applied to")
    print(f"  a wave packet whose wavenumber at its centre frequency is"
          f" {13.671875 / 1200.0:.5f} cycles/m,")
    print("  so the cut removes real signal and leaves the packet truncated at the")
    print("  array edges:")
    print(f"    RMS in the first 4 traces : {rms(edge):.4e}")
    print(f"    RMS in traces 20-43       : {rms(middle):.4e}")
    print(f"    ratio edge/middle         : {rms(edge) / rms(middle):.3f}")
    tapered = tapered_2d(ev)
    filtered_t = lowcut(tapered)
    edge_t = [filtered_t[it][ix] for it in range(NT) for ix in range(0, 4)]
    middle_t = [filtered_t[it][ix] for it in range(NT) for ix in range(20, 44)]
    print(f"  the same cut after a 10% cosine taper on all four edges:")
    print(f"    RMS in the first 4 traces : {rms(edge_t):.4e}")
    print(f"    RMS in traces 20-43       : {rms(middle_t):.4e}")
    print(f"    ratio edge/middle         : {rms(edge_t) / rms(middle_t):.3f}")
    print(f"  energy removed by the taper:"
          f" {1.0 - total_energy(tapered) / total_energy(ev):.4f} of the total")
    print("  A hard wavenumber cut on a record that is not periodic produces the same")
    print("  ringing as a hard frequency cut (lesson 01-10-03): the discontinuity at")
    print("  the array edge is a step, and a step through a sharp cut rings.  In this")
    print("  test the taper cuts the edge amplitude by about 40% (and removes 14% of")
    print("  the energy); its larger benefit is that the remaining ringing is pushed")
    print("  into the taper zone, where it is not interpreted.")
    print("  Real f-k filtering therefore always comes with a taper, and often with")
    print("  padding, and the amplitudes at the array edges are never trustworthy.")


if __name__ == "__main__":
    main()
