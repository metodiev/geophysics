# Exercises — 12-02-03 Ab Initio Mineral Physics and Elastic Constants

Attempt these before reading the
[solutions](./03-ab-initio-mineral-physics-solutions.md). The lesson is
[03 Ab Initio Mineral Physics and Elastic Constants](../03-ab-initio-mineral-physics.md).
All tensors are **SYNTHETIC** teaching values.

Useful relations: $K_V = [C_{11}+C_{22}+C_{33}+2(C_{12}+C_{13}+C_{23})]/9$;
$G_V = [C_{11}+C_{22}+C_{33}-(C_{12}+C_{13}+C_{23})+3(C_{44}+C_{55}+C_{66})]/15$;
Reuss values from the compliances $S = C^{-1}$;
$M_{ik} = C_{ijkl}n_jn_l$ with eigenvalues $\rho v^{2}$;
$A = 2C_{44}/(C_{11}-C_{12})$;
$\delta t = L\left(1/v_\text{slow} - 1/v_\text{fast}\right)$.

## ★ Foundational

**★1.** For the cubic tensor $C_{11} = 280$, $C_{12} = 110$, $C_{44} = 130$ GPa,
compute $K_V$, $G_V$ and the Zener factor $A$. State whether the crystal is close to
elastically isotropic.

**★2.** For a hexagonal tensor with $C_{11} = 300$, $C_{12} = 120$, $C_{13} = 100$,
$C_{33} = 320$, $C_{44} = 90$ GPa, compute $C_{66}$ and the Voigt bulk modulus.

**★3.** A path of 300 km passes through a medium with shear velocities 4.75 and
4.70 km s$^{-1}$. Compute the splitting time and the shear anisotropy in per cent.

## ★★ Applied

**★★4.** For the tensor of ★1 with $\rho = 4.10\ \mathrm{g\,cm^{-3}}$, write down the
Christoffel matrix along $[110]$ explicitly, solve it by hand, and report the three
speeds. Compare the S splitting with the $[100]$ direction and explain the difference
in terms of symmetry.

**★★5.** For the tensor of ★1, compute $G_R$ from the compliances and compare with
$G_V$. State the fractional difference and which value you would use for an
isotropic-equivalent velocity, with a justification.

**★★6.** A cubic tensor has $C_{44} = 130$ GPa but a computed structure gives
$C_{11} - C_{12} = -5$ GPa. State which Born criterion is violated, what the strain
energy does, and what the physical conclusion is.

**★★7.** A seismic study measures a P anisotropy of 1.2 % in a region where the
relevant crystal has a single-crystal P anisotropy of 6 %. Compute the implied
alignment fraction and state the assumption in the calculation.

## ★★★ Research-oriented

**★★★8.** Design a computation-to-seismology workflow for a candidate lower-mantle
phase. List, in order, every validation step from an ab initio result to a predicted
seismic anisotropy, and state what each step would catch. Include at least one check
that uses no seismological data.

**★★★9.** For a hexagonal crystal, write $P = C_{11}+C_{12}$, $Q = C_{13}$,
$R = C_{33}$ and put $K_V - K_R$ over a common denominator. Show that
$K_V = K_R$ **if and only if** $P = R + Q$, and evaluate $K_V - K_R$ for the tensor of
★2 (where the condition happens to hold) and for $C_{11} = 290$, $C_{12} = 230$,
$C_{13} = 110$, $C_{33} = 280$, $C_{44} = 95$ GPa. State why no corresponding equality
can hold for $G$ at any symmetry lower than isotropic.

**★★★10.** A candidate inner-core phase has a single-crystal S anisotropy of 20 %.
Using the observed small S splitting of the inner core, estimate the maximum
alignment consistent with a 2500 km path and a 2 s splitting. Then state what
additional observation would break the crystal-anisotropy/alignment degeneracy.
