# Exercises — 14-01-02 Aquifers, Porosity, Permeability and Storativity

Attempt these before reading the
[solutions](./02-aquifer-types-and-properties-solutions.md). The lesson is
[02 Aquifers, Porosity, Permeability and Storativity](../02-aquifer-types-and-properties.md).
All rocks are **SYNTHETIC** teaching values.

Constants to use: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$, $\mu_w = 1.002 \times 10^{-3}\ \mathrm{Pa\,s}$ (water
at $20\ ^\circ\mathrm{C}$), $\beta_w = 4.4 \times 10^{-10}\ \mathrm{Pa^{-1}}$,
$1\ \mathrm{darcy} = 9.869233 \times 10^{-13}\ \mathrm{m^2}$.

## ★ Foundational

**★1.** A synthetic sandstone has $\rho_b = 2.10\ \mathrm{g\,cm^{-3}}$ and
$\rho_s = 2.68\ \mathrm{g\,cm^{-3}}$. Compute the total porosity, and state how
many litres of water sit in $1\ \mathrm{m^3}$ of saturated rock.

**★2.** A synthetic sand has $n = 0.28$, $n_e = 0.24$ and $S_y = 0.22$. Compute
$S_r$ and the volume of water drained from a $1\ \mathrm{m^2}$ column when the
water table falls $2\ \mathrm{m}$. State the result in litres.

**★3.** A synthetic gravel has $K = 5.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$
measured with water at $20\ ^\circ\mathrm{C}$. Convert this to intrinsic
permeability in m$^2$ and in darcy, showing the units.

## ★★ Applied

**★★4.** A synthetic confined unit has $\alpha = 2.0 \times 10^{-9}\
\mathrm{Pa^{-1}}$, $n = 0.20$, $b = 25\ \mathrm{m}$. Compute $S_s$ and $S$. Then
compute the volume released from a $4\ \mathrm{km^2}$ area under an $8\ \mathrm{m}$
head decline, and compare it with what an unconfined unit with $S_y = 0.20$ would
release over the same area under a $1\ \mathrm{m}$ water-table decline.

**★★5.** Apply Kozeny–Carman with $c_{\text{KC}} = 180$ to a synthetic clean sand
($d = 0.30\ \mathrm{mm}$, $n = 0.30$) and to a synthetic clay
($d = 0.002\ \mathrm{mm}$, $n = 0.45$). Report both $K$ values and their ratio, and
state which of the two results should not be trusted and why.

**★★6.** A synthetic layered unit consists of 1 m at
$1.0 \times 10^{-4}\ \mathrm{m\,s^{-1}}$, 4 m at $1.0 \times 10^{-6}\
\mathrm{m\,s^{-1}}$ and 5 m at $1.0 \times 10^{-7}\ \mathrm{m\,s^{-1}}$. Compute
$K_h$, $K_v$, their ratio, and the transmissivity from $K_h$ in
m$^2$ s$^{-1}$ and m$^2$ d$^{-1}$.

## ★★★ Research-oriented

**★★★7.** Design a programme to determine $S_y$ and $S_s$ of a synthetic
unconfined-to-confined unit to accuracies of $\pm 0.01$ and $\pm 20\%$
respectively. Choose the experiments (column drainage, water-level response to a
known recharge event, pumping test), state the measurement precision each requires,
and show the arithmetic that connects the required precision to the instrument
resolution. State one systematic error per experiment that a precision argument
alone would miss.

**★★★8.** The Kozeny–Carman constant $c_{\text{KC}}$ ranges from about 10 to 200.
Compute $K$ for the sand of ★5 with $c_{\text{KC}} = 10$ and $200$, express the
range as a multiplicative factor, and then compare it with the factor by which $K$
changes when $n$ is uncertain by $\pm 15\%$. Which uncertainty should a project
attack first, given that $n$ comes from a density log with $\pm 0.02$ porosity
units of error?
