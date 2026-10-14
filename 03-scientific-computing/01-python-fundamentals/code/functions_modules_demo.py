"""Functions, scope and modules: turning a formula into a testable instrument.

Run:  python3 functions_modules_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-04.  The demonstration is split between this file and
``velocity_lib.py``, because the last point - a formula becomes an instrument
only when it can be imported and tested on its own - cannot be made inside one
file.

Demonstrates:

1. Calling the library, and reading its docstring with help().
2. Scope: local, enclosing, global, built-in (the LEGB rule) and the
   ``global`` statement used and regretted.
3. Default arguments, keyword arguments and the mutable-default trap.
4. *args / **kwargs and keyword-only parameters.
5. Returning several values, and returning a dict instead.
6. Pure functions and why they are easier to test.
"""

import math

import velocity_lib as vlib

SECTION = "-" * 72


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_call_the_library():
    section("1. A formula is not reusable until it has a name and a test")
    print("  Running the library's own self-test:")
    vlib._self_test()
    print()
    print(f"  {'medium':<22}{'vp (m/s)':>10}{'vs (m/s)':>10}"
          f"{'vp/vs':>8}{'nu':>8}{'rho*vp':>14}")
    for name, p in vlib.VELOCITY_MODEL.items():
        vp = vlib.vp_from_moduli(p["lam"], p["mu"], p["rho"])
        vs = vlib.vs_from_moduli(p["mu"], p["rho"])
        print(f"  {name:<22}{vp:>10.1f}{vs:>10.1f}"
              f"{vlib.vp_vs_ratio(vp, vs):>8.3f}"
              f"{vlib.poisson_ratio(vp, vs):>8.4f}"
              f"{vlib.impedance(p['rho'], vp):>14.4e}")
    print()
    print("  The first line of vp_from_moduli.__doc__:")
    print(f"    {vlib.vp_from_moduli.__doc__.splitlines()[0]}")
    print("  Docstrings are not decoration: help() reads them, IDEs read them,")
    print("  and the doctest module can execute the examples in them.")


def part2_scope():
    section("2. Scope: LEGB, and one global that we should not have written")
    counter = 0

    def bump():
        nonlocal counter
        counter += 1

    bump()
    bump()
    print(f"  after two nonlocal bumps, counter = {counter}")

    def leak():
        global ACCIDENTAL
        ACCIDENTAL = 42

    leak()
    print(f"  after leak(), the module global ACCIDENTAL = {ACCIDENTAL}")
    print("  A function that writes a module global is a function you cannot")
    print("  test in isolation and cannot call twice with the same result.  The")
    print("  only defensible use is a genuinely global piece of state such as a")
    print("  cache, and even then it belongs behind a name like _cache with a")
    print("  comment explaining the lifetime.")

    hidden = 1.0

    def helper(rate_mgal_per_m=0.3086):
        # 'hidden' is resolved at call time, from the enclosing module scope.
        return hidden * rate_mgal_per_m

    hidden = 2.0
    print(f"  helper() = {helper():.4f}: the global was read at call time")
    print("  Python resolves free names when the function runs, not when it is")
    print("  defined.  That is late binding, and it is why a function's result")
    print("  depends on module state you did not pass to it.")


def part3_defaults():
    section("3. Default arguments: useful, and one famous trap")
    print(f"  vlib.vp_from_moduli(9.0e9, 8.0e9, 2350.0) ="
          f" {vlib.vp_from_moduli(9.0e9, 8.0e9, 2350.0):.4f} m/s")
    print("  Keyword form, clearer at the call site:")
    print(f"  vlib.vp_from_moduli(rho=2350.0, mu=8.0e9, lam=9.0e9) ="
          f" {vlib.vp_from_moduli(rho=2350.0, mu=8.0e9, lam=9.0e9):.4f} m/s")
    print()

    def append_station_bad(code, catalogue=[]):
        """The trap: the default list is created once, at def time."""
        catalogue.append(code)
        return catalogue

    def append_station_good(code, catalogue=None):
        """The fix: None sentinel, new list per call."""
        if catalogue is None:
            catalogue = []
        catalogue.append(code)
        return catalogue

    bad1 = append_station_bad("STA01")
    print(f"  bad:  first call  -> {bad1}")
    bad2 = append_station_bad("STA02")
    print(f"  bad:  second call -> {bad2}   <- second call edited the first result")
    print(f"        bad1 is now {bad1}")
    print(f"        bad1 is bad2 -> {bad1 is bad2}")
    good1 = append_station_good("STA01")
    print(f"  good: first call  -> {good1}")
    good2 = append_station_good("STA02")
    print(f"  good: second call -> {good2}")
    print(f"        good1 is good2 -> {good1 is good2}")
    print("  Defaults are evaluated once, when the def statement executes.  A")
    print("  mutable default therefore persists across calls, which turns a")
    print("  per-station catalogue into a survey-wide one.")


