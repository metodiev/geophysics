# Exercises — 06-03-01 Faulting, Slip and the Elastic Rebound Cycle

Attempt these before reading the
[solutions](./01-faulting-and-slip-solutions.md). The lesson is
[01 Faulting, Slip and the Elastic Rebound Cycle](../01-faulting-and-slip.md),
and the demonstration is
[`../code/faulting_and_slip_demo.py`](../code/faulting_and_slip_demo.py). All
values are **SYNTHETIC** teaching values. A year is
$3.15576\times10^{7}\ \mathrm{s}$.

Unless a problem says otherwise, use the demo scenario
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $W = 12.0\ \mathrm{km}$,
$V = 35.0\ \mathrm{mm\,a^{-1}}$, $\Delta\tau = 3.0\ \mathrm{MPa}$,
$A = 40\ \mathrm{km}\times12\ \mathrm{km}$, $\mu_s = 0.60$.

## ★ Foundational

**★1.** Compute the loading rate $\dot\tau = \mu V/W$ in
$\mathrm{Pa\,a^{-1}}$ and in $\mathrm{Pa\,s^{-1}}$. Show the conversion between
the two, quoting the year length you use.

**★2.** Using your ★1 result, compute the mean recurrence interval $T =
\Delta\tau/\dot\tau$. State its unit.

**★3.** Compute the coseismic slip from $D = \Delta\tau W/\mu$ and the slip
deficit from $VT$ with your ★2 interval. Verify that the two agree, and explain
in one sentence why they *must* agree.

## ★★ Applied

**★★4.** A second SYNTHETIC fault has $W = 20.0\ \mathrm{km}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$ and $V = 10.0\ \mathrm{mm\,a^{-1}}$. It
releases the same $3.0\ \mathrm{MPa}$. Compute $\dot\tau$, $T$, $D$ and $M_0$
for a $20\ \mathrm{km}\times20\ \mathrm{km}$ rupture. State whether the longer or
shorter interval follows from the change in $V$ alone, and by what factor.

**★★5.** Show by substitution that $M_0/T = \mu A V$ *identically*, then evaluate
both sides for the demo scenario using $M_0 = 1.7280\times10^{19}\ \mathrm{N\,m}$
and $T = 34.29\ \mathrm{a}$.

**★★6.** The demo measures a periodicity residual of $2.69\times10^{-15}$. State
what quantity is being compared, and explain in two sentences why a residual of
$10^{-15}$ indicates agreement of the *arithmetic* and says nothing about the
physics.

**★★7.** A fault has stress drop $\Delta\tau = 3.0\ \mathrm{MPa}$ and fails with
$\mu_s = 0.60$. Compute the pore-pressure rise that would advance the cycle by
exactly $10$ years of loading at $\dot\tau = 8.7500\times10^{4}\ \mathrm{Pa\,a^{-1}}$.

## ★★★ Research-oriented

**★★★8.** The mean interval is $T = \Delta\tau W/(\mu V)$. Treat the four inputs
as independent with fractional uncertainties $20\%$ ($\Delta\tau$), $15\%$ ($W$),
$10\%$ ($V$) and $5\%$ ($\mu$). Propagate the uncertainties to $T$ in the
quadrature sense and state the dominant contributor. Then state one reason the
quadrature assumption is optimistic for this problem.

**★★★9.** Design a numerical experiment, using the demo's stress-stepping
integrator as a template, in which the stress drop is *not* constant between
events but is drawn from a distribution with a fixed mean. Specify the
distribution, the metric you will use to decide whether the sequence still looks
periodic, and the observation you expect. A specification that could not be
executed is a failed answer.

**★★★10.** The block-slider model puts all the deformation in a layer of width
$W$ and assumes the stress drop is uniform on the ruptured patch. Using only the
energy and force balance in Sections 3.1–3.3 of the lesson, argue (a) in which
direction the true mean interval is biased if part of the relative motion is
taken up by aseismic creep below $W$, and (b) why quoting a recurrence interval
without an aseismic-slip estimate is reporting an upper or lower bound rather
than a value.
