# Exercises — 06-09-04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM

Attempt these before reading the
[solutions](./04-migration-imaging-solutions.md). The lesson is
[04 Migration and Imaging](../04-migration-imaging.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A point diffractor is at $(x,z) = (0,1000)\ \mathrm{m}$ in a medium with
$v = 2500\ \mathrm{m\,s^{-1}}$. Compute its apex time and its diffraction time at
$x = 500\ \mathrm{m}$.

**★2.** The demonstration's diffractor is at $(0,800)\ \mathrm{m}$ with
$v = 2000\ \mathrm{m\,s^{-1}}$. Verify the printed apex time of $0.8000\
\mathrm{s}$ and state the unit bookkeeping.

## ★★ Applied

**★★3.** Two point diffractors are imaged in one section. Explain, using the
linearity of the diffraction sum, why their migrated images add without
interference, and state the one situation in which they *would* interfere.

**★★4.** Using the demonstration's focus table (peak amplitudes $12.221$ at
$v_{\text{mig}}/v_{\text{true}} = 0.80$, $25.309$ at $0.95$, $89.954$ at $1.00$,
$28.780$ at $1.05$), estimate the velocity ratio at which the peak amplitude
falls to $50\%$ of its correct value on each side, stating your interpolation.

**★★5.** The demonstration's migrated peak depth is $780$, $760$, $780$, $800$,
$820$, $800$, $680\ \mathrm{m}$ for ratios $0.80$, $0.90$, $0.95$, $1.00$,
$1.05$, $1.10$, $1.20$. Compute the depth error in metres and as a percentage of
the true $800\ \mathrm{m}$, and state which ratios are consistent with the
true depth to within the migration grid.

## ★★★ Research-oriented

**★★★6.** Design a migration-velocity scan that recovers velocity to $5\%$ using
only image focus. State the trial velocities, the number of diffraction sums per
trial in terms of the image grid, the total cost, and the stopping criterion.
Use the demonstration's grid ($71\times81$ image cells, $121$ traces,
$700$ samples) for the arithmetic.

**★★★7.** The demonstration shows that a $20\%$ velocity error moves the image
peak by $-120\ \mathrm{m}$ in depth. Derive the expected depth shift for a
uniform velocity error of $\epsilon$ (as a fraction) for a *constant-velocity*
Kirchhoff map applied to a point at depth $z_0$, and compare with the measured
$-120\ \mathrm{m}$ at $\epsilon = +0.20$. State why the measured shift is
smaller and opposite in sign to the naive prediction.
