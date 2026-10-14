# Exercises — 08-05-04 EM Inversion and Dimensionality

Attempt these before reading the
[solutions](./04-em-inversion-solutions.md). The lesson is
[04 EM Inversion and Dimensionality](../04-em-inversion.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A response of $70+1440i\ \mathrm{ppm}$ is measured with a noise model of
$2\%$ of amplitude plus a $2\ \mathrm{ppm}$ floor. Compute the standard deviation
of that datum in ppm, showing the two contributions separately.

**★2.** A model predicts $72+1450i\ \mathrm{ppm}$ where the observation is
$70+1440i\ \mathrm{ppm}$. Compute the weighted misfit contribution of this datum
and say whether it is consistent with the stated noise.

**★3.** State the target value of $\chi^2$ for a data set whose weights are the
true standard deviations, and explain in one sentence why a value of $0.4$ is a
reason for suspicion rather than satisfaction.

## ★★ Applied

**★4.** Derive the Occam normal equations from
$\Phi=\lVert W(\mathbf{d}^{\text{pred}}-\mathbf{d}^{\text{obs}})\rVert^2
+\mu\lVert R\mathbf{m}\rVert^2$
by linearising the forward model, and identify which term produces the smoothing
and which the fit.

**★5.** For the demonstration's solution, $\chi^2=0.591$ and the Jacobian's
singular values are $[145.7011,39.4459,10.8823,5.3525,2.9098,1.0397]$. Compute
the formal $1\sigma$ uncertainty along the best- and worst-determined directions
in $\log_{10}\sigma$ units and as factors in conductivity.

**★6.** Two inversions of the same six data give conductor conductivities of
$0.09705$ and $0.10096\ \mathrm{S\,m^{-1}}$ (true value $0.10$) and differ by a
factor of $2.70$ in the layer below the conductor. State what determines the
choice between them and why the data cannot.

## ★★★ Research-oriented

**★7.** Design a survey and inversion strategy that would determine the
conductivity of the demonstration's sixth layer (centre depth $360\ \mathrm{m}$,
kernel peak $0.002$, kernel width $296\ \mathrm{m}$) to within a factor of two.
Specify the frequencies, separations, parametrisation and the evidence of success;
state what the strategy costs relative to the six-frequency, $40\ \mathrm{m}$
survey of the lesson.

**★8.** The lesson finds that a real amplitude factor of $1.15$ is absorbed into a
$+12\%$ conductivity bias with $\chi^2$ of order one, whereas a complex factor
leaves $\chi^2$ in the tens. Explain the mechanism physically (not
mathematically), and predict what a frequency-*dependent* factor of the form
$1+a\ln(f/f_0)$ would do: absorbed, visible, or both?
