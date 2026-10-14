"""Fibre-optic sensing and distributed acoustic sensing (DAS).

Run:  python3 fibre_optics_sensing_demo.py
Requires: Python standard library only.

Companion to lesson 02-10-05.

The script:

1. Recomputes the step-index fibre parameters on which every fibre sensor
   rests: numerical aperture, V number, single-mode cutoff and mode count.
2. Computes Rayleigh scattering loss, its lambda^-4 scaling, and the
   two-way attenuation of a fibre-optic measurement loop, in Np and in dB.
3. Computes the Rayleigh backscatter level captured in the backward mode,
   deriving the recapture fraction from the numerical aperture and comparing
   it with the commonly used value.
4. Computes the spatial resolution of an OTDR/DAS measurement from the pulse
   width and from the sampling rate.
5. Computes the phase-to-strain sensitivity of a single-mode fibre from the
   strain-optic coefficients, and converts a seismic particle velocity into
   a strain and then into an optical phase shift.
6. Computes the gauge-length spatial response of a DAS channel: the spatial
   transfer function, its first null and its 3 dB frequency.
7. Computes the channel-spacing Nyquist limit and the maximum pulse
   repetition rate set by the round-trip time, i.e. the sampling rate limit
   of a single-ended DAS.
8. Computes the temperature cross-sensitivity and expresses it in microstrain
   equivalent, the number that decides whether a DAS temperature change can
   be mistaken for strain.

The refractive index, strain-optic and thermo-optic coefficients are nominal
values for silica fibre at 1550 nm.  A real measurement must use the fibre
manufacturer's data sheet and an in-situ calibration; the numbers here are
order-of-magnitude and are labelled as such.
"""

import math

C = 299792458.0        # m/s, exact
N_CORE = 1.4504        # nominal phase index of the GeO2-doped core at 1550 nm
N_CLAD = 1.4447        # nominal phase index of the pure-silica cladding
N_GROUP = 1.4682       # nominal group index at 1550 nm (sets propagation speed)
LAMBDA = 1550e-9       # m
CORE_RADIUS = 4.1e-6   # m
V_SINGLE_MODE = 2.4048

# Strain-optic coefficients and Poisson ratio of fused silica (nominal).
P11 = 0.121
P12 = 0.270
NU = 0.17

# Thermo-optic and thermal-expansion coefficients of silica (nominal).
DN_DT = 1.1e-5         # 1/K
ALPHA_T = 5.5e-7       # 1/K

# Fibre loss, nominal for standard single-mode fibre at 1550 nm.
LOSS_DB_PER_KM = 0.2
LOSS_NP_PER_M = LOSS_DB_PER_KM / (10.0 / math.log(10.0)) / 1000.0
RECAPTURE = 1.5e-3     # nominal Rayleigh backscatter recapture fraction


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def db(x):
    return 10.0 * math.log10(x)


def part1_geometry():
    section("1. Fibre geometry and the single-mode condition")
    NA = math.sqrt(N_CORE ** 2 - N_CLAD ** 2)
    V = 2.0 * math.pi * CORE_RADIUS / LAMBDA * NA
    lambda_c = 2.0 * math.pi * CORE_RADIUS * NA / V_SINGLE_MODE
    print(f"  n_core = {N_CORE}, n_clad = {N_CLAD}, a = {CORE_RADIUS * 1e6:.2f} um,"
          f" lambda = {LAMBDA * 1e9:.0f} nm")
    print(f"  NA = {NA:.6f}, acceptance half-angle in air = "
          f"{math.degrees(math.asin(NA)):.4f} deg")
    print(f"  V  = {V:.4f} (single mode below {V_SINGLE_MODE})")
    print(f"  cutoff lambda_c = {lambda_c * 1e9:.1f} nm")
    print(f"  propagation speed = c/n_group = {C / N_GROUP:.6e} m/s")
    print()
    print("  One spatial mode means one optical phase at the far end.  Every")
    print("  phase-based sensor depends on that: a multimode fibre carries")
    print("  several modes with different group delays, and interferometry")
    print("  between them produces speckle rather than a single phase.")


