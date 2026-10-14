"""Tectonics and the distribution of earthquakes and volcanoes.

Run:  .venv/bin/python tectonics_hazards_demo.py
Requires: numpy and scipy (and the standard library).

Companion to lesson 04-02-05, "Tectonics and the Distribution of Earthquakes
and Volcanoes".

The lesson's claim is that the global hazard map is a *consequence* of the
plate mosaic, and this script follows the chain from a plate boundary to a
number that an engineer or an emergency planner can use:

1. **The magnitude-frequency relation.** A synthetic catalogue is generated
   from the Gutenberg-Richter law, the $b$-value is recovered by maximum
   likelihood, and then the *bias* is demonstrated: analysing a catalogue
   below its magnitude of completeness gives a systematically wrong $b$. This
   is the single most common error in an amateur hazard estimate.
2. **Recurrence and probability.** The rate of magnitude 7 and 8 events is
   converted into a mean recurrence interval and then into the probability of
   at least one event in an exposure window, using the Poisson model that
   hazard assessment actually uses.
3. **Megathrust recurrence from the plate rate.** Independently of any
   catalogue, the seismic moment released over a century by a 1000 km
   megathrust follows from its area and its convergence rate. That gives a
   recurrence interval for great earthquakes which can be compared with the
   historical record -- a genuinely independent check on a hazard estimate.
4. **Tsunami.** The shallow-water speed, the travel time across an ocean
   basin, and the shoaling amplification as the wave enters shallow water. The
   two numbers that decide whether a warning is possible are the travel time
   and the amplification, and both are one line of arithmetic.

All catalogue parameters, boundary dimensions and ocean depths are NOMINAL or
ILLUSTRATIVE and are labelled. No specific event, region or published
recurrence estimate is used, because a real hazard number carries a source
model and an uncertainty that a demonstration cannot supply.
"""

from __future__ import annotations

import math

import numpy as np

YEAR = 3.15576e7
G_ACC = 9.81
MU_ROCK = 3.0e10                 # Pa, NOMINAL shear modulus


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def mle_b(magnitudes, mc, dm=0.0):
    """Aki-Utsu maximum-likelihood b-value for a catalogue above mc.

    The magnitudes here are continuous, so no bin correction is applied. A
    real catalogue records magnitudes to the nearest 0.1, and the standard
    practice is to apply a bin-width correction of half a bin; the formula
    below is written with the correction exposed so that a real analysis can
    supply it.
    """
    m = magnitudes[magnitudes >= mc - 1e-9]
    if len(m) < 2:
        return float("nan"), 0
    mbar = float(np.mean(m))
    b = math.log10(math.e) / (mbar - (mc - dm / 2.0))
    return b, len(m)


def part1_magnitude_frequency():
    section("1. The magnitude-frequency relation, and how to get it wrong")
    b_true = 1.0
    mc_complete = 2.0
    annual_rate = 5000.0            # ILLUSTRATIVE, events >= mc per year
    n_years = 200.0
    rng = np.random.default_rng(1234)

    # Inverse-transform sampling from the Gutenberg-Richter law:
    #   log10 N(>=M) = a - b M  =>  M = Mc - (1/b) log10(1 - u).
    n_events = int(annual_rate * n_years)
    u = rng.uniform(0.0, 1.0, n_events)
    mags = mc_complete - (1.0 / b_true) * np.log10(1.0 - u)
    print(f"  Synthetic catalogue: {n_events} events over {n_years:.0f} a")
    print(f"  generated from b = {b_true:.2f} and Mc = {mc_complete:.1f}.")
    print()

    # ---- Recover b from a complete catalogue.
    b_hat, n_used = mle_b(mags, mc_complete)
    print(f"  Complete catalogue, analysed at Mc = {mc_complete:.1f}:")
    print(f"    events used {n_used}, recovered b = {b_hat:.3f} "
          f"(input {b_true:.3f}, error {100 * (b_hat - b_true) / b_true:+.1f} %)")
    print()

    # ---- Now simulate incompleteness below 3.0 and analyse it two ways.
    keep_below = rng.uniform(0.0, 1.0, n_events) < 0.30
    incomplete = np.where(mags < 3.0, np.where(keep_below, mags, np.nan), mags)
    incomplete = incomplete[~np.isnan(incomplete)]
    b_low, n_low = mle_b(incomplete, mc_complete)
    b_high, n_high = mle_b(incomplete, 3.0)
    print("  Now make the catalogue incomplete below magnitude 3.0 (only 30 per")
    print("  cent of the small events recorded, which is what a real network")
    print("  did until recently):")
    print(f"    analysed at Mc = {mc_complete:.1f} (wrong): b = {b_low:.3f}, "
          f"{n_low} events")
    print(f"    analysed at Mc = 3.0 (right):  b = {b_high:.3f}, {n_high} events")
    print()
    print("  The first analysis is biased and the second is not, and the size of")
    print("  the bias is the whole point: a b-value estimated below the")
    print("  completeness magnitude is *flatter* than the truth, which makes the")
    print("  large-event rate look higher and a hazard estimate look worse. The")
    print("  fix is not a better estimator; it is a completeness analysis, and")
    print("  every catalogue used for hazard states its Mc and how it was found.")
    print()


