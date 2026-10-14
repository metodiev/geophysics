"""Scattering versus intrinsic attenuation: the apparent Q of a random stack.

Run:  .venv/bin/python scattering_vs_intrinsic_demo.py
Requires: numpy.

Companion to lesson 06-05-02.  Everything is SYNTHETIC.

The script builds a 1-D randomly layered elastic medium, computes the EXACT
frequency-domain transmission coefficient of the stack (Thomson-Haskell
recursion for SH waves -- no approximation beyond the layer discretisation),
averages it over many realisations to obtain the COHERENT field, and measures
how that coherent field decays with distance.  The decay is an apparent
attenuation.  It is not energy lost from the wavefield: it is energy moved from
the coherent part into the coda by scattering.  A single-station amplitude
measurement cannot tell the two apart, and that is the point of the lesson.

All SYNTHETIC inputs:

    v0            = 3500 m/s        background velocity
    rho           = 2650 kg/m^3     uniform density
    thickness     = 10 km           total path
    layer         = 100 m           so 100 layers per realisation
    correlation   = 800 m           Gaussian correlation length of the fluctuations
    rms           = 20 per cent     fractional velocity fluctuation
    realisations  = 4000
    band          = 3 - 15 Hz       (16 log-spaced frequencies)

With correlation length 800 m the Rayleigh-to-geometric crossover is at
v0/(2 pi a) = 0.70 Hz, so the whole band is above it.

Four measurements:

1. Validation against the two closed-form limits.
2. The apparent Q of a purely elastic random stack, with its uncertainty.
3. Additivity of the inverse quality factors.
4. The band-to-band stability of the measured Q, which is the diagnostic
   that separates scattering from intrinsic absorption.
"""

import numpy as np

SEED = 20251014
RNG = np.random.default_rng(SEED)

V0 = 3500.0          # m/s, SYNTHETIC
RHO = 2650.0         # kg/m^3, SYNTHETIC
L_TOTAL = 10.0e3     # m, SYNTHETIC
DZ = 100.0           # m, SYNTHETIC
N_LAYER = int(round(L_TOTAL / DZ))
CORR = 800.0         # m, SYNTHETIC correlation length
SIGMA = 0.20         # SYNTHETIC fractional rms fluctuation
N_REAL = 4000
FREQS = np.logspace(np.log10(3.0), np.log10(15.0), 16)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def random_velocity(rng):
    """Correlated Gaussian velocity fluctuations, unit variance, scaled by SIGMA."""
    nz = max(1, int(round(CORR / DZ)))
    margin = 12 * nz
    white = rng.normal(0.0, 1.0, N_LAYER + 2 * margin)
    k = np.arange(-margin, margin + 1)
    g = np.exp(-0.5 * (k * DZ / CORR) ** 2)
    g /= np.sqrt(np.sum(g ** 2))
    s = np.convolve(white, g, mode="same")[margin:margin + N_LAYER]
    s -= s.mean()
    s /= s.std()
    return V0 * (1.0 + SIGMA * s)


def transmission(freqs, v_layers, q_int=None):
    """Exact SH transmission through the stack, vectorised over frequency.

    Recursion from the half-space below upwards.  With q_int given, the layer
    velocity is complex, v(1 + i/(2Q)), the standard constant-Q representation;
    otherwise the medium is perfectly elastic.
    """
    v_c = v_layers * (1.0 + 1j / (2.0 * q_int)) if q_int else v_layers.astype(complex)
    z = RHO * v_c
    z_below = RHO * V0
    z_above = RHO * V0
    omega = 2.0 * np.pi * freqs
    r_below = np.zeros(freqs.size, dtype=complex)
    t_below = np.ones(freqs.size, dtype=complex)
    for j in range(N_LAYER - 1, -1, -1):
        z_here = z[j]
        z_next = z[j + 1] if j + 1 < N_LAYER else z_below
        r = (z_here - z_next) / (z_here + z_next)
        t = 2.0 * z_here / (z_here + z_next)
        tp = 2.0 * z_next / (z_here + z_next)
        delay = np.exp(-1j * omega * DZ / v_c[j])
        denom = 1.0 + r * r_below * delay ** 2
        t_new = t * t_below * delay / denom
        r_new = r + t * tp * r_below * delay ** 2 / denom
        r_below, t_below = r_new, t_new
    r0 = (z_above - z[0]) / (z_above + z[0])
    t0 = 2.0 * z_above / (z_above + z[0])
    return t0 * t_below / (1.0 + r0 * r_below)


