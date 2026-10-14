# Solutions — 07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are **SYNTHETIC** teaching values.

Lesson: [03 Spherical Harmonic Solutions and Coefficient Interpretation](../03-spherical-harmonic-solutions.md).

Constants: $GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$R = 6371\ \mathrm{km}$, $\gamma = 9.80665\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.

---

## ★1 — One zonal coefficient at the equator

$\bar P_{20}(0) = -\sqrt{5}/2 = -1.118034$.

**Geoid.**
$$\frac{GM}{R\gamma} = \frac{3.986004418\times10^{14}}{(6.371\times10^{6})
(9.80665)} = \frac{3.986004418\times10^{14}}{6.24784\times10^{7}}
= 6.379836\times10^{6}\ \mathrm{m},$$
$$N = (6.379836\times10^{6})(2.0\times10^{-5})(-1.118034)
= -142.66\ \mathrm{m}.$$

**Gravity anomaly.**
$$\frac{GM}{R^{2}} = \frac{3.986004418\times10^{14}}{(6.371\times10^{6})^{2}}
= \frac{3.986004418\times10^{14}}{4.05896\times10^{13}}
= 9.8203\ \mathrm{m\,s^{-2}},$$
$$\Delta g = (9.8203)(2-1)(2.0\times10^{-5})(-1.118034)\ \mathrm{m\,s^{-2}}
= -2.19587\times10^{-4}\ \mathrm{m\,s^{-2}} = -21.96\ \mathrm{mGal}.$$

**Units:** $GM/(R\gamma)$: $\mathrm{m^{3}\,s^{-2}}/(\mathrm{m}\cdot
\mathrm{m\,s^{-2}}) = \mathrm{m}$ ✔ (a length times a dimensionless
coefficient). $GM/R^{2}$: $\mathrm{m^{3}\,s^{-2}}/\mathrm{m^{2}} =
\mathrm{m\,s^{-2}}$ ✔.

**Note the sign and the factor $2$:** the same coefficient gives $+142.66\
\mathrm{m}$ at the pole and $-142.66\ \mathrm{m}$ at the equator, because
$\bar P_{20}$ changes sign; the anomaly changes sign with it. A "geoid high" at
one place is a "geoid low" at the other, from one number.

---

## ★2 — Information budget at $L = 75$

$$N_{\text{coef}} = (L+1)^{2} = 76^{2} = 5776 ,\qquad
\lambda_{1/2} = \frac{\pi R}{L} = \frac{\pi(6371)}{75} = 266.9\ \mathrm{km}.$$

**Why $L^{2}$ against $1/L$:** at degree $l$ there are $2l+1$ coefficients, so
the cumulated count up to $L$ is $\sum_{l=0}^{L}(2l+1) = (L+1)^{2}$ — quadratic.
The spatial scale of degree $l$ is $2\pi R/l$, so the *resolution* improves only
as $1/L$: doubling the resolution quadruples the parameter count. In an inversion
that means the ratio of unknowns to independent data grows without bound unless
the data also grow, which is why every high-degree solution needs
regularisation.

---

## ★3 — Dimensional analysis

$$\left[\frac{GM}{R\gamma}\right]
= \frac{\mathrm{m^{3}\,s^{-2}}}{\mathrm{m}\cdot\mathrm{m\,s^{-2}}}
= \frac{\mathrm{m^{3}\,s^{-2}}}{\mathrm{m^{2}\,s^{-2}}} = \mathrm{m}\ \checkmark$$

$$\left[\frac{GM}{R^{2}}C_{lm}\right]
= \mathrm{m\,s^{-2}}\cdot 1 = \mathrm{m\,s^{-2}}\ \checkmark$$

Both are consistent with $N$ a length and $\Delta g$ an acceleration. A useful
corollary: since $C_{lm}$ is dimensionless, the *same* coefficient produces a
geoid undulation of order $10^{7}C_{lm}$ metres and an anomaly of order
$10\ \mathrm{m\,s^{-2}}C_{lm}$ — a good order-of-magnitude check before any
computation.

---

## ★4 — Deriving the $(l-1)$ factor

Write a single degree of the disturbing potential, using the radial solution of
Laplace's equation, as

$$T_{l}(r) = \frac{GM}{r}\left(\frac{R}{r}\right)^{l}f_{l}(\theta,\phi)
= GM\,R^{l}\,r^{-(l+1)}f_{l}(\theta,\phi),$$

where $f_{l}$ contains the angular functions and coefficients. Then

$$\frac{\partial T_{l}}{\partial r} = -(l+1)\,GM\,R^{l}\,r^{-(l+2)}f_{l}
= -\frac{l+1}{r}\,T_{l},$$

and substituting into the **fundamental equation of physical geodesy** at
$r = R$,

$$\Delta g_{l} = -\frac{\partial T_{l}}{\partial r} - \frac{2T_{l}}{r}
= \frac{(l+1)T_{l}}{r} - \frac{2T_{l}}{r}
= \frac{(l-1)}{r}T_{l}
= \frac{GM}{R^{2}}(l-1)\left(\frac{R}{r}\right)^{l}f_{l}. \qquad\blacksquare$$

**Boundary condition used:** the gravity anomaly is defined on the reference
surface (here $r = R$), and the potential is continued there from the satellite
altitude. The $l+1$ comes from differentiating $r^{-(l+1)}$; the $-2$ comes from
the *definition* of the anomaly, which subtracts the normal field along with the
change of its own gradient with height. The two together give $l-1$.

**Dimensional check:** $(l-1)T_{l}/r$ has units
$\mathrm{m^{2}\,s^{-2}}/\mathrm{m} = \mathrm{m\,s^{-2}}$ ✔.

