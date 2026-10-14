# Exercises — 14-04-01 Contaminant Plumes and Their Geophysical Signature

Attempt before the [solutions](./01-contaminant-plumes-solutions.md). Lesson:
[01 Contaminant Plumes and Their Geophysical Signature](../01-contaminant-plumes.md).
All models **SYNTHETIC**; the tracer is a generic idealised ionic solute in
arbitrary concentration units (CU). No real contaminant or site is referenced.

Use $\theta = 0.30$, $\rho_b = 1855\ \mathrm{kg\,m^{-3}}$,
$\sigma_{w0} = 0.050\ \mathrm{S\,m^{-1}}$, $\beta = 1.0\times10^{-4}\
\mathrm{S\,m^{-1}}$ per CU, $\phi = 0.30$, $a = 1$, $m = 2$ unless stated.

## ★ Foundational

**★1.** For $K_d = 0.02\ \mathrm{mL\,g^{-1}}$, $\rho_b = 1800\
\mathrm{kg\,m^{-3}}$ and $\theta = 0.28$, compute the retardation factor and the
solute velocity for a seepage velocity of $0.060\ \mathrm{m\,day^{-1}}$. State
the units of every factor.

**★2.** For the lesson's reference model ($v = 0.050\ \mathrm{m\,day^{-1}}$,
$\alpha_L = 1.0\ \mathrm{m}$, $R = 1.3092$) compute the front position and the
10–90% transition width after 5 years.

**★3.** Compute the bulk resistivity at $C = 0$ and $C = 300$ CU. State the
assumption in the conversion from concentration to bulk conductivity.

## ★★ Applied

**★★4.** The apparent resistivity has a $3\%$ one-sigma repeatability and the
background pore-fluid conductivity is $0.050\ \mathrm{S\,m^{-1}}$. **(a)** Compute
the smallest detectable concentration at one and two sigma. **(b)** Repeat for a
background ten times more conductive and state the ratio of the two thresholds.

**★★5.** A monitoring sensor sits $30\ \mathrm{m}$ down-gradient.
**(a)** Using the reference model, compute the arrival time of the 50% front.
**(b)** Compute the resistivity at the sensor at the moment of arrival.
**(c)** Compute it again 517 days later and state what fraction of the full
change has occurred.

**★★6.** A resistivity drop of a factor of $2.5$ is mapped. Name three
mechanisms other than the tracer that would produce it, and for each state the
independent measurement that would separate it.

## ★★★ Research-oriented

**★★★7.** Derive the detection threshold
$C_\text{min} = \varepsilon\sigma_{w0}/[\beta(1-\varepsilon)]$ from
$\Delta\rho/\rho = \Delta\sigma_w/\sigma_w$ and $\sigma_w = \sigma_{w0} +
\beta C$. **(a)** Show that the threshold is proportional to $\sigma_{w0}$ and
explain the consequence for site screening. **(b)** Show what happens as
$\varepsilon \to 1$ and explain why that limit is not physical. **(c)** State the
one thing that improves the threshold without changing the site.

**★★★8.** Design a time-lapse monitoring programme for an idealised tracer
release that must constrain both the solute velocity and the dispersivity.
**(a)** Choose the survey schedule and justify it from the shape of the
concentration breakthrough curve. **(b)** Allocate the measurements between a
dense array and a sparse one, giving a reason. **(c)** State the two systematic
errors that differencing removes and the one it does not. **(d)** State the
minimum measurable change of solute velocity given a stated arrival-time
uncertainty, and show the arithmetic.