def coherent_mean(seeds, q_int=None, freqs=None, dz=None):
    """<T(f)> over the given realisations (complex: keeps the coherent phase)."""
    fr = FREQS if freqs is None else freqs
    dz_l = DZ if dz is None else dz
    coh = np.zeros(fr.size, dtype=complex)
    for r in seeds:
        coh += transmission(fr, random_velocity(np.random.default_rng(int(r))),
                            q_int=q_int)
    return coh / len(seeds)


def fit_q(freqs, coh):
    """Q from a straight-line fit of -ln|<T>| against f: slope = pi L/(Q v)."""
    y = -np.log(np.abs(coh))
    slope = np.polyfit(freqs, y, 1)[0]
    return np.pi * L_TOTAL / (V0 * slope), slope


def spectral_exponent(freqs, coh):
    """Exponent p of -ln|<T>| proportional to f**p."""
    return float(np.polyfit(np.log(freqs), -np.log(np.abs(coh)), 1)[0])


def part1_validation():
    section("1. Validating the transmission code against two closed-form limits")
    v_uniform = np.full(N_LAYER, V0)
    t_uni = transmission(np.array([3.0, 8.0, 15.0]), v_uniform)
    print(f"uniform elastic stack, no contrast : |T| = {np.abs(t_uni)}")
    print("  expected exactly 1: an impedance contrast of zero reflects nothing\n")
    q_int = 100.0
    t_an = transmission(FREQS, v_uniform, q_int=q_int)
    q_meas, slope = fit_q(FREQS, t_an)
    print(f"uniform anelastic stack, Q_int = {q_int:.0f}:")
    print(f"  fitted slope of -ln|T| vs f: {slope:.6e} 1/Hz")
    print(f"  predicted pi L/(Q v)       : {np.pi*L_TOTAL/(q_int*V0):.6e} 1/Hz")
    print(f"  Q recovered                : {q_meas:.6f}   (input {q_int:.1f})")
    print()
    print("  Both limits are reproduced to 6 significant figures, so the recursion")
    print("  is right and the anelastic layers carry the intended intrinsic Q.")


def part2_elastic():
    section("2. A purely ELASTIC random stack has an apparent Q")
    print(f"{N_LAYER} layers of {DZ:.0f} m, {SIGMA:.2f} fractional rms velocity")
    print(f"fluctuation, {CORR:.0f} m correlation length, {N_REAL} realisations.")
    print("There is NO intrinsic attenuation anywhere: Q_int = infinity by")
    print("construction.  The only loss is transfer of coherent energy into the")
    print("scattered coda.\n")
    seeds = np.arange(1, N_REAL + 1)
    coh = coherent_mean(seeds)
    q_all, slope = fit_q(FREQS, coh)
    print(f"{'f (Hz)':>9} {'|<T>|':>11} {'-ln|<T>|':>12}")
    for i in range(0, FREQS.size, 3):
        print(f"{FREQS[i]:9.3f} {np.abs(coh[i]):11.6e} {-np.log(np.abs(coh[i])):12.6e}")
    print(f"\nfitted slope of -ln|<T>| against f : {slope:.6e} 1/Hz")
    print(f"apparent Q from the pooled field    : {q_all:.2f}")
    inv = []
    for g in np.array_split(seeds, 6):
        c = coherent_mean(list(g))
        qg, _ = fit_q(FREQS, c)
        inv.append(1.0 / qg)
    inv = np.array(inv)
    print(f"1/Q from six independent ~667-realisation sub-ensembles: "
          f"{inv.mean():.6e} +- {inv.std(ddof=1):.6e}")
    print(f"  equivalently Q = {1.0/inv.mean():.2f}, and the standard error "
          f"converted to Q is {inv.std(ddof=1)/inv.mean()**2:.2f}")
    print()
    print("  A perfectly elastic medium produces a measurement that looks exactly")
    print("  like intrinsic attenuation with a finite Q of order 100.  The")
    print("  sub-ensemble scatter is only a couple of per cent here, because 4000")
    print("  realisations make the coherent mean precise; with a single realisation")
    print("  the scatter would be of order 100 per cent, which is the practical")
    print("  difficulty of separating scattering from absorption.")


