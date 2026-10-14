# Solutions — 05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling

> **Read this after attempting the exercises, not before.**

---

## ★1 — Deriving the fold formula

Per shot, a split spread places $N$ midpoints spaced $\Delta x/2$ apart, so the
number of midpoint positions falling inside a bin of width $b$ is
$\dfrac{\Delta x/2}{b} = \dfrac{\Delta x}{2b}$.

The midpoint coverage of one shot spans $N\Delta x/2$ along the line. Consecutive
shots advance the coverage by $\Delta s$, so the number of shots whose coverage
includes a given bin is $\dfrac{N\Delta x/2}{\Delta s} = \dfrac{N\Delta x}{2\Delta s}$.

Multiplying:

$$\text{fold} = \frac{N\Delta x}{2\Delta s}\cdot\frac{\Delta x}{2b}.$$

With $\Delta s = \Delta x$ and $b = \Delta x/2$:

$$\text{fold} = \frac{N\cancel{\Delta x}}{2\cancel{\Delta x}}\cdot
\frac{\cancel{\Delta x}}{2(\cancel{\Delta x}/2)} = \frac{N}{2}\cdot 1 = \frac{N}{2}.
\ \boxed{}$$

This matches the lesson's measurement for every $N$ tried (24 → 12, 48 → 24,
96 → 48, 192 → 96).

---

## ★2 — A 120-channel spread

- fold $= \dfrac{120 \times 25}{2 \times 25}\cdot\dfrac{25}{2 \times 12.5}
  = 60 \times 1 = \boxed{60}$.
- maximum offset $= N\Delta x/2 = 120 \times 25/2 = \boxed{1500\ \mathrm{m}}$.
- traces per shot $= N = \boxed{120}$.

Note that the shot interval equals the receiver interval, so the second factor is
exactly 1. Raising the shot interval to 50 m would halve the fold to 30 without
changing the cost per shot — the point of the lesson's worked example 6.1.

---

## ★3 — What geometry decides

1. **Where the samples are** (station spacing and bin size) — sets the aliasing
   limit through $k_N = \pi/\Delta x$.
2. **How many samples per estimate** (fold) — sets the noise through
   $\sigma/\sqrt{\text{fold}}$.
3. **Which offsets and azimuths were sampled** — sets whether a target at depth can
   be illuminated and located in three dimensions, and whether velocity and
   anisotropy can be constrained.

---

## ★4 — Depth and offset

**(a)** Depth $= v t_0/2 = 3000 \times 1.2/2 = \boxed{1800\ \mathrm{m}}$.

**(b)** $x_{\max} \gtrsim v t_0 = 3000 \times 1.2 = \boxed{3600\ \mathrm{m}}$. Note
that this is twice the depth; the rule as stated in the lesson is deliberately
generous, to leave moveout measurable. A tighter criterion, $x_{\max}\gtrsim
\tfrac12 v t_0 = 1800$ m, equals the depth.

---

## ★5 — Fold and the Fresnel zone

The Fresnel zone is set by the wavelength and the depth,
$r_F = \sqrt{\lambda h/2}$, and neither depends on the number of traces recorded
in a bin: fold improves the *noise*, and the Fresnel zone is the *physical*
illumination footprint.

---

## ★★6 — The taper at a target

The measured ramp per end is 925 m (predicted $N\Delta x/2 - \Delta s = 940$ m). A
target 500 m from the end therefore lies **entirely inside the taper**, at a fold
that ramps from 1 trace at the line end toward 48.

Remedies:

1. **Extend the line** by at least the ramp length (about 1 km) beyond the target
   at each end, so the target sits in the full-fold interior. Cost: extra
   acquisition for no target coverage.
2. **Move the target to the middle** of the profile when the line position is under
   the survey designer's control (e.g. a survey laid out over a known prospect).
3. (A third, partial remedy) **Increase the channel count** so that the full-fold
   *interior* grows faster than the ramp; note from the lesson that both fold and
   maximum offset grow with $N$, so this is expensive.

---

## ★★7 — Two point masses

**(a)** $s = 300\ \mathrm{m} < h = 400\ \mathrm{m}$, so $s/h = 0.75$ and the field
shows **a single anomaly** — the midpoint value equals the maximum.

**(b)** $s/h = 900/400 = 2.25$. Interpolating the measured table (0.648 at
$s/h = 2$, 0.331 at $s/h = 3$) gives roughly 0.55. The saddle is now clear, so the
pair is resolvable.

**(c)** Upward continuation **makes it harder**. Continuing upward by 200 m is
equivalent to measuring the same bodies from a greater distance: the field of each
body is attenuated by roughly $(h/(h+\Delta z))^{3}$ (measured in
[05-06-05](../../06-data-processing-principles/05-merge-and-regularisation.md) as
0.578 for a 100 m continuation of a 500 m body), and the separation measured in
units of the *new* effective depth $h+\Delta z$ falls. So the critical separation
$s_{\text{crit}} = h_{\text{effective}}$ rises while $s$ is fixed: a pair that was
resolvable becomes marginal.

---

## ★★8 — Is a 2-D line sufficient?

The body's horizontal extent is comparable to its depth (800 m), which is exactly
the case where a single line cannot be guaranteed to pass over the anomaly peak.
A 2-D line measures a *slice* of the field, so:

- the peak amplitude is under-estimated if the line misses the centre;
- **the specific artefact is sideswipe**: energy from the off-line body arrives from
  outside the assumed vertical plane, and 2-D processing places it on the line at a
  wrong position and depth, producing a spurious event or a mislocated anomaly.

