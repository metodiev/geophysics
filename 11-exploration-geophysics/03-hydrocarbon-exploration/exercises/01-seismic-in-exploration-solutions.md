# Solutions — 11-03-01 Reflection Seismic in Exploration: From 2-D to 3-D

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Several problems have more than one defensible answer; where that is true it
> is said so.

Lesson: [01 Reflection Seismic in Exploration](../01-seismic-in-exploration.md).

---

## ★1 — Wavelength, resolution and period

$$\lambda = \frac{v}{f}, \qquad h_{\lambda/4} = \frac{v}{4f}, \qquad T = \frac{1}{f}.$$

For $v = 3.40\ \mathrm{km\,s^{-1}}$, $f = 40$ Hz:
$\lambda = 3400/40 = 85.0$ m, $\lambda/4 = 21.25$ m, $T = 25$ ms.

For $v = 2.60\ \mathrm{km\,s^{-1}}$, $f = 40$ Hz:
$\lambda = 65.0$ m, $\lambda/4 = 16.25$ m, $T = 25$ ms.

The lower velocity improves resolution at fixed frequency — which is why
near-surface surveys resolve beds that a deep, fast section cannot.

---

## ★2 — Fresnel radius

$$r_f = \sqrt{\frac{\lambda z}{2}},
\qquad
r_f(1500) = \sqrt{\frac{85\times1500}{2}} = \sqrt{63\,750} = 252.5\ \mathrm{m},
\qquad
r_f(3000) = \sqrt{127\,500} = 357.1\ \mathrm{m}.$$

The argument is $\mathrm{m}\times\mathrm{m} = \mathrm{m^2}$, so the root is in
metres. ✔

---

## ★3 — Alias frequency

$$f_{\max} = \frac{1}{2\Delta x\,p},
\qquad p = \frac{2\sin\theta}{v}
\qquad\Longrightarrow\qquad
f_{\max} = \frac{v}{4\Delta x\sin\theta}.$$

$$f_{\max} = \frac{3000}{4\times30\times\sin25^\circ}
= \frac{3000}{4\times30\times0.42262}
= \frac{3000}{50.71} = 59.2\ \mathrm{Hz}.$$

