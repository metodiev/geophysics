# Exercises — 10-03-04 GPR for Pavements, Concrete and Infrastructure Inspection

Attempt these before reading the
[solutions](./04-gpr-roads-concrete-solutions.md). The lesson is
[04 GPR for Pavements, Concrete and Infrastructure Inspection](../04-gpr-roads-concrete.md).
All models and data in this module are **SYNTHETIC**: the thicknesses,
permittivities, cover depths and pick errors are teaching values. The only
non-chosen numbers are physical constants ($c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$\varepsilon_{\mathrm{air}} = 1$).

## ★ Foundational

**★1.** A metal plate calibration gives a surface reflection of $R_s = -0.42$;
the layer/base reflection is picked at $1.20\ \mathrm{ns}$. Compute the layer
permittivity, the speed, and the thickness in millimetres. State the units at each
step.

**★2.** For asphalt of $\varepsilon_r = 4.5$ surveyed at $1.5\ \mathrm{GHz}$,
compute the speed, the wavelength, the quarter-wavelength limit and the two-way
time of a $15\ \mathrm{mm}$ layer. State, with a reason, whether the $15\
\mathrm{mm}$ layer can be measured as two separate echoes.

**★3.** A $50\ \mathrm{mm}$ asphalt layer with $\varepsilon_r = 4.5$. Compute the
two-way time of the primary, the two-way time of the layer multiple, and the
apparent depth the multiple would be reported at if it were mistaken for a
primary.

## ★★ Applied

**★★4.** The demonstration's slab table shows that at $h = 20\ \mathrm{mm}$ the
p2p response is $0.3165$ for a wet base and $0.4441$ for a dry base, against an
asymptotic value of $0.3592$. Convert each into the permittivity that the metal
plate formula would infer if the layer were assumed to be thick, and state which
one would look like a plausible calibration error and which one would look like a
different material.

**★★5.** A rebar grid in a deck of $\varepsilon_r = 6.0$ has $150\ \mathrm{mm}$
bar spacing and $60\ \mathrm{mm}$ cover, with a $0.02\ \mathrm{ns}$ pick error and
a fit aperture of $\pm0.30\ \mathrm{m}$. Using the demonstration's Monte Carlo
result, decompose the $1.5\ \mathrm{mm}$ cover uncertainty into picking and
velocity terms, and state which is larger.

**★★6.** The same deck is surveyed after rain, when the surface concrete has
$\varepsilon_r = 8.0$ to a depth of $100\ \mathrm{mm}$. Compute the apex time a
$60\ \mathrm{mm}$ bar would produce in that wet layer, and the cover depth an
analyst would report if they used the dry permittivity of $6.0$. State the
direction and size of the error.

## ★★★ Research-oriented

**★★★7.** You must certify a $50\ \mathrm{mm}$ asphalt layer to
$\pm 3\ \mathrm{mm}$. Construct the error budget: the permittivity term (how
accurately must the plate calibration be read?), the timing term (how accurately
must the pick be made?), and the model term (what does a $5\ \mathrm{mm}$ tack
coat beneath the layer do?). Decide which term sets the specification, and state
the frequency you would choose. A specification that could not be executed is a
failed answer.

**★★★8.** Section 3.3 derives the exact three-layer response and shows that one
amplitude can belong to several thicknesses. For a slab of unknown thickness on a
wet base, describe a *measurement procedure* (not an assumption) that resolves
the ambiguity, and state the thickness range over which it works. Justify each
element with a formula or a number from the lesson.

**★★★9.** The metal plate calibration assumes the antenna coupling is identical on
the plate and on the surface. Design a quality-control procedure that detects a
change in coupling during a survey without a plate, and state the amplitude change
you could detect with a stated confidence.
