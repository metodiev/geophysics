# Solutions — 04-07-02 Volcanic Hazards, Monitoring and Precursors

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — The pressurised cavity and its Mogi equivalent

**(a)** $u_r(a) = a\Delta P/(4\mu) = 500\times2\times10^7/(4\times2.5\times10^{10})
= 0.100$ m, and
$\Delta V = 4\pi a^2 u_r(a) = 4\pi(2.5\times10^5)(0.1) = 3.142\times10^5$ m³.

**(b)** $C = 3a^3\Delta P/(4\mu) = 3(1.25\times10^8)(2\times10^7)/(10^{11})
= 7.50\times10^4$ m³, and $C/\Delta V = 7.5\times10^4/3.1416\times10^5 = 0.2387
= 3/(4\pi)$. The two are related by $C = 3\Delta V/(4\pi)$, which is worth
memorising because it is the bridge between a volume change reported by
geodesy and a Mogi strength used in a forward model.

**(c)** $u_z(0) = C/d^2 = 7.5\times10^4/4\times10^6 = 0.01875$ m $= 18.75$ mm.
At $r = 4$ km, $u_z = Cd/(r^2+d^2)^{3/2}
= (7.5\times10^4)(2\times10^3)/(2\times10^7)^{3/2} = 1.677\times10^{-3}$ m
$= 1.68$ mm.

**(d)** Setting $r = d$ in (3) gives $u_r = Cd/(2d^2)^{3/2} = u_z$, so they are
equal at $r = d = 2$ km by construction of the model. Numerically at $r = 2$ km
both are $7.5\times10^4\times2000/(8\times10^6)^{1.5} = 6.63\times10^{-3}$ m.

---

## ★2 — Plume scaling

**(a)** $H \propto F^{1/4}$, so doubling $F$ multiplies $H$ by
$2^{1/4} = 1.189$: a 19 per cent increase.

**(b)** $1.5^4 = 5.06$, so a 50 per cent increase in height requires five times
the buoyancy flux. Note how this inverts the practical question: a height is
easy to measure, and it constrains the flux very loosely.

**(c)** The height is measured (radar, lidar, satellite, or an observer with a
theodolite). The buoyancy flux is an *inference* from the height, the wind and
an atmospheric profile, and it carries the uncertainty of all of them.

**(d)** The dimensionless constant $C$ of order unity, and the form of the
stratification that $N$ summarises. Dimensional analysis fixes the exponent
$1/4$ and nothing else.

---

## ★3 — SO₂ flux

**(a)** $\Phi = 5\times10^{-4} \times 8 \times 2000 = 8.0$ kg s⁻¹.

**(b)** $8.0 \times 86400/1000 = 691$ t d⁻¹.

**(c)** The wind speed is normally taken from a numerical weather model, not
measured in the plume. It enters the flux linearly, so a 30 per cent wind error
is a 30 per cent flux error, and the concentration derived from the same image
contributes its own correlated error. The honest statement of a flux therefore
includes the wind source and a range, not a single number.

---

## ★4 — A precursor, quantified

**(a)** $P = \dfrac{0.8\times0.02}{0.8\times0.02 + 0.1\times0.98}
= \dfrac{0.016}{0.016+0.098} = 0.140$.

**(b)** $f = \dfrac{sp(1-P^*)}{P^*(1-p)}
= \dfrac{0.8\times0.02\times0.1}{0.9\times0.98} = 0.01814$, i.e. one false alarm
per 55 quiet intervals.

**(c)** $f = \dfrac{0.8\times0.02\times0.01}{0.99\times0.98} = 1.65\times10^{-4}$,
one false alarm per 6060 quiet intervals.

**(d)** Sensitivity is measured from eruptions the observatory has seen, whereas
the false-alarm rate requires a long and equally careful record of intervals in
which nothing happened, and that record is the one nobody keeps.

---

## ★★5 — Running the Mogi section