Dimensional check: $\mathrm{(m\,s^{-1})/m = s^{-1} = Hz}$. ✔ So 50 Hz data on a
30 m grid is unaliased for 25° dips; 30 m is a coarse grid for steep dips
(compare the lesson's table: 50 m gives 43.9 Hz at 20°).

---

## ★★4 — Fold from trace density

$$\text{fold} = \sigma_s\,T\,\Delta A, \qquad T = \sigma_r(2h_x^{\max})(2h_y^{\max}).$$

- $\sigma_s = 1/(0.040\times0.240) = 104.2\ \mathrm{km^{-2}}$
- $\sigma_r = 1/(0.025\times0.250) = 160.0\ \mathrm{km^{-2}}$
- continuum $T = 160\times5.0\times2.0 = 1600$;
  $\text{fold} = 104.2\times1600\times0.000625 = 104.2$
- discrete: $n_x = 2\,\mathrm{floor}(2500/25)+1 = 201$,
  $n_y = 2\,\mathrm{floor}(1000/250)+1 = 9$, $T = 1809$;
  $\text{fold} = 104.2\times1809\times0.000625 = 117.8$

Random-noise gain: $\sqrt{104.2} = 10.2$ (continuum) or $\sqrt{117.8} = 10.9$
(discrete).

**Why they differ.** The continuum integral counts $2h/\Delta$ positions, while a
regular grid contains $2\,\mathrm{floor}(h/\Delta)+1$ — it includes both
endpoints. The ratio factorises as $(201/200)\times(9/8) = 1.005\times1.125 =
1.131$, i.e. 13.1%, dominated by the crossline direction where the offset window
spans only four line spacings each side.

---

## ★★5 — Side-swipe versus resolution

$$z_{\text{app}} = \sqrt{z^2+y^2} = \sqrt{1800^2+900^2} = \sqrt{4.05\times10^{6}}
= 2012.5\ \mathrm{m},$$

an error of $212.5$ m, i.e. **+11.8%**. Compare that with the vertical
resolution of 21 m: the side-swipe depth error is **ten times** the resolution
limit.

**Conclusion.** For an out-of-plane feature, a 2-D line's depth is wrong by an
amount an order of magnitude larger than its own resolution, so the resolution
number is irrelevant to the interpretation. The remedy is acquisition (3-D), not
processing: the apparent position also *moves with the line location*, so the
error cannot be recognised from the data on one line.

---

## ★★6 — Is an 18 m bed resolvable at 45 Hz?

$$\lambda = \frac{3100}{45} = 68.9\ \mathrm{m},
\qquad \frac{\lambda}{4} = 17.2\ \mathrm{m}.$$

The $\lambda/4$ rule says the bed is right at the limit. The measured criterion
from the lesson is stricter: the read-off thickness becomes accurate to 10% at
$0.17\,v/f_0 = 0.17\times3100/45 = 11.7\ \mathrm{m}$. Since
$18 > 11.7$, the thickness is **resolvable to about 10%**, with a margin of
1.5×.

Two caveats must be stated with that answer:

1. The 0.17 coefficient is measured for a Ricker wavelet; a different wavelet
   changes it, so the wavelet must be named.
2. "Resolvable" here means the peak-to-trough time tracks thickness. If the
   question were "can thickness be inverted from amplitude alone?", the answer
   would be no: the amplitude–thickness relation is non-monotonic and also
   depends on the reflection coefficient.

No acquisition change is required; if the noise level were high enough that the
bed's composite amplitude fell below 3× noise, the answer would change — so the
noise must be stated.

---

## ★★★7 — A worked design

**Statement.** Target: 40 m thick reservoir at 3.0 km, $v_{\text{rms}} =
3.2\ \mathrm{km\,s^{-1}}$, steepest dip 30°, deepest useful frequency 35 Hz,
random-noise requirement: the target event at 2× noise on a single trace.

1. $\lambda = 3200/35 = 91.4$ m; $\lambda/4 = 22.9$ m. The 40 m reservoir is
   above the limit — resolvable. ✓
2. Bin: $f_{\max} = 3200/(4\Delta x\sin30^\circ) = 3200/(2\Delta x)$; requiring
   $f_{\max} \ge 35$ Hz gives $\Delta x \le 3200/70 = 45.7$ m. Choose 25 m
   (standard half-offset bin 12.5 m).
3. Fresnel: $r_f = \sqrt{91.4\times3000/2} = 370.3$ m — wider than any channel
   or fault block of interest, so migration with good offsets is mandatory.
4. Fold: choose $\sigma_s = 50\ \mathrm{km^{-2}}$, $T$ from 25 m groups on
   9 lines 300 m apart with offsets $\pm3$ km and $\pm1.2$ km:
   $T = 1600$ (continuum) and the discrete count gives
   $n_x = 241$, $n_y = 9$, $T = 2169$. With
   $\sigma_r = 1/(0.025\times0.300) = 133.3$; the discrete fold is
   $50\times2169\times0.000625 = 67.8$.
5. Gain: $\sqrt{67.8} = 8.2$, so a target at 2× noise becomes 16× — comfortable.
6. **Binding limit:** the Fresnel zone / migration quality, not fold and not
   vertical resolution. That is the answer a reviewer wants: name the limit.

---

## ★★8 — Derivation and the 10% condition

**Derivation.** With midpoints $m = \tfrac12(s+r)$ and offsets $h = r-s$,

$$\frac{\partial(m,h)}{\partial(s,r)} =
\begin{pmatrix} \tfrac12 & \tfrac12 \\ -1 & 1\end{pmatrix},
\qquad
\left|\det\right| = \tfrac12(1) - \tfrac12(-1) = 1 .$$

So the density of $(m,h)$ pairs in phase space equals the product of the source
and receiver densities, $\sigma_s\sigma_r$, and integrating over the offset
window gives

$$\text{fold} = \sigma_s\sigma_r\,\Delta A\,(2h_x^{\max})(2h_y^{\max})
= \sigma_s\,T\,\Delta A .$$

**10% condition.** For a direction where the offset window spans $N$ line
spacings, the discrete and continuum counts are $2N+1$ and $2N$, so the ratio is

$$R = \frac{2N+1}{2N} > 1.1
\qquad\Longleftrightarrow\qquad
2N+1 > 2.2N
\qquad\Longleftrightarrow\qquad
N < 5 .$$

**Check for ★★4.** Crossline: $h_y = 1000$ m, $N = 1000/250 = 4 < 5$ → $R =
9/8 = 1.125 > 1.10$ ✔. Inline: $N = 2500/25 = 100 \ge 5$ → $R = 201/200 =
1.005$. The measured count reproduces the discrete value (midpoint counting of
the synthetic grid returns the discrete fold to within the lattice effects
discussed in the lesson).
