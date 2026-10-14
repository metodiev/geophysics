# Solutions — 15-05-01 Coastal Processes, Sediment Transport and Shoreline Change

> **Read after attempting the exercises.** Lesson:
> [01 Coastal Processes](../01-coastal-processes.md). Numbers are SYNTHETIC model
> values.

## ★ Foundational

## ★1 — Dispersion at $T=8$ s, $h=8$ m

$\omega=2\pi/8=0.78540\ \mathrm{rad\,s^{-1}}$. Solving
$gk\tanh(kh)=\omega^2$ gives

$$k=0.0968\ \mathrm{m^{-1}},\qquad L=2\pi/k=64.89\ \mathrm{m},\qquad
kh=0.7746,$$

$$c=\omega/k=8.111\ \mathrm{m\,s^{-1}},\qquad c_g=6.851\ \mathrm{m\,s^{-1}} .$$

Limits: $\sqrt{gh}=8.857\ \mathrm{m\,s^{-1}}$ (the phase speed is **8.4% below**
it) and $gT/2\pi=12.486\ \mathrm{m\,s^{-1}}$ (35% above it). The wave is
intermediate: $kh=0.77$ is not small, so neither limit is accurate, which is why
the dispersion relation has to be solved rather than approximated.

## ★2 — Shoaling at 5 m depth

$$H=H_0\sqrt{\frac{c_{g0}}{c_g}}=2.5\sqrt{\frac{7.804}{6.325}}
=2.5\times1.1108=2.777\ \mathrm{m}.$$

