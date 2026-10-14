"""Exceptions, assertions and systematic debugging.

Run:  python3 errors_debugging_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-07.  The lesson's claim is that an assertion in
scientific code is a *physical* statement - "this density cannot exceed iron" -
and that a good error message is worth more than a debugging session.

Demonstrates:

1. Assertions as physical sanity checks on an input catalogue.
2. A custom exception carrying the offending value and its unit.
3. try / except / else / finally, and catching only what you mean.
4. Silent failure: a ValueError swallowed, and the wrong answer it produced.
5. Atomic exceptions: a wide try-and-ignore that hides a real bug.
6. traceback, and what a real traceback tells you.
7. The five-question checklist applied to a genuine off-by-one bug.
"""

import math
import traceback

# Nominal densities for the sanity checks (kg m^-3).  Iron is the practical
# ceiling for a crustal rock; osmium is the densest element, kept as a hard
# physical ceiling.
DENSITY_IRON = 7874.0
DENSITY_OSMIUM = 22590.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


class DataError(ValueError):
    """Raised when a measurement is physically impossible or malformed.

    Carrying the offending value and its unit in the message is the whole
    point: the exception is documentation that fires exactly when needed.
    """

    def __init__(self, field, value, unit, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"{field} = {value!r} {unit}: {reason}")


def check_density(rho, rho_unit="kg m^-3"):
    """Validate a rock density, with the physical reasons stated."""
    if not isinstance(rho, (int, float)) or isinstance(rho, bool):
        raise DataError("density", rho, rho_unit, "not a number")
    if math.isnan(rho):
        raise DataError("density", rho, rho_unit, "NaN: the measurement failed")
    if rho <= 0.0:
        raise DataError("density", rho, rho_unit, "must be positive")
    if rho > DENSITY_OSMIUM:
        raise DataError("density", rho, rho_unit,
                        f"exceeds osmium ({DENSITY_OSMIUM:.0f} kg m^-3)")
    if rho > DENSITY_IRON:
        # A warning-level anomaly, not an error: heavy ore bodies exist.
        return rho, f"warning: denser than iron ({DENSITY_IRON:.0f} kg m^-3)"
    return rho, "ok"


def part1_assertions():
    section("1. Assertions are physics, written down")
    # Every assertion below states a fact about the model, not about Python.
    lam, mu, rho = 9.0e9, 8.0e9, 2350.0
    vp = math.sqrt((lam + 2.0 * mu) / rho)
    vs = math.sqrt(mu / rho)
    assert rho > 0.0, "density must be positive"
    assert 0.0 < vs < vp, f"an isotropic solid requires 0 < vs < vp, got {vs:.1f}, {vp:.1f}"
    assert -1.0 < (vp ** 2 - 2 * vs ** 2) / (2 * (vp ** 2 - vs ** 2)) < 0.5, "Poisson ratio out of range"
    print(f"  vp = {vp:.1f} m/s, vs = {vs:.1f} m/s, both assertions held")
    print()
    print("  Two rules make assertions trustworthy:")
    print("    * assert only what you can state physically;")
    print("    * assert at the boundary where the assumption is made.")
    print("  A failed assertion should be impossible, not merely unlikely: if a")
    print("  user can trigger it with a bad file, it is a validation check and")
    print("  belongs in an if/raise, not an assert.")


def part2_validation():
    section("2. A custom exception that carries the number")
    for value in (2670.0, 8100.0, 30000.0, 0.0, float("nan"), "2670"):
        try:
            rho, note = check_density(value)
            print(f"  density {value!r:<10} -> accepted, {note}")
        except DataError as exc:
            print(f"  density {value!r:<10} -> REJECTED: {exc}")
    print()
    print("  The message contains the field name, the value and the reason,")
    print("  so a log line is enough to diagnose the problem without a")
    print("  debugger.  Compare: 'ValueError: invalid density'.")


