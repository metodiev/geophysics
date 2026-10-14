# Exercises — 14-05-01 Time-Lapse ERT for Infiltration and Transport

Attempt these before reading the
[solutions](./01-time-lapse-ert-solutions.md). The lesson is
[01 Time-Lapse ERT](../01-time-lapse-ert.md). All models are **SYNTHETIC**
teaching values, and every number needed is either in the lesson or derivable
from it with the formulae given there.

## ★ Foundational

**★1.** A SYNTHETIC soil has $\rho_w = 10\ \Omega\,\mathrm{m}$, $\phi = 0.35$,
$m = 1.80$ and $n = 2.00$. Compute the bulk resistivity at $S = 0.40$ and at
$S = 0.80$, and state the ratio $\rho(0.80)/\rho(0.40)$.

**★2.** Using the Wenner two-layer series, evaluate the two analytic limits and
show that they give $\rho_a \to \rho_1$ as $a/h \to 0$ and
$\rho_a \to \rho_1(1+k)/(1-k)$ as $a/h \to \infty$. With
$\rho_1 = 90\ \Omega\,\mathrm{m}$ and $\rho_2 = 330\ \Omega\,\mathrm{m}$, compute
the large-$a$ limit numerically.

**★3.** State the units of $\rho_a$, of the transfer resistance $R_t$, of the
geometric factor $k$ and of the time-lapse ratio $r$, and check by dimensional
analysis that $r$ is dimensionless.

## ★★ Applied

**★★4.** In the lesson's model, a wetting front reaches 0.5 m and the array
spacings are 0.5, 1, 2, 4, 8 and 16 m. From the ratio table, state the ratio at
each spacing and decide which spacings would detect the front at 3 sd against a
stated relative noise of 1.5%.

**★★5.** A survey reports $r = 0.2934$ and interprets it as a wetting front with
$\rho_w$ fixed. Write down the family of (saturation, pore-water resistivity)
pairs that fit the same number, and compute the members at splits $x = 0$,
$0.5$ and $1.0$ for $\phi = 0.35$, $n = 2.00$ and $S_0 = 0.45$. State one
measurement that would exclude the salinity member.

**★★6.** The array is designed for a 1.0 m target but the shortest spacing is
4 m. Using the ratio table, decide whether the design can detect a 0.5 m front at
the 3-sd level with 1% noise, and if not, state what must be changed.

## ★★★ Research-oriented

**★★★7.** The lesson shows that an $L_2$ penalty of weight $\alpha = 10^{-2}$
biases the recovered thickness by $-16\%$ while degrading the data fit by only
$1.1\times10^{-2}$ dex. Design an experiment that would let you *choose* $\alpha$
defensibly rather than by taste: state the metric, the data you would need, and
what you would report. A specification that could not be executed is a failed
answer.

**★★★8.** A colleague argues that because the equivalence between saturation and
salinity is exact, no resistivity monitoring programme is worth running. Write a
short rebuttal that (a) names the quantities that *are* constrained by the ratio
data, (b) states the measurements that break the equivalence, and (c) gives one
experimental design in which the ambiguity does not matter.
