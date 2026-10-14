# Exercises — 15-05-01 Coastal Processes, Sediment Transport and Shoreline Change

Attempt these before the
[solutions](./01-coastal-processes-solutions.md). The lesson is
[01 Coastal Processes, Sediment Transport and Shoreline Change](../01-coastal-processes.md).
All models and data are **SYNTHETIC** teaching values; the model constants are
those printed by `code/coastal_processes_demo.py`.

## ★ Foundational

**★1.** Solve $\omega^2=gk\tanh(kh)$ for $T=8\ \mathrm{s}$ at $h=8\ \mathrm{m}$:
give $k$, $L=\omega/k$… i.e. the wavelength, the phase speed $c$, the group
velocity $c_g$ and $kh$. Compare $c$ with both $\sqrt{gh}$ and $gT/2\pi$, and
state which limit the wave is closer to.

**★2.** Deep-water waves of $T=10\ \mathrm{s}$, $H_0=2.5\ \mathrm{m}$ have
$c_{g0}=7.804\ \mathrm{m\,s^{-1}}$; at 5 m depth the group velocity is
$6.325\ \mathrm{m\,s^{-1}}$. Compute $H$ at 5 m by energy-flux conservation and
state the amplification.

**★3.** Compute the Bruun retreat and the sediment volume per metre of shoreline
for a sea-level rise of $4.0\ \mathrm{mm\,yr^{-1}}$ on a profile with
$\tan\beta=0.015$ and a closure depth of 12 m.

## ★★ Applied

**★★4.** Compute the longshore energy flux $P$, its longshore component $P_{ls}$
and the CERC-type transport $Q$ for $H_b=1.5\ \mathrm{m}$, $\alpha_b=8^\circ$,
$\gamma=0.78$, $K=0.39$, $\rho=1030$, $\rho_s=2650\
\mathrm{kg\,m^{-3}}$, porosity 0.40. Give $Q$ in both $\mathrm{m^3\,s^{-1}}$ and
$\mathrm{m^3\,yr^{-1}}$.

**★★5.** A shoreline has a longshore transport gradient of
$\partial Q/\partial x=2\ \mathrm{m^3\,yr^{-1}}$ per metre of shoreline
(2000 m³/yr per km) and a closure depth of 12 m. Compute the shoreline change
rate in cm/yr, state the trend, and compare its magnitude with the Bruun retreat
of ★3.

**★★6.** A sediment budget closes with: longshore input 1.20,
longshore output 0.95, river input 0.10, cliff erosion 0.03, dredging removal
0.05, offshore loss unknown — all in $10^{6}\ \mathrm{m^3\,yr^{-1}}$. Compute the
offshore loss that closes the budget, then state what the closure error means if
a later measurement shows the offshore loss to be $0.05\times10^{6}\
\mathrm{m^3\,yr^{-1}}$.

## ★★★ Research-oriented

**★★★7.** A monitoring programme must resolve a shoreline-change rate of
$3\ \mathrm{cm\,yr^{-1}}$ with a $2\sigma$ detection threshold over a five-year
period. Given that a shoreline position derived from a multibeam/RTK survey has a
horizontal uncertainty of 0.5 m, compute the number of repeat surveys needed,
state the dominant error term you have neglected, and specify the survey design
(timing, spacing, referencing) that would make the detection possible. A design
that could not be executed is a failed answer.

**★★★8.** Two adjacent 5 km stretches of coast show retreat rates of 45 and
15 cm/yr with a common sea-level rise of 3.5 mm/yr and a common $\tan\beta=0.008$.
**(a)** Compute the Bruun retreat and the residual for each stretch. **(b)** Show
that the residuals imply drift gradients and compute them. **(c)** Design the
measurement programme that would distinguish a genuine drift gradient from a
spatial variation in $\tan\beta$, and state which quantity in each explanation is
a model.
