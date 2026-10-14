# Exercises — 12-02-02 High-Pressure Experiments and Diamond Anvil Cells

Attempt these before reading the
[solutions](./02-high-pressure-experiments-solutions.md). The lesson is
[02 High-Pressure Experiments and Diamond Anvil Cells](../02-high-pressure-experiments.md).
All models and data are **SYNTHETIC** teaching values.

Useful relations: $P = F/A$ with $A = \pi d_c^{2}/4$;
$P = (1/s)(\Delta\lambda/\lambda_0)$ with $s = 5.26\times10^{-4}\ \mathrm{GPa^{-1}}$,
$\lambda_0 = 694.0$ nm;
$P = \frac32 K_0(x^{7/2}-x^{5/2})[1+\frac34(K_0'-4)(x-1)]$ with
$x = (V_0/V)^{2/3}$;
$P_\text{th} \approx \alpha K_T \Delta T$ with $\alpha = 3.0\times10^{-5}$ K$^{-1}$,
$K_T = 130$ GPa.

## ★ Foundational

**★1.** A cell is loaded with 350 N on a culet of 80 µm diameter. Compute the
idealised pressure. Then compute the culet needed to reach 150 GPa at the same load.

**★2.** A synthetic pressure scale has $s = 5.26\times10^{-4}$ GPa$^{-1}$ and
$\lambda_0 = 694.0$ nm. Compute the pressure corresponding to a measured fractional
shift of $2.5\times10^{-2}$, and the pressure resolution for a wavelength resolution
of 0.05 nm. State the relative error of the measurement.

**★3.** Evaluate the third-order Birch–Murnaghan EOS for $V_0 = 40.0$,
$K_0 = 160$ GPa, $K_0' = 4.0$ at $V/V_0 = 0.95$ and at $V/V_0 = 0.80$. Report both
pressures and state which is closer to linear in $1 - V/V_0$.

## ★★ Applied

**★★4.** A fit returns $\mathrm{cov}(K_0,K_0') = \begin{pmatrix}7.0 & -0.25\\
-0.25 & 0.010\end{pmatrix}$ in units of (GPa$^2$, GPa, dimensionless). Compute the
1σ uncertainties, the correlation coefficient, and the 1σ uncertainty on the
combination $K_0 + 4K_0'$.

**★★5.** An experiment reports $V = 27.5\ \mathrm{\AA^3}$ at 28 GPa and 1700 K.
Compute the thermal pressure with the values given above, the static pressure to use
in an isothermal EOS, and the fractional size of the correction. State what an
analyst who neglects it would conclude about $K_T$.

**★★6.** A $P$–$V$ data set extends to 30 GPa with 6 points. Using the lesson's
truncation table as a guide, estimate the bias in $K_0$ and $K_0'$ you would expect,
and state what range would be needed to reduce the $K_0$ uncertainty below 2 %.

**★★7.** An experiment reports $K_0 = 158 \pm 2$ GPa on a scale whose calibration
uncertainty is ±1.5 %. Compute the systematic pressure uncertainty at 60 GPa, the
resulting uncertainty in $K_0$ (using
$\mathrm{d}K_0/\mathrm{d}P_\text{scale} \approx 1$), and state whether the quoted
±2 GPa is meaningful.

## ★★★ Research-oriented

**★★★8.** Design an experiment that determines $K_0'$ independently of $K_0$. State
the observables, the pressure range, the sample requirements, and a quantitative
prediction of the achievable uncertainty. Explain precisely why a wide pressure range
is worth more than more points in a narrow range.

**★★★9.** A deviatoric stress of 1 GPa is present in a sample during a diffraction
experiment. Estimate how it biases the fitted $K_0$, and describe a test that would
detect the bias without knowing the stress state independently.

**★★★10.** The same $P$–$V$ data are fitted with a second-order (Birch–Murnaghan
$K_0'$ fixed at 4) and a third-order EOS. Compute the pressures the two models predict
at $V/V_0 = 0.9$ and 0.7 for $K_0 = 160$ GPa, and state how the difference compares
with a 1 % pressure calibration error at 100 GPa.
