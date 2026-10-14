# Exercises — 08-03-06 Magnetic Inversion and Its Non-Uniqueness

Attempt these before reading the
[solutions](./06-magnetic-inversion-solutions.md). The lesson is
[06 Magnetic Inversion](../06-magnetic-inversion.md). All models are
**SYNTHETIC**.

## ★ Foundational

**★1.** An inversion uses 200 data and a model of 4000 cells. State the nullity
before regularisation, and the nullity if the cell size is halved in each of three
dimensions.

**★2.** The column norms of the sensitivity matrix are $1.6066\times10^{3}$ nT per
A m$^{-1}$ for the shallowest cells and $1.1764$ for the deepest. Compute the
ratio and state what it means for how the inversion distributes magnetisation.

**★3.** State what a Tikhonov penalty does to an underdetermined inverse problem
in one sentence.

## ★★ Applied

**★★4.** The recovered peak magnetisation is 4.950 A m$^{-1}$ against a true
4.00 A m$^{-1}$ at the chosen regularisation. Compute the percentage error and
state why it is not reduced by choosing a smaller $\lambda$.

**★★5.** A null-space model with 99.3% of its energy below 5 km is added at an
amplitude of 20 A m$^{-1}$; the model norm changes by 156% and the predicted data
by $5.2\times10^{-15}$ of the data norm. State what this demonstrates about the
inverse problem, and compute what the data change would be as a fraction of the
0.50 nT noise level.

**★★6.** The unconstrained inversion has 13 cells with negative magnetisation out
of 168. The non-negative solution has none, changes the model by 17.8% and
changes the total moment from $4.349\times10^{10}$ to $3.499\times10^{10}$ A m$^2$.
Compute the percentage change in moment and explain why the reduced moment is not
evidence that the true moment is smaller.

## ★★★ Research-oriented

**★★★7.** Design a survey and inversion experiment to determine how much a second,
perpendicular profile reduces the nullity of the two-body problem. State the
metric, the model parametrisation for both cases, and what you expect for the
depth resolution of the deeper body.

**★★★8.** Two inversions of the same data differ: one uses a smoothness penalty,
the other a total-variation penalty. State two quantities on which they will
agree and two on which they will differ, and say which of the four you would
report.

**★★★9.** A paper reports an induced-magnetisation inversion with a peak
susceptibility of $0.15$ and no statement of the assumed magnetisation direction.
Write the three questions you would ask, and the arithmetic reason for each.