The lesson's measured two-body limit adds a second, independent reason: bodies closer
than one body depth merge, so a single line may also fail to separate neighbouring
features. A 3-D array is justified when the target size is comparable to its depth,
which is the case here.

---

## ★★9 — Fresnel zone and aliasing

**(a)** $r_F = \sqrt{\lambda h/2} = \sqrt{60 \times 1500/2} = \sqrt{45\,000}
= \boxed{212.1\ \mathrm{m}}$.

**(b)** Diameter $= 424.3$ m.

**(c)** Aliasing requires $\Delta x \le \lambda/2 = \boxed{30\ \mathrm{m}}$ at the
minimum, and 15 m for the four-sample practice. The resolution requirement is
entirely different: it is the Fresnel-zone diameter, 424 m. **Receiver spacing
below the aliasing limit does not improve the image resolution** — it only ensures
that the recorded wavefield can be reconstructed without the 60 m component folding
to a longer wavelength.

---

## ★★★10 — A 3-D template measurement

A satisfactory answer will:

1. **Build the geometry explicitly** — a receiver patch (say $8 \times 8$ stations
   at 25 m), a shot line offset from the patch, and the shot interval; then move the
   template across the survey area.
2. **Bin by CMP** in two horizontal coordinates, and count traces per bin.
3. **Report** the fraction of bins reaching the nominal fold, and the offset/azimuth
   distribution as histograms (offset classes × azimuth classes).
4. **Expect** a non-uniform azimuth distribution concentrated near the template's
   dominant direction, and a fold that varies across the template.
5. **Design changes:** (i) increase the number of parallel shot lines to widen the
   azimuth range; (ii) widen the receiver patch relative to the shot interval to
   raise the near-offset fold. Both increase the channel count and the shot count
   respectively, i.e. both cost money in proportion to the improvement in coverage
   uniformity. A good answer quantifies the number of extra shots or channels.

---

## ★★★11 — The discrepancy in the measured $s_{\text{crit}}$

The scan used 4001 separations between $0.90h = 270$ m and $1.10h = 330$ m, so the
separation step is

$$\delta s = \frac{60}{4000} = 0.015\ \mathrm{m}.$$

The profile is 120 001 points over 6000 m, so the grid step is
$\delta x = 6000/120000 = 0.05$ m, and the maximum of the sampled field is located
to within $\pm 0.025$ m. The measured criterion "midpoint ratio $< 0.99999$" is
itself a threshold on a quantity that varies as $\mathcal{O}(\delta x^{2})$ near the
transition, so the located transition is uncertain by a few tenths of a metre from
discretisation alone.

The measured 301.06 m differs from 300.00 m by 1.06 m, which is about $70\delta s$
and $21\delta x$ — **larger than the discretisation error of the search itself**. So
the discrepancy is not explained by the grid of separations. The real cause is that
the condition implemented in the demo is not the exact curvature criterion but a
detection threshold on the sampled ratio, and the sampled peak can sit at a point
where the true function is still increasing; the extra offset is then consumed before
the ratio drops below $0.99999$. A tighter threshold (e.g. $1 - 10^{-9}$) or an
analytic curvature test would reduce the discrepancy. The honest statement is that
the numeric check confirms the *analytic* value to about 0.4 %, and that a claim of
agreement to three figures would need a different test.

---

## ★★★12 — Distinguishing $h$ from $\sqrt{2}h$

**Analytic condition.** With
$g(x) = GMh\left[(x-h_s)^{2}+h^{2}\right]^{-3/2}$ for a single body (here $h_s$ is a
horizontal offset, not to be confused with depth $h$), the summed field of two equal
masses at $x = \pm s/2$ is $G_{\text{tot}}(x) = g(x-s/2) + g(x+s/2)$. Its curvature
at the origin is $2\,g''(s/2)$, and

$$g''(u) = GMh\left[-3(u^{2}+h^{2})^{-5/2} + 15u^{2}(u^{2}+h^{2})^{-7/2}\right]
= 3GMh\,(u^{2}+h^{2})^{-7/2}\left[5u^{2} - (u^{2}+h^{2})\right].$$

Setting $u = s/2$ and requiring $G_{\text{tot}}''(0) = 0$:

$$5\frac{s^{2}}{4} - \left(\frac{s^{2}}{4}+h^{2}\right) = 0
\ \Longrightarrow\ s^{2} - h^{2} = 0
\ \Longrightarrow\ \boxed{s_{\text{crit}} = h}.$$

So the $\sqrt{2}h$ claim is refuted analytically, and the numeric evidence in the
lesson (301.06 m at $h = 300$ m) is consistent with $h$.

**Numerical verification.** For $s/h = 0.9$: $s = 270$ m,
$u = 135$ m, and $5u^{2}-(u^{2}+h^{2}) = 5(18225) - (18225+90000) = 91125 - 108225
= -17100 < 0$ → curvature **negative**, so $x=0$ is a **local maximum**: the pair is
merged. For $s = h = 300$ m: $u = 150$,
$5(22500) - (22500+90000) = 112500 - 112500 = 0$ → **zero curvature**: the transition
point. For $s/h = 1.1$: $u = 165$,
$5(27225) - (27225 + 90000) = 136125 - 117225 = +18900 > 0$ → curvature **positive**,
so $x=0$ is a **local minimum**: the pair is resolved. The three sign changes bracket
the transition exactly at $s = h$, as the measurement in the lesson records.
