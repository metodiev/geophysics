# Solutions — 15-02-02 Multibeam Bathymetry and Swath Mapping

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [02 Multibeam Bathymetry](../02-multibeam-bathymetry.md).

---

## ★1 — Swath width and outer-beam range at 800 m, 65°

$$W = 2z\tan\theta_{\max} = 2(800)\tan 65^\circ
= 1600 \times 2.14451 = 3431.2\ \mathrm{m},$$

$$R_{\text{outer}} = \frac{z}{\cos\theta_{\max}}
= \frac{800}{\cos 65^\circ} = \frac{800}{0.42262} = 1893.0\ \mathrm{m}.$$

Width-to-depth ratio $= 3431.2/800 = 4.289 = 2\tan 65^\circ$. It is independent of
depth: **the swath is a fixed cone, so coverage grows in proportion to depth and
the across-track sounding spacing does too.**

---

## ★2 — Nadir footprint difference at 800 m

$$\ell_{\text{across}}(0) = z\,\Delta\theta = 800 \times 0.0174533
= 13.96\ \mathrm{m}.$$

Unit: $\mathrm{m} \times \mathrm{rad} = \mathrm{m}$ (a radian is dimensionless), so
the product is a length. ✔

Note that this is the *beam footprint* — the patch of seafloor that
simultaneously contributes to one beam's return. It is not the sounding spacing,
which is set by $\Delta\theta$ between adjacent beam *centres* and is the same
number at nadir only because the beams are contiguous.

---

## ★3 — Sound-speed error is a range error

$$R = \frac{c_{\text{assumed}}\,t}{2}, \qquad
R_{\text{true}} = \frac{c_{\text{true}}\,t}{2}
\;\Longrightarrow\;
\frac{R}{R_{\text{true}}} = \frac{c_{\text{assumed}}}{c_{\text{true}}}.$$

Since $z = R\cos\theta$ and $\theta$ is measured (not derived from $c$), the depth
carries the same ratio:

$$\frac{\delta z}{z_{\text{true}}} = \frac{c_{\text{assumed}} - c_{\text{true}}}
{c_{\text{true}}} = \epsilon . \ ✔$$

**The single assumption** is that the *angle* $\theta$ is not affected by the
sound-speed error. In a real system the beam is steered electronically using an
assumed $c$ at the array, so a wrong $c$ also mis-steers the beam — a second,
smaller, geometry error. The range error is the leading term, and it is the one
that produces a pure scale multiplier.

---

## ★★4 — Derivation and evaluation of the across-track footprint

The beam of angular width $\Delta\theta$ at angle $\theta$ has its two edges at
slant ranges $R_{\pm} = z/\cos(\theta \pm \Delta\theta/2)$. On a flat seafloor their
ground ranges are $g_{\pm} = z\tan(\theta \pm \Delta\theta/2)$, so the footprint is
$g_+ - g_-$. For small $\Delta\theta$,

$$g_+ - g_- \approx \frac{\mathrm{d}}{\mathrm{d}\theta}\left[z\tan\theta\right]
\Delta\theta = \frac{z\,\Delta\theta}{\cos^{2}\theta},$$

using $\mathrm{d}(\tan\theta)/\mathrm{d}\theta = \sec^{2}\theta$. ✔

Evaluated at $z = 800\ \mathrm{m}$, $\Delta\theta = 1^\circ = 0.0174533\
\mathrm{rad}$ ($z\Delta\theta = 13.963\ \mathrm{m}$):

| $\theta$ | $\cos^{2}\theta$ | footprint (m) | growth vs nadir |
|---|---|---|---|
| $0^\circ$ | 1.0000 | 13.96 | 1.000 |
| $45^\circ$ | 0.5000 | 27.93 | 2.000 |
| $65^\circ$ | 0.1786 | 78.18 | 5.599 |

**Growth at $65^\circ$ is a factor $5.6$** — larger than the factor 4 at
$60^\circ$ in the lesson, because $1/\cos^{2}$ grows without bound. A wider swath
angle buys coverage at the price of resolution, and the price grows faster than the
coverage beyond about $50^\circ$.

---

## ★★5 — Required sound-speed accuracy

Half the budget: $\delta z = 1.5\ \mathrm{m}$ at $z = 1200\ \mathrm{m}$.

