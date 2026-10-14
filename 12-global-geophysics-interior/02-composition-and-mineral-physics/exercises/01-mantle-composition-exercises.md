# Exercises — 12-02-01 Mantle Composition and Peridotite Models

Attempt these before reading the
[solutions](./01-mantle-composition-solutions.md). The lesson is
[01 Mantle Composition and Peridotite Models](../01-mantle-composition.md).
All models are **SYNTHETIC** teaching values.

Useful relations: $\rho = \sum f_i\rho_i$;
$K_V = \sum f_i K_i$; $1/K_R = \sum f_i/K_i$; $K_\text{Hill} = (K_V+K_R)/2$;
$K_\text{HS} = K_1 + f_2/[1/(K_2-K_1) + (1-f_2)/(K_1+\tfrac43 G_1)]$;
$v_p = \sqrt{(K+\tfrac43 G)/\rho}$; $v_s = \sqrt{G/\rho}$ (GPa, g cm$^{-3}$ → km s$^{-1}$).

SYNTHETIC end members (Mg# = 0.90):

| mineral | $\rho$ (g cm$^{-3}$) | $K$ (GPa) | $G$ (GPa) |
|---|---|---|---|
| olivine | 3.22 | 129 | 82 |
| orthopyroxene | 3.21 | 105 | 77 |
| clinopyroxene | 3.28 | 113 | 67 |
| garnet | 3.58 | 175 | 94 |

Chosen Fe slopes per unit decrease of Mg#: $\mathrm{d}\ln\rho = +0.032$,
$\mathrm{d}\ln K = -0.045$, $\mathrm{d}\ln G = -0.065$.
Thermal sensitivities: $\partial\ln v_s/\partial T = -1.2\times10^{-5}$ K$^{-1}$,
$\alpha = 2.5\times10^{-5}$ K$^{-1}$.

## ★ Foundational

**★1.** For the mode (0.62, 0.20, 0.10, 0.08) compute the aggregate density, and
state the one step in this calculation that contains no model error.

**★2.** For the same mode compute $G_V$, $G_R$ and $G_\text{Hill}$, then
$v_s$ from each, and report the spread as a percentage of the Hill value.

**★3.** For an aggregate with $\rho = 3.30\ \mathrm{g\,cm^{-3}}$,
$K = 130\ \mathrm{GPa}$ and $G = 80\ \mathrm{GPa}$, compute $v_p$, $v_s$, $v_p/v_s$
and Poisson's ratio.

## ★★ Applied

**★★4.** A student reports $K_R = 130.2$, $K_\text{HS}^- = 128.4$,
$K_\text{Hill} = 129.0$, $K_V = 127.8$, $K_\text{HS}^+ = 131.0$ GPa, all for the
same aggregate. State which quantity must be wrong, why, and what the ordering
should be.

**★★5.** Starting from the demonstration's lherzolite mode and Mg# = 0.90, compute
the changes in $v_s$ and $\rho$ produced by (a) moving 0.05 of the mode from garnet
to olivine, and (b) lowering Mg# by 0.03. State the sign of each change and which
combination mimics a hot anomaly.

**★★6.** Two compositions fit a measured $(v_p, v_s)$ to within 0.5 %:
$(f_\text{ol}, \text{Mg\#}) = (0.60, 0.89)$ and $(0.72, 0.84)$. Using the
demonstration's slopes ($\mathrm{d}\rho/\mathrm{d}f_\text{ol} = -0.131\
\mathrm{g\,cm^{-3}}$, $\mathrm{d}\rho/\mathrm{d}\text{Mg\#} = -0.100\
\mathrm{g\,cm^{-3}}$), compute their density difference and state whether a density
measurement good to 0.2 % separates them.

**★★7.** A seismic study reports a region with
$\mathrm{d}\ln v_s = -0.30\ \%$ and $\mathrm{d}\ln\rho = +0.05\ \%$ relative to the
surrounding mantle. Using the sensitivities of the lesson, decide whether the anomaly
is more likely thermal or compositional, and give the arithmetic. State the
assumption your decision rests on.

## ★★★ Research-oriented

**★★★8.** Design an observation set that would separate a thermal anomaly from a
compositional one at 1500 km depth. State the observables, the forward model, the
parameter trade-offs you expect, and a quantitative prediction of the resolution in
temperature. Note explicitly which of your observables is the weakest.

**★★★9.** Implement the incremental Hashin–Shtrikman construction for two phases
(adding the second phase as an inclusion with its relative fraction) and show that
it reproduces the exact two-phase closed form. Then extend it to three phases and
check the ordering test against the Voigt and Reuss values.

**★★★10.** Estimate the pressure and temperature corrections needed to compare an
ambient-condition mineral velocity with a seismic velocity measured at 200 km depth.
Use $\mathrm{d}\ln v_p/\mathrm{d}P = 0.6\ \%$ GPa$^{-1}$ (a chosen value), a
lithostatic gradient of 0.033 GPa km$^{-1}$, and a temperature difference of 1300 K.
Show whether the two corrections add or cancel, and compare their size with the
compositional signals of exercise ★★5.
