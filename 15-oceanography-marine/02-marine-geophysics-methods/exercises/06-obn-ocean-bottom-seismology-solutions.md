# Solutions — 15-02-06 Ocean-Bottom Seismology and OBS Networks

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [06 Ocean-Bottom Seismology](../06-obn-ocean-bottom-seismology.md).

---

## ★1 — Water-column multiple at 2500 m

$$T_w = \frac{2h}{c} = \frac{2(2500)}{1500} = 3.3333\ \mathrm{s}, \qquad
f_1 = \frac{1}{T_w} = 0.3000\ \mathrm{Hz}.$$

Round-trip check: $h = cT_w/2 = 1500(3.3333)/2 = 2500.0\ \mathrm{m}$ ✔. The check
is worth doing every time, because the factor of two in $T_w = 2h/c$ is the
commonest error in using the water-layer period.

---

## ★2 — Depth from a repeated arrival

Repeats at $5.33$, $10.67$ and $16.00\ \mathrm{s}$ are spaced by
$T_w \approx 5.333\ \mathrm{s}$, so

$$h = \frac{1500 \times 5.333}{2} = 4000\ \mathrm{m}.$$

With the true speed $1530\ \mathrm{m\,s^{-1}}$:

$$h_{\text{true}} = \frac{1530 \times 5.333}{2} = 4080\ \mathrm{m},$$

an error of $+80\ \mathrm{m} = +2.00\,\%$. **The percentage error in the depth
equals the percentage error in the assumed sound speed** — the same one-for-one
mapping as in
[Lesson 02](../02-multibeam-bathymetry.md) — so a $2\,\%$ speed error is a $2\,\%$
depth error, and the water-layer period is a $2\,\%$ bathymetry, not a survey.

---

## ★3 — Tilt leakage at 2°

$$\text{leakage} = \sin\theta = \sin 2^\circ = 0.034899 .$$

**Units:** dimensionless — it is a ratio of amplitudes. Reported as a percentage,
$3.49\,\%$ of the horizontal ground motion appears on the vertical channel. For a
direct P with a horizontal component of $0.1$ and a vertical component of $1.0$,
the leak is $0.0035$ against a true conversion amplitude of a few per cent of
$1.0$ — so a $2^\circ$ tilt is marginal rather than fatal, and a $5^\circ$ tilt is
not.

---

## ★★4 — Ps delay and the multiple comb

$$q_p = \sqrt{\frac{1}{2.5^{2}} - 0.055^{2}}
= \sqrt{0.160000 - 0.003025} = \sqrt{0.156975} = 0.396201\ \mathrm{s\,km^{-1}},$$

$$q_s = \sqrt{\frac{1}{1.4^{2}} - 0.055^{2}}
= \sqrt{0.510204 - 0.003025} = \sqrt{0.507179} = 0.712165\ \mathrm{s\,km^{-1}},$$

$$\Delta t_{Ps} = H(q_s - q_p) = 3.0(0.315964) = 0.9479\ \mathrm{s}.$$

| water depth (m) | $T_w$ (s) | $\Delta t_{Ps}/T_w$ | verdict |
|---|---|---|---|
| 3000 | 4.000 | 0.237 | separable by inspection |
| 150 | 0.200 | **4.739** | **unresolvable comb** |

At $150\ \mathrm{m}$ the multiple spacing is a fifth of the conversion delay, so
the P multiple train lands on top of the conversion and several more arrivals pile
up in the same 1 s window. **The shelf case requires water-layer demultiple before
any conversion can be identified**, whereas at 3 km of water the first few arrivals
are separable by eye. This is the quantitative reason deep-water OBS data are the
preferred material for receiver-function work.

---

## ★★5 — Tilt leakage and the requirement

| tilt | $\sin\theta$ | leakage (%) |
|---|---|---|
| $0.3^\circ$ | 0.005236 | 0.524 |
| $1.0^\circ$ | 0.017452 | 1.745 |
| $3.0^\circ$ | 0.052336 | 5.234 |

