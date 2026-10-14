---
id: 20-03-06
title: "Multichannel and Array Filtering (f-k, Radon)"
level: research
prereqs: ["20-03-03", "20-02-01"]
tags: [signal-processing, filtering, f-k, radon, array-processing, dip-filter, spatial-aliasing, multichannel]
---

# Multichannel and Array Filtering (f-k, Radon)

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the two-dimensional Fourier transform of a linear event and **show**
   that its energy lies on the line $k = -fp$.
2. **Design** an f-k fan filter for a stated apparent slowness and **measure** its
   pass and reject performance on synthetic events.
3. **State** the spatial Nyquist condition and **compute** the dip at which a given
   frequency aliases.
4. **Explain** how spatial aliasing lets a steep event masquerade as the signal
   dip, and **quantify** the leakage.
5. **Relate** the linear Radon ($\tau$–$p$) transform to the f-k transformation and
   **state** what each one is better at.
6. **Choose** a fan half-width from a stated separation requirement.

## Prerequisites

- [20-03-03 Filter Selection for Geophysical Data](03-filter-applications.md) —
  the single-channel filtering this lesson generalises to arrays.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the transform used along the time axis.

## 1. Intuition: the second dimension is the separation

A single trace cannot separate two events that arrive at the same time. An array
can, because a wave crossing the array at a different angle arrives at different
traces at different times. The extra dimension is not more of the same data; it is
a *new discriminator*. Ground roll and a reflection can overlap completely in
frequency and still be separated if their apparent slownesses differ, which is
exactly what array acquisition buys.

The cost is a new sampling theorem. Just as time sampling limits frequency, space
sampling limits wavenumber, and an event too steep for the trace spacing aliases
into an apparent dip that may be the signal's own. The demo's central result is
that an event with dip 8.25 samples/trace — well beyond the spatial Nyquist —
passes a filter designed to reject it with **94.9%** of its energy intact, because
it aliases onto exactly the signal dip.

All models and data in this module are SYNTHETIC. The gather geometry (64
traces, 25 m spacing, 4 ms sampling) is a chosen teaching geometry.

## 2. Definitions

### 2.1 The two-dimensional spectrum

For a gather $g[n,m]$ with $n$ the time index and $m$ the trace index, define

$$G(f,k) = \sum_{n}\sum_{m} g[n,m]\,e^{-i2\pi(fn + km)},$$

with $f$ in cycles/sample and $k$ in cycles/trace. The physical wavenumber is
$\kappa = k/\Delta x$ and the physical frequency is $\nu = f/\Delta t$; the
**apparent slowness** is

$$p = \frac{k}{f}\ \text{(samples/trace)} \quad\text{or}\quad
\frac{\kappa}{\nu} = \frac{k}{f}\frac{\Delta t}{\Delta x}\ \ (\mathrm{s/m}).$$

### 2.2 Apparent velocity

The apparent horizontal velocity of a linear event with slowness $p$ samples/trace
is

$$v_{\text{app}} = \frac{\Delta x}{p\,\Delta t}.$$

For the demo's geometry ($\Delta x = 25$ m, $\Delta t = 4$ ms), $p = 2$ gives
$v_{\text{app}} = 25/(2\times0.004) = 3125$ m s$^{-1}$, and $p = -4$ gives
$1562$ m s$^{-1}$ in the opposite direction.

### 2.3 Spatial Nyquist

The wavenumber samples only $|k| \le 0.5$ cyc/trace. An event with slowness $p$ at
frequency $f$ has $|k| = |f p|$, so it is **aliased** whenever

$$\left|f p\right| > 0.5 \quad\Longleftrightarrow\quad
f > \frac{0.5}{|p|}.$$

## 3. Derivations

### 3.1 A linear event is a line in the f-k plane

Let the event be $g[n,m] = w(n - pm)$ for a wavelet $w$. Its 2-D transform is

$$G(f,k) = \sum_n\sum_m w(n-pm)e^{-i2\pi(fn+km)}.$$

Substitute $u = n - pm$ and sum over $n$ first:

