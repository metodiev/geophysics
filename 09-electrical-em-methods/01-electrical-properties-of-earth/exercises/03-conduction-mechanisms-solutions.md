# Solutions — 09-01-03 Electrolytic, Electronic and Surface Conduction

> **Read after attempting the exercises.** Lesson:
> [03 Electrolytic, Electronic and Surface Conduction](../03-conduction-mechanisms.md).

---

## ★1 — Ionic conductivity

$$\sigma_w = Fc(\mu_+ + \mu_-)
= 96485.332123\times(0.005\times1000)\times1.310\times10^{-7}
= 0.0632\ \mathrm{S\,m^{-1}}.$$

(The factor 1000 converts $\mathrm{mol\,L^{-1}}$ to $\mathrm{mol\,m^{-3}}$.)
Then $\rho_w = 1/0.0632 = 15.8\ \Omega\,\mathrm{m}$ — a brackish water, close to
the 0.01 mol/L row of the lesson's table with a factor-2 salting-up.

---

## ★2 — Archie conductivity

$$F = 0.22^{-2} = 20.66, \qquad
\sigma_0 = \frac{\sigma_w}{F} = \frac{0.30}{20.66} = 0.01452\
\mathrm{S\,m^{-1}}, \qquad \rho_0 = 68.9\ \Omega\,\mathrm{m}.$$

---

## ★3 — Parallel bound

$$\sigma_\parallel = (1-\phi)\sigma_g + \phi\sigma_p
= 0.8\times10^{4} + 0.2\times0.5 = 8000.1\ \mathrm{S\,m^{-1}}.$$

Units: $\mathrm{S\,m^{-1}}$. The matrix term dominates by four decades.

---

## ★4 — Surface conductivity and apparent porosity

$$\frac{\sigma_w}{F} = \frac{0.50}{16} = 0.03125\ \mathrm{S\,m^{-1}}, \qquad
\sigma_s = 0.08575 - 0.03125 = 0.05450\ \mathrm{S\,m^{-1}}
\ (63.6\% \text{ of the total}).$$

Ignoring it: $F_\text{app} = 0.50/0.08575 = 5.831$,
$\phi_\text{app} = 5.831^{-1/2} = 0.4141$, against a true 0.25 —
a $+65.6\%$ error.

---

## ★5 — Where the error comes from

With $\sigma_s$ 30% low ($0.03815$): $\sigma - \sigma_s = 0.04760$,
$F = 10.504$, $\phi = 0.3086$ ($+23.4\%$).

With $\sigma_s$ 30% high ($0.07085$): $\sigma - \sigma_s = 0.01490$,
$F = 33.56$, $\phi = 0.1726$ ($-31.0\%$).

So the porosity range is $0.173$ to $0.309$ — a factor of 1.8 — from a
surface-term uncertainty alone. A $\pm3\%$ error in the measured conductivity
alone would move $\phi$ by only $\pm1.5\%$. **The surface term dominates the
error budget by more than an order of magnitude**, and the lesson's message is
exactly this: in clay-bearing rock the *calibration* of $\sigma_s$ (or of $Q_v$
and $\beta$) is the measurement.

---

## ★6 — Bounds with sulphide

Parallel ($\sigma_p = 0.5$, $\sigma_g = 10^{4}$, $\phi = 0.15$):

$$\sigma_\parallel = 0.85\times10^{4} + 0.15\times0.5 = 8500.1\
\mathrm{S\,m^{-1}}.$$

Series:

$$\sigma_\text{series} = \left(\frac{0.85}{10^{4}} + \frac{0.15}{0.5}\right)^{-1}
= \left(8.5\times10^{-5} + 0.3\right)^{-1} = 3.332\ \mathrm{S\,m^{-1}}.$$

The bounds differ by a factor 2551, i.e. 3.4 decades. Because they bracket the
answer by more than three orders of magnitude, **a conductivity measurement
cannot resolve the question at all**; what is needed is a measurement sensitive
to grain *surfaces* rather than to connectivity — induced polarisation (module
09-03), or a petrographic/mineralogical determination of whether the sulphide is
in a connected network.

---

## ★7 — Tighter bounds

Tighter (Hashin–Shtrikman) bounds follow from a variational principle: they
require stating the geometry as statistically isotropic and using the
polarisability tensor of a sphere in the host. They are *not* derivable in a short
answer without that machinery, and no attempt should be made to quote them from
memory.

What can be said from the arithmetic already done: the true conductivity lies in
$[3.332, 8500.1]\ \mathrm{S\,m^{-1}}$. If an analyst inverted a *specific*
conductivity inside that interval as a porosity, the claimed precision would be
spurious by a factor of at least $2551^{1/2} = 50$ in any porosity inferred
through a square-root relation — which is the quantitative statement of "the
connectivity ambiguity destroys the porosity interpretation".

---

## ★8 — Decision tree

1. **Is the anomaly even electrical?** Check for a conductor: metal pipe,
   culvert, salt pan, clay lens. Ask for a geological map before an inverse
   model.
2. **Water chemistry:** measure $\rho_w$ on a sample. Do not use a chart.
3. **Clay content:** if CEC or a gamma/SP log shows clay, compute $Q_v$ and
   $\sigma_s$ and check whether $\sigma - \sigma_s$ is positive and larger than
   its own error. If not, stop: no saturation is recoverable.
4. **Exponent calibration:** demand $m$ from core or logs. Test
   $\phi$-apparent at several porosities; if $m$ fitted from one sample is used
   elsewhere, the answer inherits the $1/m$ amplification.
5. **Falsification test:** if the computed $S_w$ exceeds 1, or if the surface
   term is more than about half the total conductivity, the Archie assumption is
   falsified and the number must not be reported as a saturation.
6. **Independent check:** NMR or a second EM method for water content; the
   falsification criterion is agreement of the two within their stated errors.
