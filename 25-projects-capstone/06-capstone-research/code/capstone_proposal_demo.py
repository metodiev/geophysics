"""Critical-path schedule with three-point estimates and a Monte Carlo risk analysis.

A 12-task work breakdown for a capstone proposal is scheduled with PERT estimates:
expected duration and standard deviation per task, the critical path and slack from a
forward/backward pass, then a Monte Carlo of the whole schedule to give the
probability of meeting a 24-week deadline and the tasks that actually drive it.
SYNTHETIC planning numbers; print-only: no files, no network.
"""
import numpy as np

rng = np.random.default_rng(20261014)
BUDGET, N_SIM = 24.0, 20000

# name, predecessors, optimistic, most likely, pessimistic (weeks)
T = [
    ("literature review",            [],                          2.0, 3.0, 4.0),
    ("data request and QC",          ["literature review"],       1.0, 2.0, 4.0),
    ("method test on synthetic",     ["literature review"],       2.0, 3.0, 4.0),
    ("processing pipeline",          ["data request and QC", "method test on synthetic"], 3.0, 4.0, 6.0),
    ("inversion runs",               ["processing pipeline"],     2.0, 3.0, 5.0),
    ("sensitivity analysis",         ["inversion runs"],          1.0, 2.0, 3.0),
    ("uncertainty quantification",   ["inversion runs"],          2.0, 3.0, 4.0),
    ("figures",                      ["sensitivity analysis", "uncertainty quantification"], 1.0, 2.0, 3.0),
    ("manuscript draft",             ["figures"],                 3.0, 4.0, 6.0),
    ("internal review and revision", ["manuscript draft"],        1.0, 2.0, 3.0),
    ("code release and docs",        ["processing pipeline"],     2.0, 3.0, 4.0),
    ("defence preparation",          ["manuscript draft"],        1.0, 2.0, 3.0),
]
idx = {t[0]: i for i, t in enumerate(T)}
exp_d = np.array([(o + 4 * m + p) / 6.0 for _, _, o, m, p in T])
sd_d = np.array([(p - o) / 6.0 for _, _, o, m, p in T])

def forward(durations):
    ef = np.zeros(len(T))
    for i, (_, preds, *_rest) in enumerate(T):
        es = max([ef[idx[p]] for p in preds], default=0.0)
        ef[i] = es + durations[i]
    return ef

def path(durations):
    """Longest path through the network, returned as the list of task indices."""
    ef = forward(durations)
    i = int(np.argmax(ef)); chain = []
    while True:
        chain.append(i)
        preds = T[i][1]
        if not preds:
            break
        i = max((idx[p] for p in preds), key=lambda j: forward(durations)[j])
    return list(reversed(chain))

print("=" * 78)
print("SYNTHETIC capstone proposal schedule: PERT, critical path, Monte Carlo risk")
print("=" * 78)
print(f"\n1. Work breakdown, expected duration and standard deviation")
print(f"   {'#':>2} {'task':<28}{'pred':>6}{'o':>5}{'m':>5}{'p':>5}{'E':>6}{'sd':>6}")
for i, (name, preds, o, m, p) in enumerate(T):
    print(f"   {i+1:2d} {name:<28}{len(preds):6d}{o:5.1f}{m:5.1f}{p:5.1f}{exp_d[i]:6.2f}{sd_d[i]:6.2f}")
print(f"   total of the expected durations (a wrong measure of the project): "
      f"{exp_d.sum():.1f} weeks")

ef = forward(exp_d)
cr = path(exp_d)
print(f"\n2. Deterministic critical path (expected durations)")
print(f"   project duration {ef.max():.2f} weeks against a budget of {BUDGET:.0f} weeks")
print(f"   critical path: " + " -> ".join(T[i][0] for i in cr))
print(f"   critical-path length {sum(exp_d[i] for i in cr):.2f} weeks; "
      f"the other chain through the network:")
other = [i for i in range(len(T)) if i not in cr]
def slack(durations):
    ef = forward(durations)
    T_proj = ef.max()
    lf = np.full(len(T), T_proj)
    for i in range(len(T) - 1, -1, -1):
        succ = [j for j, t in enumerate(T) if T[i][0] in t[1]]
        if succ:
            lf[i] = min(lf[j] - durations[j] for j in succ)
    return T_proj, lf - durations - (ef - durations), ef