$$G(f,k) = \hat{w}(f)\sum_m e^{-i2\pi(fpm + km)}
= \hat w(f)\,\delta\!\left(k + fp\right).$$

So **every linear event collapses onto the line $k = -fp$**, with amplitude given by
the wavelet spectrum $\hat w(f)$ evaluated at the temporal frequency only. This is
the entire basis of f-k filtering: separating events is separating lines through
the origin.

The demo verifies the locus numerically. The strongest peak of $|G|$ at
$f = 0.051, 0.078, 0.102, 0.121$ cycles/sample sits at $k$ values that imply
$p = -4.000$ samples/trace at every frequency — the dip of the dominant (noise)
event, recovered to three decimals.

### 3.2 The fan filter

A fan filter multiplies $G(f,k)$ by a mask that passes a band of slownesses around
the signal dip $p_{\text{sig}}$ and rejects the rest:

$$M(f,k) = \begin{cases}
1, & \left|k + f p_{\text{sig}}\right| \le h \\
\text{taper}, & h < \left|k + f p_{\text{sig}}\right| < h + h_t \\
0, & \text{otherwise,}
\end{cases}$$

where $h$ is the half-width in cycles/trace. The demo uses a raised-cosine taper
of width $h_t = h/2$ to suppress Gibbs ringing at the mask edge. Note that the
mask is naturally symmetric under $(f,k)\to(-f,-k)$, so the output is real.

A fan filter is a **linear** operation and, because it cannot create energy,
conserves the total; it only moves and removes. What it cannot do is separate two
events whose f-k lines cross — a genuine ambiguity, not an algorithmic limitation.

### 3.3 The Radon transform

The linear Radon (slant-stack, $\tau$–$p$) transform sums along lines of constant
slowness:

$$u(p,\tau) = \sum_m g\!\left[\tau + p\,m,\ m\right],$$

i.e. it collapses each linear event to a point rather than to a line through the
origin. Its advantage over f-k is that it is not restricted to events through the
origin (hyperbolic and curved events map to compact blobs), and it makes
interference *isolation* easy: zero a region in $(p,\tau)$ and invert. Its
disadvantage is a transform artefact (smearing along the $\tau$ axis) and its cost,
which is $O(N_\tau N_p N_x)$ rather than $O(N\log N)$. The two are related by a
2-D Fourier transform in disguise; the demo uses f-k because the events are linear
and because the f-k picture makes the aliasing argument exact.

## 4. The measurement

### 4.1 Pass and reject versus fan width

Each event is filtered on its own, so retention and leakage are measured directly
as RMS-amplitude ratios:

| half-width (cyc/trace) | grid cells | signal retained | noise leaked | rejection (dB) |
|---|---|---|---|---|
| 0.0080 | 0.5 | 94.9% | 14.69% | $-16.7$ |
| 0.0160 | 1.0 | 94.9% | 19.68% | $-14.1$ |
| 0.0230 | 1.5 | 97.3% | 22.20% | $-13.1$ |
| 0.0310 | 2.0 | 97.5% | 26.20% | $-11.6$ |
| 0.0470 | 3.0 | 98.3% | 32.05% | $-9.9$ |
| 0.0625 | 4.0 | 98.7% | 37.13% | $-8.6$ |

Two features are worth explaining rather than glossing over. First, even the
narrowest fan retains 94.9% of the signal: the fan is never narrower than the
event's own spectral width, and a finite-aperture event is not a pure line.
Second, the leakage of the noise event is **14.7% even at the narrowest fan**,
because a finite aperture broadens every event into a band of wavenumbers around
$k = -fp$, and part of that band always falls inside the fan. **The rejection
ceiling is set by the aperture, not by the mask.** A longer array would sharpen
it.

Applied to the summed gather with $h = 0.023$ cyc/trace, the filtered gather has
RMS $0.0964$ against the ideal signal event's $0.0987$, and the residual (filtered
minus ideal) has RMS $0.399$ of the noise event's — the leaked tail plus transform
edge effects, since the gather is not periodic in space.

### 4.2 Spatial aliasing, quantified

