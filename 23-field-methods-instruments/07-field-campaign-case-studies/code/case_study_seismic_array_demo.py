"""Case study: deploying a temporary seismic array - synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (array resolution and aliasing, data-rate
arithmetic, duty-cycle power budget, binomial availability).  No real campaign,
instrument, vendor figure or measured dataset is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Array geometry from the science requirement")
    lam, z_target, res_target = 2000.0, 10000.0, 1000.0     # m
    print(f"  target wavelength {lam/1000:.1f} km, depth {z_target/1000:.0f} km, "
          f"requested lateral resolution {res_target/1000:.1f} km")
    d_ap = lam * z_target / res_target
    print(f"  aperture for that resolution: D = lambda z / R = {d_ap/1000:.1f} km")
    print(f"  {'stations':>9}{'spacing (m)':>13}{'aperture (km)':>15}"
          f"{'resolution (km)':>17}")
    for n in (9, 13, 21, 31, 41):
        spacing = d_ap / (n - 1)
        print(f"  {n:9d}{spacing:13.1f}{d_ap/1000:15.1f}"
              f"{lam*z_target/d_ap/1000:17.1f}")
    d_alias = lam / 2.0
    print(f"  aliasing limit at this wavelength: spacing <= {d_alias:.0f} m")
    n_needed = math.ceil(d_ap / d_alias) + 1
    print(f"  stations to satisfy both: {n_needed} at {d_ap/(n_needed-1):.1f} m")
    return d_ap, n_needed, d_alias


def section_2(n_needed):
    banner(2, "Deployment workload")
    per_station_h = 3.0
    crew = 3
    travel_h = 1.0
    print(f"  {n_needed} stations, {per_station_h:.1f} h per station with a crew of "
          f"{crew}, {travel_h:.1f} h travel per day")
    days = math.ceil(n_needed * per_station_h / (8.0 * crew / crew))
    person_days = n_needed * per_station_h * crew / 8.0
    print(f"  installation: {n_needed} x {per_station_h:.1f} h = "
          f"{n_needed*per_station_h:.1f} station-hours")
    print(f"  with {crew} people: {person_days:.1f} person-days of installation")
    print(f"  {'crews':>7}{'stations/day':>14}{'days to install':>17}")
    for c in (1, 2, 3):
        rate = c * 8.0 / per_station_h
        print(f"  {c:7d}{rate:14.1f}{math.ceil(n_needed/rate):17d}")
    print("  -> the campaign is limited by access and crew time, not by the")
    print("     instruments: a second crew halves the installation, not the costs.")


def section_3(n_needed):
    banner(3, "Data volume and the archive")
    fs, n_comp, bytes_sample, days = 100.0, 3, 4, 60
    rate = fs * n_comp * bytes_sample
    total = rate * 86400 * days * n_needed
    print(f"  {fs:.0f} Hz x {n_comp} components x {bytes_sample} B = {rate:.0f} B/s "
          f"= {rate*8/1000:.1f} kbit/s per station")
    print(f"  {n_needed} stations x {days} days = {total/1e9:.2f} GB raw")
    print(f"  at 3:1 lossless compression = {total/3/1e9:.2f} GB")
    print(f"  one 4 TB disk holds {4e12/(total/3):.0f} repeats of this campaign")
    print("  -> the archive is trivial and the field collection is not: plan the")
    print("     disks and the download bench, not the network.")


def section_4(n_needed):
    banner(4, "Power, service interval and the visit plan")
    i_sleep, i_acq, i_tx = 25e-6, 30e-3, 150e-3
    cap_ah, usable = 40.0, 0.70
    d_acq, d_tx = 1.0 / 6.0, 20.0 / 86400.0
    avg = i_sleep + i_acq * d_acq + i_tx * d_tx
    life_d = cap_ah * usable * 1000 / (avg * 1e3) / 24.0
    print(f"  continuous acquisition at 1/6 duty: I_avg = {avg*1e3:.3f} mA")
    print(f"  {cap_ah:.0f} Ah battery, {usable*100:.0f} % usable -> "
          f"{life_d:.1f} days")
    print(f"  {'duty':>8}{'I_avg (mA)':>13}{'life (days)':>13}{'visits in 60 d':>16}")
    for duty in (1.0, 0.5, 1.0 / 6.0, 1.0 / 24.0):
        a = i_sleep + i_acq * duty + i_tx * d_tx
        lf = cap_ah * usable * 1000 / (a * 1e3) / 24.0
        print(f"  {duty:8.3f}{a*1e3:13.3f}{lf:13.2f}{math.ceil(60/lf):16d}")
    print("  -> with a 60-day deployment and a 1/6 duty cycle, the single visit is")
    print("     for the data, not for the battery; a bad cell is found only then.")


def section_5(n_needed, d_ap):
    banner(5, "What the campaign actually delivers")
    rng = np.random.default_rng(RNG_SEED)
    p_survive, lost_days = 0.90, 6.0
    print(f"  {n_needed} stations, per-station survival {p_survive:.2f}, "
          f"{lost_days:.0f} days lost to access")
    usable_days = 60.0 - lost_days
    alive = rng.random((200000, n_needed)) < p_survive
    exp_stations = float(np.mean(alive.sum(axis=1)))
    print(f"  expected stations alive at the end = {exp_stations:.2f} of {n_needed}")
    eff = exp_stations * usable_days
    print(f"  effective station-days = {eff:.0f} of {n_needed*usable_days:.0f} "
          f"planned ({100*eff/(n_needed*usable_days):.1f} %)")
    achieved = d_ap / (exp_stations - 1) * n_needed
    print(f"  the effective aperture falls from {d_ap/1000:.1f} km to "
          f"{d_ap*exp_stations/n_needed/1000:.1f} km on average")
    print(f"  and the resolution cell grows from {1000:.0f} m to "
          f"{light_res(exp_stations):.0f} m")
    print(f"  a 2-station failure costs about "
          f"{abs(light_res(n_needed)-light_res(n_needed-2)):.0f} m of resolution")
    print("  -> deploy the redundancy up front: two extra stations cost two sites")
    print("     of installation and buy back the resolution of the failures.")


def light_res(n_stations):
    lam, z, spacing, n_nom = 2000.0, 10000.0, 1000.0, 21
    d = spacing * n_nom * (n_stations - 1) / (n_nom - 1)
    return lam * z / d


def main():
    print()
    banner(0, "CASE STUDY: TEMPORARY SEISMIC ARRAY: SYNTHETIC WALK-THROUGH")
    d_ap, n_needed, d_alias = section_1()
    section_2(n_needed)
    section_3(n_needed)
    section_4(n_needed)
    section_5(n_needed, d_ap)
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no real campaign,")
    print("instrument or measured dataset is reproduced.")


if __name__ == "__main__":
    main()
