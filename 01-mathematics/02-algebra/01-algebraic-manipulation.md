---
id: 01-02-01
title: "Algebraic Manipulation and Solving Equations"
level: beginner
prereqs: ["01-01-01"]
estimated_minutes: 75
tags: [algebra, equations, rearrangement, substitution]
---

# Algebraic Manipulation and Solving Equations

## Learning objectives

By the end of this lesson you will be able to:

1. **Rearrange** a physical relation for any symbol in it, using only
   equivalence-preserving operations.
2. **Solve** linear, quadratic and simple rational equations, and equations in
   which the unknown appears in an exponent.
3. **Recognise** the two operations that are not equivalences — squaring and
   multiplying by an expression that can vanish — and guard against their
   consequences.
4. **Check** every solution three ways: by substitution, by dimensions, and by a
   limiting case.
5. **Translate** a geophysical word problem into an equation, solve it, and
   interpret the answer with its units.

## Prerequisites

[01-01-01 Number Systems, Precision and Scientific Notation](../01-arithmetic/01-number-systems-and-precision.md)
for units and significant figures. Nothing else: this lesson starts from school
algebra.

## 1. Intuition: physics arrives as equations, not as answers

An instrument gives you a measurement; the physics gives you a relation between
measurements. The work of going from one to the other is algebra.

Consider three sentences that a geophysicist writes on an almost daily basis:

- "The two-way travel time is $t = 2d/v$; I know $t$ and $v$, so what is $d$?"
- "The anomaly of a buried sphere is $g = GM/d^{2}$; I measured $g$ and know
  $M$ roughly, so how deep is it?"
- "The activity has fallen to a fraction $f$ of its initial value and the decay
  constant is $\lambda$; how old is the sample?"

Each is the same operation: isolate the symbol you want. The rest of this lesson
is about doing that reliably, and about the two places where the obvious move is
wrong.

## 2. The rules of the game

### 2.1 Equivalence-preserving operations

An equation is a statement that two expressions are equal. You may apply to both
sides any operation that is:

- **well defined everywhere on the current domain**, and
- **one-to-one (injective)** on that domain.

Safe: add or subtract the same quantity; multiply or divide by a nonzero constant;
apply $\exp$; take a logarithm of a positive quantity; take an odd root.

Unsafe, and the source of nearly every algebra error in practice:

| operation | what can go wrong |
|---|---|
| divide by an expression that can vanish | you silently divide by zero and may lose solutions |
| square both sides | you **gain** extraneous solutions |
| take a square root | you may lose the negative branch |
| multiply an inequality by a negative | the direction reverses |

### 2.2 The discipline of the check

Because the two dangerous operations can both add and remove solutions, no
algebra is finished until the candidates have been **substituted back into the
original equation** — not into a rearranged form, and never into a squared form.
This single habit catches more errors than any amount of care during the
manipulation.

## 3. Solving by kind of equation

### 3.1 Linear equations

An equation is linear in $x$ if it can be written $ax + b = 0$ with $a \ne 0$.
The solution is $x = -b/a$, unique. If $a = 0$ there is either no solution
($b \ne 0$) or every $x$ is a solution ($b = 0$); never divide by $a$ without
asking whether it can be zero.

**Geophysical example.** Heat conduction in a steady state gives a linear
geothermal profile, $T(z) = T_0 + \gamma z$, where $\gamma$ is the geothermal
gradient. Solving for depth:

$$z = \frac{T - T_0}{\gamma}, \qquad \gamma \ne 0.$$

A measured temperature of $135.0\,^\circ$C with $T_0 = 10.0\,^\circ$C and
$\gamma = 25.0\,^\circ$C/km gives $z = 5.00$ km. Note the role of the
non-vanishing condition: a zero gradient would mean the temperature carries no
information about depth.

### 3.2 Quadratic equations

Any quadratic can be written $ax^{2} + bx + c = 0$ with $a \ne 0$. Two routes
are worth having at your fingertips:

- **Factorisation** when the roots are simple: $x^{2} - 3x + 2 = (x-1)(x-2)$.
- **The quadratic formula**, valid always:

$$x = \frac{-b \pm \sqrt{b^{2} - 4ac}}{2a}.$$

The **discriminant** $\Delta = b^{2} - 4ac$ tells you the character of the
solutions: $\Delta > 0$ two distinct real roots, $\Delta = 0$ one repeated real
root, $\Delta < 0$ a complex-conjugate pair (which geophysics meets in wave
propagation, and which is treated in
[01-11 Complex Numbers and Analysis](../11-complex-analysis/README.md)).

Numerical warning, carried over from
[01-01-04](../01-arithmetic/04-floating-point.md): when $\Delta$ is close to
$b^{2}$, the root using the subtraction cancels, and it should be obtained from
the product of the roots, $x_1x_2 = c/a$, instead.

### 3.3 Rational equations

If the unknown appears in a denominator, multiply through by the denominators but
**record every value that makes a denominator zero**. Those values are not
solutions, whatever the rearranged equation says.

**Example.** Solve

$$\frac{1}{v} = \frac{1}{v_1} + \frac{1}{v_2}$$

for $v$ — the parallel-resistance form, which also describes the effective
velocity of a layered medium in the time-average sense. Multiplying by
$v v_1 v_2$ gives $v_1v_2 = v(v_2 + v_1)$, hence

$$v = \frac{v_1v_2}{v_1 + v_2},$$

provided $v_1, v_2 \ne 0$ and $v_1 + v_2 \ne 0$ — which for physical velocities
is automatic, but must be stated.

### 3.4 Equations with the unknown in an exponent

If the unknown is in an exponent, isolate the exponential and take logarithms:

$$A e^{-kx} = B \;\Longrightarrow\; e^{-kx} = \frac{B}{A}
\;\Longrightarrow\; -kx = \ln\frac{B}{A}
\;\Longrightarrow\; x = -\frac{1}{k}\ln\frac{B}{A},$$

valid for $A \ne 0$, $B > 0$ and $k \ne 0$. Both signs matter: $B \le 0$ means no
real solution, and $k = 0$ means the exponential is constant and carries no
information about $x$. This one rearrangement underlies radiometric dating,
seismic attenuation, and the film-cooling law of geothermal exploration, and is
developed systematically in
[01-02-03](./03-exponentials-logarithms.md).

### 3.5 Two equations at a time

With two unknowns, the reliable hand method is **substitution**: solve one
equation for one unknown, substitute into the other, and reduce to one equation
in one unknown. Systematic elimination is deferred to
[01-02-05](./05-systems-of-equations.md).

## 4. Checking: three cheap tests

1. **Substitution.** Put the value back into the *original* equation and evaluate
   both sides. Numerical agreement to the precision of the data is the criterion.
2. **Dimensions.** Every term in a physical equation must have the same
   dimensions. If your rearranged formula puts metres on one side and seconds on
   the other, the algebra is wrong — see
   [01-01-03 Units and Dimensional Analysis](../01-arithmetic/03-units-and-dimensional-analysis.md).
3. **Limiting cases.** Push a parameter to a value where you know the answer.
   If $x = -\ln(B/A)/k$, then setting $B = A$ must give $x = 0$, and it does. If a
   formula for depth from a travel time gives a *negative* depth for a positive
   time, you have a sign error.

## 5. Worked derivations

### 5.1 Depth from a two-way travel time

A reflection's two-way time is $t = 2d/v$ with $v$ the (assumed constant) speed.

**Isolate $d$.** Divide both sides by 2 and multiply by $v$:

$$d = \frac{v t}{2}.$$

With $v = 4800$ m/s and $t = 1.25$ s this gives $d = 3000.0$ m. Substituting
back, $2d/v = 6000/4800 = 1.250000$ s, which matches the input exactly — the
check that the rearrangement introduced no error.

