---
id: 10-03-05
title: "Planetary GPR: MARSIS, SHARAD and Lunar Radar"
level: research
prereqs: ["10-01-01", "10-01-03", "10-01-05", "10-03-02"]
tags: [gpr, near-surface, geotechnical, planetary, radar-sounding, ionosphere, clutter, resolution]
---

# Planetary GPR: MARSIS, SHARAD and Lunar Radar

**All models and data in this module are SYNTHETIC.** The orbital altitudes,
target depths, ionospheric densities, bandwidths and permittivities used in the
calculations below are chosen teaching values. Instrument names are given so the
reader can locate the literature; **no measured value from any mission is quoted
or used**, and no capability of any real instrument is claimed from this lesson's
numbers. Physical constants, the permittivity of water and the plasma-frequency
constant are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the range resolution $\Delta r = c/(2B\sqrt{\varepsilon_r})$ from a
   time resolution $1/B$, and **compute** the price paid for depth in resolution.
2. **Derive** the Fresnel-zone radius $r_f = \sqrt{\lambda h/2}$ at orbital
   altitude, and **compute** the surface footprint it implies.
3. **Derive** the surface-clutter relation $x = \sqrt{2hd\sqrt{\varepsilon_r}}$,
   and **decide** whether a given subsurface echo could be mimicked by off-nadir
   surface topography.
4. **Construct** two subsurface models with the same two-way time and the same echo
   amplitude, and **quantify** the depth difference between them.
5. **Derive** the plasma frequency from the electron density, and **show** that the
   ionospheric group delay is $40.3\,\mathrm{TEC}/f^2$ by two independent routes.
6. **Compute** the differential ionospheric delay across a band, compare it with
   the range resolution, and **state** why a wideband sounding radar must correct
   for it.
7. **Distinguish** the attenuation limit from the clutter limit, and **state**
   which one binds in a cold, dry target and which in a warm, wet one.

## Prerequisites

- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — the speed, the reflection coefficient and the source pulse.
- [10-01-03 Attenuation, Penetration Depth and Frequency Trade-Offs](../01-gpr-principles/03-gpr-attenuation-penetration.md)
  — absorption, dynamic range and the depth of investigation.
- [10-01-05 Vertical and Horizontal Resolution Limits](../01-gpr-principles/05-gpr-resolution.md)
  — the Fresnel zone and the $\lambda/4$ limit.
- [10-03-02 GPR for Glacier Thickness and Internal Stratigraphy](02-gpr-glaciology.md)
  — the low-loss dielectric layer, the surface echo as an amplitude reference and
  the depth-permittivity trade.

## 1. Intuition: a radar at 300 km looking for metres

A planetary sounding radar is the same measurement as a ground GPR with three
things changed, and every difficulty follows from them:

- the antenna is **hundreds of kilometres** from the target rather than metres, so
  the *surface* is not a boundary to be avoided but the largest reflector in the
  scene;
- the target is often a **kilometre** of ice, regolith or sediment, so the
  instrument must be low-frequency and narrow-band, and pays in resolution;
- the path includes a **plasma**, which is dispersive and delays the pulse in a
  way that depends on frequency.

The reward is the only direct measurement of subsurface structure on another
body: an ice sheet's thickness, a polar deposit's layering, a regolith's
stratigraphy. The measurement is a two-way time. As everywhere in this module, a
two-way time is a depth only through a permittivity, and the permittivity at a
planetary surface is known only as well as the surface echo is calibrated and the
material is assumed.

The honest difficulty, stated once and then quantified: **the limit on a planetary
sounder is usually not the noise but the surface.** A subsurface echo and an
off-nadir surface echo can arrive at the same time, and no amount of averaging in
time separates them. The only discriminators are geometric (where on the surface
the echo came from, which the along-track orbit geometry makes measurable) and
statistical (the clutter is not smooth in the way a subsurface layer typically
is). Section 3.3 turns that statement into an equation.

## 2. Precise definitions