def part2_loss():
    section("2. Rayleigh scattering, the lambda^-4 law and the loss budget")
    print(f"  Nominal attenuation at 1550 nm: {LOSS_DB_PER_KM:.2f} dB/km = "
          f"{LOSS_NP_PER_M * 1e3:.5f} Np/km")
    print()
    print("  Rayleigh scattering is proportional to lambda^-4, so the ratio of")
    print("  the scattering loss at two wavelengths is (lambda_2/lambda_1)^4:")
    print()
    print(f"{'wavelength (nm)':>17}{'scattering ratio vs 1550 nm':>30}")
    for lam_nm in (850.0, 1064.0, 1310.0, 1550.0, 1625.0):
        print(f"{lam_nm:>17.0f}{(1550.0 / lam_nm) ** 4:>30.3f}")
    print()
    print("  At 850 nm the Rayleigh loss is larger than at 1550 nm by a factor")
    print(f"  of {(1550.0 / 850.0) ** 4:.2f}, so raising the wavelength is the cheapest way")
    print("  to reduce scattering loss.  It is not free: the infrared absorption")
    print("  bands of silica climb steeply beyond about 1600 nm, which is why the")
    print("  practical window is 1300-1600 nm and the loss minimum is near 1550.")
    print()
    print("  Loss budget of a sensing loop, in dB and as a surviving fraction:")
    print()
    print(f"{'one-way length (km)':>21}{'one-way (dB)':>14}"
          f"{'round trip (dB)':>18}{'round-trip fraction':>22}")
    for km in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0):
        one = LOSS_DB_PER_KM * km
        print(f"{km:>21.1f}{-one:>14.2f}{-2 * one:>18.2f}"
              f"{10 ** (-2 * one / 10):>22.3e}")
    print()
    print("  A 10 km loop returns 4 dB down, i.e. 40 per cent of the launched")
    print("  power has been absorbed before the backscatter has even been")
    print("  generated.  This is the first term in any DAS range budget and it")
    print("  is why long-range DAS needs a high launch power and a low-noise")
    print("  coherent receiver rather than a clever pulse shape.")


def part3_rbs():
    section("3. Rayleigh backscatter: how much comes back")
    NA = math.sqrt(N_CORE ** 2 - N_CLAD ** 2)
    theta = math.asin(NA / N_CORE)
    s_geom = theta ** 2 / 4.0
    print("  Only the fraction of the Rayleigh-scattered light that is captured")
    print("  by the backward-propagating guided mode is measured.  For isotropic")
    print("  scattering and a small numerical aperture, that fraction is the")
    print("  backward acceptance solid angle divided by 4 pi:")
    print()
    print(f"    theta_max in the core = asin(NA/n1) = {math.degrees(theta):.4f} deg"
          f" = {theta:.6f} rad")
    print(f"    S ~ theta_max^2/4 = {s_geom:.4e}")
    print()
    print(f"  This order-of-magnitude derivation gives S ~ {s_geom:.1e}.  The")
    print("  geometric estimate is a consistency check, not a substitute for a")
    print("  measurement: isotropic scattering is an idealisation, and the")
    print("  real capture fraction also depends on the anisotropy of Rayleigh")
    print("  scattering and on the polarisation of the modes.  This demo adopts")
    print(f"  S = {RECAPTURE:.1e} and states it as an adopted parameter, not a")
    print("  computed one: take it from the fibre data sheet, or calibrate it.")
    print()
    print("  Single-ended backscattered power for a rectangular pulse of width W,")
    print("  relative to the launched power:")
    print("    P_bs/P0 = S * alpha * (v W / 2) * exp(-2 alpha L)")
    print(f"  with alpha = {LOSS_NP_PER_M * 1e3:.5f} Np/km and v = {C / N_GROUP:.4e} m/s.")
    print()
    print(f"{'W (ns)':>8}{'scattering length (m)':>23}{'level at 0 km (dB)':>21}"
          f"{'level at 10 km (dB)':>22}")
    for W_ns in (5.0, 10.0, 20.0, 50.0, 100.0):
        W = W_ns * 1e-9
        length = C / N_GROUP * W / 2.0
        ratio0 = RECAPTURE * LOSS_NP_PER_M * length
        for L_km in (10.0,):
            pass
        ratio10 = ratio0 * math.exp(-2 * LOSS_NP_PER_M * L_km * 1000.0)
        print(f"{W_ns:>8.1f}{length:>23.4f}{db(ratio0):>21.2f}"
              f"{db(ratio10):>22.2f}")
    print()
    print("  The backscatter is 60-80 dB below the launched power, i.e. seven to")
    print("  eight orders of magnitude.  That is the fundamental reason DAS is a")
    print("  weak-signal technique: the useful signal is a phase modulation on a")
    print("  carrier that is eight orders of magnitude weaker than the pulse")
    print("  that created it, and a longer pulse buys signal at the cost of")
    print("  resolution.")


