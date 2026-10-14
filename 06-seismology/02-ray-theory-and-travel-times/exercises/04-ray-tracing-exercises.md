# Exercises — 06-02-04 Ray Tracing in Laterally Varying Media

Attempt these before reading the
[solutions](./04-ray-tracing-solutions.md). The lesson is
[04 Ray Tracing in Laterally Varying Media](../04-ray-tracing.md). All models are
**SYNTHETIC** teaching values. Numbers marked "from the demo" are printed by
`code/ray_tracing_demo.py`.

## ★ Foundational

**★1.** For $v(z) = 2500 + 0.60z\ \mathrm{m\,s^{-1}}$ and a take-off angle
$i_0 = 30^\circ$ from the vertical, compute the ray parameter $p$ and the arc
radius $R$ of the ray, with units.

**★2.** For the same ray, compute the turning depth $z_t$, the surface offset $X$
and the travel time $T$ from the closed forms of the lesson.

**★3.** State the ray equation in the form
$\mathrm{d}/\mathrm{d}s\left(v^{-1}\mathrm{d}\mathbf{x}/\mathrm{d}s\right) =
\nabla(v^{-1})$ and check it dimensionally, term by term.

## ★★ Applied

**★★4.** A receiver sits at $X = 10.000$ km on the model of ★1. Solve the
two-point problem exactly (the offset is $X = (2v_0/G)\cot i_0$), giving the
take-off angle, ray parameter and travel time. Then repeat it by bracketing with
the values at $30^\circ$ and $45^\circ$ and linear interpolation, and state the
interpolation error.

**★★5.** The demo's tracer is validated against a travel-time engine at five
distances (from the demo, $T$ from the engine / from the tracer in seconds):

| Δ | engine $T$ | tracer $T$ |
|---|---|---|
| 30° | 370.2639 | 370.0524 |
| 45° | 496.9685 | 496.9802 |
| 60° | 608.2804 | 608.3122 |
| 75° | 703.2422 | 703.3190 |
| 90° | 781.3348 | 782.1434 |

Compute the time error and the relative time error at each distance, identify
where the agreement degrades, and state the reason given in the lesson.

**★★6.** The demonstration reports a quadrature error of 0.5000 ms and a
model-error scatter of $113.162$ ms for a 1 % velocity perturbation. Compute the
ratio, and state the single change to the experiment that would most improve the
answer.

## ★★★ Research-oriented

**★★★7.** Write a validation plan for a *two-dimensional* ray tracer (one that
handles $v(x,z)$), including: a closed-form or semi-analytic case with lateral
variation that can be used as a reference, the two quantities to compare, the
grid or step refinement that establishes convergence, and the specific outcome
that would show the tracer was returning only first arrivals when several exist.
A plan that cannot be executed is a failed answer.

**★★★8.** At $90^\circ$ the tracer is wrong by $0.163307^\circ$ in distance and
$0.8086$ s in time. Using the neighbouring rows of the table, estimate the local
slope $\mathrm{d}T/\mathrm{d}\Delta$ and predict the time error implied by the
distance error. Compare the prediction with the measured time error, and state
what the agreement shows about the nature of the tracer's failure.
