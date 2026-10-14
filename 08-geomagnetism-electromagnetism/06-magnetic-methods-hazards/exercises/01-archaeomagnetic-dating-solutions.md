# Solutions — 08-06-01 Archaeomagnetic Dating and Secular Variation Curves

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [01 Archaeomagnetic Dating](../01-archaeomagnetic-dating.md).

---

## ★1 — GAD inclinations

$$\tan I=2\tan\lambda.$$

- $\lambda=20^\circ$: $2\tan20^\circ=2(0.36397)=0.72794$, $I=36.046^\circ$.
- $\lambda=37^\circ$: $2\tan37^\circ=2(0.75355)=1.50710$, $I=56.428^\circ$.
- $\lambda=55^\circ$: $2\tan55^\circ=2(1.42815)=2.85630$, $I=70.693^\circ$.

**Check against the lesson's table:** at $45^\circ$ the relation gives
$\arctan2=63.435^\circ$, exactly the tabulated value; at $30^\circ$ it gives
$49.107^\circ$, also matching. The relation is exact for a centred dipole, so these
are not approximations to a measurement but a prediction of the model.

---

## ★2 — Consistency at $37^\circ$

GAD expectation: $I=56.428^\circ$ (★1). Measured $I=45.0^\circ$. Difference
$11.4^\circ$.

That is **not** consistent with no tilt at a $1$–$2^\circ$ measurement uncertainty:
the site, the material or its orientation is wrong. The candidates, in the order a
practitioner checks them: (1) the site's latitude was mis-stated or the *palaeo*-latitude
is not the present one (a $10^\circ$ latitude change moves the GAD inclination by
about $15^\circ$); (2) the sample was not oriented correctly in azimuth or was
mis-tilted; (3) the material carries a secondary component that the demagnetisation
did not isolate; (4) the field at that epoch was far from the GAD direction — which
the non-dipole field can do, though $11^\circ$ of inclination is large.

**The point of the exercise:** the GAD relation is a *consistency* test, not a date.
An inconsistent inclination is a red flag about the data, not a measurement of
latitude.

---

## ★3 — Precision bound

$$\sigma_t=\frac{s}{R}=\frac{0.5^\circ}{4^\circ\ \text{per century}}
=0.125\ \text{century}=12.5\ \mathrm{yr}.$$

Reported uncertainty will be larger because (i) the reference curve itself has an
envelope, typically of the same order as the measurement error, and it enters in
quadrature or by cross-correlation; (ii) the rate of change $R$ varies along the
curve, so the conversion is only valid locally and the epoch may lie where the
direction is turning; (iii) the measurement error is not purely angular — an error
in the sample's tilt, or in the field orientation, adds a systematic component;
(iv) if the curve passes the direction more than once, the *interval* is larger than
$\pm\sigma_t$, because it includes the whole neighbourhood of both crossings.
**A precision is a local statement about the curve, and the interval is the
honest output.**

---

## ★4 — Two admissible intervals

The data determine two candidate dates, $-1200$ to $-1050$ and $-350$ to
$-150\ \mathrm{yr\,BP}$, i.e. a warm or a recent option. In increasing order of
cost:

1. **Stratigraphy** (free, if the excavation is controlled): the material's layer
   relative to an already-dated layer. If the structure is sealed by a deposit that
   cannot be younger than $1000\ \mathrm{yr\,BP}$, the recent option is excluded.
2. **A second sample of a different material** from the same structure (cheap):
   its independent measurement error and its own demagnetisation behaviour test
   whether the direction is robust.
3. **Radiocarbon on associated organic material** (moderate): independent of the
   magnetic method, and its own calibration uncertainty must be propagated.
4. **A second independent physical dating method** on the same material —
   thermoluminescence or optically stimulated luminescence (expensive): dates the
   last heating, which is precisely the event the magnetic direction dates, but it
   costs sample, laboratory time and money.

The cheapest evidence that *cannot* resolve the ambiguity is a better magnetic
measurement: a more precise direction narrows both intervals but does not merge or
select them, because both are genuine crossings of the same curve.

---

## ★5 — Bias from a curve offset

At $R=2^\circ$ per century, a $2^\circ$ offset corresponds to
$2/2=1$ century $=100\ \mathrm{yr}$ of apparent age shift — but only if the offset
acts along the direction of motion. If the offset is perpendicular to the motion, it
does not shift the crossing at all; the general statement is that the bias is
$e/|\mathrm{d}\hat{n}/\mathrm{d}t|$ where $e$ is the component of the offset along
the direction of travel of the curve.

