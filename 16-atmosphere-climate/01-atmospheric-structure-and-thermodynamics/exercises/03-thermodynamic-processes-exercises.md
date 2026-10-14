# Exercises — 16-01-03 Adiabatic Processes, Lapse Rates and Stability

Attempt these before reading the
[solutions](./03-thermodynamic-processes-solutions.md). The lesson is
[03 Adiabatic Processes, Lapse Rates and Stability](../03-thermodynamic-processes.md).
Use $g = 9.80665\ \mathrm{m\,s^{-2}}$,
$R_d = 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and
$c_p = 1004.64\ \mathrm{J\,kg^{-1}\,K^{-1}}$. All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the dry adiabatic lapse rate $\Gamma_d = g/c_p$ in
$\mathrm{K\,km^{-1}}$, and the exponent $\kappa = R_d/c_p$. Then compute the
potential temperature of air at $T = 300\ \mathrm{K}$ and $p = 900\ \mathrm{hPa}$.

**★2.** For an environment with $\Gamma = 7.0\ \mathrm{K\,km^{-1}}$ at
$T = 285\ \mathrm{K}$, compute $\mathrm{d}\theta/\mathrm{d}z$ using
$\mathrm{d}\theta/\mathrm{d}z = (\theta/T)(\Gamma_d - \Gamma)$ with
$\theta = 300\ \mathrm{K}$, and then compute $N^2 = (g/T)(\Gamma_d - \Gamma)$.
Classify the stratification.

**★3.** Compute the buoyancy period $2\pi/N$ for the environment of ★2 at
$T = 285\ \mathrm{K}$ and again at $T = 255\ \mathrm{K}$. State in one sentence
why the two differ when $\Gamma$ is the same.

**★4.** An isothermal layer has $\Gamma = 0$. Compute $N$ and the oscillation
period at $T = 255\ \mathrm{K}$, and state whether the layer is stable.

## ★★ Applied

**★★5.** Derive $\mathrm{d}\theta/\mathrm{d}z = (\theta/T)(\Gamma_d-\Gamma)$ from
$\theta = T(p_0/p)^{R_d/c_p}$, hydrostatic balance and the ideal-gas law, showing
every step and stating where the hydrostatic assumption enters. Evaluate the
result for $\Gamma = 10\ \mathrm{K\,km^{-1}}$, $T = 280\ \mathrm{K}$,
$\theta = 300\ \mathrm{K}$, and say what the sign means.

**★★6.** A parcel at $p = 900\ \mathrm{hPa}$ has $T = 290\ \mathrm{K}$. It is
lifted dry-adiabatically to $p = 700\ \mathrm{hPa}$. Compute (a) its potential
temperature at the start, (b) its temperature at $700\ \mathrm{hPa}$, (c) the
temperature change, and (d) its buoyancy acceleration if the environment at
$700\ \mathrm{hPa}$ is at $280\ \mathrm{K}$. State whether the parcel continues
to rise and why the answer does not depend on the *path* through the
$900\text{–}700\ \mathrm{hPa}$ layer.

**★★7.** Compute the dry static energy $c_p T + gz$ for (a) air at the surface
with $T = 290\ \mathrm{K}$, $z = 0$, and (b) air at $z = 5400\ \mathrm{m}$ with
$T = 250\ \mathrm{K}$. State which is larger and what that implies about lifting
surface air to $5400\ \mathrm{m}$ without any heat input. Comment on whether the
comparison is physically meaningful if the two air masses are different.

**★★8.** A parcel's potential temperature is raised from $300\ \mathrm{K}$ to
$305\ \mathrm{K}$ by heating at a mean temperature of $280\ \mathrm{K}$. Compute
$\Delta s = c_p\ln(\theta_1/\theta_0)$ and compare it with $\Delta q/T$ for a
direct heat input of $2000\ \mathrm{J\,kg^{-1}}$ at $280\ \mathrm{K}$. Are the two
answers supposed to agree? Explain.

## ★★★ Research-oriented

**★★★9.** Design a numerical experiment that measures the buoyancy period as a
function of amplitude from $10\ \mathrm{m}$ to $2\ \mathrm{km}$ in the lesson's
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ environment. Specify the integration method,
the period estimator, the metric of nonlinearity, and the expected scaling of the
period shift with amplitude. State the amplitude at which you predict a $1\%$
period shift *before* running the experiment, and say what you would do if the
prediction failed.

**★★★10.** "The lapse rate of this layer is $6.5\ \mathrm{K\,km^{-1}}$" is not a
complete statement. Enumerate at least five choices that must be specified before
the number is reproducible (depth interval, vertical coordinate, layer-mean
convention, curve fitting versus endpoint difference, treatment of moisture), and
state for each whether it is definitional or physical. Then explain how a
stability diagnostic can change sign purely through a definitional choice.

**★★★11.** A sounding shows a lapse rate close to $\Gamma_d$ through
$2\ \mathrm{km}$, then a rapid decrease to about half that value above the
lifting condensation level. Design a procedure that locates the transition level
*from the data alone*, without assuming a moist-adiabat formula, and state
exactly what would be measured, what would be modelled, and what the largest
unresolved uncertainty in the transition height would be. You may not invent
saturated-adiabat constants; say what constant you would need and where it would
have to be measured.
