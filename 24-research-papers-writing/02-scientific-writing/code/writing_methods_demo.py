#!/usr/bin/env python3
"""Writing reproducible Methods: parameter sensitivity and reporting completeness.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_methods_demo.py

Everything here is SYNTHETIC.  The processing chain is a deliberately simple
analytic surrogate whose elasticities are chosen; no seismic data are processed
and no software is invoked.

Sections
--------
1. The surrogate chain and its six parameters.
2. Elasticities: output change per 10 % parameter change.
3. Reporting completeness: does a reader reproduce the number?
4. Which single parameter is worth reporting first?
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC chain: y = Y0 * exp(sum_i e_i * d_i), d_i a normalised deviation
Y0 = 100.0                     # reported quantity, percent of a reference value
PARAMETERS = (
    # name, nominal value, unit, plausible half-range, elasticity
    ("high-cut corner", 25.0, "Hz", 5.0, 0.30),
    ("taper length", 0.50, "s", 0.10, 0.45),
    ("window length", 2.00, "s", 0.50, 0.20),
    ("velocity step", 5.0, "m/s", 1.0, 0.35),
    ("damping factor", 0.01, "", 0.005, 0.10),
    ("elevation correction", 1.0, "1 = on", 0.5, 0.60),
)
N_ATTEMPTS = 2000
TOLERANCE = 0.02               # |y - y_published| / y_published allowed
N_PLAUSIBLE_GUESSES = 4        # values a guesser would consider per unstated parameter


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def run_chain(deviations):
    """deviations: array (..., n_params) of normalised deviations in [-1, 1]."""
    deviations = np.atleast_2d(np.asarray(deviations, dtype=float))
    elasticities = np.array([e for *_, e in PARAMETERS])
    return Y0 * np.exp(deviations @ elasticities)


def main():
    names = [p[0] for p in PARAMETERS]
    half_ranges = np.array([p[3] for p in PARAMETERS])
    elasticities = np.array([p[4] for p in PARAMETERS])

    section("1. The surrogate chain and its six parameters")
    print(f"SYNTHETIC chain: y = {Y0:.0f} * exp(sum_i e_i d_i), "
          f"d_i = deviation / plausible half-range")
    print("  parameter               nominal      unit   half-range  elasticity e_i")
    for name, value, unit, half, e in PARAMETERS:
        print(f"  {name:<22s} {value:8.3f}  {unit:<9s} {half:8.3f}   {e:8.2f}")
    print(f"  number of parameters = {len(PARAMETERS)}; "
          f"a full grid of {N_PLAUSIBLE_GUESSES ** len(PARAMETERS)} guesses exists "
          f"if every value is unknown")

    section("2. Elasticities: output change per 10 % parameter change")
    order = np.argsort(-elasticities)
    for i in order:
        d = np.array([0.10 if j == i else 0.0 for j in range(len(PARAMETERS))])
        y = run_chain(d)[0]
        print(f"  {names[i]:<22s} +10 % of the half-range -> y = {y:7.3f} "
              f"({(y - Y0) / Y0 * 100:+6.2f} %)")
    print(f"  most influential parameter: {names[order[0]]} "
          f"(e = {elasticities[order[0]]:.2f})")
    print(f"  least influential parameter: {names[order[-1]]} "
          f"(e = {elasticities[order[-1]]:.2f})")
    print(f"  ratio of influence = "
          f"{elasticities[order[0]] / elasticities[order[-1]]:.1f}x")

    section("3. Reporting completeness: does a reader reproduce the number?")
    print(f"  a reader guesses each unreported parameter uniformly within "
          f"+/-50 % of its plausible half-range")
    print(f"  reproduction succeeds if |y_reproduced - y_published| / y_published "
          f"<= {TOLERANCE * 100:.0f} %")
    print("  reported   sd of log-deviation   90 % interval for y   measured success")
    deviations = RNG.uniform(-0.5, 0.5, size=(N_ATTEMPTS, len(PARAMETERS)))
    for n_reported in range(len(PARAMETERS) + 1):
        free = elasticities[n_reported:]
        sd = float(np.sqrt(np.sum(free ** 2) / 12.0))
        lo, hi = Y0 * np.exp(-1.645 * sd), Y0 * np.exp(1.645 * sd)
        dev = deviations.copy()
        dev[:, :n_reported] = 0.0
        y = run_chain(dev)
        ok = float(np.mean(np.abs(y - Y0) / Y0 <= TOLERANCE))
        print(f"  {n_reported} of 6    {sd:8.4f}              "
              f"[{lo:6.1f}, {hi:6.1f}]        {ok * 100:6.1f} %")
    print("  -> the uncertainty is set by the elasticities of the parameters that are")
    print("     NOT reported, and only complete reporting removes it.")
    print("     Reporting five of six parameters still leaves a factor of about "
          f"{np.exp(1.645 * np.sqrt(elasticities[-1] ** 2 / 12.0)):.2f} of doubt.")
    print(f"  a full grid of {N_PLAUSIBLE_GUESSES ** len(PARAMETERS)} discrete guesses "
          f"would be needed to enumerate the unstated case")

    section("4. Which single parameter is worth reporting first?")
    print("  parameter reported alone     elasticity   sd of log-deviation"
          "   90 % interval for y   success")
    for i in np.argsort(-elasticities):
        free = np.delete(elasticities, i)
        sd = float(np.sqrt(np.sum(free ** 2) / 12.0))
        lo, hi = Y0 * np.exp(-1.645 * sd), Y0 * np.exp(1.645 * sd)
        dev = deviations.copy()
        dev[:, i] = 0.0
        ok = float(np.mean(np.abs(run_chain(dev) - Y0) / Y0 <= TOLERANCE))
        print(f"  {names[i]:<26s} {elasticities[i]:8.2f}   {sd:14.4f}       "
              f"[{lo:6.1f}, {hi:6.1f}]   {ok * 100:6.1f} %")
    print(f"  none reported: sd = "
          f"{np.sqrt(np.sum(elasticities ** 2) / 12.0):.4f}, success "
          f"{np.mean(np.abs(run_chain(deviations) - Y0) / Y0 <= TOLERANCE) * 100:.1f} %")
    print("  -> rank by elasticity, not by familiarity: the parameter you always")
    print("     quote is not always the one that changes y.")


if __name__ == "__main__":
    main()
