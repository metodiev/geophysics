#!/usr/bin/env python3
"""Ensemble design for model intercomparison: how the error of an ensemble mean
shrinks with the number of members, and why it stops shrinking at the
structural (inter-model) spread.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coupled_model_intercomparison_demo.py

All models and data in this file are SYNTHETIC.  The "models" are chosen
response coefficients, not real climate models, and no published intercomparison
number is quoted.  This file deliberately avoids naming any real model or
ensemble size, because none is used.

Contents
--------
1. Internal variability only: the error of the ensemble mean versus N.
2. Structural plus internal variability: a two-level ensemble and a variance
   decomposition.
3. Why a single-model large ensemble is overconfident.
4. Weighting: equal weights, member weights and inverse-variance weights.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

INTERNAL_SIGMA_K = 0.30            # SYNTHETIC internal variability per member
FORCING_W_M2 = 4.0                 # SYNTHETIC step forcing for the comparison
SENSITIVITIES_K_PER_W_M2 = (0.5, 0.8, 1.1)   # SYNTHETIC model sensitivities
MEMBER_COUNTS = (1, 5, 10, 25, 50, 100)
N_REALISATIONS = 4000


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Internal variability only: error of the ensemble mean versus N")
    print(f"  each member = truth + noise with sigma_internal = "
          f"{INTERNAL_SIGMA_K:.2f} K")
    print(f"  measured over {N_REALISATIONS} synthetic ensembles")
    print(f"  {'N':>5s} {'std of ensemble mean (K)':>26s} "
          f"{'sigma/sqrt(N) (K)':>19s} {'ratio':>7s}")
    for n in MEMBER_COUNTS:
        draws = INTERNAL_SIGMA_K * RNG.standard_normal((N_REALISATIONS, n))
        means = draws.mean(axis=1)
        measured = float(np.std(means, ddof=1))
        predicted = INTERNAL_SIGMA_K / np.sqrt(n)
        print(f"  {n:5d} {measured:26.4f} {predicted:19.4f} "
              f"{measured / predicted:7.3f}")
    print("  The ensemble-mean error falls as 1/sqrt(N). This is the only part of")
    print("  the uncertainty that more members can reduce.")

    section("2. Structural plus internal variability")
    sensitivities = np.array(SENSITIVITIES_K_PER_W_M2)
    model_means = sensitivities * FORCING_W_M2
    structural_std = float(np.std(model_means, ddof=1))
    print(f"  synthetic forcing F = {FORCING_W_M2:.1f} W/m^2")
    print(f"  model sensitivities dT_eq = lambda*F with lambda = "
          f"{', '.join(f'{s:.2f}' for s in sensitivities)} K/(W m^-2)")
    print(f"  model equilibrium responses: "
          f"{', '.join(f'{m:.3f}' for m in model_means)} K")
    print(f"  structural standard deviation across models = "
          f"{structural_std:.4f} K")
    print(f"  {'N per model':>12s} {'internal part (K)':>18s} "
          f"{'total spread (K)':>18s} {'total std (K)':>14s}")
    for n in (1, 10, 100, 1000):
        internal = INTERNAL_SIGMA_K / np.sqrt(n)
        total_variance = structural_std ** 2 + internal ** 2
        print(f"  {n:12d} {internal:18.4f} {np.sqrt(total_variance):18.4f} "
              f"{np.sqrt(total_variance):14.4f}")
    print("  total variance = (structural std)^2 + (internal std)^2/N. The second")
    print("  term vanishes with N; the first does not.")

    section("3. Why a single-model large ensemble is overconfident")
    single = model_means[0]
    n_large = 100
    internal_se = INTERNAL_SIGMA_K / np.sqrt(n_large)
    print(f"  one model with lambda = {sensitivities[0]:.2f} K/(W m^-2) and "
          f"{n_large} members")
    print(f"  its own standard error of the mean = {internal_se:.4f} K")
    print(f"  the spread between models               = {structural_std:.4f} K")
    print(f"  underestimate factor                    = "
          f"{structural_std / internal_se:.1f}x")
    print("  A large single-model ensemble measures internal variability only.")
    print("  Reporting its standard error as the uncertainty of the forced")
    print("  response understates the total by the factor above, because the")
    print("  structural term is absent by construction.")

    section("4. Weighting the members")
    members_equal = np.concatenate([
        model_mean + INTERNAL_SIGMA_K * RNG.standard_normal(50)
        * (1.0 + 0.5 * i) for i, model_mean in enumerate(model_means)])
    equal_weight = float(members_equal.mean())
    model_means_sampled = np.array([
        model_mean + INTERNAL_SIGMA_K * RNG.standard_normal(50)
        * (1.0 + 0.5 * i) for i, model_mean in enumerate(model_means)])
    grid_means = model_means_sampled.mean(axis=1)
    model_weight = float(grid_means.mean())
    inverse_variance = float(np.mean(
        grid_means / model_means_sampled.var(axis=1, ddof=1))
        / np.mean(1.0 / model_means_sampled.var(axis=1, ddof=1)))
    print(f"  three models, but model 1 has 1x, model 2 has 1.5x and model 3 has")
    print(f"  2x the internal noise amplitude (a synthetic 'ensemble of")
    print(f"  opportunity' in which models are not equally informative).")
    print(f"  member-weighted mean          = {equal_weight:.4f} K")
    print(f"  model-weighted (equal models) = {model_weight:.4f} K")
    print(f"  inverse-variance weighted     = {inverse_variance:.4f} K")
    print(f"  spread between weighting choices = "
          f"{max(equal_weight, model_weight, inverse_variance) - min(equal_weight, model_weight, inverse_variance):.4f} K")
    print("  When models are pooled with unequal member counts, 'all members equal'")
    print("  and 'all models equal' are different estimators. Neither is the truth;")
    print("  the choice must be stated, because it moves the answer.")


if __name__ == "__main__":
    main()
