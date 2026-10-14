# Solutions — 14-03-02 Archie's Law and Saturation Estimation

> Read after attempting. Lesson:
> [02 Archie's Law and Saturation Estimation](../02-archie-and-saturation.md).
> All models **SYNTHETIC**; $a = 1.00$, $m = 2.00$, $n = 2.00$ unless stated.

---

## ★1 — Formation factor

$$F = \frac{a}{\phi^{m}} = \frac{1}{0.22^{2}} = \frac{1}{0.0484} = 20.66 .$$

$F$ is a ratio of two resistivities, hence dimensionless. $a$ is dimensionless,
$\phi$ is dimensionless and $m$ is dimensionless, so the right-hand side is
dimensionless. The unit check matters because a formula written
$F = a\phi^{m}$ looks identical on a page and is wrong by $\phi^{2m}$.

---

## ★2 — Saturation from a resistivity

$$\rho_0 = \frac{a\rho_w}{\phi^{m}} = \frac{1.00\times1.50}{0.30^{2}}
= \frac{1.50}{0.09} = 16.667\ \Omega\,\mathrm{m}.$$

$$I = \frac{\rho_t}{\rho_0} = \frac{30.0}{16.667} = 1.8000, \qquad
S_w = I^{-1/n} = 1.8000^{-0.5} = 0.7454 .$$

Directly: $S_w = (a\rho_w/(\phi^{m}\rho_t))^{1/2}
= (1.50/(0.09\times30.0))^{1/2} = (0.5556)^{1/2} = 0.7454$.

**Answer.** $S_w = 0.75$, assuming a clean matrix, $a = 1$, $m = 2$, $n = 2$ and
a pore fluid of $1.50\ \Omega\,\mathrm{m}$.

---

## ★3 — Resistivity index

$$I = S_w^{-n} = 0.60^{-2} = \frac{1}{0.36} = 2.778 .$$

$I > 1$ means the partially saturated rock is **more** resistive than the same
rock fully saturated, because the non-wetting phase (air or gas) is an insulator
and removes conducting fluid from the current path. This monotonic direction is
the entire content of the saturation law; its size is what $n$ controls.

---

## ★★4 — Elasticity of $S_w$ with respect to porosity

$$S_w = \left(\frac{a\rho_w}{\phi^{m}\rho_t}\right)^{1/n}
\;\;\Longrightarrow\;\;
\ln S_w = \frac{1}{n}\left(\ln a + \ln\rho_w - m\ln\phi - \ln\rho_t\right).$$

Differentiating with respect to $\ln\phi$ at fixed $\rho_t$:

$$\frac{\partial\ln S_w}{\partial\ln\phi} = -\frac{m}{n} = -\frac{2}{2} = -1.000 .$$

A $5\%$ porosity error gives a $-5\%$ saturation error in the opposite
direction: an over-estimated porosity makes the rock look under-saturated.
Note how the exponents divide: $m$ inflates the porosity sensitivity and $n$
deflates it, so a rock with $n = 1.5$ would have a porosity elasticity of
$-1.33$ and a rock with $n = 3$ only $-0.67$.

---

## ★★5 — Clay conduction

**(a)** Archie pore-water path:
$\sigma_\text{pore} = \phi^{m}S_w^{n}/(a\rho_w)
= 0.28^{2}\times0.50^{2}/(1.00\times2.50)
= 0.0784\times0.25/2.50 = 0.007840\ \mathrm{S\,m^{-1}}$.

Total: $\sigma_t = 0.007840 + 0.020 = 0.027840\ \mathrm{S\,m^{-1}}$, so

$$\rho_t = \frac{1}{0.027840} = 35.92\ \Omega\,\mathrm{m}.$$

**(b)**

$$S_w^\text{Archie} = \left(\frac{a\rho_w}{\phi^{m}\rho_t}\right)^{1/n}
= \left(\frac{2.50}{0.0784\times35.92}\right)^{1/2}
= \left(\frac{2.50}{2.8161}\right)^{1/2} = 0.9422 .$$

The measured value $0.94$ against a truth of $0.50$: the clay path is carrying
most of the current, and Archie attributes all of it to pore water.

**(c)** For Archie to return exactly $S_w = 1$ the measured resistivity must be
$\rho_0 = a\rho_w/\phi^{m} = 2.50/0.0784 = 31.888\ \Omega\,\mathrm{m}$, i.e.
$\sigma_t = 0.031360\ \mathrm{S\,m^{-1}}$. The pore path supplies
$0.007840\ \mathrm{S\,m^{-1}}$, so

$$\sigma_\text{clay} = 0.031360 - 0.007840 = 0.023520\ \mathrm{S\,m^{-1}} .$$

**Interpretation.** At exactly this clay conductance the error is invisible in
the rule "if $S_w > 1$, suspect clay": the answer sits precisely on the
boundary and would be read as "fully saturated, clean rock". The $S_w > 1$
diagnostic is therefore a one-sided test with a blind spot at its own threshold —
which is why shaly-sand models are calibrated rather than inferred.

---

## ★★6 — An impossible saturation

**(a)**

$$S_w = \left(\frac{2.50}{0.0784\times15.0}\right)^{1/2}
= \left(\frac{2.50}{1.1760}\right)^{1/2} = (2.1258)^{1/2} = 1.4580 .$$

**(b)** The physical maximum is $S_w = 1$, at
$\rho_0 = 31.888\ \Omega\,\mathrm{m}$. Any measured resistivity below that value
is inadmissible *under the model*, so the admissible range of the model is
$\rho_t \geq 31.888\ \Omega\,\mathrm{m}$ **for these fixed parameters**.

**(c)** Two explanations and the discriminating measurement.

1. **Clay conduction.** The pore fluid is not the only conductor. Discriminated
   by a clay indicator: natural gamma or a neutron–density clay estimate, or a
   laboratory measurement of the cation exchange capacity on a sample.
2. **A wrong pore-fluid resistivity (too low $\rho_w$).** A saltier fluid than
   assumed lowers every predicted value. Discriminated by a direct fluid sample
   or an independent salinity measurement.

A third possibility, a wrong cementation exponent, is discriminated by an
independent porosity from NMR or from a core measurement. Note that the
measurement to acquire is never more of the same resistivity.

---

## ★★7 — The $(\phi, \text{salinity})$ ambiguity table

With $\rho_t = 50.0\ \Omega\,\mathrm{m}$ and $S_w = 0.7986$,
$\rho_w = a\rho_t\phi^{m}S_w^{n} = 50.0\,\phi^{2}\times0.6378$, then
$C = 0.60/(\rho_w - 2.00)$ where defined:

| $\phi$ | required $\rho_w$ ($\Omega$ m) | required $C$ ($\mathrm{mol\,L^{-1}}$) |
|---|---|---|
| 0.24 | 1.837 | no solution |
| 0.26 | 2.156 | 3.856 |
| 0.28 | 2.500 | 1.200 |
| 0.30 | 2.870 | 0.690 |

**Excluded end.** The low-porosity end is excluded: at $\phi = 0.24$ the
required pore-fluid resistivity, $1.837\ \Omega\,\mathrm{m}$, is below the
minimum the synthetic relation can produce ($2.00\ \Omega\,\mathrm{m}$ at
infinite concentration). This is genuinely useful information — the data have
bounded porosity from below — and it is invisible if the relation is inverted
without checking its range.

**Admitted band.** Between $\phi = 0.26$ and $\phi = 0.30$ the required salinity
falls from $3.86$ to $0.69\ \mathrm{mol\,L^{-1}}$, a factor of $5.6$. The
resistivity alone does not choose within that band.

---

## ★★★8 — The corrected estimator

**(a)** Given a calibrated $\sigma_\text{clay}$, subtract it first:

$$\sigma_\text{pore} = \sigma_t - \sigma_\text{clay}
\;\;\Longrightarrow\;\;
\boxed{\;S_w = \left(\frac{a\,\rho_w\,\sigma_\text{pore}}{\phi^{m}}\right)^{1/n}
= \left(\frac{a\,\rho_w}{\phi^{m}}\left(\sigma_t - \sigma_\text{clay}\right)
\right)^{1/n} .}$$

**(b)** Setting $\sigma_\text{clay} = 0$ gives
$S_w = (a\rho_w\sigma_t/\phi^{m})^{1/n}
= (a\rho_w/(\phi^{m}\rho_t))^{1/n}$, which is Archie.

**(c)** With $\sigma_t = 0.027840$, $\sigma_\text{clay} = 0.020$:

$$\sigma_\text{pore} = 0.007840,\qquad
S_w = \left(\frac{2.50\times0.007840}{0.0784}\right)^{1/2}
= (0.2500)^{1/2} = 0.5000 .$$

The corrected value is $0.5000$ against a truth of $0.50$ — exact, as it must be
because the same model generated the datum. The uncorrected Archie value was
$0.9422$. The correction is therefore worth a factor of $1.88$ here, and it
removes the entire bias.

**(d)** The correction is exact only when $\sigma_\text{clay}$ is exact. The
sensitivity is

$$\frac{\partial \sigma_\text{pore}}{\partial \sigma_\text{clay}} = -1,$$

so an absolute error in $\sigma_\text{clay}$ of $0.001\ \mathrm{S\,m^{-1}}$
is an absolute error in $\sigma_\text{pore}$ of the same size — against a
$\sigma_\text{pore}$ of only $0.007840$, that is a $13\%$ relative error and
$\partial S_w/S_w = (1/n)\times13\% = 6.4\%$. Since
$\sigma_\text{clay}$ depends on the clay type, its cation exchange capacity and
the pore-fluid salinity, and is normally calibrated from cores with an error of
tens of per cent, the corrected saturation usually carries a larger uncertainty
than the uncorrected one — while being much better centred. Report the bias
removed *and* the variance added.

---

## ★★★9 — Separating $n$ from $S_w$ (model answer)

**(a)** An independent saturation measurement is unavoidable. Resistivity gives
one number; $S_w$ and $n$ are two unknowns, and no manipulation of a single
resistivity separates them. The independent measurement can be a laboratory
desaturation on cores, an NMR free-fluid index, a neutron log with a porosity
calibration, or a tracer-derived saturation.

**(b)** **Experiment.** On representative cores, hold $\phi$, $\rho_w$ and the
effective stress fixed; measure $\rho_t$ at five or more imposed saturations
$S_w$ set gravimetrically; plot $\log I$ against $\log S_w$. The slope is $-n$
and the intercept should be zero. Check the intercept: a non-zero intercept means
a conductive matrix, and the dataset must be discarded or modelled with the
parallel-conduction form of ★8 rather than fitted with Archie.

**(c)** **Non-transfer.** $n$ is known to depend on the saturation *history*
(drainage versus imbibition) and on the wettability of the pore surfaces, both of
which a laboratory plug can be made to represent only by choosing the right
protocol. A laboratory $n$ measured on a strongly water-wet sample under primary
drainage need not describe a field interval that has been through repeated
imbibition. **Detection from field data alone:** a saturation profile that
requires $S_w$ to be non-monotonic with depth, or to exceed 1 anywhere, or to
change discontinuously where the lithology does not, indicates that $n$ is wrong.
A second, independent indication is a saturation inverted with two different
assumed $n$ values whose profiles cross at a depth; the crossing point is a
lithology boundary, not physics.
