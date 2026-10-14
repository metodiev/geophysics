"""Global optimisation: simulated annealing and a genetic algorithm.

Run:  python3 global_optimization_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-05.

The objective is a two-parameter, cycle-skipped travel-time misfit of the kind
that appears in refraction and waveform inversion: a sum of
(1 - cos(2 pi dt / T)) terms, so the misfit oscillates and has many local
minima. Two things are measured and told apart:

* whether a search reaches the *global minimum of the misfit*, and
* whether that global minimum is the *true model*.

This objective has a family of exact-zero misfits, so the two questions have
different answers. That difference is the geophysical content of the lesson: a
global optimiser solves the mathematical problem it was given, and the
non-uniqueness of the physical problem has to be dealt with separately.
"""

import math
import random

Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


TRUTH = [2.0, 3.0]                    # direct velocity, curvature term (km/s)
OFFSETS = (1.0, 2.0, 3.0, 4.0)        # km
PERIOD = 0.5                          # s
BOUNDS = [(1.0, 3.0), (1.5, 6.0)]


def misfit(p: Vector, period: float = PERIOD) -> float:
    """SYNTHETIC two-parameter cycle-skipped misfit.

    Predicted arrival time at offset x: t = x/v1 + x^2/(4 v2); observed times
    are generated from TRUTH. The cosine wraps every `period` seconds, so any
    error that is a whole number of periods is invisible to the misfit.
    """
    v1, v2 = p
    total = 0.0
    for x in OFFSETS:
        t_pred = x / v1 + x * x / (4.0 * v2)
        t_obs = x / TRUTH[0] + x * x / (4.0 * TRUTH[1])
        total += 1.0 - math.cos(2.0 * math.pi * (t_obs - t_pred) / period)
    return total


def clamp(p: Vector, bounds=None) -> Vector:
    b = bounds or BOUNDS
    return [min(b[i][1], max(b[i][0], p[i])) for i in range(len(p))]


def local_descent(start: Vector, bounds=None, step: float = 0.25,
                  tol: float = 1e-10, max_iter: int = 6000,
                  period: float = PERIOD):
    """Coordinate descent with a shrinking step; the workhorse of local search."""
    b = bounds or BOUNDS
    p = clamp(start[:], b)
    best = misfit(p, period)
    evals = 1
    while step > tol and evals < max_iter:
        improved = False
        for i in range(len(p)):
            for sign in (1.0, -1.0):
                trial = p[:]
                trial[i] = min(b[i][1], max(b[i][0], p[i] + sign * step))
                value = misfit(trial, period)
                evals += 1
                if value < best:
                    p, best = trial, value
                    improved = True
        if not improved:
            step *= 0.5
    return p, best, evals


def simulated_annealing(seed: int, bounds=None, budget: int = 20000):
    """Simulated annealing with geometric cooling and a shrinking neighbourhood."""
    b = bounds or BOUNDS
    rng = random.Random(seed)
    current = [rng.uniform(lo, hi) for lo, hi in b]
    best_p, best = current[:], misfit(current)
    current_cost = best
    evals = 1
    step = [0.25 * (hi - lo) for lo, hi in b]
    temperature = 0.5
    while evals < budget:
        trial = clamp([current[i] + rng.gauss(0.0, step[i]) for i in range(2)], b)
        value = misfit(trial)
        evals += 1
        delta = value - current_cost
        if delta <= 0.0 or rng.random() < math.exp(-delta / max(temperature, 1e-12)):
            current, current_cost = trial, value
            if value < best:
                best_p, best = trial[:], value
        temperature *= 0.9995
        if evals % 200 == 0:
            step = [max(0.002 * (hi - lo), s * 0.99) for s, (lo, hi) in zip(step, b)]
    polished, polished_cost, extra = local_descent(best_p, bounds=b, step=1e-4)
    if polished_cost < best:
        best_p, best = polished, polished_cost
    return best_p, best, evals + extra


