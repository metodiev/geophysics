# Solutions — 20-03-06 Multichannel and Array Filtering (f-k, Radon)

> **Read after attempting the exercises.** Lesson:
> [06 Multichannel and Array Filtering](../06-multichannel-filtering.md).

---

## ★1 — Apparent velocity

$$v_{\text{app}} = \frac{\Delta x}{p\,\Delta t} = \frac{50}{3 \times 0.001}
= 16666.7\ \mathrm{m\,s^{-1}}.$$

This is far above any real seismic velocity, so a 3 samples/trace dip on a 50 m
array is aliased for essentially all frequencies of interest — the array is too
coarsely spaced for that dip.

---

## ★2 — Spatial Nyquist

$$\left|f\,p\right| \le 0.5\ \text{cyc/trace}
\quad\Longleftrightarrow\quad
f \le \frac{0.5}{|p|}\ \text{cycles/sample}.$$

Equivalently, in physical units, $f\nu\Delta x$... the clean statement is: the
event aliases when the phase shift between adjacent traces exceeds $\pi$ radians,
i.e. $2\pi f p > \pi$.

---

## ★3 — Line, not blob

The 2-D transform of $w(n-pm)$ separates into $\hat w(f)$ (a function of
frequency only) times a delta in $(k+fp)$. The spatial dependence collapses
because the wavelet is *identical* on every trace except for a linear time shift,
whose transform is a pure phase ramp. A general 2-D event (one that changes shape
across traces, like a spherical wavefront) does not collapse and appears as a
spread blob.

---

## ★4 — Derivation

$$G(f,k) = \sum_n\sum_m w(n-pm)e^{-i2\pi(fn+km)}.$$

Substitute $u = n - pm$, so $n = u + pm$ and $fn = fu + fpm$:

$$G = \sum_m e^{-i2\pi\big(fpm + km\big)}\sum_u w(u)e^{-i2\pi fu}
= \hat w(f)\sum_m e^{-i2\pi(fp+k)m}
= \hat w(f)\,\delta(k+fp).$$

With a **finite-bandwidth** wavelet, $\hat w(f)$ is nonzero over a band, so each
frequency row of $|G|$ has a peak at $k = -fp$ with width set by the *aperture*:
the delta in $k$ is replaced by $\mathrm{Dirichlet}$-like sidelobes of width
$\sim1/N_x$. This is why finite-aperture events leak into a fan filter (the demo's
14.7% at the narrowest fan) and why a longer array rejects better.

---

## ★5 — Choosing a fan half-width

The retention requirement of 98% is met at $h = 0.047$ (98.3%) and at $h = 0.0625$
(98.7%); it is *not* met at $h = 0.031$ (97.5%) or below. Choose the smaller of the
two that meets the requirement: **$h = 0.047$ cyc/trace**, with leakage 32.05%
(rejection $-9.9$ dB). Choosing $h = 0.0625$ buys 0.4% more retention for 5
percentage points more leakage — a poor trade. Note also that the leakage is
already 15–20% at the narrowest fans, so the requirement "retain 98%" implicitly
accepts substantial contamination; state both numbers.

---

## ★6 — Aliased event retained at 94.9%

The event has true $k = -fp = -0.160 \times 8.25 = -1.320$ cyc/trace, well beyond
the spatial Nyquist of $0.5$. The 2-D DFT samples wavenumber on a grid of spacing
$1/N_x = 0.0156$; a true wavenumber $k$ is indistinguishable from
$k \bmod 1$ wrapped into $[-0.5,0.5)$. Here

$$-1.320 + 1.0 = -0.320 \quad\Longleftrightarrow\quad \text{apparent }
p = \frac{0.320}{0.160} = +2.000\ \text{samples/trace},$$

exactly the signal dip. The fan centred on $+2$ therefore passes it. The filter
cannot distinguish a true dip from an aliased one, because after sampling they are
the *same numbers*.

Acquisition change: reduce the trace spacing until the largest dip of interest is
unaliased. Aliasing requires $|fp| \le 0.5$ cyc/trace, i.e.
$p \le 0.5/f = 0.5/0.160 = 3.125$ samples/trace. A dip of 8.25 samples/trace needs
the sample interval in *space* reduced by $8.25/3.125 = 2.64$, i.e. $\Delta x$
reduced from 25 m to about 9.5 m. Alternatively, accept the aliasing and remove the
steep event before stacking using a method that uses its full moveout (a Radon
transform with a large $p$ range, or an f-k filter applied to the *unaliased*
low-frequency part and extrapolated).

---

## ★★★7 — When f-k cannot separate two events

Take two events with the **same** slowness, $p_1 = p_2 = 2$ samples/trace, at
different zero-offset times. Their f-k loci are the *same line* $k = -2f$; the
filter has no way to distinguish them, and any mask that passes one passes the
other. This is the fundamental limit: f-k separates by dip, and both events have
the same dip.

A $\tau$–$p$ (linear Radon) transform also collapses both events to points on the
same $p$ row but at different $\tau$ values. Because the transform output is
two-dimensional in $(p,\tau)$, the two events occupy *different* $\tau$ cells, so
a mask in $(p,\tau)$ **can** separate them: zero one $\tau$ cell and keep the
other. The transform therefore succeeds where f-k fails, though it introduces
$p$-axis smearing (the transform's limited aperture) as a new artifact, and the
separation requires the events to be genuinely distinct in intercept time.

The general statement: f-k separates by dip; Radon separates by dip *and*
intercept time. Neither can separate events that coincide in both.

---

## ★★★8 — Sample-spacing condition

Let $s$ be the **physical** slowness in s/m, $\nu$ the physical frequency in Hz,
$\Delta x$ the trace spacing and $\Delta t$ the sample interval. Then

$$f = \nu\,\Delta t\ \text{(cycles/sample)},\qquad
p = \frac{s\,\Delta x}{\Delta t}\ \text{(samples/trace)},$$

and the aliasing condition $|f p| \le 0.5$ becomes

$$\left|\nu\,\Delta t \cdot \frac{s\,\Delta x}{\Delta t}\right|
= \left|\nu\,s\,\Delta x\right| \le 0.5.$$

The sample interval cancels, leaving the clean acquisition rule

$$\boxed{\;\Delta x \le \frac{1}{2\,\nu_{\max}\,s_{\max}}.\;}$$

**Application.** A 25 Hz signal with dips up to 10 samples/trace on a 25 m array
at $\Delta t = 4$ ms corresponds to a physical slowness

$$s_{\max} = \frac{p\,\Delta t}{\Delta x} = \frac{10 \times 0.004}{25}
= 1.6\times10^{-3}\ \mathrm{s\,m^{-1}} \quad(625\ \mathrm{m\,s^{-1}}).$$

The required spacing is

$$\Delta x \le \frac{1}{2 \times 25 \times 1.6\times10^{-3}} = \frac{1}{0.08}
= 12.5\ \mathrm{m}.$$

**A 25 m spacing must be halved to 12.5 m** to record 25 Hz energy at up to
10 samples/trace without aliasing. Note that $\Delta t$ does not appear in the
final rule: temporal sampling sets the frequency band, spatial sampling sets the
dip band, and the two are independent constraints on array design.