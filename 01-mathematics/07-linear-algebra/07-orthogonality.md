---
id: 01-07-07
title: "Orthogonality, Projections and Least Squares"
level: advanced
prereqs: ["01-07-04", "01-07-05"]
estimated_minutes: 90
tags: [linear-algebra, least-squares, projection, normal-equations]
---

# Orthogonality, Projections and Least Squares

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** orthogonality as the zero of an inner product, and use it to
   characterise the closest point in a subspace.
2. **Derive** the normal equations $G^\mathsf{T}Gm = G^\mathsf{T}d$ from the
   stationarity condition of $\tfrac12\|Gm-d\|^{2}$, not from memory.
3. **Interpret** a least-squares solution as an orthogonal projection, and verify
   the projection's idempotence and symmetry numerically.
4. **Compute** leverage values and explain what an individual datum contributes to
   the fit.
5. **Solve** a least-squares problem by Householder QR, and explain why the normal
   equations square the condition number and cost half the digits.
6. **Carry out** weighted least squares, and explain why the weights are part of the
   definition of the problem rather than an optional refinement.
7. **Recognise** an ill-scaled basis from its condition number, and repair it by
   centring and scaling rather than by changing the algorithm.

## Prerequisites

[01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) for the
column space and the existence question, and
[01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md)
for the condition number that governs the two solution routes of Section 3.4.

## 1. Intuition: the origin of linear inversion

Most measurements do not determine a model exactly. Eight gravity stations do not
pin down a level and a trend to sixteen digits; they give you eight numbers that are
consistent with a line only to within their own scatter. The system $Gm = d$ has no
solution, and the useful question becomes: **which model comes closest?**

"Closest" needs a distance, and any distance worth the name comes from an inner
product. So the problem is

$$\text{minimise} \quad \phi(m) = \tfrac12\|Gm - d\|^{2} ,$$

and the answer is geometry: the minimiser is the orthogonal projection of $d$ onto
the column space of $G$. The residual must be perpendicular to every column — if it
were not, moving along the column with which it had positive inner product would
reduce the length. Writing "perpendicular to every column" out in algebra gives the
**normal equations**

$$G^\mathsf{T}(Gm - d) = 0 \quad\Longleftrightarrow\quad G^\mathsf{T}Gm = G^\mathsf{T}d .$$

That is the origin of every linear inversion: gravity and magnetic inversion,
tomographic travel-time inversion, surface-wave dispersion, receiver functions, and
the linearised outer loop of full-waveform inversion all solve a system of this form
at every iteration.

Three facts about it need care, and they are the substance of the lesson.

- The normal equations are *not* the algorithm of choice. Solving them squares the
  condition number; QR does not ([01-07-05](./05-determinants-inverses.md)
  Section 3.6 quantifies the loss).
- The problem has no unique solution if $G$ has a null space; the minimum-norm
  solution is then selected by the geometry as well, and
  [01-07-08](./08-svd.md) is the tool for seeing it.
- "Least squares" without weights asserts that every measurement has the same
  uncertainty. That is a physical claim, and it is usually false.

## 2. Precise definitions

### 2.1 Orthogonality and orthogonal bases

Two vectors are orthogonal if $\langle x, y\rangle = 0$; a set is orthogonal if every
pair is, and orthonormal if in addition each has unit norm. In an orthonormal basis
$\{q_1,\dots,q_n\}$, coordinates are free:

$$x = \sum_i \langle x, q_i\rangle q_i , \qquad \|x\|^{2} = \sum_i \langle
x, q_i\rangle^{2} ,$$

the second being Parseval's identity. The practical value of an orthonormal basis is
that a least-squares problem in it decouples: each coefficient is determined
independently, and the normal matrix $G^\mathsf{T}G$ is diagonal. Householder QR and
the SVD are, at bottom, systematic constructions of orthonormal bases.

### 2.2 Orthogonal complements and the projection theorem

For a subspace $S \subseteq \mathbb{R}^{m}$, the **orthogonal complement**
$S^{\perp}$ is the set of vectors orthogonal to every element of $S$. Then
$\mathbb{R}^{m} = S \oplus S^{\perp}$: every vector decomposes uniquely as
$y = y_S + y_{\perp}$ with $y_S \in S$. The **projection theorem** states that
$y_S$ is the unique closest point of $S$ to $y$, and it is proved in two lines.
Take any $s \in S$. Then

