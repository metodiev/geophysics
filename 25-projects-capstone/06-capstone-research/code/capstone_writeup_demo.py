"""A numerical-integrity audit of a manuscript against the analysis that produced it.

Every quantitative claim must trace to a value in the result registry, with the same
units, the same rounding and the same derivation. The audit recomputes each claim from
the registry, flags mismatches, checks that every cited figure and table exists, and
reports how much of the text is traceable. SYNTHETIC manuscript; print-only.
"""
import numpy as np

rng = np.random.default_rng(20261014)

REGISTRY = {
    "H_mean": (35.04, "km", "capstone_execution: mean of 40000 budget draws"),
    "H_sd": (2.001, "km", "capstone_execution: standard deviation of the budget"),
    "H_sd_stat": (1.198, "km", "capstone_execution: statistical part of the budget"),
    "H_sd_sys": (1.600, "km", "capstone_execution: systematic part of the budget"),
    "S_k": (0.474, "-", "capstone_execution: first-order Sobol index of Vp/Vs"),
    "S_t": (0.356, "-", "capstone_execution: first-order Sobol index of t"),
    "n_accepted": (45, "count", "fetch_waveforms: stations passing QC"),
    "n_requested": (52, "count", "fetch_waveforms: stations requested"),
    "t_ps": (4.3493, "s", "hk_grid: Ps delay at the reference station"),
    "n_sched": (20000, "count", "capstone_proposal: Monte Carlo schedules"),
}
FIGURES = {"figure_01_map", "figure_02_budget", "figure_03_schedule"}
TABLES = {"table_01_inputs", "table_02_budget", "table_03_schedule"}

VERDICTS = {}
def verdict_of(text):
    return VERDICTS.get(text, "flag")

def T(x):                      # normalised tolerance: rounding at the quoted precision
    return 0.006 * max(abs(x), 1e-9)

claims = [
    ("H = 35.04 +/- 2.00 km (1 sd)", 35.04,
     lambda: REGISTRY["H_mean"][0], ("H_mean",)),
    ("95% interval of +/- 3.92 km", 3.92,
     lambda: 1.959964 * REGISTRY["H_sd"][0], ("H_sd",)),
    ("95% interval of +/- 3.29 km (using z = 1.645)", 3.29,
     lambda: 1.959964 * REGISTRY["H_sd"][0], ("H_sd",)),
    ("the systematic term is 64% of the variance", 64.0,
     lambda: REGISTRY["H_sd_sys"][0] ** 2 / REGISTRY["H_sd"][0] ** 2 * 100, ("H_sd",)),
    ("the systematic term is 71% of the variance", 71.0,
     lambda: REGISTRY["H_sd_sys"][0] ** 2 / REGISTRY["H_sd"][0] ** 2 * 100, ("H_sd",)),
    ("the dominant input has Sobol index 0.474", 0.474,
     lambda: REGISTRY["S_k"][0], ("S_k",)),
    ("the ray-parameter index is 0.356", 0.356,
     lambda: REGISTRY["S_t"][0], ("S_t",)),
    ("45 of 52 stations passed QC (87%)", 87.0,
     lambda: REGISTRY["n_accepted"][0] / REGISTRY["n_requested"][0] * 100,
     ("n_accepted", "n_requested")),
    ("45 of 52 stations passed QC (92%)", 92.0,
     lambda: REGISTRY["n_accepted"][0] / REGISTRY["n_requested"][0] * 100,
     ("n_accepted", "n_requested")),
    ("the Ps delay is 4.35 s", 4.35, lambda: REGISTRY["t_ps"][0], ("t_ps",)),
    ("the budget exceeds 2400 m at 95%", 2400.0, lambda: 2000.0 * 1.2, ()),
    ("H = 35 km (see figure_04_resolution)", 35.0,
     lambda: REGISTRY["H_mean"][0], ("H_mean",)),
]

print("=" * 78)
print("SYNTHETIC manuscript numerical-integrity audit")
print("=" * 78)
print(f"\n1. Registry: {len(REGISTRY)} values, each with a unit and a provenance")
for k, (v, u, src) in REGISTRY.items():
    print(f"   {k:<12}{v:>10.4f} {u:<6} <- {src}")

