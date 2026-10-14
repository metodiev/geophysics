"""IoT and autonomous sensor networks: a synthetic design walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (data-rate arithmetic, duty-cycle limits,
detection probability, free-space and empirical path loss, binomial
availability).  No vendor figure, product specification or measured radio link
is used or reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Data volume: what the science asks for and what can be moved")
    fs = 100.0          # Hz per component
    n_comp = 3
    bytes_sample = 4    # int32, uncompressed
    n_nodes = 20
    days = 180.0
    rate_bps = fs * n_comp * bytes_sample
    per_day = rate_bps * 86400.0
    total = per_day * n_nodes * days
    ratio = 3.0         # synthetic lossless compression factor
    print(f"  {fs:.0f} Hz x {n_comp} components x {bytes_sample} bytes = "
          f"{rate_bps:.0f} B/s = {rate_bps*8/1000:.1f} kbit/s per node")
    print(f"  per node per day      = {per_day/1e6:9.2f} MB")
    print(f"  {n_nodes} nodes x {days:.0f} days  = {total/1e9:9.2f} GB")
    print(f"  after {ratio:.0f}:1 compression = {total/ratio/1e9:9.2f} GB")
    return per_day


def section_2(per_day):
    banner(2, "Airtime: the duty-cycle limit against the data rate")
    rate_link = 50e3        # bit/s effective throughput, synthetic
    duty_limit = 0.01       # 1 % duty cycle, typical of licence-free bands
    airtime_needed = per_day * 8.0 / rate_link
    airtime_allowed = duty_limit * 86400.0
    frac = airtime_needed / 86400.0
    print(f"  link {rate_link/1e3:.0f} kbit/s effective, duty limit {duty_limit*100:.0f} %")
    print(f"  raw airtime needed  = {airtime_needed/3600.0:8.2f} h/day "
          f"({frac*100:5.1f} % of the day)")
    print(f"  airtime allowed     = {airtime_allowed:8.0f} s/day")
    print(f"  deliverable at the limit = {airtime_allowed*rate_link/8.0/1e6:8.2f} MB/day")
    print(f"  shortfall factor    = {airtime_needed/airtime_allowed:8.2f} x")
    print("  -> live streaming is impossible in-band; the node must trigger,")
    print("     decimate or buffer, or the data must be collected on a visit.")


def section_3():
    banner(3, "Detection probability and the wake interval it forces")
    tau_event = 2.0     # s, event duration
    w_record = 5.0      # s, recording window per wake
    print(f"  event duration {tau_event:.0f} s, recording window {w_record:.0f} s")
    print(f"  {'wake interval (s)':>19}{'P(detect)':>12}{'duty':>9}")
    for delta in (300.0, 120.0, 60.0, 30.0, 7.78):
        p = min(1.0, (tau_event + w_record) / delta)
        print(f"  {delta:19.2f}{p:12.4f}{w_record/delta:9.4f}")
    needed = (tau_event + w_record) / 0.90
    print(f"  for P = 0.90 the wake interval must be {needed:.2f} s,")
    print(f"  i.e. a {w_record/needed*100:.0f} % acquisition duty cycle -- which the")
    print("  airtime budget of section 2 already rules out for raw data.")
    return needed


def section_4():
    banner(4, "Link budget and range: free space against a real path")
    p_tx, g_tx, g_rx = 14.0, 2.0, 2.0     # dBm, dBi, dBi (synthetic)
    sensitivity = -120.0                  # dBm (synthetic)
    f_hz = 868e6
    allowed = p_tx + g_tx + g_rx - sensitivity
    print(f"  EIRP {p_tx+g_tx:.0f} dBm, receiver sensitivity {sensitivity:.0f} dBm")
    print(f"  allowable path loss = {allowed:.0f} dB at {f_hz/1e6:.0f} MHz")
    d_fs = 10 ** ((allowed - 20 * math.log10(f_hz) + 147.55) / 20.0)
    print(f"  free space gives d = {d_fs/1000:8.1f} km -- a geometric statement,")
    print("     not a prediction: it ignores ground, clutter and the Fresnel zone.")
    n_exp = 3.5           # synthetic empirical path-loss exponent
    pl_10m = 60.0         # dB at 10 m, synthetic reference
    d_all = 10.0 * 10 ** ((allowed - pl_10m) / (10.0 * n_exp))
    d_mar = 10.0 * 10 ** ((allowed - 20.0 - pl_10m) / (10.0 * n_exp))
    print(f"  with n = {n_exp:.1f} and {pl_10m:.0f} dB at 10 m:")
    print(f"    no-margin range   = {d_all:8.1f} m")
    print(f"    with 20 dB margin = {d_mar:8.1f} m")
    print(f"    a 20 dB margin costs a factor {d_all/d_mar:.2f} in range")
    return d_all, d_mar


def section_5():
    banner(5, "Node availability: what redundancy actually buys")
    n_nodes = 20
    p_survive = 0.90        # synthetic per-node survival over the campaign
    need = 16
    print(f"  {n_nodes} nodes, per-node survival {p_survive:.2f}, need at least {need}")
    prob = sum(math.comb(n_nodes, k) * p_survive ** k * (1 - p_survive) ** (n_nodes - k)
               for k in range(need, n_nodes + 1))
    print(f"  analytic P(at least {need}) = {prob:.4f}")
    rng = np.random.default_rng(RNG_SEED)
    trials = 200000
    alive = rng.random((trials, n_nodes)) < p_survive
    mc = float(np.mean(alive.sum(axis=1) >= need))
    print(f"  Monte Carlo ({trials} trials) = {mc:.4f}  "
          f"(difference {abs(mc-prob):.4f})")
    print(f"  expected nodes alive = {n_nodes*p_survive:.1f} of {n_nodes}")
    print("  -> redundancy is bought with node-days, so a failing node is a data")
    print("     loss only if the array is already at its minimum count.")


def section_6():
    banner(6, "Node-days budget: the metric the campaign is really spent in")
    n_nodes, days, p_survive = 20, 180.0, 0.90
    planned = n_nodes * days
    expected = planned * p_survive
    print(f"  planned node-days   = {planned:8.0f}")
    print(f"  expected node-days  = {expected:8.0f}  ({p_survive*100:.0f} % survival)")
    print(f"  lost to failure     = {planned-expected:8.0f}  "
          f"({(1-p_survive)*100:.0f} %)")
    print(f"  two extra nodes deployed from the start would return")
    print(f"  2 x {days:.0f} x {p_survive:.2f} = {2*days*p_survive:.0f} node-days for the")
    print("  cost of two extra sites set up once, against 360 node-days lost to the")
    print("  failures the spares absorb.")
    print("  -> spares deployed up front are almost always cheaper than a revisit.")


def main():
    print()
    banner(0, "AUTONOMOUS SENSOR NETWORK DESIGN: SYNTHETIC WALK-THROUGH")
    per_day = section_1()
    section_2(per_day)
    section_3()
    section_4()
    section_5()
    section_6()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no vendor specification,")
    print("regulatory figure or measured radio link is reproduced.")


if __name__ == "__main__":
    main()
