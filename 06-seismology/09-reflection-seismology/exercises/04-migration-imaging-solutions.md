# Solutions — 06-09-04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [04 Migration and Imaging](../04-migration-imaging.md).

---

## ★1 — Diffraction times

Apex ($x=0$):

$$t_{\text{apex}} = \frac{2z_0}{v} = \frac{2\times1000}{2500}
= 0.800000\ \mathrm{s}.$$

At $x = 500\ \mathrm{m}$:

$$t(x) = \frac{2\sqrt{x^{2}+z_0^{2}}}{v}
= \frac{2\sqrt{500^{2}+1000^{2}}}{2500}
= \frac{2\times1118.034}{2500} = 0.894427\ \mathrm{s}.$$

So the hyperbola rises from $0.800\ \mathrm{s}$ at the apex to
$0.894\ \mathrm{s}$ only $500\ \mathrm{m}$ away: at this velocity the diffraction
tail is steep, and a migration aperture of a few hundred metres captures most of
it.

---

## ★2 — Apex time of the demonstration's diffractor

$$t_{\text{apex}} = \frac{2z_0}{v} = \frac{2\times800}{2000}
= 0.800000\ \mathrm{s},$$

printed as $0.8000\ \mathrm{s}$. **Unit bookkeeping:**
$[z]/[v] = \mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$, and the factor $2$ is
the down-and-up path. The coincidence that both exercises give $0.800\ \mathrm{s}$
is arithmetic (different $z_0$ and $v$), not physics.

---

## ★3 — Why two images add without interference

The diffraction sum is a **linear** operator: for data $d = d_1 + d_2$ it returns
$I = I_1 + I_2$. Each diffractor's energy lies on its own travel-time curve
$t_i(x) = 2\sqrt{(x-x_i)^{2}+z_i^{2}}/v$, and summing along the *wrong* curve
$t_1$ of data belonging to diffractor 2 does not vanish — it gives a small,
migrated-artefact contribution. So the images add "without interference" in the
sense that they never *cancel*: the cross-term

$$\text{cross} = \sum_x d_2\big(x, t_1(x)\big)$$

is generally non-zero but small, and it appears as a weak smile artefact.

**When they would interfere:** if the two diffractors have the same apex time and
are closer than the Fresnel radius (lesson 07), their hyperbolae overlap within
one wavelet and the migrated image is a single composite anomaly whose amplitude
is a sum — the same non-uniqueness as the thin-bed tuning problem. Interference
in the strict sense (destructive) requires coherent superposition with opposite
polarity, which happens for two reflectors of opposite sign within a
half-wavelength.

---

## ★4 — Velocity ratio that halves the amplitude

Interpolate in $\log_{10}(v_{\text{mig}}/v_{\text{true}})$, which is the natural
variable for a ratio.

**Low side** ($28.1\%$ at $0.95$, $100\%$ at $1.00$):

$$\text{fraction} = \frac{50-28.1}{100-28.1} = 0.304, \qquad
\log_{10}r = \log_{10}0.95 + 0.304(\log_{10}1.00-\log_{10}0.95)
= -0.02228 + 0.304\times0.02228 = -0.01551,$$
$$r = 10^{-0.01551} = 0.965 .$$

**High side** ($100\%$ at $1.00$, $32.0\%$ at $1.05$):

$$\text{fraction} = \frac{100-50}{100-32.0} = 0.735, \qquad
\log_{10}r = 0 + 0.735\times\log_{10}1.05 = 0.735\times0.02119 = 0.01558,$$
$$r = 10^{0.01558} = 1.037 .$$

So the focus falls to half at roughly $v_{\text{mig}} = 0.965\,v_{\text{true}}$
and $1.037\,v_{\text{true}}$: an asymmetric window of about
$-3.5\%$/$+3.7\%$. The asymmetry is real (the smile/frown residuals differ) and
is why a focus scan is quoted with both bounds.

---

## ★5 — Depth error versus velocity ratio

| $v_{\text{mig}}/v_{\text{true}}$ | peak depth (m) | error (m) | error (%) |
|---|---|---|---|
| 0.80 | 780 | $-20$ | $-2.5\%$ |
| 0.90 | 760 | $-40$ | $-5.0\%$ |
| 0.95 | 780 | $-20$ | $-2.5\%$ |
| 1.00 | 800 | $0$ | $0.0\%$ |
| 1.05 | 820 | $+20$ | $+2.5\%$ |
| 1.10 | 800 | $0$ | $0.0\%$ |
| 1.20 | 680 | $-120$ | $-15.0\%$ |

