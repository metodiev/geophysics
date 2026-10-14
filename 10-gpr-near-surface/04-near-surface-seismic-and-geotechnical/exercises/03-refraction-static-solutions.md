# Solutions — 10-04-03 Near-Surface Refraction for Static Corrections

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that is
> said. All models are **SYNTHETIC**.

Lesson: [03 Near-Surface Refraction for Static Corrections](../03-refraction-static.md).

Two formulas are used throughout:

$$z = \frac{t_i}{2\sqrt{1/v_w^{2}-1/v_r^{2}}},
\qquad
t_w = \frac{i}{2\sqrt{1-(v_w/v_r)^{2}}},$$

where the second is the weathering *time* $z/v_w$ written directly in terms of the
intercept time. Deriving it once: substituting the first into $z/v_w$ gives
$t_w = t_i/(2v_w\sqrt{1/v_w^2-1/v_r^2}) = t_i/(2\sqrt{1-v_w^2/v_r^2})$.

---

## ★1 — Weathering depth

$$1/v_w^{2} = 1/500^{2} = 4.0000\times10^{-6}\ \mathrm{s^2\,m^{-2}},$$
$$1/v_r^{2} = 1/1600^{2} = 3.90625\times10^{-7}\ \mathrm{s^2\,m^{-2}},$$
$$\text{difference} = 3.609375\times10^{-6},\qquad
\sqrt{\cdot} = 1.90010\times10^{-3}\ \mathrm{s\,m^{-1}},$$

$$z = \frac{9.5\times10^{-3}}{2(1.90010\times10^{-3})} = 2.5002\ \mathrm{m}.$$

Units: the slowness difference is $\mathrm{s^2\,m^{-2}}$, its square root
$\mathrm{s\,m^{-1}}$, and $\mathrm{s}/(\mathrm{s\,m^{-1}}) = \mathrm{m}$.

---

## ★2 — A $4\ \mathrm{ms}$ systematic static error

$$A(f) = \cos(2\pi f\,\Delta t), \qquad \Delta t = 4.0\times10^{-3}\ \mathrm{s}.$$

| $f$ (Hz) | $2\pi f\Delta t$ (rad) | $A$ |
|---|---|---|
| $25$ | $0.6283$ | $0.8090$ |
| $50$ | $1.2566$ | $0.3090$ |
| $100$ | $2.5133$ | $-0.8090$ |

**The $50\ \mathrm{Hz}$ band is the casualty**: $69\%$ of its amplitude is lost,
because $4\ \mathrm{ms}$ is a quarter of the $50\ \mathrm{Hz}$ period ($20\
\mathrm{ms}$) — a quarter-period shift puts the stacked wavelet a quarter cycle out
of phase, where the sum of cosines cancels. At $100\ \mathrm{Hz}$ the shift is half
a period and the factor is **negative**: the amplitude is restored *with reversed
polarity*, which on a section looks like a bright event rather than a lost one.
A $4\ \mathrm{ms}$ static error is therefore not "a small shift"; it is a
frequency-selective filter, and at the top of the band it is a sign change.

---

## ★3 — A datum static, term by term

$z_w = 4.5\ \mathrm{m}$, $v_w = 550\ \mathrm{m\,s^{-1}}$, elevation $3.0\
\mathrm{m}$ above the datum so $d = 3.0\ \mathrm{m}$, $v_{\mathrm{rep}} = 2200\
\mathrm{m\,s^{-1}}$.

$$\text{weathering term} = \frac{z_w}{v_w} = \frac{4.5}{550}
= 8.1818\times10^{-3}\ \mathrm{s} = 8.1818\ \mathrm{ms},$$

$$\text{replacement term} = \frac{z_w-d}{v_{\mathrm{rep}}} = \frac{1.5}{2200}
= 6.8182\times10^{-4}\ \mathrm{s} = 0.6818\ \mathrm{ms},$$

$$t_{\mathrm{stat}} = 8.1818 - 0.6818 = 7.5000\ \mathrm{ms}.$$

**If the datum were placed at the base of the weathering** ($d = z_w = 4.5\
\mathrm{m}$), the replacement term would be exactly zero and
$t_{\mathrm{stat}} = z_w/v_w = 8.1818\ \mathrm{ms}$ — the pure weathering
correction. That limit is the check that the sign convention of Section 3.2 is
right: a datum at the base of the weathering leaves nothing to replace, so the
replacement term must vanish.

---

## ★4 — Depth error versus static error, $v_w = 660$ for a true $600$

**Intercept time** (fixed by the data, from the true layer):

