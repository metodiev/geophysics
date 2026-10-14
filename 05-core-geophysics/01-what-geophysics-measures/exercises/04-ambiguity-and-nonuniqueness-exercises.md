# Exercises — 05-01-04 Non-Uniqueness of Geophysical Models

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** State in one sentence why a finite, noise-free data set cannot determine
a continuous source distribution.

**★2.** Define the null space of a linear operator $\mathbf{G}$ and explain
what a null-space vector implies for interpretation.

**★3.** For a 2-D sheet at depth $d$, state the transform relation between the
anomaly and the sheet density, and identify the depth-dependent factor.

---

## ★★ Applied

**★★4.** Two sheets are at depths $d_1 = 400$ m and $d_2 = 100$ m and produce
identical surface fields. Write the filter relating their Fourier transforms
and compute its value at a wavenumber corresponding to a wavelength of 1 km.
State whether the shallower or the deeper equivalent is broader.

**★★5.** A discretised operator has 150 observations and 600 model cells of
full row rank. State a lower bound on the null-space dimension and explain why
it is only a bound.

**★★6.** Explain why the deeper equivalent source in ★★4 is unusable in
practice, using the behaviour of the filter.

**★★7.** A published gravity model fits the data to within the estimated noise.
List three further pieces of information you would require before treating the
model as a geological interpretation.

---

## ★★★ Research-oriented

**★★★8.** Construct the null space numerically. Build $\mathbf{G}$ for a stated
line of observations and a stated deeper grid of sheet cells, compute the SVD,
extract the right singular vector with the smallest singular value, and verify
that $\lVert\mathbf{G}\mathbf{n}\rVert/(\sigma_\text{max}\lVert\mathbf{n}\rVert)
< 10^{-14}$. Then add a scaled multiple of $\mathbf{n}$ to a chosen model and
report the change in total mass and in the computed field. Conclude with a
statement about what the data determine.

**★★★9.** Quantify the instability. Repeat the inversion of noisy data
(0.02 mGal) for source sheets at 50, 100, 300, 600 and 1200 m. Tabulate the
condition number, the recovered model RMS, and the data misfit. Identify the
depth at which round-off starts to limit the data fit, explain why, and state
which prior information you would add to make any of these models defensible.

**★★★10.** Write a two-page critique of the sentence "our inversion reproduces
the observed anomaly, so the model is reliable." Address: what is actually
reproduced, what is not constrained, how the regularisation chose the answer,
and what test would distinguish a meaningful model from an equivalent one.
