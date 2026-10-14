# Exercises — 05-03-01 The Forward Problem: From Model to Data

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Write the forward problem in general and in linear form, naming each
symbol and its unit.

**★2.** State the kernel $G_{ij}$ for gravity on a cell grid and check its
dimensions.

**★3.** Explain in two sentences why the forward problem is well-posed and the
inverse problem is not.

---

## ★★ Applied

**★★4.** A single prism with density contrast 500 kg/m³ occupies
$x,y\in[-100,100]$ m, $z\in[50,250]$ m. Write the kernel entry $G_{11}$ for an
observation at the origin and one model cell (the whole prism), compute the
anomaly, and compare with the tabulated value 1.021214 mGal.

**★★5.** Refine the model into $2\times2\times2$ equal sub-prisms. Predict, from
superposition, whether the total anomaly changes. Then state what *does* change
if the prism is subdivided.

**★★6.** Explain why two adjacent cells give nearly identical columns of
$\mathbf{G}$, and what that implies for the condition number.

---

## ★★★ Research-oriented

**★★★7.** Build $\mathbf{G}$ for a stated 1-D line of 40 observations and a
50-cell sheet model. Report $\mathrm{cond}(\mathbf{G})$, the singular value
spectrum's decay, and the number of singular values below $10^{-6}$ of the
largest. State what that number means for how many independent parameters the
data can support.

**★★★8.** Validation exercise. Take the closed-form prism anomaly and the
Gauss–Legendre quadrature of the same integral, and report the measured relative
agreement at $n = 4, 8, 16, 32, 64$ nodes. Identify the round-off floor and
state the tolerance you would adopt for a production code, with justification.
Then inject a 2% error into the kernel and confirm your tolerance rejects it.
---

**★★★9.** Build the resolution matrix $\mathbf{R} = \mathbf{G}^{+}\mathbf{G}$ for a
stated line of observations and a stated sheet discretisation. Report (a) the
diagonal entry at the central cell, (b) the row sum and the corresponding spatial
width, (c) the largest off-diagonal entry, and (d) the ratio of the resolution
width to the source depth. Then answer: what fraction of the true central-cell
value does the inversion recover, where does the rest go, and why is the
resolution width *narrower* than the anomaly half-width? Finally, state which
single change to the survey would raise the diagonal most, and justify it from
the structure of $\mathbf{R}$ rather than from trial and error.