**(a)** Wall displacement $0.083333$ m; cavity volume change
$1.047198\times10^6$ m³; Mogi strength $2.500000\times10^5$ m³; ratio $C/\Delta V
= 3/(4\pi) = 0.238732$.

**(b)** Maximum uplift $27.7778$ mm = 0.027778 m. $u_r = u_z$ at $r = 3.000$ km
$= d$, where both are $9.8209$ mm.

**(c)** The tilt peak is at $r = 1.5000$ km $= d/2$, with peak tilt
$7.950464\times10^{-6}$ rad $= 7.950$ µrad.

**(d)** With $C$ fixed at $2.5\times10^5$ m³ and the depth increased by a
factor of 2 from 3 km to 6 km:

- $u_z(0) = C/d^2$ falls by $2^2 = 4$: from 27.778 mm to **6.944 mm**.
- The peak tilt is $\tfrac{3}{2}Cd(d/2)/(5d^2/4)^{5/2}$, which simplifies to
  $0.8587\,C/d^3$, so it falls by $2^3 = 8$: from 7.950 µrad to
  **0.994 µrad**.

The same two exponents describe the ★1 case, where the depth increased by a
factor of 3 and the uplift and tilt fell by 9 and 27. Both scalings follow from
(3) and (4) with no new physics, and the contrast between them is the reason a
tiltmeter is a *shallow*-source instrument while a GNSS array, which measures
displacement, holds up better for a deep source. Inverting a sparse network for
a source that is both deeper and weaker therefore degrades very rapidly.

---

## ★★6 — Microgravity and depth

**(a)** At 3 km: $9.319\times10^{-6}$ m s⁻² $= 0.932$ mGal. At 5 km:
$3.355\times10^{-4}$ mGal $= 335$ µGal. At 10 km: $8.387\times10^{-5}$ mGal
$= 83.9$ µGal.

**(b)** With $\Delta g = GV\Delta\rho/d^2$ and $V = 4.189\times10^9$ m³,
$\Delta\rho = \Delta g\,d^2/(GV)
= (10^{-6})(2.5\times10^7)/(6.674\times10^{-11}\times4.189\times10^9)
= 89.4$ kg m⁻³.

**(c)** The signal falls as $1/d^2$ while the noise floor is fixed, so the depth
range over which an intrusion of a given density contrast is detectable is set
by the survey precision, not by the survey design. (b) shows the trade: at 5 km
it takes an 89 kg m⁻³ density change to make 100 µGal, which is a large
fraction of a plausible magma–host contrast.

**(d)** $d = \sqrt{GV\Delta\rho/\Delta g} = \sqrt{83.87/5\times10^{-8}}
= 4.1\times10^4$ m $\approx 41$ km — far deeper than any magma chamber, so the
limitation is not the gravimeter.

---

## ★★7 — Posteriors, and the value of no signal

| $p$ | $s$ | $f$ | $P(\text{erupt}\mid\text{precursor})$ |
|---|---|---|---|
| 0.001 | 0.90 | 0.05 | 0.0177 |
| 0.01 | 0.90 | 0.05 | 0.1538 |
| 0.05 | 0.95 | 0.02 | 0.7143 |

Only the third case could support an evacuation on the precursor alone: the
posterior is above one half, and even then it is a 29 per cent chance of *not*
erupting. The first row is the one to stare at: a 90 per cent sensitive
precursor at a volcano with a one-in-a-thousand annual rate raises the
probability from 0.1 to 1.8 per cent. The precursor is real, the physics behind
it is real, and the number it produces is not actionable.

For the absence of the precursor, with $p = 0.01$, $s = 0.9$, $f = 0.05$:

$$P(\text{erupt}\mid\text{no precursor})
= \frac{(1-s)p}{(1-s)p + (1-f)(1-p)}
= \frac{0.001}{0.001+0.9405} = 0.00106 .$$

So the absence of the precursor *reduces* the probability ninefold, from 1 per
cent to 0.11 per cent. This is the part of monitoring that is easiest to
justify and least often advertised: a negative result from a sensitive
instrument is a strong statement, for exactly the same arithmetic reason that a
positive one is weak. A monitoring programme that keeps its quiet-interval
records can make that statement quantitatively; one that does not cannot.

