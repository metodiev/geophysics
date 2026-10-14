# Solutions — 15-02-03 Side-Scan Sonar and Seafloor Imaging

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [03 Side-Scan Sonar](../03-side-scan-sonar.md).

---

## ★1 — Slant-to-ground mapping at $h = 12$ m

$$x = \sqrt{r^{2}-h^{2}}, \qquad g = \arcsin(h/r), \qquad
\frac{\mathrm{d}x}{\mathrm{d}r} = \frac{r}{\sqrt{r^{2}-h^{2}}}.$$

| $r$ (m) | $x$ (m) | $g$ (deg) | stretch |
|---|---|---|---|
| 14.0 | $\sqrt{196-144} = 7.211$ | 58.997 | 1.941 |
| 25.0 | $\sqrt{625-144} = 21.932$ | 28.685 | 1.140 |
| 90.0 | $\sqrt{8100-144} = 89.196$ | 7.662 | 1.009 |

**The near-range end is geometrically worst.** The stretch is 1.94 at $14\
\mathrm{m}$ and 1.009 at $90\ \mathrm{m}$, and it diverges as $r\to h$: a fixed
increment of slant range corresponds to a rapidly shrinking increment of ground
range near the nadir. The consequence is that the plan-position correction is
*most sensitive to the altitude* exactly where the data are least useful, and that
the nominal across-track resolution near nadir (small) is not achievable in plan
view because the altitude is not known well enough.

---

## ★2 — Blind zone at $h = 12$ m, first return $r = 14$ m

$$x_{\text{blind}} = \sqrt{r_{\min}^{2}-h^{2}} = \sqrt{196-144}
= 7.211\ \mathrm{m}.$$

So the innermost $7.2\ \mathrm{m}$ of ground range on each side of the track is
never ensonified — the beam has not reached the seafloor yet. In a mosaic this
appears as a gap along every track line, and it is one of the reasons side-scan
mosaics are usually accompanied by a multibeam bathymetry rather than replacing it.

---

## ★3 — Decibels of intensity and of amplitude

$$10\log_{10}(0.02) = -16.99\ \mathrm{dB}, \qquad
20\log_{10}(0.02) = -33.98\ \mathrm{dB}.$$

**TS uses the intensity form**, $10\log_{10}$, because a target strength is a
ratio of *intensities* (or of powers). The $20\log_{10}$ form applies to pressure
or voltage amplitude ratios. A factor of 0.02 in intensity is $-17.0\ \mathrm{dB}$;
a factor of 0.02 in amplitude is $-34.0\ \mathrm{dB}$. Confusing the two produces a
factor-of-two error in every decibel, which is the most common arithmetic error in
sonar work.

---

## ★★4 — Derivation and evaluation of the across-track resolution

The pulse occupies $c\tau$ in space (two-way path), so a *range* interval of
$c\tau/2$ in one-way distance. A range interval $\delta r$ projects onto the
seafloor along a direction inclined at grazing angle $g$ to the seafloor as
$\delta g = \delta r/\sin g$. Hence

$$\ell_{\text{across}} = \frac{c\,\tau}{2\sin g} . \ ✔$$

With $\tau = 0.08\ \mathrm{ms}$: $c\tau/2 = 1500 \times 8\times10^{-5}/2
= 0.060\ \mathrm{m}$.

| $g$ | $\sin g$ | $\ell_{\text{across}}$ (m) |
|---|---|---|
| $60^\circ$ | 0.8660 | 0.0693 |
| $20^\circ$ | 0.3420 | 0.1754 |
| $5^\circ$ | 0.0872 | 0.6884 |

**The floor** is $c\tau/2 = 0.060\ \mathrm{m}$, reached only at $g = 90^\circ$
(vertical incidence). No geometry beats it: it is the pulse's own length in the
medium. This is the same statement as the $\lambda/4$ limit of
[Lesson 01](../01-marine-seismic-reflection.md) in a different guise — the
resolution cannot be finer than the probe.

---

## ★★5 — Target strength at two grazing angles

$$\mathrm{TS}(g) = 10\log_{10}\!\left(\sin^{2}g\right)
= 20\log_{10}(\sin g)\ \mathrm{dB}.$$

$$\mathrm{TS}(40^\circ) = 20\log_{10}(0.64279) = -3.839\ \mathrm{dB},$$
$$\mathrm{TS}(8^\circ) = 20\log_{10}(0.13917) = -17.129\ \mathrm{dB},$$