| Quantity | Symbol | Meaning | Unit |
|---|---|---|---|
| bandwidth | $B$ | transmitted band | Hz |
| range resolution | $\Delta r$ | best separable two-way separation | m |
| altitude | $h$ | orbiter above the surface | m |
| Fresnel radius | $r_f$ | first-zone radius at altitude | m |
| off-nadir distance | $x$ | surface point with a matching delay | m |
| electron density | $n_e$ | plasma density | $\mathrm{m^{-3}}$ |
| plasma frequency | $f_p$ | cutoff/refraction scale | Hz |
| total electron content | TEC | column integral $\int n_e\,dl$ | $\mathrm{m^{-2}}$ |

**Nadir** means directly below the orbiter: the shortest range, the zero-Doppler
line, and the only direction from which a specular subsurface return is expected.
**Clutter** is any echo arriving from a direction other than nadir. **Distributed
versus specular**: a subsurface interface is usually *specular* at nadir (a
coherent, usually smooth echo) while a rough surface at a large incidence angle is
*distributed* (an incoherent, speckled echo). That difference is what a coherent
radar exploits.

**Instrument context (literature pointers, no numbers used here).** Mars has been
sounded by a low-frequency radar on an orbiter whose band extends down to a few
MHz, and by a higher-frequency sounder centred near $20\ \mathrm{MHz}$ with a
bandwidth of the order of $10\ \mathrm{MHz}$; the Moon was sounded in the
$1970$s by a sounder operating in the HF and VHF bands. Those specifications are
published in the papers listed in Section 10 and are **not** used in any
calculation here; the demonstration uses SYNTHETIC bandwidths of $1$, $10$ and
$100\ \mathrm{MHz}$ and a SYNTHETIC altitude, so every printed number is
traceable.

## 3. Derivations

### 3.1 Bandwidth into range resolution

A pulse of bandwidth $B$ occupies a time of order $1/B$. Two echoes separated by
less than that cannot be told apart, so the *time* resolution is $\Delta t = 1/B$
and the two-way range resolution is

$$\Delta r = \frac{c\,\Delta t}{2} = \frac{c}{2B},$$

where the factor $2$ is the round trip and the factor $c$ applies in vacuum. In a
medium of permittivity $\varepsilon_r$ both the speed and the wavelength shrink by
$\sqrt{\varepsilon_r}$, so the *spatial* resolution improves:

$$\Delta r = \frac{c}{2B\sqrt{\varepsilon_r}}.$$

*Numerical check.* The demonstration's table:

| $B$ (MHz) | $\Delta r$ vacuum (m) | in ice, $\varepsilon_r = 3.17$ (m) | in water (m) |
|---|---|---|---|
| $1$ | $149.9$ | $84.2$ | $16.7$ |
| $10$ | $15.0$ | $8.4$ | $1.7$ |
| $100$ | $1.5$ | $0.8$ | $0.2$ |

This is the central trade of planetary sounding: a $1\ \mathrm{MHz}$ bandwidth —
necessary to penetrate kilometres of ice — resolves $84\ \mathrm{m}$ in ice.
Any claim of a "metre-scale layer" from such a sounding must be a claim about
*modelling*, not about resolution.

### 3.2 The Fresnel zone at altitude

For a monostatic radar at altitude $h$, a surface point at horizontal distance $x$
from nadir has a two-way path longer than the nadir path by

$$\Delta \ell = 2\left(\sqrt{h^2+x^2}-h\right) \simeq \frac{x^2}{h}
\quad \mathrm{for}\ x \ll h.$$

Setting $\Delta \ell = \lambda/2$ for the first zone:

$$r_f = \sqrt{\frac{\lambda h}{2}}.$$

*Numerical check* (SYNTHETIC altitude $300\ \mathrm{km}$):

| $f$ (MHz) | $\lambda$ (m) | $r_f$ (m) | $r_f$ (km) | two-way time to the surface ($\mu$s) |
|---|---|---|---|---|
| $5$ | $59.96$ | $2\,999$ | $2.999$ | $2001.4$ |
| $20$ | $14.99$ | $1\,499$ | $1.499$ | $2001.4$ |
| $100$ | $3.00$ | $671$ | $0.671$ | $2001.4$ |

The footprint is **kilometres**, so a single echo averages the surface over that
circle. The along-track resolution that a map appears to have is bought back by
coherent processing of the Doppler history (synthetic aperture), which is why
these radars are coherent systems and why the along-track sampling is much finer
than $r_f$.