$$\|y - s\|^{2} = \|(y - y_S) + (y_S - s)\|^{2} = \|y - y_S\|^{2} + \|y_S - s\|^{2}$$

because the two terms are orthogonal, with the cross term
$2\langle y - y_S, y_S - s\rangle = 0$ since $y_S - s \in S$ and $y - y_S \in
S^{\perp}$. Both terms are nonnegative, so the minimum is attained at $s = y_S$.
This is the Pythagorean identity of
[01-07-01](./01-vectors-and-spaces.md) Section 3.1 doing real work.

### 2.3 The projection matrix

If the columns of $G$ are independent, the matrix of the orthogonal projection onto
$\mathcal{C}(G)$ is

$$P = G(G^\mathsf{T}G)^{-1}G^\mathsf{T} ,$$

characterised by $P^{2} = P = P^\mathsf{T}$ and $\mathcal{C}(P) = \mathcal{C}(G)$.
The fitted values are $\hat d = Pd$, the residual is $r = (I - P)d$, and the
decomposition $d = \hat d + r$ satisfies

$$\|d\|^{2} = \|\hat d\|^{2} + \|r\|^{2} ,$$

the Pythagorean identity for data.

The diagonal entries $P_{ii} = h_i$ are the **leverages**. They satisfy
$0 \le h_i \le 1$ and $\sum_i h_i = \operatorname{tr}P = \operatorname{rank}G$, so
the average leverage is $(\text{number of parameters}) / (\text{number of data})$.
A datum with $h_i$ far above the average exerts an unusual amount of influence on the
fit; a datum with $h_i$ near zero contributes almost nothing that the other data do
not already supply.

### 2.4 The normal equations, and the assumptions behind them

Setting $\nabla_m\phi = G^\mathsf{T}(Gm - d) = 0$ gives
$G^\mathsf{T}Gm = G^\mathsf{T}d$. The matrix $G^\mathsf{T}G$ is symmetric and
positive semidefinite; it is positive definite, hence invertible, exactly when $G$
has full column rank. With weights $W$ (and $W = C_d^{-1}$ in the statistical
reading) the problem becomes

$$\text{minimise} \quad \tfrac12(Gm - d)^\mathsf{T}W(Gm - d)
\quad\Longrightarrow\quad G^\mathsf{T}WGm = G^\mathsf{T}Wd .$$

The statistical content: unweighted least squares asserts that all data have equal
variance and are uncorrelated. Weighted least squares asserts $C_d = W^{-1}$.
Nothing in the algebra tells you which is true about the instrument.

### 2.5 QR

A **QR factorisation** writes $G = QR$ with $Q$ having orthonormal columns and $R$
upper triangular. Then

$$\|Gm - d\|^{2} = \|R m - Q^\mathsf{T}d\|^{2} + \|(I - QQ^\mathsf{T})d\|^{2} ,$$

so the minimiser solves the triangular system $Rm = Q^\mathsf{T}d$ by back
substitution, and the second term is the irreducible residual norm. No normal
equations are formed, so no squaring of the condition number occurs:
$\kappa_2(R) = \kappa_2(G)$, whereas $\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2}$.
Householder QR is the standard construction: at each column, reflect the subcolumn
onto a multiple of the first unit vector with an orthogonal transformation $I -
2vv^\mathsf{T}/v^\mathsf{T}v$.

## 3. Step-by-step derivations

### 3.1 A linear fit to gravity versus elevation

Take eight stations at elevations $z = 0, 200, \ldots, 1400$ m with a synthetic
gravity residual built as $g = 25.0 - 0.3086z + \epsilon$, in mGal, with a
deterministic $\epsilon$ of magnitude below $0.06$ mGal. The slope is chosen to be
numerically equal to the free-air gradient $0.3086\ \mathrm{mGal\,m^{-1}}$, which is
$308.6\ \mu\mathrm{Gal\,m^{-1}}$. (In a real survey the fitted slope would also
contain Bouguer, terrain and instrumental effects; the number here is a scale
reference, not an interpretation.)

Building $G = [\mathbf{1} \mid z]$ and the normal matrix:

$$G^\mathsf{T}G = \begin{bmatrix} 8 & 5600 \\ 5600 & 5\,600\,000 \end{bmatrix},
\qquad G^\mathsf{T}d = \begin{bmatrix} -1528.160000 \\ -1\,588\,198.000000
\end{bmatrix},$$

