# Exercises — 10-03-03 GPR in Archaeology, Forensics and Buried Utilities

Attempt these before reading the
[solutions](./03-gpr-archaeology-forensics-solutions.md). The lesson is
[03 GPR in Archaeology, Forensics and Buried Utilities](../03-gpr-archaeology-forensics.md).
All models and data in this module are **SYNTHETIC**: the targets, depths,
permittivities and pick errors are teaching values. The only non-chosen numbers
are physical constants and standard material permittivities ($c =
0.299792458\ \mathrm{m\,ns^{-1}}$, $\varepsilon_{\mathrm{water}} = 80.1$,
$\varepsilon_{\mathrm{air}} = 1$).

## ★ Foundational

**★1.** A hyperbola has an apex time $t_0 = 24.0\ \mathrm{ns}$ and a time of
$33.6\ \mathrm{ns}$ at $x = 1.0\ \mathrm{m}$. Fit $t^2$ against $x^2$: compute the
slope, the velocity, the depth and the implied permittivity. State the units of
each.

**★2.** A host soil has $\varepsilon_r = 12.0$. Compute the reflection
coefficient (with sign) and the relative amplitude in dB for an air-filled void
and for a water-filled void at the same depth. State the two ways in which the
echoes differ and the one in which they do not.

**★3.** At $400\ \mathrm{MHz}$ in a medium of $\varepsilon_r = 12.0$, a reflector
lies at $1.20\ \mathrm{m}$. Compute the wavelength, the quarter-wavelength limit,
and the first Fresnel zone radius. State which of the last two is a resolution
statement and which is a detection statement.

## ★★ Applied

**★★4.** The lesson reports that reducing a hyperbola's aperture from
$\pm2.00\ \mathrm{m}$ to $\pm0.50\ \mathrm{m}$ (with $41$ traces and a
$0.20\ \mathrm{ns}$ pick error) raises the velocity uncertainty from $0.3\%$ to
$3.2\%$ and the depth uncertainty from $0.4\%$ to $3.3\%$, with the correlation
rising from $+0.948$ to $+0.999$. For a target at $1.50\ \mathrm{m}$, compute the
depth error interval that the short aperture implies at one standard deviation and
at two, and state whether the survey meets a $\pm0.10\ \mathrm{m}$ specification.

**★★5.** At $500\ \mathrm{MHz}$ in a soil of $\varepsilon_r = 9$, a $30\
\mathrm{mm}$ target returns $30\ \mathrm{dB}$ above the noise floor. Compute the
echo strength in dB above the noise for targets of $15\ \mathrm{mm}$ and $8\
\mathrm{mm}$, and state the largest detectable target size if the detection
threshold is $6\ \mathrm{dB}$ above the noise.

**★★6.** Using the migration table of the lesson, compute the loss of focus in
dB when the migration velocity is $20\%$ too low, and the depth that would be
reported for a target whose true depth is $1.50\ \mathrm{m}$. State which of the
two numbers a migration-focus velocity analysis could measure and which it could
not.

## ★★★ Research-oriented

**★★★7.** Design a utility-mapping procedure that reports a service depth to
$\pm0.15\ \mathrm{m}$ in a soil of $\varepsilon_r = 12$. Specify: the frequency,
the trace spacing, the velocity measurement (with its own uncertainty), the
aperture, how you will report a service that is not crossed at its apex, and the
assumption that would invalidate the result if it failed. A specification that
could not be executed is a failed answer.

**★★★8.** Show analytically that if the apex time $t_0$ is known exactly and the
fitted slope $m$ carries a small relative error $\epsilon$, then $v$ and $z$ each
carry the relative error $-\epsilon/2$. Then explain why the *measured*
correlation between the fitted $v$ and the fitted $z$ is $+0.999$ rather than
$-1$ or $0$, and why a longer aperture reduces it to $+0.948$.

**★★★9.** A forensic survey looks for a disturbed grave in a soil of
$\varepsilon_r = 9$. The disturbance changes the permittivity by $4\%$ and the
conductivity by a factor of two in a $1.0\ \mathrm{m} \times 0.6\ \mathrm{m}$
volume. Compute the reflection coefficient of the disturbance boundary, express
it in dB relative to a $0.30$ contrast, and state — with numbers — whether the
detectable signature is likely to be a reflection, an attenuation change, or a
disruption of the natural stratigraphy.
