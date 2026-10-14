# Exercises — 01-16-05 Ill-Posedness in the Sense of Hadamard

Attempt these **closed-book** before opening the
[solutions](./05-ill-posedness-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the gravity kernel of the lesson is
$K(s) = (z/\pi)/(s^2+z^2)$ with depth $z$, acting as
$d(x) = \int_0^1K(x-y)m(y)\,dy$ on $L^2(0,1)$; $\sigma_k$ are singular values in
decreasing order; the weighted model norm is $\sqrt{h\sum_im_i^2}$ on a grid with
spacing $h$. Report the residual **and** the model norm whenever an inversion is
discussed.

---

## ★ Foundational

**★1.** State Hadamard's three conditions. For each, name a geophysical problem
that fails it, and the remedy that addresses that specific failure. State which
condition regularisation does *not* repair.

---

**★2.** Show that $K(s) = (z/\pi)/(s^2+z^2)$ integrates to 1, and that its Fourier
transform is $\hat K(f) = e^{-2\pi z\lvert f\rvert}$. Hence compute the wavenumber
at which the operator attenuates a model component by a factor of $10^{-3}$ for
$z = 0.05$.

---

**★3.** Explain why a compact operator with infinite-dimensional range has an
unbounded inverse, and why its range is not closed. Relate each statement to one
of Hadamard's conditions.

---

## ★★ Applied

**★★4.** Using the refinement table of Section 2.1 of the lesson, compute the
ratio of condition numbers for each doubling of $n$. Show that
$\log_{10}(\text{condition})$ is approximately linear in $n$, estimate the slope,
and state the practical implication for quoting a condition number.

---

**★★5.** For the unattainable datum of Section 3, explain why the relative
residual decreases from 0.833 at rank 8 to 0.117 at rank 48 and then to
$4.1\times10^{-13}$ at rank 80, while the model norm jumps from 0.42 (attainable)
to 174 (unattainable). Which statement is the honest description of the problem:
"the residual reaches machine precision, so the inversion converged" or "the
residual floor at rank 48 is a property of the datum"?

---

**★★6.** Using the amplification table of Section 4.2, compute the largest model
perturbation — in absolute weighted norm and as a multiple of
$\lVert m_{\text{true}}\rVert = 0.421$ — that is invisible at a 1 per cent noise
level, for each of the modes $k = 8, 16, 32, 48, 64$. State the trend.

---

## ★★★ Research-oriented

**★★★7.** Construct one datum that is exactly in the range of the 80-node kernel
and four that are not, and report for each the relative residual at retained ranks
20 and 48 and the model norm at full rank. The demonstration's setup uses
$z = 0.05$, a 0.10-wide Gaussian at $x = 0.4$ for the in-range case, and
out-of-range data are Gaussians centred at $x = 0.5$.

(a) Tabulate the results for widths 0.006, 0.012, 0.025 and 0.05, plus a step
function.
(b) Report the trend in the rank-20 residual against width and explain it in terms
of the wavenumber content of each datum.
(c) Explain the model norm column and why it is the more diagnostic quantity.

---

**★★★8.** Truncation at rank $r$ was used in the lesson as a crude regulariser.
Implement instead the smooth spectral filter $f_k = \lambda_k^2/(\lambda_k^2 +
\alpha)$ on the same problem, choose $\alpha$ so that the residual matches the
1 per cent noise level, and compare the model error with the best truncated
inversion at the same noise level.

(a) Report $\alpha$, the residual, and the model error for the filtered inversion.
(b) Report the rank, residual and model error for the best truncated inversion.
(c) Explain which does better and why, in terms of the shape of the filter as a
function of $\lambda_k$.

---

**★★★9.** Downward continuation is the exact inverse of the attenuation that makes
the gravity inverse problem ill posed. A potential field measured on a plane at
height $h$ above the source region is related to the field on the source plane by
multiplication of the wavenumber-$f$ component by $e^{-2\pi h\lvert f\rvert}$.

(a) Derive the amplification factor for the *inverse* operation.
(b) If the data carry relative noise $\varepsilon$, show that components with
$f > \ln(1/\varepsilon)/(2\pi h)$ are not recoverable, and compute the limiting
wavenumber and the limiting wavelength for $\varepsilon = 10^{-3}$ and
$h = 1$ km.
(c) Repeat for a borehole palaeoclimate problem, where the kernel is diffusive and
the diffusive length scale is $\sqrt{\kappa t}$: state which role the depth plays
and explain why the recoverable time span is much shorter than the measurement
span.

---

**★★★10.** A reviewer writes: "The inversion is well posed because the matrix has
full rank and the condition number is only $10^3$."

(a) State two reasons why this is wrong.
(b) Give the two numbers that would make the claim testable, and say how they
would be measured.
(c) Explain what happens to the claim as the discretisation is refined, using the
growth rate estimated in exercise 4.
(d) Write three sentences of a reply that a reviewer would accept.
