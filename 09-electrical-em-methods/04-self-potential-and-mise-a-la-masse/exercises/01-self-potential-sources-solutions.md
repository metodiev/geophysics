# Solutions — 09-04-01 Sources of Self-Potential: Electrokinetic, Electrochemical

> **Read after attempting the exercises.** Lesson:
> [01 Sources of Self-Potential](../01-self-potential-sources.md). All models
> **SYNTHETIC**.

---

## ★1 — The coupling coefficient and its conversion

$$\varepsilon = \varepsilon_r\varepsilon_0 = 80.1 \times 8.8541878128\times10^{-12}
= 7.092204\times10^{-10}\ \mathrm{F\,m^{-1}},$$

$$\frac{\partial V}{\partial P} = \frac{\varepsilon\zeta}{\eta\sigma}
= \frac{7.092204\times10^{-10} \times (-0.025)}
{1.0\times10^{-3} \times 0.020}
= \frac{-1.773051\times10^{-11}}{2.0\times10^{-5}}
= -8.865\times10^{-7}\ \mathrm{V\,Pa^{-1}}.$$

One metre of water head is
$\rho_w g = 1000 \times 9.80665 = 9806.65$ Pa, so

$$\frac{\partial V}{\partial h} = -8.865\times10^{-7} \times 9806.65
= -8.694\times10^{-3}\ \mathrm{V\,m^{-1}} = -8.694\ \mathrm{mV\ per\ m\ of\ head}.$$

For a $5.0$ mV anomaly:
$h = 5.0/8.694 = 0.575$ m of head. Note the sign: with $\zeta < 0$ the potential
*rises* in the direction of flow, so this 5 mV appears as a decrease upstream of
the flow and an increase downstream.

---

## ★2 — A standard cell

$$E^{0}_{\text{cell}} = E^{0}_{\text{cathode}} - E^{0}_{\text{anode}}
= +0.342 - (-0.762) = +1.104\ \mathrm{V}.$$

The convention: reduction potentials are quoted versus the standard hydrogen
electrode at 25 °C and unit activity, and the cell potential is the cathode
(reduction) minus the anode (oxidation). The reaction proceeds spontaneously in
the direction that makes the cell potential positive.

---

## ★3 — Membrane potentials

With $\frac{RT}{F}\ln 10 = 59.159$ mV and
$t_- = 1 - t_+$:

- $t_+ = 0.30$: $E = 59.159 \times (0.30 - 0.70) = -23.664$ mV — the medium is
  anion-selective, so the dilute side becomes positive relative to the
  concentrated side.
- $t_+ = 0.75$: $E = 59.159 \times (0.75 - 0.25) = +29.580$ mV — cation
  selective.

The maximum magnitude at one decade is $59.159$ mV, at $t_+ = 1$; the sign
changes at $t_+ = 0.5$, where the medium is unselective.

---

## ★4 — The dipole width rule

Take $V(x) = V_{0}\,h/\left(x^{2}+h^{2}\right)^{3/2}$. The maximum is at $x = 0$:
$V_{\max} = V_0/h^{2}$. Setting $V = V_{\max}/2$:

$$\frac{h}{\left(x^{2}+h^{2}\right)^{3/2}} = \frac{1}{2h^{2}}
\;\Longrightarrow\;
\left(x^{2}+h^{2}\right)^{3/2} = 2h^{3}
\;\Longrightarrow\;
x^{2}+h^{2} = 2^{2/3}h^{2},$$

$$x^{2} = h^{2}\left(2^{2/3}-1\right)
\;\Longrightarrow\;
x = h\sqrt{2^{2/3}-1} = 0.7664\,h .$$

The full width at half maximum is twice this:

$$\mathrm{FWHM} = 2\sqrt{2^{2/3}-1}\;h = 1.5328\,h . \qquad\blacksquare$$

For comparison, the point-source profile $1/\sqrt{x^{2}+h^{2}}$ gives
$x = \sqrt{3}\,h$ and $\mathrm{FWHM} = 3.4641\,h$, a factor $2.26$ larger.
**The two rules differ by that factor for the same measured width**, which is why
the source geometry must be stated before a depth is quoted.

---

## ★5 — A depth from a width

$$\text{point electrode: } h = \frac{120.0}{3.4641} = 34.6\ \mathrm{m},
\qquad
\text{compact dipole: } h = \frac{120.0}{1.5328} = 78.3\ \mathrm{m},$$

a ratio of $2.26$. Neither is "the" depth: each is the depth *under an assumed
geometry*. A distributed source has a width set largely by its own length, and
neither constant applies — the lesson's shallow sheet gives $120.0$ m FWHM from a
$120$ m long source at only $10$ m depth.

---

## ★6 — The buried electrode and the apparent-resistivity identity