### 3.3 Surface clutter: the same delay, a different place

Now the discriminating equation. A subsurface interface at depth $d$ returns an
echo whose two-way time, measured from the surface echo, is

$$\Delta t_{\mathrm{sub}} = \frac{2d\sqrt{\varepsilon_r}}{c}.$$

A surface point at horizontal distance $x$ returns an echo delayed from the nadir
surface echo by

$$\Delta t_{\mathrm{surf}} = \frac{x^2}{hc}.$$

Equating the two:

$$\frac{2d\sqrt{\varepsilon_r}}{c} = \frac{x^2}{hc}
\;\Longrightarrow\;
x = \sqrt{2hd\sqrt{\varepsilon_r}}.$$

*Numerical check* (SYNTHETIC $h = 300\ \mathrm{km}$):

| $d$ (m) | $x$ for $\varepsilon_r = 3.17$ (km) | $x$ for $\varepsilon_r = 80.1$ (km) |
|---|---|---|
| $10$ | $3.27$ | $7.33$ |
| $100$ | $10.34$ | $23.17$ |
| $1000$ | $32.68$ | $73.28$ |

**A subsurface echo at $100\ \mathrm{m}$ sits at the same delay as a surface echo
from $10\ \mathrm{km}$ off nadir.** Range alone cannot separate them. The
separators are the Doppler history (an off-nadir surface patch has a different
range-rate than the nadir point, so it focuses at a different azimuth) and the
scattering statistics (surface clutter is incoherent and speckled at the
resolution scale; a subsurface interface is usually specular). This is precisely
why clutter simulation is a required part of interpreting a candidate subsurface
reflection, and why the demonstration prints the geometry rather than an
amplitude.

### 3.4 The permittivity ambiguity: one observation, two models

A single sounding gives a two-way time and an amplitude. Write them as

$$\Delta t = \frac{2d\sqrt{\varepsilon_r}}{c},
\qquad
A = R(\varepsilon_r)\,\exp\!\left[-2\!\int_0^d \alpha\,dz\right] \times (\text{system}).$$

The time fixes the **product** $d\sqrt{\varepsilon_r}$; it does not fix $d$. The
amplitude adds one more equation but introduces the absorption, which is itself
unknown. Two models with the same two observations therefore differ in depth.

*Constructed example (SYNTHETIC).* Take a two-way time of $20.0\ \mu$s and a
bed echo amplitude that, after geometric spreading, corresponds to a total
attenuation factor of $33.68\ \mathrm{dB}$:

| model | $\varepsilon_r$ | $d$ (m) | one-way $\alpha$ (dB/m) | two-way loss (dB) |
|---|---|---|---|---|
| A | $3.17$ | $1684$ | $0.0100$ | $33.68$ |
| B | $4.00$ | $1499$ | $0.0112$ | $33.68$ |

Both reproduce the same time **and** the same amplitude. Their depths differ by
$185\ \mathrm{m}$, i.e. $11.0\%$ of model A. The ambiguity is broken only by an
independent constraint on the permittivity — the calibrated surface reflection, a
known thickness, or a laboratory analogue.

### 3.5 The ionosphere: plasma frequency and group delay

A cold plasma has the dispersion relation $\omega^2 = \omega_p^2 + k^2c^2$, with
the plasma (angular) frequency

$$\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}.$$

With $e = 1.602176634\times10^{-19}\ \mathrm{C}$,
$\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$ and
$m_e = 9.1093837015\times10^{-31}\ \mathrm{kg}$:

$$\frac{e^2}{\varepsilon_0 m_e} = 3182.7\ \mathrm{m^3\,s^{-2}}
\;\Rightarrow\;
\omega_p = 56.405\sqrt{n_e}\ \mathrm{rad\,s^{-1}}
\;\Rightarrow\;
f_p = \frac{\omega_p}{2\pi} = 8.98\sqrt{n_e}\ \mathrm{Hz}.$$

*Numerical check.* For the SYNTHETIC $n_e = 1.0\times10^{11}\ \mathrm{m^{-3}}$:
$f_p = 8.98\sqrt{10^{11}} = 2.840\ \mathrm{MHz}$ (the demonstration prints
$2.840\ \mathrm{MHz}$). At a $20\ \mathrm{MHz}$ carrier, $f_p/f = 0.142$, so the
wave propagates with a small perturbation.

