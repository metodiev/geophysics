# Solutions — 17-03-04 Atmospheric and Orbital Error Correction in InSAR

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [04 Atmospheric and Orbital Error Correction](../04-insar-atmospheric-correction.md).

---

## ★1 — Zenith delay from an exponential profile

$$L_{\text{zenith}} = 10^{-6}\int_0^{\infty} N_s e^{-z/H}\,\mathrm{d}z
= 10^{-6} N_s H.$$

$$L_{\text{zenith}} = 10^{-6} \times 300\ \mathrm{ppm} \times 7500\ \mathrm{m}
= 2.2500\ \mathrm{m}.$$

Units: $N$ has units of ppm but is $10^{6}(n-1)$ and therefore dimensionless;
multiplying by the $10^{-6}$ prefactor and by a length in metres gives metres.

At $z = 45^\circ$ in the plane-parallel mapping:
$$L(45^\circ) = \frac{2.2500}{\cos 45^\circ} = \frac{2.2500}{0.7071}
= 3.1819\ \mathrm{m}.$$

The mapping factor is $1/\cos z = 1.4142$, a $41\%$ increase. Note that this
approximation overestimates the delay at large $z$ for a real (curved) Earth,
which is why operational processing uses a mapping function rather than
$1/\cos z$.

---

## ★2 — Delay to phase and apparent displacement

$$\Delta\phi = \frac{4\pi}{\lambda}\Delta L = 222.16\ \mathrm{rad\,m^{-1}}
\times 0.015\ \mathrm{m} = 3.3324\ \mathrm{rad}.$$

Fringes:
$$\frac{3.3324}{2\pi} = 0.5303\ \text{fringes}.$$

Apparent line-of-sight displacement: **1.50 cm** (the one-to-one conversion).

If the motion were assumed purely vertical at $\theta = 35^\circ$:
$$d_v = \frac{d_{\text{LOS}}}{\cos\theta} = \frac{1.50}{0.8192}
= 1.831\ \mathrm{cm} = 18.31\ \mathrm{mm}.$$

So the same phase is "1.5 cm of range change" or "1.83 cm of uplift", depending
entirely on an assumption that the data do not test. That inflation factor
$1/\cos\theta = 1.221$ is a property of the geometry, and forgetting it is a
$22\%$ error.

---

## ★3 — The three sources and their signatures

| source | spatial signature | temporal signature |
|---|---|---|
| stratified | smooth, monotone (or nearly) in elevation; repeats its *shape* whenever the weather is similar | appears in individual dates, does not accumulate; appears identical in pairs sharing the same acquisition |
| turbulent | random, scale-dependent, no correlation with topography; structure function power-law | redrawn at every acquisition (decorrelates in hours to days) |
| orbital | low-order polynomial in range and azimuth across the whole scene; often a long-wavelength tilt | identical in all pairs sharing the same orbit solution; persists across dates and correlates between them |

The discriminating question is always "does it repeat when the geometry or the
solution repeats?" A deformation signal repeats in *space* but evolves in *time*
with the physical process; a stratified screen repeats with weather; an orbital
error repeats with the orbit.

---

## ★4 — Why the regression slope is biased

**(a)** The least-squares slope is
$$\hat{c}_1 = \frac{\mathrm{cov}(h,d)}{\mathrm{var}(h)}
= \frac{\sum_k (h_k-\bar{h})(d_k-\bar{d})}{\sum_k (h_k-\bar{h})^{2}}.$$

The true $d(h) = 3.00\,x - 0.25\,x^{2}$ mm with $x = h/1\ \mathrm{km}$, and the
curvature term $x^{2}$ is *correlated with* $x$ over a one-sided range of $x$
(here $x$ spans about $0.23$–$0.82$, so $x^{2}$ is nearly monotone in $x$).
A positive correlation between $x^{2}$ and $x$ means the curvature contributes
positively to $\mathrm{cov}(h,d)$, and since the true coefficient is negative
($-0.25$) the contribution to the fitted slope is negative: $\hat{c}_1$ is
**biased low**, which is what the demonstration measures
($2.3077 < 3.00\ \mathrm{mm\,km^{-1}}$). The size scales as
$c_2\,\mathrm{cov}(x,x^{2})/\mathrm{var}(x)$.

**(b)** If the relation were exactly linear, the least-squares line would recover
the slope exactly and the residual rms would be **zero** (to numerical precision),
because the fit spans the same design that generated the data.

That is the diagnostic value and its limit: a small residual rms certifies only
that the model is flexible enough to describe *this* profile. It says nothing
about whether the fitted coefficients are the physical ones — a straight line
through a quadratic has a small residual over a narrow range while its slope is
$23\%$ wrong. Residual size is a *fit* diagnostic; coefficient size is the
*physical* diagnostic, and they must be checked separately.

---

## ★5 — Structure function extrapolation

$$D(r) = D_0\left(\frac{r}{r_0}\right)^{0.71}
= 4.0 \left(\frac{4.0}{1.0}\right)^{0.71}.$$

$4^{0.71} = e^{0.71 \times 1.3863} = e^{0.9843} = 2.676$.

$$D(4\ \mathrm{km}) = 4.0 \times 2.676 = 10.70\ \mathrm{mm^{2}}.$$

RMS difference:
$$\sqrt{10.70} = 3.27\ \mathrm{mm}.$$

Largest separation with $D < 5.0\ \mathrm{mm^{2}}$:
$$\left(\frac{r}{1\ \mathrm{km}}\right)^{0.71} = \frac{5.0}{4.0} = 1.25
\;\Longrightarrow\;
r = 1.25^{1/0.71} = 1.25^{1.408} = 1.369\ \mathrm{km}.$$