whence $a = 25.01583333$ mGal and $b = -0.3086226190$ $\mathrm{mGal\,m^{-1}}$, that
is $-308.6226$ $\mu\mathrm{Gal\,m^{-1}}$. The recovered slope differs from the
construction by $2.3\times10^{-5}$ $\mathrm{mGal\,m^{-1}}$, which is what the noise
allows.

The residuals, in mGal,

$$(0.02416667,\ -0.04130952,\ 0.05321429,\ -0.05226190,\ 0.02226190,\
-0.05321429,\ 0.06130952,\ -0.01416667),$$

sum to $1.9\times10^{-13}$ — forced by the first column being $\mathbf{1}$, since
orthogonality to it means the residuals sum to zero — and satisfy
$G^\mathsf{T}r = (1.9\times10^{-13}, -4.5\times10^{-11})$, that is, zero to
round-off. Their Euclidean norm is $\|r\| = 0.12304664$ mGal, which is the smallest
achievable misfit for any $(a,b)$, and the value any claimed solution must reproduce.

### 3.2 The projection picture, verified

With $P = G(G^\mathsf{T}G)^{-1}G^\mathsf{T}$ the demonstration finds the leverages

$$h = (0.416667,\ 0.273810,\ 0.178571,\ 0.130952,\ 0.130952,\ 0.178571,\
0.273810,\ 0.416667),$$

with $\sum h_i = 2.000000$ — the number of parameters — and
$\max|P^{2} - P| = 2.22\times10^{-16}$, so $P$ is idempotent to round-off. The
residual is annihilated: $\max|Pr| = 9.740\times10^{-14}$. And the Pythagorean check
closes: $\|d\|^{2} = 451\,925.645600$ while
$\|\hat d\|^{2} + \|r\|^{2} = 451\,925.645600$.

Two readings of the leverages deserve emphasis. First, they depend only on the
*design* — on the station elevations — and not on the measured values, so they can be
computed before the survey. Second, the pattern is symmetric and largest at the two
endpoints ($h = 0.4167$) and smallest at the centre ($h = 0.1310$): the two extreme
stations control the slope, and a blunder at either end damages the fit more than a
blunder in the middle. That is the quantitative version of a rule of thumb every
surveyor knows.

### 3.3 Deriving the normal equations without memorising them

From $\phi(m) = \tfrac12\|Gm - d\|^{2} = \tfrac12 m^\mathsf{T}G^\mathsf{T}Gm -
m^\mathsf{T}G^\mathsf{T}d + \tfrac12 d^\mathsf{T}d$ and the derivative identities
of [01-07-10](./10-matrix-calculus.md) Section 3,

$$\nabla_m\phi = G^\mathsf{T}Gm - G^\mathsf{T}d ,$$

verified numerically in
[`code/matrix_calculus_demo.py`](./code/matrix_calculus_demo.py) Section 1 against a
central difference (analytic $(8.0, 17.0)$ against numerical
$(8.0, 17.000000001)$, maximum error $6.0\times10^{-10}$). Setting the gradient to
zero is the normal equations. Because $G^\mathsf{T}G$ is positive definite when $G$
has full column rank, this stationary point is the unique global minimum:

$$\phi(m^{*} + \delta) = \phi(m^{*}) + \tfrac12\delta^\mathsf{T}G^\mathsf{T}G\delta
\ge \phi(m^{*}) ,$$

with equality only if $G\delta = 0$. A null space therefore appears here as a flat
direction of the misfit — non-uniqueness at the level of a function, not merely of a
matrix — which is [01-07-04](./04-rank-and-nullspace.md)'s result expressed as
curvature. The eigenvalue discussion of [01-07-06](./06-eigenvalues.md) Section 2.4
is the language.

### 3.4 Normal equations against QR, with an exact reference

Because the data are synthetic and the abscissae are integers, the least-squares
solution can be computed in exact rational arithmetic. That gives a reference against
which both float routes can be judged. Three cases:

**Case A — degree-3 trend, centred and scaled basis with
$s_i = (z_i - 700)/1400$.** $\kappa_2(G) = 40.747$ and
$\kappa_2(G^\mathsf{T}G) = 1.6603\times10^{3}$; the maximum relative parameter errors
are $2.931\times10^{-12}$ for the normal equations and $2.538\times10^{-12}$ for QR.
Both routes are at round-off. This is what a well-scaled basis looks like.

