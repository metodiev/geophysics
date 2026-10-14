# Exercises — 08-01-03 Spherical Harmonic Analysis of the Magnetic Field

Attempt these before reading the
[solutions](./03-spherical-harmonic-magnetic-solutions.md). The lesson is
[03 Spherical Harmonic Analysis](../03-spherical-harmonic-magnetic.md). All
coefficients are **SYNTHETIC** teaching values.

Use $a = 6371\ \mathrm{km}$ and Schmidt semi-normalised harmonics with
$P_1^0 = \cos\theta$, $P_1^1 = \sin\theta$.

## ★ Foundational

**★1.** Evaluate $P_2^2(\cos\theta)$ and $P_3^1(\cos\theta)$ at
$\theta = 45^{\circ}$ from the definition, showing the normalisation factor
explicitly.

**★2.** Write down the orthogonality integral for $(n,m) = (2,2)$ and evaluate
both the closed form and the value the demonstration obtained by quadrature.

**★3.** For $g_1^0 = -30000$, $g_1^1 = -1800$ and $h_1^1 = +4800\ \mathrm{nT}$,
compute the degree-1 power $R_1$ from
$R_n = (n+1)\sum_m\left[(g_n^m)^2+(h_n^m)^2\right]$.

## ★★ Applied

**★★4.** At $(\text{lat},\text{lon}) = (0^{\circ}, 0^{\circ})$ with
$g_1^0 = -30000\ \mathrm{nT}$, compute $X$, $Z$ and $I$, then repeat after adding
$g_2^0 = +1200\ \mathrm{nT}$. Explain why $X$ does not change and why $Z$ is
three times the quadrupole coefficient's Legendre contribution.

**★★5.** What maximum degree is needed to represent a feature of wavelength
2000 km (a) at the Earth's surface, (b) at an altitude of 400 km? State the
formula and the two numbers.

**★★6.** A satellite at 400 km measures a degree-5 component with amplitude
$20\ \mathrm{nT}$. What is its amplitude at the surface, and at 100 km altitude?
If the noise at degree 13 is $1\ \mathrm{nT}$ rms at 400 km, what is it after
naive downward continuation to the surface, and what does that imply for the
usable maximum degree?

## ★★★ Research-oriented

**★★★7.** Derive the determinant of the internal/external separation matrix
$$\begin{pmatrix}1 & 1\\ (1-\varepsilon)^{-(n+2)} & (1-\varepsilon)^{n-1}\end{pmatrix}$$
to first order in $\varepsilon$, where the two radii are $a$ and $a(1-\varepsilon)$.
Evaluate it for $n = 2$, $\varepsilon = 0.05$ and compare with the exact value
$-0.27774$. State the scaling of the coefficient errors with $\varepsilon$.

**★★★8.** Specify a scheme for downward-continuing a noisy satellite model to a
depth of your choosing. Give the objective function, how the maximum degree is
chosen, the stopping rule, and one validation test that would detect an
over-continued model. A specification that could not be executed is a failed
answer.
