# Solutions — 14-02-05 Surface NMR for Direct Water Detection

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All kernels and profiles are **SYNTHETIC**.

Lesson: [05 Surface NMR for Direct Water Detection](../05-nmr-for-groundwater.md).

---

## ★1 — Larmor frequency and tuning

$$f_L = \frac{\gamma}{2\pi}B = 42.577 \times 47\,000\ \mathrm{Hz}
= 2.0011 \times 10^{6}\ \mathrm{Hz} = \mathbf{2.0011\ kHz}.$$

(Scale-check against the lesson's table: 50 000 nT gives 2.1289 kHz and
47 000/50 000 × 2.1289 = 2.001 ✓.)

**Mistuning.** The proton resonance in a porous medium is a narrow line, so
mistuning by 50 Hz means the excitation only partly tips the spins: the recorded
amplitude falls in a way that is indistinguishable from less water. In a field that
varies by 100 nT across the loop, the Larmor frequency varies by

$$\Delta f = 42.577 \times 100\ \mathrm{Hz} = 4.26\ \mathrm{kHz}$$

across the loop — a spread thousands of times larger than the line width, so a
single narrow-band excitation excites one part of the loop and not the rest. The
consequence is quantified as if it were a water-content variation, which is why a
surface-NMR survey near a magnetic anomaly must map the field across the loop (with a
magnetometer) and either widen the bandwidth or split the loop.

---

## ★2 — Pulse moment and kernel width

$$z_q = 12\sqrt{q} = 30\ \mathrm{m}
\Longrightarrow
\sqrt{q} = \frac{30}{12} = 2.5
\Longrightarrow
q = 6.25\ \mathrm{A\,ms}.$$

Normalized FWHM:
$$\mathrm{FWHM} = 1.1548\,z_q = 1.1548 \times 30 = 34.6\ \mathrm{m}.$$

**What that means for a 5 m layer at 30 m.** The kernel is an order of magnitude
wider than the layer, so the measurement integrates the layer together with roughly
30 m of its surroundings: the recovered water content is a *weighted average over
±17 m*, and a 5 m layer cannot be resolved at that depth by this method at all. The
kernel width grows in proportion to depth, so the ratio (layer thickness)/(kernel
width) worsens linearly with depth: **at 30 m, surface NMR sees stratigraphy coarser
than about 35 m, full stop.** (This is why a thin aquifer at depth is a legitimate
"no" answer even when the water is certainly there.)

---

## ★3 — Water column

$$\text{water column} = \theta \times b = 0.15 \times (35 - 20) = 2.25\ \mathrm{m}
= \mathbf{2250\ mm}.$$

The water column is the product the method determines most robustly, because the
forward model integrates over depth and so is insensitive to how the water is
distributed within the kernel. Reporting "2.25 m of water between 20 and 35 m" is a
defensible statement even when the layer boundaries are not.

---

## ★★4 — Noise required to resolve $\theta = 0.10$ at 2σ

$\sigma_\theta$ scales linearly with the noise level $\sigma$:
$$\frac{\sigma_\theta}{\sigma} = \frac{0.0194}{0.05} = 0.388
\quad \text{for the 20–30 m band.}$$

To resolve $\theta = 0.10$ at two standard deviations, we need
$2\sigma_\theta \le 0.10$, i.e. $\sigma_\theta \le 0.05$:
$$\sigma = \frac{0.05}{0.388} = 0.129\ \text{(in sounding-amplitude units)}.$$

The lesson's inversion ran with $\sigma = 0.0504$, i.e. **2.0% of the peak modelled
amplitude** (2.52), so the required level is
$$\frac{0.129}{2.52} = 5.1\%\ \text{of the peak} \quad\approx 2.6\times
\text{the noise actually used.}$$

Stacking improves the signal-to-noise ratio as $\sqrt{N}$, so the factor of 2.6 costs
about $2.6^{2} \approx 7$ stacks — cheap.

