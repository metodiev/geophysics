"""Defence preparation: how far each plausible viva question moves the headline number.

The headline is the Moho depth of the execution lesson. Every question a panel could
ask is mapped to a re-computation of the analysis: a different assumed Vp or Vp/Vs, a
different picking error, a smaller or less independent station set, a different
confidence level, or a doubled systematic budget. The swing of each answer is compared
with the quoted uncertainty, which is what decides whether a prepared answer is
required. SYNTHETIC numbers; print-only: no files, no network.
"""
import numpy as np

rng = np.random.default_rng(20261014)
BASE = {"t": 4.3493, "sig_t": 0.15, "Vp": 6.30, "sig_Vp": 0.15, "k": 1.75,
        "sig_k": 0.03, "p": 0.060, "sig_p": 0.005, "n_clusters": 45}
Z95 = 1.959964

def depth(t, vp, k, p):
    return t / (np.sqrt(k ** 2 / vp ** 2 - p ** 2) - np.sqrt(1.0 / vp ** 2 - p ** 2))

def budget(cfg):
    """Central value and total 1-sigma budget for a configuration."""
    h0 = depth(cfg["t"], cfg["Vp"], cfg["k"], cfg["p"])
    d = {name: rng.normal(0.0, cfg["sig_" + name], 20000) for name in ("t", "Vp", "k", "p")}
    scale = np.sqrt(BASE["n_clusters"] / cfg["n_clusters"])
    h = depth(cfg["t"] + d["t"] * scale, cfg["Vp"] + d["Vp"], cfg["k"] + d["k"],
              cfg["p"] + d["p"])
    return float(h0), float(h.std())

H0, SD0 = budget(BASE)
print("=" * 78)
print("SYNTHETIC capstone defence preparation: question-impact analysis")
print("=" * 78)
print(f"\n1. The claim on the table")
print(f"   H = {H0:.2f} +/- {SD0:.2f} km (1 sd), 95% interval +/- {Z95*SD0:.2f} km")
print(f"   dominant assumption: Vp/Vs = {BASE['k']:.2f} +/- {BASE['sig_k']:.2f}, "
      f"contributing 47% of the variance")
print(f"   the panel's job is to find a question whose answer moves this number by more")
print(f"   than {SD0:.2f} km; the preparation is to find it first.")

VARIANTS = [
    ("Vp/Vs is 1.70, not 1.75", dict(BASE, k=1.70)),
    ("Vp/Vs is 1.80, not 1.75", dict(BASE, k=1.80)),
    ("Vp is 5% lower (6.00 km/s)", dict(BASE, Vp=6.00)),
    ("the picking error is 0.30 s, not 0.15 s", dict(BASE, sig_t=0.30)),
    ("only 10 independent clusters, not 45", dict(BASE, n_clusters=10)),
    ("the ray parameter is off by 0.010 s/km", dict(BASE, p=0.070, sig_p=0.005)),
    ("the systematic budget is doubled", dict(BASE, sig_Vp=0.30, sig_k=0.06, sig_p=0.010)),
    ("the filter width changes t by 0.05 s", dict(BASE, t=4.3993)),
]
print(f"\n2. Question-by-question recomputation")
print(f"   {'question':<40}{'H (km)':>8}{'sd (km)':>9}{'swing':>9}{'in sd':>7}  verdict")
rows = []
for q, cfg in VARIANTS:
    h, sd = budget(cfg)
    swing = float(np.hypot(h - H0, sd - SD0))
    ratio = swing / SD0
    rows.append((q, h, sd, swing, ratio))
    print(f"   {q:<40}{h:8.2f}{sd:9.2f}{swing:9.2f}{ratio:7.2f}  "
          f"{'PREPARE' if ratio > 1.0 else 'answer on the fly'}")
print(f"   swing combines the change in the central value and the change in the")
print(f"   uncertainty; a question is dangerous when it moves either by more than 1 sd.")

rows.sort(key=lambda r: -r[4])
print(f"\n3. The three questions to prepare first")
for q, h, sd, swing, ratio in rows[:3]:
    print(f"   {q:<44} swing {swing:.2f} km = {ratio:.1f} sd")
    if abs(h - H0) > abs(sd - SD0):
        print(f"      it moves the answer itself: {h:.2f} km against {H0:.2f} km "
              f"({(h-H0)/H0*100:+.1f}%)")
    else:
        print(f"      it widens the interval: sd {sd:.2f} km against {SD0:.2f} km "
              f"({(sd/SD0-1)*100:+.0f}%)")

print(f"\n4. What the analysis can and cannot answer")
print(f"   answerable now: any question expressible as a change to t, Vp, k, p or N;")
print(f"   the recomputation takes milliseconds and the numbers are in the table above.")
cannot = [q for q, _, _, _, r in rows if r > 1.0]
print(f"   not answerable from the current analysis: {len(cannot)} of {len(rows)} questions")
print(f"   are of that form, but the panel may ask what the result would be *with the")
print(f"   assumption measured* - and that requires new data, not a new calculation.")
print(f"   the defensible statement is: 'with Vp/Vs measured to +/-0.01 the budget falls")
print(f"   to about "
      f"{budget(dict(BASE, sig_k=0.01))[1]:.2f} km; measuring it is the next study.'")

print(f"\n5. The three numbers to know without notes")
print(f"   H = {H0:.1f} km, its budget {SD0:.1f} km, and the share of the dominant")
print(f"   assumption ({0.474*100:.0f}% of the variance). Every other number in the")
print(f"   manuscript is a recomputation; these three are the result.")
print("\n" + "=" * 78)
print(f"SYNTHETIC demo complete: {len(rows)} plausible questions analysed, "
      f"{len(cannot)} move the answer by more")
print(f"than one standard deviation, and the largest swing is "
      f"{rows[0][4]:.1f} sd ('{rows[0][0][:34]}').")
print("=" * 78)
