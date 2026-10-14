---
id: 03-01-04
title: "Functions, Scope, Modules and Packages"
level: beginner
prereqs: ["03-01-03"]
estimated_minutes: 75
tags: [functions, scope, modules, testing, rock-physics]
---

# Functions, Scope, Modules and Packages

A formula written inline in a script is a *statement*. A formula written as a
named function with a docstring, a unit and a test is an *instrument*. The
difference is not stylistic, and it is not about tidiness: it is that only the
second one can be calibrated.

This lesson takes the velocity relations of isotropic elasticity — the formulas
behind every seismic interpretation — and turns them into a module you can
import, test and reuse. Along the way it settles the questions that decide
whether Python code is maintainable: what a scope is, why a default argument is
evaluated once, what `*args` and `**kwargs` actually do, and how Python finds a
module on disk.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a function with a docstring, type hints, an explicit return value
   and input validation, and say what makes it testable.
2. **Explain** the LEGB rule for name resolution, and demonstrate late binding of
   globals with a measured example.
3. **Use** positional, keyword, default, keyword-only and variadic parameters
   correctly, and identify the mutable-default trap and its fix.
4. **Return** multiple values as a tuple or a dict, and choose between them on
   the grounds of how the result will be used.
5. **Organise** code into a module with an `if __name__ == "__main__"` self-test,
   and explain how `import` finds that module.
6. **Justify** why the same physical formula is worth writing once: units,
   verification, reuse, and the elimination of copy-paste divergence.

## Prerequisites

- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](./03-control-flow.md)
  — the loop bodies that become function bodies here.

## 1. What a function is for

Four reasons, in order of importance for science.

**Verification.** A function can be called with a known input and its output
compared with a hand calculation. Code inside a loop cannot. The module you will
read below carries a `_self_test()` that asserts physical invariants: $v_p > v_s$
for a solid, Poisson's ratio in $(-1, 0.5)$, zero shear velocity for a fluid.
Those assertions are cheap and they are the calibration of the instrument.

**Reuse without divergence.** The relation
$v_p = \sqrt{(\lambda + 2\mu)/\rho}$ appears in the lab, in a processing script,
in a plotting script and in a report. Written four times, it will acquire four
slightly different behaviours — one of them using $\rho$ in g cm⁻³. Written once
and imported, there is one behaviour to fix.

**Units and naming.** A function signature is a contract with units:
`vp_from_moduli(lam, mu, rho)` takes Pa, Pa and kg m⁻³, because the docstring says
so and the units cancel to m s⁻¹. A bare expression `sqrt((l + 2*m) / r)` conveys
none of that.

**A place to put the assumption.** "An isotropic solid" is an assumption. It
belongs next to the formula, not in a comment three files away.

## 2. Worked walkthrough: packaging a formula

The worked example is [`code/velocity_lib.py`](./code/velocity_lib.py). Its
central function is short:

```python
def vp_from_moduli(lam: float, mu: float, rho: float) -> float:
    """P-wave speed in m/s: ``sqrt((lambda + 2*mu) / rho)``.

    # (the Parameters section is omitted here; the full docstring is in
    #  code/velocity_lib.py)
    Raises
    ------
    ValueError
        If ``rho`` is not positive, or if ``mu`` is not positive.
    """
    if rho <= 0.0:
        raise ValueError(f"density must be positive, got {rho!r}")
    if mu <= 0.0:
        raise ValueError(f"shear modulus must be positive, got {mu!r}")
    return math.sqrt((lam + 2.0 * mu) / rho)
```

Five things are worth naming explicitly, because each is a habit.

- **Type hints.** `lam: float` and `-> float` are documentation that tools can
  check. They are not enforced at runtime, which is why they do not replace
  validation.
- **A docstring with sections.** Parameters, units, what it raises, and a
  runnable example. The example is executable: `python3 -m doctest velocity_lib.py`
  runs it and reports "doctest OK".
- **Validation with a message that carries the value.** `got 0.0` tells you what
  arrived; `invalid density` does not. The `!r` shows the *repr*, so a string
  `'2670'` is visibly a string.
- **A guard, not an assertion.** The caller can pass a bad density from a file,
  so this is input validation and must survive `python3 -O`, which strips
  assertions.
- **The formula itself is one line**, and the rest of the function is about the
  contract. That ratio is typical of production scientific code.

Calling the library across three nominal media gives:

```text
  medium                  vp (m/s)  vs (m/s)   vp/vs      nu        rho*vp
  sandstone (nominal)       3261.6    1845.1   1.768  0.2647    7.6649e+06
  limestone (nominal)       4883.3    2842.0   1.718  0.2439    1.2696e+07
  steel (nominal)           5908.0    3232.0   1.828  0.2865    4.6378e+07
```