A continuous 40 Hz event on this geometry has $f = 40 \times 0.004 = 0.160$
cycles/sample. Aliasing starts when $|fp| > 0.5$, i.e. $p > 3.125$ samples/trace.
The 2-D spectrum wraps true wavenumbers into $[-0.5, 0.5)$:

| true $p$ (samples/trace) | true $k$ | aliased $k$ | apparent $p$ | retained by the $+2$ fan |
|---|---|---|---|---|
| 2.00 | $-0.320$ | $-0.320$ | $+2.000$ | 94.9% |
| 5.00 | $-0.800$ | $+0.200$ | $-1.250$ | 1.8% |
| 8.25 | $-1.320$ | $-0.320$ | $+2.000$ | **94.9%** |
| 12.00 | $-1.920$ | $+0.080$ | $-0.500$ | 1.2% |

The $p = 8.25$ event is aliased — it is 2.6 times past the spatial Nyquist — and yet
it is retained as strongly as the genuine signal, because its aliased wavenumber
equals the signal's exactly. The $p = 5$ and $p = 12$ events alias to different
apparent dips and are rejected. **An f-k filter cannot tell a true dip from an
aliased one; only a finer spatial sampling can.** This is why field acquisition
design is a filtering decision made before any data exist.

## 5. Worked example (SYNTHETIC)

A 96-trace shot gather, $\Delta x = 20$ m, $\Delta t = 2$ ms, carries a 30 Hz
reflection at $p = +1.5$ samples/trace and ground roll at $p = -6$ samples/trace.

1. **Apparent velocities**: reflection
   $v = 20/(1.5 \times 0.002) = 6667$ m s$^{-1}$; ground roll
   $v = -20/(6\times0.002) = -1667$ m s$^{-1}$ (up-dip in the gather sense).
2. **Grid**: $f = 30 \times 0.002 = 0.060$ cycles/sample; $k$ grid spacing
   $1/96 = 0.0104$ cyc/trace.
3. **Fan**: choose half-width $h = 2$ grid cells $= 0.021$ cyc/trace. The
   reflection sits at $k = -0.090$; the ground roll at $k = +0.36$.
4. **Aliasing check**: ground roll aliases when $f > 0.5/6 = 0.083$ cyc/sample
   $= 41.7$ Hz. At 30 Hz it is *not* aliased, so the fan separates it cleanly.
5. **Separation margin**: the two events are $|0.36 - (-0.09)| = 0.45$ cyc/trace
   apart, more than twenty times the fan width, so leakage is limited by the
   aperture, not by the fan.

Change any one number and the conclusion can flip. If the ground-roll dip were 12
samples/trace instead of 6, it would alias above $0.5/12 = 0.0417$ cyc/sample
$= 20.8$ Hz, so at 30 Hz it would appear at an apparent dip of
$-0.36$ — right on top of the reflection — and the fan would pass it.

## 6. Assumptions and regime of validity

1. **Events are linear (or nearly so) within the window.** f-k filtering assumes
   the dip is constant over the analysis window; a curved event smears in f-k and
   needs a windowed or Radon treatment.
2. **The gather is uniformly sampled in space.** Non-uniform trace spacing breaks
   the wavenumber axis and turns the fan into an approximate operator; interpolate
   first.
3. **The events are not aliased.** The load-bearing assumption. §4.2 shows a
   counter-example; the defence is acquisition design, not processing.
4. **The array is long enough.** Rejection is limited by aperture (14.7% leakage
   here at the narrowest fan).
5. **Source and receiver geometry are static.** A moving source or changing
   geometry changes $p$ within the window.
6. **The 2-D transform is treated as if the gather were periodic.** It is not, so
   edge effects appear. Tapering the gather in space and time before transforming
   reduces them.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| temporal frequency | $f$ | cycles/sample | $\nu\Delta t$ |
| wavenumber | $k$ | cycles/trace | $\kappa\Delta x$ |
| slowness | $p$ | samples/trace | $k/f$ |
| slowness | — | s/m | $k\Delta t/(f\Delta x)$ |
| apparent velocity | $v_{\text{app}}$ | m s$^{-1}$ | $\Delta x/(p\Delta t)$ |
| fan half-width | $h$ | cycles/trace | $\ge 1/N_x$ |

