# Solutions — 11-06-03 Buried Objects, UXO Detection and Clearance

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [03 Buried Objects, UXO Detection and Clearance](../03-buried-objects-uxo.md).

---

## ★1 — Magnetic moment

$$ m = M V = M\frac{4}{3}\pi R^{3}
= 800\times\frac{4}{3}\pi(0.15)^{3}
= 800 \times 1.4137\times10^{-2} = 11.31\ \mathrm{A\,m^{2}}. $$

---

## ★2 — On-axis dipole field

$$ B_z = 2\times10^{-7}\frac{m}{z^{3}}: $$

| $z$ (m) | $B_z$ (nT) |
|---|---|
| 0.5 | $2\times10^{-7}(11.31)/0.125 = 1.81\times10^{4} = 18095.6$ |
| 1.0 | $2261.9$ |
| 2.0 | $282.7$ |

Each doubling of depth divides the anomaly by 8 — the $z^{-3}$ dipole falloff.
Stated in nT, because $1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$.

---

## ★3 — GPR apex and offset time

$$ t(0) = \frac{2z}{v} = 12.0\ \mathrm{ns}
\;\Longrightarrow\;
z = \frac{v\,t(0)}{2} = \frac{0.10 \times 12.0}{2} = 0.60\ \mathrm{m}. $$

$$ t(0.5) = \frac{2\sqrt{0.5^{2}+0.6^{2}}}{0.10}
= \frac{2(0.7810)}{0.10} = 15.62\ \mathrm{ns}. $$

---

## ★4 — POD depths

$$ z_{50} = \left(\frac{2\times10^{-7}(11.31)}{2.0\times10^{-9}}\right)^{1/3}
= \left(1.131\times10^{6}\right)^{1/3} = 10.42\ \mathrm{m}. $$

For 90%: the required anomaly is $T + 1.2816\sigma = 2.0 + 1.2816 = 3.2816\
\mathrm{nT}$:

$$ z_{90} = \left(\frac{2\times10^{-7}(11.31)}{3.2816\times10^{-9}}\right)^{1/3}
= \left(6.894\times10^{5}\right)^{1/3} = 8.83\ \mathrm{m}. $$

The 90% depth is 15% less than the 50% depth: the transition is sharp, so
quoting a single "detection depth" hides which POD it belongs to.

---

## ★5 — Clearance probability

$$ P(\text{all found}) = \mathrm{POD}^{n} = 0.97^{30} = 0.401. $$

So there is a **60% chance** that at least one of the 30 objects is missed, and
the expected number missed is $30(1-0.97) = 0.90$.

This is the arithmetic behind the lesson's warning: even a 97% detection rate
does not clear a site, and the number that matters is $\mathrm{POD}^{n}$, which
falls fast with $n$.

---

## ★6 — Aperture and the velocity-depth trade

At $z = 1.0\ \mathrm{m}$ the apex time is $t(0) = 2(1.0)/0.12 = 16.67\
\mathrm{ns}$. The demonstration's deeper-target table fits a noisy hyperbola for
this case and reports, for an aperture of $\pm0.6\ \mathrm{m}$ (0.6 times the
depth):

$$ v = 0.099\text{-}0.166\ \mathrm{m\,ns^{-1}}, \qquad
z = 0.79\text{-}1.43\ \mathrm{m}. $$

That is roughly $\pm30\%$ in velocity and $\pm40\%$ in depth. Narrowing the
aperture to $\pm0.4\ \mathrm{m}$ widens it to $v = 0.085$-$0.215$ and
$z = 0.69$-$1.80$; widening it to $\pm1.5\ \mathrm{m}$ tightens it to
$v = 0.116$-$0.126$ and $z = 0.93$-$1.09$.

The trade is exact, not incidental: the apex fixes $z/v$ and the curvature fixes
$vz$, so a short aperture under-determines the pair. A wide aperture is preferred
whenever the ground allows it, because the velocity then comes from the data
rather than from an assumption about the soil — and an assumed velocity that is
20% wrong puts the target 20% wrong in depth, which matters when the specification
is in metres.

---

## ★7 — Clearance survey design (specification)

**Certification target.** Fragments of $R \ge 0.10\ \mathrm{m}$ at
$M = 1000\ \mathrm{A\,m^{-1}}$ (moment $4.19\ \mathrm{A\,m^{2}}$), to a clearance
depth of $1.0\ \mathrm{m}$.

**Instrument and noise.** A total-field magnetometer (or gradiometer) with a
$0.8\ \mathrm{nT}$ noise floor at a $1.5\ \mathrm{nT}$ threshold. From the $m^{1/3}$
law, the moment detectable at 50% at $2\ \mathrm{m}$ is

$$ m = \frac{T z^{3}}{2(\mu_0/4\pi)}
= \frac{(1.5\times10^{-9})(8)}{2\times10^{-7}} = 6.0\times10^{-2}\
\mathrm{A\,m^{2}}, $$

far below the $4.19\ \mathrm{A\,m^{2}}$ target: the instrument has margin, and the
depth resolution, not the moment, is the limit.

