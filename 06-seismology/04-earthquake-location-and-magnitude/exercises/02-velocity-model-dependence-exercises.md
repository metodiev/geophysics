# Exercises — 06-04-02 Dependence on the Velocity Model and Joint Inversion

Attempt these before reading the
[solutions](./02-velocity-model-dependence-solutions.md). The lesson is
[02 Dependence on the Velocity Model and Joint Inversion](../02-velocity-model-dependence.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A travel time in a reference model is $T = 24.000\ \mathrm{s}$. Compute
the predicted time if every velocity is multiplied by $s = 1.03$, and state why
the ray path does not change.

**★2.** For $d = +0.02$, compute $1 - 1/(1+d)$ and use it to find the residual at
stations with $T = 14.423\ \mathrm{s}$ and $T = 118.029\ \mathrm{s}$.

**★3.** State, in one sentence, why the bias from a uniform velocity error cannot
be reduced by adding stations.

## ★★ Applied

**★★4.** Given $\mathrm{d}^{2}\chi^{2}/\mathrm{d}z^{2} = 2.2295\ \mathrm{km^{-2}}$,
compute $\sigma_z$ and the 95 per cent depth bound, and compare with the
$+2$ per cent bias of $-5.75\ \mathrm{km}$.

**★★5.** The demonstration's picks accept a uniform velocity error of only
0.19 per cent. Using the acceptance criterion "rms residual below
$\sigma_t = 0.05\ \mathrm{s}$", show by hand why a 1 per cent error fails at
every depth (use the residual scale factor of ★2).

**★★6.** Explain the sign of the bias: why does a *faster* locating model place
this regional event *shallower*? Use
$\partial T/\partial z = z/(v r)$ and the fact that the residual grows with
epicentral distance.

## ★★★ Research-oriented

**★★★7.** Specify a joint inversion for (depth, velocity scale) that would use a
borehole velocity measurement with a stated 3 per cent uncertainty, and predict
how the depth interval from the demonstration's consistency scan would change.

**★★★8.** Design a numerical experiment to decide whether a *depth-dependent*
velocity error (for example a 10 per cent error confined to the top 5 km) biases
the depth in the same direction as a uniform error of the same average size.
State the metric, the control, and the expected outcome if the two differ.