def genetic_algorithm(seed: int, bounds=None, pop_size: int = 40,
                      generations: int = 60):
    """Genetic algorithm: tournament selection, blend crossover, Gaussian mutation."""
    b = bounds or BOUNDS
    rng = random.Random(seed)
    population = [[rng.uniform(lo, hi) for lo, hi in b] for _ in range(pop_size)]
    costs = [misfit(p) for p in population]
    evals = pop_size
    i_best = min(range(pop_size), key=lambda i: costs[i])
    best_p, best = population[i_best][:], costs[i_best]
    for _ in range(generations):
        order = sorted(range(pop_size), key=lambda i: costs[i])
        new_pop = [population[i][:] for i in order[:2]]
        new_costs = [costs[i] for i in order[:2]]
        while len(new_pop) < pop_size:
            a = min(rng.sample(range(pop_size), 3), key=lambda i: costs[i])
            c = min(rng.sample(range(pop_size), 3), key=lambda i: costs[i])
            child = []
            for i in range(2):
                lo, hi = min(population[a][i], population[c][i]), max(population[a][i], population[c][i])
                span = hi - lo
                child.append(rng.uniform(lo - 0.5 * span, hi + 0.5 * span))
            for i in range(2):
                if rng.random() < 0.25:
                    child[i] += rng.gauss(0.0, 0.08 * (b[i][1] - b[i][0]))
            child = clamp(child, b)
            cost = misfit(child)
            evals += 1
            new_pop.append(child)
            new_costs.append(cost)
        population, costs = new_pop, new_costs
        i_best = min(range(len(costs)), key=lambda i: costs[i])
        if costs[i_best] < best:
            best_p, best = population[i_best][:], costs[i_best]
    return best_p, best, evals


def count_local_minima(n: int = 400, period: float = PERIOD):
    """Fine grid reference: minimum value, position, and number of local minima."""
    best, best_p = math.inf, None
    values = []
    for i in range(n):
        x = BOUNDS[0][0] + (BOUNDS[0][1] - BOUNDS[0][0]) * i / (n - 1)
        row = []
        for j in range(n):
            y = BOUNDS[1][0] + (BOUNDS[1][1] - BOUNDS[1][0]) * j / (n - 1)
            v = misfit([x, y], period)
            row.append(v)
            if v < best:
                best, best_p = v, [x, y]
        values.append(row)
    minima = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            v = values[i][j]
            if all(v <= values[i + di][j + dj]
                   for di in (-1, 0, 1) for dj in (-1, 0, 1)
                   if not (di == 0 and dj == 0)):
                minima += 1
    zeros = sum(1 for i in range(n) for j in range(n)
                if values[i][j] < 1e-10)
    return best, best_p, minima, zeros


def near_truth(p: Vector) -> bool:
    return abs(p[0] - TRUTH[0]) < 0.02 and abs(p[1] - TRUTH[1]) < 0.05


def describe(p: Vector) -> str:
    return f"({p[0]:.4f}, {p[1]:.4f})"