def part4_variadic():
    section("4. *args, **kwargs and keyword-only parameters")
    def survey_mean(*readings, weight=None, verbose=False):
        if not readings:
            raise ValueError("survey_mean needs at least one reading")
        value = sum(readings) / len(readings)
        if weight is not None:
            value *= weight
        if verbose:
            print(f"    survey_mean received {len(readings)} readings")
        return value

    print(f"  survey_mean(1.0, 2.0, 3.0)                ="
          f" {survey_mean(1.0, 2.0, 3.0):.4f}")
    print(f"  survey_mean(1.0, 2.0, 3.0, weight=2.0)    ="
          f" {survey_mean(1.0, 2.0, 3.0, weight=2.0):.4f}")
    print("  survey_mean(1.0, 2.0, 3.0, verbose=True):")
    survey_mean(1.0, 2.0, 3.0, verbose=True)
    readings = [4.0, 5.0]
    print(f"  survey_mean(*readings)                    ="
          f" {survey_mean(*readings):.4f}")
    print()
    print("  The bare '*' makes weight and verbose keyword-only: they cannot be")
    print("  passed positionally, so a caller can never silently swap them.")


def part5_returns():
    section("5. Returning several values - and when not to")
    def trace_summary(samples):
        """Return (npts, mean, peak) as a tuple."""
        n = len(samples)
        if n == 0:
            raise ValueError("empty trace")
        return n, sum(samples) / n, max(abs(s) for s in samples)

    samples = [0.4, -1.2, 0.8, 2.0, -0.3]
    npts, mean, peak = trace_summary(samples)
    print(f"  tuple unpacking: npts={npts} mean={mean:.4f} peak={peak:.4f}")

    def trace_summary_dict(samples):
        return {"npts": len(samples),
                "mean": sum(samples) / len(samples),
                "peak": max(abs(s) for s in samples)}

    summary = trace_summary_dict(samples)
    print(f"  dict return    : {summary}")
    print()
    print("  A tuple is unambiguous and unpacks positionally; a dict documents")
    print("  its own fields and survives added fields.  Up to three values, use")
    print("  a tuple.  Beyond that, or if the fields will be stored, build a")
    print("  named structure (lesson 08).")


def part6_purity():
    section("6. Pure functions: the same input, the same output, always")
    def impedance_pure(rho, vp):
        return rho * vp

    cache = {}

    def impedance_cached_impure(rho, vp):
        key = (rho, vp)
        cache[key] = cache.get(key, rho * vp)  # writes outside the function
        return cache[key]

    a = impedance_pure(2500.0, 3000.0)
    b = impedance_pure(2500.0, 3000.0)
    print(f"  pure:   {a:,.1f} then {b:,.1f}")
    print(f"  impure: {impedance_cached_impure(2500.0, 3000.0):,.1f} and the")
    print(f"          module now carries {len(cache)} entry outside the function")
    print()
    print("  Both return correct numbers.  Only the pure one can be tested by")
    print("  comparing its output with a hand-computed value, and that is the")
    print("  property that makes a scientific codebase auditable.")


if __name__ == "__main__":
    part1_call_the_library()
    part2_scope()
    part3_defaults()
    part4_variadic()
    part5_returns()
    part6_purity()
    print(f"\n{SECTION}\nmodule functions_modules_demo executed as __main__")
