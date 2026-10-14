# Exercises — 08-01-02 The Geocentric Dipole, IGRF and WMM Models

Attempt these before reading the
[solutions](./02-dipole-and-igrf-solutions.md). The lesson is
[02 The Geocentric Dipole, IGRF and WMM Models](../02-dipole-and-igrf.md). All
coefficients and coefficients-derived numbers here are **SYNTHETIC** teaching
values; nothing is quoted from IGRF or WMM.

Use $a = 6371\ \mathrm{km}$, the dipole tilt $11.5^{\circ}$, and the synthetic
axial coefficient $g_1^0 = -30000\ \mathrm{nT}$ unless a problem says otherwise.

## ★ Foundational

**★1.** Using $\tan I = 2\tan\lambda$, compute $I$ at geomagnetic latitudes
$20^{\circ}$, $35^{\circ}$ and $70^{\circ}$, and compute $\lambda$ for
$I = 55.0^{\circ}$.

**★2.** For an axial dipole with $g_1^0 = -30000\ \mathrm{nT}$ at $r = a$,
compute $X$, $Z$ and $F$ at $\lambda = 60^{\circ}$ from the component formulas,
and check the result against the demonstration's table.

**★3.** Write down the radial factor for degree $n$ and evaluate it for degree 1
and degree 4 at an altitude of $600\ \mathrm{km}$.

## ★★ Applied

**★★4.** A satellite flies at $400\ \mathrm{km}$ and measures
$F = 24991.11\ \mathrm{nT}$ at the dipole equator. Recover $|g_1^0|$ and explain
which single number you had to assume.

**★★5.** How many Gauss coefficients does a model truncated at degree 6 need?
Derive the count from the number of $(n,m)$ pairs, and compare with degree 10.
If a plan requires resolving horizontal structure of wavelength $3000\
\mathrm{km}$ at the Earth's surface, what minimum degree is needed?

**★★6.** The demonstration's degree-1 fit to a degree-1-plus-2 synthetic field
left an rms residual of 4.87% of the rms field. Using the same synthetic
coefficients, fit a degree-1 model to the **four** points
$(20^{\circ},30^{\circ})$, $(45^{\circ},120^{\circ})$,
$(-60^{\circ},250^{\circ})$, $(10^{\circ},300^{\circ})$ instead of a full grid,
and report the bias in $g_1^0$. State what feature of the local sampling causes
it.

## ★★★ Research-oriented

**★★★7.** Derive the internal/external separation algebra. A degree-$n$
harmonic has an internal form with radial dependence $(a/r)^{n+2}$ and an
external form with $(r/a)^{n-1}$; both produce the same surface field. Show how
data at two radii separate the two amplitudes, compute the degree-2 coefficients
of the separation matrix at $r = 0.95a$, and state how the conditioning behaves
as the two radii approach each other.

**★★★8.** Design a test of whether a coefficient set you have been given is
Schmidt semi-normalised or fully normalised, using only field values at a
handful of points and one of the models as a hypothesis. State the metric, the
decision rule, and the failure mode of the test.
