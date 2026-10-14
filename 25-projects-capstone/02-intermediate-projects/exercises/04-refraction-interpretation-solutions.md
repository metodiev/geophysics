# Solutions — 25-02-04 Project: Interpreting a Refraction Survey

> Read after attempting. Lesson:
> [04 Refraction Interpretation](../04-refraction-interpretation.md). All values
> are **SYNTHETIC** teaching numbers printed by
> [`code/refraction_interpretation_demo.py`](../code/refraction_interpretation_demo.py).
> Times are in milliseconds, offsets in metres, velocities in m s⁻¹ unless stated.

---

## ★1 — Critical angles and the first arrival at 40 m

$$\theta_{12} = \arcsin\frac{v_1}{v_2} = \arcsin\frac{0.40}{1.60} = \arcsin 0.25
= 14.48°,$$

$$\theta_{13} = \arcsin\frac{0.40}{4.00} = \arcsin 0.10 = 5.74°.$$

At $X = 40\ \mathrm{m}$:

$$t_1 = \frac{40}{400} = 0.1000\ \mathrm{s} = 100.00\ \mathrm{ms},$$

$$t_2 = \frac{40}{1600} + \frac{2 \times 3.0 \times 1549.19}{400 \times 1600}
= 25.000 + 14.524 = 39.52\ \mathrm{ms},$$

$$t_3 = \frac{40}{4000} + \frac{6 \times 3979.95}{1.6\times10^{6}}
+ \frac{16 \times 3666.06}{6.4\times10^{6}}
= 10.000 + 14.925 + 9.165 = 34.09\ \mathrm{ms}.$$

**Branch 3 is the first arrival** (34.09 ms) — the deep interface, not the
weathered layer, because at 40 m the survey is well past both crossovers
(8.0 m and 26.0 m).

---

## ★2 — A crossover

$$X_c = 2h_1\sqrt{\frac{v_2+v_1}{v_2-v_1}}
= 2 \times 4.0 \times \sqrt{\frac{2.00+0.50}{2.00-0.50}}
= 8.0 \times \sqrt{1.6667} = 8.0 \times 1.2910 = 10.33\ \mathrm{m}.$$

---

## ★3 — Thickness from a branch intercept

$$h_1 = \frac{a_2\,v_1v_2}{2\sqrt{v_2^{2}-v_1^{2}}}
= \frac{0.014522115 \times 400 \times 1600}{2\sqrt{1600^{2}-400^{2}}}
= \frac{0.014522115 \times 640\,000}{3098.387} = 3.00\ \mathrm{m}.$$

Unit check: $\mathrm{s} \times (\mathrm{m\,s^{-1}})^{2} /
\mathrm{m\,s^{-1}} = \mathrm{m}$ ✔.

---

## ★4 — The second thickness

Layer 1's contribution to the branch-3 intercept:

$$\frac{2h_1\sqrt{v_3^{2}-v_1^{2}}}{v_1v_3}
= \frac{6 \times 3979.95}{400 \times 4000} = \frac{23\,879.7}{1.6\times10^{6}}
= 0.0149248\ \mathrm{s}.$$

Residual intercept:
$a_3' = 0.0240915 - 0.0149248 = 0.0091667\ \mathrm{s}$.

$$h_2 = a_3' \times \frac{v_2v_3}{2\sqrt{v_3^{2}-v_2^{2}}}
= 0.0091667 \times \frac{1600 \times 4001}{2\sqrt{4001^{2}-1600^{2}}}
= 0.0091667 \times 872.83 = 8.00\ \mathrm{m},$$

against a true 8.0 m. Note how the residual is $38\%$ of the raw intercept: the
upper layer's delay dominates it, which is why an error in $h_1$ propagates
amplified into $h_2$.

---

## ★5 — The hidden layer in model B

**Crossover 1 → 2:**

$$X_c^{(12)} = 2h_1\sqrt{\frac{v_2+v_1}{v_2-v_1}}
= 4.0\sqrt{\frac{2.50}{0.50}} = 4.0 \times 2.2361 = 8.94\ \mathrm{m} \approx 9.0\ \mathrm{m}.$$

**Crossover 2 → 3.** Set $t_2 = t_3$ with the intercepts
$t_i^{(2)} = \frac{4\sqrt{2.25-1.00}}{1.0\times1.5} = 0.0029814\ \mathrm{s}$ and

$$t_i^{(3)} = \frac{4\sqrt{25-1}}{1.0\times5.0} + \frac{4\sqrt{25-2.25}}{1.5\times5.0}
= 0.0039192 + 0.0025466 = 0.0064658\ \mathrm{s}:$$

