# Exercises — 10-04-01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole

Attempt these before reading the
[solutions](./01-spt-cpt-crosshole-solutions.md). The lesson is
[01 Geotechnical Testing: SPT, CPT, Cross-Hole and Down-Hole](../01-spt-cpt-crosshole.md).
All models and data in this module are **SYNTHETIC**: the blow counts, cone
resistances, unit weights, velocities and timing errors are teaching values. The
adopted conventions (60% reference energy ratio, $100\ \mathrm{kPa}$ reference
stress, cone net-area ratio $0.8$) are labelled as conventions.

## ★ Foundational

**★1.** A blow count $N = 12$ is measured with a hammer whose energy ratio is
$ER = 55\%$, at a depth where $\sigma'_v = 70\ \mathrm{kPa}$. Compute $N_{60}$,
$C_N$ and $(N_1)_{60}$. State the unit of each.

**★2.** Two cross-hole receivers are at the same depth in boreholes
$5.0\ \mathrm{m}$ apart, and the S-wave first arrival is at $19.2\ \mathrm{ms}$.
Compute $V_s$ and, for $\rho = 1950\ \mathrm{kg\,m^{-3}}$, $G_{\max}$ in MPa.
State the two assumptions the calculation makes.

**★3.** A cone records $q_c = 5.0\ \mathrm{MPa}$, $u_2 = 300\ \mathrm{kPa}$ and
$f_s = 45\ \mathrm{kPa}$ at a depth where $\sigma_v = 90\ \mathrm{kPa}$ and
$\sigma'_v = 60\ \mathrm{kPa}$. Compute $q_t$ with $a = 0.8$, $R_f$, $Q$ and $F$.
State whether the pore-pressure correction is significant here.

## ★★ Applied

**★★4.** In the lesson's SYNTHETIC cross-hole model the exact arrival times at
receivers $2$ and $3\ \mathrm{m}$ deep from a source at $1\ \mathrm{m}$ are
$22.906$ and $20.002\ \mathrm{ms}$. **(a)** Compute the interval velocity with the
straight-ray formula and explain the sign. **(b)** Compute what the formula would
have returned if the second arrival had been at $24.000\ \mathrm{ms}$ instead, and
state what physical situation that would correspond to.

**★★5.** A down-hole survey uses receivers at $1\ \mathrm{m}$ spacing with a
$0.2\ \mathrm{ms}$ pick precision and a $0.05\ \mathrm{ms}$ random trigger jitter.
Compute the relative velocity uncertainty of an interval in a
$180\ \mathrm{m\,s^{-1}}$ layer and in a $600\ \mathrm{m\,s^{-1}}$ layer, and state
which interval is worse and by what factor.

**★★6.** A site gives $(N_1)_{60} = 18$ at $4\ \mathrm{m}$ and
$V_s = 280\ \mathrm{m\,s^{-1}}$. Compute the ratio $(N_1)_{60}/V_s$. State, in one
sentence each, three things you would need before using that ratio to convert a
blow count into a velocity at a different site.

## ★★★ Research-oriented

**★★★7.** Design a borehole seismic programme that determines an interval shear
velocity to $5\%$ in a $180\ \mathrm{m\,s^{-1}}$ layer, given a triggering system
with a $0.2\ \mathrm{ms}$ random jitter and a picker with a $0.05\ \mathrm{ms}$
precision. Choose the geometry (same-depth or fixed-source), the receiver spacing,
the number of receivers per layer, and the quality-control checks. State what
would invalidate the result and how you would detect it in the field.

**★★★8.** The lesson quotes $(N_1)_{60}/V_s = 0.0765$ and
$0.0554\ \mathrm{s\,m^{-1}}$ at two depths of two SYNTHETIC profiles. Construct a
numerical argument for why a *transferable* correlation would require a population
rather than a ratio: state the regression you would fit, the statistic that
measures its usefulness, and the two site conditions under which you would refuse
to apply it.

**★★★9.** A cross-hole survey reports $V_s = 340\ \mathrm{m\,s^{-1}}$ in a layer
that a down-hole survey reports as $290\ \mathrm{m\,s^{-1}}$. Both are said to be
$3\%$ measurements. Enumerate the possible causes in order of likelihood, say how
you would distinguish them with data you could collect in one day, and state what
you would report to the engineer in the meantime.