**Case B — the same fit with the raw cubic basis in metres.** Now
$\kappa_2(G) = 3.2518\times10^{9}$ and $\kappa_2(G^\mathsf{T}G) = 1.0574\times10^{19}$,
which exceeds $1/\epsilon_{\text{mach}}$. The parameter errors are
$1.149\times10^{-10}$ and $2.164\times10^{-12}$: the normal equations are 53 times
worse. Survivable here only because this particular dataset has almost no signal in
the weak directions; the weak directions are where an inverse problem's interesting
information lives.

**Case C — two nearly parallel rays, $\delta = 10^{-8}$ km.** With
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$ and exact data from
$m = (0.05, -0.02)$ $\mathrm{s/km}$:

| route | result | maximum relative error |
|---|---|---|
| exact (rational) | $(0.05,\ -0.02)$ | — |
| normal equations | **failed**: numerically singular, zero pivot | — |
| Householder QR | $(0.0499999999,\ -0.0199999999)$ | $7.97\times10^{-9}$ |

The normal-equation system cannot even be factored. QR recovers both parameters to
eight digits, consistent with $\kappa\,\epsilon = 4\times10^{8}\times2.2\times10^{-16}
= 8.8\times10^{-8}$.

The rule that emerges: **the error of the normal-equation route grows like
$\kappa(G)^{2}\epsilon$ and the error of QR grows like $\kappa(G)\epsilon$.** Both
statements are worst-case bounds and neither is always attained — Case A shows both
routes at round-off — but the difference in the exponent is what decides whether a
method survives contact with a real problem.

### 3.5 Weighted least squares, and why it is not optional

Suppose each station's residual has an uncertainty
$\sigma_i = 0.05 + z_i/20\,000$ mGal, growing slightly with elevation. Weighting by
$w_i = 1/\sigma_i^{2}$ and minimising $\sum_i w_i r_i^{2}$ gives

| fit | $a$ (mGal) | $b$ ($\mathrm{mGal\,m^{-1}}$) | $\chi^{2}$ |
|---|---|---|---|
| ordinary | $25.01583333$ | $-0.3086226190$ | $2.381256$ |
| weighted | $25.02154838$ | $-0.3086316960$ | $2.356033$ |

The weighted fit has a lower weighted misfit, as it must: it optimises that
functional. The two slopes differ by about $9\times10^{-6}$
$\mathrm{mGal\,m^{-1}}$, which is small here because the synthetic noise is nearly
homoscedastic. With realistic heteroscedastic uncertainties the difference is not
small, and the ordinary fit is simply the answer to a different question.

The context for the $\chi^{2}$ values: with 8 data and 2 parameters, a good fit with
correctly stated uncertainties would give $\chi^{2}$ near 6. Both values are far
below that, which is honest information about this dataset — the $\sigma_i$ chosen
for the illustration are larger than the perturbations actually built into it — and
it illustrates the standard diagnostic use of $\chi^{2}$ as a test of the *stated*
uncertainties rather than of the model.

### 3.6 More parameters always fit better

Fitting polynomials of increasing degree to the same eight points:

| degree | parameters | $\|r\|$ (mGal) | standard error of slope |
|---|---|---|---|
| 1 | 2 | $0.12304664$ | $3.875605\times10^{-5}$ |
| 2 | 3 | $0.12164546$ | $1.527792\times10^{-4}$ |
| 3 | 4 | $0.12058838$ | $3.799759\times10^{-4}$ |
| 4 | 5 | $0.11915558$ | $7.921050\times10^{-4}$ |
| 5 | 6 | $0.09566172$ | $1.339791\times10^{-3}$ |

The residual norm decreases monotonically — it must, because a larger column space
can only be closer to the data — while the standard error of the slope, computed as
$\hat\sigma\sqrt{(G^\mathsf{T}G)^{-1}_{22}}$ with
$\hat\sigma^{2} = \|r\|^{2}/(n - p)$, rises by a factor of 35. **A small residual is
therefore not evidence of a good model.** Model comparison requires a criterion that
penalises parameters, and constructing such a criterion is
[18-inverse-problems](../../18-inverse-problems/README.md)'s business.

## 4. Physical interpretation

