"""Probability axioms, conditional probability and Bayes' rule in geophysics.

Run:  python3 probability_axioms.py
Requires: Python standard library only.
Random seed: 20240117 (fixed, so every number below is reproducible).

Companion to lesson 01-13-01.

Every number in this script is either (a) an exactly computed quantity, or
(b) an *illustrative input* of a worked example. The detection sensitivities,
specificities and priors are chosen to make a point legible; they are not
measurements of any real instrument or prospect. Where a simulation reproduces
an analytic value, both are printed so the agreement can be judged.
"""

import random

SEED = 20240117


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


# --------------------------------------------------------------------------
# 1. The axioms, used rather than stated
# --------------------------------------------------------------------------

def axiom_arithmetic() -> None:
    section("1. The axioms in practice: complement, intersection, union")
    # Two independent seismic stations each register a regional event with
    # probability 0.85 (illustrative trigger probability).
    p_single = 0.85
    p_miss = 1.0 - p_single
    p_at_least_one = 1.0 - p_miss ** 2
    p_both = p_single ** 2
    p_union_direct = p_single + p_single - p_both
    print(f"  P(station triggers)              = {p_single}")
    print(f"  Axiom 1 (complement): P(no trigger) = 1 - P(trigger) = {p_miss:.4f}")
    print(f"  Independence: P(both trigger)        = 0.85^2       = {p_both:.4f}")
    print(f"  P(at least one) = 1 - P(neither)     = 1 - 0.15^2   = {p_at_least_one:.4f}")
    print(f"  Inclusion-exclusion check: P(A)+P(B)-P(A and B)     = {p_union_direct:.4f}")
    print("  The two routes agree because independence pins P(A and B).")


# --------------------------------------------------------------------------
# 2. Conditional probability and the multiplication rule
# --------------------------------------------------------------------------

def conditional_example() -> float:
    section("2. Conditional probability: a two-hypothesis subsurface model")
    # H1: a low-velocity wedge is present.  H2: the section is layered flat.
    # d : an observed travel-time residual larger than the array noise level.
    prior = {"H1": 0.40, "H2": 0.60}
    # Illustrative likelihoods of seeing the residual under each model.
    likelihood = {"H1": 0.70, "H2": 0.20}
    evidence = sum(prior[h] * likelihood[h] for h in prior)
    posterior = {h: prior[h] * likelihood[h] / evidence for h in prior}
    print(f"  Priors      P(H1) = {prior['H1']:.2f}   P(H2) = {prior['H2']:.2f}")
    print(f"  Likelihoods P(d|H1) = {likelihood['H1']:.2f}   P(d|H2) = {likelihood['H2']:.2f}")
    print(f"  Evidence    P(d) = 0.40*0.70 + 0.60*0.20 = {evidence:.4f}")
    print(f"  Posterior   P(H1|d) = 0.28/0.28... = {posterior['H1']:.6f}")
    print(f"              P(H2|d) = {posterior['H2']:.6f}   (sums to "
          f"{sum(posterior.values()):.1f})")
    return posterior["H1"]


# --------------------------------------------------------------------------
# 3. Sequential updating: today's posterior is tomorrow's prior
# --------------------------------------------------------------------------

def sequential_update(p1: float) -> None:
    section("3. Sequential updating with a second independent measurement")
    likelihood = {"H1": 0.70, "H2": 0.20}
    prior = {"H1": p1, "H2": 1.0 - p1}
    evidence = sum(prior[h] * likelihood[h] for h in prior)
    post = {h: prior[h] * likelihood[h] / evidence for h in prior}
    print(f"  Prior (from measurement 1): P(H1) = {prior['H1']:.6f}")
    print(f"  Evidence P(d2) = {evidence:.6f}")
    print(f"  Posterior P(H1|d1,d2) = {post['H1']:.6f}")
    print("  Order does not matter: the two measurements commute, and only the")
    print("  product of likelihoods enters. Bayes' rule is a bookkeeping device")
    print("  for evidence, not a recipe that depends on the order of arrival.")


# --------------------------------------------------------------------------
# 4. Base rates: why rare-target detection is hard
# --------------------------------------------------------------------------

