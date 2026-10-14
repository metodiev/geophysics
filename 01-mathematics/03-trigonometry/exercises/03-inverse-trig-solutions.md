# Solutions — 01-03-03 Inverse Trigonometric Functions and Branch Ambiguity

> **Read this after attempting the exercises, not before.**
>
> Numeric values were computed; angles are in radians unless stated. Where a
> branch choice is involved, the reasoning that fixes it is given, because the
> branches are the whole subject of this lesson.

---

## ★1 — All solutions in $[0, 2\pi)$

**(a)** $\sin x = 0.3$. The principal value is
$x_0 = \arcsin 0.3 = 0.3046926540$. The second solution in one period is
$\pi - x_0 = 2.8368999996$. Both lie in $[0, 2\pi)$, so

$$\boxed{x = 0.3046926540 \ \text{or}\ x = 2.8369000000 .}$$

For all real $x$: $x = 0.3046926540 + 2\pi k$ or
$x = 2.8369000000 + 2\pi k$, $k \in \mathbb{Z}$.

**(b)** $\cos x = -0.5$. The principal value is
$\arccos(-0.5) = 2.0943951024$ (i.e. $120°$). The cosine is even, so the second
solution is $-2.0943951024$, which is negative; add $2\pi$ to bring it into range:

$$\boxed{x = 2.0943951024 \quad\text{and}\quad x = 4.1887902048 .}$$

Note the structural difference from (a): for the sine, the second solution is a
*reflection about* $\pi/2$ (a supplement); for the cosine it is a *reflection about
zero* (a sign change). Getting this wrong swaps the answer between the two
solutions, which is a $60°$ error here.

**(c)** $\tan x = 1.5$. The principal value is $\arctan 1.5 = 0.9827937232$, and
the tangent has period $\pi$, so

$$\boxed{x = 0.9827937232 \quad\text{and}\quad x = 4.1243863768 .}$$

**A consistency check worth doing every time.** Evaluate the sine, cosine or
tangent of each answer in the original equation. In (a),
$\sin 0.3046926540 = 0.3000000000$ and $\sin 2.8369000000 = 0.3000000000$; in (b),
both cosines are $-0.5000000000$; in (c), both tangents are $1.5000000000$. Three
checks that cost nothing and would have caught any of the standard errors in the
reflection rules.

---

## ★2 — `atan2` and `atan` compared

| $y$ | $x$ | `atan(y/x)` (deg) | `atan2(y, x)` (deg) |
|---|---|---|---|
| 1 | 1 | 45.0000 | 45.0000 |
| 1 | $-1$ | $-45.0000$ | 135.0000 |
| $-1$ | $-1$ | 45.0000 | $-135.0000$ |
| $-1$ | 1 | $-45.0000$ | $-45.0000$ |
| 0 | 1 | 0.0000 | 0.0000 |
| 1 | 0 | undefined | 90.0000 |
| 0 | $-1$ | 0.0000 | 180.0000 |

`atan` **discards the signs of the two components individually, retaining only
their ratio**, so it cannot distinguish two directions $180°$ apart and cannot
represent either component being zero with the other non-zero.

Note the row $(0, -1)$: the ratio is $-0$ and `atan` returns 0, i.e. *due east*,
when the true direction is **due west**. A direction error of $180°$ arising from
a division by negative zero is exactly the kind of failure that survives code
review, because the expression `y/x` looks harmless.

---

## ★3 — The derivative of arcsine

$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^{2}}}, \qquad |x| < 1 .$$

| $x$ | $d(\arcsin x)/dx$ |
|---|---|
| 0 | 1.0000000 |
| 0.5 | 1.1547005 |
| 0.9 | 2.2941573 |
| 0.99 | 7.0888121 |

Setting $1/\sqrt{1-x^{2}} = 10$ gives $\sqrt{1-x^{2}} = 0.1$, so
$1 - x^{2} = 0.01$ and

$$|x| = \sqrt{0.99} = \boxed{0.9949874371} \quad (84.26°\ \text{in angle terms}).$$