The most common unit error is mixing samples/trace with s/m. They differ by
$\Delta t/\Delta x$; at the demo's geometry that factor is
$0.004/25 = 1.6\times10^{-4}$ s m$^{-1}$ per (sample/trace), enough to make a
plausible-looking dip wrong by orders of magnitude.

## 8. Python demonstration

`code/multichannel_filtering_demo.py` builds a two-event gather, computes its 2-D
spectrum and recovers the event dips, designs a fan filter, measures retention and
leakage versus fan width, and demonstrates the aliasing of a steep event onto the
signal dip. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 2** — the spectral peak implies $p = -4.000$ at every frequency.
2. **section 3** — leakage grows monotonically with fan width; rejection falls
   from $-16.7$ to $-8.6$ dB.
3. **section 4** — the residual is dominated by the aperture-limited leakage.
4. **section 5** — $p = 8.25$ is retained at 94.9% because it aliases to $+2$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/06-multichannel-filtering-exercises.md`](exercises/06-multichannel-filtering-exercises.md)
and
[`exercises/06-multichannel-filtering-solutions.md`](exercises/06-multichannel-filtering-solutions.md).

- **★** Compute the apparent velocity of an event with $p = 3$ samples/trace at
  $\Delta x = 50$ m and $\Delta t = 1$ ms.
- **★★** Derive the locus $k = -fp$ and state what happens to a wavelet with a
  finite bandwidth.
- **★★** Given the aliasing table, choose the trace spacing that would un-alias
  an event with $p = 12$ samples/trace at 40 Hz.
- **★★★** Explain why a Radon transform can separate an event that f-k filtering
  cannot, and construct a synthetic case where it succeeds.

## Mastery checkpoint

Complete this without notes:

> A 128-trace gather has $\Delta x = 15$ m and $\Delta t = 1$ ms. A reflection
> arrives at $p = +1$ sample/trace and a shear wave at $p = -10$ samples/trace,
> both at 35 Hz. **(a)** Compute both apparent velocities. **(b)** Compute both
> wavenumbers in cycles/trace. **(c)** State whether the shear event is spatially
> aliased at 35 Hz and, if so, its apparent dip. **(d)** Choose a fan half-width
> that passes the reflection and state the resulting leakage scale. **(e)** State
> the acquisition change that would make the separation reliable.

A worked version appears in the
[solutions](exercises/06-multichannel-filtering-solutions.md).

## Common pitfalls

1. **Trusting a fan filter on aliased data.** The aliased event's retained energy
   is 94.9% — the filter looks successful while passing the wrong thing.
2. **Choosing the fan by taste.** State the separation requirement and the grid
   spacing, then set $h$ in grid cells.
3. **Ignoring edge effects.** The gather is not periodic; taper it in space and
   time before transforming.
4. **Confusing samples/trace with s/m.** The conversion factor is
   $\Delta t/\Delta x$.
5. **Applying f-k filtering trace-by-trace or after stacking.** Both destroy the
   spatial information that makes the method work.

## Related modules

- [20-06-02 Beamforming, Slowness Estimation and f-k Analysis](../06-polarisation-and-array-processing/02-beamforming.md) —
  the estimation counterpart of the filtering done here.
- [20-03-03 Filter Selection for Geophysical Data](03-filter-applications.md) —
  the single-channel case.
- [20-03-05 Adaptive Filtering and Noise Cancellation](05-adaptive-filtering.md) —
  the data-driven alternative when the dips overlap.
- [20-04-04 Deconvolution in the Presence of Noise](../04-deconvolution-and-inverse-filtering/04-deconvolution-noise.md) —
  what the noise left in a gather does to the reflectivity estimate.
- [01-10-07 Two-Dimensional Fourier Analysis and Wavenumber Filtering](../../01-mathematics/10-fourier-analysis/07-2d-fourier.md) —
  the transform used throughout.
- [06-02-03 Tau-p and the Radon Transform](../../06-seismology/02-ray-theory-and-travel-times/03-tau-p.md) —
  the Radon transform in its travel-time role.
