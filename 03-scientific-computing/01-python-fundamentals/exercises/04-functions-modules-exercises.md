# Exercises — 03-01-04 Functions, Scope, Modules and Packages

Attempt these **closed-book** before opening the
[solutions](./04-functions-modules-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/velocity_lib.py`](../code/velocity_lib.py) or
[`../code/functions_modules_demo.py`](../code/functions_modules_demo.py) require
you to run them and report their **actual** output.

---

## ★ Foundational

**★1.** An idealised medium has $\lambda = 8.0\times10^{9}$ Pa,
$\mu = 4.0\times10^{9}$ Pa and $\rho = 2200$ kg m⁻³.

(a) Compute $v_p = \sqrt{(\lambda+2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$.
(b) Compute $v_p/v_s$ and Poisson's ratio
$\nu = (v_p^2 - 2v_s^2)/(2(v_p^2 - v_s^2))$.
(c) Verify (a) and (b) with `velocity_lib.vp_from_moduli`,
`velocity_lib.vs_from_moduli` and `velocity_lib.poisson_ratio`.
(d) Look at your value of $\nu$ and state which single number in the input
determines it. Then state the physical meaning of $\nu = 1/3$.

---

**★2.** Run each and report the exact output:

```bash
python3 velocity_lib.py
python3 -m doctest velocity_lib.py
python3 functions_modules_demo.py
```

State what each command tests, and why the first two can be run without executing
the third.

---

**★3.** State the value of `bad2` and whether `bad1 is bad2` for the demo's
mutable-default function, and explain in one sentence why the second call changed
the first result.

---

## ★★ Applied

**★★4.** Write a function

```python
def add_reading(value, readings=None):
    ...          # <- your implementation goes here
```

that appends to a per-call list, returns it, and *proves* on each call that it is
not sharing state:

(a) Implement it with the `None` sentinel.
(b) Add an assertion that the returned list's length equals the number of items
passed in that call.
(c) Demonstrate with three calls of different lengths that the lengths are 1, 2
and 3, and that no two returned lists are the same object.

---

**★★5.** Run `python3 functions_modules_demo.py` and report:

(a) the three scope outputs (the `nonlocal` counter, the leaked global, and
`helper()`);
(b) the four default-argument outputs and the identity test;
(c) the two purity outputs and the cache size.

Then explain why `helper()` is 0.6172 and not 0.3086.

---

**★★6.** Design the signature of a function that computes a terrain correction
for a station, given: the station's elevation, the surrounding elevations (a
variable number), a density, a maximum terrain radius, and an option to return a
diagnostic dict.

(a) Write the `def` line, making every optional parameter keyword-only and giving
each a sensible default.
(b) Justify the placement of the bare `*`.
(c) Write the docstring's Parameters section with units on every parameter.

---

## ★★★ Research-oriented

**★★★7.** Build a module.

Write `gravity_lib.py` containing:

- `free_air_mgal(h_m, gradient=0.3086)` — linear free-air correction;
- `slab_mgal(h_m, rho=2670.0)` — the infinite-slab Bouguer term;
- `simple_bouguer_mgal(observed_mgal, h_m, rho=2670.0)` — free-air minus slab;
- a `_self_test()` asserting at least four physical invariants;
- an `if __name__ == "__main__":` guard.

(a) List each invariant you assert and say why it has no exceptions.
(b) Test with a known case: $h = 100$ m, $\rho = 2670$ kg m⁻³, and show that the
slab term is the value the module's exercise set quotes elsewhere in this module.
(c) Add validation that `rho` is positive and that `h_m` is a number, and show
what each raises.
(d) Import the module from a *second* file and call one function, proving that
importing does not execute the self-test.

---

**★★★8.** A velocity function takes `(v, rho, depth)`. All three are in SI, but
the calling script holds depth in kilometres and density in g cm⁻³.

(a) Explain why no type hint, no docstring and no assertion in the function can
detect the units error.
(b) Propose three changes to the *interface* — not the body — that make the error
detectable or impossible, and say what each costs the caller.
(c) The velocities for water-saturated and dry sandstone differ by about 10 per
cent. Estimate the depth error that a 2× density error would produce in a
depth-from-gravity inversion, using $z \propto \sqrt{1/\rho}$ at fixed mass, and
state whether the error would be obvious or subtle.

---

**★★★9.** A colleague's 900-line script is a sequence of top-level statements with
no functions. Write a 400–500 word refactoring plan that names: the three functions
you would extract first and why; the one piece of state that must become a
parameter rather than a global; the test you would write before touching anything;
and the risk of doing the refactoring without that test.
