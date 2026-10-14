# Exercises — 07-04-05 ITRF, Plate Motion Models and Frame Transformations

Attempt these before reading the
[solutions](./05-itrf-and-plate-models-solutions.md). The lesson is
[05 ITRF and Plate Motion Models](../05-itrf-and-plate-models.md). All poles,
rates, stations and frames are **SYNTHETIC**; use
$R = 6371\ \mathrm{km}$ and
$1^{\circ}\,\mathrm{Myr^{-1}} = 1.745329\times10^{-8}\ \mathrm{rad\,yr^{-1}}$.

## ★ Foundational

**★1.** Convert $2.5^{\circ}\,\mathrm{Myr^{-1}}$ to $\mathrm{rad\,yr^{-1}}$ and to
a velocity at the equator for a rigid rotation whose pole is on the equator.

**★2.** Write $\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}$ in components and
verify by direct calculation that $\mathbf{v}\cdot\mathbf{r} = 0$.

**★3.** State why three parameters describe a rigid plate's velocity field, and
what the residuals of an Euler-vector fit then mean physically.

## ★★ Applied

**★★4.** A pole is at $(50^{\circ}, -120^{\circ})$ with rate
$0.90^{\circ}\,\mathrm{Myr^{-1}}$. Compute the angular velocity vector and the
horizontal speed at a station at $(0^{\circ}, 0^{\circ})$, and verify your answer
against the lesson's table ($94.77\ \mathrm{mm\,yr^{-1}}$).

**★★5.** Two plates have poles $(30^{\circ}, 10^{\circ})$ at
$0.60^{\circ}\,\mathrm{Myr^{-1}}$ and $(60^{\circ}, -170^{\circ})$ at
$0.40^{\circ}\,\mathrm{Myr^{-1}}$. Compute the relative pole and rate, and the
relative speed per Earth radius.

**★★6.** Estimate the velocity error introduced by an unmodelled frame rotation of
$0.05\ \mathrm{mas\,yr^{-1}}$ at the equator and at $60^{\circ}$ latitude, and state
whether it would be mistaken for strain.

## ★★★ Research-oriented

**★★★7.** A network of five stations fits one Euler vector with residuals of
$1.5\ \mathrm{mm\,yr^{-1}}$. Decide whether the network can distinguish the plate
rotation from an internal deformation field of $10\ \mathrm{nstrain\,yr^{-1}}$,
stating the test and the data you would need.

**★★★8.** Design a station distribution that determines a plate's Euler pole to
$0.5\%$ in rate and $1^{\circ}$ in pole position, given
$1\ \mathrm{mm\,yr^{-1}}$ velocity noise. State the geometry condition, the number
of stations, and the frame requirements.
