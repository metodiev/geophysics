"""Random number generation and reproducible seeds.

Run:  .venv/bin/python random_demo.py
Requires: numpy only.

Companion to lesson 03-02-06. Everything generated here is SYNTHETIC noise: no
observed data is involved. The point of the script is that every stochastic
result is reproducible, so the numbers printed below can be checked.

The script:

1. Shows that two generators with the same seed give bit-identical output, and
   that generators with different seeds do not.
2. Demonstrates ``default_rng`` (the modern API) and contrasts it with the
   legacy global ``np.random.seed``, whose results depend on call order.
3. Adds seeded Gaussian noise to a synthetic trace and compares the measured
   moments with the nominal ones.
4. Draws from uniform, Poisson and choice/permutation, and checks the sample
   statistics against their analytic values.
5. Measures the 1/sqrt(N) convergence of the standard error of the mean.
"""

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


SEED = 20261014


def part1_reproducibility():
    section("1. Reproducibility: the same seed, bit for bit")

    a = np.random.default_rng(SEED).normal(size=5)
    b = np.random.default_rng(SEED).normal(size=5)
    c = np.random.default_rng(SEED + 1).normal(size=5)
    print(f"rng({SEED}).normal(size=5)   = {a}")
    print(f"rng({SEED}).normal(size=5)   = {b}")
    print(f"rng({SEED + 1}).normal(size=5) = {c}")
    print(f"a and b are identical     : {np.array_equal(a, b)}")
    print(f"a and c differ            : {not np.array_equal(a, c)}")
    print(f"a.tobytes() == b.tobytes(): {a.tobytes() == b.tobytes()}")

    rng = np.random.default_rng(SEED)
    first = rng.normal(size=3)
    rng = np.random.default_rng(SEED)
    drawn_twice = np.concatenate([rng.normal(size=2), rng.normal(size=1)])
    print(f"\nsplitting one stream two ways: "
          f"normal(2)+normal(1) == normal(3): "
          f"{np.array_equal(first, drawn_twice)}")
    print("  A generator is a STATE, not a function of the seed alone. Calling")
    print("  it advances the state, so the same seed reproduces a whole")
    print("  SEQUENCE, and only the sequence.")


def part2_legacy():
    section("2. The legacy global API and its call-order dependence")

    np.random.seed(SEED)
    legacy_a = np.random.normal(size=3)
    np.random.seed(SEED)
    _ = np.random.uniform(size=2)            # an unrelated draw consumes state
    legacy_b = np.random.normal(size=3)
    print(f"after seed({SEED}): normal(3)              = {legacy_a}")
    print(f"after seed({SEED}), uniform(2), normal(3)   = {legacy_b}")
    print(f"identical: {np.array_equal(legacy_a, legacy_b)}   <- they are not")
    print("\n  The legacy module-level functions share one global state, so")
    print("  adding a plotting routine that draws two numbers silently changes")
    print("  every later result. default_rng returns an independent, explicitly")
    print("  passed object; use it in all new code.")


def part3_noise_on_trace():
    section("3. Synthetic noise on a trace")

    rng = np.random.default_rng(SEED)
    n = 100_000
    nominal_sigma = 2.0                       # nT
    noise = rng.normal(loc=0.0, scale=nominal_sigma, size=n)
    print(f"nominal sigma       = {nominal_sigma} nT")
    print(f"sample mean         = {noise.mean():+.6f} nT")
    print(f"sample std (ddof=0) = {noise.std():.6f} nT")
    print(f"sample std (ddof=1) = {noise.std(ddof=1):.6f} nT")
    print(f"expected std of the mean = sigma/sqrt(n) = "
          f"{nominal_sigma / np.sqrt(n):.6f} nT")
    print(f"observed |mean|          = {abs(noise.mean()):.6f} nT")
    print(f"skewness (g1)       = {((noise - noise.mean()) ** 3).mean() / noise.std() ** 3:+.6f}")
    print(f"excess kurtosis     = "
          f"{((noise - noise.mean()) ** 4).mean() / noise.std() ** 4 - 3:+.6f}")
    print("\n  For a Gaussian sample the last two are 0 +- sqrt(6/n) and")
    print("  0 +- sqrt(24/n) respectively; both are consistent with zero here.")
    print("  The ddof difference (1 vs 0) is a systematic factor n/(n-1):")
    print("  NumPy defaults to ddof=0 while many texts quote ddof=1.")


def part4_distributions():
    section("4. The distributions a geophysicist actually samples")

    rng = np.random.default_rng(SEED)

    u = rng.uniform(low=0.0, high=1.0, size=200_000)
    print(f"uniform   : mean {u.mean():.6f} (nominal 0.5), "
          f"std {u.std():.6f} (nominal {1 / np.sqrt(12):.6f})")

    counts = rng.poisson(lam=4.0, size=200_000)      # e.g. events per box
    print(f"poisson(4): mean {counts.mean():.6f} (nominal 4), "
          f"var  {counts.var():.6f} (nominal 4)")

    picked = rng.choice(np.arange(10), size=200_000, replace=True)
    print(f"choice    : frequencies = "
          f"{np.bincount(picked) / 200_000}  (nominal 0.1 each)")

    deck = np.arange(52)
    perm = rng.permutation(deck)
    print(f"permutation of 0..51 is a permutation: "
          f"{np.array_equal(np.sort(perm), deck)}")
    print(f"first 10 of the shuffled order: {perm[:10]}")

    print("\n  Poisson counts come from rng.poisson; 'events in a cell' is")
    print("  Poisson only if events are independent and the rate is constant,")
    print("  which earthquakes globally are not (aftershocks cluster). State")
    print("  the assumption next to the draw.")


def part5_convergence():
    section("5. The 1/sqrt(N) law of the sample mean")

    rng = np.random.default_rng(SEED)
    sigma = 3.0
    print(f"{'N':>10}{'observed std of mean':>24}{'sigma/sqrt(N)':>18}"
          f"{'ratio':>10}")
    for n in (10 ** 2, 10 ** 4, 10 ** 6):
        reps = 400
        sample = rng.normal(0.0, sigma, size=(reps, n))
        means = sample.mean(axis=1)
        expected = sigma / np.sqrt(n)
        print(f"{n:>10}{means.std(ddof=1):>24.6f}{expected:>18.6f}"
              f"{means.std(ddof=1) / expected:>10.3f}")
    print("\n  Each ten-thousandfold increase in N cuts the spread of the mean")
    print("  by a factor of 100 -- the 1/sqrt(N) rule. It is why characterising")
    print("  a background noise level to 1 per cent needs ~10^4 samples.")


def main():
    print("NumPy random generation -- companion to lesson 03-02-06")
    print(f"numpy version: {np.__version__}, SEED = {SEED}")
    part1_reproducibility()
    part2_legacy()
    part3_noise_on_trace()
    part4_distributions()
    part5_convergence()


if __name__ == "__main__":
    main()