**Interpretation.** Inside $|x| < 0.995$ the inversion amplifies a relative input
error by less than 10; beyond that it degrades rapidly, and at $x = 0.9999$ the
amplification is 70.7. There is no threshold at which the function "breaks" — it
degrades continuously, which is why it must be assessed with arithmetic rather
than by inspection.

---

## ★★4 — Azimuth from components

**(a)** With azimuth measured clockwise from north and
`azimuth = atan2(east, north) mod 360`:

| Target (E, N) km | `atan2(E, N)` |
|---|---|
| $(10, 10)$ | $45.0000°$ |
| $(10, -10)$ | $135.0000°$ |
| $(-10, -10)$ | $225.0000°$ |
| $(-10, 10)$ | $315.0000°$ |

**(b)** `atan(E/N)` returns $45.0000$, $-45.0000$, $45.0000$ and $-45.0000$
respectively. Only the north-east target is correct. **The failure pattern is
structured, not random**: the naive values all lie in $[-90°, 90°]$, so the whole
southern half-plane is folded onto the northern one, and the south-west target is
mapped onto the north-east azimuth. A contour map or an interpolation built on
those numbers folds the survey across the east–west axis, and the result looks
like a geological structure rather than a bug. This is why the failure survives so
long in practice.

**(c)** $(0, -15)$: the ratio $E/N = 0$ and `atan(0)` returns 0, i.e. **due
north**, when the target is due *south*. `atan2(0, -15)` returns $180.0000°$ ✓.
Here the naive form is not just imprecise; there is no arithmetic that can recover
the answer from the ratio alone, because the ratio does not contain the sign
information.

---

## ★★5 — Inverting the take-off relation

**(a)** Invert $\Delta = \pi - 2i$:

$$i = \frac{\pi - \Delta}{2}.$$

| $\Delta$ | $i$ |
|---|---|
| $60°$ | $60.0000°$ |
| $90°$ | $45.0000°$ |
| $120°$ | $30.0000°$ |

This inversion is trivial and cannot be the source of a branch problem — but note
that it is only valid for a *single* chord, which is what the uniform-sphere model
gives.

**(b)** $p = R\sin i / v$ with $R = 6371$ km, $v = 6$ km/s:

| $i$ | $p$ (s/rad) |
|---|---|
| $60°$ | $919.574641$ |
| $45°$ | $750.829550$ |
| $30°$ | $530.916667$ |

**Sanity check on the units.** $p$ has units of time per radian because
$\Delta$ is dimensionless. In the seismological literature $p$ is usually quoted
per degree, which is $57.2958$ times smaller: for example
$919.574641/57.2958 = 16.0496$ s/deg. Always check which convention a table uses
before comparing numbers.

**(c)** The relation requires $0 \le i \le 90°$, hence $0 \le \Delta \le 180°$. For
$\Delta = 200°$ the inversion returns $i = -10°$, a **negative take-off angle**,
which is physically meaningless: a ray cannot leave the source upwards into the
Earth's interior. The model has failed, not the algebra. Beyond $\Delta = 180°$ a
real ray has passed the antipode and the geometry must be reformulated — the
shortest path from source to receiver is $360° - 200° = 160°$ the *other way
round*, and the ray that reaches a receiver at $200°$ from the source is a
different ray. **Spotting an out-of-range inverse as a model failure rather than a
numerical one is a habit worth acquiring**: an inverse trigonometric function
returning a value outside its physical range is always telling you something about
the model, not about the arithmetic.

---

## ★★6 — Phase unwrapping

**(a)** Walking the series and adding the wrapped step:

| $k$ | wrapped sample | wrapped step | unwrapped |
|---|---|---|---|
| 0 | 0.00 | — | 0.0000000 |
| 1 | 1.20 | 1.20 | 1.2000000 |
| 2 | 2.40 | 1.20 | 2.4000000 |
| 3 | 3.00 | 0.60 | 3.0000000 |
| 4 | $-2.80$ | $-5.80 \to +0.4831853$ | 3.4831853 |
| 5 | $-1.60$ | $-5.0831853 \to +1.2000000$ | 4.6831853 |
| 6 | $-0.40$ | $-5.0831853 \to +1.2000000$ | 5.8831853 |
| 7 | $0.80$ | $-5.0831853 \to +1.2000000$ | 7.0831853 |