$$\Delta\mathrm{TS} = -17.129 - (-3.839) = -13.290\ \mathrm{dB}.$$

As an intensity ratio: $10^{-13.290/10} = 0.0469$, i.e. **the low-grazing-angle
return is 21.3 times weaker** (equivalently, $1/21.3$). **A 32-degree change in
grazing angle produces a factor of 21 in intensity under this model**, with no
change in the seafloor whatever. That is the size of the effect that a
grazing-angle correction must remove, and it is why an amplitude map without the
correction is a map of geometry.

---

## ★★6 — EL at two ranges

$$\mathrm{EL}(R) = \mathrm{SL} - 2\left(20\log_{10}R + \alpha R\right)
+ \mathrm{TS}(g(R)) - 40.$$

At $R = 220\ \mathrm{m}$: $20\log_{10}220 = 46.85$, $\alpha R = 22.0$,
$\mathrm{TL} = 68.85$, $2\mathrm{TL} = 137.70$; $g = \arcsin(20/220)
= 5.22^\circ$, $\mathrm{TS} = 20\log_{10}(0.09099) = -20.82\ \mathrm{dB}$.

$$\mathrm{EL} = 220 - 137.70 - 20.82 - 40 = +21.48\ \mathrm{dB}.$$

At $R = 280\ \mathrm{m}$: $20\log_{10}280 = 48.94$, $\alpha R = 28.0$,
$\mathrm{TL} = 76.94$, $2\mathrm{TL} = 153.88$; $g = \arcsin(20/280)
= 4.10^\circ$, $\mathrm{TS} = 20\log_{10}(0.07148) = -22.92\ \mathrm{dB}$.

$$\mathrm{EL} = 220 - 153.88 - 22.92 - 40 = +3.19\ \mathrm{dB}.$$

Both positive, so **the detection limit falls between 280 m and the value the
demonstration finds by bisection, 291.0 m.** The two computed points straddle a
20 dB drop over 60 m of range — about $0.33\ \mathrm{dB}$ per metre — which is why
the range is a soft limit: a 3 dB improvement in any term buys only about 9 m of
additional range.

---

## ★★7 — Raising the tow from 20 m to 50 m at fixed 180 m slant range

**(a)** Ground half-width $= \sqrt{180^{2}-h^{2}}$:

$$h = 20\ \mathrm{m}: \sqrt{32400-400} = 178.89\ \mathrm{m}, \qquad
h = 50\ \mathrm{m}: \sqrt{32400-2500} = 172.92\ \mathrm{m}.$$

**(b)** Far-edge grazing angle $= \arcsin(h/180)$: $6.38^\circ$ at $20\ \mathrm{m}$;
$16.13^\circ$ at $50\ \mathrm{m}$.

**(c)** Across-track resolution $= 0.075/\sin g$ (with $\tau = 0.1\ \mathrm{ms}$):
$0.675\ \mathrm{m}$ at $20\ \mathrm{m}$ altitude; $0.270\ \mathrm{m}$ at
$50\ \mathrm{m}$ altitude.

**(d)** **Gained:** far-edge across-track resolution improves by a factor 2.5, and
the grazing angle at the far edge more than doubles. **Lost:** ground coverage
falls by $3.3\,\%$ ($178.9 \to 172.9\ \mathrm{m}$), and the blind zone grows from
$\sqrt{(20+2)^{2}-20^{2}} = 9.2\ \mathrm{m}$ to
$\sqrt{(50+2)^{2}-50^{2}} = 14.3\ \mathrm{m}$.

The trade is therefore **far-field resolution against near-field coverage**, and it
is a genuine exchange rather than a free improvement. A survey optimised for
detecting small targets at long range tows high; one optimised for imaging a
shallow, narrow corridor tows low.

---

## ★★★8 — Measuring the angular exponent $n$

**The circularity.** The measured intensity is

$$I_{\text{obs}}(g) = I_{\text{seafloor}}(g)\times B(g)\times G(g),$$