**Sanity:** at $l = 1$ the factor vanishes — a dipole term is a translation of
the origin, not a gravity anomaly, which is another reason degree 1 is set to
zero by convention.

---

## ★5 — Crossover degree for the stated error spectrum

Set $\sigma_{l} = \epsilon_{l}$:

$$10^{-5}\left(\frac{2}{l}\right)^{2} = 3.0\times10^{-9}l^{1/2}
\;\Longrightarrow\; \frac{4.0\times10^{-5}}{l^{2}}
= 3.0\times10^{-9}l^{1/2}
\;\Longrightarrow\; l^{2.5} = \frac{4.0\times10^{-5}}{3.0\times10^{-9}}
= 1.3333\times10^{4}.$$

Take logarithms: $\ln l = \dfrac{\ln(1.3333\times10^{4})}{2.5}
= \dfrac{9.4980}{2.5} = 3.7992$, so $l = 44.7$.

The highest **integer** degree with signal above noise is $l = 44$, and

$$\lambda_{1/2} = \frac{\pi(6371)}{44} = 455\ \mathrm{km}.$$

**What lies above it:** coefficients at $l > 44$ are not determined by these data
to this accuracy. If a solution reports them, they are supplied by the a priori
spectrum, the damping, or another data type — and the report should say which.
(This is the lesson's "the regularisation writes the high degrees" in numbers.)

---

## ★6 — Which difference is a data difference?

The signal spectrum falls roughly as $l^{-2}$ in amplitude while the error
spectrum at best stays constant or grows, so the *ratio* of signal to error drops
steeply with degree. Therefore:

- At **degree 15** the signal-to-noise ratio is high for both analyses, and a
  $2\%$ difference between two independent solutions is a difference in the
  measurements (data weighting, tracking type, processing choices).
- At **degree 120** the solution is near or beyond the crossover for at least one
  analysis; a $40\%$ difference there is likely dominated by the two
  regularisations and by the different a priori spectra.

**The one report item that settles it:** the **error covariance (or the
signal-to-noise ratio per degree)** of each solution. If the two error spectra
overlap at degree 120, the difference is not significant; if both claim small
errors yet differ by $40\%$, the regularisation is mis-specified or the
covariance is wrong, and the difference is a modelling discrepancy rather than a
measurement discrepancy. Reporting a coefficient without its error is what makes
this question unanswerable.

---

## ★7 — Demonstrating that regularisation writes the high degrees

A specification that could be executed:

1. **Truth.** A synthetic coefficient set from a stated power-law spectrum with a
   different smooth realisation at each seed (e.g. $\sigma_{l} = 10^{-5}(2/l)^{2}$
   as in the lesson).
2. **Forward operator.** A tall, ill-conditioned matrix $G$ representing, say,
   $5\times10^{5}$ synthetic range-link observations at $\sim 200\ \mathrm{km}$
   separation computed from the truth through the $(R/a)^{l}$ attenuation — with
   additive Gaussian noise at a stated level. The condition number of $G$ should
   be reported.
3. **Regularisation family.** Tikhonov with an a priori spectrum constraint:
   minimise $\|Gm - d\|^{2} + \lambda\|m - m_{\text{apriori}}\|^{2}_{\Sigma^{-1}}$.
4. **Sweep.** $\lambda$ over, say, six decades; at each $\lambda$ record
   (a) the data misfit, (b) the error *relative to the truth* per degree,
   (c) the value of $\lambda$ that the discrepancy principle would choose.
5. **Diagnostic.** Plot the per-degree *truth-minus-recovered* error against
   degree for each $\lambda$. **Prediction:** the curves fan out above the
   crossover degree $l^{*}$ of Section 5, and above $l^{*}$ the recovered
   coefficients track the *a priori* spectrum rather than the truth — visible as
   a recovered spectrum whose shape is that of $m_{\text{apriori}}$ regardless of
   the truth's realisation.
6. **Second diagnostic.** Re-run with two different seeds for the truth's high
   degrees but the same a priori model: if the recovered high degree coefficients
   are nearly identical between the two runs, they cannot be tracking the data.
   That is the decisive test.

**A failed specification** would be one that only reports the misfit as a
function of $\lambda$: the misfit is minimised by fitting noise, so it cannot
reveal the regularisation bias.

---

## ★8 — The effect of a latitude-varying $\gamma$

Normal gravity varies between the stated synthetic extremes:

$$\gamma_{0} = 9.7803,\qquad \gamma_{90} = 9.8322\ \mathrm{m\,s^{-2}},
\qquad
\frac{\Delta\gamma}{\gamma} = \frac{9.8322 - 9.7803}{9.80665} = 5.30\times10^{-3}.$$

Since Bruns' formula is $N = T/\gamma$, a relative error $\delta$ in $\gamma$
gives a relative error $-\delta$ in $N$:

$$\left|\frac{\delta N}{N}\right| = 5.3\times10^{-3}.$$

For a geoid undulation of $N = 100\ \mathrm{m}$ the error is $0.53\ \mathrm{m}
= 53\ \mathrm{cm}$ — **two orders of magnitude larger than a $1\ \mathrm{cm}$
target**. Even a $10\ \mathrm{m}$ undulation would be biased by $5\ \mathrm{cm}$.

**What an analyst must therefore do:**
1. Use a latitude-dependent normal gravity formula, or the ellipsoidal
   generalisation of Bruns' formula, rather than one global mean value.
2. Note that the difference is not random but a smooth function of latitude, so
   it appears as a spurious North–South tilt in the geoid — the worst possible
   error for a height system, because it is systematic and correlates with the
   levelling network geometry.
3. Include the normal-gravity model choice in the list of things a geoid model
   depends on, alongside the coefficients, the terrain mass model and the
   integration cap. A geoid is a *model*, and this is one of its assumptions.
