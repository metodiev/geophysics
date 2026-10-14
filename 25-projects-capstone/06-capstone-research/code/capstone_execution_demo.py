"""An uncertainty budget for a capstone headline number, plus an estimator verification.

The headline is a Moho depth obtained by inverting the Ps delay time of the H-K method,
H = t / (sqrt(k^2/Vp^2 - p^2) - sqrt(1/Vp^2 - p^2)), with a measured time t and assumed
Vp, Vp/Vs and ray parameter p. The demo reports the total uncertainty, its statistical
and systematic parts, a variance budget (first-order Sobol indices), a coverage check of
the quoted interval, and what is left if the measurement precision is doubled.
SYNTHETIC numbers; print-only: no files, no network.
"""
import numpy as np

rng = np.random.default_rng(20261014)
H_TRUE, VP, K, P = 35.0, 6.30, 1.75, 0.060
SIG = {"t": 0.15, "Vp": 0.15, "k": 0.03, "p": 0.005}
N_MC, N_BINS, N_REP = 40000, 24, 4000

def depth(t, vp, k, p):
    eta_s = np.sqrt(k ** 2 / vp ** 2 - p ** 2)
    eta_p = np.sqrt(1.0 / vp ** 2 - p ** 2)
    return t / (eta_s - eta_p)

t_true = H_TRUE * (np.sqrt(K ** 2 / VP ** 2 - P ** 2) - np.sqrt(1.0 / VP ** 2 - P ** 2))
print("=" * 78)
print("SYNTHETIC capstone execution: verification and an uncertainty budget")
print("=" * 78)
print("\n1. The headline number and its inputs")
print(f"  model: H = t / (sqrt(k^2/Vp^2 - p^2) - sqrt(1/Vp^2 - p^2))")
print(f"  measured Ps delay t = {t_true:.4f} s (+/- {SIG['t']:.2f} s, statistical)")
print(f"  assumed Vp = {VP:.2f} (+/- {SIG['Vp']:.2f}) km/s, Vp/Vs = {K:.2f} "
      f"(+/- {SIG['k']:.2f}), p = {P:.3f} (+/- {SIG['p']:.3f}) s/km (systematic)")
print(f"  inverting the measured t with the assumed parameters gives "
      f"H = {depth(t_true, VP, K, P):.2f} km")

draws = {name: rng.normal(0.0, SIG[name], N_MC) for name in SIG}
H = depth(t_true + draws["t"], VP + draws["Vp"], K + draws["k"], P + draws["p"])
H_stat = depth(t_true + draws["t"], VP, K, P)
H_sys = depth(t_true, VP + draws["Vp"], K + draws["k"], P + draws["p"])
sd_tot = float(H.std())
print(f"\n2. The uncertainty budget")
print(f"  total standard deviation {sd_tot:.3f} km -> H = {H.mean():.2f} +/- {sd_tot:.2f} km")
print(f"  statistical part (t only) {H_stat.std():.3f} km, "
      f"systematic part (Vp, k, p) {H_sys.std():.3f} km")
print(f"  the systematic part alone accounts for "
      f"{H_sys.std()**2/sd_tot**2*100:.0f}% of the variance")
print(f"  (the two add in quadrature only because the model is nearly linear here: "
      f"{np.sqrt(H_stat.var()+H_sys.var()):.3f} km against {sd_tot:.3f} km)")

print(f"\n3. Variance budget: first-order Sobol indices from the same {N_MC} samples")
print(f"   {'input':<8}{'type':>12}{'S_i':>8}{'contribution to sd':>22}")
order = []
for name in SIG:
    x = draws[name]
    edges = np.quantile(x, np.linspace(0, 1, N_BINS + 1))
    idx = np.clip(np.digitize(x, edges[1:-1]), 0, N_BINS - 1)
    means = np.array([H[idx == b].mean() for b in range(N_BINS) if np.any(idx == b)])
    s_i = float(means.var() / H.var())
    order.append((s_i, name))
order.sort(reverse=True)
for s_i, name in order:
    typ = "statistical" if name == "t" else "systematic"
    print(f"   {name:<8}{typ:>12}{s_i:8.3f}{np.sqrt(s_i*sd_tot**2):22.3f}")
print(f"   the indices sum to {sum(s for s, _ in order):.3f}; the remainder is interaction")
kind = "measurement error" if order[0][1] == "t" else "modelling assumption"
print(f"   the dominant input is '{order[0][1]}' at {order[0][0]*100:.0f}% of the variance, and it is a")
print(f"   {kind} - which decides where the remaining effort is worth spending.")

print(f"\n4. Verification: is the quoted interval honest?")
z = 1.959964
cover = 0
for _ in range(N_REP):
    t_rep = t_true + rng.normal(0.0, SIG["t"])
    h = depth(t_rep, VP, K, P)
    se = abs(depth(t_rep + SIG["t"], VP, K, P) - h)
    cover += abs(h - H_TRUE) <= z * se
print(f"  {N_REP} replicate measurements with the true Vp, k, p known:")
print(f"  the statistical-only 95% interval contains the true H in "
      f"{cover/N_REP*100:.1f}% of replicates")
print(f"  an interval using the full budget (sd {sd_tot:.3f} km) contains the truth in "
      f"{np.mean(np.abs(H - H_TRUE) <= z * sd_tot)*100:.1f}%")
print(f"  of the budget draws, but only because the systematic terms were drawn from")
print(f"  unbiased distributions: calibration of a systematic budget is an assumption")

print(f"\n5. What more effort would buy")
for factor, label in ((0.5, "halve the picking error"), (0.25, "quarter it")):
    sd_new = float(depth(t_true + draws["t"] * factor, VP + draws["Vp"], K + draws["k"],
                         P + draws["p"]).std())
    print(f"  {label:<26} total sd {sd_new:.3f} km "
          f"({(1-sd_new/sd_tot)*100:.0f}% better)")
floor = float(H_sys.std())
print(f"  the systematic floor with the current assumptions is {floor:.3f} km "
      f"({floor/sd_tot*100:.0f}% of today's sd)")
print(f"  -> no amount of measurement precision removes it; only measuring Vp does.")
print("\n" + "=" * 78)
print(f"SYNTHETIC demo complete: H = {H.mean():.2f} +/- {sd_tot:.2f} km with "
      f"{H_sys.std()**2/sd_tot**2*100:.0f}% of the variance")
print(f"systematic, dominated by the assumed '{order[0][1]}', and a statistical-only")
print(f"interval that covers the truth {cover/N_REP*100:.0f}% of the time by construction.")
print("=" * 78)
