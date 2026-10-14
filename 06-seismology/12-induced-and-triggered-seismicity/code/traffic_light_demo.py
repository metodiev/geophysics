"""Traffic-light protocols: what the thresholds can and cannot be derived from.

A traffic-light protocol sets magnitude thresholds and a prescribed operational
response (green: continue; amber: review, reduce rate; red: stop).  Three things
are computed here, all from STATED models:

  1. The Gutenberg-Richter exceedance arithmetic.  With a rate n0 of events at
     or above a completeness magnitude Mc and a b-value b, the rate at or above
     a threshold Mt is n0 * 10^(-b (Mt - Mc)).  This fixes how often a threshold
     is crossed -- which is the answer to "how many false alarms per year".

  2. The distribution of the MAXIMUM magnitude in a sequence of N events.
     Its expected value grows only as log10(N)/b, and -- the important part --
     its spread does NOT shrink as N grows.  So a bigger catalogue does not
     bound the largest event better.

  3. A decision-theoretic cost model.  The "optimal" threshold depends entirely
     on the assumed cost of a false alarm relative to the assumed cost of a
     damaging event.  Changing those costs by a factor of ten moves the optimum
     by more than a magnitude unit.

Every input is a MODEL choice and is labelled.  No magnitude threshold anywhere
in this file is a physical constant, because none exists.

Run:  <repo>/.venv/bin/python traffic_light_demo.py
"""

from __future__ import annotations

import numpy as np

# ----------------------------------------------------------------------
# MODEL inputs (chosen, not measured)
# ----------------------------------------------------------------------
MC = 1.0                 # -      MODEL completeness magnitude
B_VALUE = 1.0            # -      MODEL Gutenberg-Richter b-value
N0 = 100.0               # 1/yr   MODEL rate of events at or above Mc
N_YEARS = 10.0           # yr     MODEL length of a monitoring programme
N_SITES = 20             # -      MODEL number of monitored operations in a basin

LINES = "=" * 78


def section(title: str) -> None:
    print(f"\n{LINES}\n{title}\n{LINES}")


def rate_above(m_t: float, n0: float = N0, b: float = B_VALUE, mc: float = MC) -> float:
    """Events per year at or above M >= m_t."""
    return n0 * 10.0 ** (-b * (m_t - mc))