def part4_resolution():
    section("4. Spatial resolution: pulse width and sampling rate")
    v = C / N_GROUP
    print(f"  Round-trip mapping: a pulse of width W occupies W*v/2 of fibre, so")
    print(f"  the spatial resolution is dz = v W/2 = {v / 2:.4e} x W.")
    print()
    print(f"{'W (ns)':>8}{'dz = vW/2 (m)':>16}{'PRF limit for 10 km (Hz)':>26}")
    for W_ns in (5.0, 10.0, 20.0, 50.0, 100.0, 200.0):
        dz = v * (W_ns * 1e-9) / 2.0
        print(f"{W_ns:>8.1f}{dz:>16.3f}{v / (2 * 10e3):>26.1f}")
    print()
    print("  The pulse width sets the *resolution*; the round-trip time sets the")
    print("  maximum repetition rate, i.e. the bandwidth of the acquisition.")
    print("  The two are independent: a 5 ns pulse resolves better but does not")
    print("  let the system fire faster, because the fibre still has to be")
    print("  traversed twice by light.")
    print()
    print(f"{'fibre length (km)':>19}{'round trip (ms)':>18}"
          f"{'max pulse rate (Hz)':>22}")
    rate = None
    for km in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0):
        rt = 2 * km * 1000.0 / v
        print(f"{km:>19.1f}{rt * 1e3:>18.4f}{1.0 / rt:>22.1f}")
    print()
    print("  At 100 MS/s the receiver samples one metre every 10 ns, which is")
    print("  finer than any practical pulse; the useful resolution is therefore")
    print("  set by the pulse, and the sampling rate is chosen to oversample it.")
    print()
    print("  Number of independent sensing channels, at a stated channel")
    print("  spacing, on a 10 km fibre:")
    print()
    print(f"{'spacing (m)':>13}{'channels':>10}{'spatial Nyquist k (rad/m)':>27}"
          f"{'f_Nyquist at 3000 m/s (Hz)':>28}")
    for dx in (0.5, 1.0, 2.0, 5.0):
        kn = math.pi / dx
        print(f"{dx:>13.1f}{10000.0 / dx:>10.0f}{kn:>27.4f}"
              f"{kn * 3000.0 / (2 * math.pi):>28.1f}")
    print()
    print("  Ten thousand channels at 1 m spacing on a single cable is the")
    print("  defining capability of DAS: it is an array of strain gauges that")
    print("  needs no downhole electronics and no clamping, because the fibre")
    print("  *is* the sensor.")


def part5_phase_strain():
    section("5. Phase-to-strain sensitivity of a single-mode fibre")
    xi = 1.0 - 0.5 * N_CORE ** 2 * (P12 - NU * (P11 + P12))
    print("  The optical phase is phi = 2 pi n L / lambda.  Straining the fibre")
    print("  changes L and, through the strain-optic effect, n:")
    print()
    print("    Delta phi / phi = [ 1 - (n^2/2)(p12 - nu(p11 + p12)) ] * epsilon")
    print()
    print(f"  p11 = {P11}, p12 = {P12}, nu = {NU}, n = {N_CORE}")
    print(f"  xi = 1 - (n^2/2)(p12 - nu(p11+p12)) = {xi:.6f}")
    print(f"  (the commonly quoted value for silica is about 0.78)")
    print()
    per_m = 2.0 * math.pi * N_CORE * xi / LAMBDA
    print(f"  phase change per metre per unit strain = 2 pi n xi/lambda =")
    print(f"    {per_m:.4e} rad per metre per unit strain")
    print()
    print(f"{'gauge length L (m)':>20}{'rad per 1 nstrain':>20}"
          f"{'deg per 1 nstrain':>20}{'rad per 1 ustrain':>20}")
    for L in (1.0, 5.0, 10.0, 20.0, 40.0):
        print(f"{L:>20.1f}{per_m * L * 1e-9:>20.5f}"
              f"{math.degrees(per_m * L * 1e-9):>20.4f}{per_m * L * 1e-6:>20.5f}")
    print()
    print("  A one nanometre-per-metre strain over a 10 m gauge gives a phase")
    print(f"  change of {per_m * 10 * 1e-9:.4f} rad, about "
          f"{math.degrees(per_m * 10 * 1e-9):.2f} degrees.  Phase is measured")
    print("  interferometrically to milliradians, so DAS detects strain of order")
    print("  1e-11 — five orders of magnitude below the elastic limit of rock.")
    print()
    print("  Converting ground motion to strain: for a plane wave of phase")
    print("  velocity c the strain is epsilon = v/c, so:")
    print()
    print(f"{'particle velocity (mm/s)':>25}{'c (m/s)':>10}{'strain':>13}"
          f"{'phase over 10 m (rad)':>23}")
    for v_mm in (0.01, 0.1, 1.0, 10.0):
        for c in (1500.0, 3000.0):
            eps = (v_mm * 1e-3) / c
            print(f"{v_mm:>25.2f}{c:>10.0f}{eps:>13.3e}"
                  f"{per_m * 10.0 * eps:>23.4f}")
    print()
    print(f"  Typical seismic ground motion of 0.01-1 mm/s at 3000 m/s gives strains")
    print(f"  of {0.01e-3 / 3000.0:.2e} to {1.0e-3 / 3000.0:.2e} and phase signals of")
    print(f"  {per_m * 10.0 * 0.01e-3 / 3000.0:.3f} to {per_m * 10.0 * 1.0e-3 / 3000.0:.1f} rad over a 10 m gauge — enormous by")
    print("  interferometric standards.  That is why DAS recordings saturate in")
    print("  the near field of a seismic source while remaining sensitive to")
    print("  microseisms kilometres away, and why the dynamic range of the")
    print("  measurement, not its sensitivity, is usually the limiting factor.")


