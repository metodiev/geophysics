# Exercises — 06-03-03 Moment Tensors, Decomposition and Physical Meaning

Attempt these before reading the
[solutions](./03-moment-tensors-solutions.md). The lesson is
[03 Moment Tensors, Decomposition and Physical Meaning](../03-moment-tensors.md)
and the demonstration is
[`../code/moment_tensor_demo.py`](../code/moment_tensor_demo.py). All tensors are
**SYNTHETIC**. Use the conventions of the lesson:
$M_{\text{iso}} = \mathrm{tr}(M)/3$, $M_0 = (\lambda_1-\lambda_3)/2$ on the
deviatoric part, $\varepsilon = -\lambda_2/\max(|\lambda_1|,|\lambda_3|)$,
$1\ \mathrm{N\,m} = 10^{7}\ \mathrm{dyn\,cm}$, and
$M_{\mathrm w} = \tfrac23\log_{10}M_0[\mathrm{N\,m}] - 6.033333$.

## ★ Foundational

**★1.** For $M = \mathrm{diag}(4,-1,-3)\times10^{19}\ \mathrm{N\,m}$, compute
$\mathrm{tr}(M)$, $M_{\text{iso}}$, $M_0$ and $\varepsilon$.

**★2.** For the same tensor, write out $M^{\text{dc}}$ and $M^{\text{clvd}}$
explicitly and add them to recover $M$.

**★3.** Compute $M_{\mathrm w}$ for the $M_0$ of ★1 using both the exact SI offset
and the commonly quoted $-6.07$. State the difference in magnitude units and the
corresponding factor in $M_0$.

## ★★ Applied

**★★4.** A tensor is $M = 2.0\times10^{19}\,\mathrm{I}
+ \mathrm{diag}(5,0,-5)\times10^{19}\ \mathrm{N\,m}$. Compute $\mathrm{tr}(M)$,
$M_{\text{iso}}$, $M'$, $M_0$, $\varepsilon$, and the ratio
$M_{\text{iso}}/\max|M_{ij}|$. Compare the last number with the demo's
"isotropic + DC" row and explain any difference.

**★★5.** Prove that the isotropic and deviatoric parts are orthogonal under
$A:B = \sum_{ij}A_{ij}B_{ij}$, and that $\lVert M\rVert^2 =
\lVert M_{\text{iso}}\rVert^2 + \lVert M'\rVert^2$.

**★★6.** For a general double couple $M = M_0(\hat n\hat s^{\mathsf T}
+ \hat s\hat n^{\mathsf T})$ with $\hat n\perp\hat s$, prove that the eigenvalues
are $+M_0$, $0$ and $-M_0$, and hence that $M_0$ as defined in the lesson is the
scalar moment and $\varepsilon = 0$.

**★★7.** The demo prints a "trace" of $+2.56\times10^{2}\ \mathrm{N\,m}$ and an
"eigenvalue sum" of $-5.12\times10^{2}\ \mathrm{N\,m}$ for a source built to be
traceless with $M_0 = 3.4\times10^{18}\ \mathrm{N\,m}$. Compute the spacing of
double-precision numbers near $3.4\times10^{18}$ and use it to explain why the two
printed numbers differ and why neither is physically meaningful.

## ★★★ Research-oriented

**★★★8.** A moment-tensor inversion of a small induced event returns
$\varepsilon = 0.35$ with a stated confidence interval that excludes zero.
List, in order of increasing plausibility for a *shallow, small, fluid-affected*
event, at least four distinct physical or modelling causes of a large
$\varepsilon$, and for each name the single additional observation that would
most directly test it.

**★★★9.** Design a synthetic experiment that measures the bias in $\varepsilon$
introduced by using a **one-dimensional** velocity model to invert data generated
in a **three-dimensional** model. Specify the model perturbation, the inversion
parameterisation, the metric (e.g. mean and spread of $\hat\varepsilon$ over many
noise realisations), and the perturbation size at which you predict the bias
exceeds the noise-induced spread. A specification that could not be executed is a
failed answer.

**★★★10.** Show that a change of $\Delta$ in $M_{\mathrm w}$ corresponds to a
moment factor $10^{1.5\Delta}$, and use it to argue how many significant figures
of $M_0$ are justified when $M_{\mathrm w}$ is quoted to two decimal places.
Then state what this implies for reporting $M_0$ as a physical measurement.
