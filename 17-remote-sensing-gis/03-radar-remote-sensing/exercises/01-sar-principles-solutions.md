# Solutions — 17-03-01 SAR Principles: Geometry, Polarisation, Backscatter

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [01 SAR Principles](../01-sar-principles.md).

---

## ★1 — Range resolution and its ground projection

Slant range:
$$\Delta r = \frac{c}{2B} = \frac{299\,792\,458}{2 \times 60\times10^{6}}
= 2.4983\ \mathrm{m} \approx 2.50\ \mathrm{m}.$$

Ground range, using the flat local surface assumption
($\mathrm{d}g = \mathrm{d}r/\sin\theta$):
$$\Delta g = \frac{2.4983}{\sin 30^\circ} = \frac{2.4983}{0.5}
= 4.9965\ \mathrm{m} \approx 5.00\ \mathrm{m}.$$

**Assumption:** the facet is locally flat and its local incidence angle equals
the look angle $\theta$; the projection is $\sin\theta$ only under that
assumption. On a slope the local incidence changes and with it the projection.

---

## ★2 — Real versus synthetic azimuth resolution

Real aperture:
$$\delta_{\text{real}} = \frac{\lambda R}{L}
= \frac{0.03123 \times 7.0\times10^{5}}{4.0} = 5465.3\ \mathrm{m}.$$

Synthetic aperture:
$$\delta_{\text{syn}} = \frac{L}{2} = 2.00\ \mathrm{m}
\qquad(\text{measured}\ -3\ \mathrm{dB\ width}\ 0.886\times2.00 = 1.77\ \mathrm{m}).$$

**Which depends on range:** only the real-aperture value does, through
$\lambda R/L$; the synthetic resolution is set by $L$ alone because the
illumination time grows in proportion to $R$, so the Doppler bandwidth
$2v/L$ — and hence the compressed width — is range-independent.

---

## ★3 — Cross section of a resolution cell

$$\sigma^{0} = -10\ \mathrm{dB} \Rightarrow \sigma^{0} = 10^{-1.0} = 0.1000.$$
$$A_{\text{cell}} = 4.0 \times 5.0 = 20.0\ \mathrm{m^{2}}, \qquad
\sigma = 0.1000 \times 20.0 = 2.00\ \mathrm{m^{2}},$$
$$\sigma_{\text{dB}} = 10\log_{10} 2.00 = +3.01\ \mathrm{dB\,m^{2}}.$$

**Why $\sigma^{0}$ is preferred:** the echo of a *cell* scales with the cell
area, which the user changes whenever the resolution or the incidence angle
changes. Dividing by the area removes that dependence and leaves a quantity
that can be compared between images with different pixels and geometries. The
absolute cross section $\sigma$ is still the right quantity for a point target
such as a corner reflector.

---

## ★4 — The PRF window

Azimuth-ambiguity bound:
$$f_{\text{PRF}} > B_d = \frac{2v}{L} = \frac{2 \times 7500}{4}
= 3750\ \mathrm{Hz}.$$

Range-ambiguity (swath) bound:
$$f_{\text{PRF}} < \frac{c}{2W} = \frac{299\,792\,458}{2 \times 60\,000}
= 2498.3\ \mathrm{Hz}.$$

The window is empty: $3750 > 2498.3$, so **no PRF works** for this combination.
The conflict is closed when the two bounds meet:
$$\frac{2v}{L} = \frac{c}{2W} \Rightarrow L_{\min} = \frac{4vW}{c}
= \frac{4 \times 7500 \times 6.0\times10^{4}}{2.99792458\times10^{8}}
= 6.00\ \mathrm{m}.$$

**Interpretation:** $L \ge 6.00\ \mathrm{m}$ opens the window. This inequality
is the fundamental swath-versus-azimuth-resolution trade of a strip-map SAR; it
is why wide-swath systems use a *longer* azimuth antenna (coarser resolution)
or several azimuth channels, and why "fine resolution and wide swath at the same
time" is a design problem rather than a processing problem.

---

## ★5 — SNR scaling

**(a)** $P_r \propto R^{-4}$, so doubling $R$ multiplies $P_r$ by
$2^{-4} = 1/16$:
$$10\log_{10}(1/16) = -12.04\ \mathrm{dB}.$$

**(b)** Doubling $P_t$ gives $+3.01\ \mathrm{dB}$; the net change is
$$+3.01 - 12.04 = -9.03\ \mathrm{dB},$$
i.e. the compressed SNR becomes $0.892 \times 10^{-0.903}
= 0.892 \times 0.125 = 0.1115$.

**(c)** SNR is linear in $\sigma$:
$$0.892 \times 5 = 4.46 \quad (+6.5\ \mathrm{dB}).$$

Note that (c) is the cheap way to win: a five-fold larger cross section buys as
much as a five-fold power increase, and a real corner reflector is cheaper than
a bigger transmitter.

---

## ★6 — Foreshortening, layover, shadow