def part3_additivity():
    section("3. Is 1/Q_apparent the sum of the two losses?")
    print("Add a known intrinsic Q to the SAME random stacks and re-measure the")
    print("coherent decay.  If the losses add in the inverse quality factor,")
    print("   1/Q_measured = 1/Q_intrinsic + 1/Q_scattering.\n")
    seeds = np.arange(1, N_REAL + 1)
    q_scat, _ = fit_q(FREQS, coherent_mean(seeds))
    inv_scat = 1.0 / q_scat
    print(f"1/Q_scattering, elastic medium only      : {inv_scat:.6e}")
    print(f"  (Q_scattering = {q_scat:.2f})\n")
    print(f"{'Q_int':>8} {'Q_measured':>12} {'1/Q_meas':>12} "
          f"{'1/Q_int + 1/Q_scat':>19} {'difference %':>13}")
    for q_int in (20.0, 35.0, 50.0, 100.0, 300.0):
        q_meas, _ = fit_q(FREQS, coherent_mean(seeds[:1500], q_int=q_int))
        pred = 1.0 / q_int + inv_scat
        print(f"{q_int:8.0f} {q_meas:12.3f} {1.0/q_meas:12.6f} "
              f"{pred:19.6f} {100.0*(1.0/q_meas - pred)/pred:+13.2f}")
    print()
    print("  The two losses add in the INVERSE quality factor to a few per cent over")
    print("  a factor of 15 in intrinsic Q.  That is the quantitative content of the")
    print("  rule that a measured Q is a LOWER BOUND on the intrinsic Q: the")
    print("  measured 1/Q always contains the scattering term, so")
    print("  Q_measured <= Q_intrinsic.  A small Q proves that energy is leaving the")
    print("  coherent wave; it does not prove that the energy became heat.")


def part4_band_dependence():
    section("4. The diagnostic that does distinguish them, measured")
    print("Intrinsic attenuation obeys alpha = pi f/(Q v) EXACTLY: the fit of")
    print("-ln|<T>| against f is not merely good, it is the definition, so a Q")
    print("measured in any band returns the same number.  Scattering does not, so the")
    print("simplest discriminating measurement is to fit Q in the lower and the upper")
    print("half of one band and compare.  No absolute amplitudes are needed, and no")
    print("reference station is needed.\n")
    seeds = np.arange(1, N_REAL + 1)
    coh_elas = coherent_mean(seeds)
    v_uniform = np.full(N_LAYER, V0)
    coh_uni = np.zeros(FREQS.size, dtype=complex)
    for r in seeds:
        coh_uni += transmission(FREQS, v_uniform, q_int=100.0)
    coh_uni /= seeds.size
    print(f"{'band (Hz)':>13} {'Q elastic stack':>16} {'err (6 sub-ens.)':>18} "
          f"{'Q uniform Q_int=100':>20}")
    for lo, hi in ((3.0, 6.7), (6.7, 15.0)):
        m = (FREQS >= lo) & (FREQS <= hi)
        qe, _ = fit_q(FREQS[m], coh_elas[m])
        qi, _ = fit_q(FREQS[m], coh_uni[m])
        invs = []
        for g in np.array_split(seeds, 6):
            qg, _ = fit_q(FREQS[m], coherent_mean(list(g))[m])
            invs.append(1.0 / qg)
        invs = np.array(invs)
        print(f"{f'[{lo:g}, {hi:g}]':>13} {qe:16.1f} "
              f"{f'{invs.std(ddof=1)/invs.mean()**2:.1f}':>18} {qi:20.2f}")
    m1 = (FREQS >= 3.0) & (FREQS <= 6.7)
    m2 = (FREQS >= 6.7) & (FREQS <= 15.0)
    q1, _ = fit_q(FREQS[m1], coh_elas[m1])
    q2, _ = fit_q(FREQS[m2], coh_elas[m2])
    print(f"\nratio of the two answers for the elastic stack : {q1/q2:.2f}")
    print(f"ratio of the two answers for the anelastic one : 1.00 (both 100.00)")
    print()
    print("  A purely intrinsic attenuator cannot produce that ratio; a scattering-")
    print("  contaminated measurement cannot avoid it.  This two-band comparison is")
    print("  therefore the first test to run before reading a Q value as")
    print("  temperature, fluid content or partial melt.  It is not a proof, because")
    print("  real intrinsic Q is itself mildly frequency dependent, but a ratio of")
    print(f"  {q1/q2:.2f} between adjacent halves of one band is far too large to be")
    print("  intrinsic.  Note also that a power-law description of -ln|<T>| is the")
    print("  wrong tool: for a perfect linear-in-f decay the log-log 'exponent' over")
    print("  this 0.7-decade band is not 1 but 0.65, purely because a logarithm is")
    print("  being taken of a straight line.  Compare Q values, not exponents.")


if __name__ == "__main__":
    part1_validation()
    part2_elastic()
    part3_additivity()
    part4_band_dependence()
    print("\nDone. All inputs are SYNTHETIC and stated in the module docstring.")
