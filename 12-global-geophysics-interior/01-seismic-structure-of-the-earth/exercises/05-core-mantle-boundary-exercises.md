# Exercises — 12-01-05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite

Attempt these before reading the
[solutions](./05-core-mantle-boundary-solutions.md). The lesson is
[05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](../05-core-mantle-boundary.md).
All models and data are **SYNTHETIC** teaching values.

Useful relations: $R = (Z_2-Z_1)/(Z_2+Z_1)$ with $Z = \rho v$;
$\delta t = 2h\left(1/v_s' - 1/v_s\right)$ with $v_s' = v_s(1-\delta)$;
$\Delta P = C - \gamma(T_\text{CMB} - T_\text{ref})$;
$h_{D''} = \Delta P/(\rho g)$;
$T_\text{thresh} = T_\text{ref} + C/\gamma$.

Reference values used throughout (from lesson 01, SYNTHETIC):
mantle at the CMB $\rho = 5.57\ \mathrm{g\,cm^{-3}}$, $v_p = 13.72$,
$v_s = 7.26\ \mathrm{km\,s^{-1}}$; outer core $\rho = 9.90$, $v_p = 8.06$,
$v_s = 0\ \mathrm{km\,s^{-1}}$; $\rho g = 59.38\ \mathrm{MPa\,km^{-1}}$.

## ★ Foundational

**★1.** Compute the normal-incidence reflection coefficient at the CMB for (a) SH
waves and (b) P waves, using the reference values above. Then recompute (b) for an
outer core of density $10.50\ \mathrm{g\,cm^{-3}}$ and state whether the boundary
becomes more or less transparent to P.

**★2.** A ULVZ is 18 km thick with $v_s$ reduced by 15 %. Compute $v_s'$ and the
postcursor delay, and state the units of each factor.

**★3.** A post-perovskite transition lies 12.0 GPa above the CMB pressure at the
reference temperature. Compute the D'' thickness in kilometres.

## ★★ Applied

**★★4.** A measured ScS postcursor delay is 1.800 s. Build the $(h,\delta)$ family
for $h$ = 10, 20, 30 and 40 km, reporting $\delta$ in per cent and $v_s'$. State
which members of the family a mineral physicist would reject and why.

**★★5.** For $C = 12.0\ \mathrm{GPa}$ and $T_\text{ref} = 2600\ \mathrm{K}$,
compute the shut-off temperature for $\gamma = 7$, 8 and 9
$\mathrm{MPa\,K^{-1}}$. State the range in kelvin implied by that plausible range
of $\gamma$.

**★★6.** A reflection from the top of D'' arrives 12.0 s before the CMB reflection.
Compute the D'' thickness for $v_s = 7.26\ \mathrm{km\,s^{-1}}$ and for velocities
2 % and 3 % lower, and state how the answer should be reported.

**★★7.** A ULVZ is detected with a delay of 0.90 s. Its thickness is independently
bounded by waveform modelling to be less than 12 km. What does that bound imply
about $\delta$ and about the density contrast? Use the demonstration's
parametrisation.

## ★★★ Research-oriented

**★★★8.** The demonstration reports an energy ratio of 1.000 to within 0.1 % for a
lossless stack. Modify the physics: add attenuation by making the layer velocity
complex, $v \to v(1 + i/2Q)$, and predict (with arithmetic) the energy ratio for
$Q = 100$ over two-way times of 3 s and 12 s. State what the measurement would
constrain if both the delay and the energy ratio were measured.

**★★★9.** Derive $\mathrm{d}T_\text{thresh}/\mathrm{d}\gamma$ and evaluate it at
$\gamma = 8\ \mathrm{MPa\,K^{-1}}$, $C = 10\ \mathrm{GPa}$. Then design the
observational test that would most tightly constrain $\gamma$: state what is
measured, what else must be known, and quantify the residual ambiguity.

**★★★10.** Design an experiment to measure a ULVZ thickness *and* its velocity drop
separately. State the observables, the frequency band, the assumed density–velocity
relation you must still adopt, and the predicted resolution in kilometres.
