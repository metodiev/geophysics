# Exercises — 10-03-05 Planetary GPR: MARSIS, SHARAD and Lunar Radar

Attempt these before reading the
[solutions](./05-gpr-planetary-solutions.md). The lesson is
[05 Planetary GPR: MARSIS, SHARAD and Lunar Radar](../05-gpr-planetary.md).
All models and data in this module are **SYNTHETIC**: the altitudes, bandwidths,
target depths, ionospheric densities and permittivities are teaching values, and
no measured value from any mission is used. The only non-chosen numbers are
physical constants ($c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$e = 1.602176634\times10^{-19}\ \mathrm{C}$,
$\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$,
$m_e = 9.1093837015\times10^{-31}\ \mathrm{kg}$, $\varepsilon_{\mathrm{ice}} = 3.17$,
$\varepsilon_{\mathrm{water}} = 80.1$).

## ★ Foundational

**★1.** A sounder has a bandwidth of $5\ \mathrm{MHz}$. Compute the two-way time
resolution and the range resolution in vacuum and in ice
($\varepsilon_r = 3.17$). State the units.

**★2.** At an altitude of $300\ \mathrm{km}$, compute the first Fresnel zone radius
at $5\ \mathrm{MHz}$ and at $20\ \mathrm{MHz}$. Give the ratio and derive the
frequency dependence from the formula.

**★3.** A candidate subsurface interface is $50\ \mathrm{m}$ deep in ice
($\varepsilon_r = 3.17$) below a sounder at $300\ \mathrm{km}$. Compute the
off-nadir surface distance whose echo has the same delay, and state in one
sentence why this number is the reason a delay is not proof of depth.

## ★★ Applied

**★★4.** A two-way time of $30.0\ \mu$s is measured to an interface, together
with an attenuation-corrected echo amplitude. Model A takes
$\varepsilon_r = 3.17$ and a one-way absorption of $0.005\ \mathrm{dB\,m^{-1}}$;
model B takes $\varepsilon_r = 4.00$. Compute both depths, the depth difference in
metres and per cent, and the absorption that model B requires to reproduce the
same amplitude.

**★★5.** For a total electron content of $5\times10^{15}\ \mathrm{m^{-2}}$ and a
$20\ \mathrm{MHz}$ carrier, compute the excess path (round-trip range bias) and
the differential delay across a band from $15$ to $25\ \mathrm{MHz}$. Compare the
differential delay with the range resolution of a $10\ \mathrm{MHz}$ bandwidth in
ice and comment.

**★★6.** A target has a one-way absorption of $0.02\ \mathrm{dB\,m^{-1}}$. Compute
the depth at which a $60\ \mathrm{dB}$ two-way budget is spent. Then compute the
depth below which clutter is unavoidable within a $500\ \mathrm{m}$ along-track
window for $h = 300\ \mathrm{km}$ and $\varepsilon_r = 3.17$. State which limit
binds.

## ★★★ Research-oriented

**★★★7.** Design a discrimination test between a genuine subsurface echo at
$200\ \mathrm{m}$ in ice and a surface-clutter echo, under a SYNTHETIC
$h = 300\ \mathrm{km}$. Specify the observable, the number of independent
along-track samples you require and why, the clutter distance implied by the
target depth, and the two ways the test could fail. A specification that could not
be executed is a failed answer.

**★★★8.** Derive the dispersion constant $40.3\ \mathrm{m^3\,s^{-2}}$ from the
plasma-frequency constant $8.98$, and show that the two expressions for the
excess path used in the lesson agree to better than $0.1\%$ for
$f_p/f = 0.142$. Compute the next term of the group-index expansion and state
whether it is significant against a $15\ \mathrm{m}$ range resolution.

**★★★9.** A candidate layer is reported with a thickness of $30\ \mathrm{m}$ in a
cold polar deposit, from a $10\ \mathrm{MHz}$ bandwidth sounding. Assess the
claim: compute the resolution, state what the layer detection actually rests on,
and say what measurement would raise the claim from a model inference to a
measurement.
