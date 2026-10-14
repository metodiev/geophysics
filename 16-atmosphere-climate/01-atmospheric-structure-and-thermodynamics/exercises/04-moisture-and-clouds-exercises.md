# Exercises — 16-01-04 Moisture, Humidity Variables and Cloud Formation

Attempt these before reading the
[solutions](./04-moisture-and-clouds-solutions.md). The lesson is
[04 Moisture and Clouds](../04-moisture-and-clouds.md). Use
$R_d = 287.041$, $R_v = 461.5$, $c_p = 1004.64\ \mathrm{J\,kg^{-1}\,K^{-1}}$,
$g = 9.80665\ \mathrm{m\,s^{-2}}$, $L_v = 2.501\times10^{6}\ \mathrm{J\,kg^{-1}}$
and $e_{s0} = 611.2\ \mathrm{Pa}$ at $273.15\ \mathrm{K}$. All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** Compute $e_s$ at $283.15\ \mathrm{K}$ and at $293.15\ \mathrm{K}$ using
Clausius–Clapeyron, and compute the relative sensitivity
$L_v/(R_vT^2)$ at each. State in one sentence what the pair of numbers means for
the water-vapour content of a warming atmosphere.

**★2.** Air at $290\ \mathrm{K}$ and $950\ \mathrm{hPa}$ has
$\mathrm{RH} = 0.70$. Compute $e_s$, $e$, the mixing ratio $w$, the specific
humidity $q$ and the dewpoint $T_d$. Verify that $e_s(T_d) = e$.

**★3.** For the state of ★2, compute the LCL height with the
$125\ \mathrm{m\,K^{-1}}$ rule of thumb, and state the dewpoint depression you
used.

**★4.** Compute the saturated adiabatic lapse rate at $T = 280\ \mathrm{K}$,
$p = 900\ \mathrm{hPa}$ and the ratio $\Gamma_m/\Gamma_d$. State whether the parcel
is warmer or colder than a dry parcel lifted the same distance.

## ★★ Applied

**★★5.** Derive Clausius–Clapeyron from the Clapeyron equation, stating the two
approximations used. Then integrate it and show that it reproduces the tabulated
$e_s(288.15\ \mathrm{K}) = 1716.80\ \mathrm{Pa}$.

**★★6.** Find the exact LCL for the state of ★2 by the balance
$w_s(T_p(z),p_e(z)) = w$, assuming the environment is a polytropic atmosphere with
surface state $T_0 = 290\ \mathrm{K}$, $p_0 = 950\ \mathrm{hPa}$ and
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$. Compare with the rule-of-thumb answer from ★3
and state the percentage difference. Explain why the sign of the discrepancy is
what it is.

**★★7.** Derive the saturated adiabatic lapse rate
$\Gamma_m = (g/c_p)(1+A)/(1+B)$ with $A = L_vw_s/(R_dT)$ and
$B = L_v^2w_s/(c_pR_vT^2)$, starting from
$c_p\,\mathrm{d}T + (\rho_e/\rho_p)g\,\mathrm{d}z = -L_v\,\mathrm{d}w_s$. Then show
that $\Gamma_m \to \Gamma_d$ as $w_s \to 0$ and identify which physical statement
that limit encodes.

**★★8.** A parcel at the surface has $T = 292\ \mathrm{K}$, $w = 12\ \mathrm{g\,kg^{-1}}$.
It is lifted to $3\ \mathrm{km}$ where the environment has $T_e = 268\ \mathrm{K}$
and $p_e = 700\ \mathrm{hPa}$. Assume the LCL is at $600\ \mathrm{m}$ and that above
it the parcel follows a saturated adiabat with an average lapse rate of
$5.5\ \mathrm{K\,km^{-1}}$. Compute (a) the parcel temperature at $3\ \mathrm{km}$,
(b) the buoyancy acceleration there, and (c) whether the parcel is accelerating
or decelerating. State the largest assumption in your calculation.

## ★★★ Research-oriented

**★★★9.** The lesson measures the fractional residual of the first-law identity
with the exact $w_s$ as $0.01355$ at $z = 475\ \mathrm{m}$, against
$e_s/p = 0.01340$. Design an experiment that measures that residual as a function
of height from the LCL to $8\ \mathrm{km}$ and of surface temperature from
$280$ to $305\ \mathrm{K}$. Predict the scaling of the residual with $e_s/p$
*before* running it, and state what a systematic departure from your prediction
would imply about the derivation of $\Gamma_m$.

**★★★10.** CAPE computed in this lesson assumes an undiluted parcel. Design a
dilution experiment: a parcel entrains environmental air at a stated fractional
rate, so that its $\theta$ and $w$ are relaxed toward the environment. Specify the
entrainment equation, the numerical scheme, the metric (the ratio of diluted to
undiluted CAPE), and predict qualitatively how the metric varies with the
entrainment rate and with the depth of the cloud. State which of your predictions
could be falsified by the experiment and how.

**★★★11.** A colleague writes: "Because saturation vapour pressure rises
$6.5\%$ per kelvin, global precipitation must rise $6.5\%$ per kelvin." Identify
every step at which the argument fails or becomes a modelling assumption, and
state for each whether the gap is physical, definitional, or a matter of
parameterisation. Do not invent numbers: where a number is needed, say what
measurement or model output would be required and how you would test it. Then
write the strongest defensible version of the claim.