For $f \gg f_p$ the group refractive index is
$n_g \simeq 1 + \tfrac{1}{2}(f_p/f)^2$, so a plasma column of length $L$ adds an
excess path

$$\Delta \ell = \frac{1}{2}\left(\frac{f_p}{f}\right)^{2}L
= \frac{1}{2}\cdot\frac{80.64\,n_e}{f^{2}}\,L
= \frac{40.3\,\mathrm{TEC}}{f^{2}},$$

with $\mathrm{TEC} = n_e L$ in $\mathrm{m^{-2}}$ and $f$ in Hz. The standard
dispersion constant $40.3\ \mathrm{m^3\,s^{-2}}$ is therefore not a mystery
number: it is $\tfrac{1}{2}(8.98)^2 = 40.32$, i.e. the plasma-frequency constant
squared over two.

*Numerical check, two routes.* With SYNTHETIC $n_e = 10^{11}\ \mathrm{m^{-3}}$ over
$100\ \mathrm{km}$, so $\mathrm{TEC} = 10^{16}\ \mathrm{m^{-2}}$, at
$f = 20\ \mathrm{MHz}$:

$$\Delta\ell_{\mathrm{slab}} = \frac{1}{2}(0.14200)^{2}(10^{5}) = 1008.0\ \mathrm{m},$$

$$\Delta\ell_{\mathrm{TEC}} = \frac{40.3 \times 10^{16}}{(2\times10^{7})^{2}}
= 1007.5\ \mathrm{m}.$$

The two agree to $0.05\%$ — the residual being exactly the rounding of $8.98$
against the exact $8.9772$ and of $40.3$ against $40.32$. **That agreement is a
check on the constants, not on the ionosphere**, and it is the reason these
constants can be used interchangeably.

The round-trip group delay is $2\Delta\ell/c = 6.7\ \mu$s, i.e. a **range bias of
about $1\ \mathrm{km}$**. Two consequences:

- the surface and the subsurface echoes *share* the delay (both traverse the same
  plasma), so a **thickness is unaffected** while an **absolute range, hence an
  altitude and a topographic datum, is not**;
- the delay scales as $1/f^2$, so it is *different* at the two ends of the band.
  Across $15$–$25\ \mathrm{MHz}$ the differential delay is
  $40.3(10^{16})(1/15^{2}-1/25^{2})\times10^{-12} = 1146\ \mathrm{m}$, against a
  range resolution of $15.0\ \mathrm{m}$ — a factor of $76$. **Uncorrected, the
  ionosphere smears a single interface over more than a kilometre of apparent
  depth**, which is why these systems estimate and remove the dispersive phase
  before any depth is computed.

### 3.6 Attenuation or clutter?

The two candidate limits behave completely differently:

$$\text{attenuation limit}: \quad d_{60} = \frac{60\ \mathrm{dB}}{2\alpha},
\qquad
\text{clutter limit}: \quad d_{\mathrm{clutter}} = \frac{W^2}{2h\sqrt{\varepsilon_r}},
$$

where $W$ is the along-track window within which clutter is not (or cannot be)
discriminated. With SYNTHETIC $\alpha = 0.010\ \mathrm{dB\,m^{-1}}$ the
attenuation limit is $3000\ \mathrm{m}$, while for $W = 1\ \mathrm{km}$,
$h = 300\ \mathrm{km}$, $\varepsilon_r = 3.17$ the clutter limit is
$d = W^2/(2h\sqrt{\varepsilon_r}) = 0.94\ \mathrm{m}$. In **cold, dry** material
the binding limit at depth is therefore clutter, not absorption — the opposite of
the warm or wet case, where $\alpha$ is tens of $\mathrm{dB\,m^{-1}}$ and the echo
is gone before clutter matters. This is why the same instrument can map kilometres
of cold polar ice and only metres of a wet temperate deposit.

## 4. Physical interpretation

- **Resolution and penetration are one parameter, not two.** Bandwidth buys
  resolution and costs depth; a planetary sounder is a low-bandwidth instrument
  *by design*, and every metre-scale claim from it is a modelling claim.
