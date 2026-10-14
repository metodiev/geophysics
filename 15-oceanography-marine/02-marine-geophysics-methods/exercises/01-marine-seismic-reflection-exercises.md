# Exercises — 15-02-01 Marine Seismic Reflection: Airguns, Streamers, Processing

Attempt these before reading the
[solutions](./01-marine-seismic-reflection-solutions.md). The lesson is
[01 Marine Seismic Reflection](../01-marine-seismic-reflection.md). All models
are **SYNTHETIC** teaching values.

Use SI units throughout:
$\rho_{\text{water}} = 1025\ \mathrm{kg\,m^{-3}}$,
$c_{\text{water}} = 1500\ \mathrm{m\,s^{-1}}$.

## ★ Foundational

**★1.** Compute $Z_1$, $Z_2$, the impedance contrast
$(Z_2-Z_1)/(Z_2+Z_1)$, $R$ and $T$ for an interface with
$v_1 = 1600\ \mathrm{m\,s^{-1}}$, $\rho_1 = 1900\ \mathrm{kg\,m^{-3}}$,
$v_2 = 2400\ \mathrm{m\,s^{-1}}$, $\rho_2 = 2200\ \mathrm{kg\,m^{-3}}$. State the
polarity and check that $1 + R = T$.

**★2.** A multi-layer section has $R = -0.18$ at an interface. State what that
implies about the impedance below relative to above, and give the transmitted
coefficient.

**★3.** Show by dimensional analysis that $R$ is dimensionless and that
$Z = \rho v$ has units of $\mathrm{kg\,m^{-2}\,s^{-1}}$.

## ★★ Applied

**★★4.** Derive $t^{2} = t_0^{2} + x^{2}/v^{2}$ from the two-leg geometry of a
single reflector. Then compute the moveout at $x = 1200\ \mathrm{m}$ for
$t_0 = 1.5\ \mathrm{s}$ and $v = 2000\ \mathrm{m\,s^{-1}}$.

**★★5.** Compute the first-order residual moveout
$\Delta t_{\text{res}} \approx (x^{2}/2t_0)(1/v_{\text{try}}^{2} - 1/v^{2})$ for a
$3\,\%$ velocity error with $x = 3000\ \mathrm{m}$, $t_0 = 1.0\ \mathrm{s}$,
$v = 2000\ \mathrm{m\,s^{-1}}$. Compare with the half-width of a $30\ \mathrm{Hz}$
wavelet and state whether the stack survives.

**★★6.** For the synthetic model of the lesson, the water bottom has
$R = +0.3908$ and the third interface $R = +0.1718$. A processor normalises the
whole trace by the water-bottom peak. What are the three interface coefficients
expressed as fractions of the water-bottom coefficient, and why is this
normalisation the reason that "relative amplitudes" survive and "absolute
amplitudes" do not?

**★★7.** Compute $\lambda/4$ at $30\ \mathrm{Hz}$ in (a) water at
$1500\ \mathrm{m\,s^{-1}}$, (b) sediment at $1800\ \mathrm{m\,s^{-1}}$,
(c) sediment at $3000\ \mathrm{m\,s^{-1}}$, and (d) the same sediment as (c) but
after attenuation has lowered the dominant frequency to $12\ \mathrm{Hz}$. State
which change costs more resolution.

## ★★★ Research-oriented

**★★★8.** The lesson's wedge model shows a non-monotonic tuning curve, so an
amplitude anomaly has two possible thicknesses. Design a processing or
acquisition test that resolves the ambiguity for a real dataset. State what you
would measure, the assumption the test relies on, and the failure mode that would
produce a confident wrong answer. A specification that could not be executed is a
failed answer.

**★★★9.** The demonstration measures the residual moveout at one offset. Derive
the *worst-case* residual over a whole offset range $[x_1, x_2]$ and the
associated fractional amplitude loss for a Gaussian wavelet of standard deviation
$\sigma_t$. Express the requirement on the velocity error as an inequality, and
state how it scales with cable length and with two-way time.
