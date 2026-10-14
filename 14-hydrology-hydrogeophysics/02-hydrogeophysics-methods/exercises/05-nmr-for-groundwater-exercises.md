# Exercises — 14-02-05 Surface NMR for Direct Water Detection

Attempt these before reading the
[solutions](./05-nmr-for-groundwater-solutions.md). The lesson is
[05 Surface NMR for Direct Water Detection](../05-nmr-for-groundwater.md). All
kernels, profiles and pore sizes are **SYNTHETIC**.

Use
$f_L = (\gamma/2\pi)B = 42.577\,B_{\mathrm{nT}}\ \mathrm{Hz}$ with
$\gamma = 2.6752218744 \times 10^{8}\ \mathrm{rad\,s^{-1}\,T^{-1}}$;
$z_q = 12\sqrt{q}$ m with $q$ in A ms; normalized FWHM $= 1.1548\,z_q$;
$A(q) = \int K(q,z)\theta(z)\,\mathrm{d}z$;
$\sigma_\theta \approx \sigma/\sqrt{\sum_q\sum_z K^2\Delta z}$; and
$T_2 = r/(3\rho_2)$.

## ★ Foundational

**★1.** A site has $B = 47\ 000\ \mathrm{nT}$. Compute the Larmor frequency in
kHz, and state what happens to the signal if the system is tuned 50 Hz away from
it in a field that varies by 100 nT across the loop.

**★2.** Compute the pulse moment whose kernel peaks at 30 m, and the normalized
full width at half maximum of that kernel. State in one sentence what the width
means for a 5 m thick layer at that depth.

**★3.** A unit has $\theta = 0.15$ between 20 and 35 m. Compute the water column in
mm and in metres of water.

## ★★ Applied

**★★4.** Using the lesson's detection-limit table
($\sigma_\theta = 0.0194$ for the 20–30 m band at $\sigma = 0.05$), compute the
noise level required to resolve $\theta = 0.10$ at two standard deviations. Compare
it with the $\sigma = 0.05$ noise used in the lesson's inversion, express both as a
fraction of the peak sounding amplitude, and state the practical implication for the
deepest band in the table (45–60 m).

**★★5.** An NMR sounding measures $T_2 = 40$ ms in a sandy unit. Compute the pore
radius for $\rho_2 = 20\ \mathrm{\mu m\,s^{-1}}$, then for
$\rho_2 = 40\ \mathrm{\mu m\,s^{-1}}$ on the same data. State the practical
consequence of not knowing $\rho_2$.

**★★6.** A neutron log gives total porosity 0.30 in a unit where the surface NMR
water content is 0.22. Compute the invisible fraction, state two physically
distinct explanations, and say which measurement distinguishes them.

## ★★★ Research-oriented

**★★★7.** Design a surface NMR sounding for a 20 m thick aquifer whose top is at
25 m depth beneath a conductive clay cover. Specify the pulse-moment range, the
number of moments and the stacking, using the kernel's depth and width scalings;
give the error budget for water content; and state the form in which the result must
be reported (given the regularisation requirement). Then explain in two sentences
why the conductive cover is both a help and a hindrance compared with ERT.

**★★★8.** State precisely what the demonstration's linearity check
($A(2\theta) = 2A(\theta)$ to 2.000000000) verifies and what it does not. Then
design a verification suite for a surface-NMR forward model: one analytic limit,
one physical-scaling check, one convergence or interpolation check, and one
consistency check between the sounding and a borehole NMR log. Explain what each
test would catch that the others would not, and identify the single thing a
verification suite cannot establish about a surface-NMR result.