- **The surface is the competition.** A subsurface echo is confirmed by geometry
  and coherence, never by its delay alone.
- **The permittivity is the depth.** The time gives $d\sqrt{\varepsilon_r}$; only
  a calibration or an assumption gives $d$.
- **The plasma is shared, so it cancels in a difference and biases an absolute
  range.** It also disperses, which a wideband system must correct.
- **A single sounding is an under-determined problem with a rich observable set**
  — time, amplitude, polarisation, Doppler — and the way the literature improves
  its confidence is by accumulating independent constraints, not by asserting the
  first one.

## 5. Worked examples

### Example 1 — what a bandwidth can and cannot see

A sounder with $B = 10\ \mathrm{MHz}$ images a layered polar deposit with
$\varepsilon_r = 3.17$.

1. $\Delta r = c/(2B\sqrt{\varepsilon_r})$, evaluated for this example as
   $2.99792458\times10^{8}/(2\times10^{7}\times1.7804) = 8.42\ \mathrm{m}$.
2. A four-sample Ricker-like wavelet is then about $34\ \mathrm{m}$ long, and two
   interfaces closer than that are one event, however well the amplitudes are
   measured.
3. A reported "layering at $20\ \mathrm{m}$ spacing" from such data must come from
   the *phase* of a composite wavelet (a forward model), and the honest statement
   of its uncertainty is the admitted range of that model — not $8.42\ \mathrm{m}$.

### Example 2 — is that a subsurface echo or a cliff?

A candidate interface appears at $1.2\ \mu$s after the surface echo, in a region
with $\varepsilon_r = 3.17$. Convert the delay to a depth and to a clutter
distance:

1. Depth: $d = c\Delta t/(2\sqrt{\varepsilon_r})$, evaluated as
   $2.99792458\times10^{8}(1.2\times10^{-6})/3.5609 = 359.75/3.5609 =
   101.0\ \mathrm{m}$.
2. Clutter distance: $x = \sqrt{2hd\sqrt{\varepsilon_r}}$. With
   $h = 300\ \mathrm{km}$ and $d = 101.0\ \mathrm{m}$,
   $x = \sqrt{2(3\times10^{5})(101.0)(1.7804)} = 10\,388\ \mathrm{m}$, i.e.
   about $10.4\ \mathrm{km}$.