def part3_try_forms():
    section("3. try / except / else / finally")
    def reciprocal_velocity(v):
        try:
            slowness = 1.0 / v
        except ZeroDivisionError:
            print("    except: velocity was zero")
            return None
        else:
            print(f"    else: slowness = {slowness:.6e} s/m")
            return slowness
        finally:
            print("    finally: this runs either way"

                  " (closing files, releasing locks)")

    for v in (3000.0, 0.0):
        print(f"  reciprocal_velocity({v})")
        reciprocal_velocity(v)


def part4_silent_failure():
    section("4. The cost of swallowing an exception")
    raw = ["12.4", "oops", "9.1"]

    total_bad = 0.0
    for text in raw:
        try:
            total_bad += float(text)
        except ValueError:
            pass                       # silently skipped
    print(f"  with 'except ValueError: pass' -> total = {total_bad}")

    total_good = 0.0
    skipped = 0
    for text in raw:
        try:
            total_good += float(text)
        except ValueError:
            skipped += 1
    print(f"  with a counted skip            -> total = {total_good},"
          f" skipped = {skipped}")
    print()
    print("  Both produced a number.  Only the second told you that one third")
    print("  of the data never entered the sum.  In a 10^6-row file, one silent")
    print("  skip per row is a result that is wrong by a factor, not a digit.")


def part5_too_wide():
    section("5. A try that is too wide hides a real bug")
    def anomaly(offset, depth):
        return 1.0 / (offset * offset + depth * depth) ** 1.5

    print("  A function with a genuine unit bug: depth passed in km, not m.")
    try:
        # 'depth_km' is 0.5 km; the caller believed it was 500 m.
        value = anomaly(0.0, 0.5)
        print(f"  anomaly(0, 0.5) = {value:.6e} - a legal float, a wrong physics")
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        print(f"  caught: {exc}")
    print()
    print("  No exception is raised, because nothing illegal happened.  The")
    print("  defence is not a broad except; it is a unit-carrying name, a")
    print("  docstring, and a test with a known answer (lesson 07's exercise 6).")


def part6_traceback():
    section("6. What a traceback actually tells you")

    def outer(n):
        return middle(n)

    def middle(n):
        return inner(n)

    def inner(n):
        return [0.0] * n[0]         # n is a float, not a sequence

    try:
        outer(5.0)
    except TypeError as exc:
        # traceback.extract_tb() gives the frames as objects, so a log line can
        # carry the call path without an operating-system-specific file path.
        frames = traceback.extract_tb(exc.__traceback__)
        print(f"  the call path, outermost first ({len(frames)} frames):")
        for frame in frames:
            print(f"    {frame.name}()  line {frame.lineno}:  {frame.line}")
        print(f"  the exception: {type(exc).__name__}: {exc}")
    print()
    print("  Read a traceback bottom-up: the last frame is where it broke, and")
    print("  the frames above it are the path that got there.  The path is the")
    print("  part people skip, and it is the part that identifies the caller.")
    print("  'float object is not subscriptable' says the object is a number.")
    print("  The frame above says the caller passed a depth as a scalar where a")
    print("  sequence was expected - that is the information that fixes it.")


def part7_checklist():
    section("7. A real bug, found by systematic questioning")
    data = [10.0, 20.0, 30.0, 40.0]
    print("  Task: mean of the first half of a 4-value list.")
    print(f"  data = {data}")
    naive = sum(data[:len(data) // 2]) / len(data[:len(data) // 2])
    print(f"  naive (first half)   = {naive}")
    wrong = sum(data[:len(data) // 2 + 1]) / (len(data) // 2)
    print(f"  buggy   (n//2+1)/(n//2) = {wrong}  <- wrong, and plausible-looking")
    print()
    print("  The five questions that catch it:")
    print("    1. What is the input type and shape? (list of 4 floats)")
    print("    2. What is the expected output? (mean of 2 values = 15.0)")
    print("    3. What did I get? (30.0)")
    print("    4. Where do the two first diverge? (the slice, not the sum)")
    print("    5. What is the smallest test that shows it? (n = 4)")
    print("  Debugging is bisection on the *first divergence*, not staring.")


if __name__ == "__main__":
    part1_assertions()
    part2_validation()
    part3_try_forms()
    part4_silent_failure()
    part5_too_wide()
    part6_traceback()
    part7_checklist()
