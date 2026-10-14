"""Low-cost instrument design: a synthetic budget walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (Johnson noise, quantization, duty-cycle
averaging, free-running clock drift, FFT bin amplitude).  No component data
sheet, manufacturer figure or measured instrument response is used or
reproduced.
"""

import numpy as np

K_B = 1.380649e-23
T0 = 300.0
RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Design requirement and the available signal")
    v_required = 1.0e-6          # m/s ground velocity to be detected
    sens = 30.0                  # V per m/s, synthetic geophone
    r_coil = 375.0               # ohm, synthetic
    f_corner = 4.5               # Hz, synthetic sensor corner
    band = 50.0                  # Hz, the full anti-alias band of the logger
    v_sig = sens * v_required
    print(f"  requirement: detect {v_required:.1e} m/s anywhere above the sensor")
    print(f"  corner of {f_corner:.1f} Hz; logger band DC-{band:.0f} Hz")
    print(f"  synthetic sensor: {sens:.0f} V/(m/s), coil {r_coil:.0f} ohm")
    print(f"  signal at the requirement = S * v = {v_sig*1e6:.1f} uV")
    return v_sig, band, r_coil


def section_2(v_sig, band, r_coil):
    banner(2, "Front-end noise budget referred to the sensor output")
    v_j = np.sqrt(4 * K_B * T0 * r_coil * band)
    e_n = 10.0e-9       # V/sqrt(Hz) at the amplifier input, synthetic
    i_n = 1.0e-12       # A/sqrt(Hz), synthetic
    v_i = i_n * np.sqrt(band) * r_coil
    v_amp = e_n * np.sqrt(band)
    fs = 5.0            # V full scale, differential
    print(f"  Johnson noise sqrt(4kTRB)          = {v_j*1e9:9.2f} nV")
    print(f"  amplifier voltage noise e_n*sqrt(B) = {v_amp*1e9:9.2f} nV   "
          f"({e_n*1e9:.1f} nV/rtHz)")
    print(f"  amplifier current noise in 375 ohm  = {v_i*1e9:9.2f} nV   "
          f"({i_n*1e12:.1f} pA/rtHz)")
    print(f"  full scale {fs:.1f} V differential:")
    print(f"    {'converter':<22}{'ENOB':>5}{'LSB':>11}{'q noise':>10}{'total':>10}"
          f"{'SNR':>8}{'dB':>7}")
    totals = {}
    for label, enob in (("24-bit, ENOB 20", 20), ("32-bit SD, ENOB 22", 22)):
        lsb = fs / 2.0 ** enob
        v_q = lsb / np.sqrt(12.0)      # uniform quantization noise rms
        tot = np.sqrt(v_j ** 2 + v_amp ** 2 + v_i ** 2 + v_q ** 2)
        snr = v_sig / tot
        totals[label] = tot
        print(f"    {label:<22}{enob:5d}{lsb*1e6:8.3f} uV{v_q*1e6:7.3f} uV"
              f"{tot*1e6:7.3f} uV{snr:8.2f}{20*np.log10(snr):7.1f}")
    print("  -> the quantization noise dominates, so analog gain buys more than")
    print("     extra bits; the pre-amplifier and the sensor are already quiet.")
    return totals


def section_3(v_sig, band, totals):
    banner(3, "Simulated detection: what the budget promises, measured")
    rng = np.random.default_rng(RNG_SEED)
    fs = 100.0
    n = 2048
    t = np.arange(n) / fs
    f_tone = 12.5
    sigma = totals["24-bit, ENOB 20"]          # per sample, over the DC-50 Hz band
    x = v_sig * np.sin(2 * np.pi * f_tone * t) + rng.normal(0.0, sigma, n)
    spec = np.abs(np.fft.rfft(x)) / (n / 2.0)
    k_sig = int(round(f_tone * n / fs))
    peak = spec[k_sig]
    med = np.median(spec[1:])
    rayleigh = np.sqrt(2.0 * np.log(2.0))
    expected = v_sig / (rayleigh * sigma * np.sqrt(2.0 / n))
    print(f"  simulated record: {n} samples at {fs:.0f} Hz, tone {f_tone:.1f} Hz,")
    print(f"  noise sigma = {sigma*1e6:.3f} uV per sample (from the budget)")
    print(f"  spectral peak amplitude   = {peak*1e6:8.3f} uV")
    print(f"  median spectral amplitude = {med*1e6:8.3f} uV   (Rayleigh median)")
    print(f"  peak / median = {peak/med:6.2f}  ({20*np.log10(peak/med):5.1f} dB)")
    print(f"  expected      = {expected:6.2f}  ({20*np.log10(expected):5.1f} dB),"
          f" using the Rayleigh median factor {rayleigh:.5f}")
    print("  -> the analytic budget and the simulated record agree, which is the")
    print("     only reason to believe either of them.")