**Practical implication.** Resolving a 10% water content at 20–30 m is
*comfortable*: the lesson's own inversion recovered a layer average of 0.222 for a
true 0.25 (11% low) at $\sigma = 0.05$. What is *not* comfortable is the deepest
band: the 45–60 m entry has $\sigma_\theta/\sigma = 0.0571/0.05 = 1.14$, so
resolving $\theta = 0.10$ at 2σ would require
$$\sigma \le \frac{0.05}{1.14} = 0.044,$$
which is *below* the 0.0504 achieved in the example. **There is a depth beyond which
the target water content cannot be resolved at any realistic stacking**, and the
sounding design must compute that depth (as in ★★★7) rather than assume a
rule-of-thumb depth limit.

---

## ★★5 — $T_2$ to pore radius, and the $\rho_2$ penalty

$$T_2 = \frac{r}{3\rho_2} \Longrightarrow r = 3\rho_2 T_2.$$

For $\rho_2 = 20\ \mathrm{\mu m\,s^{-1}} = 20 \times 10^{-6}\ \mathrm{m\,s^{-1}}$
and $T_2 = 40\ \mathrm{ms} = 0.040$ s:
$$r = 3 \times 20 \times 10^{-6} \times 0.040 = 2.4 \times 10^{-6}\ \mathrm{m}
= \mathbf{2.4\ \mu m}.$$

For $\rho_2 = 40\ \mathrm{\mu m\,s^{-1}}$:
$$r = 3 \times 40 \times 10^{-6} \times 0.040 = 4.8 \times 10^{-6}\ \mathrm{m}
= \mathbf{4.8\ \mu m}.$$

**The same data give a pore radius differing by a factor of two**, because $r$ is
directly proportional to $\rho_2$. The practical consequence is that a
$T_2$-derived pore size is a *model output* unless $\rho_2$ has been measured for
that mineral assemblage (typically from a core: measure $T_2$ on a sample of known
pore size, or calibrate against mercury injection or thin sections). What survives
without calibration is:
- the *distribution* of $T_2$ (a relative pore-size distribution),
- the *mobile-water fraction*, since the echo-time threshold is in $T_2$, not in
  radius,
- relative comparisons between units logged with the same tool.
What does not survive is an absolute pore radius, or a permeability that depends on
it through an uncalibrated constant.

---

## ★★6 — The invisible fraction

$$\theta_{\text{invisible}} = 0.30 - 0.22 = 0.08,
\qquad \frac{0.08}{0.30} = \mathbf{26.7\%}.$$

**Two physically distinct explanations.**

1. **Clay-bound (and capillary) water in micropores.** With
   $\rho_2 = 20\ \mathrm{\mu m\,s^{-1}}$ and a 2.3 ms echo time, water in pores
   below $r_{\min} = 3\rho_2 t_{\text{echo}} = 3(20 \times 10^{-6})(2.3 \times
   10^{-3}) = 0.14\ \mu$m relaxes before the first echo and is not recorded. In a
   unit with 27% of its porosity in that size range, the unit is clay- or
   silt-rich.
2. **Water in isolated pores or dead-end volumes**, which is proton-visible and
   relaxes slowly, but does not contribute to the *flux* the unit can transmit. This
   is the mobile-versus-immobile distinction. It would NOT be invisible to a
   surface-NMR measurement (the protons are still there), so it cannot explain a
   *deficit* in NMR water content — it is the explanation for a difference between
   NMR-derived and *producible* water, not between NMR and total.

So explanation 2 cannot account for the observed deficit, and a strictly honest
answer distinguishes it: for this dataset the deficit must be fast-relaxing water.

**What distinguishes them** (for the deficit case):
- the **$T_2$ spectrum** from the same sounding: a peak at short $T_2$ (below a few
  ms) confirms bound or capillary water, whereas a deficit with no short-$T_2$ peak
  points to a measurement or calibration problem instead;
- a **core measurement** of the clay fraction and its cation-exchange capacity, or a
  **mercury-injection** pore-size distribution, which quantifies the sub-0.14 µm
  fraction directly;