$$\epsilon = \frac{\delta z}{z} = \frac{1.5}{1200} = 1.25\times10^{-3}
= 0.125\,\% .$$

In sound-speed units, with $c \approx 1500\ \mathrm{m\,s^{-1}}$:

$$\delta c = 0.125\times10^{-2} \times 1500 = 1.875\ \mathrm{m\,s^{-1}} .$$

So the **path-averaged** sound speed must be known to better than about
$1.9\ \mathrm{m\,s^{-1}}$. Real ocean sound speeds vary by tens of
$\mathrm{m\,s^{-1}}$ over a daily cycle in the surface layer and by
$\sim90\ \mathrm{m\,s^{-1}}$ between the surface and $4\ \mathrm{km}$, so this is a
demanding requirement on the *column average*, and a comfortable one on any single
measurement. It is also why the requirement is stated on the average: local errors
average out along the ray, and the scale error is driven by the average.

---

## ★★6 — Roll displacement against footprint at 1500 m

Outer-beam slant range: $R = z/\cos 60^\circ = 1500/0.5 = 3000\ \mathrm{m}$.
Cross-track displacement is $R\,\delta\theta$; the outer-beam across-track
footprint for $\Delta\theta = 1^\circ$ is

$$\ell_{\text{across}}(60^\circ) = \frac{1500 \times 0.0174533}{\cos^{2}60^\circ}
= \frac{26.180}{0.25} = 104.72\ \mathrm{m}.$$

| roll bias | displacement $R\,\delta\theta$ (m) | as a fraction of the footprint |
|---|---|---|
| $0.02^\circ$ | 1.05 | 1.0 % |
| $0.10^\circ$ | 5.24 | 5.0 % |
| $0.50^\circ$ | 26.18 | 25.0 % |

A $0.1^\circ$ roll bias displaces the outer beam by 5 % of its own footprint
(small), while a $0.5^\circ$ bias displaces it by a quarter of a footprint
(large). The linearity of the relation makes it easy to set a specification: to
keep the displacement below 10 % of the footprint, the roll must be known to
better than $0.2^\circ$ at this depth — **and the same roll error at half the
depth has the same displacement while the footprint halves, so the requirement
tightens with depth.** Attitude accuracy is a deep-water problem as much as a
shallow-water one.

---

## ★★7 — Sounding geometry at 6 kn, 1200 m, 12 Hz, 0.5° spacing

**(a)** $v = 6 \times 0.514444 = 3.0867\ \mathrm{m\,s^{-1}}$;

$$\text{along-track spacing} = \frac{v}{f_p} = \frac{3.0867}{12}
= 0.2572\ \mathrm{m}.$$

**(b)**

$$\text{across-track spacing at nadir} = z\,\Delta\theta
= 1200 \times 0.0087266 = 10.472\ \mathrm{m}.$$

**(c)** Ratio $= 10.472/0.2572 = 40.7$: the data are **41 times denser
along-track than across-track**.

**(d)** Density $= 1/(0.2572 \times 10.472) = 0.371$ soundings per
$\mathrm{m^{2}}$ at nadir.

**What this implies.** Any gridded product from this survey must choose a cell at
least as large as the across-track spacing ($10.5\ \mathrm{m}$) to avoid
interpolating, and in doing so it discards all but $1/41$ of the along-track data.
The redundant soundings are not useless — they are the basis for statistical
averaging and for detecting noise — but they do not improve the horizontal
resolution, and a grid finer than the across-track spacing is a *display* choice,
not a measurement.

---

## ★★★8 — Detecting a sound-speed scale error in a delivered grid

**(i) What the test needs.** An independent measure of depth at one or more
points in the grid. Candidates, in descending order of defensibility:

1. **A collocated, independently calibrated depth**: a bar check at a known
   pressure, a downward-looking acoustic Doppler's bottom track, or a
   single-beam survey whose sound speed was measured in situ.
2. **A tie with another grid** produced by a different system with a measured
   profile. Cross-line ties in the *same* survey do not count: a scale error is
   shared by all lines, so ties are self-consistent and the error is invisible.
3. **A physical constraint**: the gravity field's implied bathymetry (from a
   satellite-derived model) constrains the *shape* but not the scale, and its own
   scale is also uncertain — so this constrains but does not determine.

