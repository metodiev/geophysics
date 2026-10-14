---
id: 06-08-01
title: "Receiver Functions: Deconvolution and Ps Conversions"
level: doctoral
prereqs: ["06-01-02", "06-02-02", "03-10-05"]
tags: [seismology, receiver-functions, deconvolution, crustal-structure, ps-conversion]
---

# Receiver Functions: Deconvolution and Ps Conversions

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ray parameter $p$ from Snell's law for a layered medium, and
   define the vertical slowness $q = \sqrt{v^{-2} - p^{2}}$ for P and S.
2. **Derive** the Ps delay time
   $\Delta t = H\left(q_s - q_p\right)$ from the ray geometry, and explain why
   the down-going P leg is common to the direct P and the converted Ps.
3. **Show** that a single Ps delay time cannot determine both the layer thickness
   $H$ and the ratio $k = v_p/v_s$, and **quantify** the trade-off.
4. **Derive** the source-equalisation deconvolution from the convolutional
   model, and explain why it requires a water level or another stabiliser.
5. **Measure** the deconvolution trade-off between resolution and noise gain,
   and state the regularisation bias it buys.
6. **Recognise** the diagnostics (moveout sign, magnitude) that separate a
   primary conversion from a multiple.

## Prerequisites

- [06-01-02 P and S Waves](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  the two body-wave polarisations and their speeds.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter as a conserved quantity.
- [03-10-05 Filtering and Detrending](../../03-scientific-computing/10-obspy-and-seismic-data/05-filtering-detrending.md) —
  the practical frequency-domain tools used here.

## 1. Intuition: reading crustal structure from a distant earthquake

A teleseism is an earthquake thousands of kilometres away. Its energy arrives at
a station as a nearly vertical P wave. On the way up through the crust beneath
the station, a small fraction of that P energy converts to an S wave every time
the ray crosses a contrast in elastic properties. That converted wave is called
**Ps** (or P-to-S). It travels the last part of its path as a slower S wave, so
it arrives **after** the direct P by a delay that grows with the depth of the
converting interface.

That is the whole idea of a receiver function: listen to the P coda, find the
converted arrivals, and convert their delays into depths. The method is the
workhorse of crustal and upper-mantle structure, and its popularity comes from a
single practical fact — one three-component station can do it, no explosion or
controlled source required.

Two details make it harder than it sounds, and this lesson is largely about
them.

- The earthquake source is unknown and different every time, so the shape of the
  incoming wavelet varies from event to event. We must **remove the source**.
  That removal is a deconvolution, and every deconvolution is an ill-posed
  inverse problem.
- The delay time of Ps depends on the layer thickness $H$ **and** on both
  velocities. One measured delay therefore cannot give all three. This
  non-uniqueness is not a nuisance to be hidden; it is the central fact of
  receiver-function interpretation and the honesty point of this module.

## 2. Precise definitions

### 2.1 The ray parameter

For a stack of horizontal layers, Snell's law requires the horizontal slowness

$$p \equiv \frac{\sin i}{v} \qquad (\mathrm{s\,km^{-1}} \text{ or } \mathrm{s\,m^{-1}})$$

to be the same in every layer, where $i$ is the angle between the ray and the
vertical. We call $p$ the **ray parameter**. A teleseismic P has $p$ between
roughly $0.04$ and $0.08\ \mathrm{s\,km^{-1}}$; the exact value depends on the
earthquake distance. Unless stated otherwise, all numbers in this lesson are
**SYNTHETIC** teaching values, not measurements.

### 2.2 Vertical slowness

Only the vertical component of the slowness carries the wave across an
interface. For a phase of speed $v$,

$$q(v,p) = \sqrt{\frac{1}{v^{2}} - p^{2}} \qquad (\mathrm{s\,km^{-1}}).$$

Geometrically, if $i$ is the angle from the vertical, $\cos i = \sqrt{1-\sin^2 i}
= v\sqrt{v^{-2}-p^{2}} = v\,q$, so $q = \cos i / v$: the reciprocal of the
vertical phase speed. The time to cross a layer of thickness $H$ at this angle is
$H\,q$.

### 2.3 The converted phase

A P wave incident on an interface with a non-zero angle generates reflected and
transmitted P and S waves (the four-wave problem). The transmitted S is the Ps
conversion. At normal incidence ($p = 0$) the conversion coefficient vanishes by
symmetry; for teleseismic rays it is small but measurable, typically a few per
cent of the direct P amplitude. The receiver function is the record of these
conversions.

## 3. Derivations

### 3.1 Delay time of the Ps conversion

Place the station on the surface, a horizontal converter at depth $H$, and
consider a ray arriving from below with ray parameter $p$. Two arrivals share the
same horizontal slowness $p$ by Snell's law:

- the **direct P**, which stays P through the layer;
- the **Ps**, which is P down to the interface and S on the way back up.

The down-going leg is identical for both, and it takes time $H q_p$. On the
up-going leg, P takes $H q_p$ and S takes $H q_s$. The measured delay of Ps
relative to direct P is therefore the **difference of the up-going legs**:

$$
\boxed{\;\Delta t_{Ps} = H\,q_s - H\,q_p
= H\left(\sqrt{v_s^{-2} - p^{2}} - \sqrt{v_p^{-2} - p^{2}}\right).}
$$

*Numerical check (SYNTHETIC).* With $H = 32.0\ \mathrm{km}$,
$v_p = 6.00\ \mathrm{km\,s^{-1}}$, $v_s = 3.50\ \mathrm{km\,s^{-1}}$,
$p = 0.060\ \mathrm{s\,km^{-1}}$:

$$q_p = \sqrt{0.027778 - 0.003600} = 0.155492\ \mathrm{s\,km^{-1}},$$
$$q_s = \sqrt{0.081633 - 0.003600} = 0.279343\ \mathrm{s\,km^{-1}},$$
$$\Delta t_{Ps} = 32.0 \times (0.279343 - 0.155492)
= 32.0 \times 0.123851 = 3.9632\ \mathrm{s}.$$

This is the number the demonstration `code/rf_principle_demo.py` prints.

### 3.2 The H-k trade-off, quantified

Rewrite $\Delta t$ using $k = v_p/v_s$ and $v_p$:

$$\Delta t = H\left(\frac{1}{v_s}\sqrt{1 - p^{2}v_s^{2}}
- \frac{1}{v_p}\sqrt{1 - p^{2}v_p^{2}}\right).$$

One measured number, $\Delta t$, and two unknowns of interest, $H$ and $k$
(with $v_p$ assumed known). Holding $\Delta t$ fixed, $H$ and $k$ move together.
Differentiating with respect to $k$ at fixed $\Delta t$:

$$\frac{\mathrm{d}H}{\mathrm{d}k}\bigg|_{\Delta t}
= -\,\frac{H}{\Delta t}\,\frac{\partial \Delta t}{\partial k}
= -\,\frac{H}{\Delta t}\cdot H \frac{\partial (q_s - q_p)}{\partial k}.$$

Since $q_s = \sqrt{k^{2}v_p^{-2} - p^{2}}$ and $\partial q_s/\partial k
= k/(v_p^{2} q_s)$,

$$\frac{\mathrm{d}H}{\mathrm{d}k}\bigg|_{\Delta t}
= -\,\frac{H^{2}}{\Delta t}\,\frac{k}{v_p^{2}\,q_s}.$$

*Numerical check.* $H^2/\Delta t = 1024/3.9632 = 258.4\ \mathrm{km}$;
$k/(v_p^2 q_s) = 1.714/((36)(0.279343)) = 0.1704\ \mathrm{km\,s^{-1}}$;
the product is $-44.0\ \mathrm{km}$ per unit $k$. The demonstration reports
$-43.2\ \mathrm{km}$ per unit $k$ by finite differences over $1.65 \le k \le 1.80$
— agreement to about 2%, the residual being second-order curvature. A **1%
error in $k$ moves the depth by roughly 0.7–0.8 km**; a 5% error moves it by
3–4 km. That is why H-k stacking, which adds more measurements, exists.

### 3.3 Moveout of the conversion

Because $q$ depends on $p$, so does $\Delta t$. Expanding for small $p$:

$$q \approx \frac{1}{v}\left(1 - \tfrac{1}{2}p^{2}v^{2}\right)
= \frac{1}{v} - \frac{1}{2}p^{2}v,$$

so

$$\Delta t \approx H\left(\frac{1}{v_s} - \frac{1}{v_p}\right)
- \frac{H}{2}p^{2}\left(v_s - v_p\right).$$

The delay depends on $p^{2}$ to leading order, which is why moveout is almost
linear in $p^{2}$ at teleseismic slownesses. The demonstration measures a slope
$\mathrm{d}(\Delta t)/\mathrm{d}(p^{2}) = +45.3\ \mathrm{s\,(s\,km^{-1})^{-2}}$
and a maximum deviation from the straight line of only $4.5\ \mathrm{ms}$ over
$0.02 \le p \le 0.08\ \mathrm{s\,km^{-1}}$.

### 3.4 Source equalisation by deconvolution

Let the vertical component be $V(\omega)$ and the radial component $R(\omega)$.
In the convolutional model both are the source wavelet $S(\omega)$ convolved
with the receiver-side response:

$$V(\omega) = S(\omega)\,E_v(\omega), \qquad
R(\omega) = S(\omega)\,E_r(\omega).$$

$E_v$ is nearly a delta for teleseismic P (the vertical is dominated by the
direct arrival); $E_r$ contains the Ps conversions. Divide:

$$E(\omega) = \frac{R(\omega)}{V(\omega)} = \frac{E_r(\omega)}{E_v(\omega)}.$$

This is the receiver function: the source cancels because it is common to both
components. In practice we stabilise the division with a **water level** $w$:

$$E(\omega) = \frac{R(\omega)\,V^{*}(\omega)}
{\left|V(\omega)\right|^{2} + w\,\max_\omega \left|V(\omega)\right|^{2}}.$$

Where $|V|$ is large the result is the exact ratio; where $|V|\to 0$ (source
notches, high frequencies) the denominator is $w\max|V|^{2}$ and the
contribution is suppressed instead of blowing up. **The water level is a
regularisation parameter, and setting it is choosing a resolution-to-noise
trade.**

## 4. Physical interpretation

- $\Delta t$ is a *time*, and it is a difference of two travel times along the
  same down-going path. The conversion depth enters only through $H$.
- Increasing $p$ (a more distant, more horizontal ray) *increases* $\Delta t$:
  the up-going legs are longer, and the S leg lengthens faster than the P leg.
  This is the measured positive moveout slope.
- Deconvolution in the frequency domain is a *division*. Every division by a
  quantity that can approach zero is a stability question, and the receiver
  function is no exception.
- **Why not cross-correlate?** A common alternative is to correlate the radial
  with the vertical instead of dividing spectra. Correlation multiplies by the
  source spectrum rather than cancelling it, so the result is a receiver function
  convolved with the source autocorrelation — a *smoothed* image whose pulses
  broaden as the source lengthens. Deconvolution removes the source; correlation
  only averages it away when the source is stable between events.
- **The third component.** The transverse (T) component is not used in this
  lesson. For horizontal, isotropic structure it should contain no Ps energy, so
  any T signal is evidence of something else — anisotropy, a dipping interface,
  or noise. That is the subject of [04](04-anisotropy-receiver-functions.md).

## 5. Assumptions

1. The structure is **horizontally layered and isotropic** beneath the station.
   A dipping interface or anisotropy breaks this and is treated in
   [04 Anisotropy from Receiver Functions](04-anisotropy-receiver-functions.md).
2. The ray parameter $p$ is known (from the earthquake distance and a
   reference model).
3. The vertical component is dominated by the direct P; source-side structure
   and the radiation pattern are common to both components and therefore
   cancel, but scattering does not.
4. The interface is sharp compared with the shortest wavelength in the band; a
   finite-width transition reduces the conversion amplitude (see
   [03 Moho Discontinuity Depth and Sharpness](03-moho-interface.md)).
5. Noise is additive and independent between components.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| ray parameter | $p$ | $\mathrm{s\,km^{-1}}$ | $\sin i$ dimensionless / $v$ |
| vertical slowness | $q$ | $\mathrm{s\,km^{-1}}$ | $v^{-2}$ is $\mathrm{s^2 km^{-2}}$; $\sqrt{\cdot}$ gives $\mathrm{s\,km^{-1}}$ |
| thickness | $H$ | km | |
| delay time | $\Delta t$ | s | $\mathrm{km} \times \mathrm{s\,km^{-1}} = \mathrm{s}$ |

The product $H q$ is the only combination that can produce a time, and it must:
a slowness times a length is a time. If a computation of $\Delta t$ comes out in
$\mathrm{s^2 km^{-1}}$ or $\mathrm{km^2 s^{-1}}$, a factor of a velocity has been
misplaced.

## 7. Worked examples

### Example 1 — delay time and the depth trade-off

A station records a Ps delay of $4.20\ \mathrm{s}$ at $p = 0.055\ \mathrm{s\,km^{-1}}$.
Assume $v_p = 6.20\ \mathrm{km\,s^{-1}}$ and $k = 1.75$.

1. $v_s = v_p/k = 3.543\ \mathrm{km\,s^{-1}}$.
2. $q_p = \sqrt{1/38.44 - 0.003025} = \sqrt{0.023027} = 0.151746$.
3. $q_s = \sqrt{1/12.552 - 0.003025} = \sqrt{0.076643} = 0.276845$.
4. $H = \Delta t / (q_s - q_p) = 4.20/(0.125099) = 33.57\ \mathrm{km}$.

Now suppose the true $k$ were $1.70$, not $1.75$. Then $v_s = 3.647$,
$q_s = \sqrt{0.075179-0.003025}=0.268619$, and
$H = 4.20/0.116873 = 35.94\ \mathrm{km}$. A $3\%$ change in $k$ moved the depth
by $2.4\ \mathrm{km}$ — *and the data are identical*. This is the trade-off.

### Example 2 — moveout correction of a wrong velocity

Using the demonstration's SYNTHETIC model, if the analyst adopts $k_{\text{try}}
= 1.60$ instead of the true $1.714$ but keeps the same measured delay, the
inferred thickness is $38.00\ \mathrm{km}$ instead of $32.00\ \mathrm{km}$ — a
$+6.0\ \mathrm{km}$ ($+18.8\%$) depth error. The stack peak stays at 100% of its
correct value because the residual misalignment is nearly independent of $p$
(its spread is $0.010\ \mathrm{s}$). **A wrong velocity biases the depth far more
than it degrades the stack.**

### Example 3 — deconvolution noise gain

The demonstration adds noise of rms $0.0045$ (4.9% of the radial rms) and
deconvolves with water levels from $10^{-8}$ to $10^{-1}$:

| water level | Ps/P amplitude | pulse FWHM (s) | noise gain |
|---|---|---|---|
| $10^{-8}$ | 0.347 | 0.160 | 23.8× |
| $10^{-6}$ | 0.345 | 0.160 | 3.3× |
| $10^{-3}$ | 0.346 | 0.200 | 1.1× |
| $10^{-1}$ | 0.350 | 0.260 | 0.8× |

The recovered Ps/P ratio is $0.347$ against a true injected value of $0.350$:
the amplitude ratio is robust because numerator and denominator scale together.
What the water level really controls is the pair (resolution, noise gain), and
they move in opposite directions. A tiny water level sharpens the pulse and
amplifies noise 24-fold; a large one suppresses noise and broadens the pulse by
60%. The forward-model residual (convolving the recovered function back with the
vertical) measures the price: $0.00\%$ at $w=10^{-8}$, $1.29\%$ at $10^{-3}$,
and $19.45\%$ at $10^{-1}$. That growth is the **regularisation bias**.

## 8. Python demonstration

`code/rf_principle_demo.py` performs the whole calculation and prints labelled
results with units. It:

1. computes $\Delta t_{Ps}$ from the depth-slowness relation and prints $q_p$,
   $q_s$;
2. tabulates $\Delta t$ versus $p$ and measures the moveout slope;
3. tabulates the $(H,k)$ pairs that reproduce one delay;
4. computes the multiple-bounce times $t_{PpPs}$ and $t_{PpSs+PsPs}$;
5. measures the water-level trade-off (resolution versus noise gain);
6. verifies the spectral ratio against the *analytic* transfer function
   $1 + (a_{Ps}/a_p)e^{-i\omega \Delta t}$ on the band carrying source energy —
   agreement to $5.5\times10^{-7}$ — and against a forward model, whose residual
   grows with the water level as the regularisation bias.

A subtlety worth understanding: a Ricker wavelet of $1\ \mathrm{Hz}$ has
essentially no spectral energy above about $4\ \mathrm{Hz}$, so only $127$ of
$1001$ frequency bins carry signal. Deconvolution cannot recover what the source
never emitted; it can only return a band-limited image of the Earth. That is the
physical face of the same underdetermination the water level stabilises.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-receiver-function-principle-exercises.md`](./exercises/01-receiver-function-principle-exercises.md)
and
[`exercises/01-receiver-function-principle-solutions.md`](./exercises/01-receiver-function-principle-solutions.md).

- **★** Compute $\Delta t_{Ps}$ for $H=28$ km, $v_p=6.1$, $v_s=3.5$ at
  $p=0.05\ \mathrm{s\,km^{-1}}$, and state the units of each factor.
- **★★** Derive $\mathrm{d}H/\mathrm{d}k|_{\Delta t}$ from the closed form and
  evaluate it for the model in Example 1.
- **★★** Given the demonstration's noise-gain table, choose a water level for a
  survey that must resolve a $0.5\ \mathrm{s}$ pulse and justify the choice.
- **★★★** Show that a $1\%$ error in $p$ produces a smaller depth error than a
  $1\%$ error in $k$, and quantify the ratio for the demonstration model.

## 10. Common mistakes

1. **Reporting one depth from one delay.** A receiver function plus an assumed
   $k$ gives a depth *conditional on that $k$*. Without the assumption the answer
   is a curve, not a number.
2. **Choosing the water level by taste.** It must be chosen against a stated
   noise level and a stated resolution target; otherwise the result is not
   reproducible.
3. **Normalising away the amplitude.** Receiver functions are usually normalised,
   which discards the conversion amplitude that carries information about the
   sharpness and the impedance contrast.
4. **Reading multiples as structure.** A peak in the receiver function that has
   the wrong moveout sign is a multiple, not a deeper interface.
5. **Forgetting the unit of $p$.** Mixing $\mathrm{s\,km^{-1}}$ with
   $\mathrm{s\,m^{-1}}$ changes $\Delta t$ by a factor of $10^{3}$.

## 11. Real-world applications

- **Crustal thickness mapping.** H-k stacking of receiver functions from
  temporary arrays is the standard method for mapping the Moho without
  controlled sources, and it is how continent-scale crustal-thickness maps are
  made.
- **Mantle transition zone.** The same deconvolution applied to longer delays
  images the 410 km and 660 km discontinuities, whose depths are temperature
  proxies.
- **Instrument response and data quality.** Because the method divides by the
  vertical component, it is unusually sensitive to instrument problems; a
  mis-oriented horizontal sensor converts vertical noise into a spurious
  transverse signal.
- **Signal-processing practice.** Water-level deconvolution, predictive
  deconvolution and spiking deconvolution in exploration seismology are the same
  mathematics applied to a different band.

## 12. Further reading

- **Langston, C. A. (1979). Structure under Mount Rainier, Washington, inferred
  from teleseismic body waves. *Journal of Geophysical Research*, 84(B9),
  4749–4762.** Level: research. The paper that introduced the receiver-function
  concept; read it for the physical argument, not the maths.
- **Ammon, C. J. (1991). The isolation of receiver effects from teleseismic
  P waveforms. *Bulletin of the Seismological Society of America*, 81(6),
  2504–2510.** Level: research. The source-equalisation deconvolution in the
  form used here.
- **Ligorría, J. P., & Ammon, C. J. (1999). Iterative deconvolution and
  receiver-function estimation. *Bulletin of the Seismological Society of
  America*, 89(5), 1395–1400.** Level: research. An alternative to the
  water-level spectral division that avoids selecting a water level.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference. The
  `obspy.signal` and `obspy.taup` modules provide the tools used in the demo.
- **FDSN web services specification.** <https://www.fdsn.org/webservices/> —
  Level: reference. How to obtain the waveforms this method needs, offline or
  online.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md) — the
  standard remedy for the trade-off derived in Section 3.2.
- [03 Moho Discontinuity Depth and Sharpness](03-moho-interface.md) — what the
  conversion amplitude says, and where multiples confuse it.
- [04 Anisotropy from Receiver Functions and Shear-Wave Splitting](04-anisotropy-receiver-functions.md) —
  what the transverse component adds.
- [05 Joint Inversion of Receiver Functions and Surface Waves](05-joint-inversion-rf.md) —
  how an independent measurement of $v_s$ breaks the trade-off.
- [06-02-03 Tau-p and the Radon Transform](../02-ray-theory-and-travel-times/03-tau-p.md) —
  the slowness domain used throughout.

## 14. Self-assessment checklist

- [ ] I can derive $\Delta t_{Ps} = H(q_s - q_p)$ from the ray geometry without notes.
- [ ] I can state the units of $p$, $q$, $H$ and $\Delta t$ and check the product.
- [ ] I can explain why one delay cannot give both $H$ and $k$.
- [ ] I can estimate $\mathrm{d}H/\mathrm{d}k$ numerically and analytically.
- [ ] I can explain why deconvolution needs a water level and what it trades away.
- [ ] I can read a noise-gain versus resolution table and choose a water level.
- [ ] I can state one diagnostic that separates a multiple from a primary.
