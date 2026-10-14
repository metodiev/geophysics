# Solutions — 17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> The instrument is a **SYNTHETIC** teaching geometry.

Lesson: [04 Spatial, Spectral, Temporal and Radiometric Resolution](../04-resolution-concepts.md).

---

## ★1 — GSD and its off-nadir growth

$$\mathrm{GSD} = H\,\theta_{\rm IFOV} = 6.00\times10^{5}\times15\times10^{-6}
= 9.00\ \mathrm{m}.$$

At $45°$ off-nadir, flat-Earth:

$$\mathrm{GSD}(45°) = \frac{\mathrm{GSD}}{\cos^{2}45°}
= \frac{9.00}{0.500} = 18.0\ \mathrm{m}.$$

A factor of two at a moderate look angle. Since a real image is *resampled* to a
uniform grid, the corners of a wide-field image are interpolated from wider
footprints, which is a genuine loss of information, not a cosmetic one.

---

## ★2 — Nyquist frequency and the smallest representable scale

$$f_N = \frac{1}{2w} = \frac{1}{2\times5} = 0.100\ \mathrm{cycles\,m^{-1}}.$$

The smallest representable spatial period is $1/f_N = 2w = 10.0\ \mathrm{m}$. This
is the *sampling* limit. If the optical cut-off lies below $1/(2w)$, the optics
protects the design from aliasing; if it lies above, high-frequency scene content
folds into the image as a false pattern.

---

## ★3 — Airy spot versus GSD

$$d_A = 1.22\frac{\lambda H}{D}
= 1.22\times\frac{0.66\times10^{-6}\times7.00\times10^{5}}{0.30}
= 1.879\ \mathrm{m}.$$

$$\frac{\mathrm{GSD}}{d_A} = \frac{7.00}{1.879} = 3.73.$$

The GSD is $3.7\times$ coarser than the diffraction spot, so in this band the
detector, not the aperture, sets the sampling — but see ★4 for the sampling
consequence.

---

## ★4 — Pitch that matches the cut-off to Nyquist

$$f_c = f_N \;\Longrightarrow\; \frac{D}{\lambda H} = \frac{1}{2w}
\;\Longrightarrow\; w = \frac{\lambda H}{2D}.$$

$$w = \frac{0.66\times10^{-6}\times7.00\times10^{5}}{2\times0.30}
= 0.770\ \mathrm{m}.$$

**Comment.** A $0.77\ \mathrm{m}$ ground pitch at $700\ \mathrm{km}$ requires an
angular pitch of $0.77/7.0\times10^{5} = 1.10\ \mathrm{\mu rad}$, i.e. detector
elements roughly $9\times$ smaller than the synthetic design's. That may be
technologically possible, but the design then becomes *aperture-limited*: the
Airy spot is $1.879\ \mathrm{m}$ against a $0.77\ \mathrm{m}$ pitch, so the optics
cannot deliver contrast at the Nyquist frequency at all. The honest conclusion is
that the two constraints — Nyquist compliance and aperture-limited resolution —
must be satisfied *together*, and doing so requires a larger aperture, a lower
orbit, or a coarser GSD accepted as the design point.

---

## ★5 — NEΔT at two scene temperatures

$$L = B_\lambda(T),\qquad
\frac{\mathrm{d}L}{\mathrm{d}T} = L\,\frac{hc}{\lambda k_BT^{2}},\qquad
\mathrm{NE}\Delta T = \frac{\mathrm{NE}\Delta L}{\mathrm{d}L/\mathrm{d}T}.$$

| $T$ (K) | $L$ (W m⁻² sr⁻¹ m⁻¹) | $\mathrm{d}L/\mathrm{d}T$ | $\mathrm{NE}\Delta T$ (K) |
|---|---|---|---|
| 300 | $9.6694\times10^{6}$ | $1.4313\times10^{5}$ | $0.1397$ |
| 320 | $1.2811\times10^{7}$ | $1.6667\times10^{5}$ | $0.1200$ |
| 340 | $1.6438\times10^{7}$ | $1.8944\times10^{5}$ | $0.1056$ |

**Direction.** $\mathrm{d}L/\mathrm{d}T$ grows faster than $L$ does (it carries an
extra factor $1/T^{2}$ relative to $L/T$ through the Wien form), so the same
instrument resolves a *smaller* temperature difference over a hotter scene. NEΔT
is a property of the instrument **and** the scene, which is why it must be quoted
with the scene state.

