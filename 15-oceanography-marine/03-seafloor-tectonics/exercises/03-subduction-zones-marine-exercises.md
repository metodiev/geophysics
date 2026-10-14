# Exercises — 15-03-03 Marine Subduction Zones, Trenches and Accretionary Prisms

Attempt these before the
[solutions](./03-subduction-zones-marine-solutions.md). The lesson is
[03 Marine Subduction Zones](../03-subduction-zones-marine.md). All models and
data are **SYNTHETIC** teaching values; the model constants are those printed by
`code/subduction_zones_marine_demo.py`.

## ★ Foundational

**★1.** With $K=3.000$, $\mu_b=0.55$, $\lambda=\lambda_b=0.30$ and
$\beta=4^\circ$, compute the critical taper $\theta$ and the surface slope
$\alpha$ in degrees. Show the arithmetic.

**★2.** Compute $D=ET_e^3/[12(1-\nu^2)]$ for $T_e=20\ \mathrm{km}$,
$E=70\ \mathrm{GPa}$, $\nu=0.25$, and state its unit. Then compute
$\alpha_f=(4D/\Delta\rho g)^{1/4}$ for $\Delta\rho=2270\ \mathrm{kg\,m^{-3}}$.

**★3.** A line load of $2.0\times10^{12}\ \mathrm{N\,m^{-1}}$ acts on a plate
whose flexural parameter is $74.12\ \mathrm{km}$ and whose rigidity is
$1.68\times10^{23}\ \mathrm{N\,m}$. Compute the peak deflection and the height and
position of the outer-rise bulge.

## ★★ Applied

**★★4.** Using the taper relation, compute how much $\lambda$ must rise from 0.40
to double the surface slope $\alpha$ for $\beta=3^\circ$, $\mu_b=0.55$,
$K=3.000$. State whether the required change is physically attainable, and what
limits it.

**★★5.** A prism receives $500\ \mathrm{m}$ of sediment at a convergence rate of
$60\ \mathrm{mm\,yr^{-1}}$. Compute the volume flux in
$\mathrm{km^3\,Myr^{-1}\,km^{-1}}$, then the prism cross-section and the prism
width after 5 Myr for accreted fractions of 0.25 and 0.75 at a taper of
$12.17^\circ$. By what factor does the width change?

**★★6.** Compute the fibre stress for the lesson's model at $T_e=30\ \mathrm{km}$
and at $T_e=20\ \mathrm{km}$ with the load adjusted so the deflection stays at
$908.8\ \mathrm{m}$. State the scaling that relates the two answers and explain
why it is not simply $\propto T_e^{-2}$.

## ★★★ Research-oriented

**★★★7.** The taper relation contains three unknowns
($\mu_b(1-\lambda_b)$, $\lambda$, $K$) and one measured angle. Specify the
measurements that would determine the system: for each, say what it measures, the
precision required for a $\pm1$ MPa constraint on the décollement's effective
stress at 3 km depth, and which unknown remains unconstrained if the measurement
is unavailable. Show the arithmetic that relates your precision requirement to the
taper sensitivity $\mathrm{d}\alpha/\mathrm{d}\lambda$ computed in the lesson.

**★★★8.** The lesson's flexure model predicts an outer-rise bulge of
$39.3\ \mathrm{m}$ at $232.8\ \mathrm{km}$ from the load. Observed outer rises are
often larger and closer to the trench. Enumerate the model assumptions that would
have to change to produce a larger, nearer bulge — at least three — and for each
state whether the change makes the plate stronger or weaker and what observation
would discriminate the alternatives. Conclude with the one statement about
$T_e$ that your data set can support and the one it cannot.