After the initial transient the unwrapped phase advances by exactly
$1.2000000$ rad per sample, which is the ramp the data were generated from. Note
that the *wrapped* series jumps in the middle — from $3.00$ to $-2.80$, a jump of
$-5.80$ — and that is precisely the signature of a wrap, not of a physical
discontinuity. The algorithm assumes the latter and corrects for the former.

**(b)** The assumption: **the true phase changes by less than $\pi$ between
consecutive samples.** The wrapped step is therefore the true step, once reduced
into $(-\pi, \pi]$.

**(c)** A failing series: samples $0.00$, $3.50$, $0.7168147$ (the last being
$7.0 - 2\pi$). The true phase is the ramp $0, 3.5, 7.0$ — a step of $3.5$ rad per
sample. Unwrapping gives

$$u_0 = 0, \quad u_1 = 0 + \operatorname{wrap}(3.5) = -2.7831853, \quad
u_2 = -2.7831853 + \operatorname{wrap}(3.5) = -5.5663706,$$

i.e. a *descending* ramp, the mirror image of the truth. The failure occurs at the
very first step.

**Why the algorithm cannot detect it.** The wrapped step is $-2.7831853$ and the
true step is $+3.5$; these differ by exactly $2\pi$, and the data contain no
information that distinguishes them — both are consistent with the same two
measured samples. The algorithm's rule (choose the step of magnitude below $\pi$)
is the only choice available without extra information, and it happens to be
wrong whenever the true step exceeds $\pi$. Extra information that would fix it:
a coarser but unambiguous measurement (e.g. a lower-frequency band where the phase
is known to move slowly), a physical model bounding the phase rate, or continuity
across a spatial rather than temporal neighbourhood. **This is the same branch
problem as `arcsin`, in a different costume: the measurement has lost information,
and no algorithm can restore it.**

---

## ★★7 — Velocity from a near-critical observation

**(a)** At the critical angle, $\sin i_c = v_1/v_2$, so

$$v_2 = \frac{v_1}{\sin i_c} = \frac{6.0}{\sin 28.0°} = \frac{6.0}{0.46947156}
= \boxed{12.780327\ \text{km/s}} .$$

**(b)** Differentiate

$$\frac{dv_2}{di_c} = -\frac{v_1\cos i_c}{\sin^{2}i_c}
= -\frac{6.0 \times 0.88294759}{0.22040419} = -24.0363\ \text{km/s per radian}.$$

With $\sigma_{i_c} = 0.3° = 5.23599\times10^{-3}$ rad:

$$\sigma_{v_2} = 24.0363 \times 5.23599\times10^{-3} = \boxed{0.1259\ \text{km/s}},$$

a fractional uncertainty of $0.1259/12.7803 = \boxed{0.98\ \text{percent}}$.

**(c)** For $i_c = 60.0°$:

$$v_2 = \frac{6.0}{\sin 60°} = 6.928203\ \text{km/s}, \qquad
\frac{dv_2}{di_c} = -\frac{6.0 \times 0.5}{0.75} = -4.0\ \text{km/s per radian},$$

$$\sigma_{v_2} = 4.0 \times 5.23599\times10^{-3} = 0.02094\ \text{km/s},
\qquad \text{fraction} = 0.30\ \text{percent}.$$

**Comparison.** The same $\pm0.3°$ angular uncertainty produces a fractional
velocity uncertainty of 0.98 percent at $28°$ but only 0.30 percent at $60°$ — a
factor of 3.2 worse in the near-critical case. The reason is the derivative above:
$dv_2/di_c = -v_1\cos i_c/\sin^{2}i_c$ grows faster than $v_2$ itself as
$i_c \to 0$, so the *fractional* sensitivity
$|dv_2/di_c|/v_2 = \cot i_c$ diverges as $i_c \to 0$. (Check the algebra:
$\cot 28° = 1.8807$; $1.8807 \times 0.005236 = 0.00985$, i.e. 0.985 percent ✓,
and $\cot 60° = 0.5774$ giving 0.302 percent ✓. This closed form is a much faster
route and is worth remembering.)