**(ii) Size of the detectable error.** With a single independent depth known to
$\pm1\ \mathrm{m}$ in $2500\ \mathrm{m}$ of water, the detectable scale error is
about $\pm0.04\,\%$ — an order of magnitude better than the demonstration's
$0.5\,\%$ term. With no independent depth but a well-known flat abyssal plain at
$\pm10\ \mathrm{m}$, the test is limited to $\pm0.4\,\%$.

**(iii) The mathematical form.** Write the true depth as $z_t$ and the delivered
as $z_d = (1+\epsilon)z_t$. A fit of $(z_d - z_{\text{ref}})/z_{\text{ref}}$
against 1 over the reference points estimates $\epsilon$ and its uncertainty
directly. A useful refinement: fit $(z_d - z_{\text{ref}})$ against
$z_{\text{ref}}$ — a slope differing from 0 is the signature of a scale error,
whereas an intercept differing from 0 is a datum or transducer-draft error. The
two are separable with two or more reference points at different depths.

**(iv) The failure mode that gives a false all-clear.** A reference that *shares*
the error. If the bar check was itself computed using the same assumed sound
speed, or if the "independent" grid was calibrated against this one, the test
finds perfect agreement and concludes that the scale is right. This is the
commonest way such tests fail, and the remedy is procedural: the reference must be
traceable to a different physical principle (pressure, or a two-way time with an
independently measured sound speed), and the traceability must be stated.

---

## ★★★9 — Separating a scale error from an attitude error

**Mathematical form of each error.** Let $\theta$ be the beam angle and
$R = c_{\text{a}}t/2$ the computed slant range.

- **Sound-speed scale error $\epsilon$:** depth error
  $\delta z = \epsilon\, z(\theta) = \epsilon\,R(\theta)\cos\theta$. As a function
  of beam angle at fixed depth this is *constant* (every beam is off by the same
  fraction); as a function of cross-track distance $x = z\tan\theta$ it grows
  linearly with $|x|$ but the fractional error is flat in $x$. Its cross-swath
  signature is therefore **flat**.
- **Roll bias $\delta\phi$:** the beam is mis-steered by a constant angle, so the
  sounding is displaced across-track by $R\,\delta\phi$ and its depth is wrong by
  $R\,\delta\phi\sin\theta \approx z\tan\theta\,\delta\phi$. As a function of
  cross-track distance this is **linear in $x$**, with the opposite sign on the
  two halves of the swath if the bias alternates, or the same sign if it is a
  static bias. Its signature is **a ramp across the swath**.
- **Heave $h(t)$:** a *temporal* error, common to all beams in a ping, constant
  across the swath, and varying along-track with the vessel's motion spectrum.

**Covariates to fit.** On a repeat line over a region assumed flat, or on the
cross-over differences between two lines, fit

$$\delta z_i = a + b\,z_i + c\,|x_i| + d\,x_i + e\,x_i^{2} + \cdots$$

over soundings $i$, with $x$ the cross-track distance from nadir. The coefficient
$b$ is the scale error $\epsilon$ (dimensionless); $d$ is the roll bias (units of
slope); $c$ captures beam-angle calibration error; $a$ captures datum and heave
bias.

**Expected degeneracy.** $b\,z_i$ and $c\,|x_i|$ are highly correlated over a swath
whose depth range is small, because $|x|$ and $z$ are related through
$\theta$: on a single flat-depth line, $z$ is nearly constant and $|x|$ varies
fully, so they are separable — but across a *sloping* seafloor, depth and
cross-track distance covary and the two collapse. Similarly, $d\,x_i$ and a
cross-track *tilt* in the seafloor are degenerate: a static roll bias is
indistinguishable from a genuine seafloor that slopes uniformly across the swath.
That is the fundamental degeneracy of line-oriented bathymetry, and it is why
attitude is calibrated independently rather than inverted for.

**What breaks it.** A **reciprocal line** — the same track steamed in the opposite
direction. A true seafloor slope is invariant under reversal; a static roll bias
displaces soundings to the same *geographic* side regardless of heading, so the
apparent cross-track tilt changes sign between the two headings. Differencing the
reciprocal lines therefore isolates attitude from topography with no assumption
about the seafloor at all. A second useful breaker is a **multi-line survey with
opposing headings over the same patch**, which does the same job in two
dimensions and also separates pitch.