---

## ★6 — Swath and revisit

$$T_r = \frac{2\pi R_E}{N W}
= \frac{2\pi\times6371\ \mathrm{km}}{14.3\times250\ \mathrm{km}}
= \frac{40030}{3575} = 11.20\ \mathrm{days}.$$

Two satellites: $11.20/2 = 5.60$ days.

For a $2$-day revisit with one satellite:

$$W = \frac{2\pi R_E}{N T_r}
= \frac{40030}{14.3\times2} = 1400\ \mathrm{km}.$$

A $1400\ \mathrm{km}$ swath is a wide-swath design, and the corresponding GSD at
$700\ \mathrm{km}$ with this aperture would be far coarser than $7\ \mathrm{m}$.
**Revisit and detail come from the same optical budget.**

---

## ★7 — Contrast at Nyquist

At a design's own Nyquist frequency $f_N = 1/(2w)$, the detector factor is

$$\mathrm{MTF}_{\rm det} = \operatorname{sinc}(f_N w)
= \operatorname{sinc}\!\left(\tfrac{1}{2}\right)
= \frac{\sin(\pi/2)}{\pi/2} = \frac{2}{\pi} = 0.6366,$$

independent of $w$. With the cut-off-limited optics
$\mathrm{MTF}_{\rm opt} = 1 - f/f_c$,

$$\mathrm{MTF}_{\rm net} = \frac{2}{\pi}\left(1 - \frac{1}{2wf_c}\right).$$

For $w = 8.40\ \mathrm{m}$, $f_c = 0.64935$: $2wf_c = 10.909$,
$1 - 1/10.909 = 0.9083$, and

$$\mathrm{MTF}_{\rm net} = 0.6366\times0.9083 = 0.5783.$$

That is the fraction of the ideal contrast surviving at the finest scale the
detector can represent. A value near 0.58 means adjacent-pixel contrast is
reduced to roughly six tenths — usable, but the reason a *smaller* GSD does not
linearly improve interpretability.

---

## ★8 — The single-band null space

**Parametrisation.** With background radiance $L_{\rm bg}$ and measured pixel
radiance $L_{\rm pix}$, the two-component mixture gives

$$L_{\rm pix} = fL_{\rm hot} + (1-f)L_{\rm bg}
\;\Longrightarrow\;
L_{\rm hot} = \frac{L_{\rm pix} - (1-f)L_{\rm bg}}{f},
\qquad T_{\rm hot} = B_\lambda^{-1}(L_{\rm hot}).$$

Given $L_{\rm bg} = 9.6694\times10^{6}$ and
$L_{\rm pix} = 1.0213\times10^{7}$ at $10.8\ \mathrm{\mu m}$:

| $f$ | implied $L_{\rm hot}$ (W m⁻² sr⁻¹ m⁻¹) | implied $T_{\rm hot}$ (K) |
|---|---|---|
| 0.01 | $6.4009\times10^{7}$ | 509.49 |
| 0.10 | $1.5103\times10^{7}$ | 332.94 |
| 0.50 | $1.0756\times10^{7}$ | 307.28 |

The pattern is the point: as the assumed cover $f$ rises, the target temperature
implied by the *same* measurement falls smoothly from $509\ \mathrm{K}$ to
$307\ \mathrm{K}$. **For every $f$ there is a target temperature that reproduces
the measurement**: the inverse problem has a one-parameter family of solutions,
and no single band selects among them.

**What a second band adds.** At wavelength $\lambda_2$ the mixture gives

$$L_{\rm pix}(\lambda_2) = fB_{\lambda_2}(T_{\rm hot})
+ (1-f)B_{\lambda_2}(T_{\rm bg}).$$

Together with the first band that is **two equations in the two unknowns
$(f, T_{\rm hot})$**, provided (i) the two wavelengths have appreciably different
Planck curvature, so the two equations are not nearly parallel, and (ii) the
background radiance is known at both wavelengths to better than the signal sought.
The condition number of the $2\times2$ Jacobian

$$J = \begin{pmatrix}
B_{\lambda_1}(T_{\rm hot}) - B_{\lambda_1}(T_{\rm bg}) &
f\,\partial_T B_{\lambda_1}(T_{\rm hot})\\
B_{\lambda_2}(T_{\rm hot}) - B_{\lambda_2}(T_{\rm bg}) &
f\,\partial_T B_{\lambda_2}(T_{\rm hot})
\end{pmatrix}$$

