#!/usr/bin/env python3
"""Remote sensing for disaster response: synthetic SAR-like scenes, water
detection by a threshold, the confusion matrix, a cost-weighted threshold, and
how revisit and cloud set the time to a usable image.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python disaster_response_rs_demo.py

Everything here is SYNTHETIC.  The scenes, the backscatter values, the costs and
the cloud statistics are chosen teaching values, not a real event or sensor.  No
file is read or written and no network access is used.

Contents
--------
1. A synthetic pre/post pair with a flood patch.
2. Water detection by a threshold, and the confusion matrix against truth.
3. A threshold sweep, and the cost-weighted choice of threshold.
4. A change-magnitude damage proxy.
5. Time to a usable image from revisit and cloud.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H, W = 120, 120


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def confusion(pred, truth):
    tp = int((pred & truth).sum())
    fp = int((pred & ~truth).sum())
    fn = int((~pred & truth).sum())
    tn = int((~pred & ~truth).sum())
    return tp, fp, fn, tn


def main():
    yy, xx = np.mgrid[0:H, 0:W]
    r2 = (xx - 45.0) ** 2 + (yy - 75.0) ** 2
    flood = r2 < 30.0 ** 2                       # open water
    wet = (r2 >= 30.0 ** 2) & (r2 < 46.0 ** 2)   # saturated soil ring
    pre = RNG.normal(-8.0, 2.0, (H, W))          # dry land ~ -8 dB, speckle 2 dB
    post = RNG.normal(-8.0, 2.0, (H, W))
    post[wet] = RNG.normal(-13.0, 1.5, int(wet.sum()))
    post[flood] = RNG.normal(-18.5, 1.5, int(flood.sum()))

    section("1. A synthetic pre/post pair (SYNTHETIC)")
    print(f"scene {H} x {W} pixels")
    print(f"open water = {int(flood.sum())} px ({100 * flood.mean():.1f}%); "
          f"saturated soil ring = {int(wet.sum())} px ({100 * wet.mean():.1f}%)")
    print(f"dry land ~ -8 dB, wet soil ~ -13 dB, water ~ -18.5 dB (SYNTHETIC)")
    print(f"post-image land mean = {np.mean(post[~(flood | wet)]):.2f} dB, "
          f"wet-soil mean = {np.mean(post[wet]):.2f} dB, "
          f"water mean = {np.mean(post[flood]):.2f} dB")
    print("Smooth water acts as a mirror and sends little energy back to the")
    print("radar, so water is dark in a SAR image -- but saturated soil is dark")
    print("too, and that is the ambiguity a threshold has to navigate.")

    section("2. Threshold detection and its confusion matrix (SYNTHETIC)")
    thr = -14.0
    pred = post < thr
    tp, fp, fn, tn = confusion(pred, flood)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print(f"threshold = {thr:.0f} dB (water if backscatter < threshold)")
    print(f"TP = {tp}, FP = {fp}, FN = {fn}, TN = {tn}")
    print(f"precision = {precision:.3f}, recall = {recall:.3f}, F1 = {f1:.3f}")
    print("Every detected 'flood' pixel is a decision, not a measurement; the")
    print("confusion matrix is the honest form of the map.")

    section("3. Threshold sweep and the cost-weighted choice (SYNTHETIC)")
    print("  threshold   precision   recall     F1     FP    FN   cost")
    c_miss, c_fa = 10.0, 1.0
    best = None
    for t in np.arange(-16.0, -4.5, 1.0):
        p = post < t
        tp, fp, fn, tn = confusion(p, flood)
        pr = tp / (tp + fp) if tp + fp else float("nan")
        rc = tp / (tp + fn) if tp + fn else float("nan")
        f = 2 * pr * rc / (pr + rc) if pr > 0 else 0.0
        cost = c_miss * fn + c_fa * fp
        print(f"  {t:9.0f}   {pr:9.3f}   {rc:6.3f}   {f:5.3f}   {fp:5d} {fn:5d}   "
              f"{cost:6.0f}")
        if best is None or cost < best[1]:
            best = (t, cost)
    print(f"costs: a missed flood pixel = {c_miss:.0f}, a false alarm = {c_fa:.0f}")
    print(f"lowest-cost threshold = {best[0]:.0f} dB (cost {best[1]:.0f})")
    print("The 'best' threshold depends on the costs. Maximising F1 is a choice,")
    print("not a law; in a response, a missed house costs far more than a")
    print("false alarm, so the threshold is pushed to catch more water.")

    section("4. A change-magnitude damage proxy (SYNTHETIC)")
    delta = post - pre
    damaged = delta < -6.0
    print(f"mean change over the water = {delta[flood].mean():.2f} dB")
    print(f"mean change over wet soil  = {delta[wet].mean():.2f} dB")
    print(f"mean change over dry land  = {delta[~(flood | wet)].mean():.2f} dB")
    print(f"pixels with a drop > 6 dB = {int(damaged.sum())}, of which "
          f"{int((damaged & wet).sum())} are wet soil (false alarms) and "
          f"{int((damaged & flood).sum())} are water")
    print("A large drop is a change in surface roughness or moisture, which")
    print("correlates with inundation or damage; it is a proxy, and flooding")
    print("and saturated soil can look alike in one channel.")

    section("5. Time to a usable image (SYNTHETIC)")
    revisit = 5.0
    print(f"revisit = {revisit:.0f} d (SYNTHETIC)")
    print("  clear fraction   E[days to first clear image]")
    for clear in (0.9, 0.7, 0.5, 0.3):
        print(f"  {clear:14.2f}   {revisit / clear:28.1f}")
    print("Latency = revisit / clear fraction. For a response, the schedule and")
    print("the weather are part of the measurement: a perfect map that arrives a")
    print("week late changed fewer decisions than a coarse map that arrived fast.")


if __name__ == "__main__":
    main()