At $R=8^\circ$ per century the same $2^\circ$ offset gives
$2/8=0.25$ century $=25\ \mathrm{yr}$. So **the same physical offset costs four
times less at the fast-moving epoch**: the bias from a curve error is inversely
proportional to the local rate of change, exactly like the measurement error, since
both are angular errors converted to time by $1/R$.

Above some size the bias stops being a shift and becomes a branch jump: the lesson's
demonstration shows a $4^\circ$ offset moving the date by $-575\ \mathrm{yr}$ at an
epoch where the neighbouring crossing is only a few degrees away in direction space.

---

## ★6 — A $5^\circ$ tectonic rotation

A clockwise rotation by $5^\circ$ changes the *recorded declination* by
$+5^\circ$ (if the block rotates clockwise as seen from above, the sample's
reference direction rotates with it, so the recorded declination measured in
present-day coordinates shifts by an equal amount in the corresponding sense).

What it does to the age: the determined age is biased by
$5^\circ/R$ where $R$ is the rate of change of declination (or, more precisely, the
component of the curve's motion along the direction of the offset, as in ★5). At
$R=2^\circ$ per century that is $250\ \mathrm{yr}$ — larger than the measurement
error, and enough to move a date across an archaeological period boundary. At
$R=8^\circ$ per century it is $63\ \mathrm{yr}$.

The important asymmetry: an *inclination* test (★2) does not detect a rotation about
a vertical axis, and the GAD relation constrains only inclination. So a tectonic
rotation is invisible to the check in ★2 and must be detected independently —
structurally, regionally, or by comparing an archaeomagnetic date with an
independent one from the same site.

---

## ★7 — Designing a curve campaign

**Materials.** Prefer materials whose last heating is well defined and whose
remanence is thermally stable: kiln floors and walls, hearth linings, oven bases,
furnace linings, burnt clay with an adequate magnetite/haematite content. Exclude
loose sediment unless carefully oriented and sampled in a known reference frame,
because its depositional remanence shallows the inclination.

**Reference structures.** The curve needs *independently and tightly dated* points.
A workable design: at least three independently dated structures per century
interval (typical historical dating, dendrochronology or radiocarbon with
independent constraints), giving about $30$ reference points for $3000$ years, each
contributing a direction with its own uncertainty, and enough overlap in space
(within a few hundred kilometres) that the non-dipole field is shared.

**Propagating the envelope.** For each reference point, combine the measurement
error (typically $1$–$2^\circ$ per component) with the dating uncertainty (converted
to an *angular* uncertainty through the local rate of change, $e=R\sigma_t$) and
with the site's structural correction uncertainty (tilt and rotation). Then fit a
smooth curve (a spline or a Bayesian time series) through the points and report the
posterior envelope at each epoch; the envelope is the output, not a decoration.

**Usability criterion.** Declare the curve usable for an epoch when (i) the envelope
is narrower than the difference between distinct branches of the curve (so the
direction-to-age map is locally single-valued), and (ii) the local rate of change
exceeds a stated threshold, e.g. $1^\circ$ per century, above which the age
precision is better than $100\ \mathrm{yr}$ for a $1^\circ$ measurement. Publish the
epochs where the criterion fails; a still-stand must be declared, not smoothed over.

---

## ★8 — Reporting a date as a construction date

A defensible paragraph:

> The structure yielded a mean archaeomagnetic direction of
> $D=...,\ I=...$ ($\alpha_{95}=...^\circ$), which the [name] regional
> secular-variation curve admits at $1500\pm50\ \mathrm{yr\,BP}$. This dates the
> last heating of the sampled material to that interval. Two uncertainties dominate:
> (i) the reference curve's own envelope for this epoch, equivalent to
> $\pm...\ \mathrm{yr}$; and (ii) the possibility of a local rotation or tilt of the
> block, which is not detectable from the inclination alone and which we have tested
> by [structural measurement / comparison with an independent date from the same
> site]. The interpretation of this date as the construction date of the building
> rests on the stratigraphic argument that [the heated material is sealed by ...,
> and no later heating feature is present]; the single observation that would most
> improve the claim is an independent radiocarbon or luminescence date from the same
> sealed context, which would test the calibration rather than the measurement.

The two largest uncertainties: the curve's envelope (not the measurement error) and
the unrecognised rotation/tilt. The one observation that would most improve it: an
independent date from the same context.