$$X\left(\frac{1}{1500}-\frac{1}{5000}\right) = 0.0064658 - 0.0029814
\;\Longrightarrow\; X \times 4.6667\times10^{-4} = 0.0034844
\;\Longrightarrow\; X = 7.47\ \mathrm{m}.$$

Since $7.47 < 8.94$, the deeper refractor overtakes the direct wave **before** the
hidden layer ever does, so branch 2 is never the first arrival — the demonstration
confirms it is first at zero offsets.

**General condition.** A layer is hidden when its travel-time line lies above the
line of the layer beneath it over the entire observable offset range; for a single
hidden layer this is equivalent to the crossover to the deeper refractor occurring
at a shorter offset than the crossover to the hidden one.

---

## ★6 — The apparent depth error

The two-layer interpretation uses $a_3 = 0.0064658\ \mathrm{s}$ with
$v_1 = 1000$, $v_3 = 5000\ \mathrm{m\,s^{-1}}$:

$$h_\text{app} = a_3\frac{v_1v_3}{2\sqrt{v_3^{2}-v_1^{2}}}
= 0.0064658 \times \frac{5.0\times10^{6}}{2 \times 4898.98}
= 0.0064658 \times 510.31 = 3.30\ \mathrm{m}.$$

Error against the true cover of 4.00 m:

$$\frac{4.00-3.30}{4.00} = 17.5\%, \qquad \text{absolute } -0.70\ \mathrm{m}.$$

**In units of the statistical uncertainty.** The branch-3 picks span 15.5–60 m
(the demonstration selects $X > 15$) at 0.5 m spacing, so $N = 90$,
$\bar X = 37.75\ \mathrm{m}$ and
$\sum(X_i-\bar X)^{2} = d^{2}N(N^{2}-1)/12 = 0.25 \times 60742.5 = 15\,186\
\mathrm{m^{2}}$. With $\sigma_t = 1.5\ \mathrm{ms}$,

$$\sigma_a = \sigma_t\sqrt{\frac{1}{N} + \frac{\bar X^{2}}{\sum(X_i-\bar X)^{2}}}
= 1.5\times10^{-3}\sqrt{0.01111 + 0.09384} = 4.86\times10^{-4}\ \mathrm{s},$$

$$\sigma_{h} = 510.31 \times 4.86\times10^{-4} = 0.248\ \mathrm{m},
\qquad
\frac{|{-0.70}|}{0.248} = 2.8\sigma.$$

**Interpretation.** The hidden-layer bias is $2.8$ standard errors — it is neither
negligible nor overwhelming, and it will **not** shrink with more picks at the
same offsets, because it is a model error rather than a random one. Only a
different measurement (★7) or an offset distribution reaching the near field can
reduce it, and the near field is precisely where the branch does not exist.

---

## ★★★7 — Removing the hidden-layer ambiguity

**The added method.** Multi-channel analysis of surface waves (MASW), or a
downhole seismic/CPT velocity log if a borehole is available.

**What it measures.** MASW measures the dispersion of Rayleigh waves: the
phase-velocity curve $c(f)$ over tens of hertz. Each frequency samples a depth
range of order a third to a half of its wavelength, so the inverted
$V_s(z)$ profile is sensitive to *every* layer, including one of intermediate
velocity, because dispersion depends on the whole profile rather than on first
arrivals only.

**Why it is sensitive where refractions are not.** First-arrival interpretation
can only use arrivals that are *fastest* at a given offset; a hidden layer is
never that. Dispersion uses the *whole* wavefield's frequency-dependent velocity,
which is monotonic in the profile's stiffness-contrast structure rather than in
its first-arrival ordering. A velocity inversion, which is invisible to
refraction, is a characteristic feature of dispersion curves and is routinely
inverted.

**Expected depth resolution.** For a 2 m layer at 2 m depth with
$V_s \approx 300$–$500\ \mathrm{m\,s^{-1}}$, the layer must be sampled by
wavelengths of 4–10 m, i.e. frequencies of roughly 30–80 Hz. A 24-channel spread
at 1 m spacing with a 5 kg sledgehammer source records usable dispersion to about
50–70 Hz, so resolving the 2 m layer to $\pm0.3\ \mathrm{m}$ is realistic; the
resolution limit is the highest usable frequency, not the inversion algorithm.

**Cost.** One extra acquisition pass over the same line — typically 15 to 30
minutes of field time with the same source and receivers — plus the dispersion
picking and inversion, which is the dominant analysis cost. Against a $2.8\sigma$
systematic error in a foundation depth, that is cheap.

**What it still does not give.** An absolute $V_s$ independent of the
$V_p$–$V_s$ assumption and the density model; the dispersion inversion has its own
non-uniqueness, and the honest report quotes the 1-D $V_s$ profile with its
resolution kernel rather than a single number.