$$t_i = 2(3.5)\sqrt{1/600^{2}-1/1800^{2}} = 7(1.57144\times10^{-3})
= 10.999\ \mathrm{ms}.$$

**Depth from the wrong velocity:**

$$z = \frac{0.010999}{2\sqrt{1/660^{2}-1/1800^{2}}}
= \frac{0.010999}{2(1.44294\times10^{-3})} = 3.9015\ \mathrm{m},$$

against $3.500\ \mathrm{m}$: **$+11.47\%$**.

**Weathering time:**

$$t_w(600) = \frac{0.010999}{2\sqrt{1-(600/1800)^{2}}} = \frac{0.010999}{1.885618}
= 5.8333\ \mathrm{ms},$$

$$t_w(660) = \frac{0.010999}{2\sqrt{1-(660/1800)^{2}}} = \frac{0.010999}{1.860700}
= 5.9114\ \mathrm{ms},$$

so the error in the quantity the static actually uses is **$+0.0781\ \mathrm{ms}$**.

**Stack factors** for that $0.0781\ \mathrm{ms}$:

$$A(40) = \exp\!\left(-2\pi^{2}(40)^{2}(7.81\times10^{-5})^{2}\right) = 0.9998,$$

$$A(80) = \exp\!\left(-2\pi^{2}(80)^{2}(7.81\times10^{-5})^{2}\right) = 0.9992.$$

**Which consequence is noticed first, and why the answer is uncomfortable.** Neither,
from the section: a $0.02\%$ amplitude change is invisible. The $11.5\%$ depth error
is also invisible on the stack, and appears only where the weathering depth is
*used* — a shallow structural interpretation, a depth conversion, a drilling-depth
prediction. **The uncomfortable part is that the error is silent in the very product
(statics) that is inspected most closely.** The one place it shows is the
$80\ \mathrm{Hz}$ residual after a residual-statics pass at a level
($0.08\%$) far below anything a processor can measure, so the detection has to be
geological or borehole-based, not amplitude-based.

---

## ★5 — Two solutions differing by a constant

**(a)** Add $c = 8.0\ \mathrm{ms}$ to every source term and subtract it from every
receiver term:

$$(s_i + c) + (r_j - c) = s_i + r_j = T_{ij}
\quad\text{for every pair, exactly.}$$

The residual difference is zero in exact arithmetic and of order $10^{-18}\
\mathrm{s}$ in double precision (the lesson's demonstration measures
$1.7\times10^{-18}\ \mathrm{s}$ for $c = 5\ \mathrm{ms}$). Both solutions fit the
data equally well; the data cannot choose.

**(b)** Apparent depth difference:

$$\delta z = \frac{v\,\delta t}{2} = \frac{3000(0.0080)}{2} = 12.0\ \mathrm{m}
\;\text{(one solution relative to the other)}.$$

Note carefully what is and is not affected: a *constant* added to all source terms
and subtracted from all receiver terms shifts the whole section's time zero but
leaves the *relative* geometry unchanged, so a constant of that form is harmless
for structure and fatal for anything tied to an absolute time (a datum, a well tie,
a cross-line merge).

**(c)** The measurement that fixes it is any **absolute** reference: the datum and
replacement velocity of Section 3.2, an uphole time, a borehole check shot, or a
refraction solution that yields an absolute weathering time. That is the entire
reason a statics workflow carries a datum and a replacement velocity rather than
just a set of relative shifts.

---

## ★6 — Systematic against random, $2.0\ \mathrm{ms}$

$$A_{\text{syst}} = \cos(2\pi f\Delta t), \qquad
A_{\text{rand}} = \exp(-2\pi^{2}f^{2}\sigma_t^{2}),
\qquad \Delta t = \sigma_t = 2.0\times10^{-3}\ \mathrm{s}.$$

| $f$ (Hz) | $2\pi f\sigma_t$ (rad) | systematic $\cos$ | random Gaussian |
|---|---|---|---|
| $30$ | $0.3770$ | $0.9298$ | $0.9314$ |
| $60$ | $0.7540$ | $0.7290$ | $0.7526$ |
| $120$ | $1.5080$ | $0.0628$ | $0.3208$ |

**The random error is worse at $60$ and $120\ \mathrm{Hz}$**, by a factor of $1.03$
and $5.1$ respectively; at $30\ \mathrm{Hz}$ the two are equal to $0.2\%$.

**Why they agree at low frequency and diverge at high.** For a small argument the
two functions are the same to second order:

$$\cos x = 1-\frac{x^{2}}{2}+O(x^{4}), \qquad
e^{-x^{2}/2} = 1-\frac{x^{2}}{2}+O(x^{4}),
\qquad x = 2\pi f\sigma_t.$$

The agreement is therefore exact in the limit $x \to 0$ and fails as $x$ grows —
and $x$ is the shift measured in radians of phase, so the same $2\ \mathrm{ms}$
is $0.377\ \mathrm{rad}$ at $30\ \mathrm{Hz}$ and $1.508\ \mathrm{rad}$ at
$120\ \mathrm{Hz}$. Beyond $x \approx 1$ the cosine begins to *reverse* (it
crosses zero at $x = \pi/2$, i.e. at a quarter of the wavelet period, and reaches
$-1$ at $x = \pi$), whereas the Gaussian merely decays. The two errors are
therefore not interchangeable anywhere near the top of the band, and only the
random one can be measured from the data by a stack-power criterion, because
misalignment is all it leaves behind.

---

## ★7 — A workflow for a $5\ \mathrm{km}$ line over $15\ \mathrm{m}$ of relief

**Requirement:** the weathering thickness varies $1$–$8\ \mathrm{m}$; the section
must not acquire the topographic relief mimics. Specify:

1. **Acquisition for the weathering velocity.** Shot and receiver spacing of
   $5\ \mathrm{m}$ with a $240\ \mathrm{m}$ spread in a split-spread geometry,
   reversed shots every $100\ \mathrm{m}$, and the first-arrival picks carried out
   to offsets at least four times the expected maximum thickness
   ($\approx 32\ \mathrm{m}$), i.e. well beyond the crossover. The weathering
   velocity is the near-offset slope of the travel-time curve, and it must be
   determined *per shot* to track lateral change, since the exercise's $1$–$8\
\mathrm{m}$ range implies a variable weathering. Where topography breaks the
   line, dips of the refractor require the plus-minus formulation, which is why
   reversed shots are mandatory, not optional.
2. **The absolute level.** A datum elevation and a documented replacement velocity,
   plus at least one uphole or borehole measurement of the *weathering time* per
   kilometre. The uphole is what fixes the constant of Section 3.4; without it the
   profile is only relative.
3. **The long-wavelength shape.** Refraction tomography over the whole line with the
   uphole times as hard constraints, rather than a station-by-station two-layer
   solution whose long-wavelength part is exactly what the reflection data cannot
   check. Reversing the tomographic profile is the check that the solution is
   consistent with both shot directions.
4. **Verification band.** $30$–$80\ \mathrm{Hz}$: below $30\ \mathrm{Hz}$ a
   3–4 ms error is invisible ($\cos$ factor near $1$), and above
   $80\ \mathrm{Hz}$ the migrated section is band-limited by absorption and by the
   source anyway. The residual-statics pass is run on the $30$–$80\ \mathrm{Hz}$
   band, and the acceptance criterion is a residual with no spatial correlation
   with the weathering thickness or with the topography.
5. **The independent end check.** Re-occupy one uphole location and one shot
   position at the end of the line, and compare the static profile with the beginning:
   a difference beyond the timing repeatability invalidates the profile, and a check
   for the *spatial* correlation of the residuals with the topography is the
   specific test that catches a wrong replacement velocity.

**What would invalidate it.** A weathering velocity that varies faster laterally
than the reversed-shot interval, or a low-velocity layer within the weathered zone
(the blind zone of ★8, which the travel-time curve cannot reveal, so that the
uphole measurement becomes the *only* defence).

---

## ★8 — The blind zone: a large depth error with an almost silent stack

**Intercept time** from the true layer ($v_w = 450\ \mathrm{m\,s^{-1}}$,
$z = 3.0\ \mathrm{m}$, $v_r = 1800\ \mathrm{m\,s^{-1}}$):

$$t_i = 2(3.0)\sqrt{1/450^{2}-1/1800^{2}} = 6(2.15171\times10^{-3})
= 12.910\ \mathrm{ms}.$$

**Depth from the fitted velocity** $600\ \mathrm{m\,s^{-1}}$:

$$z_{\text{fit}} = \frac{0.012910}{2\sqrt{1/600^{2}-1/1800^{2}}}
= \frac{0.012910}{3.14288\times10^{-3}} = 4.1079\ \mathrm{m},$$

against $3.0\ \mathrm{m}$: **$+36.9\%$** — the blind zone makes the weathering look
a third thicker than it is.

**Weathering time from the fit:**

$$t_{w,\text{fit}} = \frac{0.012910}{2\sqrt{1-(600/1800)^{2}}}
= \frac{0.012910}{1.885618} = 6.8465\ \mathrm{ms},$$

