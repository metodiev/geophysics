# Exercises — 03-03-02 scipy.integrate: Quadrature and ODE Integration

Attempt these **closed-book** before opening the
[solutions](./02-integrate-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/integrate_demo.py`](../code/integrate_demo.py) require you to run it
and report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/integrate_demo.py
```

Assume $G = 6.6743\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ and
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ throughout.

---

## ★ Foundational

**★1.** The demo reports the quadrature of $4/(1+x^2)$ on $[0,1]$:

```
    trapezoid on n=11                 3.139925988907159       1.67e-03
    trapezoid on n=101                3.141575986923129       1.67e-05
    simpson   on n=11                 3.141592613939215       3.97e-08
    simpson   on n=101                3.141592653589754       3.95e-14
```

(a) State the convergence order in $n$ of each rule, from the numbers.
(b) Predict the trapezoid error at $n = 201$ and at $n = 401$, then verify
numerically.
(c) Predict the Simpson error at $n = 21$ and verify.
(d) Explain why the Simpson errors at $n = 101$ are three orders of magnitude
below what the $n^{-4}$ rule predicts from $n = 11$, i.e. why the asymptotic
regime has already been reached.

---

**★2.** The demo reports, for a wide thin polygon with density contrast
$\rho = 300\ \mathrm{kg\,m^{-3}}$ and thickness $t = 1$ km:

```
     half-width W (km)     gz (mGal)  exact (mGal)    relative
                   200     12.440613     12.580759    1.11e-02
                  2000     12.566743     12.580759    1.11e-03
                 20000     12.579358     12.580759    1.11e-04
```

(a) Verify the exact value from $g_z = 2\pi G\rho t$.
(b) Compute the same quantity for $\rho = 400\ \mathrm{kg\,m^{-3}}$ and
$t = 500$ m, in mGal.
(c) Predict the relative error at a half-width of 400 km, given the scaling in
the table, and explain the scaling.
(d) State in one sentence why the error is a property of the truncated model
rather than of the quadrature.

---

**★3.** The demo reports for the decay problem ($t_{1/2} = 10^9$ yr, chosen as
an input):

```
    steps taken 95, function evaluations 566, max relative error 5.81e-11
```

(a) The requested tolerance was `rtol=1e-10`. Explain why the achieved maximum
relative error of $5.8\times10^{-11}$ is consistent with that request.
(b) Compute $\lambda$ in s⁻¹ from the half-life.
(c) Verify the value $N/N_0 = 0.707106781187$ at $t = t_{1/2}$.
(d) Explain why the error does not grow with $t$ even though the solution
decays from 1 to 0.0625.

---

## ★★ Applied

**★4.** In the inscribed-polygon study the demo separates two errors:

```
           n   R_eff (m)  quadrature err  geometry err
          16      2961.5        1.84e-06      2.55e-02
          64      2997.6        3.33e-16      1.61e-03
         256      2999.8        8.88e-16      1.00e-04
        1024      3000.0        4.00e-15      6.27e-06
```

(a) Compute the exponent $p$ in geometry error $\propto n^{-p}$ from the
$n = 16$ and $n = 1024$ rows.
(b) Predict the geometry error at $n = 4096$ and verify by running a modified
script.
(c) The area deficit of an inscribed $n$-gon is
$1 - \tfrac{n}{2}\sin(2\pi/n)/\pi$. Expand it for large $n$ and show that the
leading term is $2\pi^2/(3n^2)$.
(d) Explain why the *field* error scales as $n^{-2}$ when the *area* deficit
does, and why the two constants are close but not equal.

---

**★5.** The demo reports the stiffness comparison:

```
    method     steps    nfev   njac     max |err|
    RK45        2197   13190      0      4.30e-09
    BDF           81     166      2      7.85e-09
    Radau         41     306      2      7.69e-09
```

(a) State which method you would use for a stiff problem and which for a smooth
non-stiff one, with a reason in one sentence each.
(b) Compute the ratio of `nfev` between `RK45` and `BDF`.
(c) `Radau` takes the fewest steps but more evaluations than `BDF`. Explain.
(d) Predict what happens to the `RK45` `nfev` if the stiffness coefficient 1000
is raised to 10 000 with the interval held fixed, and explain why the *error*
stays the same.

---

**★6.** The demo reports the spike integrand:

```
      without points=  0.000000   reported abserr 0.00e+00   |error| 1.00e+00
      with    points=  1.000000   reported abserr 1.11e-14   |error| 1.10e-13
```

(a) Explain in two sentences why the adaptive rule returns zero with a
reported error of zero.
(b) Design the `points=` argument for an integrand that is continuous but has a
kink at $x = 0.37$, on $[0,1]$.
(c) Design it for an integrand that is discontinuous at $x = 0.25$ and $0.75$,
with different constants either side.
(d) A colleague reports that `quad` "gave a wrong answer" for a gravity kernel
across a body boundary, and that increasing `epsabs` did not help. Explain
what is wrong with that diagnosis and what to do instead.

---

**★7.** A 3-D uniform sphere of radius $R = 5$ km, centre at 10 km depth and
density $2700\ \mathrm{kg\,m^{-3}}$, is integrated over its volume:

```
    volume quadrature  gz = 94.355693 mGal
    point mass G*M/d^2    = 94.355693 mGal
```

(a) Compute $G M/d^2$ by hand and check the value.
(b) Compute the mass of the sphere.
(c) Explain why the volume integral reproduces the point-mass answer exactly,
and name the theorem.
(d) State what would happen if the observation point were *inside* the sphere,
and whether the same quadrature would still reproduce the analytic answer.

---

## ★★★ Research-oriented

**★8.** Derive the reduction used by the demo:

$$\int_{z_1}^{z_2}\frac{z\,dz}{(x-x_0)^2+z^2}
= \tfrac12\ln\frac{(x-x_0)^2+z_2^2}{(x-x_0)^2+z_1^2} .$$

(a) Perform the integral.
(b) Show that the resulting one-dimensional integrand is smooth in the interior
of every interval between vertex abscissae, and say exactly where it is not
smooth and why the demo splits the range there.
(c) The body in the demo is convex. Describe precisely what the
`min(zs), max(zs)` logic does for a *non-convex* cross-section, and construct a
small counterexample where it gives the wrong field.
(d) Propose a modification that handles the non-convex case and state its cost.

---

**★9.** The demo verifies its quadrature against two exact limits. Design a
*third* independent verification for the arbitrary body of §4.2 and carry it
out.

(a) Choose a reference that shares no code with the quadrature and that has a
closed form.
(b) Carry out the comparison and report the measured relative difference.
(c) State which of the three verifications is the strongest, and why.