**The residual is orthogonal to every column, so each column is unexplained by the
residual.** For the linear fit the two orthogonality conditions read: the residuals
sum to zero (no net offset left in the data) and the residuals are uncorrelated with
elevation (no trend left). Those are exactly the two statements a geophysicist makes
after detrending a profile, and they are not heuristic — they are the definition of
the best fit.

**Weights are the physics of the instrument.** A gravimeter reading, a hand-picked
arrival time and a satellite-derived gravity value have different uncertainties, and
the relative uncertainties are known. Least squares in units of the data's own
uncertainty is the only version with a statistical interpretation, and the choice
$W = C_d^{-1}$ is the statement "the data covariance is $C_d$". When the data are
correlated — common with smoothed or gridded products, and unavoidable with
interferometric measurements — $W$ is not diagonal and the off-diagonal structure
matters. See
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).

**Leverage is survey design.** The leverages of Section 3.2 follow from the station
positions alone, so they can be optimised before the survey is paid for. Placing
stations to make the leverages uniform is a standard design objective, and the
converse — recognising that a datum with near-zero leverage adds nothing — is how one
avoids needless fieldwork.

**A least-squares fit is a projection and therefore a low-pass operation.** It
removes the component of the data orthogonal to the model space and keeps the rest.
In a trend-removal step, the "rest" is thrown away as regional; in a tomographic
inversion the "rest" is the part of the signal the parameterisation cannot represent.
Both are the same projection, and the resolution matrix of
[01-07-08](./08-svd.md) is what tells you which is which.

**The centring-and-scaling rule is a condition-number rule.** Section 3.4 Case B is
$8\times10^{7}$ times worse conditioned than Case A for identical physics. Scaling a
basis so that all columns have comparable norm and mean zero is not cosmetic tidiness;
it is the difference between a solvable problem and an unsolvable one, and it costs
nothing.

## 5. Python demonstration

The companion script is
[`code/least_squares_demo.py`](./code/least_squares_demo.py), with six sections: the
data and design matrix, the normal equations solved by hand, the projection picture,
normal equations versus Householder QR against an exact rational reference, weighted
least squares, and the residual-decreases-with-parameters table.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 2, fit | $a = 25.01583333$ mGal, $b = -0.3086226190$ $\mathrm{mGal\,m^{-1}}$ ($-308.6226$ $\mu\mathrm{Gal\,m^{-1}}$) | the slope recovers the free-air-gradient scale used to build the data |
| 2, orthogonality | $G^\mathsf{T}r = (1.9\times10^{-13}, -4.5\times10^{-11})$, $\sum r_i = 1.9\times10^{-13}$ | residuals perpendicular to the column space, to round-off |
| 2, misfit | $\|r\| = 0.12304664$ mGal | the minimum achievable by any $(a, b)$ |
| 3, leverage | $h = (0.4167, 0.2738, 0.1786, 0.1310, 0.1310, 0.1786, 0.2738, 0.4167)$, $\sum h_i = 2$ | endpoint stations control the slope |
| 3, projection | $\max\|P^{2} - P\| = 2.22\times10^{-16}$, $\max\|Pr\| = 9.74\times10^{-14}$ | idempotent, and it annihilates the residual |
| 3, Pythagoras | $\|d\|^{2} = 451\,925.645600 = \|\hat d\|^{2} + \|r\|^{2}$ | the geometric decomposition is exact |
| 4, centred basis | $\kappa(G) = 40.747$, errors $2.9\times10^{-12}$ and $2.5\times10^{-12}$ | a good basis makes both routes fine |
| 4, raw basis | $\kappa(G) = 3.25\times10^{9}$, errors $1.15\times10^{-10}$ and $2.16\times10^{-12}$ | 53× worse, and $\kappa(G^\mathsf{T}G) = 1.06\times10^{19}$ |
| 4, near-parallel rays | normal equations **fail with a zero pivot**; QR gives $7.97\times10^{-9}$ relative error | $\kappa^{2}\epsilon$ versus $\kappa\epsilon$, made visible |
| 5, weighted fit | $a = 25.02154838$, $b = -0.3086316960$; $\chi^{2}$ $2.356033$ against $2.381256$ | weighting is part of the definition of the problem |
| 6, overfitting | $\|r\|$ falls $0.12304664 \to 0.09566172$ while the slope's standard error rises $3.9\times10^{-5} \to 1.34\times10^{-3}$ | a better fit, a worse model |