For leakage below $0.5\,\%$:

$$\sin\theta \le 0.005 \;\Longrightarrow\; \theta \le 0.2865^\circ .$$

**The tilt must be known and corrected to about a quarter of a degree** — a factor
20 tighter than a naive instrument specification would suggest, and the reason OBS
packages carry a compass and an accelerometer and why the two horizontal channels
are checked for long-period coherence after recovery.

---

## ★★6 — Clock drift over 250 days

$$\Delta t = 0.005\ \mathrm{s\,day^{-1}} \times 250\ \mathrm{days}
= 1.250\ \mathrm{s}.$$

Converted to distance at two apparent velocities:

$$v_{\text{app}} = 8.0\ \mathrm{km\,s^{-1}}:\quad
1.250 \times 8000 = 10\,000\ \mathrm{m} = 10.0\ \mathrm{km},$$

$$v_{\text{app}} = 3.5\ \mathrm{km\,s^{-1}}:\quad
1.250 \times 3500 = 4375\ \mathrm{m} = 4.4\ \mathrm{km}.$$

**The faster phase is the more sensitive**, and the sensitivity is *inverse* to
what one might guess: a fixed timing error converts to a larger distance for a
faster apparent velocity, because the phase covers more ground per second. For
teleseismic P ($v_{\text{app}}$ of tens of $\mathrm{km\,s^{-1}}$) a $1.25\ \mathrm{s}$
error is tens of kilometres of apparent mislocation; for a slow S arrival it is
less. The practical statement is that clock drift matters most for the *fastest*
arrivals, which are usually the ones used for travel-time work.

---

## ★★7 — Diagnostics of a correct compliance correction

**(a)** Two diagnostics:

1. **The residual variance equals the independently known instrument noise.** The
   demonstration measures a residual standard deviation of $0.0494$ against an
   instrument noise of $0.0494$. If the residual were larger, some coherent
   compliance would be left; if it were smaller, the correction would be removing
   signal as well as noise.
2. **The squared coherence between the corrected vertical and the pressure falls to
   zero.** The demonstration measures $5\times10^{-6}$. Before correction the
   coherence is near unity by construction. A coherence that remains non-zero means
   either that the transfer is not fully captured (frequency-dependence,
   nonlinearity) or that part of the "compliance" is real signal that happens to
   correlate with pressure.

A third, weaker check is that the estimator leaves an uncorrelated pair's variance
essentially unchanged (measured ratio $1.12$), which establishes that the method
does not manufacture a correction where none is needed.

**(b)** A single scalar transfer assumes $Z$ is the same at every frequency. In the
demonstration $Z$ peaks near $0.015\ \mathrm{Hz}$ and falls off either side, so a
band-averaged $Z$ over-corrects where the true $Z$ is small and under-corrects
where it is large. The residual is then the *frequency-dependent mismatch*, which
is why it is eight times larger than the instrument noise. The general lesson: any
coherent-noise removal whose transfer varies with frequency must be estimated as a
function of frequency, and the residual should always be compared with an
independent noise estimate.

---

## ★★★8 — An OBS deployment for a 1 mm s⁻¹ mantle anomaly

**What sets the requirement.** A $1\ \mathrm{mm\,s^{-1}}$ anomaly in mantle shear
velocity against a background of $\sim4.5\ \mathrm{km\,s^{-1}}$ is $2.2\times10^{-4}$
in fractional terms. For a differential delay between two stations or two phases,
the required timing precision is therefore roughly

$$\delta t \sim \frac{\Delta t_{\text{path}} \times 2.2\times10^{-4}}{1} ,$$

e.g. for a $10\ \mathrm{s}$ differential delay, $\delta t \sim 2.2\ \mathrm{ms}$.

**Instrument requirements.**