def part2_recurrence():
    section("2. Recurrence and probability from the magnitude-frequency law")
    b_true = 1.0
    mc = 4.0
    rate_ge_mc = 10.0                # events per year, ILLUSTRATIVE
    print(f"  Assume b = {b_true:.1f}, Mc = {mc:.1f}, and "
          f"{rate_ge_mc:.0f} events at or above Mc per year.")
    print("  Then N(>=M) = N(>=Mc) 10^(-b(M - Mc)), so the rate of M >= 7 is")
    print("    rate = 10 * 10^(-1 * (7 - 4)) = 0.01 per year.")
    print()
    print(f"  {'M':>5}{'rate (per a)':>14}{'mean interval (a)':>20}"
          f"{'P(>=1 in 50 a)':>17}{'P(>=1 in 500 a)':>18}")
    for m in (4.0, 5.0, 6.0, 7.0, 8.0, 9.0):
        rate = rate_ge_mc * 10.0 ** (-b_true * (m - mc))
        interval = 1.0 / rate
        p50 = 1.0 - math.exp(-rate * 50.0)
        p500 = 1.0 - math.exp(-rate * 500.0)
        print(f"  {m:>5.1f}{rate:>14.4g}{interval:>20.4g}"
              f"{p50:>17.3f}{p500:>18.3f}")
    print()
    print("  Two features of this table drive the whole practice of hazard")
    print("  assessment.")
    print()
    print("  The mean interval is the reciprocal of the rate, which is exact,")
    print("  but it is an *average over a Poisson process*. The process has no")
    print("  memory: an event yesterday does not make one tomorrow less likely,")
    print("  and the 'interval' is not a clock. A recurrence of 100 years means")
    print("  a 1 per cent annual probability, not a guarantee one century from")
    print("  now.")
    print()
    print("  The probability accumulates and then saturates, and it saturates at")
    print("  different levels for different magnitudes. In a 50 year window the")
    print("  chance of at least one M >= 6 is 0.993 while the chance of at least")
    print("  one M >= 9 is 0.005; both are the same physics and neither number is")
    print("  more 'correct' than the other. That is why a hazard map for a 50")
    print("  year building code and a hazard map for a long-lived facility on the")
    print("  same fault are different maps: the exposure time, and the magnitude")
    print("  range that matters for the decision, both change.")
    print()


