# Solutions — 20-06-01 Particle Motion Analysis and Polarisation Attributes

> Read after attempting. Numbers computed. Lesson:
> [01 Particle Motion](../01-particle-motion.md).

---

## ★1 — Attributes from eigenvalues

$$R = 1 - \frac{\lambda_2+\lambda_3}{2\lambda_1}
= 1 - \frac{1.0+0.0}{2(9.0)} = 1 - 0.0556 = 0.9444,$$
$$P = 1 - \frac{2\lambda_3}{\lambda_1+\lambda_2}
= 1 - \frac{0}{10.0} = 1.000 .$$

$R$ near 1 with $P = 1$ means motion confined to a plane **and** nearly along a
line — a linearly polarised body wave (P or S), not a surface wave.

---

## ★2 — Azimuth and incidence

$$\phi = \operatorname{atan2}(0.3536,\ 0.3536) = 45^\circ
\pmod{180^\circ}, \qquad
\iota = \arccos|0.8660| = 30.0^\circ .$$

The azimuth is an axis: $45^\circ$ and $225^\circ$ are the same polarisation, so
the reportable range is $[0^\circ, 180^\circ)$.

---

## ★3 — Circular motion

For a circle $b = a$, so $R = 1 - b^{2}/(2a^{2}) = 0.5$ and $P = 1$.

The principal eigenvector is arbitrary within the plane of the circle, so the
azimuth is **undefined**: a circular motion has no preferred axis. The
demonstration measures an azimuth scatter of about $50^\circ$–$57^\circ$ at every
SNR, which is the signature of a uniform distribution on $[0^\circ,180^\circ)$
($180^\circ/\sqrt{12} = 52.0^\circ$).

---

## ★★4 — Azimuth error at SNR 4

Order-of-magnitude result: $\delta\phi \sim 1/\mathrm{SNR}$ radians, so

$$\delta\phi \sim \frac{1}{4}\ \mathrm{rad} = 14.3^\circ .$$

**Assumption.** A first-order perturbation of the eigenvector by noise of
amplitude $1/\mathrm{SNR}$ relative to the signal; the exact constant depends on
the noise geometry and the incidence angle, so this is an order-of-magnitude
statement, not a formula.

**Comparison.** The demonstration measured $6.3^\circ$ at SNR 5 and $2.9^\circ$ at
SNR 10; the crude estimate gives $11.5^\circ$ and $5.7^\circ$. The measured values
are about a factor of two smaller, so the scaling is right and the constant is
not — use the estimate for trend reasoning, and calibrate any absolute claim
against a Monte Carlo like the demonstration's.

---

## ★★5 — Ellipse with axial ratio 0.5

$$R = 1 - \frac{b^{2}}{2a^{2}} = 1 - \frac{0.25}{2} = 1 - 0.125 = 0.875 .$$

A Rayleigh wave with axial ratio 0.5 gives $R = 0.875$, which is **higher** than
the $0.755$ of the lesson's $b/a = 0.7$ example — i.e. a more rectilinear
Rayleigh wave overlaps the range where body waves and noise can sit. $R$ alone
therefore does not classify a phase: the ratio $b/a$ must be estimated (from
$R$), and the incidence and azimuth read together, before a surface wave is
claimed. A nearly linear Rayleigh wave ($b/a \to 0$, $R \to 1$) is
indistinguishable from a body wave by $R$ alone.

---

## ★★6 — A rotated sensor

The azimuth is measured in the sensor frame. A sensor rotated by
$+\theta$ reports an azimuth smaller by $\theta$ (from the demonstration's table:
$+10^\circ$ rotation shifted the reported azimuth by $-10^\circ$). A true
back-azimuth of $60^\circ$ with a $+15^\circ$ rotation is reported as

$$60^\circ - 15^\circ = 45^\circ .$$

**Correction.** The shift can be corrected *if and only if* an independent
estimate of the orientation exists — a gyroscopic or compensated-borehole
heading, a known calibration event, or the arrival's known back-azimuth from the
event location and a well-constrained velocity model. It **cannot** be corrected
from the three-component data alone, because no absolute reference direction
enters a covariance eigen-decomposition.

---

## ★★★7 — A polarisation phase detector

**Features** (computed on a sliding window of $N_w$ samples, after mean removal
and band-pass filtering):

1. rectilinearity $R$;
2. planarity $P$;
3. the principal-eigenvalue share $\lambda_1/(\lambda_1+\lambda_2+\lambda_3)$;
4. the azimuth angle and its consistency between adjacent windows.

**Decision rule.** Declare a candidate body-wave phase when
$R > 0.85$, $\lambda_1/(\sum\lambda) > 0.5$ and the azimuth changes by less than
$20^\circ$ between consecutive windows; classify P vs S by the incidence
($\iota < 50^\circ$ strongly vertical; $>\ 50^\circ$ strongly horizontal for an
S arrival at typical distance ranges). Declare a surface wave when $P > 0.95$ and
$R$ sits in the elliptical band $0.5$–$0.9$ while the incidence stays near
$90^\circ$.

**Window length.** A few cycles of the dominant signal period; long enough for
stable eigenvalues, short enough not to mix phases. The demonstration's lesson is
the cost of getting this wrong: mixing a P and an S into one window depressed $R$
from $0.99$ and $0.93$ to $0.83$ and shifted the azimuth to a value corresponding
to no physical direction.

**Failure modes and their measurement.**

- *Mixed window.* Detect by scanning $N_w$; a detector whose $R$ falls sharply as
  $N_w$ grows is mixing phases, and the fix is a shorter window.
- *Channel phase mismatch.* Instrument-response differences turn a line into an
  ellipse and depress $R$ everywhere. Detect by checking $R$ on a known
  impulsive calibration event, or by cross-correlating channel pairs for a
  non-zero lag.

---

## ★★★8 — $R = 0.62$, $P = 0.99$

Candidates, most likely first:

1. **Elliptical surface wave** (Rayleigh) — $P=1$ is expected and $R = 0.62$
   corresponds to a near-circular ellipse, $b/a \approx \sqrt{2(1-R)} = 0.87$;
2. **A window containing a body wave plus a surface wave** — the planar part
   dominates $P$, and the body wave's linear part and the ellipse together give
   an intermediate $R$;
3. **Anisotropy or a dipping interface**, producing a genuine elliptical
   polarisation of a converted phase — much less common than (1) or (2);
4. **Instrument or orientation problems** — a channel phase mismatch, giving a
   spurious ellipse.

**Distinguishing (1) from (2).** Scan the window length and the start time.
Case (1) is stable: $R \approx 0.62$ and azimuth $\approx$ constant for every
window inside the wave train, and the azimuth is stable as the window slides.
Case (2) is not: a window late in the record (containing only the surface wave)
returns a lower $R$ and a different azimuth, and a window early in the record
(only the body wave) returns $R \to 1$. The time dependence of the attributes is
the discriminator, and it is also what distinguishes surface waves from body
waves in routine processing: **a surface wave is dispersive, so its attributes
are frequency-dependent as well as time-dependent.** Add a narrow-band filter at
two frequencies; a Rayleigh wave's $R$ and azimuth change with frequency while a
body wave's do not.