Read the columns as the instrument's output, not as rock properties. The
$v_p/v_s$ ratio and Poisson's ratio are *discriminants*: 1.77 for a quartz-rich
rock, 1.72 for a carbonate, 1.83 for steel — the numbers are plausible
order-of-magnitude values for idealised media, and the code labels them
"nominal" for exactly that reason. The last column is acoustic impedance
$\rho v_p$ in kg m⁻² s⁻¹, which is the quantity a reflection survey actually
measures a contrast in.

The self-test is the part that makes this a module rather than a file:

```text
velocity_lib: all self-tests passed
```

Run it directly with `python3 velocity_lib.py`; the `if __name__ == "__main__"`
guard is what makes that possible without side effects on import.

## 3. Worked walkthrough: scope, and late binding

Python resolves a free name by searching four scopes, in order: **L**ocal,
**E**nclosing, **G**lobal (module), **B**uilt-in. The demo makes two of these
concrete.

```text
  after two nonlocal bumps, counter = 2
  after leak(), the module global ACCIDENTAL = 42
  helper() = 0.6172: the global was read at call time
```

- **`nonlocal`** rebinds a name in the nearest enclosing function scope. It is how
  a nested helper can update a counter owned by its parent — with the caveat that
  the counter is now hidden state.
- **`global`** rebinds a name at module level. The demo uses it to do something it
  then argues against: a function that writes a module global cannot be tested in
  isolation and cannot be called twice with the same result. The legitimate uses
  are a cache and a module-level constant defined once; both should be named so
  that their lifetime is obvious (`_CACHE`, with a comment).
- **Late binding.** The last line is the subtle one. The module sets
  `hidden = 1.0`, defines `helper()` which reads `hidden`, then sets
  `hidden = 2.0`, and *then* calls `helper()`. The result is 0.6172, which is
  $2.0 \times 0.3086$, not $1.0 \times 0.3086$. Python resolved the free name when
  the function *ran*, not when it was defined.

Late binding is why a function whose result depends on module state you did not
pass to it is hard to reason about. It is also why closures over loop variables
surprise people: a list of lambdas created in a loop all capture the *same*
variable, so they all see its final value. The fix is a default argument
(`lambda x=x: ...`), which binds at definition time — the same mechanism that
makes default arguments interesting, and the reason for the next section.

## 4. Worked walkthrough: the mutable-default trap

```text
  bad:  first call  -> ['STA01']
  bad:  second call -> ['STA01', 'STA02']   <- second call edited the first result
        bad1 is now ['STA01', 'STA02']
        bad1 is bad2 -> True
  good: first call  -> ['STA01']
  good: second call -> ['STA02']
        good1 is good2 -> False
```

The buggy function is `def append_station_bad(code, catalogue=[]):`. The default
`[]` is evaluated **once**, when the `def` statement executes, and the same list
object is then used for every call that omits the argument. The second call does
not start from an empty list; it starts from the list the first call returned —
literally the same object, as `bad1 is bad2 → True` shows.

The fix is the `None` sentinel:

```python
def append_station_good(code, catalogue=None):
    if catalogue is None:
        catalogue = []
    catalogue.append(code)
    return catalogue
```

`None` is immutable, so sharing it between calls is harmless.

This is the single most common surviving bug in Python scientific code, because
its symptom is not a crash but a growing list. A per-station catalogue becomes a
survey-wide one, and the failure appears far from its cause. Two related traps:

- **A mutable *attribute* as a class default** has the same problem; set it in
  `__init__` instead (lesson [08](./08-classes-and-oop.md)).
- **A default computed from the environment** — a path, a version string, a
  timestamp — is also evaluated once, so it silently freezes. Compute it in the
  body.

## 5. Variadic parameters and keyword-only arguments

```text
  survey_mean(1.0, 2.0, 3.0)                = 2.0000
  survey_mean(1.0, 2.0, 3.0, weight=2.0)    = 4.0000
  survey_mean(1.0, 2.0, 3.0, verbose=True):
    survey_mean received 3 readings
  survey_mean(*readings)                    = 4.5000
```

`*readings` collects any number of positional arguments into a tuple;
`**kwargs` would collect keyword arguments into a dict. The important part of
this example is the bare `*`:

```python
def survey_mean(*readings, weight=None, verbose=False):
```

Everything after the `*` is **keyword-only**: it cannot be passed positionally.
That is a real safety property. A function mixing a variable-length positional
list with optional settings is a function where `survey_mean(1.0, 2.0, True)`
would otherwise be silently interpreted as three readings rather than two
readings and a flag. Keyword-only parameters make that call a `TypeError`.