- **Clock:** the drift must be under $\sim1\ \mathrm{ms}$ over the whole deployment
  *after correction*. Since the correctable part is removed by cross-correlating
  common events, the requirement is on the **short-term stability and linearity**
  of the drift, not on its magnitude — a drifting but *monotone* clock at
  $50\ \mathrm{ms\,day^{-1}}$ can be corrected to sub-millisecond if the drift
  rate is stable between the events used to estimate it. A GNSS-disciplined clock
  at one site anchors the network.
- **Tilt:** better than $0.3^\circ$ *known* and recorded continuously, since the
  package settles. Leakage below $0.5\,\%$ of the horizontal amplitude is required
  to leave the vertical channel interpretable.
- **Pressure:** a co-located pressure sensor is mandatory, for compliance removal.
  Without it the low-frequency vertical channel is unusable and the $2.2\ \mathrm{ms}$
  precision is unreachable.
- **Coupling:** the package must be rigidly coupled. A soft-sediment landing
  produces a resonance that is a first-order problem and cannot be corrected after
  the fact; it must be avoided by design (heavy, low-profile frames) or detected
  (from the horizontal-to-vertical coherence at the resonance).

**Array geometry.** The anomaly is a *lateral* variation, so the array must resolve
it in space: station spacing matched to the expected anomaly length scale, at least
$8$–$12$ instruments to separate the anomaly from the reference structure, and a
geometry with crossing paths so that the inversion has coverage in more than one
azimuth.

**Noise budget.** Compliance (removed with pressure), tilt leakage (corrected),
clock drift (corrected), coupling resonance (avoided), and oceanic microseism
(partly removable by stacking over many events). The dominant residual is the
finite number of usable events, which is a *statistical* budget rather than an
instrument one.

**The requirement that cannot be verified until after recovery.** The clock drift
and tilt record. Both are logged and both determine whether the deployment met its
specification. If the logger failed, the data are not merely degraded — the
correction cannot be applied and the deployment's precision is unknown. This is why
redundant logging, and the habit of checking the loggers on the deck before and
after, are part of the experiment rather than part of the instrument.

---

## ★★★9 — Exploiting the multiple comb rather than suppressing it

**The step.** The multiple train is a *periodic repetition* of the primary sequence
at lag $T_w$, with a known (if variable) reflection coefficient. Its autocorrelation
therefore has a peak at lag $T_w$, and that peak is present for *every* arrival in
the record. So:

1. Compute the autocorrelation of the vertical channel over a window containing
   several multiples.
2. Locate the peak at lag $T_w$ and refine it by parabolic interpolation.
3. Convert to depth with $h = cT_w/2$, and stack the estimate over the whole
   deployment (many windows) to reduce the error.

**Why this is better than picking the multiples by hand.** The autocorrelation
sums the coherent contribution of every multiple of every arrival, so the precision
of $T_w$ improves with the number of arrivals rather than with the amplitude of one
of them. It is also robust to the seafloor reflection coefficient, which appears as
a *weighting* of the peak rather than as a requirement to identify individual
bounces.

**The assumption it requires.** That the seafloor reflection coefficient is
**constant over the record**, or at least that its variation does not move the peak.
This matters more than it looks: the coefficient varies with angle and with
frequency, so an event arriving at a different angle has a differently weighted
comb. The defence is to run the estimate in windows, per event, and to treat the
scatter across events as the uncertainty. A second, smaller assumption is that the
sound speed profile — and therefore the effective $c$ in $T_w$ — is stable, which it
is over a deployment but not over a season, so the estimate is an average over the
deployment's season and should be reported as such.

**A useful by-product.** Once $T_w$ is known to better than the sampling interval,
the multiple train can be predicted and subtracted with a small number of
parameters — turning the nuisance of Section 2 of the lesson into a well-posed
deghosting operator. The same autocorrelation estimate that measures the bathymetry
supplies the operator's timing.
