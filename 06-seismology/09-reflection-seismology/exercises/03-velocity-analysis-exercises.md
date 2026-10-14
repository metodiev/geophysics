# Exercises — 06-09-03 Velocity Analysis and Moveout Interpretation

Attempt these before reading the
[solutions](./03-velocity-analysis-solutions.md). The lesson is
[03 Velocity Analysis](../03-velocity-analysis.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** A reflector has $t_0 = 1.5\ \mathrm{s}$ and $v = 2800\
\mathrm{m\,s^{-1}}$. Compute its two-way time and moveout at $x = 2000\
\mathrm{m}$.

**★2.** From the demonstration's cable-length table, compute the *relative*
90%-width at each offset ($\text{width}/2500\ \mathrm{m\,s^{-1}}$) and compare
with the printed percentages.

## ★★ Applied

**★★3.** Derive $\partial(\Delta t)/\partial v$ for the hyperbolic moveout and
show that, at small offset, it scales as $x^{2}/v^{3}$. Explain in words why
that scaling is the statement that "longer cables measure velocity better".

**★★4.** A reflector is picked with $v_{\text{stack}} = 3200\
\mathrm{m\,s^{-1}}$ at $t_0 = 1.8\ \mathrm{s}$ and its true dip is $30^\circ$.
Compute the true velocity, the bias as a percentage of the true velocity, and
the depth error that would be made by converting $t_0$ with the stacking
velocity instead of the true one.

**★★5.** Using the demonstration's resolution table (widths $350$, $160$, $90$,
$50$, $40\ \mathrm{m\,s^{-1}}$ at maximum offsets $800$, $1200$, $1600$, $2400$,
$3200\ \mathrm{m}$), compute the exponent $-\log(w_2/w_1)/\log(x_2/x_1)$ for each
consecutive pair. State which rows follow the $x^{-2}$ prediction of ★3 and
which do not, and give the reason.

## ★★★ Research-oriented

**★★★6.** A survey requires velocity to $1\%$ at $t_0 \approx 1.5\ \mathrm{s}$,
$v \approx 2500\ \mathrm{m\,s^{-1}}$, using a $30\ \mathrm{Hz}$ wavelet. Using the
demonstration's measurements, state whether the tabulated cable lengths can
reach that precision, and specify the smallest change (cable length, wavelet
frequency, or both) that would. Show the arithmetic of your extrapolation and
state its exponent.

**★★★7.** Design a velocity-analysis QC procedure that would detect a
$1/\cos\theta$ dip bias before it entered a depth conversion. State the
observable, the diagnostic threshold, and the independent measurement that would
confirm the diagnosis. Use only quantities that a processing sequence already
produces.