Use `*args` when the *number of physical inputs* genuinely varies (a list of
readings from an instrument); do not use it to avoid naming parameters. A
signature is the function's specification, and `*args, **kwargs` is an
unspecified one — the reason decorators need it (lesson
[10](./10-context-managers-decorators.md)) and ordinary functions usually do not.

## 6. Returning several values

```text
  tuple unpacking: npts=5 mean=0.3400 peak=2.0000
  dict return    : {'npts': 5, 'mean': 0.34, 'peak': 2.0}
```

A function can return a tuple, which unpacks positionally, or a dict, which
documents its own fields. The guidance is short:

- **Up to three values, related and fixed: return a tuple.** `npts, mean, peak`
  is unambiguous and cheap.
- **More than three, or unstable: return a dict or a named record.** A dict
  survives adding a field without changing every call site, and reads better in a
  log line.
- **If the values will be stored or passed around: define a record** (a
  `namedtuple` or a dataclass, lesson [08](./08-classes-and-oop.md)). Positional
  unpacking of a six-element tuple is a bug waiting for a field reorder.

Note the small print: none of these copies the data. Returning a list returns a
reference to the same list, so a caller that mutates it mutates the function's
data — the aliasing rule from lesson [02](./02-types-and-variables.md) §7.

## 7. Physical interpretation: why a formula must be a function

The rock-physics example is chosen because the physics is unambiguous and the
software lesson follows from it.

**Units are part of the type.** The velocity formulas take SI. The single most
common error in a velocity calculation is a density in g cm⁻³ (2670 becomes
2.67), which changes $v$ by a factor of $\sqrt{1000} = 31.6$ — a P-wave speed of
100 km s⁻¹, which is not a rock, it is a bug. A function that documents its units
and validates its inputs converts that into an exception at the source.

**Physical invariants are assertions.** For an isotropic elastic solid,
$v_p > v_s > 0$ identically, and $-1 < \nu \le 0.5$. If a computed $v_p$ is less
than $v_s$, either the moduli are inconsistent or the formula is wrong; there is
no third possibility, and no physical situation in which the answer is simply
"smaller". An invariant that has no exceptions is an assertion, and putting it in
a self-test is free.

