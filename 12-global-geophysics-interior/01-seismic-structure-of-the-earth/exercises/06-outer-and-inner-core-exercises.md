# Exercises — 12-01-06 Outer Core, Inner Core Anisotropy and Rotation

Attempt these before reading the
[solutions](./06-outer-and-inner-core-solutions.md). The lesson is
[06 Outer Core, Inner Core Anisotropy and Rotation](../06-outer-and-inner-core.md).
All models and data are **SYNTHETIC** teaching values.

Useful relations: for a layer with $v$ linear in $r$,
$\int \mathrm{d}r/v = L\ln(v_2/v_1)/(v_2-v_1)$;
$G = \rho v_s^2$; $K = \rho\left(v_p^2-\tfrac43 v_s^2\right)$;
$\nu = (v_p^2-2v_s^2)/[2(v_p^2-v_s^2)]$;
$R = (Z_2-Z_1)/(Z_2+Z_1)$ with $Z=\rho v$;
$\delta t = -A\cos^2\xi\int A_\text{taper}(r)\,\mathrm{d}l/v$;
$\delta t_S = 2B T_s$; and a rotation rate
$\omega = \dot{\delta t}\big/\left|\mathrm{d}(\delta t)/\mathrm{d}\phi\right|$.

## ★ Foundational

**★1.** An outer core has $v_p$ linear in radius from 8.20 km s$^{-1}$ at the CMB
to 10.40 km s$^{-1}$ at the ICB, over 2258.5 km. Compute (a) the exact vertical
travel time using the logarithmic integral, (b) the estimate from the arithmetic
mean of the endpoints, and (c) the estimate from the harmonic mean. State which is
closest to the truth and why none is exact.

**★2.** An inner core has $\rho = 12.90\ \mathrm{g\,cm^{-3}}$,
$v_p = 11.15$ and $v_s = 3.55\ \mathrm{km\,s^{-1}}$. Compute $G$, $K$, the ratio
$K/G$ and Poisson's ratio, and say in one sentence what the result implies about the
material.

**★3.** Compute the ICB reflection coefficient for P waves given
$\rho_\text{oc} = 12.17$, $v_{p,\text{oc}} = 10.29$,
$\rho_\text{ic} = 12.76$, $v_{p,\text{ic}} = 11.03$. State the units of the
impedances you form and why they cancel.

## ★★ Applied

**★★4.** A ray has an inner-core leg time of 180.0 s with a taper-weighted mean of
0.75, and the axial–equatorial differential is $-3.375\ \mathrm{s}$. Compute the P
anisotropy $A$.

**★★5.** The two-way S travel time through the inner core is 681.578 s. (a) Compute
the splitting for $B = 0.5\ \%$. (b) Compute the $B$ implied by a measured splitting
of 3.0 s. (c) If a P anisotropy of 2 % is measured on the same paths, compute the
ratio of the P to S anisotropy and explain why that ratio is the physically
informative quantity.

**★★6.** A study measures a secular travel-time change of 0.030 s/yr and uses the
demonstration's sensitivity of $-0.01278$ s per degree of rotation. Compute the
implied rotation rate for heterogeneity amplitudes of 0.3 % and 0.6 %, and state the
one-parameter family that the data actually determine.

**★★7.** A measured splitting of 1.5 s is attributed to anisotropy in a 200 km thick
layer at the top of the inner core rather than to the whole inner core. Compute the
implied $B$ in the layer, using $v_s = 3.52\ \mathrm{km\,s^{-1}}$, and explain how
its size changes the interpretation.

## ★★★ Research-oriented

**★★★8.** Derive $\langle\cos^2\xi\rangle = 1/3$ for an isotropic distribution of ray
directions, and show how the *reported* anisotropy of a data set changes with its
direction coverage. State two concrete acquisition strategies that would bias a
study and the size of the bias in each.

**★★★9.** The first-order differential formula treats the change in the ray path as
a second-order effect (Fermat's principle), but the *turning radius* changes by
about $A\,r_{tp}$ when the anisotropy is switched on. Estimate the change in the
inner-core leg time caused by that geometry change for a shallow-penetrating path,
and state the condition under which the first-order formula remains adequate.

**★★★10.** Design a data set and analysis that would separate inner-core rotation
from inner-core heterogeneity and from anisotropy. State the observables, the
azimuthal and temporal coverage, the forward model, and a quantitative prediction of
the resolution you expect in the rotation rate.
