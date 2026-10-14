# Solutions — 08-02-06 Magnetic Survey Design, Diurnal Correction and Levelling

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [06 Magnetic Survey Design, Diurnal Correction and Levelling](../06-magnetic-survey-procedures.md).

---

## ★1 — Residual from a 10-minute lag

For a harmonic of amplitude $\alpha$ and angular frequency
$\omega = 2\pi/24\ \mathrm{h} = 4.36332\times10^{-3}\ \mathrm{min^{-1}}$, the
residual of a correction lagged by $\delta$ is

$$\Delta(t) = \alpha\left[\sin\omega t - \sin\omega(t-\delta)\right],$$

whose amplitude is

$$|\Delta|_{\max} = 2\alpha\sin\frac{\omega\delta}{2}
= 2\times20\times\sin\!\left(\frac{4.36332\times10^{-3}\times10}{2}\right)
= 40\sin(0.0218166) = 0.87260\ \mathrm{nT}.$$

To first order in the lag this is $\alpha\omega\delta
= 20\times4.36332\times10^{-3}\times10 = 0.87266\ \mathrm{nT}$ — the linearisation
is good to five digits here. **A ten-minute clock error is a $0.87\ \mathrm{nT}$
error**, twice the instrument noise of a good survey: synchronising clocks is not
bookkeeping.

---

## ★2 — Main-field gradient and span at $40^{\circ}$

$$F(\lambda) = |g_1^0|\sqrt{1+3\sin^{2}\lambda}, \qquad
\frac{\mathrm{d}F}{\mathrm{d}\lambda}
= |g_1^0|\frac{3\sin\lambda\cos\lambda}{\sqrt{1+3\sin^{2}\lambda}}.$$

At $\lambda = 40^{\circ}$: $\sin\lambda = 0.642788$,
$\cos\lambda = 0.766044$, so $3\sin\lambda\cos\lambda = 1.47716$ and
$\sqrt{1+3\times0.413176} = \sqrt{2.239528} = 1.496505$:

$$\frac{\mathrm{d}F}{\mathrm{d}\lambda}
= 30000\times\frac{1.47716}{1.496505} = 29613\ \mathrm{nT\,rad^{-1}}
= 516.9\ \mathrm{nT\,deg^{-1}}.$$

Per kilometre: $516.9/111.195 = 4.648\ \mathrm{nT\,km^{-1}}$.

Across 30 km: $4.648\times30 = 139.4\ \mathrm{nT}$ — larger than any but the
strongest anomaly, which is why the main-field removal is mandatory.

---

## ★3 — Sampling an 80 m anomaly

$$\text{quarter-wavelength spacing} = \frac{80}{4} = 20\ \mathrm{m}, \qquad
\text{Nyquist threshold} = \frac{80}{2} = 40\ \mathrm{m}.$$

Designing at 40 m is designing at the aliasing threshold: the worst-case retention
over the anomaly's phase is zero, so whether you see the anomaly at all depends on
where the peak falls relative to the samples.

---

## ★4 — Epoch error versus position error

$$\Delta g_1^0 = -40\ \mathrm{nT\,yr^{-1}}\times3\ \mathrm{yr}
= -120\ \mathrm{nT}.$$

Its variation across the survey is

$$120\times0.001883 = 0.226\ \mathrm{nT},$$

i.e. essentially uniform: the error is an offset.

A 1 km position error at a $4.5\ \mathrm{nT\,km^{-1}}$ gradient is

$$\Delta B_{\text{pos}} = 4.5\ \mathrm{nT\,km^{-1}}\times1\ \mathrm{km}
= 4.5\ \mathrm{nT},$$

and, crucially, it is a **gradient** error: it changes across the survey in
proportion to position. Comparing the two:

| error | size | spatial character | removable by levelling? |
|---|---|---|---|
| epoch error (3 yr) | 120 nT in $g_1^0$; 0.226 nT variation | offset | yes |
| 1 km position error | 4.5 nT | gradient | no |

The epoch error is 27 times larger in absolute terms and 20 times *less* harmful,
because it is uniform. **Magnitude is not harmfulness; spatial character is.**

---

## ★5 — What a levelling adjustment determines

With six lines and nine crossings, the system has five independent offsets to
determine (one datum fixed) and nine equations, so it is over-determined by four
degrees of freedom.

**Determines:** the *differences* between line levels, to within the residual
misfit of $0.4\ \mathrm{nT}$ per crossing. That is what the map needs: relative
levels are what make an anomaly map continuous across lines.

**Assumes:** (i) each line has a *constant* offset, so the misfit model is one
number per line; (ii) the tie lines are themselves error-free at the level of the
differences they define (in practice they carry their own noise, which inflates
the residual); (iii) the datum, i.e. the absolute level of the first line.

**Cannot remove:**
- a within-line error such as a diurnal ramp or a drape effect — the model has no
  parameter for it, so it survives the adjustment and appears as a gradient along
  the line;
- a mis-positioned station, which is a coordinate error rather than a level error;
- a gradient imposed by the reference field model (lesson §3.1).

---

## ★6 — Error budget arithmetic

$$\sigma_{\text{tot}} = \sqrt{0.2^{2}+0.8^{2}+1.5^{2}+0.3^{2}}
= \sqrt{0.04+0.64+2.25+0.09} = \sqrt{3.02} = 1.7378\ \mathrm{nT}.$$

Dominant term share of the variance:

$$\frac{1.5^{2}}{3.02} = \frac{2.25}{3.02} = 74.50\%.$$

