# Exercises — 06-01-08 Wave Propagation in Anisotropic Media

Attempt these before reading the
[solutions](./08-anisotropic-propagation-solutions.md). The lesson is
[08 Wave Propagation in Anisotropic Media](../08-anisotropic-propagation.md); all
numbers are printed by
[`../code/anisotropic_propagation_demo.py`](../code/anisotropic_propagation_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For $\alpha_0 = 4000\ \mathrm{m\,s^{-1}}$,
$\beta_0 = 2400\ \mathrm{m\,s^{-1}}$, $\rho = 2600\ \mathrm{kg\,m^{-3}}$ compute
$C_{33}$ and $C_{44}$ in Pa and in GPa, and verify the units by dimensional
analysis.

**★2.** With $\varepsilon = \gamma = 0.20$, compute $C_{11}$, $C_{66}$ and
$C_{12}$, and state what value of $C_{11}-C_{33}$ an isotropic medium with the
same $\alpha_0$ would have.

**★3.** Write the Christoffel tensor $\Gamma_{ik} = C_{ijkl}n_jn_l$ for a VTI
medium with $\mathbf n = (0,0,1)$, and read off the three eigenvalues as speeds.
State which branch is degenerate.

## ★★ Applied

**★★4.** Compute $C_{13}$ from
$C_{13} = \sqrt{2C_{33}(C_{33}-C_{44})\delta + (C_{33}-C_{44})^2} - C_{44}$ for
$\delta = 0.15$, and check that feeding the resulting tensor back into
$\delta = [(C_{13}+C_{44})^2 - (C_{33}-C_{44})^2]/[2C_{33}(C_{33}-C_{44})]$ returns
$0.15$.

**★★5.** Using the exact formula $v_{SH}(\theta) =
\beta_0\sqrt{1+2\gamma\sin^2\theta}$, compute $v_{SH}$ at
$\theta = 0^\circ, 45^\circ, 90^\circ$ for $\gamma = 0.20$, and compare with the
demonstration's table values $2400.0000$, $2629.0683$ and $2839.7183\
\mathrm{m\,s^{-1}}$.

**★★6.** Evaluate the Thomsen approximations for $v_{qP}$ and $v_{qSV}$ at
$\theta = 45^\circ$ and compare with the exact values $4346.0321$ and
$2464.1439\ \mathrm{m\,s^{-1}}$. State the percentage error in each and comment on
whether the qSV approximation or the qP approximation is the better one at this
angle.

## ★★★ Research-oriented

**★★★7.** Derive $\mathbf v_g = v\hat{\mathbf n} +
(\mathrm{d}v/\mathrm{d}\theta)\hat{\boldsymbol\theta}$ from
$\mathbf v_g = \partial\omega/\partial\mathbf k$ for a phase speed that depends
only on the angle $\theta$ from the symmetry axis, and state what the formula
predicts for the ray–phase split on the axis and in the plane perpendicular to it.

**★★★8.** The demonstration measures a shear-wave splitting of
$439.72\ \mathrm{m\,s^{-1}}$ for a horizontal ray but exactly zero for a vertical
ray, in a medium with $\gamma = 0.20$ throughout. Design an experiment that
determines the *minimum* number of distinct ray directions needed to constrain
both $\gamma$ and the orientation of the symmetry axis, assuming the ray
azimuths are known. State what each measurement adds.

**★★★9.** The weak-anisotropy error for $v_{qP}$ grows to $1.1265\%$ at
$\theta = 75^\circ$ while the qSV error peaks at $45^\circ$ and then falls. Explain
the different angular behaviour of the two truncation errors, and state what that
implies for choosing a fit band when inverting for $\varepsilon$ and $\delta$.