**Geophysical reading.** A *near-critical* observation is not the same as a
*small-critical-angle* one. A critical angle of $28°$ means a very large velocity
contrast — a factor of 2.13 — and the inversion of such a contrast from an angular
measurement is intrinsically more sensitive than the inversion of a mild one. In a
real survey the picks near the critical distance are also the hardest to make,
because the refracted branch merges into the direct arrival there, so the
conditioning and the pick quality degrade together. Weight those picks
accordingly.

---

## ★★8 — Forward and reverse azimuths

**(a)** With `azimuth = atan2(sinΔλ cosφ₂, cosφ₁ sinφ₂ − sinφ₁ cosφ₂ cosΔλ)`:

- from the receiver $(37.00°\text{N}, 23.50°\text{E})$ to the station
  $(38.00°\text{N}, 25.00°\text{E})$: $\boxed{49.505°}$;
- from the station to the receiver: $\boxed{230.418°}$;
- the epicentral distance is $1.554362°$ (from the module's demonstration).

**(b)** The two azimuths differ by

$$230.418° - 49.505° = 180.913°,$$

so the deviation from $180°$ is $\boxed{0.913°}$ — nearly a degree, which on a
100 km baseline is an offset of order 1.6 km. It is far larger than any angular
measurement error, so it cannot be ignored.

**(c)** For two points on the same meridian, say $(37.00°\text{N}, 25.00°\text{E})$
and $(38.00°\text{N}, 25.00°\text{E})$, the azimuths are $0.000°$ and $180.000°$,
differing by exactly $180°$.

**The one-sentence reason.** A great circle crosses successive meridians at a
changing angle unless it *is* a meridian, so the heading you set out on and the
heading you arrive with are equal only when the path runs north–south.

**Practical consequence.** Software that derives a back-azimuth by adding $180°$
to a forward azimuth is correct for regional arrays arranged north–south and
silently wrong by an amount that grows with the longitude span of everything else.
The error is systematic and correlates with geometry, which is the worst kind:
it mimics a real signal in a focal-mechanism misfit map.

---

## ★★★9 — Take-off angle, travel time and the ray parameter

**(a)** The table for $R = 6371$ km, $v = 6$ km/s, chord
$L = 2R\cos i$, $T = L/v$, $p = R\sin i/v$:

| $i$ (deg) | $\Delta$ (deg) | $L$ (km) | $T$ (s) | $p$ (s/rad) |
|---|---|---|---|---|
| 0 | 180.000000 | 12742.0000 | 2123.6667 | 0.000000 |
| 10 | 160.000000 | 12548.4204 | 2091.4034 | 184.385423 |
| 20 | 140.000000 | 11973.5634 | 1995.5939 | 363.168389 |
| 30 | 120.000000 | 11034.8957 | 1839.1493 | 530.916667 |
| 40 | 100.000000 | 9760.9383 | 1626.8230 | 682.533310 |
| 50 | 80.000000 | 8190.3997 | 1365.0666 | 813.411525 |
| 60 | 60.000000 | 6371.0000 | 1061.8333 | 919.574641 |
| 70 | 40.000000 | 4358.0207 | 726.3368 | 997.796948 |
| 80 | 20.000000 | 2212.6251 | 368.7708 | 1045.701699 |
| 90 | 0.000000 | 0.0000 | 0.0000 | 1061.833333 |

Note $T$ and $p$ are listed per radian; divide by $57.2958$ for the per-degree
convention.

**(b)–(c)** Finite-difference estimates of $dT/d\Delta$ against the exact $p$:

| midpoint $i$ | step | $dT/d\Delta$ (s/rad) | $p$ exact (s/rad) | difference |
|---|---|---|---|---|
| $5°$ | $10°$ | 92.427456 | 92.544873 | $1.174\times10^{-1}$ |
| $45°$ | $10°$ | 749.876931 | 750.829550 | $9.526\times10^{-1}$ |
| $0.25°$ | $0.5°$ | 4.633093 | 4.633107 | $1.470\times10^{-5}$ |
| $4.75°$ | $0.5°$ | 87.928236 | 87.928515 | $2.790\times10^{-4}$ |

Reducing the step by a factor of 20 reduces the discrepancy by about a factor of
400 — i.e. the error scales as $h^{2}$, which is the expected behaviour of a
centred difference and is the empirical confirmation that the remaining
discrepancy is truncation, not a failure of the identity.

**(d)** With $T = 2R\cos i/v$ and $\Delta = \pi - 2i$, the chain rule gives

$$\frac{dT}{d\Delta} = \frac{dT/di}{d\Delta/di}
= \frac{-2R\sin i/v}{-2} = \frac{R\sin i}{v} = p .$$

The identity is *exact*, and it is why the two quantities are numerically
interchangeable in this model.

**(e)** The model assumes a **spherically symmetric Earth with a single constant
velocity**. Remove either assumption and the closed forms fail:

- varying velocity with depth turns the chord into a curved ray, and
  $\Delta = \pi - 2i$ becomes an integral over the ray parameter (the standard
  $\Delta(p) = 2p\int \frac{dr}{r\sqrt{(r/v)^{2} - p^{2}}}$ formula);
- asphericity (an ellipsoid, or lateral heterogeneity) makes the relation depend
  on azimuth as well as distance.

What survives in both cases is the structure: $p$ is dimensionless-free of the
take-off angle and is still equal to $dT/d\Delta$ for a given ray, which is why
seismology parameterises travel-time curves by $p$ rather than by $i$.

---

## ★★★10 — Conditioning of the inverse sine

**(a)–(b)** With

$$\kappa(c) = \left|\frac{c}{\arcsin c\,\sqrt{1-c^{2}}}\right|,$$

| $c$ | $\kappa(c)$ |
|---|---|
| 0.1 | 1.003358 |
| 0.5 | 1.102658 |
| 0.9 | 1.843899 |
| 0.99 | 4.910191 |
| 0.999 | 14.641457 |
| 0.9999 | 45.421379 |

Solving $\kappa(c) = 10$ and $= 100$ numerically:

- $\kappa > 10$ for $c > 0.997798119965$, i.e. $i > 86.197°$ — within $3.8°$ of
  grazing;
- $\kappa > 100$ for $c > 0.999979570453$, i.e. $i > 89.634°$ — within $0.37°$ of
  grazing.

**(c)** A central difference with $\delta c = 10^{-6} c$ reproduces the predicted
amplification at all five values in the table, with a worst absolute discrepancy
of $1.8\times10^{-6}$ in $\kappa$. That residual is the truncation error of the
difference quotient, consistent with the third-derivative term of the Taylor
expansion.

**(d)** Since $\sin i = c$, the dangerous regime is **$i$ within a few degrees of
grazing**, i.e. take-off angles close to $90°$ from the vertical. In a refraction
survey those are the rays that travel almost horizontally and graze the refractor;
their travel times carry the most information about $v_2$, and their inversion is
the worst conditioned. What to do in practice:

- report the uncertainty, and do not quote a near-critical velocity to more
  significant figures than the angular measurement supports;
- weight the near-critical picks down in an over-determined inversion, where the
  sensitivity matrix will assign them small leverage anyway if it is built
  correctly;
- combine the angular information with an independent constraint — a well-log
  velocity, a wide-angle reflection moveout, or a gravity model — rather than
  relying on a single weak measurement.

**(e)** As $c \to 0^{+}$,

$$\kappa(c) \to \frac{c}{c \cdot 1} = 1,$$

the minimum possible value for any relative condition number: the inversion then
amplifies nothing at all. The function is *perfectly* conditioned at normal
incidence. But a refraction survey cannot use it, because at $i \to 0$ the ray is
nearly vertical and never grazes the deeper interface — it carries almost no
information about $v_2$. The information content is *maximal* exactly where the
conditioning is *worst*. That tension between sensitivity and stability is not a
curiosity of this example; it is the geometric content of ill-posedness, developed
in [18-inverse-problems](../../../18-inverse-problems/README.md) and in the
framework of
[16-functional-analysis](../../16-functional-analysis/README.md).