**Limiting case.** $t = 0 \Rightarrow d = 0$, as it must. Units:
$(\mathrm{m\,s^{-1}})(\mathrm{s}) = \mathrm{m}$.

### 5.2 Rearranging a product for whichever symbol you need

The point-mass gravity anomaly is

$$g = \frac{GM}{d^{2}}.$$

Solving for each symbol:

$$M = \frac{g d^{2}}{G}, \qquad d = \sqrt{\frac{GM}{g}}, \qquad G = \frac{g d^{2}}{M}.$$

The middle one is worth a remark: solving for $d$ requires a square root, so
**only the positive root is physical** — a depth cannot be negative. The minus
branch is a reminder that roots must be interpreted, not merely computed.

Demonstration numbers: with $G = 6.674\times10^{-11}$,
$M = 1.0\times10^{12}$ kg and $d = 1500$ m, the anomaly is
$g = 2.966222\times10^{-5}\ \mathrm{m\,s^{-2}}$, i.e. 2.966 mGal. Inverting
returns $d = 1500.000000$ m and $M = 1.000000\times10^{12}$ kg.

### 5.3 The step that manufactures solutions

Solve

$$\sqrt{x + 5} = x - 1.$$

Square both sides: $x + 5 = x^{2} - 2x + 1$, i.e. $x^{2} - 3x - 4 = 0$, i.e.
$(x-4)(x+1) = 0$, so the candidates are $x = 4$ and $x = -1$.

Now substitute into the **original** equation:

| candidate | left side $\sqrt{x+5}$ | right side $x - 1$ | valid? |
|---|---|---|---|
| $x = 4$ | $3.000000$ | $3.000000$ | **yes** |
| $x = -1$ | $2.000000$ | $-2.000000$ | **no** |

The candidate $x = -1$ arose because squaring cannot distinguish a number from
its negative. This is not a technicality: it is the reason that both sides of a
squared equation must be checked for sign consistency.

### 5.4 Solving for the argument of an exponential

An Arrhenius-type relation between a diffusion coefficient and temperature is

$$D = D_0 \exp\!\left(-\frac{E_a}{R T}\right).$$

Solve for $T$. Divide by $D_0$, take the natural logarithm, then rearrange:

$$\ln\frac{D}{D_0} = -\frac{E_a}{RT}
\qquad\Longrightarrow\qquad
T = \frac{E_a}{R\,\ln(D_0/D)}.$$

Note the sign pattern: a *negative* logarithm of a ratio above 1 becomes a
positive denominator, so the expression is positive as long as $D_0 > D > 0$,
which is guaranteed because $D \le D_0$ for a thermally activated process.

**Numbers.** Using **ILLUSTRATIVE** constants — not literature values for any
particular mineral — $D_0 = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$,
$E_a = 2.0\times10^{5}$ J/mol, $R = 8.31446261815324$ J/(mol K), and a target
$D = 1.0\times10^{-18}\ \mathrm{m^{2}\,s^{-1}}$:

$$T = \frac{2.0\times10^{5}}{8.31446 \times \ln(10^{12})} = 870.560\ \mathrm{K}.$$

Substituting back gives $D = 1.000000\times10^{-18}\ \mathrm{m^{2}\,s^{-1}}$ —
the check. Dimensionally, J/mol divided by (J mol$^{-1}$ K$^{-1}$ × dimensionless)
is kelvin, as required.

*Caveat, stated deliberately:* real diffusion constants have their own
uncertainties in $D_0$ and $E_a$, and the answer above is a demonstration of the
algebra, not a statement about any rock.

### 5.5 Solving a refraction problem for layer thickness

Two horizontal layers with speeds $v_1 < v_2$ produce a direct arrival
$t_d = x/v_1$ and a head wave

$$t_h = \frac{x}{v_2} + \frac{2H\cos\theta_c}{v_1},$$

where $\theta_c$ is the critical angle satisfying $\sin\theta_c = v_1/v_2$ and
$H$ is the thickness of the first layer.