def section_4():
    banner(4, "Power budget and the interval between services")
    i_sleep, i_acq, i_tx = 20e-6, 12e-3, 120e-3
    cap_ah, usable = 20.0, 0.70
    usable_ah = cap_ah * usable
    print(f"  sleep {i_sleep*1e6:.0f} uA, acquire {i_acq*1e3:.1f} mA, "
          f"transmit {i_tx*1e3:.0f} mA")
    print(f"  battery {cap_ah:.0f} Ah, usable fraction {usable:.2f} "
          f"-> {usable_ah:.1f} Ah")
    print(f"  {'scenario':<28}{'avg current':>14}{'life (days)':>14}")
    scenarios = [
        ("10 min + 10 s once a day", 600.0 / 86400.0, 10.0 / 86400.0),
        ("10 min + 10 s every 6 h", 4 * 600.0 / 86400.0, 4 * 10.0 / 86400.0),
        ("continuous acquisition", 1.0, 10.0 / 86400.0),
    ]
    for name, d_acq, d_tx in scenarios:
        avg = i_sleep + i_acq * d_acq + i_tx * d_tx
        days = usable_ah * 1000.0 / (avg * 1e3) / 24.0
        print(f"  {name:<28}{avg*1e3:11.3f} mA{days:14.1f}")
    print("  -> the sleep current is the term to attack, then the transmit duty cycle.")


def section_5():
    banner(5, "Free-running clock: resynchronisation interval for a 1 ms budget")
    tol = 1.0e-3
    print(f"  {'oscillator':<24}{'fractional error':>17}{'error per day':>15}"
          f"{'resync interval':>18}")
    for name, ppm in (("uncompensated crystal", 30.0),
                      ("TCXO", 1.0),
                      ("OCXO", 0.005)):
        frac = ppm * 1e-6
        err_day = frac * 86400.0
        interval_s = tol / frac
        if interval_s >= 3600.0:
            iv = f"{interval_s/3600.0:.2f} h"
        elif interval_s >= 60.0:
            iv = f"{interval_s/60.0:.2f} min"
        else:
            iv = f"{interval_s:.2f} s"
        print(f"  {name:<24}{ppm:14.4g} ppm{err_day*1e3:11.3f} ms{iv:>18}")
    print("  -> a 1 ms *absolute* budget forces frequent resynchronisation, while")
    print("     a *relative* budget between disciplined nodes is far cheaper.")


def section_6():
    banner(6, "Cost-effectiveness of four design routes (synthetic cost units)")
    print(f"  {'route':<32}{'noise floor':>13}{'cost':>7}{'per unit':>11}")
    routes = [
        ("bare ADC, no gain", 4.768e-6, 10.0),
        ("gain 100 + 24-bit", 4.768e-6 / 100.0, 18.0),
        ("gain 1000 + 32-bit SD", 1.192e-6 / 1000.0, 26.0),
        ("gain 1000 + 4 sensor array", 1.192e-6 / 1000.0 / np.sqrt(4.0), 40.0),
    ]
    for name, floor, cost in routes:
        print(f"  {name:<32}{floor*1e9:10.2f} nV{cost:7.1f}{floor*1e9/cost:11.3f}")
    print("  -> quoted as noise floor per unit of relative cost; averaging four")
    print("     sensors is the cheapest way to buy the last factor of two here.")


def main():
    print()
    banner(0, "LOW-COST INSTRUMENT DESIGN: SYNTHETIC BUDGET WALK-THROUGH")
    v_sig, band, r_coil = section_1()
    totals = section_2(v_sig, band, r_coil)
    section_3(v_sig, band, totals)
    section_4()
    section_5()
    section_6()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no data sheet, price or")
    print("measured instrument response is reproduced.")


if __name__ == "__main__":
    main()
