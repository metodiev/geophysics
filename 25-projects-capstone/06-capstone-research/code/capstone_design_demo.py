"""Power analysis and a weight-sensitivity screen for six candidate capstone studies.

Each candidate is described by the effect it must detect, the single-measurement
uncertainty, the number of independent measurements, a data-availability score, a
method-maturity score and an effort in weeks. The screen computes the detectable
signal-to-noise ratio, the minimum detectable effect at the chosen power, a weighted
feasibility score, and how often each candidate wins under perturbed weights.
SYNTHETIC planning numbers; print-only: no files, no network.
"""
import numpy as np

rng = np.random.default_rng(20261014)
Z_ALPHA, Z_BETA = 1.96, 0.84          # 5% two-sided, 80% power

CAND = [
    # name, effect, unit, single-measurement sigma, N independent, data, method, weeks
    ("RF H-K stack, regional network", 1.5, "km Moho depth", 4.0, 20, 0.9, 0.9, 16),
    ("InSAR time series, deforming volcano", 0.8, "cm/yr uplift", 0.5, 120, 0.7, 0.6, 20),
    ("Joint gravity-seismic basin inversion", 0.015, "g/cm3 density contrast", 0.04, 30, 0.8, 0.5, 24),
    ("Ambient-noise monitoring, geothermal", 0.4, "% velocity change", 0.3, 200, 0.8, 0.7, 18),
    ("b-value mapping, regional catalogue", 0.15, "b-value difference", 0.12, 60, 1.0, 0.9, 12),
    ("3-D MT inversion, geothermal prospect", 0.15, "log10 resistivity", 0.35, 25, 0.5, 0.4, 28),
]
WEEKS_AVAILABLE = 24.0
W_BASE = {"detectability": 0.40, "data": 0.25, "method": 0.20, "effort": 0.15}

print("=" * 78)
print("SYNTHETIC capstone design screen: power analysis plus weight sensitivity")
print("=" * 78)
print(f"\n1. Assumptions")
print(f"   significance {Z_ALPHA:.2f} sigma (two-sided 5%), power {Z_BETA:.2f} sigma (80%)")
print(f"   time available: {WEEKS_AVAILABLE:.0f} weeks")
print(f"   detectable effect = (z_alpha + z_beta) * sigma / sqrt(N)")
print(f"\n2. Detectability of each candidate's hypothesised effect")
print(f"   {'candidate':<38}{'effect':>8}{'sigma':>7}{'N':>5}{'SNR':>7}{'MDE':>8}  unit")
rows = []
for name, eff, unit, sig, n, dat, meth, wk in CAND:
    se = sig / np.sqrt(n)
    snr = eff / se
    mde = (Z_ALPHA + Z_BETA) * se
    rows.append((name, eff, unit, sig, n, dat, meth, wk, se, snr, mde))
    flag = "" if eff >= mde else "  <- underpowered"
    print(f"   {name:<38}{eff:8.3f}{sig:7.2f}{n:5d}{snr:7.2f}{mde:8.3f}  {unit}{flag}")
print(f"   SNR = effect / (sigma/sqrt(N)); MDE = the smallest effect detectable at 80% power")

snr = np.array([r[9] for r in rows])
eff = np.array([r[1] for r in rows])
mde = np.array([r[10] for r in rows])
dat = np.array([r[5] for r in rows]); meth = np.array([r[6] for r in rows])
wk = np.array([r[7] for r in rows])
def norm(x):
    return (x - x.min()) / (x.max() - x.min())
det = norm(np.log(snr))                      # log-scaled: detectability spans 3 decades
eff_sc = np.clip(1.0 - (wk - WEEKS_AVAILABLE) / wk.max(), 0, 1)
def score(w):
    return (w["detectability"] * det + w["data"] * dat + w["method"] * meth
            + w["effort"] * eff_sc)