is the quantitative measure of "appreciably different": in the far-infrared the
two bands differ mainly by a multiplicative factor and the system is nearly
singular; across the $3$–$5$ and $8$–$12\ \mathrm{\mu m}$ ranges the curvature
differs enough to separate the terms. This is the physical basis of two-band
fire and hot-spot retrieval.

---

## ★9 — Specifying a synthetic instrument for three requirements

**Requirements.** (i) GSD $\le 20\ \mathrm{m}$ in the visible;
(ii) $\mathrm{NE}\Delta T \le 0.2\ \mathrm{K}$ at $300\ \mathrm{K}$, $10.8\
\mathrm{\mu m}$; (iii) equatorial revisit $\le 5$ days.

**Step 1 — geometry (requirement i).** With an angular IFOV of
$20\ \mathrm{\mu rad}$ the GSD is $H\times20\ \mathrm{\mu rad}$; for
$H = 800\ \mathrm{km}$ that is $16.0\ \mathrm{m}$, satisfying (i) with margin.
Choose $H = 800\ \mathrm{km}$ (a lower orbit than the default).

**Step 2 — sampling and aperture.** To be Nyquist-compliant at
$\lambda = 0.66\ \mathrm{\mu m}$ the pitch must satisfy
$w \le \lambda H/(2D)$, i.e. $D \le \lambda H/(2w) = 0.66\times10^{-6}\times
8.0\times10^{5}/(2\times16) = 0.0165\ \mathrm{m}$ — impossible for a real
telescope. So a $16\ \mathrm{m}$ GSD at $800\ \mathrm{km}$ **cannot** be
Nyquist-compliant in the visible with any practical aperture; the design must
accept a cut-off well above Nyquist and rely on the optical MTF to suppress
aliasing. State that explicitly rather than pretending otherwise. A larger
aperture makes the optics *sharper*, which makes aliasing *worse*, not better, at a
fixed pitch — the criterion is $D \le \lambda H/(2w)$, so a larger $D$ at fixed
$w$ and $H$ violates it.

**Step 3 — spectral (requirement ii).** $\mathrm{NE}\Delta T = \mathrm{NE}\Delta L/
(\mathrm{d}L/\mathrm{d}T)$ with $\mathrm{d}L/\mathrm{d}T = 1.4313\times10^{5}$ at
$300\ \mathrm{K}$; for $\mathrm{NE}\Delta T = 0.2\ \mathrm{K}$ we need
$\mathrm{NE}\Delta L \le 0.2\times1.4313\times10^{5} = 2.86\times10^{4}$
$\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$. A detector with
$\mathrm{NE}\Delta L = 2.0\times10^{4}$ satisfies it, with a margin of $1.43\times$.
Widen the thermal band if the detector is noisier, remembering the trade below.

**Step 4 — revisit (requirement iii).** For $T_r \le 5$ days at
$N = 14.3$ orbits/day:

$$W \ge \frac{2\pi R_E}{N T_r} = \frac{40030}{14.3\times5}
= 560\ \mathrm{km}.$$

**Which requirement forces the others.** Requirement (i) and (iii) *conflict*:
satisfying (i) needs a narrow swath or a low orbit, and (iii) needs a wide swath.
With $H = 800\ \mathrm{km}$ and $W = 560\ \mathrm{km}$, the cross-track field of
view is $560/800 = 0.70\ \mathrm{rad} = 40°$ — a wide field, which forces a
large focal plane and a fast optical design, and the resulting off-nadir
$\sec^{2}\phi$ growth at the swath edge makes the edge pixels
$1/\cos^{2}(20°) = 1.13\times$ wider than nadir, i.e. $18.1\ \mathrm{m}$ against
$16.0\ \mathrm{m}$. That is acceptable for this specification, but it must be
reported: **a single GSD cannot describe this instrument.** Requirement (ii) is
the easiest to satisfy here, and if the detector were noisier it would be the
binding constraint through the $\mathrm{GSD}^{2}\times\Delta\lambda$ trade: a
$16\ \mathrm{m}$ GSD at $800\ \mathrm{km}$ collects $(16/7)^{2} = 5.2\times$ less
signal per pixel than the default design's $7\ \mathrm{m}$ GSD at $700\ \mathrm{km}$
(in ground-area terms, and less still after accounting for the shorter
integration time a wide swath entails), so the thermal band width must be widened
by a comparable factor or several pixels must be averaged — which coarsens the
thermal product back toward its Airy limit.