**The formula is the shared object, not the numbers.** $v_p = \sqrt{(\lambda+2\mu)/\rho}$
and $v_s = \sqrt{\mu/\rho}$ are the same two lines in seismology, rock physics,
engineering seismology and exploration. They are also the point at which the
elastic moduli of module
[02-04 Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
become the velocities ObsPy reads from a station file in module
[03-10](../10-obspy-and-seismic-data/README.md). One implementation, imported
everywhere, is the only version that stays consistent.

**A function is the unit of testing, and testing is the unit of trust.** The
module's self-test is six assertions long. That is enough to catch a unit error, a
sign error and a swapped parameter, which are the three error classes that
survive visual inspection.

## 8. Modules and packages

A **module** is a `.py` file. A **package** is a directory of modules with an
`__init__.py`. When you write `import velocity_lib`, Python searches
`sys.path` in order: the script's own directory first, then installation
directories. That is why running `python3 functions_modules_demo.py` from inside
`code/` finds `velocity_lib.py` next to it, and why running it from elsewhere
with a copy of the file elsewhere may find a *different* module with the same
name. Module name collisions are a real failure mode; prefix your modules
(`geophys_core`, not `core`).

Four conventions that make a module importable without side effects:

- **`if __name__ == "__main__":`** guard for anything that runs on import
  (printing, file writing, computation). Without it, importing the module
  executes the demo.
- **Prefer imports at the top**, so dependencies are visible, and prefer absolute
  imports (`import velocity_lib`) unless the project is a package.
- **`__all__`** states the public surface. The module in this lesson lists six
  functions; everything else (including `math`) is private by convention.
- **A self-test that is a function**, so it can be called by a test runner in
  module [03-13](../13-testing-profiling-packaging/README.md) rather than only by
  hand.

Relative imports come next, in module 13's packaging material — and they only
work inside a package.

## 9. Assumptions and limits

1. **The velocity relations assume isotropy and homogeneity.** A real rock is
   anisotropic; a shale can differ by 20 per cent in $v_p$ between the bedding
   direction and the bedding normal. The formulas here are the isotropic
   reference case against which anisotropy is measured, not a substitute for it.
2. **They assume a linear elastic solid.** A fluid has $\mu = 0$ and
   `vs_from_moduli` returns 0.0 rather than raising, because a fluid really does
   transmit no shear wave. That is a physically correct answer that will break
   arithmetic downstream — a division by zero in a $v_p/v_s$ ratio, for instance —
   so the caller must handle it.
3. **`velocity_lib`'s "nominal" media are teaching values.** The Lamé parameters
   chosen bracket the range from a saturated sandstone to steel. They are not
   measurements of a named rock.
4. **Type hints are not validation.** `vp_from_moduli(9e9, 8e9, "2350")` raises a
   `TypeError` from the comparison, not a helpful message, because the annotation
   is not enforced. Validate what matters.
5. **Scope is dynamic in time, not lazy in lookup.** Late binding means a
   function's behaviour depends on the module state *at call time*. Tests that
   mutate module globals are therefore order-dependent.
6. **Mutable defaults, mutable attributes, and shared imported state** are the
   three ways a function acquires hidden state. All three are avoidable.

## 10. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 velocity_lib.py              # the module's own self-test
python3 -m doctest velocity_lib.py   # the docstring examples
python3 functions_modules_demo.py    # the six sections of this lesson
```

The third command prints the tables quoted above. Note the final line:
`module functions_modules_demo executed as __main__`. The demo prints that under
its `if __name__ == "__main__"` guard, which is how you can tell an executed
script from an imported module — a distinction that matters the first time an
import triggers a demo that writes a file.

## 11. Common mistakes

1. **The mutable default argument.** §4. It ships.
2. **A function that is too long to name.** If the docstring needs "and", split it.
3. **Returning `None` implicitly on one path.** A function that sometimes returns
   a value and sometimes falls off the end is a `None` that will be divided.
4. **Writing to a module global.** Late binding makes the result depend on call
   order; the demo shows both the mechanism and the objection.
5. **Forgetting the bare `*`.** Without it, every optional setting can be passed
   positionally, and a caller who adds an argument in the wrong order gets a
   silent misinterpretation rather than a `TypeError`.
6. **Shadowing a built-in.** A parameter named `max`, `sum` or `len` removes the
   built-in inside the function.
7. **Ignoring a return value.** Every function that returns something and is
   called for effect should either be a procedure returning `None` or have its
   result used; a hybrid is a bug.
8. **Copy-pasting a formula instead of importing it.** The fourth copy is where
   the discrepancy appears.
9. **Importing for side effects.** A module that prints on import cannot be
   tested quietly; use the `__main__` guard.
10. **Naming a module after a common library.** A local `csv.py` or `random.py`
    shadows the standard library for the whole project.

## 12. Real-world applications

- **Rock-physics libraries.** Every velocity, density and impedance relation is
  a small function like the ones here; a mature rock-physics toolkit is a package
  of a few hundred such functions with a test suite.
- **Processing pipelines.** A seismic processing sequence is a chain of functions
  from samples to samples, each with a specification and a test; the module
  boundary is what makes them independently testable.
- **Analysis notebooks.** The moment a notebook cell is worth reusing in a second
  notebook, it is worth being a function in a module. That is module
  [03-06](../06-jupyter-and-notebooks/README.md)'s subject.
- **Cross-language work.** A validated function with a documented signature and a
  test is portable: the same contract can be implemented in Fortran or C for
  speed (module [19](../12-numerical-simulation-python/README.md) and beyond) and
  checked against the Python reference.

## 13. Further reading

- NumPy — [numpy.org](https://numpy.org): the same functions, rewritten to take
  arrays, and with the signature conventions that make vectorised APIs usable.
- SciPy — [scipy.org](https://scipy.org): a well-documented look at how a large
  scientific library documents parameters, units and return values.
- ObsPy — [docs.obspy.org](https://docs.obspy.org): a real, large scientific
  package whose function-level documentation is a model for this lesson's
  docstrings.

## 14. Related lessons

- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](./03-control-flow.md)
  — the loop body as a function.
- [03-01-07 Exceptions, Assertions and Systematic Debugging](./07-errors-and-debugging.md)
  — what to validate and how to report it.
- [03-01-08 Classes, Objects and When Not to Use OOP](./08-classes-and-oop.md)
  — when a function is not the right unit any more.
- [03-01-10 Context Managers, Decorators and Functional Idioms](./10-context-managers-decorators.md)
  — functions that take functions.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — where the velocity relations come from.

## 15. Exercises

[`exercises/04-functions-modules-exercises.md`](./exercises/04-functions-modules-exercises.md) —
eight problems, ★ to ★★★. Problem ★★5 requires the mutable-default outputs;
problem ★★★8 asks you to design an interface for a function whose units cannot be
inferred from its arguments, and defend it.

## 16. Self-assessment checklist

- [ ] I can write a function with a docstring, type hints, validation and a
      doctest that runs.
- [ ] I can explain the LEGB rule and demonstrate late binding.
- [ ] I can explain why `def f(x, acc=[])` is a bug and how to fix it.
- [ ] I can say when to use a bare `*` to make parameters keyword-only.
- [ ] I can choose between a tuple, a dict and a record for a multi-value return.
- [ ] I can list the four conventions that make a module importable without side
      effects.
- [ ] I can state three physical invariants of an isotropic elastic solid and
      write them as assertions.
