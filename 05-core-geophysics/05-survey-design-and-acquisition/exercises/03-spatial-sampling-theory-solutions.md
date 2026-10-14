# Solutions — 05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction

> **Read this after attempting the exercises, not before.** All values computed here
> with the folding formula; the lesson's measured values are quoted from its script.

---

## ★1 — Nyquist wavenumbers

$k_N = \pi/\Delta x$, $\lambda_N = 2\Delta x$:

| $\Delta x$ (m) | $k_N$ (rad/m) | $\lambda_N$ (m) |
|---|---|---|
| 25 | 0.125664 | 50 |
| 50 | 0.062832 | 100 |
| 200 | 0.015708 | 400 |

---

## ★2 — Apparent wavelength of a 250 m anomaly

$k_0 = 2\pi/250 = 0.025133$ rad/m.

**(a)** $\Delta x = 100$ m: $k_N = 0.031416$. $k_0/k_N = 0.80 < 1$ → **not aliased**;
apparent wavelength 250 m.

**(b)** $\Delta x = 200$ m: $k_N = 0.015708$. $k_0/k_N = 1.60 > 1$ → **aliased**.
Fold:
$k_{\text{app}} = ((0.025133+0.015708)\bmod 0.031416) - 0.015708
= 0.009425 - 0.015708 = -0.006283$ rad/m, so
$\lambda_{\text{app}} = 2\pi/0.006283 = \boxed{1000\ \mathrm{m}}$. The survey
reports a 1 km feature from a 250 m source — a factor 4 error.

**(c)** $\Delta x = 50$ m: $k_N = 0.062832$, ratio 0.40 → **not aliased**.

---

## ★3 — The sampling condition

Band-limited form: the field can be reconstructed exactly if its spectrum vanishes
for $|k| > k_N = \pi/\Delta x$, equivalently $\lambda_{\min} \ge 2\Delta x$.

The condition is about the spectrum because a field can contain a *small* component
at a short wavelength even when its dominant feature is long; that component folds,
and — as the lesson measures — the fold is an exact substitution, not a small
perturbation.

---

## ★4 — A 30 m feature sampled at 40 m

**(a)** $\lambda_N = 2\Delta x = \boxed{80\ \mathrm{m}}$.

**(b)** $k_0 = 2\pi/30 = 0.209440$; $k_N = \pi/40 = 0.078540$.
Fold: $k_0 + k_N = 0.287980$; $\bmod 0.157080 = 0.130900$;
$-0.078540 \Rightarrow k_{\text{app}} = 0.052360$ rad/m, so
$\lambda_{\text{app}} = \boxed{120\ \mathrm{m}}$. The 30 m feature is reported as a
120 m feature.

---

## ★5 — Why a longer profile does not help

The Nyquist wavenumber is set by the *sample spacing* ($k_N = \pi/\Delta x$) and not
by the record length; a longer record sharpens the spectrum but does not widen the
band.

---

## ★★6 — A 250 m gravity survey for a 400 m half-width target

**(a)** $k_N = \pi/250 = \boxed{0.012566\ \mathrm{rad/m}}$;
$\lambda_N = \boxed{500\ \mathrm{m}}$.

**(b)** A 200 m anomaly wavelength has $k = 0.031416 > k_N$, so it is **not
representable** — it would fold to
$((0.031416+0.012566)\bmod 0.025133)-0.012566 = 0.018849-0.012566 = 0.006283$,
i.e. a reported wavelength of 1000 m.

