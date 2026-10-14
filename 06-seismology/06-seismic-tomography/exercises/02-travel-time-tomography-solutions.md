# Solutions — 06-06-02 Travel-Time Tomography: Parametrisation and Inversion

Exercises:
[02-travel-time-tomography-exercises.md](02-travel-time-tomography-exercises.md).

## ★ Foundational

**1.** $\mathrm{d}x = 16000/16 = 1000\ \mathrm{m}$,
$\mathrm{d}z = 5500/12 = 458.3\ \mathrm{m}$; parameters
$16\times12 = 192$. The parametrisation forbids: a discontinuity or a gradient
*inside* a cell, any feature narrower than about 1 km horizontally or 458 m
vertically, and (with identity damping) any cell whose value is not demanded by
the data.

**2.** $140/192 = 0.73$. The ratio says only that the problem *looks*
underdetermined. The measured rank on the equivalent $16\times12$ cross-hole
problem was 136 of 140 (cells basis) and 140 of 140 (nodes basis), so the ratio
and the rank disagree: rank is a property of the geometry and of the basis, not
of the counts.

**3.** $\sqrt{N}\sigma_{\text{eff}} = 5.561\times10^{-2}$ with $N = 140$ gives
$\sigma_{\text{eff}} = 5.561\times10^{-2}/\sqrt{140} =
4.70\times10^{-3}\ \mathrm{s} = \mathbf{4.70\ ms}$, statistically
indistinguishable from the stated 5 ms — which is the intended result, since the
damping was chosen to sit exactly at the discrepancy level.

## ★★ Applied

**4.** From the table: 5 iterations give misfit $2.1686\times10^{-3}$ s and a
distance of $9.52\times10^{-4}$ from the direct solution; 10 give
$1.4846\times10^{-3}$ and $1.65\times10^{-4}$; 20 give
$1.4694\times10^{-3}$ and $6.30\times10^{-6}$. Ten iterations already reach
within 1.65 per cent of the direct solution's model norm scale
($\sqrt{n}$-normalised distance $1.65\times10^{-4}$ against a model rms of order
$10^{-2}$), so a sensible stopping rule is "stop when the misfit has stopped
decreasing by more than 1 per cent per iteration" — with the iteration count
reported, because at 1 hour per matrix-vector product the stopping rule *is* the
model.

**5.** For the $8\times6$ grid: total $1.6292\times10^{-2}$, row-space
$7.1711\times10^{-3}$, null fraction 0.519 (so the null part contributes
$0.519\times$ the truth's rms). The truth's rms over that grid is
$\sqrt{(\text{total})^2 - (\text{row})^2}$ if the decomposition were orthogonal,
giving $\sqrt{1.6292^2 - 0.7171^2}\times10^{-2} = 1.463\times10^{-2}$, i.e. a
null fraction of $1.463/1.629 = \mathbf{0.898}$ — which does *not* match the
reported 0.519, because the reported null fraction is computed on the *truth*
while the error includes the noise-driven part of the observable components. The
quantitative check that does work is that the row-space error is much smaller
than the total ($7.2\times10^{-3}$ against $1.63\times10^{-2}$), i.e. most of
the error is unreachable rather than badly estimated.

**6.** A Laplacian operator has a larger null space than a first-difference one:
in addition to constants it does not penalise any *linear ramp* in $x$ and $z$
(each row of the second-difference stencil sums to zero, and its first moment is
constant). With a pure Laplacian and no identity term, the plane components of
the model are determined by the data alone; in a limited-angle geometry those
components are among the least constrained, so the mean and the tilt of the
image become noise-driven. The demonstration's fix — stack 5 per cent of the
identity — is exactly a way of making the operator full-rank.

## ★★★ Research-oriented

**7.** A quadratic fit to the three points: $T(d)-T(0) = k d^2$ gives
$k = 45.101/1^2 = 45.1$, $11.315/0.25 = 45.3$, $2.595/0.0625 = 41.5$ — so
$k \approx 45\ \mathrm{ms\,km^{-2}}$. For $d = 2$ km the prediction is
$45.1\times4 = \mathbf{180\ ms}$. The assumption is that the quartic term stays
negligible: the three points are consistent with $k$ constant to about 4 per
cent, which bounds the quartic contribution at the 1 km point to roughly 1 ms;
at 2 km that contribution is 16 times larger (16 ms), so the prediction is good
to about 10 per cent, not 1 per cent.

**8.** The residual falls by 1400 because the dominant error in the first
linearised step is the *parametrisation* nonlinearity — the difference between
$1/(1+p)$ and $1-p$ — and re-linearising about the updated model removes it
almost completely; the second step is a Newton step on a smooth, nearly
quadratic function, so the residual drops quadratically. The model error against
the recoverable part barely moves ($7.77\times10^{-4} \to 7.18\times10^{-4}$,
7.6 per cent) because that error was already dominated by the damping bias, not
by the parametrisation: with $\lambda = 10^{-3}\lVert G\rVert$ the estimate is
shrunk towards zero and the bias that remains is not reducible by iterating. A
third iteration changes neither number materially (the residual reaches the
numerical floor at $5.9\times10^{-8}$ s); what would change them is different
damping, not more iterations.