The amplification is 11.1%. Note it is *smaller* than the amplification at
breaking (17.7% for the lesson's 2.5 m, 10 s wave), because the group velocity
continues to fall toward shore.

## ★3 — Bruun retreat and volume

$$R=\frac{S}{\tan\beta}=\frac{0.004}{0.015}=0.2667\ \mathrm{m\,yr^{-1}}
=26.7\ \mathrm{cm\,yr^{-1}},$$

$$\text{volume}=S\frac{h_c}{\tan\beta}
=0.004\times\frac{12}{0.015}=0.004\times800=3.2\ \mathrm{m^3\,yr^{-1}}$$

per metre of shoreline. The closure depth scales the volume but not the retreat —
the single most useful thing to remember about this pair of formulas.

## ★★ Applied

## ★4 — Longshore energy flux and transport

$$P=\frac{\rho g^{3/2}}{8\sqrt{\gamma}}H_b^{5/2}
=\frac{1030\times30.712}{8\times0.8832}\times1.5^{2.5}
=\frac{31633}{7.0657}\times2.7557=12\,337\ \mathrm{W\,m^{-1}},$$

$$P_{ls}=\tfrac12P\sin 2\alpha_b=0.5\times12\,337\times\sin16^\circ
=0.5\times12\,337\times0.27564=1\,700\ \mathrm{W\,m^{-1}},$$

$$\rho g(s-1)(1-p)=1030\times9.80665\times1.5728\times0.60
=9\,532\ \mathrm{J\,m^{-3}},$$

$$Q=\frac{0.39\times1700}{9532}=0.06955\ \mathrm{m^3\,s^{-1}}
=2.195\times10^{6}\ \mathrm{m^3\,yr^{-1}} .$$

## ★5 — Shoreline change from a gradient

$$\frac{\mathrm{d}y}{\mathrm{d}t}=-\frac{1}{h_c}\frac{\partial Q}{\partial x}
=-\frac{2}{12}=-0.1667\ \mathrm{m\,yr^{-1}}=-16.7\ \mathrm{cm\,yr^{-1}},$$

an **erosion** rate (the transport increases in the direction of positive $x$, so
sediment is exported). It is 63% of the 26.7 cm/yr Bruun retreat of ★3 and in the
same direction if the two add: **the two mechanisms are of comparable size at this
site**, which is the lesson's central practical point. Reporting the 40 cm/yr
total as "sea-level-driven retreat" would overstate the sea-level term by more
than a factor of two.

## ★6 — Closing the budget

Balance: $\text{in}-\text{out}=\Delta\text{storage}$; with steady storage,

$$1.20+0.10+0.03-0.95-0.05-L_{\text{offshore}}=0
\;\Rightarrow\;L_{\text{offshore}}=0.33\times10^{6}\ \mathrm{m^3\,yr^{-1}} .$$

If an independent measurement shows the offshore loss to be $0.05\times10^{6}\
\mathrm{m^3\,yr^{-1}}$, then the budget's residual is
$0.33-0.05=0.28\times10^{6}\ \mathrm{m^3\,yr^{-1}}$, i.e. **a 24% closure error**
relative to the 1.20 unit input. That residual is not noise to be distributed among
the other terms: it means one of them is wrong by 24%, and the standard practice is
to report the closure error and the term most likely to be responsible (here the
longshore output, which is itself a modelled transport with a $H^{5/2}$ dependence).

## ★★★ Research-oriented

## ★7 — Detecting 3 cm/yr in five years

**Signal.** Over five years, 3 cm/yr accumulates to 0.15 m. With a single-position
uncertainty of $\sigma=0.5\ \mathrm{m}$ and independent surveys, the standard error
of the change from $n$ surveys is approximately $\sigma\sqrt{2/n}$ (the difference
of two means of $n/2$ surveys each, or equivalently the formal error of a linear
fit over the period). Requiring

$$\sigma\sqrt{2/n}\le\frac{0.15}{2}=0.075\ \mathrm{m}$$

(the $2\sigma$ detection threshold means the *threshold* is $2\sigma_{\text{change}}$,
so the change must exceed $4\sigma_{\text{change}}$ for a nominal detection; taking
$2\sigma=0.075$ gives a conservative requirement)

$$n\ge 2\left(\frac{0.5}{0.075}\right)^{2}=2\times44.4=89\ \text{surveys}.$$

That is one survey every three weeks for five years per profile — which shows that
the *requirement as stated cannot be met by 0.5 m-precision profiles.* The honest
answers are to (i) use a better horizontal reference (RTK-GNSS or a fixed
benchmark network rather than a float-based survey), (ii) measure *profiles*
rather than instantaneous shorelines so that the same datum is differenced, or
(iii) lengthen the observation period. With a 0.1 m precision (achievable with
RTK-GNSS profiles tied to bedrock) the count falls to
$n\ge2(0.1/0.075)^2=3.6$, i.e. **four surveys in five years**, which is a normal
coastal-monitoring cadence.

**Neglected dominant error:** vertical datum and land motion. A 2 mm/yr benchmark
subsidence over five years is 10 mm — comparable to the signal — and any vertical
reference change enters the shoreline position directly. The neglected term is
usually larger than the random survey error, so a design without a repeated
levelling/GNSS tie is uninterpretable.

**Design:** at least four profile surveys spread through the period (not clustered
at the ends), each tied to the same stable GNSS/levelling network, with the
foreshore profile measured to the closure depth or to the limit of wading, and the
data reduced to a common vertical datum. Report the rate with the datum-uncertainty
term quoted separately.

## ★8 — Two stretches, one sea level

**(a)** Bruun retreat with $S=0.0035\ \mathrm{m\,yr^{-1}}$ and
$\tan\beta=0.008$:

$$R=\frac{0.0035}{0.008}=0.4375\ \mathrm{m\,yr^{-1}}=43.75\ \mathrm{cm\,yr^{-1}}$$

for *both* stretches. Residuals: stretch A $45-43.75=+1.25\
\mathrm{cm\,yr^{-1}}$; stretch B $15-43.75=-28.75\ \mathrm{cm\,yr^{-1}}$.

**(b)** The residual is a drift-driven change,
$\mathrm{d}y/\mathrm{d}t=-\partial Q/\partial x/h_c$. Taking $h_c=10\ \mathrm{m}$
(a model choice): stretch A needs $\partial Q/\partial x=-0.0125\times10=
-0.125\ \mathrm{m^3\,yr^{-1}}$ per metre (convergent drift, slight accretion);
stretch B needs $\partial Q/\partial x=+0.2875\times10=+2.875\
\mathrm{m^3\,yr^{-1}}$ per metre (divergent, strong erosion). The divergence over
the 5 km stretch is $2.875\times5000=1.44\times10^{4}\ \mathrm{m^3\,yr^{-1}}$,
i.e. 1.4% of the lesson's $0.95\times10^{6}\ \mathrm{m^3\,yr^{-1}}$ total drift:
**a 1% alongshore change in the drift explains the entire difference between the
two stretches.**

**(c) Distinguishing a drift gradient from a slope change.** Both explanations are
testable:

| explanation | prediction | measurement |
|---|---|---|
| drift gradient | the *profile shape* is preserved; the shoreline retreats while the closure-depth limit is unchanged; the change is alongshore-coherent over the drift cell | repeated profiles to closure depth, plus a wave/drift calculation from the measured wave climate |
| $\tan\beta$ difference | the profile **shape** differs between the stretches (a steeper profile retreats less for the same rise, by construction of $R=S/\tan\beta$) | the *initial* profile slope from the first survey, and its persistence over repeats |

The discriminating measurement is the profile geometry itself: a drift gradient
moves the whole active profile landward without changing its slope, whereas a
slope difference is visible in the profile before any change occurs.

**The model quantity in each explanation:** in the drift explanation the modelled
quantities are the closure depth $h_c$ and the CERC coefficient $K$; in the slope
explanation it is $\tan\beta$ as the "active-profile slope" (itself a choice,
because it depends on the depth range over which it is averaged) and the
translation assumption of the Bruun rule. Neither explanation can be tested
without a model, and that is the honest conclusion.