> **Breaking exercise.** In Section 4, add a ninth station at elevation $3000$ m to
> the dataset of Section 1 and re-fit the line. Predict, before running: (a) the new
> leverage of that station and of the original endpoints, (b) whether the slope
> estimate becomes more or less precise, and (c) what happens to the condition
> number of the raw cubic basis. Then run and reconcile. The leverage calculation can
> be done with a calculator; the condition number will astonish you.

## 6. Exercises

Full set and worked solutions:
[`exercises/07-orthogonality-exercises.md`](./exercises/07-orthogonality-exercises.md)
and
[`exercises/07-orthogonality-solutions.md`](./exercises/07-orthogonality-solutions.md).
Four to start with:

**★1.** Find the least-squares line $y = a + bx$ for the four points
$(0,1), (1,2), (2,2), (3,4)$. Report $a$, $b$, the residual vector, $\|r\|$, and
verify $G^\mathsf{T}r = 0$ by hand.

**★2.** Derive the normal equations from
$\phi(m) = \tfrac12\|Gm - d\|^{2}$ by writing out the components and
differentiating with respect to $m_k$, and confirm that you obtain
$G^\mathsf{T}Gm = G^\mathsf{T}d$ entry by entry.

**★★3.** For the data of ★1, compute the projection matrix $P$, the leverages, and
verify $\sum h_i = 2$ and $P^{2} = P$. Which point has the largest leverage, and
what does that mean about its influence on the fitted slope?

**★★4.** A three-parameter model is fitted to five data. (a) Write the QR step for
the first column of $G$ explicitly (the Householder reflector). (b) Explain why
$\kappa_2(R) = \kappa_2(G)$. (c) State the smallest $\kappa_2(G)$ at which the
normal equations lose at least eight digits in double precision.

**★★★5.** Weighted least squares. Data: two measurements of the same physical
quantity, $d_1 = 10.0 \pm 0.1$ and $d_2 = 11.0 \pm 1.0$. (a) Compute the weighted
mean and state the weights. (b) Compute the unweighted mean. (c) Show that the
weighted mean has smaller variance under the stated uncertainties, using
$\mathrm{Var}(\hat m) = 1/\sum w_i$ for the weighted case and computing the
unweighted variance explicitly. (d) Explain in one sentence why the unweighted answer
is not merely less efficient but wrong.

**★★★6.** Orthogonal polynomials. For the eight elevations of Section 3.1,
construct the basis $\{1, s, s^{2}, s^{3}\}$ with $s = (z-700)/1400$ (a) and the
monomial basis in metres (b). (a) Compute $\kappa_2(G)$ for both by constructing
$G^\mathsf{T}G$ and taking a square root of the eigenvalue ratio, or by any
equivalent method you can justify. (b) Compute the condition number of $G^\mathsf{T}G$
directly for both. (c) Re-fit the data with degree 3 in both bases and report the
maximum difference between the two sets of *fitted values*. (d) Explain why the
fitted values agree far better than the parameters do.

## 7. Common mistakes

1. **Solving the normal equations out of habit.** They square the condition number;
   QR costs a similar amount of work and does not. Section 3.4 Case C shows the
   difference between eight correct digits and no answer at all.
2. **Believing that "least squares" specifies a problem.** It does only once the
   weights are stated. Unweighted least squares is a physical claim about the
   instrument.
3. **Reporting a small residual as evidence of a good model.** Section 3.6 shows the
   residual falling monotonically as parameters are added, with the parameter
   uncertainties rising by a factor of 35.
4. **Comparing fitted values from different bases as though the parameters were
   comparable.** Coefficients in a monomial basis are not physical quantities; the
   fitted values and the predictions are.
5. **Ignoring leverage.** A single high-leverage datum can determine the fit, and a
   blunder there is not averaged out by the rest.
6. **Assuming the residual is uncorrelated with everything.** It is orthogonal to the
   *column space* and to nothing else. Structure in the residuals is exactly what
   the columns failed to represent.
7. **Assuming correlated data can be treated as independent.** For gridded or
   smoothed products they cannot; $W$ must then include the off-diagonal terms.
8. **Failing to scale the basis.** An uncentred basis over a wide abscissa range is
   numerically hopeless (Section 3.4 Case B), and the repair is free.