def part6_gauge():
    section("6. The gauge length is a spatial filter")
    print("  A DAS channel reports the strain averaged over the gauge length L,")
    print("  which convolves the strain field with a boxcar.  For a sinusoidal")
    print("  strain field of spatial wavelength Lambda the response is")
    print("    |sinc(pi L / Lambda)| = |sin(pi L/Lambda)/(pi L/Lambda)|,")
    print("  so the channel is blind to wavelengths that fit a whole number of")
    print("  half-cycles in the gauge.")
    print()
    print(f"{'gauge L (m)':>13}{'first null Lambda (m)':>23}"
          f"{'first null f, v=3000 (Hz)':>28}{'3 dB f, v=3000 (Hz)':>22}")
    for L in (1.0, 2.0, 5.0, 10.0, 20.0, 40.0):
        null_lam = L
        f_null = 3000.0 / null_lam
        x3 = 1.3915573724      # sinc(x) = 1/sqrt(2)
        f3 = x3 * 3000.0 / (math.pi * L)
        print(f"{L:>13.1f}{null_lam:>23.2f}{f_null:>28.1f}{f3:>22.1f}")
    print()
    print("  The response over a range of frequencies for a 10 m gauge in rock")
    print("  with v = 3000 m/s:")
    print()
    print(f"{'f (Hz)':>9}{'Lambda (m)':>13}{'L/Fambda':>11}{'response':>12}"
          f"{'response (dB)':>15}")
    L = 10.0
    for f in (1.0, 5.0, 10.0, 30.0, 100.0, 150.0, 300.0, 600.0):
        lam = 3000.0 / f
        x = math.pi * L / lam
        ratio = L / lam
        at_null = abs(ratio - round(ratio)) < 1e-9 and ratio > 0
        r = 0.0 if at_null else abs(math.sin(x) / x)
        text = "   -inf" if at_null else f"{db(r):15.2f}"
        print(f"{f:>9.1f}{lam:>13.1f}{ratio:>11.3f}{r:>12.4f}{text}")
    print()
    print("  This is the single most important instrument-response correction in")
    print("  DAS processing.  A gauge of 10 m has a 3 dB point near 133 Hz and a")
    print("  null at 300 Hz for a 3000 m/s wave; recording the same event with a")
    print("  5 m gauge moves both to 266 Hz and 600 Hz.  Comparing amplitudes")
    print("  across gauges without applying this filter is comparing two")
    print("  different instruments.")