Thresholds at $\theta = 35^\circ$: **layover** for a facet facing the radar when
$\alpha > \theta = 35^\circ$; **shadow** for a facet facing away when
$\alpha > 90^\circ - 35^\circ = 55^\circ$. Between the thresholds a facing facet
is foreshortened but invertible.

| facet | $\alpha$ | local incidence | verdict | foreshortening factor $\sin(\theta-\alpha)/\sin\theta$ |
|---|---|---|---|---|
| facing, $50^\circ$ | $50^\circ$ | $-15^\circ$ | **layover** ($50 > 35$) | $|\sin(-15^\circ)|/\sin 35^\circ = 0.451$ (magnitude only: the ordering has already folded) |
| facing, $30^\circ$ | $30^\circ$ | $+5^\circ$ | foreshortened, invertible | $\sin 5^\circ/\sin 35^\circ = 0.152$ |
| away, $60^\circ$ | $60^\circ$ | $95^\circ$ | **shadow** ($60 > 55$) | undefined: no illumination |

The $30^\circ$ row is the honest middle case: the facet is compressed to $15\%$
of its ground extent — severe foreshortening — yet the slant-range ordering is
still monotonic and the slope can be reconstructed from the geometry. Only when
$\theta-\alpha$ changes sign does the ordering fold, and only then does the
geometry stop being invertible. "Foreshortened" and "in layover" are therefore
not synonyms, and a strong compression is not by itself a reason to discard a
measurement.

Check with the fold condition $\mathrm{d}r/\mathrm{d}s = 0$: it requires
$\tan\alpha = \tan\theta$, so the onset is exactly $\alpha = \theta$ — which the
lesson's demonstration reproduces numerically to the $0.1^\circ$ scan step.

---

## ★7 — Separating speckle from additive noise (specification)

**Statistic.** The normalised intensity moments of a homogeneous region,
$\hat{m}_k = \langle I^{k}\rangle/\langle I\rangle^{k}$, plus the intensity
probability density compared against two models.

**Models.** (i) Fully developed speckle from a scene of many independent
scatterers: $I$ is exponentially distributed, so $m_2 = 2$, $m_3 = 6$,
$m_4 = 24$ and the normalised variance is $1$. (ii) Additive complex Gaussian
receiver noise *added to* a weaker speckle signal: $I = I_s + I_n$ with two
independent exponential/ $\chi^{2}$ contributions, which raises the normalised
variance above $1$ and changes the small-intensity tail.

**Expectation.** If only speckle is present, the histogram of $I/\langle I\rangle$
in a homogeneous region collapses onto a single exponential curve for every
polarisation and every look count, and $\hat{m}_2 \to 2$ as the region grows.
If additive noise contributes, the histogram at low intensity is *flatter* than
exponential (the noise floor), the second moment exceeds 2, and — decisively —
the excess grows when the region is chosen where the scene is dark, and shrinks
where it is bright. Speckle alone cannot produce a signal-dependent excess.

**Reporting.** Report, per region and per look count: the estimated
$\hat{m}_2$ with its uncertainty, the fraction of variance attributable to the
noise floor by fitting the two-component model, and the SNR below which the
distinction is not significant. State the region, its size in resolution cells,
and the radiometric calibration used.

---

## ★8 — Where 0.886 comes from, and what a taper changes

For an unweighted (rectangular) aperture of duration $T_s$ the compressed
response is $\operatorname{sinc}$: with the chirp rate $K_a$ and $B_d = K_aT_s$,
the amplitude is
$$\left|\operatorname{sinc}\!\left(\frac{B_d\,\delta t}{1}\right)\right|
= \left|\frac{\sin(\pi B_d\,\delta t)}{\pi B_d\,\delta t}\right|^{-1}\text{-normalised},$$
whose half-power points satisfy $\operatorname{sinc}(u) = 1/\sqrt{2}$, i.e.
$u = 0.4429$. The full width at half power is therefore
$$2 \times 0.4429 = 0.8858 \approx 0.886 \quad \text{in units of } 1/B_d,$$
and in platform position that is $0.886\,v/B_d = 0.886\,L/2$.

**Raised-cosine (Hann-type) taper:**

| quantity | change | direction |
|---|---|---|
| mainlobe width | broadens by about $1.30$–$1.44\times$ | **degrades** |
| peak sidelobe level | falls from $-13.3\ \mathrm{dB}$ to below $-30\ \mathrm{dB}$ | **improves** |
| integrated sidelobe ratio | falls (less energy in the sidelobes) | **improves** |
| SNR / peak response | falls, because the taper down-weights the aperture ends | **degrades** |

A system accepts the taper when the science target is a weak feature next to a
strong one — an ice sheet edge beside an ocean, or a small deformation signal
adjacent to a strong scatterer — because the sidelobe floor, not the mainlobe
width, sets the contrast that can be detected. It rejects the taper when the
target is homogeneous and the best possible resolution and SNR are wanted. The
choice is a statement about the target, not a numerical preference.