---

## ★★★8 — Discriminating mass change from volume change

**(a)** For a Mogi source with cavity volume change $\Delta V$ at depth $d$,
$C = 3\Delta V/(4\pi)$ and

$$u_z(0) = \frac{C}{d^2} = \frac{3\Delta V}{4\pi d^2}.$$

The gravity change from a compact mass of density contrast $\Delta\rho$
occupying the same volume at the same depth is $\Delta g = GV\Delta\rho/d^2$.
Their ratio is

$$\frac{\Delta g}{u_z} = \frac{4\pi G \Delta\rho}{3}, \tag{S-1}$$

which contains **no depth** and no volume. That is the whole point: the ratio of
a gravity change to an uplift measures the density contrast of whatever changed,
independently of where it is or how big it is.

**(b)** $4\pi G/3 = 2.796\times10^{-10}$ (m s⁻²) per metre of uplift per
kg m⁻³, i.e. $27.96$ µGal m⁻¹ per 1000 kg m⁻³. So:

- Hypothesis A, $\Delta\rho = +300$: **8.39 µGal per metre of uplift**.
- Hypothesis B, $\Delta\rho = -100$: **−2.80 µGal per metre of uplift**.

**(c)** For $u_z = 0.15$ m: A gives $+1.26$ mGal and B gives $-0.42$ mGal. The
signs differ, which is the observable content: new magma adds mass and increases
gravity; gas expansion adds volume and removes mass.

**(d)** A joint deformation–gravity measurement therefore distinguishes
"new material" from "same material, larger volume", which is precisely the
question a hazard assessment needs answered, because gas-driven unrest can lead
to an explosive eruption from magma that arrived years earlier. The diagnostic
breaks if the mass change is not compact and at the same depth as the volume
change (a sill, a dyke, or a distributed density change), if the deformation
source is not spherical, or if the host rock's elastic properties vary enough
between the two depths that a single $G$ and $\mu$ are not defensible. In
practice (S-1) is used as a *scatter plot gradient* over a long time series,
which is more robust than a single ratio.

---

## ★★★9 — How long does it take to measure a false-alarm rate?

**(a)** For a binomial proportion the standard error is
$\sqrt{f(1-f)/n}$, so $n = f(1-f)/\mathrm{se}^2$:

- $\mathrm{se} = 0.005$: $n = 0.05\times0.95/2.5\times10^{-5} = 1900$ intervals.
- $\mathrm{se} = 0.01$: $n = 0.0475/10^{-4} = 475$ intervals.

**(b)** With one interval per year, 1900 intervals is 1900 years of record. A
newly instrumented volcano will have a few decades, so it cannot measure its own
false-alarm rate to anything like the precision (11) demands for a high
posterior. It can measure a sensitivity from a handful of eruptions, which is
why sensitivity is what gets reported and the false-alarm rate is what decides.

**(c)** Pooling requires the volcanoes to be *exchangeable*: the precursor's
false-alarm behaviour must be the same at all of them, up to a known offset.
That is defensible within a volcano type with similar magma and edifice
properties and it is not defensible across types, because the false-alarm
sources differ — hydrothermal systems are noisy in the same band as volcanic
unrest, a glaciated volcano has a different seismic background, and a
silicic system has a different seismicity style from a basaltic one. If the
assumption is false, the pooled rate is a biased estimate of every individual
rate and the derived posteriors inherit a systematic error that no amount of
extra instruments on one volcano can remove.

**(d)** The most effective change is usually to add comparable instruments to
*neighbouring quiet volcanoes* rather than more instruments to the restless one:
that is what generates quiet intervals. A second effective change is to define
and record the precursor operationally — a written threshold and a written
outcome for every interval — so that the quiet intervals are scored by the same
rule as the restless ones. Both changes produce data; a fourth sensor on the
same edifice mostly produces correlation.