def part7_limits():
    section("7. Repetition rate, aliasing and channel spacing")
    print("  A single-ended DAS cannot launch a second pulse before the first has")
    print("  returned, so the pulse repetition frequency is f_prf = v/(2L), and")
    print("  that is also the temporal sampling rate of the recording.")
    print()
    print(f"{'range (km)':>12}{'f_prf = v/(2L) (Hz)':>22}"
          f"{'Nyquist = f_prf/2 (Hz)':>24}")
    v = C / N_GROUP
    for km in (1.0, 2.0, 5.0, 10.0, 20.0):
        f_prf = v / (2 * km * 1000.0)
        print(f"{km:>12.1f}{f_prf:>22.1f}{f_prf / 2:>24.1f}")
    print()
    print("  A 10 km single-ended system samples at about 10 kHz and is Nyquist-")
    print("  limited to about 5 kHz.  That is ample for seismic and microseismic")
    print("  work and short of the 10-100 kHz range of acoustic emission and")
    print("  ultrasound, for which a shorter fibre or a chirped-pulse scheme is")
    print("  needed.  Aliasing in DAS is not a subtle failure: an event above the")
    print("  Nyquist frequency appears at a wrong frequency with full amplitude.")
    print()
    print("  The spatial analogue: channels spaced dx apart can represent")
    print("  spatial wavenumbers only up to pi/dx, which is a maximum frequency")
    print("  of v/(2 dx).")
    print()
    print(f"{'dx (m)':>8}{'max wavenumber (rad/m)':>25}"
          f"{'max f, v=3000 (Hz)':>21}{'max f, v=1500 (Hz)':>21}")
    for dx in (0.25, 0.5, 1.0, 2.0, 5.0):
        k = math.pi / dx
        print(f"{dx:>8.2f}{k:>25.4f}{k * 3000.0 / (2 * math.pi):>21.1f}"
              f"{k * 1500.0 / (2 * math.pi):>21.1f}")
    print()
    print("  With 1 m spacing, waves faster than 3000 m/s at frequencies below")
    print("  1500 Hz are unaliased; slow surface waves at 200 m/s alias above")
    print("  100 Hz unless the channel spacing is reduced.  Channel spacing, not")
    print("  gauge length, sets the spatial Nyquist limit, and the two are set")
    print("  independently in the instrument configuration.")


def part8_temperature():
    section("8. Temperature cross-sensitivity")
    print("  Temperature changes the phase through thermal expansion and through")
    print("  the thermo-optic effect: (1/phi) dphi/dT = alpha_T + (1/n) dn/dT.")
    print()
    alpha_eff = ALPHA_T + DN_DT / N_CORE
    per_m_K = 2.0 * math.pi * N_CORE / LAMBDA * alpha_eff
    print(f"  alpha_T            = {ALPHA_T:.2e} /K  (thermal expansion, nominal)")
    print(f"  (1/n) dn/dT        = {DN_DT / N_CORE:.4e} /K  (thermo-optic, nominal)")
    print(f"  sum                = {alpha_eff:.4e} /K")
    xi = 1.0 - 0.5 * N_CORE ** 2 * (P12 - NU * (P11 + P12))
    per_m_eps = 2.0 * math.pi * N_CORE * xi / LAMBDA
    print()
    print(f"  phase per metre per kelvin   = {per_m_K:.3e} rad/m/K")
    print(f"  phase per metre per strain   = {per_m_eps:.3e} rad/m per unit strain")
    equiv = per_m_K / per_m_eps
    print(f"  temperature equivalent of unit strain = {equiv:.4e} K")
    print(f"  i.e. 1 K is equivalent to {equiv * 1e6:.2f} microstrain.")
    print()
    print(f"{'temperature change (K)':>24}{'phase over 10 m (rad)':>23}"
          f"{'strain equivalent (ustrain)':>30}")
    for dT in (0.001, 0.01, 0.1, 1.0, 10.0):
        print(f"{dT:>24.3f}{per_m_K * 10.0 * dT:>23.4f}"
              f"{equiv * dT * 1e6:>30.3f}")
    print()
    print("  One kelvin of temperature change produces the same phase shift as")
    print(f"  about {equiv * 1e6:.0f} microstrain.  Seismic strain signals are of order 1e-9 to")
    print("  1e-7, so a temperature drift of millikelvin is comparable with a")
    print("  local earthquake and a diurnal surface temperature swing of a few")
    print("  kelvin swamps it entirely.  This is why every strain-based fibre")
    print("  measurement needs either a co-located temperature reference, a")
    print("  strain-free reference fibre, or a cable design that decouples the")
    print("  fibre from thermal expansion — and why a DAS record from a cable in")
    print("  a shallow trench carries a strong daily thermal signal that must be")
    print("  removed before the seismic signal is interpreted.")


def main():
    print("Fibre-optic sensing and distributed acoustic sensing")
    print("Nominal silica parameters at 1550 nm; a real measurement needs the")
    print("fibre data sheet and an in-situ calibration.")
    part1_geometry()
    part2_loss()
    part3_rbs()
    part4_resolution()
    part5_phase_strain()
    part6_gauge()
    part7_limits()
    part8_temperature()


if __name__ == "__main__":
    main()