So beyond about $1.4\ \mathrm{km}$ this screen exceeds the $5\ \mathrm{mm^{2}}$
threshold — which is the quantitative statement of "the atmosphere decorrelates
over a few kilometres", and it is what a spatial filter or a dense GNSS network
is trying to beat. Note that the exponent $0.71$ was measured over a specific
range of separations (Section 3.4); extrapolating to $4\ \mathrm{km}$ assumes the
scaling continues, which the saturation behaviour says it will not indefinitely.

---

## ★6 — What a stack can average down

$$\sigma_{\text{mean}} = \sigma\sqrt{\rho + \frac{1-\rho}{N}},
\qquad \sigma = 8.0\ \mathrm{mm},\ N = 30.$$

| $\rho$ | $\sqrt{\rho + (1-\rho)/30}$ | $\sigma_{\text{mean}}$ (mm) |
|---|---|---|
| 0.0 | $\sqrt{0.03333} = 0.1826$ | 1.46 |
| 0.3 | $\sqrt{0.32333} = 0.5686$ | 4.55 |
| 0.6 | $\sqrt{0.61333} = 0.7832$ | 6.27 |
| 0.9 | $\sqrt{0.90333} = 0.9504$ | 7.60 |

Check the extremes: at $\rho = 0$ the result is the familiar
$\sigma/\sqrt{N} = 8/\sqrt{30} = 1.46\ \mathrm{mm}$; at $\rho \to 1$ it is
$\sigma$ itself, since a screen present in every epoch cancels in every
difference and never appears in the mean, while the common-mode part is exactly
what the *mean* retains.

**Practical consequence:** the useful length of a stack is set by how correlated
the weather is between acquisitions, not by how many acquisitions there are.
Beyond the correlation time of the screens, adding epochs buys the
$1/\sqrt{N}$ reduction; within it, it buys almost nothing. The diagnostic is to
plot the residual of the epoch mean against $N$ for nested subsets, and check
whether it follows $1/\sqrt{N}$ or flattens — the flattening *is* the measurement
of $\rho$.

---

## ★7 — Validating an atmospheric correction (specification)

**Target.** $2\ \mathrm{mm\,yr^{-1}}$ over 4 years is $8\ \mathrm{mm}$ of total
signal, i.e. $0.28$ of a fringe at this wavelength. The correction must therefore
be good to well under a fringe, and its *bias* matters more than its scatter.

**Independent data.** (i) A local continuous GNSS station (or several) sampling
the same region, whose height time series is independent of the radar. (ii) A
numerical weather model field at the acquisition times, used to compute a
physically modelled delay. (iii) The radar amplitude and coherence, to exclude
regions where the correction is being applied to noise.

**Statistics.** The bias is the quantity to test: the mean of
(corrected InSAR rate − GNSS rate) over many stations, with its standard error.
The scatter alone is not a validation, because a correction can be precise and
biased.

**Acceptance criterion.** The *bias* must be below the target trend divided by
three, i.e. below $0.7\ \mathrm{mm\,yr^{-1}}$, and the scatter must be below the
single-epoch noise propagated into the rate. Both must be stated before the
comparison is made.

**Detecting that the correction removed signal.** Compare the corrected and
uncorrected rates in a region known to be deforming and in a region known to be
stable. A correction that is too aggressive reduces the *apparent* rate in the
stable region toward zero — good — but also flattens the deforming region, which
shows up as an over-correction. The signature is a decreasing trend with
increasing correction strength in the *deforming* area while the stable area
stops improving. The demonstration's ramp experiment is the toy version of this
test: the "quadratic, all pixels" row had the smallest residual and recovered
only $60\%$ of the signal.

---

## ★8 — Why a $300\times300$ scene cannot measure a turbulent exponent

**Conditions.** The power-law scaling $D \propto r^{\beta-1}$ requires
$k_{\min} r \ll 1$ (the separation small compared with the largest structure) and
$k_{\max} r \gg 1$ (large compared with the smallest structure). Writing $r$ in
pixels, $k_{\max} = 2\pi/10$ rad/pixel for the stated smallest structure of 10
pixels, and $k_{\min} \gtrsim 1/L$ where $L$ is the scene size in pixels.

**Scale separation.** The window over which a power law can be fitted is
approximately $r \in [10, L/10]$: at least 10 pixels above the smallest structure
and a factor 10 below the largest scale present. With $L = 300$ pixels that
window is $r \in [10, 30]$ — one third of a decade. A log-log fit over a third of
a decade has an exponent uncertainty of order a few tenths (the demonstration
needed a 500-fold band and still had a residual of 0.06 in the exponent). Any
exponent reported from such a fit is dominated by the fit range.

**What can legitimately be estimated from a 300-pixel scene:**
1. the **variance** of the screen over the scene (a single number, no scaling
   assumption);
2. the **structure function at one or two specific separations**, quoted as
   values with their separations, not as an exponent;
3. an **empirical decorrelation length** defined by the separation at which
   $D(r)$ reaches some stated fraction (say half) of its saturation value — a
   definition that is always well posed even when no power law exists;
4. the **correlation with topography**, which needs no scaling assumption at all
   and is the most useful diagnostic in practice.

The honest report therefore says "the screen has an rms of 3 mm and a
decorrelation length of 12 km (half-saturation definition)", not "the screen has
a turbulent exponent of 0.7".