def part3_megathrust_recurrence():
    section("3. Megathrust recurrence from the plate rate alone")
    print("  Independent of any catalogue: a subduction megathrust has an area")
    print("  and a convergence rate, so it has a moment rate.")
    print()
    length_km, width_km, convergence_mm_a = 1000.0, 150.0, 60.0
    print(f"  Megathrust: length {length_km:.0f} km, seismogenic width "
          f"{width_km:.0f} km, convergence {convergence_mm_a:.0f} mm/a")
    print("  (NOMINAL values for an order-of-magnitude calculation).")
    print()
    area = (length_km * 1e3) * (width_km * 1e3)
    v_ms = convergence_mm_a * 1e-3 / YEAR
    moment_rate_per_s = MU_ROCK * area * v_ms
    moment_rate_per_a = moment_rate_per_s * YEAR
    print(f"  Area A = {area:.3e} m^2")
    print(f"  M0 rate = mu A v = {moment_rate_per_s:.3e} N m/s")
    print(f"                      = {moment_rate_per_a:.3e} N m/a")
    print()

    def mw_to_m0(mw):
        return 10.0 ** (1.5 * mw + 9.1)

    # ---- The naive calculation, shown so that it can be recognised.
    print("  The naive version of this calculation attributes the whole moment")
    print("  rate to events of a single size. It is wrong, and it is wrong in a")
    print("  way that is easy to spot:")
    print()
    print(f"  {'event Mw':>10}{'M0 (N m)':>13}{'naive interval (a)':>20}")
    for mw in (7.5, 8.0, 8.5, 9.0):
        print(f"  {mw:>10.1f}{mw_to_m0(mw):>13.3e}"
              f"{mw_to_m0(mw) / moment_rate_per_a:>20.1f}")
    print()
    print("  An interval of less than a year for magnitude 7.5 would mean the")
    print("  megathrust produced one such event every year, which no margin")
    print("  does, and it would leave no moment for anything else. The")
    print("  error is treating the moment budget as if it were spent on one")
    print("  magnitude rather than distributed over a magnitude range.")
    print()

    # ---- The correct calculation: magnitude-balanced Gutenberg-Richter.
    b = 1.0
    m_min, m_max = 6.0, 9.5
    # The moment rate is the integral over magnitude of the moment released by
    # events in each magnitude band:
    #   M0rate = int M0(M) * (-dN/dM) dM,   -dN/dM = b ln10 10^(a - bM),
    # with M0(M) = 10^(1.5M + 9.1).  With b = 1 the integral is
    #   M0rate = 2 * 10^a * 10^9.1 * (10^(0.5 m_max) - 10^(0.5 m_min)),
    # because the ln10 from -dN/dM cancels against the 1/(0.5 ln10) from the
    # integral of 10^(0.5 M).  Hence
    #   10^a = M0rate / (2 * 10^9.1 * (10^(0.5 m_max) - 10^(0.5 m_min))).
    numer = moment_rate_per_a
    denom = 2.0 * 10.0 ** 9.1 * (
        10.0 ** (0.5 * m_max) - 10.0 ** (0.5 * m_min))
    a_value = math.log10(numer / denom)
    print("  The correct version balances the moment over the whole magnitude")
    print("  distribution. With b = 1.0 between Mw 6.0 and Mw 9.5, the")
    print("  Gutenberg-Richter intercept that matches the moment rate is")
    print(f"    a = {a_value:.3f}, i.e.  N(>=M) = 10^({a_value:.3f} - M) per year.")
    print()
    print(f"  {'M >= Mw':>10}{'rate (per a)':>14}{'mean interval (a)':>20}")
    for mw in (6.0, 7.0, 8.0, 9.0):
        rate = 10.0 ** (a_value - mw)
        print(f"  {mw:>10.1f}{rate:>14.4g}{1.0 / rate:>20.0f}")
    print()
    print("  These are the right order for a major subduction zone: M >= 8")
    print("  roughly once every fifty years and M >= 9 roughly once every five")
    print("  centuries, with the smaller events filling the time between.")
    print()
    print("  One internal check. Attribute the whole budget to Mw 9 and the")
    print(f"  interval would be {mw_to_m0(9.0) / moment_rate_per_a:.0f} a, which is the")
    print("  shortest interval any distribution can give, since nothing else")
    print("  would then receive any moment. The balanced value is several times")
    print("  longer, as it must be, because the smaller events take their share.")
    print()
    print("  Nothing here used a catalogue, a b-value from a regression or an")
    print("  extrapolation of small events; it used the plate motion that lesson")
    print("  04-02-04 measures, plus the assumption that the magnitude")
    print("  distribution has the standard form.")
    print()
    print("  That assumption matters, and the sensitivity is easy to state. The")
    print("  moment integral is dominated by the largest magnitudes, so the")
    print("  result depends strongly on M_max and only weakly on b: a larger")
    print("  M_max absorbs more of the budget into rare great events and leaves")
    print("  fewer for the smaller ones. This is why an estimate of the maximum")
    print("  magnitude is the single most consequential input to a long-term")
    print("  seismic hazard assessment, and why it is argued about.")
    print()
    print("  The other assumption is that the entire convergence is released")
    print("  seismically. Real subduction zones are partly *aseismic*: some of")
    print("  the plate motion is accommodated by slow slip and creep that")
    print("  produces no strong shaking. The fraction released seismically --")
    print("  the coupling coefficient -- differs between margins by large")
    print("  factors and is a target of offshore observatories. So this table is")
    print("  an upper bound on the rate of strongly shaking events, and it is a")
    print("  bound with a physical meaning rather than a fitted number.")
    print()