def base_rate(prevalence: float, sensitivity: float, specificity: float) -> dict:
    p_target = prevalence
    p_none = 1.0 - prevalence
    p_pos = sensitivity * p_target + (1.0 - specificity) * p_none
    ppv = sensitivity * p_target / p_pos
    npv = specificity * p_none / (1.0 - p_pos)
    return {"p_pos": p_pos, "ppv": ppv, "npv": npv}


def base_rates() -> None:
    section("4. Base rates: the arithmetic that makes rare targets hard")
    for specificity in (0.90, 0.99):
        r = base_rate(0.01, 0.95, specificity)
        print(f"  prevalence 0.010, sensitivity 0.950, specificity {specificity:.2f}")
        print(f"    P(positive test)          = {r['p_pos']:.6f}")
        print(f"    P(target | positive) PPV  = {r['ppv']:.6f}  "
              f"({100 * r['ppv']:.2f} % of 'hits' are real)")
        print(f"    P(no target | negative)   = {r['npv']:.6f}")
    print("  Raising specificity from 0.90 to 0.99 lifts the positive predictive")
    print("  value from under one in ten to about one in two. When the target is")
    print("  rare, the false-positive rate dominates the answer.")


# --------------------------------------------------------------------------
# 5. Monte Carlo verification of Bayes' rule
# --------------------------------------------------------------------------

def monte_carlo_bayes(prevalence: float, sensitivity: float, specificity: float,
                      trials: int, rng: random.Random) -> tuple:
    positives = 0
    true_positives = 0
    for _ in range(trials):
        target = rng.random() < prevalence
        if target:
            hit = rng.random() < sensitivity
        else:
            hit = rng.random() >= specificity  # false positive
        if hit:
            positives += 1
            if target:
                true_positives += 1
    return positives, true_positives


def bayes_simulation() -> None:
    section("5. Monte Carlo check of the base-rate arithmetic (seed 20240117)")
    trials = 1_000_000
    rng = random.Random(SEED)
    positives, tps = monte_carlo_bayes(0.01, 0.95, 0.90, trials, rng)
    analytic = base_rate(0.01, 0.95, 0.90)
    observed_ppv = tps / positives
    print(f"  simulated trials            = {trials:,}")
    print(f"  simulated positives         = {positives:,}")
    print(f"  analytic P(positive)        = {analytic['p_pos']:.6f}")
    print(f"  simulated P(positive)       = {positives / trials:.6f}")
    print(f"  analytic PPV                = {analytic['ppv']:.6f}")
    print(f"  simulated PPV               = {observed_ppv:.6f}")
    print(f"  absolute difference in PPV  = {abs(observed_ppv - analytic['ppv']):.6f}")
    se = (analytic["ppv"] * (1 - analytic["ppv"]) / positives) ** 0.5
    print(f"  standard error of simulated PPV = {se:.6f}  "
          f"({abs(observed_ppv - analytic['ppv']) / se:.2f} SE)")


# --------------------------------------------------------------------------
# 6. Simulation of the two-hypothesis update
# --------------------------------------------------------------------------

def simulate_update(prior: float, likelihood: dict, trials: int,
                    rng: random.Random) -> float:
    h1_count = 0
    observed_d = 0
    for _ in range(trials):
        h1 = rng.random() < prior
        key = "H1" if h1 else "H2"
        if rng.random() < likelihood[key]:
            observed_d += 1
            if h1:
                h1_count += 1
    return h1_count / observed_d


def update_simulation() -> None:
    section("6. Simulating the subsurface update of Section 2")
    trials = 1_000_000
    rng = random.Random(SEED + 1)
    likelihood = {"H1": 0.70, "H2": 0.20}
    observed = simulate_update(0.40, likelihood, trials, rng)
    analytic = 0.40 * 0.70 / (0.40 * 0.70 + 0.60 * 0.20)
    print(f"  trials                     = {trials:,}")
    print(f"  analytic  P(H1|d)          = {analytic:.6f}")
    print(f"  simulated P(H1|d)          = {observed:.6f}")
    print(f"  difference                 = {abs(observed - analytic):.6f}")


def main() -> None:
    axiom_arithmetic()
    p1 = conditional_example()
    sequential_update(p1)
    base_rates()
    bayes_simulation()
    update_simulation()
    print("\nDone. All figures above are reproducible with seed 20240117.")


if __name__ == "__main__":
    main()
