"""Case study: a magnetotelluric campaign - synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (skin depth, the coherence-accuracy relation
for an impedance estimate, data-rate arithmetic, depth resolution from the
period range).  No real campaign, instrument, vendor figure or measured dataset
is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "The period band from the target depth")
    target = 2000.0
    print(f"  target depth {target:.0f} m; delta = 503.3 sqrt(rho / f) [m, ohm m, Hz]")
    print(f"  {'rho (ohm m)':>12}{'f for delta = 2 km (Hz)':>24}{'T (s)':>9}")
    for rho in (1.0, 10.0, 100.0, 1000.0):
        f = rho / (target / 503.3) ** 2
        print(f"  {rho:12.1f}{f:24.4f}{1.0/f:9.3f}")
    f_10 = 10.0 / (target / 503.3) ** 2
    print(f"  a 10 ohm m target at 2 km needs T >~ {1.0/f_10:.2f} s, i.e. the low")
    print(f"  end of the frequency band ({f_10:.4f} Hz); a 100 ohm m target at the")
    print(f"  same depth needs {100.0/(target/503.3)**2:.4f} Hz, ten times higher.")
    print(f"  {'T (s)':>9}{'delta, 10 ohm m (m)':>22}{'delta, 100 ohm m (m)':>23}")
    for T in (0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0):
        f = 1.0 / T
        print(f"  {T:9.3f}{503.3*math.sqrt(10.0/f):22.1f}"
              f"{503.3*math.sqrt(100.0/f):23.1f}")
    return target


def section_2():
    banner(2, "Recording time from the coherence requirement")
    print("  relative impedance error: sigma_Z = sqrt((1 - gamma^2) / (2 N gamma^2))")
    print(f"  {'gamma^2':>9}{'N for 1 %':>12}{'N for 5 %':>12}{'T (s)':>8}"
          f"{'time for 1 % (min)':>21}")
    for g2 in (0.5, 0.8, 0.9, 0.95, 0.99, 0.998):
        n1 = (1 - g2) / (2 * 0.01 ** 2 * g2)
        n5 = (1 - g2) / (2 * 0.05 ** 2 * g2)
        T = 10.0
        print(f"  {g2:9.3f}{n1:12.1f}{n5:12.1f}{T:8.1f}{n1*T/60:21.1f}")
    print("  -> the recording time is set by the coherence, not by the instrument:")
    print("     a fall from 0.99 to 0.90 is a factor 10.5 in the required periods.")


def section_3():
    banner(3, "Remote reference and what it buys")
    print(f"  {'local gamma^2':>15}{'remote gamma^2':>16}{'N local':>10}"
          f"{'N remote':>10}{'time ratio':>12}")
    for gl, gr in ((0.90, 0.98), (0.80, 0.95), (0.99, 0.998)):
        nl = (1 - gl) / (2 * 0.01 ** 2 * gl)
        nr = (1 - gr) / (2 * 0.01 ** 2 * gr)
        print(f"  {gl:15.3f}{gr:16.3f}{nl:10.1f}{nr:10.1f}{nl/nr:12.2f}")
    print("  -> a remote reference improves the coherence at the low-coherence")
    print("     bands, and the payoff is the ratio of the required periods: the")
    print("     gain is largest exactly where the local data are worst.")


def section_4(n_sites=30):
    banner(4, "Campaign arithmetic: sites, crews and days")
    days_site = 3.0
    sites_per_crew_day = 0.0
    print(f"  {n_sites} sites, {days_site:.1f} days of recording per site")
    print(f"  {'crews':>7}{'site-days':>12}{'crew-days':>12}{'days':>8}"
          f"{'days + 20 %':>14}")
    site_days = n_sites * days_site
    for crews in (1, 2, 3):
        days = site_days / crews
        print(f"  {crews:7d}{site_days:12.0f}{site_days:12.0f}{days:8.1f}"
              f"{days*1.2:14.1f}")
    print("  the last column adds 20 % for access, weather and equipment failures")
    print(f"  data volume: 5 channels x 500 Hz x 4 B = {5*500*4/1000:.1f} kB/s")
    per_site = 5 * 500 * 4 * 86400 * days_site
    print(f"  per site = {per_site/1e9:.2f} GB, all {n_sites} sites = "
          f"{per_site*n_sites/1e9:.1f} GB")
    print("  -> the archive is small; the schedule is the scarce resource, and it")
    print("     is set by the recording time the coherence demands.")
    return n_sites


def section_5():
    banner(5, "Depth resolution from the period range")
    print(f"  {'periods (s)':>22}{'decades':>9}{'layers at 0.5 dec':>19}"
          f"{'modelled layers':>17}")
    for lo, hi in ((0.001, 1.0), (0.001, 100.0), (0.01, 1000.0), (0.1, 1000.0)):
        dec = math.log10(hi / lo)
        print(f"  {lo:9.3f}-{hi:<9.1f}{dec:9.2f}{dec/0.5:19.1f}{int(dec/0.5):17d}")
    print("  -> one independent layer per half-decade is the usual rule of thumb,")
    print("     so a 5-decade band supports about 10 layers -- and the dead band")
    print("     in the middle removes the layers it covers.")
    rng = np.random.default_rng(RNG_SEED)
    periods = np.logspace(-3, 3, 40)
    coh = 0.99 - 0.06 * np.exp(-((np.log10(periods) - 0.2) / 0.5) ** 2)
    i_dead = int(np.argmin(coh))
    print(f"  synthetic coherence: minimum {coh.min():.4f} at T = "
          f"{periods[i_dead]:.3f} s (the dead band), elsewhere > "
          f"{np.percentile(coh, 25):.4f}")
    print("  -> the band must be planned around the dead band, not through it.")


def main():
    print()
    banner(0, "CASE STUDY: A MAGNETOTELLURIC CAMPAIGN: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no real campaign,")
    print("instrument or measured dataset is reproduced.")


if __name__ == "__main__":
    main()