- a **shorter echo time** (a smaller loop or a purpose-built system), which moves
  $r_{\min}$ down and should recover part of the deficit if the cause is fast
  relaxation.

---

## ★★★7 — Sounding design for a 20 m aquifer at 25 m beneath a clay cover

**Pulse moments.** For a target interval of 25–45 m, the kernel must peak between
25 and 45 m: $z_q = 12\sqrt{q}$ gives
$$q_{\min} = \left(\frac{25}{12}\right)^{2} = 4.34\ \mathrm{A\,ms}, \qquad
q_{\max} = \left(\frac{45}{12}\right)^{2} = 14.1\ \mathrm{A\,ms}.$$

To sample the interval with overlapping kernels, use at least the width per step:
the FWHM at $z_q = 35$ m is 40 m, which is wider than the whole interval, so a
logarithmic ladder of **12–16 moments from 2 to 20 A ms** provides overlapping
coverage with some redundancy; there is no point going beyond the point where
kernel amplitude at 45 m is below the noise.

**Stacking.** The noise enters as
$\sigma_\theta = \sigma/\sqrt{\sum_q\sum_z K^2\Delta z}$ — every additional useful
moment adds to the denominator, and stacking reduces $\sigma$ as $\sqrt{N}$. The
lesson's inversion achieved $\sigma = 0.0504$ (2% of the peak amplitude), which is the
target here; the number of stacks needed to reach it from a site's unstacked noise
$\sigma_0$ is roughly $(\sigma_0/0.0504)^{2}$ per moment, which is why a
surface-NMR sounding takes hours rather than minutes.

**Error budget for the water content.**

| source | magnitude | effect on $\theta$ |
|---|---|---|
| noise at $\sigma = 0.05$ (after stacking) | | 0.013–0.057 depending on band (lesson table) |
| regularisation bias (λ chosen by the discrepancy principle) | | 0.01–0.03 on a 20 m unit |
| excitation/off-resonance (field variation across the loop) | 2–5% | 0.005–0.015 |
| unknown $T_2$ distribution (bound water) | up to 0.04 in clay-rich units | 0.02–0.04 |
| Combined | | $\approx 0.05$ on a 20 m unit |

**Form of the report.** Because the inverse problem has 12–16 data and tens of
unknowns, the deliverable must be: (i) the water column in mm within the target
interval, with its uncertainty; (ii) the depth interval over which water content
exceeds a stated threshold; (iii) the mobile water fraction from the $T_2$ spectrum;
(iv) the regularisation parameter, the data misfit and the residual pattern; and
(v) an explicit statement that the layer boundaries are model-dependent. **A
profile with sharp boundaries is not a defensible output of a sounding.**

**Why the conductive cover is both a help and a hindrance.**

- **Help:** surface NMR is essentially independent of the ground's conductivity, so
  the clay cover that attenuates and screens ERT and TDEM does not degrade the NMR
  signal at all — the method sees through the very unit that blinds the electrical
  methods. This is the single strongest reason to choose NMR here.
- **Hindrance:** the clay cover is also a water-bearing unit (bound and capillary
  water), and it lies in the kernel of the shallow pulse moments; some of its water
  contributes to the $T_2$ spectrum and can be mistaken for deeper mobile water, and
  the field's homogeneity is usually poorer in clay-rich ground, which broadens the
  resonance and lowers the signal. The mitigation is a $T_2$ analysis with a
  moisture-plot (mobile versus bound) display, and a sounding with enough moments
  to separate the cover from the aquifer.

---

## ★★★8 — What the linearity check proves, and a verification suite

**What $A(2\theta) = 2A(\theta)$ to $1 \times 10^{-9}$ verifies.** That the
implementation of the depth integral is *linear* in the water content: the kernel is
applied as a matrix, the quadrature weights are applied consistently, and no
normalisation depends on the profile. It confirms that the inverse problem is
linear, which justifies the bounded-linear solver used in the lesson. **It is a
code check, not a physics check.** A wrong kernel — one whose $z_q$ scaling was
$\sqrt{2q}$ instead of $\sqrt{q}$ — would pass it perfectly, because linearity is
invariant to the kernel's shape.

