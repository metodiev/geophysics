# Exercises — 10-04-03 Near-Surface Refraction for Static Corrections

Attempt these before reading the
[solutions](./03-refraction-static-solutions.md). The lesson is
[03 Near-Surface Refraction for Static Corrections](../03-refraction-static.md).
All models and data in this module are **SYNTHETIC**: the velocities, weathering
depths, elevations, datum, replacement velocity and timing errors are teaching
values. The formulas used for the stack response and the surface-consistent
decomposition are exact and are derived in the lesson.

## ★ Foundational

**★1.** Compute the weathering-layer depth for an intercept time of
$9.5\ \mathrm{ms}$, $v_w = 500\ \mathrm{m\,s^{-1}}$ and
$v_r = 1600\ \mathrm{m\,s^{-1}}$. Show the arithmetic for both square roots and
state the units.

**★2.** A systematic static error of $4.0\ \mathrm{ms}$ affects every trace. Compute
the stack amplitude factor at $25$, $50$ and $100\ \mathrm{Hz}$, and state which
frequency band the error removes and what happens at $100\ \mathrm{Hz}$.

**★3.** A station has a weathering thickness of $4.5\ \mathrm{m}$
($v_w = 550\ \mathrm{m\,s^{-1}}$) and lies $3.0\ \mathrm{m}$ above the datum, with
a replacement velocity of $2200\ \mathrm{m\,s^{-1}}$. Compute the two terms of the
datum static separately, the total, and the value the formula gives if the datum
were placed at the base of the weathering.

## ★★ Applied

**★★4.** A refraction solution adopts $v_w = 660\ \mathrm{m\,s^{-1}}$ where the
truth is $600\ \mathrm{m\,s^{-1}}$, with $v_r = 1800\ \mathrm{m\,s^{-1}}$. For a
uniform weathering thickness of $3.5\ \mathrm{m}$, compute the intercept time, the
depth from the wrong velocity, the weathering time from both, and the stack factor
at $40$ and $80\ \mathrm{Hz}$ for the time difference. State which consequence you
would notice first in the field, and why the answer is uncomfortable.

**★★5.** Two surface-consistent static solutions for the same line differ only by
$8.0\ \mathrm{ms}$ added to every source term and subtracted from every receiver
term. **(a)** Show that both fit the data equally well, quoting the residual
difference. **(b)** Compute the apparent depth difference this makes to a reflector
at $2.5\ \mathrm{s}$ with a stacking velocity of $3000\ \mathrm{m\,s^{-1}}$.
**(c)** State which measurement fixes the disagreement.

**★★6.** A reflection is stacked with a $2.0\ \mathrm{ms}$ systematic static error
and, in a second processing run, with a $2.0\ \mathrm{ms}$ rms random static
error. Compute both stack factors at $30$, $60$ and $120\ \mathrm{Hz}$, state
which run has the better high-frequency content, and explain why the two factors
agree so closely at $30\ \mathrm{Hz}$ while differing by a factor of five at
$120\ \mathrm{Hz}$.

## ★★★ Research-oriented

**★★★7.** Design a statics workflow for a $5\ \mathrm{km}$ line crossing
$15\ \mathrm{m}$ of topographic relief over a weathered layer whose thickness
varies between $1$ and $8\ \mathrm{m}$. Specify: the acquisition that determines the
weathering velocity (shot/receiver geometry and spacing), what fixes the absolute
level of the static profile, what fixes the long-wavelength shape, the frequency
band you will use to verify the result, and the independent check you will run at
the end. A specification that could not be executed is a failed answer.

**★★★8.** A two-layer refraction fit overestimates the weathering velocity because
a thin low-velocity layer lies within the weathered zone (the blind-zone problem of
[06-10-01](../../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md)).
For a weathering layer of true velocity $450\ \mathrm{m\,s^{-1}}$ and true
thickness $3.0\ \mathrm{m}$ that the fit reports as $600\
\mathrm{m\,s^{-1}}$, compute the intercept time, the fitted depth, the weathering
time from the fit, and the stack factors at $40$ and $80\ \mathrm{Hz}$. Explain
why the stack is an almost silent witness to this error, and state both the
measurement that would detect it and what it looks like in a residual-statics map.

**★★★9.** Compare the frequency dependence of systematic and random static errors
for $2\ \mathrm{ms}$ and $6\ \mathrm{ms}$ at $30$, $60$ and $120\ \mathrm{Hz}$.
State which kind of error a residual-statics pass can estimate from the data and
which it cannot, and construct the argument in terms of the null space derived in
Section 3.4 of the lesson.
