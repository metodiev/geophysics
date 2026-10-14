# Exercises — 18-02-03 The Generalised (Moore-Penrose) Inverse

Attempt these before reading the
[solutions](./03-generalized-inverse-solutions.md). The lesson is
[03 The Generalised Inverse](../03-generalized-inverse.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the four Moore–Penrose conditions and say in words what each one does.

**★2.** Write $G^{+}$ in terms of the SVD and explain why only non-zero singular
values appear.

**★3.** For $G$ of shape $8\times6$ with rank $4$, give the shapes of $G^{+}$,
$GG^{+}G$, $G^{+}GG^{+}$, $GG^{+}$ and $G^{+}G$, and the rank of the two projectors.

## ★★ Applied

**★★4.** Show algebraically that if $X$ and $Y$ both satisfy the four conditions
then $X = Y$, and state which condition you used at each step.

**★★5.** The demonstration reports that `solve(G.T@G, G.T@d)` returns numbers with
$\kappa(G^{\!\top}G) = 3.357\times10^{17}$ and a maximum error of $1.902$ against
$G^{+}\mathbf{d}$. (a) Explain why no exception was raised. (b) State the two checks
that would have caught it.

**★★6.** With $\mathbf{d} = G(1,2,3,4,5,6)^{\!\top}$ the complete solution set is
$\mathbf{m} = \hat{\mathbf{m}} + (I-G^{+}G)\mathbf{z}$ with
$\lVert\hat{\mathbf{m}}\rVert = 9.402127$. Verify the measured values
$\lVert\mathbf{m}\rVert = 9.4120$ at $\lVert\mathbf{z}\rVert = 0.5$ and $9.4415$ at
$\lVert\mathbf{z}\rVert = 2.0$ using the orthogonality of the two terms.

## ★★★ Research-oriented

**★★★7.** The continuity table shows
$\max\lVert\Delta G^{+}\rVert/\lVert G^{+}\rVert = 14334.9$ at
$\delta = 10^{-3}$ and $43071.9$ at $\delta = 10^{-4}$. Estimate the growth law,
predict the value at $\delta = 10^{-5}$, and state the consequence for choosing a
rank tolerance in an automated pipeline.

**★★★8.** You are building a production inversion library. Specify the rank
decision procedure you will implement (tolerance rule, diagnostics printed, refusal
conditions), and justify each element with a measurement from this lesson or its
prerequisites.