against the true $t_w = 3.0/450 = 6.6667\ \mathrm{ms}$: an error of
**$+0.1799\ \mathrm{ms}$**.

**Stack factors:**

$$A(40) = \exp\!\left(-2\pi^{2}(40)^{2}(1.799\times10^{-4})^{2}\right) = 0.9990,$$

$$A(80) = 0.9959.$$

**Why the stack is a silent witness.** The same wrong velocity is used twice, and
the two errors nearly cancel in $t_w$ (Section 4 of the lesson: a $10\%$ velocity
error moves the depth by $11.5\%$ and the time by $0.08\ \mathrm{ms}$). The
processor sees a $0.1\%$ amplitude change at $40\ \mathrm{Hz}$ — nothing — while the
weathering *depth* is $37\%$ too large. Because the error is systematic and
correlated with the weathering, it does not average out; it becomes a spurious
long-wavelength structure in the shallow section and a systematic error in any
depth conversion that uses the weathering thickness.

**Detection.** The only reliable measurements are *time* measurements through the
weathering: an uphole survey, a borehole with a surface source, or a
down-hole/cross-hole velocity. All three bypass the two-layer inversion whose
assumption is the problem. A "blind-zone" low-velocity layer inside the weathering
cannot be seen by first-arrival refraction at any offset, so more refraction data
do not help.

**What it looks like in a residual-statics map.** A smooth, long-wavelength
anomaly whose shape correlates with the weathering thickness — not with the shot
geometry and not with the receiver spread. That correlation is the diagnostic:
random statics and geometry errors produce patterns tied to the acquisition, while
a near-surface velocity error produces a pattern tied to the *geology*. The further
check is the standard one: apply the statics, then re-run the residual statics and
compare the second set with the first; a near-surface error reappears.

---

## ★9 — Systematic against random, and what a residual-statics pass can estimate

| $f$ (Hz) | $2\ \mathrm{ms}$ systematic | $2\ \mathrm{ms}$ random | $6\ \mathrm{ms}$ systematic | $6\ \mathrm{ms}$ random |
|---|---|---|---|---|
| $30$ | $0.9298$ | $0.9314$ | $0.4258$ | $0.5275$ |
| $60$ | $0.7290$ | $0.7526$ | $-0.6374$ | $0.0774$ |
| $120$ | $0.0628$ | $0.3208$ | $-0.1874$ | $0.0000$ |

Read the two columns separately.

**At small errors ($2\ \mathrm{ms}$) the systematic and random columns are almost
identical** at every frequency — to within $3\%$ at $30\ \mathrm{Hz}$ and a factor
of five at $120\ \mathrm{Hz}$, where both are destroying the band anyway. At small
shifts, and for a zero-phase wavelet, the cosine and the Gaussian agree to
second order in the shift: $\cos x \approx 1-x^2/2$ and
$\exp(-x^2/2) \approx 1-x^2/2$ with $x = 2\pi f\sigma_t$.

**At large errors ($6\ \mathrm{ms}$) they diverge sharply**, and in the direction
that matters: the systematic column goes *negative* (polarity reversal) while the
random column stays positive and small. A systematic error of $6\ \mathrm{ms}$
turns $60\ \mathrm{Hz}$ upside down; a random error of the same rms merely reduces
it to $8\%$.

**What a residual-statics pass can estimate, in terms of the null space.** From
Section 3.4 of the lesson, the surface-consistent model $T_{ij}=s_i+r_j$ determines
the statics up to one constant — so a residual-statics pass can, in principle,
estimate every *relative* static, i.e. the random, short- and medium-wavelength
part, and it does so by maximising stack power. What it cannot estimate is:

1. **the constant** — fixed only by an external absolute reference (a datum, an
   uphole time);
2. **the long-wavelength part that trades with structure** — because a
   long-wavelength static and a depth change move reflections in the same
   direction, and the stack-power objective is nearly indifferent to the trade
   (both hypotheses stack almost equally well);
3. **a systematic static applied to *all* traces equally** — there is no misalignment
   left to measure, because every trace is shifted identically; the stack is
   already aligned and merely wrong.

**The practical conclusion.** A residual-statics pass addresses the random,
short-wavelength part of the error, which is what destroys the stack. The
systematic and long-wavelength parts — the ones that create false structure — must
come from refraction, uphole or borehole measurements, and they must come *before*
the interpretation. Estimating them from the reflection data alone would be
attempting to resolve a trade with the very quantity (structure) that the
reflection data are being used to measure.
