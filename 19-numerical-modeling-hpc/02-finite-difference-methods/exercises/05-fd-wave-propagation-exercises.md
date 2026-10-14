# Exercises — 19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation

Attempt these before reading the
[solutions](./05-fd-wave-propagation-solutions.md). The lesson is
[05 Wave Propagation](../05-fd-wave-propagation.md). All models are
**SYNTHETIC**. Numbers printed by
`../code/fd_wave_propagation_demo.py` may be quoted directly.

## ★ Foundational

**★1.** Write the fourth-order Laplacian stencil and its symbol
$S(k_xh,k_yh)$ for the two-dimensional case.

**★2.** Write the discrete dispersion relation of the fourth-order leapfrog
scheme and state what it reduces to for small $kh$.

**★3.** State why the phase speed below four points per wavelength cannot be
trusted, using the measured table.

## ★★ Applied

**★★4.** Compute the exact von Neumann limit of the 2-D fourth-order scheme from
$S_{\max}$ and compare with the five-point scheme's $1/\sqrt2$. State the
practical consequence for a time step copied from a second-order code.

**★★5.** An interface has $\rho_1 = 2000$, $c_1 = 2500$, $\rho_2 = 2200$,
$c_2 = 3200$ (SI units). Compute $Z_1$, $Z_2$, $R$ and $T$. Then state what
measured $R$ a scheme at 8 cells per wavelength would give, using the
demonstration's proportional error.

**★★6.** A 2-D model runs at 10 points per wavelength. Using the measured
anisotropy, estimate the arrival-time error between two receivers 3 km apart on
the diagonal relative to two on the axis, for $c = 3000\ \mathrm{m\,s^{-1}}$.

## ★★★ Research-oriented

**★★★7.** Design a complete verification suite for a 3-D elastic staggered
solver: list the four experiments, the exact (analytic) reference each is
compared with, the acceptance criterion, and which implementation error each
would catch. Order them so that a failure is localised as early as possible.

**★★★8.** A wavefield is migrated with the fourth-order scheme at eight points
per wavelength. A colleague observes an apparent dip of $2\,\%$ in a
reflector's moveout and interprets it structurally. Assess the claim using the
measured phase-speed errors on the axis and the diagonal, state what additional
measurement would settle it, and describe what the numerical explanation would
look like in the migrated image.