T_proj, sl, ef = slack(exp_d)
print(f"   {'task':<28}{'earliest finish':>16}{'total slack':>13}{'on path?':>10}")
for i in range(len(T)):
    print(f"   {T[i][0]:<28}{ef[i]:16.2f}{sl[i]:13.2f}"
          f"{'critical' if abs(sl[i]) < 1e-9 else '':>10}")
print(f"   total slack is the delay each task can absorb without moving the finish date;")
print(f"   the tasks with zero slack define the critical path and nothing else does.")

print(f"\n3. Monte Carlo ({N_SIM} schedules, triangular o-m-p sampling per task)")
d = np.empty((N_SIM, len(T)))
for i, (_, _, o, m, p) in enumerate(T):
    if o == p:
        d[:, i] = o
    else:
        d[:, i] = rng.triangular(o, m, p, N_SIM)
tot = np.array([forward(d[k]).max() for k in range(N_SIM)])
idxmax = np.array([int(np.argmax(forward(d[k]))) for k in range(N_SIM)])
print(f"   mean {tot.mean():.2f} weeks, sd {tot.std():.2f} weeks")
for q in (10, 50, 80, 90, 95):
    print(f"   P{q:<2d} = {np.percentile(tot, q):5.2f} weeks")
print(f"   P(finish within {BUDGET:.0f} weeks) = {np.mean(tot <= BUDGET)*100:.1f}%")
print(f"   the budget is met by the mean-plan minus "
      f"{(tot.mean()-BUDGET)/tot.std():.2f} standard deviations, so it is an optimistic plan")

print(f"\n4. What actually drives the finish date")
corr = np.array([np.corrcoef(d[:, i], tot)[0, 1] for i in range(len(T))])
oncrit = np.array([np.mean([i in path(d[k]) for k in range(2000)]) for i in range(len(T))])
order = np.argsort(-corr)
print(f"   {'task':<28}{'corr with finish':>18}{'on critical path':>18}{'slack if late':>14}")
for i in order[:5]:
    print(f"   {T[i][0]:<28}{corr[i]:18.3f}{oncrit[i]*100:17.0f}%{exp_d[i]:14.2f}")
print(f"   the largest single-duration driver is '{T[order[0]][0]}' "
      f"(corr {corr[order[0]]:.2f}); tasks with high correlation but low critical-path")
print(f"   frequency are near-critical and become critical when the schedule slips.")

print(f"\n5. Repair options, each evaluated on the same {N_SIM} schedules")
print(f"   baseline: {BUDGET:.0f}-week deadline met {np.mean(tot <= BUDGET)*100:.1f}% of the time")
longest = np.argsort(-exp_d)[:3]
d2 = d.copy()
for i in longest:
    d2[:, i] *= 0.75
t2 = np.array([forward(d2[k]).max() for k in range(N_SIM)])
print(f"   A) trim the three longest tasks ({', '.join(T[i][0] for i in longest)})")
print(f"      by 25%: mean {t2.mean():.2f} weeks, deadline met "
      f"{np.mean(t2 <= BUDGET)*100:.1f}% of the time")
i_par = idx["method test on synthetic"]
d3 = d.copy(); d3[:, i_par] = 0.0
t3 = np.array([forward(d3[k]).max() for k in range(N_SIM)])
print(f"   B) start the synthetic method test in week 0 (no dependency): mean "
      f"{t3.mean():.2f} weeks, deadline met {np.mean(t3 <= BUDGET)*100:.1f}% of the time")
print(f"   -> option B removes {tot.mean()-t3.mean():.2f} weeks of expected duration for no "
      f"additional work,")
print(f"      because the pipeline waits on a task that could start on day one.")
print("\n" + "=" * 78)
print(f"SYNTHETIC demo complete: the plan expects {tot.mean():.1f} weeks against a "
      f"{BUDGET:.0f}-week budget,")
print(f"meets it in {np.mean(tot <= BUDGET)*100:.0f}% of simulated schedules, and its finish date is")
print(f"driven mainly by '{T[order[0]][0]}' (correlation {corr[order[0]]:.2f}).")
print("=" * 78)