3. So a real subsurface interface at about $101\ \mathrm{m}$ and a topography at
   about $10.4\ \mathrm{km}$ off nadir are equally consistent with the delay. The
   test is not the delay: it is whether the echo's Doppler history matches a fixed
   point in the subsurface frame (the interface focuses at zero Doppler and its
   range-rate follows the orbiter's altitude) or a surface point with a different
   range-rate and a speckled amplitude.

### Example 3 — the ionospheric delay, corrected and uncorrected

The same $1.2\ \mu$s interface, with the SYNTHETIC plasma of Section 3.5.

1. Uncorrected absolute range: the surface echo is delayed by about
   $1008\ \mathrm{m}$ of one-way path (twice that in round-trip time), so an altitude
   derived from the surface echo is wrong by a kilometre — a real problem for
   topography, and a silent one, because the surface echo still looks sharp.
2. Uncorrected dispersion: the differential delay of $1146\ \mathrm{m}$ across a
   $10\ \mathrm{MHz}$ band is $76\times$ the range resolution, so the interface is
   smeared into an unreadable ramp rather than a delayed event.
3. Thickness: the *difference* between the surface and the interface delay is
   almost free of the plasma, because both traverse the same column; the residual
   is second-order in the plasma and is the reason thickness estimates survive
   poor ionospheric knowledge while topographic ones do not.

## 6. Assumptions and regime of validity

1. **A plane, layered subsurface and a specular interface.** A rough or dipping
   interface scatters incoherently and the coherent sum that both the resolution
   and the amplitude budget assume is lost.
2. **Low loss and a non-magnetic medium** for $\Delta r$ and for
   $v = c/\sqrt{\varepsilon_r}$; in a conducting or magnetised medium the
   dispersion relation changes and the two-way path is no longer a simple product.
3. **$f \gg f_p$** for the group-delay expansion. In the SYNTHETIC example
   $f_p/f = 0.142$; the next term of the expansion,
   $(3/8)(f_p/f)^4 L = 15.2\ \mathrm{m}$, is $1.5\%$ of the $1008\ \mathrm{m}$
   delay — small but not zero, and quoted rather than dropped.
4. **A flat surface for the clutter relation.** Topography changes $x$ and, in a
   rough region, replaces the single specular clutter point with a statistical
   distribution.
5. **A nadir-looking, monostatic geometry** for $\Delta r$, $r_f$ and the clutter
   equation. An off-nadir or bistatic geometry changes all three.
6. **A known system response** for any amplitude work: the antenna pattern, the
   transmitted waveform and the receiver are all part of the calibration, and none
   of them is measured by the echo itself.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| bandwidth | $B$ | Hz | $1/[\mathrm{time}]$ |
| range resolution | $\Delta r$ | m | $c/(2B\sqrt{\varepsilon_r})$ |
| Fresnel radius | $r_f$ | m | $\sqrt{\mathrm{m}\times\mathrm{m}}$ |
| clutter distance | $x$ | m | $\sqrt{\mathrm{m}\times\mathrm{m}}$, dimensionless $\varepsilon_r$ |
| plasma frequency | $f_p$ | Hz | $8.98\sqrt{n_e}$ with $n_e$ in $\mathrm{m^{-3}}$ |
| TEC | $\int n_e\,dl$ | $\mathrm{m^{-2}}$ | density $\times$ length |
| dispersion constant | $40.3$ | $\mathrm{m^3\,s^{-2}}$ | $(1/2)(8.98)^2$ |
| excess path | $\Delta\ell$ | m | $40.3\,\mathrm{TEC}/f^2$ |

The dispersion constant's unit is worth checking once: $\mathrm{m^3\,s^{-2}}$
multiplied by $\mathrm{m^{-2}}$ and divided by $\mathrm{s^{-2}}$ gives
$\mathrm{m}$ — a length, as the excess path must be.

## 8. Python demonstration

[`code/gpr_planetary_demo.py`](code/gpr_planetary_demo.py) prints every number
quoted above:

1. range resolution against bandwidth, in vacuum, in ice and in water;
2. the Fresnel radius at a SYNTHETIC $300\ \mathrm{km}$ altitude for three
   frequencies;
3. the clutter distance for three target depths in two media;
4. two models with the same time and the same amplitude and an $11.0\%$ depth
   difference;
5. the plasma frequency from an electron density and the ionospheric excess path
   computed two independent ways, agreeing to $0.05\%$;
6. the differential delay across a $10\ \mathrm{MHz}$ band, compared with the
   range resolution;
7. the attenuation limit against the clutter limit.

The demonstration uses no orbital data, no instrument file and no network; it is
print-only, uses the fixed seed `20261014`, and exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-gpr-planetary-exercises.md`](exercises/05-gpr-planetary-exercises.md)
and
[`exercises/05-gpr-planetary-solutions.md`](exercises/05-gpr-planetary-solutions.md).

- **★** A $5\ \mathrm{MHz}$ bandwidth sounding in ice ($\varepsilon_r = 3.17$).
  Compute the range resolution and the two-way time resolution.
- **★★** At the same altitude, compute the Fresnel radius at $5$ and at
  $20\ \mathrm{MHz}$, and state the ratio and its physical reason.
- **★★★** Design a discrimination test between a subsurface echo at
  $200\ \mathrm{m}$ and surface clutter, stating the observable, the sample size
  needed for the statistics you rely on, and what would make the test fail.

## 10. Further reading

- **Picardi, G., et al. (2005). Radar soundings of the subsurface of Mars.
  *Science*, 310.** Level: research. The first report of a Mars subsurface
  sounding radar.
- **Seu, R., et al. (2007). SHARAD sounding radar on the Mars Reconnaissance
  Orbiter. *Journal of Geophysical Research: Planets*, 112.** Level: research.
  Instrument description; the source of the published specifications referred to
  in Section 2, none of which is used numerically here.
- **Phillips, R. J., et al. (2011). Massive CO$_2$ ice deposits sequestered in
  the south polar layered deposits of Mars. *Science*, 332.** Level: research. A
  worked example of turning a radar stratigraphy into a deposit inventory — and
  of the permittivity assumptions that step requires.
- **Orosei, R., et al. (2018). Radar evidence of subglacial liquid water on Mars.
  *Science*, 361.** Level: research. The most closely argued recent case for a
  subsurface interface, and the best available example of the clutter and
  amplitude arguments of Sections 3.3–3.4 in practice.
- **Porcello, L. J., et al. (1970). The Apollo Lunar Sounder Radar System.
  *Proceedings of the IEEE*, 58.** Level: research. The earliest orbital
  subsurface sounder; instructive for how much of the modern processing chain was
  already present.
- **Neal, A. (2004). Ground-penetrating radar and its use in sedimentology.
  *Earth-Science Reviews*, 66.** Level: research. The terrestrial analogue for
  the amplitude-versus-roughness problem.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. No measurement, capability or
> performance figure from these works is used in this lesson.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A sounder at $h = 300\ \mathrm{km}$ operates with $B = 10\ \mathrm{MHz}$ centred
> at $20\ \mathrm{MHz}$, over a target with $\varepsilon_r = 3.17$. It records a
> surface echo and a candidate subsurface echo $1.2\ \mu$s later.
> **(a)** Compute the range resolution in the target and the two-way time
> resolution. **(b)** Compute the Fresnel radius and state the surface area that
> contributes to one echo. **(c)** Convert $1.2\ \mu$s to a depth. **(d)** Compute
> the off-nadir distance whose surface echo has the same delay, and state two
> observables that distinguish the two candidates. **(e)** The dispersion constant
> is $40.3\ \mathrm{m^3\,s^{-2}}$; derive it from the plasma-frequency constant
> $8.98$. **(f)** Compute the differential ionospheric delay across the band for
> $\mathrm{TEC} = 10^{16}\ \mathrm{m^{-2}}$ and compare it with (a).

Worked versions of (a)–(d) and (f) are in the
[solutions](exercises/05-gpr-planetary-solutions.md).

## Common pitfalls

1. **Quoting a resolution that the bandwidth cannot deliver.** A
   $1\ \mathrm{MHz}$ band resolves $84\ \mathrm{m}$ in ice, whatever the sampling
   interval of the data product.
2. **Trusting a delay as proof of depth.** A subsurface echo at $100\ \mathrm{m}$ and
   a surface echo from $10\ \mathrm{km}$ off nadir arrive at the same time.
3. **Reporting a depth without the permittivity.** The time constrains
   $d\sqrt{\varepsilon_r}$; the demonstration's two models differ by $11\%$ in
   depth with identical observations.
4. **Treating the ionosphere as a constant delay.** It is dispersive: a
   differential delay of $1146\ \mathrm{m}$ across a $10\ \mathrm{MHz}$ band,
   against $15\ \mathrm{m}$ of resolution.
5. **Assuming a polar deposit's permittivity.** Density, dust content and
   temperature all move it, and the surface echo is the only in-situ constraint.
6. **Confusing the attenuation limit with the detection limit.** In cold dry
   material the clutter window binds first, and it does not improve with a longer
   stack.

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the wave physics,
  resolution and attenuation the sounding inherits.
- [10-03 GPR Applications](./README.md) — the terrestrial applications, including
  the glaciological case whose physics the polar soundings reuse.
- [17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md)
  — the same radar geometry from orbit, for the *surface* rather than the
  subsurface.
- [06-13 Planetary and Applied Seismology Frontiers](../../06-seismology/13-planetary-and-exploration-seismology/README.md)
  — the complementary planetary subsurface measurement.
- [02-07 Electromagnetism](../../02-physics/07-electromagnetism/README.md) — the
  plasma dispersion relation used in Section 3.5.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/gpr_planetary_demo.py`](code/gpr_planetary_demo.py) | The seven computations of Section 8 |
| [`exercises/05-gpr-planetary-exercises.md`](exercises/05-gpr-planetary-exercises.md) | Graded problems |
| [`exercises/05-gpr-planetary-solutions.md`](exercises/05-gpr-planetary-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_planetary_demo.py
```