**Line spacing and sensor height.** Line spacing no larger than the required
positional confidence, and a sensor height of $0.3$-$0.5\ \mathrm{m}$ (or a
gradiometer to suppress the geological background). Use a gradiometer pair so the
deep regional field is removed by differencing.

**Clearance depth with POD.** Specify "clearance to $1.0\ \mathrm{m}$ depth for
objects of moment $\ge 0.06\ \mathrm{A\,m^{2}}$ at $\mathrm{POD} = 0.95$", and
state the object density assumed.

**Expected digs and residual risk.** For a stated clutter rate of
$2$ false alarms per $1000\ \mathrm{m^{2}}$ on $20\ \mathrm{ha}$:

$$ N_{\text{fa}} = 2 \times \frac{2\times10^{5}}{1000} = 400\ \text{digs}. $$

For an assumed object density of $1$ per hectare ($n = 20$),

$$ P(\text{all found}) = 0.95^{20} = 0.358, \qquad
\mathbb{E}[\text{missed}] = 20(0.05) = 1.0\ \text{object}. $$

**Largest uncertainties.** (i) The object density $n$ — it is a prior, not a
measurement, and it enters $\mathrm{POD}^{n}$ exponentially; (ii) the assumed
moment/magnetisation of the hazardous objects — the $m^{1/3}$ law makes the depth
limit move as the cube root, but a low-magnetisation or corroded object can be an
order of magnitude below the assumed value. Stating both is part of the
certification.

---

## ★8 — Correlated misses

**(1) A systematic line-spacing gap or a magnetically noisy feature.** If a
feature that suppresses detection (a metallic fence line, a pipeline, a
service trench, a conductive fill) runs across the site, every object in it is
missed together. Then the number of *independent* opportunities is not $n$ but the
number of independent regions, and $\mathrm{POD}^{n}$ should be replaced by a
per-region product, e.g. $\prod_j \mathrm{POD}_j^{n_j}$ with the noisy region's
$\mathrm{POD}_j$ much lower. The site clearance probability is then far below
$\mathrm{POD}^{n}$.

**(2) Depth-dependent detection with an unknown depth distribution.** Objects
below the POD envelope are all missed, and a cluster of objects at one depth
(a dumped load) is missed as a group. Here the effective $\mathrm{POD}$ is the
integral of the POD-versus-depth curve against the object depth distribution, and
a single number hides a bimodal reality.

**(3) A third process worth naming: operator/algorithm bias.** If the picking or
inversion is tuned to a signature (dipole-like, symmetric), then objects whose
signature is distorted — a hit item, or one overlapping another — are
systematically missed.

**Design changes that reduce correlation.** (i) Survey the same lines in
orthogonal directions, so an object lying along a line is seen on the cross
lines; (ii) re-survey anomalous or suppressed areas with a different sensor
height or a different method (EM for non-ferrous, GPR for shallow); (iii) verify
the detection by digging a stratified random *sample* of flagged locations and
using the count of missed objects to estimate the real POD for the site.

---

## Worked mastery checkpoint

**(a) Moment and radius for a 50% POD at 2 m.** With $T = 1.5\ \mathrm{nT}$
($=1.5\times10^{-9}$ T) and $z = 2\ \mathrm{m}$:

$$ m = \frac{T z^{3}}{2(\mu_0/4\pi)} = \frac{(1.5\times10^{-9})(8)}{2\times10^{-7}}
= 6.0\times10^{-2}\ \mathrm{A\,m^{2}}. $$

For $M = 1200\ \mathrm{A\,m^{-1}}$:

$$ R = \left(\frac{3m}{4\pi M}\right)^{1/3}
= \left(\frac{0.18}{4\pi(1200)}\right)^{1/3}
= (1.194\times10^{-5})^{1/3} = 2.29\times10^{-2}\ \mathrm{m} \approx 2.3\
\mathrm{cm}. $$

**(b) 90% POD depth for twice the moment** ($m = 0.12\
\mathrm{A\,m^{2}}$). The required anomaly is $T + 1.2816\sigma = 1.5 + 1.025 =
2.526\ \mathrm{nT}$:

$$ z_{90} = \left(\frac{2\times10^{-7}(0.12)}{2.526\times10^{-9}}\right)^{1/3}
= (9.50)^{1/3} = 2.12\ \mathrm{m}. $$

**(c) A $\pm0.4\ \mathrm{m}$ aperture for a target at $0.6\ \mathrm{m}$.** The
aperture is **smaller** than the depth ($0.67\times z$). By the lesson's table, an
aperture of $0.6\times$ the depth admits roughly $\pm30\%$ in velocity and
$\pm40\%$ in depth, so the admitted ranges here are of that order: the apex time
($t_0 = 2z/v = 12\ \mathrm{ns}$) is well determined, and the *pair* $(v,z)$ is
not. What is determined is the ratio $z/v$; what is not is either variable
separately.

**(d) Two hectares with 15 objects per hectare** gives $n = 30$ objects:

$$ P(\text{all detected}) = 0.9^{30} = 0.042, \qquad
\mathbb{E}[\text{missed}] = 30(0.10) = 3.0. $$

A **96% chance** that at least one object is missed, and an expectation of three
missed objects. A "clearance" claim at this POD and object density is not
supportable without stating both numbers.
