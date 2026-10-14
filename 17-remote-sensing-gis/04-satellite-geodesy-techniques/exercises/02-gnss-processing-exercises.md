# Exercises — 17-04-02 GNSS Processing: Networks, PPP and Error Sources

Attempt these before reading the
[solutions](./02-gnss-processing-solutions.md). The lesson is
[02 GNSS Processing](../02-gnss-processing.md). All models are **SYNTHETIC**
teaching values.

Constants: $c = 299\,792\,458\ \mathrm{m\,s^{-1}}$,
$R_E = 6\,371\,000\ \mathrm{m}$, $\lambda_1 = 0.190294\ \mathrm{m}$,
one fringe $= \lambda_1$ of range.

## ★ Foundational

**★1.** Write the single-difference and double-difference combinations and state,
for each, one error term that cancels and one that does not.

**★2.** A receiver at $z_A = 20^\circ$ and one at $z_B = 20^\circ$ see the same
satellite. Explain why the differential tropospheric delay is then small, and what
happens to it when $z_A = 5^\circ$ and $z_B = 70^\circ$.

**★3.** Compute the mapping functions $1/\cos z$ and the curved-Earth form with
$H = 8\ \mathrm{km}$ at $z = 40^\circ$, and give the percentage difference.

## ★★ Applied

**★★4.** A station observes at $z = 65^\circ$. **(a)** Compute the height error
from a $1.5\ \mathrm{cm}$ zenith wet-delay error using the curved mapping.
**(b)** State which is larger here, the wet-delay term or a VDOP $= 2.0$ applied
to $4\ \mathrm{mm}$ of phase noise.

**★★5.** Using the lesson's ambiguity table: **(a)** at $\sigma = 0.30$ cycles,
estimate the wrong-fix rate from the trend in the table; **(b)** compute the rms
range error expected if every wrong fix were excluded, and state why that number
is not achievable in practice.

**★★6.** A 2.5-year daily position record contains a $5\ \mathrm{mm}$ annual
signal. **(a)** Predict the order of the rate bias from omitting the annual term,
scaling from the lesson's $1.2\ \mathrm{yr}$ case. **(b)** State the two
properties of the record that determine whether the bias is larger or smaller than
your prediction.

## ★★★ Research-oriented

**★★★7.** Design the processing chain and the validation for a 10-station network
whose purpose is to detect a $1\ \mathrm{mm\,yr^{-1}}$ regional uplift over five
years. Specify: the observation strategy, the difference or PPP choice and why, the
noise model you would assume and how you would test it, the seasonal and
discontinuity terms in the model, and the external dataset you would compare
against. Justify each number from the lesson. A specification that could not be
executed is a failed answer.

**★★★8.** The lesson measures a factor of 7.3 between white and flicker noise in
the velocity scatter, for equal *variance*. **(a)** Explain why equal variance
does not mean equal information for a trend estimate. **(b)** State how the ratio
would change if the record were ten times longer, and argue the answer
qualitatively in terms of the correlation time. **(c)** Propose the diagnostic you
would use to identify the noise model from data alone.
