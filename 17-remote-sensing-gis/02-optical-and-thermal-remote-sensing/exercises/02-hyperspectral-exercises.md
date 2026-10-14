# Exercises — 17-02-02 Hyperspectral Sensing and Spectral Unmixing

Attempt these before reading the
[solutions](./02-hyperspectral-solutions.md). The lesson is
[02 Hyperspectral Sensing and Spectral Unmixing](../02-hyperspectral.md).
All libraries and spectra are **SYNTHETIC** teaching values.

Example library used below (two bands, two endmembers):
$\mathbf{e}_1 = (0.10, 0.30)$, $\mathbf{e}_2 = (0.40, 0.50)$, so
$\mathbf{G} = \mathbf{M}^{\!\top}\mathbf{M} = \begin{pmatrix}0.100 & 0.190\\
0.190 & 0.410\end{pmatrix}$ and $\mathbf{G}^{-1} = \begin{pmatrix}83.673 &
-38.776\\ -38.776 & 20.408\end{pmatrix}$.

## ★ Foundational

**★1.** Unmix $\mathbf{x} = (0.25, 0.40)$ with the example library. Is the
answer admissible on the simplex? Show the arithmetic.

**★2.** Compute $\kappa(\mathbf{G})$ and $\kappa(\mathbf{M})$ for the example
library and verify the relation between them.

**★3.** State the two constraints that define the probability simplex and say
which of them a closed-form solution can enforce and which cannot.

## ★★ Applied

**★★4.** Derive the sum-to-one constrained solution by endmember reduction for
the three-endmember library $\mathbf{e}_1 = (0.10, 0.30, 0.20)$,
$\mathbf{e}_2 = (0.40, 0.50, 0.60)$, $\mathbf{e}_3 = (0.20, 0.40, 0.80)$ and the
pixel $\mathbf{x} = (0.27, 0.42, 0.52)$. Verify that the abundances sum to
exactly one.

**★★5.** Using the example library and $\sigma = 0.005$, compute the abundance
standard deviations and state which endmember's fraction is measurably worse.
How many extra pixels would be needed to bring the worse one to the precision of
the better one?

**★★6.** For the example library, describe the abundance direction that the data
cannot constrain. Compute the change in the pixel spectrum produced by trading
$0.10$ of abundance between the two endmembers, and compare it with unit band
noise of $\sigma = 0.002$.

**★★7.** A library is built with 6 endmembers where the sixth is $99\%$
endmember 4 and $1\%$ endmember 5. The demonstration measured
$\kappa(\mathbf{G}) = 6.7\times10^{16}$ against $5328.5$ for the 5-endmember
library. Explain in two sentences why adding a physically sensible endmember can
make the inversion *worse*, and state the diagnostic you would report.

## ★★★ Research-oriented

**★★★8.** Design an experiment to measure the boundary bias of FCLS as a
function of band noise $\sigma$ for a true abundance of $0.02$. State the metric,
the prediction, and the false conclusion the experiment is designed to avoid. A
specification that could not be executed is a failed answer.

**★★★9.** A scene contains one mineral whose spectral library entry varies by
$\pm8\%$ in shape across the scene. Specify a multiple-endmember formulation
(algebra and solver), state how you would validate it without ground truth, and
state the residual diagnostic that would reveal whether the variability is
actually endmember variability or an error elsewhere in the processing chain.
