"""Case study: a marine geophysical cruise - synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (record length from depth and velocity, the
CDP fold relation, sail-speed and shot-interval arithmetic, feathering geometry,
data-rate arithmetic).  No real cruise, vessel, vendor figure or measured
dataset is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014
KN = 0.514444          # m/s per knot


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Record length and offsets from the target")
    z_target, v_rms = 2000.0, 2500.0
    t_two_way = 2 * z_target / v_rms
    margin = 1.0
    t_rec = t_two_way + margin
    print(f"  target {z_target/1000:.1f} km at {v_rms:.0f} m/s: two-way time "
          f"{t_two_way:.3f} s")
    print(f"  plus a {margin:.1f} s migration tail -> record length {t_rec:.2f} s")
    print("  far offset for velocity analysis ~ 1.4 x depth:")
    print(f"  {'depth (km)':>11}{'two-way (s)':>13}{'record (s)':>12}"
          f"{'far offset (m)':>16}")
    for z in (0.5, 1.0, 2.0, 3.0, 5.0):
        twt = 2 * z * 1000 / v_rms
        print(f"  {z:11.1f}{twt:13.4f}{twt+margin:12.3f}{1.4*z*1000:16.0f}")
    print("  -> the record length and the cable length follow from the deepest")
    print("     target; both are decided before the vessel is booked.")
    return t_rec, t_two_way


def section_2():
    banner(2, "Fold, binning and the acquisition geometry")
    n_ch, d_group, d_shot = 240, 12.5, 25.0
    spread = n_ch * d_group
    fold = spread / (2.0 * d_shot)
    bin_size = d_group / 2.0
    print(f"  {n_ch} channels at {d_group:.1f} m = {spread/1000:.2f} km cable")
    print(f"  shot interval {d_shot:.1f} m, bin = group/2 = {bin_size:.2f} m")
    print(f"  fold = (N d_group) / (2 d_shot) = {fold:.1f}")
    print(f"  {'channels':>9}{'cable (km)':>12}{'shot (m)':>10}{'fold':>8}"
          f"{'bin (m)':>9}")
    for nc, ds in ((120, 25.0), (240, 25.0), (480, 25.0), (480, 12.5)):
        sp = nc * d_group
        print(f"  {nc:9d}{sp/1000:12.2f}{ds:10.1f}{sp/(2*ds):8.1f}"
              f"{d_group/2:9.2f}")
    print("  -> fold is bought with cable length and shot density, and it buys")
    print("     signal-to-noise, not resolution: the bin size sets the resolution.")


def section_3(t_rec):
    banner(3, "Cruise arithmetic: line km, shots and days")
    n_lines, line_km = 40, 60.0
    speed_kn = 4.5
    v = speed_kn * KN
    t_line_h = (line_km * 1000.0 / v) / 3600.0
    t_turn_h = 0.5
    t_tot_h = n_lines * (t_line_h + t_turn_h)
    weather = 0.20
    transit_h = 2 * 72.0
    print(f"  {n_lines} lines x {line_km:.0f} km = {n_lines*line_km:.0f} line km")
    print(f"  speed {speed_kn:.1f} kn = {v:.3f} m/s = {v*3.6:.2f} km/h")
    print(f"  per line: {t_line_h:.2f} h steaming + {t_turn_h:.1f} h turn")
    print(f"  survey time {t_tot_h:.1f} h = {t_tot_h/24:.2f} days")
    print(f"  with {weather*100:.0f} % weather downtime = "
          f"{t_tot_h*(1+weather)/24:.2f} days")
    print(f"  plus {transit_h:.0f} h transit = "
          f"{(t_tot_h*(1+weather)+transit_h)/24:.2f} days total")
    n_shots = int(n_lines * line_km * 1000.0 / 25.0)
    print(f"  shots at 25 m = {n_shots:,} across the survey")
    print(f"  shot interval in time at {speed_kn:.1f} kn = {25.0/v:.2f} s")
    print("  -> the schedule is kilometres divided by speed plus turns; weather")
    print("     downtime and transit are the terms the plan most often omits.")
    return n_lines, line_km, n_shots


def section_4(n_shots, t_rec):
    banner(4, "Data volume and the vessel's day rate")
    n_ch, dt_ms = 240, 4.0
    n_samples = int(t_rec / (dt_ms / 1000.0))
    bytes_trace = n_samples * 4
    per_shot = n_ch * bytes_trace
    total = n_shots * per_shot
    print(f"  record {t_rec:.2f} s at {dt_ms:.1f} ms = {n_samples} samples per trace")
    print(f"  {n_ch} traces x {n_samples} samples x 4 B = {per_shot/1e6:.4f} MB per shot")
    print(f"  {n_shots:,} shots -> {total/1e12:.3f} TB raw")
    print(f"  {'day rate (k units)':>20}{'20 days':>10}{'30 days':>10}{'40 days':>10}")
    for rate in (50.0, 100.0, 200.0):
        print(f"  {rate:20.0f}{rate*20:10.0f}{rate*30:10.0f}{rate*40:10.0f}")
    print(f"  -> the archive is only {total/1e9:.1f} GB; the budget is the vessel:")
    print("     30 days at 100 k units is 3000 k units, far above the cost of")
    print("     storing the data, so schedule risk is the financial risk.")
    return total


def section_5():
    banner(5, "Feathering, positioning and the QC that matters at sea")
    print(f"  cross-line displacement of a streamer at offset x and feather angle a:")
    print(f"  {'offset (m)':>12}{'2 deg':>9}{'5 deg':>9}{'10 deg':>9}{'15 deg':>9}")
    for off in (600.0, 1500.0, 3000.0, 6000.0):
        row = f"  {off:12.0f}"
        for ang in (2.0, 5.0, 10.0, 15.0):
            row += f"{off*math.sin(math.radians(ang)):9.1f}"
        print(row)
    rng = np.random.default_rng(RNG_SEED)
    feather = rng.normal(4.0, 2.0, 2400)
    print(f"  synthetic feathering over a line: mean {feather.mean():.2f} deg, "
          f"sd {feather.std():.2f} deg")

    for tol in (6.0, 8.0, 10.0, 12.0):
        frac = 100 * float(np.mean(np.abs(feather) > tol))
        print(f"  shots beyond a {tol:4.1f} deg tolerance: {frac:6.2f} %")
    print("  -> the feathering distribution, not its mean, decides how much of the")
    print("     line is usable: a 12 deg tolerance rejects nothing here and a")
    print("     6 deg tolerance rejects about 16 % of the same line.")


def main():
    print()
    banner(0, "CASE STUDY: A MARINE GEOPHYSICAL CRUISE: SYNTHETIC WALK-THROUGH")
    t_rec, t_twt = section_1()
    section_2()
    n_lines, line_km, n_shots = section_3(t_rec)
    section_4(n_shots, t_rec)
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no real cruise, vessel,")
    print("vendor figure or measured dataset is reproduced.")


if __name__ == "__main__":
    main()
