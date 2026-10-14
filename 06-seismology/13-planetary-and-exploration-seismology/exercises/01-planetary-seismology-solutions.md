# Solutions — 06-13-01 Planetary Seismology: InSight and Lunar Seismic Experiments

The lesson is [01 Planetary Seismology](../01-planetary-seismology.md). All
models are **SYNTHETIC**.

## ★ Foundational

**★1.**
$$R = \sqrt{\Delta^{2} + h^{2}} = \sqrt{30.0^{2} + 20.0^{2}} = \sqrt{1300}
= 36.0555\ \mathrm{km},$$
$$t_P = \frac{36.0555}{6.00} = 6.0093\ \mathrm{s}, \qquad
t_S = \frac{36.0555}{3.46} = 10.4207\ \mathrm{s},$$
$$t_S - t_P = 10.4207 - 6.0093 = 4.4114\ \mathrm{s}.$$
(The S−P time can be computed directly as
$R(1/V_s - 1/V_p) = 36.0555 \times (0.289017 - 0.166667) = 4.4114\
\mathrm{s}$, which also checks the arithmetic.)

**★2.**
$$\tan i = \frac{\Delta}{h} = \frac{30.0}{20.0} = 1.50
\;\Rightarrow\; i = 56.31^{\circ}.$$
The optimum for polarisation is $i = 45^{\circ}$; at $56.31^{\circ}$ the
fractional sensitivity is $\mathrm{d}\ln\Delta/\mathrm{d}i = 2/\sin(112.62^{\circ})
= 2/0.9230 = 2.167$ per radian $= 3.78\%$ per degree — close to the best case,
so this geometry is favourable, though $\Delta/h = 1$ would be slightly better
($3.49\%$ per degree).

**★3.**
$$\sigma_R = \frac{\sigma_t}{1/V_s - 1/V_p} = \frac{0.030}{0.122351}
= 245.2\ \mathrm{m} = 0.245\ \mathrm{km},$$
i.e. $0.245/36.0555 = 0.68\%$ of $R$. The conversion factor is the **reciprocal
difference** $1/V_s - 1/V_p = 0.122351\ \mathrm{s\,km^{-1}}$: it is not the
velocity contrast in $\mathrm{km\,s^{-1}}$ but its effect on slowness. A larger
$V_p - V_s$ (i.e. a smaller reciprocal difference relative to the velocities)
makes the S−P time a sharper range measurement.

## ★★ Applied

**★★4.** Fix $t_S - t_P = 4.4114\ \mathrm{s}$, so
$R = 4.4114/0.122351 = 36.0555\ \mathrm{km}$ and
$h = \sqrt{R^{2} - \Delta^{2}}$:

| $\Delta$ (km) | $h$ required (km) |
|---|---|
| 5.0 | 35.707 |
| 15.0 | 32.787 |
| 30.0 | 20.000 |
| 50.0 | 0.000 (would need $h^{2} < 0$) |
| 120.0 | none — $R$ is already exceeded |

Within the circle of radius $R$, every $({\Delta}, h)$ pair on it reproduces the
measured time difference exactly. The table proves that a single S−P time
determines the slant range and leaves the split between distance and depth
entirely free.

**★★5.** With $V_p/V_s$ $4\%$ too large and $V_p$ fixed, $V_s$ is $4\%$ too small:
$V_s' = 3.46/1.04 = 3.3269\ \mathrm{km\,s^{-1}}$. The new reciprocal difference is
$$1/3.3269 - 1/6.00 = 0.300578 - 0.166667 = 0.133911\ \mathrm{s\,km^{-1}},$$
$$R' = \frac{4.4114}{0.133911} = 32.943\ \mathrm{km},$$
an error of $32.943 - 36.056 = -3.11\ \mathrm{km}$, i.e. $-8.63\%$. The pick
error of ★3 was $0.245\ \mathrm{km}$ ($0.68\%$): **the velocity-model error is
$12.7$ times the pick error**, confirming that model error, not picking, is the
limit.

**★★6.** For $\Delta/h = 2$, $i = 63.43^{\circ}$, $2i = 126.87^{\circ}$,
$\sin 2i = 0.8000$, so
$$\frac{\mathrm{d}\ln\Delta}{\mathrm{d}i} = \frac{2}{0.8000} = 2.500\
\mathrm{rad^{-1}} = \frac{2.500}{57.2958} = 4.36\%\ \mathrm{per\ degree}.$$
A $2^{\circ}$ error therefore gives a fractional distance error of
$2 \times 4.36\% = 8.7\%$ — at a true distance of $30\ \mathrm{km}$ that is
$2.6\ \mathrm{km}$, again far larger than the pick-limited range uncertainty.

## ★★★ Research-oriented

**★★★7.** **Quantitative comparison.** Use the lesson's numbers, all of which
follow from the geometry rather than from any mission.

- *Option (i), one station with a velocity model:* the distance is limited by
  model error, which is $2.31\%$ per $1\%$ of $V_p/V_s$ error (lesson §3). With a
  plausible $2$–$5\%$ model error this is $5$–$12\%$ in distance, and the depth
  is essentially unconstrained in the sense that any model error re-splits
  $({\Delta}, h)$ along the curve of §2. *Assumption:* the model is right at the
  station, and the ray is straight.
- *Option (ii), two stations:* the trade-off collapses through geometry (lesson
  §6), with a perpendicular uncertainty $\sigma_d \approx \sigma_R r/d$ — for
  $b = 10\ \mathrm{km}$, $d = 5\ \mathrm{km}$ and $\sigma_R = 409\ \mathrm{m}$
  that is $578\ \mathrm{m}$. But two stations along a baseline fail for sources
  near the baseline ($\sigma_d/b = 0.41$ at $d = 0.5\ \mathrm{km}$), so the
  option is a *coverage* improvement, not a uniform one. *Assumption:* the
  stations share a velocity model, i.e. the structure between them is laterally
  homogeneous.