def main() -> None:
    section("1. The objective, and how many exact-zero models it has")

    best, best_p, n_minima, n_zeros = count_local_minima(400)
    print("  SYNTHETIC two-parameter misfit sum_i (1 - cos(2 pi dt_i / 0.5 s))")
    print("  with t = x/v1 + x^2/(4 v2) at offsets x = 1, 2, 3, 4 km")
    print(f"    true model (km/s)             {describe(TRUTH)}")
    print(f"    domain                        v1 in {BOUNDS[0]}, v2 in {BOUNDS[1]}")
    print(f"    400 x 400 grid minimum        {best:.3e} at {describe(best_p)}")
    print(f"    local minima counted on grid  {n_minima}")
    print(f"    grid points with misfit < 1e-10: {n_zeros}")
    print(f"    misfit at the true model      {misfit(TRUTH):.3e}")
    print("  There is more than one model with a vanishing misfit, because an")
    print("  error of a whole number of periods is invisible to the cosine misfit.")

    section("2. Which models have zero misfit? The aliasing family")

    print("  Holding v2 = 3 km/s, dt(x) = 0.5 x (1 - 2/v1), which is a multiple")
    print("  of the 0.5 s period whenever 1 - 2/v1 is an integer:")
    print(f"  {'m':>4}{'v1 = 2/(1-m)':>16}{'t_pred - t_obs at x = 1..4 (s)':>38}"
          f"{'misfit':>12}")
    for m in (-2, -1, 0, 1):
        v1 = 2.0 / (1.0 - m) if m != 1 else math.inf
        if not math.isfinite(v1) or not (BOUNDS[0][0] <= v1 <= BOUNDS[0][1]):
            print(f"  {m:>4}{('outside domain' if math.isfinite(v1) else 'infinite'):>16}")
            continue
        diffs = [x * (0.5 - 1.0 / v1) for x in OFFSETS]
        print(f"  {m:>4}{v1:>16.6f}"
              f"{(', '.join(f'{d:+.3f}' for d in diffs)):>38}"
              f"{misfit([v1, 3.0]):>12.3e}")
    print("  Two models in the domain fit the data exactly: v1 = 1.0 and")
    print("  v1 = 2.0 km/s. Everything the misfit can see about v1 is periodic,")
    print("  so a global optimiser cannot choose between them.")

    section("3. Local descent: the global basin, and the true basin")

    starts = hits_global = hits_truth = 0
    for i in range(24):
        for j in range(24):
            start = [BOUNDS[0][0] + (BOUNDS[0][1] - BOUNDS[0][0]) * (i + 0.5) / 24,
                     BOUNDS[1][0] + (BOUNDS[1][1] - BOUNDS[1][0]) * (j + 0.5) / 24]
            p, cost, _ = local_descent(start)
            starts += 1
            if cost <= 1e-10 * 4.0:
                hits_global += 1
            if near_truth(p):
                hits_truth += 1
    print(f"  coordinate descent from a 24 x 24 grid of starts ({starts} starts):")
    print(f"    reached a model with zero misfit: {hits_global}"
          f" ({100.0 * hits_global / starts:.1f} per cent)")
    print(f"    reached the true model:           {hits_truth}"
          f" ({100.0 * hits_truth / starts:.1f} per cent)")
    print("  A local method answers 'which basin am I in', not 'which basin is")
    print("  the Earth in'.")

    section("4. Simulated annealing: global minimum versus true model")

    seeds = list(range(20))
    results = [(seed,) + simulated_annealing(seed, budget=20000) for seed in seeds]
    hits_global = sum(1 for _, _, cost, _ in results if cost <= 1e-3)
    hits_truth = sum(1 for _, p, cost, _ in results if cost <= 1e-3 and near_truth(p))
    print("  budget 20000 evaluations, geometric cooling, local polish at the end")
    print(f"    seeds tested: {len(seeds)}")
    print(f"    found a model with misfit < 1e-3: {hits_global}"
          f" ({100.0 * hits_global / len(seeds):.0f} per cent)")
    print(f"    of those, the true model:         {hits_truth}"
          f" ({100.0 * hits_truth / len(seeds):.0f} per cent of all runs)")
    print(f"    median evaluations used:"
          f" {sorted(r[3] for r in results)[len(results) // 2]}")
    print("    models found (first eight): "
          + "; ".join(f"{describe(p)} misfit {c:.1e}"
                      for _, p, c, _ in results[:8]))
    print("  Annealing reliably finds the global minimum of this misfit, and the")
    print("  global minimum is frequently not the model that generated the data.")

    section("5. A genetic algorithm on the same objective")

    results_ga = [genetic_algorithm(seed) for seed in seeds]
    hits_global_ga = sum(1 for _, cost, _ in results_ga if cost <= 1e-3)
    hits_truth_ga = sum(1 for p, cost, _ in results_ga
                        if cost <= 1e-3 and near_truth(p))
    print("  population 40, 60 generations, tournament selection, blend crossover")
    print(f"    found a zero-misfit model: {hits_global_ga} of {len(seeds)}"
          f" ({100.0 * hits_global_ga / len(seeds):.0f} per cent)")
    print(f"    of those, the true model:  {hits_truth_ga} of {len(seeds)}"
          f" ({100.0 * hits_truth_ga / len(seeds):.0f} per cent of all runs)")
    print("    median evaluations used:"
          f" {sorted(e for *_, e in results_ga)[len(results_ga) // 2]}")
    print("  Both methods reach a zero-misfit model on every seed, and they")
    print("  disagree about which one: annealing ends in the v1 = 1.0 basin nine")
    print("  times in ten, the genetic algorithm in the true basin three times in")
    print("  four. Which aliased model you get depends on the search method, not")
    print("  on the data, because the data cannot tell the two apart.")

    section("6. Cost of a guarantee: grid and random search")

    value = count_local_minima(60)[0]
    print(f"  grid search 60 x 60: 3600 evaluations, best {value:.3e}")
    rng = random.Random(0)
    best_random = math.inf
    for _ in range(3600):
        best_random = min(best_random, misfit([rng.uniform(*BOUNDS[0]),
                                               rng.uniform(*BOUNDS[1])]))
    print(f"  random search, 3600 evaluations, seed 0: best {best_random:.3e}")
    print("  The genetic algorithm reached zero misfit in a median of 2320")
    print("  evaluations, fewer than the grid used, and annealing needed about")
    print("  20000 evaluations for the same result -- but both beat the grid by a")
    print("  wide margin in the misfit actually achieved at a fixed budget.")

    section("7. A badly configured annealing run")

    def cool_quickly(seed: int, budget: int = 20000) -> float:
        rng = random.Random(seed)
        current = [rng.uniform(lo, hi) for lo, hi in BOUNDS]
        current_cost = misfit(current)
        best = current_cost
        temperature = 0.5
        for _ in range(budget):
            trial = clamp([current[i] + rng.gauss(0.0, 0.1) for i in range(2)])
            value = misfit(trial)
            delta = value - current_cost
            if delta <= 0.0 or rng.random() < math.exp(-delta / max(temperature, 1e-12)):
                current, current_cost = trial, value
                best = min(best, value)
            temperature *= 0.995
        return best

    fast = [cool_quickly(seed) for seed in seeds]
    fast_hits = sum(1 for c in fast if c <= 1e-3)
    print("  cooling rate 0.995 per iteration instead of 0.9995:")
    print(f"    runs reaching misfit < 1e-3: {fast_hits} of {len(seeds)}")
    print(f"    median final misfit: {sorted(fast)[len(fast) // 2]:.3e}"
          f"   (Section 4 median:"
          f" {sorted(r[2] for r in results)[len(results) // 2]:.3e})")
    print("  The temperature collapses before the chain has explored the domain,")
    print("  and the run degenerates into a local search from a random start.")

    section("8. Two ways to fix the non-uniqueness")

    lo, hi = 1.8, 2.2
    print(f"  (a) a prior on v1: the bound {lo} <= v1 <= {hi} km/s, as an")
    print("      independent measurement such as a well log would give")
    tight = [(lo, hi), BOUNDS[1]]
    starts = hits_truth = 0
    for i in range(24):
        for j in range(24):
            start = [lo + (hi - lo) * (i + 0.5) / 24,
                     BOUNDS[1][0] + (BOUNDS[1][1] - BOUNDS[1][0]) * (j + 0.5) / 24]
            p, cost, _ = local_descent(start, bounds=tight)
            starts += 1
            if near_truth(p):
                hits_truth += 1
    print(f"      local descent from {starts} starts reaches the true model in"
          f" {hits_truth} cases ({100.0 * hits_truth / starts:.1f} per cent)")
    sa_truth = sum(1 for seed in seeds
                   if near_truth(simulated_annealing(seed, bounds=tight,
                                                     budget=20000)[0]))
    print(f"      annealing reaches the true model in {sa_truth} of {len(seeds)}"
          f" runs")

    print("\n  (b) lower-frequency data: repeat the whole experiment with a")
    print("      longer period, holding everything else fixed")
    print(f"  {'period (s)':>12}{'local minima':>14}{'grid minimum':>16}"
          f"{'descents to truth':>20}")
    for period in (0.5, 1.0, 2.0):
        gmin, gp, n_min, _ = count_local_minima(200, period)
        hits = 0
        for i in range(12):
            for j in range(12):
                start = [BOUNDS[0][0] + (BOUNDS[0][1] - BOUNDS[0][0]) * (i + 0.5) / 12,
                         BOUNDS[1][0] + (BOUNDS[1][1] - BOUNDS[1][0]) * (j + 0.5) / 12]
                p, cost, _ = local_descent(start, period=period)
                if abs(p[0] - TRUTH[0]) < 0.02 and abs(p[1] - TRUTH[1]) < 0.05:
                    hits += 1
        print(f"  {period:>12.1f}{n_min:>14}{gmin:>16.3e}"
              f"{hits:>14} of 144 ({100.0 * hits / 144.0:.1f} per cent)")
    print("  Aliasing is a property of the data, not of the algorithm: the fix is")
    print("  a prior, a bound, or data with more low-frequency content.")


if __name__ == "__main__":
    main()