def part4_tsunami():
    section("4. Tsunami: travel time and shoaling")
    print("  Long-wavelength shallow-water waves travel at c = sqrt(g h),")
    print("  independent of the wave's amplitude and period.")
    print()
    print(f"  {'depth (m)':>10}{'c (m/s)':>10}{'c (km/h)':>10}"
          f"{'time over 8000 km (h)':>24}")
    for h in (6000.0, 4000.0, 2000.0, 500.0, 100.0, 20.0):
        c = math.sqrt(G_ACC * h)
        t = 8000e3 / c / 3600.0
        print(f"  {h:>10.0f}{c:>10.1f}{c * 3.6:>10.1f}{t:>24.2f}")
    print()
    print("  Across a 4 km deep ocean the wave crosses 8000 km in about eleven")
    print("  hours at roughly 700 km/h, comparable to a jet's cruising speed.")
    print("  That is")
    print("  the number the warning system is built on: a tsunami generated at a")
    print("  trench arrives at a distant coast within hours, so a warning has to")
    print("  be issued within minutes of the earthquake and cannot be based on")
    print("  an analysis of the rupture.")
    print()
    print("  As the wave enters shallow water it slows, and because the energy")
    print("  flux has to be conserved the amplitude grows. For a slowly varying")
    print("  depth the shoaling factor in the Green's law limit is")
    print("  H2/H1 = (h1/h2)^(1/4).")
    print()
    print(f"  {'from depth (m)':>16}{'to depth (m)':>14}{'amplification':>15}"
          f"{'H_out for H_in = 0.5 m':>26}")
    h_in = 4000.0
    for h_out in (200.0, 100.0, 50.0, 20.0, 10.0):
        amp = (h_in / h_out) ** 0.25
        print(f"  {h_in:>16.0f}{h_out:>14.0f}{amp:>15.2f}{0.5 * amp:>26.2f}")
    print()
    print("  Green's law is an idealisation: it ignores refraction, trapping,")
    print("  reflection, harbour resonance and the run-up on a beach, all of")
    print("  which matter for the height at a particular address. What it does")
    print("  show is why an offshore wave of half a metre becomes a serious")
    print("  coastal hazard -- the amplification is a factor of 3 or more before")
    print("  any local effect is added -- and why the offshore amplitude is a")
    print("  quantity worth measuring with the seafloor pressure gauges that are")
    print("  now part of the warning systems.")
    print()
    print("  There is also a wavelength effect that the shallow-water formula")
    print("  hides. A tsunami's wavelength is hundreds of kilometres, so it")
    print("  feels the seafloor everywhere along its path and it 'shoals' over a")
    print("  distance comparable with its own wavelength: the whole wavefront")
    print("  slows and steepens at once. That is why a tsunami is a wall of water")
    print("  at the coast rather than a breaking swell, and why the same")
    print("  physics does not describe a wind-driven wave.")
    print()


def main():
    print("Tectonics and the distribution of earthquakes and volcanoes.")
    part1_magnitude_frequency()
    part2_recurrence()
    part3_megathrust_recurrence()
    part4_tsunami()
    print("=" * 74)
    print("Catalogue parameters, boundary dimensions and ocean depths are")
    print("NOMINAL or ILLUSTRATIVE and are labelled. The b-value and the")
    print("recurrence estimates are computed here, not quoted.")
    print("=" * 74)


if __name__ == "__main__":
    main()