## 8. Real-world applications

- **Trend removal and regional-residual separation.** A least-squares polynomial or
  spline trend is subtracted from gravity, magnetic or elevation data; the projection
  language makes precise what is retained and what is discarded.
- **Travel-time inversion.** The linearised system $G\Delta m = \Delta d$ is solved by
  least squares at every iteration of a tomographic inversion, usually as the inner
  problem of a Gauss–Newton scheme
  ([18-inverse-problems](../../18-inverse-problems/README.md)).
- **Velocity calibration and instrument constants.** Fitting a straight line to a
  calibration series is the simplest possible inverse problem and the one most often
  done carelessly, without weights.
- **Geodetic adjustment.** Network adjustment is weighted least squares with a
  carefully constructed covariance matrix including correlations between baselines;
  the design matrix is where the geometry of the network enters. See
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Regression in machine learning.** Ridge regression, ordinary least squares and
  the normal equations of a linear layer are the same mathematics; the numerical
  lesson about QR transfers unchanged. See
  [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).
- **Spectral and admittance estimation.** Estimating a transfer function between two
  fields is a weighted least-squares problem in the frequency domain, with weights
  from the coherence.
- **Survey design.** Choosing station positions to make the design matrix's columns
  orthogonal — and the leverages uniform — is a direct application of this lesson's
  geometry.

## 9. Further reading

- **Strang, G. *Introduction to Linear Algebra.* Wellesley–Cambridge Press.**
  Orthogonal projections and least squares, with the geometry developed before the
  algebra. Level: beginner to intermediate.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lecture 11 on
  least squares, and the argument for QR over the normal equations in its sharpest
  form. Level: intermediate to advanced.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations.* Johns Hopkins
  University Press.** Chapter 5 on orthogonalisation and least-squares problems,
  including rank-deficient cases. Level: advanced.
- **Lawson, C. L., & Hanson, R. J. *Solving Least Squares Problems.* SIAM.**
  The classical reference, including the column-scaling and rank-deficiency
  discussions. Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic
  Press.** The geophysicist's version, with the generalised inverse, the
  resolution matrix and the data-covariance weighting. Level: intermediate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and Inverse
  Problems.* Academic Press.** Least squares as the first of a family, with a
  careful treatment of the statistical assumptions. Level: intermediate to
  advanced.
- **Draper, N. R., & Smith, H. *Applied Regression Analysis* (3rd ed.). Wiley.**
  Leverage, residuals and diagnostics for practitioners. Level: intermediate.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can derive the normal equations from the stationarity condition, and I know
      where the assumption of full column rank enters.
- [ ] I can explain the projection theorem and use it to say why the minimiser is
      the projection of the data onto the column space.
- [ ] I can construct a projection matrix, verify its idempotence and symmetry, and
      compute leverages.
- [ ] I can explain why the residual is orthogonal to every column and what that
      means for a detrended profile.
- [ ] I can implement Householder QR for a small problem and explain why it avoids
      the squaring of the condition number.
- [ ] I can set up and solve a weighted least-squares problem and say what the
      weights assert.
- [ ] I can explain why a smaller residual can accompany a worse model, with
      numbers.
- [ ] I can recognise an ill-scaled basis and repair it by centring and scaling.

## 11. Related lessons

- [01-07-04 Rank, Null Space and Solvability](./04-rank-and-nullspace.md) — what
  happens to the least-squares solution when the columns are dependent.
- [01-07-05 Determinants, Inverses and Matrix Conditioning](./05-determinants-inverses.md) —
  the condition-number arithmetic that decides between the two solution routes.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) —
  positive definiteness of $G^\mathsf{T}G$, and the curvature interpretation of the
  misfit.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — the
  right way to solve least squares when the singular values span many orders of
  magnitude, and the resolution matrix as a by-product.
- [01-07-10 Matrix Calculus and Sensitivity Derivatives](./10-matrix-calculus.md) —
  where the gradient $G^\mathsf{T}(Gm-d)$ comes from, and the nonlinear generalisation
  to Gauss–Newton.
- [01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md) —
  why $W = C_d^{-1}$ is the statistically correct weight.
- [01-14 Optimization and Variational Methods](../14-optimization/README.md) —
  least squares as a convex problem, and what changes when it is not.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  least-squares fitting when the basis is a set of sinusoids.
