# Exercises — 01-07-07 Orthogonality, Projections and Least Squares

Attempt these **closed-book**, on paper, before opening the
[solutions](./07-orthogonality-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Find the least-squares line $y = a + bx$ for the four points
$(0,1), (1,2), (2,2), (3,4)$.

(a) Form $G$, $G^\mathsf{T}G$ and $G^\mathsf{T}d$ and solve the normal equations.
(b) Report the residual vector and $\|r\|$.
(c) Verify $G^\mathsf{T}r = 0$ by hand and state what it means in words about the
residuals and the elevation.
(d) Verify that the residuals sum to zero, and explain why they must.

---

**★2.** Derive $\nabla_m\tfrac12\|Gm - d\|^{2} = G^\mathsf{T}(Gm - d)$ from components:
write the sum out explicitly, differentiate with respect to a single component $m_k$,
and confirm that the result assembles into $G^\mathsf{T}(Gm-d)$.

---

## ★★ Applied

**★★3.** For the data of ★1:

(a) Compute the projection matrix $P = G(G^\mathsf{T}G)^{-1}G^\mathsf{T}$ and give it
explicitly.
(b) Report the leverages $h_i$ and verify $\sum h_i = 2$.
(c) Verify $P^{2} = P$ and $P = P^\mathsf{T}$ to machine precision.
(d) Which point has the largest leverage, and what does that mean about its influence on
the fitted slope?
(e) A blunder adds $1.0$ to the datum at the largest-leverage point. Estimate the change
in the fitted slope, and compare with the same blunder applied at the smallest-leverage
point.

---

**★★4.** A three-parameter model is fitted to five data.

(a) Write out the Householder reflector for the first column of $G$: give the vector $v$
and the matrix $I - 2vv^\mathsf{T}/v^\mathsf{T}v$, and show that it maps the first
column onto a multiple of $e_1$.
(b) Show that $\kappa_2(R) = \kappa_2(G)$ for the triangular factor $R$ of a QR
factorisation.
(c) State the smallest $\kappa_2(G)$ at which the normal-equation route loses at least
eight decimal digits in double precision, and derive the number.
(d) State how many digits the QR route retains at that conditioning.

---

## ★★★ Research-oriented

**★★★5.** Weighted least squares with two measurements of the same physical quantity:
$d_1 = 10.0 \pm 0.1$ and $d_2 = 11.0 \pm 1.0$.

(a) State the weights implied by $W = C_d^{-1}$ for independent measurements.
(b) Compute the weighted mean and the unweighted mean.
(c) Compute the variance of each estimator under the stated uncertainties
($\mathrm{Var} = 1/\sum w_i$ for the weighted estimate; derive the unweighted variance
explicitly).
(d) Report both standard deviations and the efficiency ratio.
(e) Explain in one sentence why the unweighted answer is not merely inefficient but
*wrong*.

---

**★★★6.** Orthogonal polynomials and basis conditioning. For the eight elevations of
the lesson's gravity dataset ($z = 0, 200, \ldots, 1400$ m), fit a cubic trend with

(a) the centred, scaled basis $\{1, s, s^{2}, s^{3}\}$ with $s = (z-700)/1400$;
(b) the raw monomial basis $\{1, z, z^{2}, z^{3}\}$ in metres.

Compute (i) $\kappa_2(G)$ for both bases, (ii) the fitted values at the eight stations
for both, (iii) the maximum absolute difference between the two sets of fitted values,
and (iv) the maximum *relative* difference between the parameter vectors (after
converting to the same units, or state why they are not comparable).

Then explain in a short paragraph why the fitted values agree far better than the
parameters do, and what that implies about which quantity to trust in an inversion.