$$V(0) = \frac{\rho I}{2\pi z} = \frac{50 \times 1.0}{2\pi \times 60}
= 0.13263\ \mathrm{V} = 132.63\ \mathrm{mV},$$

$$V(100) = \frac{\rho I}{2\pi\sqrt{x^{2}+z^{2}}}
= \frac{50}{2\pi\sqrt{100^{2}+60^{2}}}
= \frac{50}{2\pi \times 116.619} = 0.068237\ \mathrm{V} = 68.24\ \mathrm{mV}.$$

Apparent resistivity from $\rho_a = 2\pi r V/I$ with
$r = \sqrt{x^{2}+z^{2}}$:

- at $x = 0$: $\rho_a = 2\pi \times 60 \times 0.13263/1.0 = 50.00\ \Omega$ m;
- at $x = 100$ m: $\rho_a = 2\pi \times 116.619 \times 0.068237/1.0
  = 50.00\ \Omega$ m.

Both give the true resistivity, which is the identity of the lesson's
Section 2.2: **in a homogeneous half-space a buried electrode produces no
apparent-resistivity anomaly, so any variation of $\rho_a$ along the profile is
the signature of heterogeneity.**

---

## ★7 — Separating streaming from redox sources (specification)

The two mechanisms differ in **what drives them**, so they correlate with
different external variables. The design exploits that.

**Measurements.**
1. A high-resolution SP profile across the anomaly (station spacing $\le$ one
   tenth of the expected FWHM, so the width is resolved).
2. A resistivity or ERT section along the same line, to fix $\sigma$ — needed
   because the streaming coefficient carries $1/\sigma$ and the potential carries
   another $1/\sigma$.
3. A survey repeated after a recharge event or at a different stage of the
   hydrological cycle, or (for a redox source) after a period in which the water
   table is unchanged.
4. Independent hydrological information: head gradients, piezometric levels, or
   topography/drainage direction.

**Predictions.**
- *Streaming:* the anomaly amplitude scales as $\partial V/\partial h \times
  \Delta h$ with $\partial V/\partial h \propto 1/\sigma$; it changes when the
  head changes, correlates with topography and drainage, and is positive
  downslope for $\zeta < 0$.
- *Redox:* the amplitude is set by the potential difference across the body and
  the $IR$ drop in the ground, scales as $1/\sigma$ through the potential
  expression but is *independent of the head*; it does not change with
  hydrological stage (unless the water table intercepts the body), and its sign
  follows the polarity of the dominant half-reaction.

**Statistic.** Fit the two models to the profile *and* to the change between the
two surveys, and compare $\chi^{2}$: the streaming model predicts a
proportionality between the anomaly change and the head change, with the
coefficient fixed by the measured $\sigma$ to within the uncertainty of $\zeta$.
The redox model predicts no such correlation and a *zero* change in the anomaly
under a head change at constant chemistry. The decisive statistic is therefore
the regression of anomaly amplitude against head change, with the predicted slope
$\partial V/\partial h = \varepsilon\zeta/(\eta\sigma) \times \rho_w g$ and its
sign. A slope consistent with zero rejects the streaming hypothesis at the
survey's own noise level.

**What this design cannot do.** It cannot separate two redox couples from each
other, nor a streaming source from a thermoelectric one, without ionic or thermal
data. The honest conclusion is a ranking of mechanisms, not an identification.

---

## ★8 — Shrinking the (depth, length) ridge

The ridge exists because a deeper, longer, stronger dipole reproduces the same
surface profile over a *finite aperture* with a *finite station spacing*. Two
measurements attack it:

1. **Widen the aperture.** The ridge's endpoints correspond to sources whose
   flanks fall outside the measured profile; extending the profile to several
   times the anomaly width removes those solutions, because an undeclared
   long-wavelength trend is no longer available to absorb the difference.
   *Predicted effect:* the admitted length range shrinks from $[4.0, 36.0]$ m
   while the depth range shrinks more slowly (depth is better constrained than
   length by the shape).
2. **Add an independent source of depth information** — for example a small
   controlled-source or mise-à-la-masse sounding from a borehole that fixes the
   body's position, or an SP measurement in a second borehole that constrains the
   depth directly.

*Direction of the shrinkage:* the admitted set stays a **ridge**, not a point.
The degeneracy between depth and moment is intrinsic to a potential-field
measurement: the far-field profile depends on $IL/h^{2}$ at fixed shape, so
depth and moment trade exactly in the far field, and only the near-field
curvature breaks it. A wider aperture and lower noise shrink the ridge's extent
along the (depth, length) direction but cannot collapse it to a point without a
measurement that is not a surface potential at all. The correlation should fall
from $+0.854$ towards zero as the aperture and the signal-to-noise ratio improve,
because the length information comes from the anomaly's *shape* while the depth
comes from its *scale* — and the two enter the fit differently once the flanks
are measured.