**A verification suite.**

1. **Analytic limit: zero water content.** With $\theta \equiv 0$ the sounding must
   return exactly zero at every moment, and with $\theta$ a constant $\theta_0$ the
   sounding must equal $\theta_0 \int K(q,z)\,\mathrm{d}z$ — computable by an
   independent high-accuracy quadrature. *Catches:* a missing quadrature weight, an
   offset, a wrong depth axis origin. *Misses:* any error in the kernel's shape.

2. **Physical-scaling check: the $\sqrt{q}$ law.** Verify that
   $\arg\max_z K(q,z) = 12\sqrt{q}$ and that the normalized FWHM scales as
   $1.1548\,z_q$, both derived in the lesson by solving $ue^{1-u} = 0.5$. *Catches:*
   a kernel whose peak does not move correctly with the pulse moment — the error that
   would misassign *depth* to every recovered water content. *Misses:* an error in
   the kernel's amplitude, which the zero and constant tests already fix.

3. **Convergence/interpolation check.** The inversion integrates a kernel sampled on
   a grid; halve $\Delta z$ and confirm that the modelled sounding for a *known*
   profile converges at the expected order (and that the discrete kernel's
   normalisation is grid-independent). *Catches:* a kernel normalised by the number
   of cells, or a quadrature that depends on the grid — the failure mode that makes a
   result irreproducible on a different depth grid.

4. **Consistency check against a borehole NMR log.** Forward-model the *measured*
   borehole water-content profile through the surface kernel and compare the
   prediction with the observed sounding, including its noise. *Catches:* a wrong
   transmit current calibration (which scales $q$ and therefore every depth), a
   wrong loop geometry, and any systematic error in the surface-measured amplitude.
   This is the only test in the list that is a **validation** rather than a
   verification, because it compares the model with a measurement rather than with
   itself.

**What the suite cannot establish.** That the inverted *profile* is the true
subsurface water distribution. The kernels overlap so heavily that a family of
profiles reproduces any sounding within its noise — the regularisation bias measured
in the lesson (layer average 0.222 against a true 0.25, and a water column accurate
to 1.2% while the boundaries move by metres) is *physical* non-uniqueness, not a
code defect. No verification test can remove it; only an independent measurement
(a borehole log, a core, a second surface method) can reduce it, and the honest
deliverable remains the bounded family plus its stated regularisation.

---

## Module mastery checkpoint, parts (a)–(b)

**Part (a).** With $q = 4$ A ms:
$$z_q = 12\sqrt{q} = 12\sqrt{4} = \mathbf{24.0\ m}, \qquad
\mathrm{FWHM} = 1.1548\,z_q = 1.1548 \times 24 = \mathbf{27.72\ m}$$
(printed as 27.7 m on the demonstration's 0.1 m depth grid).

**What the width implies for the 24–32 m aquitard.** An 8 m thick unit inside a
27.7 m wide kernel is **not resolvable**: the kernel's half-width (13.9 m) exceeds the
unit's thickness, so the aquitard's low water content is smeared over roughly ±14 m and
appears only as a reduction in the *average* water content of the interval 10–38 m.
The correct claim is a bound — "the average water content between about 10 and 38 m is
$X$" — not "there is a dry unit at 24–32 m".

**Part (b).** Water column over 10–25 m:
$$0.2232 \times (25 - 10) = 0.2232 \times 15 = 3.348\ \mathrm{m}
= \mathbf{3348\ mm}.$$

**Why the water column is more reliable than the boundaries.** The sounding is a depth
*integral* of the water content, so the total is a linear functional of the data that is
well constrained by the data themselves; the *distribution* within the kernel is not.
The lesson's inversion demonstrates this directly: it recovered the water column to
$-1.2\%$ (10 591.9 mm against a true 10 725.0 mm) while the layer boundaries moved by
metres and the layer average came back as 0.222 against a true 0.25. **Report the
column, bound the profile.**