**(c)** With half-width 400 m, the body's centre depth is of order 400 m, so
$2/h = 0.005$ rad/m, three times smaller than $k_N$. **Geological aliasing is not
the concern**; the concern is cultural noise, which is generated at the surface and
contains high wavenumbers that will fold freely (the lesson's Section 8).

---

## ★★7 — Ground roll and reflections on the same line

**(a)** $f_{\max} = v_a/(2\Delta x) = 400/(2 \times 25) = \boxed{8\ \mathrm{Hz}}$.

**(b)** $f_{\max} = 3000/50 = \boxed{60\ \mathrm{Hz}}$.

**(c)** The aliasing limit depends on *apparent* velocity, and ground roll is slow
while reflections are fast — a factor 7.5 between them here. The standard remedy for
the slow arrival is a *receiver array*, i.e. a spatial anti-alias filter applied
before sampling, rather than a spacing small enough for ground roll (which would cost
7.5× the channels for no benefit to the reflections).

---

## ★★8 — Which spacing produced which width?

A reported width that is *double* the true one is the signature of a fold with
$k_0/k_N$ between 1 and 2. For a true wavelength $\lambda_0$, the reported
$\lambda_{\text{app}} = \lambda_0/(|\lambda_0/(2\Delta x) \cdot 2 - 1|)$… rather than
invert the algebra, use the concrete case: the lesson's 100 m field sampled at 60 m
reports 150 m (a factor 1.5); a 400 m true width reported as 800 m requires
$\Delta x$ such that $2\Delta x$ lies just below 400 m, i.e. $\Delta x$ slightly
under 200 m — for instance $\Delta x = 300$ m gives $\lambda_N = 600$ m,
$k_0 = 0.015708$, $k_N = 0.010472$, fold →
$((0.015708+0.010472)\bmod 0.020944)-0.010472 = 0.005236-0.010472 = -0.005236$ →
$\lambda_{\text{app}} = 1200$ m.

The reliable reasoning is therefore: **the survey that reports the shorter feature is
the better sampled one, and the coarser survey's longer wavelength is the alias.** The
800 m interpretation is the likely error, and it should be checked against the flight
line spacing, which must be below 200 m to represent a 400 m feature at all.

---

## ★★9 — Anisotropic sampling of a 45° structure

**(a)** Along the structure, $\lambda = 100$ m, so
$k = 2\pi/100 = 0.062832$ rad/m and, at 45°,
$k_x = k_y = 0.062832/\sqrt{2} = 0.044430$ rad/m.

**(b)** $k_N^{(x)} = \pi/20 = 0.157080$ and $k_N^{(y)} = \pi/40 = 0.078540$. Both
component magnitudes (0.044430) are below both limits, so this structure is **not
aliased**.

**(c)** The point of the exercise is the *contrast*: because
$k_N^{(y)}$ is half $k_N^{(x)}$, structures trending roughly north–south (large
$k_y$) alias twice as soon as structures trending east–west. A contour map of such a
grid can therefore show a spurious orientation preference. It is a sampling artefact
because it originates in $\Delta y \ne \Delta x$, not in the Earth; the test is to
re-grid to a symmetric interval and see whether the preference survives.

---

## ★★★10 — Truncated sinc reconstruction

A satisfactory experiment:

1. Build a band-limited field as a sum of sinusoids with $|k| \le k_N$.
2. Sample at $\Delta x$; reconstruct with the sinc interpolant truncated at $\pm m$
   samples, using the *periodic* sinc sum (rectangular window).
3. Measure the RMS reconstruction error over the interior, for $m = 1, 2, 4, 8, 16$
   and for samples-per-shortest-wavelength of 2, 3, 4, 6, 8.
4. **Expected behaviour:** the error falls as $1/m$ for a rectangular truncation
   (slow, logarithmic-like in practice for a spectrum with energy near $k_N$), and
   falls much faster once the samples-per-wavelength ratio rises, because the
   energy near $k_N$ — where truncation error is worst — is then small.
5. **Empirical rule:** use at least four samples per shortest wavelength to be
   preserved, and taper the truncation window. This is the quantitative basis of the
   lesson's "four to five stations" rule.
6. **Where it fails:** if the field is *not* band-limited, the error does not fall
   with $m$ at all — the reconstruction converges to the alias. That is the crucial
   negative result, and it should be demonstrated by adding a component above $k_N$
   and showing the error plateau.

---

## ★★★11 — Attempting to un-alias

A satisfactory answer will report:

- **(i) single-fold assumption.** Per component this is a single linear equation in
  one unknown, so it "succeeds" — but only because it *assumes* the answer, i.e. it
  picks the fold consistent with the interpreter's expectation. Two different
  assumptions give two different fields, both consistent with the samples. No
  information was added, so this is not a recovery.
- **(ii) compact support in the spectrum.** Succeeds if the true spectrum occupies a
  band narrower than the fold interval, because the overlapping replicas can then be
  separated. Measured behaviour: the recovery is exact when the support condition
  holds and fails completely when it does not; the boundary is sharp.
- **(iii) prior knowledge of a buried compact body.** This can succeed, because the
  prior is a genuine constraint: a small number of parameters (position, depth,
  moment) is being fitted to many samples. This is a **super-resolution** result: the
  information comes from the prior, not from the data. It is legitimate provided the
  prior is stated and tested, and illegitimate when it is smuggled in as
  "processing".

The role of the prior is therefore the whole content: aliasing destroys information,
and only a prior can replace it. Saying so is the honest report.

---

## ★★★12 — A two-component field at 60 m spacing

Components: $k_1 = 2\pi/100 = 0.062832$, $k_2 = 2\pi/600 = 0.010472$ rad/m;
$k_N = \pi/60 = 0.052360$.

Folding of the 100 m component:
$((0.062832+0.052360)\bmod 0.104720)-0.052360 = 0.010472-0.052360 = -0.041888$ →
apparent wavelength 150 m, **identical to the 600 m component's own fold** (the
600 m component, ratio 0.20, is not aliased and appears at 600 m). So after sampling
the record contains:

- an apparent 150 m component of amplitude 1.0 (the alias of the 100 m field);
- a genuine 600 m component of amplitude 0.4.

A low-pass with a 150 m cutoff passes wavelengths **longer** than 150 m, i.e. it
keeps the 600 m component and attenuates the 150 m alias — which is *not* the truth,
because the truth at that wavenumber was the 100 m field. The filter therefore
removes the alias and leaves a record whose only remaining content is a 600 m
component: **the filtered result is a 600 m anomaly of amplitude 0.4, and the
original 100 m anomaly has vanished entirely.** This is the concrete demonstration of
the lesson's claim: the filter removed the peak and left nothing that was true.