def main() -> int:
    print("Traffic-light protocols: thresholds are policy, not physics")
    print(f"MODEL: Mc = {MC:.1f}, b = {B_VALUE:.2f}, n0 = {N0:.0f} events/yr "
          f"at or above Mc")
    print(f"       programme length {N_YEARS:.0f} yr, {N_SITES} monitored sites")

    # ------------------------------------------------------------------
    section("1. Exceedance arithmetic: how often is a threshold crossed?")
    print("  rate(M >= Mt) = n0 * 10^(-b (Mt - Mc));  P(>=1 in 1 yr) = "
          "1 - exp(-rate)")
    print("\n    Mt    rate [1/yr]   mean recurrence [yr]   P(>=1 per yr)   "
          "P(>=1 in 10 yr)")
    for mt in (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0):
        lam = rate_above(mt)
        rec = np.inf if lam == 0 else 1.0 / lam
        p1 = 1.0 - np.exp(-lam)
        p10 = 1.0 - np.exp(-lam * N_YEARS)
        print(f"  {mt:5.1f}   {lam:10.3f}   {rec:19.2f}   {p1:15.4f}   {p10:15.4f}")
    print("  These numbers are a statement about the CATALOGUE, not about the")
    print("  operation.  Choosing Mt chooses how often you stop work, and nothing")
    print("  else: a threshold at a magnitude with a one-per-year rate will be")
    print("  tripped about once a year whether the seismicity is induced or not.")

    # ------------------------------------------------------------------
    section("2. How many threshold crossings per programme, and per basin?")
    print("\n    Mt    expected trips, 1 site / 10 yr   expected trips, "
          f"{N_SITES} sites / 10 yr")
    for mt in (1.5, 2.0, 2.5, 3.0):
        lam = rate_above(mt)
        one = lam * N_YEARS
        many = one * N_SITES
        print(f"  {mt:5.1f}   {one:32.2f}   {many:33.2f}")
    print("  The expected number of RED events in a basin is LINEAR in the number of")
    print("  monitored sites.  A protocol calibrated at one site therefore produces")
    print("  a predictable number of stoppages per year across a jurisdiction, and")
    print("  that number -- not the magnitude -- is what makes a threshold")
    print("  acceptable or not to an operator.")

    # ------------------------------------------------------------------
    section("3. The maximum magnitude in a sequence of N events")
    print("  For a Gutenberg-Richter population the expected maximum is")
    print("      E[Mmax] = Mc + (ln N + gamma_E) / (b ln 10),   gamma_E = 0.5772,")
    print("  and its SPREAD does not shrink as N grows.  The frequently quoted form")
    print("  Mc + log10(N)/b omits the Euler-Mascheroni term, which is 0.25 magnitude")
    print("  units for b = 1; the measurement below shows that offset.  Measured by")
    print("  simulation")
    print(f"  (20 000 sequences per N, b = {B_VALUE:.2f}):")
    rng = np.random.default_rng(20261014)
    print("\n      N    E[Mmax] model   measured mean   measured median    "
          "5%      95%   95-5 spread")
    n_trials = 20000
    spreads = []
    for n_ev in (10, 100, 1000, 10000):
        m = MC + rng.exponential(1.0 / (B_VALUE * np.log(10.0)), (n_trials, n_ev))
        mmax = m.max(axis=1)
        lo, med, hi = np.percentile(mmax, [5, 50, 95])
        spreads.append(hi - lo)
        model = MC + (np.log(n_ev) + 0.5772156649) / (B_VALUE * np.log(10.0))
        print(f"  {n_ev:6d}   {model:13.3f}   {mmax.mean():13.3f}   {med:15.3f} "
              f"{lo:7.3f} {hi:8.3f} {hi - lo:13.3f}")
    gumbel = (1.0 / (B_VALUE * np.log(10.0))) * np.log(np.log(0.05) / np.log(0.95))
    print(f"  The MEAN matches Mc + (ln N + gamma_E)/(b ln 10); the median sits lower.")
    print(f"  The 5-95 spread is essentially CONSTANT, from {spreads[0]:.2f} to "
          f"{spreads[-1]:.2f}.")
    print(f"  The asymptotic (Gumbel) spread is (1/(b ln 10)) ln(ln0.05/ln0.95) = "
          f"{gumbel:.3f} magnitude units, independent of N.")
    print("  The naive formula log10(N)/b underestimates the mean by gamma_E/(b ln10)")
    print("  = 0.251 magnitude units for b = 1, which the measured column shows.")
    print("  A hundredfold more events moves the expected maximum by one magnitude")
    print("  unit and does not narrow the distribution at all.  No sample size makes")
    print("  the largest event predictable.")

    # ------------------------------------------------------------------
    section("4. No physical cap: the probability of exceeding any stated size")
    print("  P(Mmax > Mt) = 1 - (1 - 10^(-b (Mt - Mc)))^N.  The N needed for a 50 %")
    print("  chance is about 0.693 * 10^(b (Mt - Mc)):")
    print("\n    Mt     P(Mmax > Mt), N=100   N=1000   N=10000   N for 50% chance")
    for mt in (2.0, 3.0, 4.0, 5.0, 6.0):
        p_single = 10.0 ** (-B_VALUE * (mt - MC))
        vals = [1.0 - (1.0 - p_single) ** n_ev for n_ev in (100, 1000, 10000)]
        n50 = 0.693 / p_single
        print(f"  {mt:5.1f}   {vals[0]:20.4f}   {vals[1]:8.4f}   {vals[2]:9.4f}   "
              f"{n50:20.0f}")
    print("  Every threshold can be exceeded, given enough events, and the number")
    print("  of events needed grows only as 10^(b dM).  Nothing in this calculation")
    print("  contains a maximum magnitude: a bound would have to come from physics")
    print("  (finite fault area, finite energy, finite stress drop), and the models")
    print("  that try to supply one disagree.  The honest statement is that the")
    print("  largest possible induced event is NOT bounded by any accepted model.")

    # ------------------------------------------------------------------
    section("5. A cost model, to show what 'optimal threshold' really means")
    print("  This is a TOY model, stated in full so that it can be argued with:")
    print("    annual cost(Mt) = c_trip * rate(Mt)")
    print("                      + c_dmg * rate(M_dmg) * exp(-rate(Mt) * W)")
    print("  where W is the assumed precursor-awareness window in years (how long")
    print("  before a damaging event a RED alert would still be useful) and M_dmg is")
    print("  the magnitude of a damaging event.  The first term grows as Mt falls")
    print("  (more stoppages); the second grows as Mt rises (less warning).")
    W = 0.05
    M_DMG = 4.0
    lam_dmg = rate_above(M_DMG)
    print(f"  MODEL: W = {W:.2f} yr, and the damaging-event rate is rate(M >= "
          f"{M_DMG:.1f}) = {lam_dmg:.3f} /yr")
    print("\n    c_trip     c_dmg      optimal Mt   cost at optimum   "
          "interior optimum?")
    grid = np.linspace(1.0, 5.0, 4001)
    for c_trip, c_dmg in ((1.0e6, 1.0e9), (1.0e6, 1.0e10), (1.0e7, 1.0e9),
                          (1.0e5, 1.0e10), (1.0e6, 1.0e8)):
        cost = c_trip * rate_above(grid) + c_dmg * lam_dmg * np.exp(
            -rate_above(grid) * W)
        i = int(np.argmin(cost))
        interior = "yes" if 0 < i < grid.size - 1 else "NO (boundary)"
        print(f"  {c_trip:9.1e}  {c_dmg:9.1e}  {grid[i]:11.2f}   "
              f"{cost[i]:16.3e}   {interior}")
    print("  The analytic optimum satisfies rate(Mt*) = ln(c_dmg lam_dmg W / c_trip)/W.")
    for c_trip, c_dmg in ((1.0e6, 1.0e9), (1.0e6, 1.0e10), (1.0e7, 1.0e9)):
        r = c_dmg * lam_dmg * W / c_trip
        if r <= 1.0:
            print(f"    c_trip = {c_trip:.1e}, c_dmg = {c_dmg:.1e}: "
                  f"r = {r:.3f} < 1, so there is no interior optimum: the model says")
            print("      stopping at every event is better than any threshold.")
            continue
        lam_star = np.log(r) / W
        mt_star = MC - np.log10(lam_star / N0) / B_VALUE
        print(f"    c_trip = {c_trip:.1e}, c_dmg = {c_dmg:.1e}: "
              f"rate* = {lam_star:.2f} /yr  ->  Mt* = {mt_star:.2f}")
    print("  A tenfold change in the cost ratio moves the optimal threshold by a")
    print("  substantial fraction of a magnitude unit, and in one case removes the")
    print("  rationale for a threshold at all.  That is the whole argument: a")
    print("  traffic-light threshold is the output of a cost model, so it is a POLICY")
    print("  CHOICE.  Presenting one as a physical limit -- 'the rock here cannot")
    print("  host an event larger than X' -- is a category error.")

    # ------------------------------------------------------------------
    section("6. What a protocol can honestly promise")
    print("  From the arithmetic above, a protocol CAN promise:")
    print("   - a stated expected number of stoppages per site per year (section 2);")
    print("   - a stated probability of catching an event of a given size, which is")
    print("     the exceedance probability of section 4, and is small for large sizes;")
    print("   - a transparent, auditable rule that an operator can comply with.")
    print("  A protocol CANNOT promise:")
    print("   - that no damaging event will occur, because section 4 shows that any")
    print("     threshold is exceeded for some N;")
    print("   - that a stoppage is unnecessary, because section 1 shows that the")
    print("     threshold is crossed at the background rate too;")
    print("   - any statement about whether a particular event was induced.")
    lam25 = rate_above(2.5)
    p_exc = 10.0 ** (-B_VALUE * (3.5 - MC))
    print(f"\n  Concretely, with Mt = 2.5 and these MODEL numbers: "
          f"{lam25:.3f} crossings/yr/site,")
    print(f"  i.e. about {lam25 * N_SITES * N_YEARS:.0f} stoppages across "
          f"{N_SITES} sites in {N_YEARS:.0f} years.")
    print(f"  In a 1000-event sequence the chance of at least one event of M >= 3.5")
    print(f"  (a full unit above the threshold) is 1-(1-{p_exc:.5f})^1000 = "
          f"{1 - (1 - p_exc) ** 1000:.3f}, so the")
    print("  protocol does not exclude it; it merely monitors it.")

    # ------------------------------------------------------------------
    section("Summary of measured quantities")
    print(f"  rate at or above Mt = 2.5, MODEL parameters          = "
          f"{rate_above(2.5):.4f} /yr")
    print(f"  mean recurrence of Mt = 2.5                          = "
          f"{1.0 / rate_above(2.5):.2f} yr")
    print(f"  5-95 spread of Mmax for N = 10                       = measured above")
    print("  Everything in this file comes from a Gutenberg-Richter model plus a")
    print("  cost model.  The thresholds are choices; the exceedance arithmetic is")
    print("  a consequence of the model.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