where $B(g)$ is the beam pattern (a property of the transducer, measurable in a
tank or on a calibration range) and $G(g)$ is the geometric spreading and
insonified-area correction (calculable). To estimate $n$ in
$I_{\text{seafloor}} = A\sin^{n}g$, one needs $B(g)$ and $G(g)$; but $B(g)$ is
often *unknown*, and the temptation is to absorb it into $n$ — which is exactly the
circularity. The exponent that comes out is then $n + n_B$, a property of the
instrument, and quoting it as a seafloor property is an error.

**How to break it.** Three routes, in order of strength:

1. **Measure $B(g)$ independently.** A calibration range with a known target, or a
   tank measurement, gives $B(g)$ as a function of angle. This is the only route
   that yields an absolute $n$.
2. **Differential geometry.** Fly the same patch at two altitudes. The seafloor's
   angular response is a function of $g$ alone; the beam pattern is a function of
   the *steering angle*, which differs between passes. Fitting both passes
   simultaneously with a shared $n$ and a shared $B(g)$ separates them.
3. **Reciprocal headings.** Steaming the same track in opposite directions
   displaces the beam-pattern imprint relative to the seafloor imprint, breaking
   the degeneracy exactly as it does for roll in
   [Lesson 02](../02-multibeam-bathymetry.md).

**Geometry for the widest range of grazing angles.** A low tow altitude (or a long
range) gives the widest span, because $g$ goes from $\arcsin(h/r_{\min})$ to
$\arcsin(h/r_{\max})$. With $h = 10\ \mathrm{m}$ and $r$ from 12 to
$200\ \mathrm{m}$, $g$ spans $56^\circ$ to $2.9^\circ$ — a factor of 19 in
$\sin g$, or $25\ \mathrm{dB}$ under an $n = 2$ law, which is a well-conditioned
fit. A high tow over a short range span gives a narrow range of $g$ and a badly
conditioned one, which is the practical reason $n$ is poorly determined from
shallow, narrow surveys.

**The systematic that would bias $n$.** Sediment-type variation along the record.
If the seafloor changes from sand (high $n$) near the nadir to mud at range, a
single fitted $n$ is a weighted average of two different seafloors, and the
residual pattern looks like an instrument error. The defence is to fit $n$ in
windows and to report its spatial variability rather than a single value — which
is, of course, the scientifically interesting answer.

---

## ★★★9 — Asymptotic sensitivity of range to absorption

**Setup.** Set $\mathrm{EL} = 0$:

$$2\alpha R + 40\log_{10}R + 40 = \mathrm{SL} + \mathrm{TS}(g(R)) + \mathrm{const}.$$

If we treat $\mathrm{TS}$ as slowly varying (it is logarithmic in $R$ at long
range) and keep only the dominant terms, the balance is approximately

$$2\alpha R \approx C_0 \;\Longrightarrow\; R \approx \frac{C_0}{2\alpha}
\;\Longrightarrow\; R \propto \alpha^{-1}.$$

So **the asymptotic exponent is $-1$**: halving $\alpha$ doubles the range. The
demonstration measures $1.59$, i.e. an exponent of
$-\log(1.59)/\log(1/2) = -0.67$, not $-1$.

**Why the measured exponent is weaker.** The $\alpha R$ term only dominates when
$2\alpha R \gg 40\log_{10}R$, i.e. roughly when
$\alpha R \gg 20\log_{10}R$. At the demonstration's crossing point
$R = 291\ \mathrm{m}$ and $\alpha = 0.10\ \mathrm{dB\,m^{-1}}$, $\alpha R = 29.1$
and $20\log_{10}R = 49.3$: the **spreading term is still the larger of the two.**
The demonstration's operating point is therefore in the *transition* regime, not
the asymptotic one, and the measured exponent $0.67$ is the correct answer there.

**Validity range.** The asymptotic $R \propto 1/\alpha$ applies when
$\alpha R \gtrsim 40\log_{10}R$; with $\alpha = 0.10$ that requires
$R \gtrsim 700\ \mathrm{m}$, and with $\alpha = 0.5\ \mathrm{dB\,m^{-1}}$ it
requires $R \gtrsim 140\ \mathrm{m}$. The practical statement is that
**absorption-limited scaling applies only at high frequency, in deep or low-tow
geometry, or both** — and that a survey's design curve must be computed, not
extrapolated from the asymptotic law. The measured $0.67$ exponent at the
demonstration's parameters versus the asymptotic $1.0$ is a factor-of-two error in
a design calculation, which is exactly the kind of mistake a budget prevents.
