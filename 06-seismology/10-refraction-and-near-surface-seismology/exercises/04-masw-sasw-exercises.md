# Exercises — 06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./04-masw-sasw-solutions.md). The lesson is
[04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../04-masw-sasw.md).
The demonstration model is a Love-wave case: $v_{s1} = 200\
\mathrm{m\,s^{-1}}$, $\rho_1 = 1800\ \mathrm{kg\,m^{-3}}$, $H = 10\ \mathrm{m}$ over
$v_{s2} = 800\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$, so
$\mu_2/\mu_1 = 17.778$.

## ★ Foundational

**★1.** State the interval within which the phase velocity of the fundamental Love
mode must lie for this model, and give the two frequencies at which the
demonstration comes to within $0.0012\%$ of the two bounds. Explain in one sentence
why the bound is exact and not approximate.

**★2.** At $f = 2\ \mathrm{Hz}$ the measured phase velocity is
$790.98\ \mathrm{m\,s^{-1}}$. Compute $\lambda$, $\lambda/3$ and $c/2f$, with units,
and state which of the three is an exact relation and which are conventions.

**★3.** Verify numerically that $c = 206.4294\ \mathrm{m\,s^{-1}}$ satisfies the
dispersion relation at $f = 20\ \mathrm{Hz}$: compute
$x = \omega H\sqrt{1/v_{s1}^{2}-1/c^{2}}$ and compare $\tan x$ with
$(\mu_2/\mu_1)\sqrt{1/c^{2}-1/v_{s2}^{2}}/\sqrt{1/v_{s1}^{2}-1/c^{2}}$.

## ★★ Applied

**★★4.** From the Jacobian table, a $5\%$ error in $v_{s1}$ changes $c$ by
$\partial\ln c/\partial\ln v_{s1} \times 5\%$. Compute that change at $50\
\mathrm{Hz}$ and at $2\ \mathrm{Hz}$, and state which measurement each frequency
would be used for.

**★★5.** In the short-spread (8–40 Hz) ridge, the accepted $H$ range is
$9.00$–$11.00\ \mathrm{m}$ and the accepted $v_{s1}$ range is
$195.0$–$200.0\ \mathrm{m\,s^{-1}}$. Express both as percentages of the true values
($H = 10.0\ \mathrm{m}$, $v_{s1} = 200.0\ \mathrm{m\,s^{-1}}$) and state what the
asymmetry of the two ranges says about which parameter the curve pins down.

**★★6.** The correlation between the $H$ column and the $v_{s1}$ column of the
Jacobian is $-0.9356$. Compute $r^{2}$ and state what it means for the acceptable
set of models.

## ★★★ Research-oriented

**★★★7.** Specify an experiment to test whether widening the frequency band breaks
the thickness–velocity ridge. State the model, the noise realisations and why they
must be shared, the grid, the metric (the half-width of the accepted $H$ range),
and the outcome you expect with a number from the lesson's table.

**★★★8.** The dispersion relation depends on $\mu = \rho v_s^{2}$, and the
demonstration assumes the densities. Derive the density error that a $5\%$ error in
$v_s$ would compensate, and state the practical consequence for a site where the
water table is shallower than the depth being measured.