- *Option (iii), one station plus a refraction profile:* $V_p$ to $1\%$ and
  $V_p/V_s$ to $2\%$ bounds the model error, hence the distance error, to roughly
  $4.6\%$ (twice the $2.31\%$ sensitivity at $2\%$), and constrains $h$ through
  the curve of §2. The depth remains conditional, because the S−P time still
  gives one number for two unknowns. *Assumption:* the near-surface refraction
  structure is representative of the source–receiver path — the weakest link,
  since a refraction profile samples the top metres while the ray samples the
  whole path.

**Best option.** For *locations*, option (ii) is best because it is the only one
that breaks the depth–distance degeneracy directly; for *structure*, option (iii)
is best because it fixes the velocities that everything else is conditional on.
The honest answer is that the choice is set by the mission's question, and that
option (i) alone cannot deliver hypocentres.

**Diagnostics.** For (i) and (iii): a synthetic recovery test in which the true
model is perturbed by the claimed model error, reporting how far the recovered
$({\Delta}, h)$ move. For (ii): the two-station residuals as a function of
azimuth, which expose lateral heterogeneity; and the source-to-baseline offset
of each event, which exposes the near-baseline failure mode. For all three: a
multi-event consistency check, since a wrong velocity model produces a
systematic offset in depth across events, whereas random pick error does not.

**★★★8.** **Counting with an extra phase.** Unknowns: $\Delta$, $h$, $V_p$, $V_s$
(4), plus any parameter describing the interface that generates the extra phase
(a reflector depth $z$), so 4 (or 5). Observations: $t_P$, $t_S - t_P$,
incidence, and the extra phase's time relative to $P$, which for a conversion or
surface reflection depends on $h$ and $z$ but *not* on $\Delta$ (its raypath is
nearly vertical and its incidence depends only on the local structure). So 4
observations in the simplest description.

- If the extra phase introduces no new unknown (a free-surface reflection on the
  direct path), unknowns = 4 and observations = 4: the degeneracy **is** broken,
  because the extra observation is sensitive to $h$ and not to $\Delta$, which is
  exactly the direction that the S−P time could not constrain.
- If it requires a new unknown (a converter at unknown depth $z$), unknowns = 5
  and observations = 4: one degree of freedom remains, now shared between $h$ and
  $z$. The degeneracy is *moved*, not removed: the family is relabelled.

**New assumption introduced.** That the extra phase is correctly identified and
that its raypath is the simple one assumed — a conversion from a dipping
interface, a multiple, or a phase from a laterally varying structure all
contaminate the interpretation, and the contamination is not diagnosable from a
single record. The practical consequence: extra phases buy depth information only
when their *identity* is secure, which in a single-station setting is often the
hardest part of the analysis.

## Module mastery checkpoint (worked)

The module [README](../README.md) sets a checkpoint on a single station with
$t_S - t_P = 3.50\ \mathrm{s}$, incidence $50^{\circ}$,
$V_p = 6.00\ \mathrm{km\,s^{-1}}$, $V_s = 3.50\ \mathrm{km\,s^{-1}}$,
$\sigma_t = 0.05\ \mathrm{s}$.

**(a)**
$$\frac{1}{V_s} - \frac{1}{V_p} = 0.2857143 - 0.1666667
= 0.1190476\ \mathrm{s\,km^{-1}},$$
$$R = \frac{3.50}{0.1190476} = 29.400\ \mathrm{km}, \qquad
\sigma_R = \frac{0.05}{0.1190476} = 0.420\ \mathrm{km} = 420.0\ \mathrm{m},$$
i.e. a $1.43\%$ range constraint.

**(b)** With $i = 50^{\circ}$,
$$\Delta = R\sin i = 29.400 \times 0.766044 = 22.522\ \mathrm{km}, \qquad
h = R\cos i = 29.400 \times 0.642788 = 18.898\ \mathrm{km},$$
which checks against $R$: $\sqrt{22.522^{2} + 18.898^{2}} = 29.400$. The S−P
time alone determines the **slant range only**; the split into distance and depth
comes entirely from the polarisation and the velocity model.

**(c)** Using the lesson's measured sensitivity of $2.31\%$ in distance per $1\%$
error in $V_p/V_s$, a $2\%$ error gives about $4.6\%$ of $22.522\ \mathrm{km} =
1.04\ \mathrm{km}$ — about **$2.5$ times the pick-limited uncertainty of
$0.42\ \mathrm{km}$**. In this configuration the model error dominates, and its
sign is not recoverable from the record.

**(d)** See the lesson-04 solutions, ★★6 of the exercise set: with
$c_{\min} = 250\ \mathrm{m\,s^{-1}}$ and $f_{\max} = 20\ \mathrm{Hz}$,
$\lambda_{\min} = 12.5\ \mathrm{m}$, so $d < 6.25\ \mathrm{m}$ (choose
$d = 5\ \mathrm{m}$) and $L \approx 0.4\lambda_{\min} = 5.0\ \mathrm{m}$ for a
broadband objective (or $L \lesssim 5.5\ \mathrm{m}$ for full-band registration).

**(e)** Any one of: a refraction profile or a second station (lesson 01, to
replace the velocity model or break the depth–distance degeneracy); radar or a
borehole (lesson 02, to fix the ice thickness independently of the layer
velocity); a narrowband LP detector run in parallel with a broadband tremor
envelope (lesson 03, so that the reported performance does not depend on a single
combination rule); a co-located point sensor (lesson 04, to test the coupling
between fibre strain and ground strain).