**Crossover distance.** Setting $t_d = t_h$:

$$\frac{x}{v_1} - \frac{x}{v_2} = \frac{2H\cos\theta_c}{v_1}
\;\Longrightarrow\;
x\left(\frac{v_2 - v_1}{v_1v_2}\right) = \frac{2H\cos\theta_c}{v_1}
\;\Longrightarrow\;
x_c = \frac{2H v_2\cos\theta_c}{v_2 - v_1}.$$

Using $\cos\theta_c = \sqrt{1 - (v_1/v_2)^{2}} = \sqrt{v_2^{2}-v_1^{2}}/v_2$
and $v_2^{2}-v_1^{2} = (v_2-v_1)(v_2+v_1)$:

$$x_c = \frac{2H\sqrt{v_2^{2}-v_1^{2}}}{v_2 - v_1}
= 2H\sqrt{\frac{v_2+v_1}{v_2-v_1}}.$$

**Solving for $H$** is then immediate:

$$H = \frac{x_c}{2}\sqrt{\frac{v_2 - v_1}{v_2 + v_1}}.$$

**Numbers.** $v_1 = 1200$ m/s, $v_2 = 3000$ m/s, $x_c = 60$ m:

$$\theta_c = \arcsin(1200/3000) = 23.5782^\circ, \qquad H = 19.639610\ \mathrm{m}.$$

The same value is obtained by bisection on the residual, which is a useful
independent check and a preview of
[01-02-04](./04-polynomials-roots.md): the two routes agree to all printed
digits.

**Interpretation.** A near-surface layer 19.6 m thick with a 2.5:1 velocity
contrast produces a crossover at 60 m. Note the sensitivity: because $H$ scales
linearly with $x_c$ but only as the square root of the velocity ratio, a 10%
error in the crossover distance is a 10% error in thickness, while a 10% error in
the velocity ratio is only a 5% error in thickness.

## 6. Python demonstration

```bash
python3 code/algebraic_manipulation_demo.py
```

The script `code/algebraic_manipulation_demo.py` uses only the standard library
and covers: solving for a target variable and checking by substitution;
rearranging $g = GM/d^{2}$ three ways; extraneous roots from squaring; verifying
an identity by sampling; solving for a temperature inside an exponential; a
$2\times2$ system by substitution; and the danger of dividing by a quantity that
can vanish. Observed output:

```text
d = v t / 2 = 4800 * 1.25 / 2 = 3000.000 m
check by substitution: 2d/v = 1.250000000000 s = t
```

```text
solve sqrt(x + 5) = x - 1
  x =   4.0: left side = 3.000000, right side = 3.000000, equal? True
  x =  -1.0: left side = 2.000000, right side = -2.000000, equal? False
```

```text
for D = 1e-18 m**2/s:  T = Ea / (R ln(D0/D)) = 870.560 K
check: D(T) = 1.000000e-18 m**2/s
```

| Observation | Consequence in geophysics |
|---|---|
| substitution reproduces the input | the rearrangement is verified, not assumed |
| $x=-1$ satisfies the squared equation but not the original | always substitute into the *original* |
| the exponential inversion needs $\ln(D_0/D)$ | sign conventions in age equations are where errors hide |
| the $2\times2$ system solved in two lines | small systems are best done by substitution, and checked |

## 7. Exercises

Ten graded exercises with full worked solutions are in
[`exercises/01-algebraic-manipulation-exercises.md`](./exercises/01-algebraic-manipulation-exercises.md)
and
[`exercises/01-algebraic-manipulation-solutions.md`](./exercises/01-algebraic-manipulation-solutions.md).

**★1.** Solve for $v$: $\dfrac{1}{v} = \dfrac{1}{v_1} + \dfrac{1}{v_2}$, and
state the conditions on $v_1$ and $v_2$.