The migration grid has $71$ depth cells over the model; the grid spacing sets a
quantisation of the peak position, and the peak is picked as the *maximum
amplitude*, not as a centroid. To within that quantisation, the ratios $0.95$,
$1.00$ and $1.10$ all put the peak at $780$-$800\ \mathrm{m}$, i.e. within
$\pm20\ \mathrm{m} = \pm2.5\%$ of the true depth. Reading the table as a
velocity estimator: **depths alone are a weak velocity criterion near the correct
value** (three ratios give nearly the same depth), whereas the *amplitude* column
of the demonstration varies by a factor of $3$ over the same range — which is why
focus (amplitude) and not position is the standard velocity criterion.

---

## ★6 — Migration-velocity scan to 5% (specification)

**Trial velocities.** To recover a ratio to $5\%$ the scan must sample finer than
the target, e.g. $2\%$ steps over $\pm20\%$:

$$r \in \{0.84, 0.86, \dots, 1.16\}, \qquad \text{16 trials}.$$

**Cost per trial.** The diffraction sum evaluates, for every image cell, a
summation over traces:

$$\text{operations per trial} \approx N_x^{\text{image}} \times N_z^{\text{image}}
\times N_{\text{traces}}
= 81 \times 71 \times 121 = 695\,871 \approx 7.0\times10^{5}.$$

**Total cost.** $16 \times 7.0\times10^{5} = 1.1\times10^{7}$ interpolation-and-add
operations — trivial for one point diffractor, and the reason the demonstration
runs in a few seconds. For a real 3-D survey the same recipe is prohibitive by
four or five orders of magnitude, which is the practical reason RTM and
beam/scanning methods are used instead of brute-force Kirchhoff scans.

**Stopping criterion.** Stop when the half-amplitude window of ★4 is narrowed to
the target: with a $2\%$ sampling, quote the curvature of the amplitude versus
ratio and stop when the parabola's half-width is $<5\%$, or when the
amplitude-versus-ratio curve becomes noise-limited (the amplitude scatter between
neighbouring trials is comparable to the trend).

---

## ★7 — Expected depth shift from a velocity error

For a constant-velocity Kirchhoff map the image depth is obtained by evaluating
the diffraction curve with the *migration* velocity:

$$t = \frac{2\sqrt{(x-x_m)^{2}+z^{2}}}{v_{\text{mig}}}.$$

A point at depth $z_0$ whose true data lie on $t = 2\sqrt{x^{2}+z_0^{2}}/v_{\text{true}}$
is imaged where the two curves cross at $x = 0$:

$$\frac{2z_0}{v_{\text{true}}} = \frac{2z_{\text{imaged}}}{v_{\text{mig}}}
\;\Longrightarrow\;
z_{\text{imaged}} = z_0\frac{v_{\text{mig}}}{v_{\text{true}}}
= z_0(1+\epsilon).$$

So the **naive prediction** for $\epsilon = +0.20$ is
$z_{\text{imaged}} = 800\times1.20 = 960\ \mathrm{m}$, i.e. $+160$ m *deeper*.

The measurement is $-120\ \mathrm{m}$ (shallower at the *largest* error
$1.20$). The difference has two parts:

1. The naive formula holds for the apex trace; the demonstration picks the
   **maximum-magnitude** cell of the migrated image, and with an incorrect
   velocity the energy is defocused and the maximum wanders laterally as well as
   in depth (the measured peak $x$ is $+380\ \mathrm{m}$ at $1.20$, far from the
   true $0$). A defocused maximum is not the apex, so the naive mapping does not
   apply.
2. The migration grid is coarse ($71$ depths over the model, so of the order of
   $10\ \mathrm{m}$ to $20\ \mathrm{m}$ per cell, with the peak quantised to
   that grid), and at large velocity error the true apex region is no longer the
   brightest.

**The lesson to state:** for small errors the apex mapping
$z_{\text{imaged}} = z_0(1+\epsilon)$ is the right estimate and the demonstration
follows it at $0.95$/$1.00$/$1.05$ ($-20$, $0$, $+20$ m for $\mp5\%$); at large
errors the focus criterion breaks down and the peak position is no longer a
reliable datum.