print(f"\n2. Claim-by-claim recomputation")
print(f"   {'claim as written':<46}{'quoted':>9}{'recomputed':>12}  verdict")
n_flag, flags = 0, []
for text, quoted, expect_fn, refs in claims:
    expected = float(expect_fn())
    if not refs:
        verdict, note = "FLAG no provenance", "not traceable to any registry value"
    elif abs(quoted - expected) <= T(expected):
        verdict, note = "pass", ""
    else:
        verdict, note = "FLAG value", f"registry and derivation give {expected:.4g}"
    if "figure_" in text and note == "" and "figure_04" in text:
        verdict, note = "FLAG citation", "cited figure is not in the figure list"
    VERDICTS[text] = verdict
    if verdict != "pass":
        n_flag += 1
        flags.append((text, verdict, note))
    print(f"   {text[:44]:<46}{quoted:9.2f}{expected:12.4f}  {verdict}"
          + (f"  [{note}]" if note else ""))

print(f"\n3. Derived-quantity checks")
print(f"   quadrature of the budget parts: sqrt({REGISTRY['H_sd_stat'][0]:.3f}^2 + "
      f"{REGISTRY['H_sd_sys'][0]:.3f}^2) = "
      f"{np.hypot(REGISTRY['H_sd_stat'][0], REGISTRY['H_sd_sys'][0]):.3f} km against the "
      f"sampled {REGISTRY['H_sd'][0]:.3f} km")
print(f"   Sobol indices sum to {REGISTRY['S_k'][0]+REGISTRY['S_t'][0]+0.143+0.018:.3f}; the "
      f"manuscript must state the interaction remainder")
print(f"   unit conversion in the abstract: 2.00 km = 2000 m (the abstract quotes metres "
      f"and the figures kilometres)")

print(f"\n4. Citation audit")
print(f"   figures listed in the manuscript: {sorted(FIGURES)}")
print(f"   tables listed in the manuscript:  {sorted(TABLES)}")
cited_figs = set()
for text, _, _, _ in claims:
    for f in FIGURES | {"figure_04_resolution"}:
        if f in text:
            cited_figs.add(f)
print(f"   figures cited in the claim list:  {sorted(cited_figs)}")
print(f"   figures never cited: "
      f"{sorted(FIGURES - cited_figs) if FIGURES - cited_figs else 'none'}")

print(f"\n5. Audit summary")
print(f"   claims checked: {len(claims)}; passed: {len(claims)-n_flag}; flagged: {n_flag} "
      f"({n_flag/len(claims)*100:.0f}%)")
for text, verdict, note in flags:
    print(f"   - {verdict:<16} {text[:52]}" + (f"  [{note}]" if note else ""))
print(f"   traceability: {sum(1 for c in claims if c[3])/len(claims)*100:.0f}% of quantitative "
      f"claims carry a registry reference")
print(f"   the four flag classes are: wrong derivation (z = 1.645 instead of 1.96),")
print(f"   wrong quantity (a ratio reported as a variance share), a rounding or")
print(f"   arithmetic slip (92% instead of 87%), and an untraceable or miscited claim.")
print(f"   none of them is detectable by reading the manuscript alone.")
N_DRAW = 2000
print(f"\n6. Robustness of the audit to rounding at the quoted precision")
print(f"   {N_DRAW} perturbations of every quoted value, uniform within half a unit of")
print(f"   the last quoted digit; a claim flips verdict when the perturbation crosses")
print(f"   its tolerance")
flips = []
for text, quoted, expect_fn, refs in claims:
    if verdict_of(text) in ("FLAG citation", "FLAG no provenance"):
        flips.append((text, None)); continue
    expected = float(expect_fn())
    digit = 10.0 ** np.floor(np.log10(max(abs(quoted), 1e-9))) * 0.005
    ok = 0
    for _ in range(N_DRAW):
        q = quoted + rng.uniform(-digit, digit)
        passed = bool(refs) and abs(q - expected) <= T(expected)
        if passed == (verdict_of(text) == "pass"):
            ok += 1
    flips.append((text, ok / N_DRAW))
for text, rate in flips:
    shown = "n/a: not a rounding question" if rate is None else f"{rate*100:5.1f}% stable"
    print(f"   {text[:52]:<54}{shown:>12}")
print(f"   a flag that is stable at 100% is a real defect; a flag that flips is a")
print(f"   marginal rounding question and should be resolved by quoting more digits.")

print("\n" + "=" * 78)
print(f"SYNTHETIC demo complete: {len(claims)} quantitative claims audited against "
      f"{len(REGISTRY)} registry values,")
print(f"{n_flag} flagged before submission, every one of which would have reached a")
print("referee undetected without a recomputation.")
print("=" * 78)