**★★2.** Solve for $H$ in $x_c = 2H\sqrt{(v_2+v_1)/(v_2-v_1)}$ and evaluate for
$v_1 = 1500$ m/s, $v_2 = 4000$ m/s, $x_c = 120$ m.

**★★★3.** A cubic has three real roots, two of them close together. Explain how
the closed-form quadratic result for the remaining factor becomes inaccurate as
the two roots coalesce, and design a numerical experiment that measures the
degradation. Report the method, the measured crossover, and the limitation of
your conclusion.

## 8. Common mistakes

1. **Dividing by a symbol without asking whether it can vanish.** A zero velocity
   or a zero gradient is physically possible, and the division is then invalid.
2. **Squaring to remove a root sign and stopping there.** Check the sign of both
   sides of the original equation.
3. **Dropping the negative root of $d^{2} = GM/g$.** It is a genuine solution of
   the algebra and a non-solution of the physics; say which you are using and why.
4. **Forgetting that a logarithm needs a positive argument.** $\ln(D/D_0)$ with
   $D > D_0$ describes a process that cannot happen, not a negative temperature.
5. **Rearranging an inequality as if it were an equation.** Multiplying by a
   negative quantity reverses the direction.
6. **Checking the answer in the rearranged equation only.** A rearrangement can
   be wrong; the original equation cannot.

## 9. Real-world applications

- **Seismic reflection processing.** Converting two-way times to depths,
  normal-moveout corrections, and velocity analysis are all rearrangements of
  travel-time equations.
- **Geochronology.** The age equation $D^{*}/P = e^{\lambda t} - 1$ is inverted
  with a logarithm; the same algebra appears for every decay scheme.
- **Refraction and travel-time interpretation.** Layer thickness from crossover
  distance, as in Section 5.5, is a standard field calculation.
- **Heat flow and thermal modelling.** Geothermal gradients, cooling times, and
  the thermal time constant of an intrusion are linear, quadratic and exponential
  rearrangements respectively.
- **Instrument calibration.** Converting a measured reading to a physical value
  through a two-point calibration is a linear system solved by substitution.

## 10. Further reading

- **Bronshtein, I. N., Semendyayev, K. A., Musiol, G., & Mühlig, H. *Handbook of
  Mathematics* (current edition). Springer.** Level: reference. The standard
  compact reference for algebraic identities and elementary solution formulae.
- **Stewart, J. *Calculus: Early Transcendentals* (current edition).** Chapters
  1–2 and the algebra review appendix. Level: beginner. Reliable for the
  algebraic manipulation techniques assumed here.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd
  ed.). Wiley.** Chapters 1–2. Level: beginner to intermediate. Written for
  physical scientists, with problems that are actually physical.
- **Wilson, W. *A Refresher Course in Mathematics* or any comparable
  school-algebra text.** Level: beginner. Nothing here requires more.

> Note on citations: bibliographic details above are given so you can locate the
> works, and several are widely used textbooks whose exact printing varies. This
> repository does not host or reproduce copyrighted text; confirm editions and
> availability through your library before citing.

## 11. Related lessons

- [02 Functions, Graphs and Transformations](./02-functions-and-graphs.md) —
  the shapes these equations describe.
- [03 Exponentials, Logarithms and Decay Laws](./03-exponentials-logarithms.md)
  — Section 3.4 developed in full.
- [04 Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md) —
  Section 3.2 generalised to higher degree.
- [05 Linear and Nonlinear Systems of Equations](./05-systems-of-equations.md)
  — Section 3.5 generalised.
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../01-arithmetic/03-units-and-dimensional-analysis.md)
  — the dimensional check of Section 4.

## Self-assessment checklist

- [ ] I can rearrange a formula for any symbol and check it by substitution.
- [ ] I can solve a quadratic, including the case of a repeated root.
- [ ] I can list the values that make a denominator zero before dividing.
- [ ] I can solve for a variable inside an exponential.
- [ ] I always substitute candidate solutions into the original equation.
- [ ] I can state what each symbol's units are in the final expression.