Smallest term share:

$$\frac{0.2^{2}}{3.02} = 1.32\%.$$

**Halving the total.** To halve $\sigma_{\text{tot}}$ from 1.7378 to
0.8689 nT, the total variance must fall to $0.8689^{2} = 0.755\ \mathrm{nT^{2}}$,
i.e. by $3.02-0.755 = 2.265$. The dominant term alone contributes 2.25, so
**removing the dominant term entirely achieves very nearly the halving**:
$\sqrt{3.02-2.25} = \sqrt{0.77} = 0.8775\ \mathrm{nT}$. Improving the smallest
term is worth nothing: eliminating it entirely changes the total from 1.7378 to
1.7263 nT, a 0.7% improvement.

---

## ★7 — Ground survey design (specification)

**Sensor.** A scalar magnetometer with a $0.1\ \mathrm{nT}$ reading noise and a
0.5 Hz or better reading rate. A $5\ \mathrm{nT}$ target in a field whose diurnal
variation reaches tens of nT is well within reach of any modern scalar instrument;
resolution is not the binding constraint (see the budget below).

**Station spacing.** An anomaly from a $20\ \mathrm{m}$ deep, $100\ \mathrm{m}$
strike-length body has a width of order 20–40 m across strike and a length of
order 100 m along strike. Applying the quarter-wavelength rule with
$\lambda \approx 40\ \mathrm{m}$ gives a $10\ \mathrm{m}$ station spacing along
lines, and the same $10\ \mathrm{m}$ for line spacing — an
effectively continuous survey on a $10\ \mathrm{m}$ grid.

**Lines.** Orient lines across the expected strike so the anomaly is narrow across
strike and smooth along it; use lines at 10 m spacing over the target area and
wider spacing (say 50 m) outside it, with a stated rationale for the change.

**Base station.** One magnetometer at a quiet site within the survey area,
sampling continuously at an interval far shorter than the diurnal variation's
shortest period (say 1 s or faster, see ★8), with a GPS-disciplined clock. A
second base station 5–10 km away for the first day, to test the uniformity
assumption.

**Levelling.** Tie lines every five survey lines, crossing the whole area; a
least-squares adjustment with the primary line as datum; report the residual
misfit.

**Levelling of the instrument itself.** For each station, record the sensor's
height above ground and orientation. A $50\ \mathrm{nT\,m^{-1}}$ vertical gradient
(a strong near-surface source) with a $10\ \mathrm{cm}$ height error is a
$5\ \mathrm{nT}$ error, the same size as the target — hence the requirement.

**Expected total uncertainty.** Instrument 0.1 nT; diurnal residual with a 1 s
synchronised base, well under 0.1 nT; main-field removal 0.3 nT; levelling 0.4 nT;
position and height 1.0 nT (the largest term, driven by the gradient argument
above). Quadrature total: $\sqrt{0.01+0.01+0.09+0.16+1.0} = 1.13\ \mathrm{nT}$.

**Where to spend money.** The **position and height control** dominates the
budget, at 1.0 nT of 1.13 nT total. A differential GNSS with a real-time height
solution, plus a surveyor's level for the sensor height, is the upgrade that
matters; a better magnetometer would change the total by less than 1%.

---

## ★8 — The lagged correction, in general

Taylor-expand the diurnal signal about $t$:

$$D(t-\delta) = D(t) - \delta\dot D(t) + \frac{\delta^{2}}{2}\ddot D(t)
- \cdots,$$

so the residual of a lagged correction is

$$\Delta(t) = D(t) - D(t-\delta)
= \delta\dot D(t) - \frac{\delta^{2}}{2}\ddot D(t) + O(\delta^{3})
\;\approx\; \delta\dot D(t).$$

**Linear drift.** If $D(t) = ct$ exactly, then $\dot D = c$ and
$\Delta(t) = c\delta$: a **constant**. A constant offset along a line is removed
by levelling (and along a closed loop it shows up as a closure error of the same
size). This is why a slow linear drift in the base station is comparatively
harmless.

**Curved drift.** If $\dot D$ varies, then $\Delta(t) = \delta\dot D(t)$ varies
with time. Along a line the residual is a ramp whose slope is
$\delta\ddot D$: a spurious **gradient**, which levelling cannot remove. The
demonstration's residual peak of $0.96\ \mathrm{nT}$ at a 15-minute lag is exactly
this term.

**Implied base-station sampling interval.** The correction interpolates the base
record, so the interpolation error must be smaller than the target uncertainty.
With linear interpolation between samples separated by $\Delta t_b$, the maximum
interpolation error is $\tfrac{1}{8}\ddot D\Delta t_b^{2}$. Requiring it below
$0.01\ \mathrm{nT}$ for a signal with
$\ddot D \approx \alpha\omega^{2} = 20\times(4.363\times10^{-3})^{2}
= 3.8077\times10^{-4}\ \mathrm{nT\,min^{-2}}$ gives

$$\Delta t_b \le \sqrt{\frac{8\times0.01}{3.8077\times10^{-4}}}
= \sqrt{210.1} = 14.5\ \mathrm{min}.$$

So a one-minute base sampling is entirely adequate for the smooth daily
variation — but not for the pulsation-band activity (periods of seconds to
minutes) that a magnetometer also sees. **Sampling at 1 Hz costs nothing and
removes the question**; that is the standard choice, and it is made for the
high-frequency part of the spectrum rather than for the daily wave.
