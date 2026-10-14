# Exercises — 06-01-04 Reflected, Refracted and Converted Body Waves

Attempt these before reading the
[solutions](./04-body-wave-arrivals-solutions.md). The lesson is
[04 Body-Wave Arrivals](../04-body-wave-arrivals.md); all numbers are printed by
[`../code/body_wave_arrivals_demo.py`](../code/body_wave_arrivals_demo.py). All
models are **SYNTHETIC** teaching values; the only externally defined numbers used
here are the tabulated travel times of the standard `iasp91` reference model,
which the demonstration queries.

## ★ Foundational

**★1.** For the demonstration's two-layer model ($v_p = 3000$,
$\rho = 2400\ \mathrm{kg\,m^{-3}}$ above; $v_p = 4500$,
$\rho = 2600\ \mathrm{kg\,m^{-3}}$ below), compute $Z_1$, $Z_2$, the
potential-convention reflection coefficient and the displacement-convention
transmission coefficient. State the unit of $Z$.

**★2.** Verify the energy-flux balance $R^2 + (Z_2/Z_1)T^2 = 1$ with your
numbers, and state in one sentence why the factor $Z_2/Z_1$ — rather than
$v_1/v_2$, or nothing — appears.

**★3.** Compute the critical angle of the P leg and say which of the four
coefficients becomes complex beyond it.

## ★★ Applied

**★★4.** The demonstration reports that replacing $Z_2/Z_1$ by $v_1/v_2$ gives a
flux sum of $0.4436885865$ (an error of $0.5563$) and omitting the density factor
gives $0.6371882086$ (an error of $0.3628$). Reproduce both values, and work out
the ratio of the correct flux factor to each wrong one, expressing your answers in
terms of the velocity and density contrasts.

**★★5.** At an incidence angle of $25^\circ$ the demonstration prints
$p = 1.408727539\times10^{-4}\ \mathrm{s\,m^{-1}}$ and transmitted/converted
angles of $39.340477^\circ$, $14.122249^\circ$ and $21.485710^\circ$. Identify
which angle is which, and verify all three from Snell's law using
$v_p = 3000/4500$ and $v_s = 1732/2600\ \mathrm{m\,s^{-1}}$.

**★★6.** Using the demonstration's energy-partition table, write down the
partition at $25^\circ$ and at $45^\circ$ and explain why $R_{pp}$ becomes large
in magnitude while $T_{pp}$ exceeds 1 beyond the critical angle. State what the
flux-sum column being exactly 1.000000 means in that regime.

## ★★★ Research-oriented

**★★★7.** Derive the normal-incidence limit of the Zoeppritz system: show that at
$p = 0$ the four equations decouple into a P system and an S system, that the S
amplitudes vanish identically, and that the P reflection coefficient reduces to
$(Z_2-Z_1)/(Z_2+Z_1)$. Then explain why this limit is *insensitive* to the
overall sign of the transmitted amplitudes.

**★★★8.** The demonstration states that a sign error in the transmitted columns
was caught by re-deriving the four continuity conditions independently, and was
*not* caught by the normal-incidence limit or by the energy sum. Design two
further independent checks that would catch such an error, state what each
measures, and say which one you would trust more and why.

**★★★9.** `Pn` appears in the demonstration's table at $2^\circ$ and $5^\circ$ but
not at $30^\circ$ or $60^\circ$, while `PcP` and `ScS` appear at every distance and
are always later than `P` where both exist. Explain both observations from the
physics of the model, and state which one is a statement about a velocity
contrast and which is a statement about geometry.