base = score(W_BASE)
order = np.argsort(-base)
print(f"\n3. Weighted feasibility score")
print(f"   weights: " + ", ".join(f"{k} {v:.2f}" for k, v in W_BASE.items()))
print(f"   {'rank':>4} {'candidate':<38}{'score':>7}{'SNR':>7}{'weeks':>7}{'fits?':>7}")
for j, i in enumerate(order):
    print(f"   {j+1:4d} {rows[i][0]:<38}{base[i]:7.3f}{snr[i]:7.2f}{wk[i]:7.0f}"
          f"{'yes' if wk[i] <= WEEKS_AVAILABLE else 'NO':>7}")

print(f"\n4. Is the ranking a property of the candidates or of the weights?")
N_DRAW = 500
wdraw = rng.dirichlet([4.0, 2.5, 2.0, 1.5], N_DRAW)
wins = np.zeros(len(rows)); top2 = np.zeros(len(rows)); scores = np.zeros((N_DRAW, len(rows)))
for d in range(N_DRAW):
    w = {"detectability": wdraw[d, 0], "data": wdraw[d, 1],
         "method": wdraw[d, 2], "effort": wdraw[d, 3]}
    sc = score(w)
    scores[d] = sc
    wins[int(np.argmax(sc))] += 1
    top2[np.argsort(-sc)[:2]] += 1
print(f"   {N_DRAW} Dirichlet-perturbed weight vectors centred on the stated weights")
print(f"   {'candidate':<38}{'wins':>7}{'top-2':>7}{'score range over draws':>24}")
for i in np.argsort(-wins):
    print(f"   {rows[i][0]:<38}{wins[i]/N_DRAW*100:6.1f}%{top2[i]/N_DRAW*100:6.1f}%"
          f"{scores[:, i].min():12.3f} to {scores[:, i].max():.3f}")
print(f"   the winner changes in {100*(1-wins.max()/N_DRAW):.0f}% of weightings: the top choice is")
print(f"   {'stable' if wins.max()/N_DRAW > 0.8 else 'weight-dependent'}; a candidate chosen on a "
      f"weight of 0.05 must not")
print(f"   be presented as the best study, only as the best under that weighting.")

print(f"\n5. What the design would have to change to be feasible")
feasible = [i for i in range(len(rows)) if wk[i] <= WEEKS_AVAILABLE]
print(f"   candidates inside the {WEEKS_AVAILABLE:.0f}-week budget: {len(feasible)} of {len(rows)}")
for i in range(len(rows)):
    if eff[i] < mde[i]:
        need = (mde[i] / eff[i]) ** 2
        print(f"   {rows[i][0][:36]:<38} underpowered: needs N > {need*rows[i][4]:.0f} "
              f"(has {rows[i][4]})")
    if wk[i] > WEEKS_AVAILABLE:
        print(f"   {rows[i][0][:36]:<38} over budget by {wk[i]-WEEKS_AVAILABLE:.0f} weeks")
viable = [i for i in range(len(rows)) if wk[i] <= WEEKS_AVAILABLE and eff[i] >= mde[i]]
robust = [i for i in viable if wins[i] / N_DRAW > 0.8]
print(f"\n   viable on all three counts (in budget, at power, robust to the weighting): "
      f"{len(robust)}")
print(f"   in budget and at power: {len(viable)}; of those, the best wins only "
      f"{max(wins[i] for i in viable)/N_DRAW*100:.0f}% of perturbed weightings, so the choice")
print("   between them is set by the weighting rather than by the analysis - a design")
print("   choice that must be stated, not implied.")
print("\n" + "=" * 78)
print(f"SYNTHETIC demo complete: the screen ranks {rows[order[0]][0]}")
print(f"first at the stated weights ({base[order[0]]:.3f}), it wins "
      f"{wins[order[0]]/N_DRAW*100:.0f}% of perturbed weightings, and")
print(f"{sum(1 for r in rows if r[1] < r[10])} of {len(rows)} candidates are underpowered.")
print("=" * 78)
