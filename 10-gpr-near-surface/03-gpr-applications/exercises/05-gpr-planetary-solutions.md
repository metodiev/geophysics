# Solutions — 10-03-05 Planetary GPR: MARSIS, SHARAD and Lunar Radar

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment. Where a problem has more than one defensible answer, that
> is said. Nothing here is a measurement; all models are **SYNTHETIC**.

Lesson: [05 Planetary GPR: MARSIS, SHARAD and Lunar Radar](../05-gpr-planetary.md).
Constants: $c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$\varepsilon_{\mathrm{ice}} = 3.17$, $\varepsilon_{\mathrm{water}} = 80.1$,
$e = 1.602176634\times10^{-19}\ \mathrm{C}$,
$\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$,
$m_e = 9.1093837015\times10^{-31}\ \mathrm{kg}$.

---

## ★1 — Bandwidth and resolution

$$\Delta t = \frac{1}{B} = \frac{1}{5\times10^{6}} = 2.0\times10^{-7}\ \mathrm{s}
= 0.200\ \mu\mathrm{s}.$$

$$\Delta r_{\mathrm{vac}} = \frac{c}{2B}
= \frac{2.99792458\times10^{8}}{2(5\times10^{6})} = 29.98\ \mathrm{m},$$

$$\Delta r_{\mathrm{ice}} = \frac{\Delta r_{\mathrm{vac}}}{\sqrt{3.17}}
= \frac{29.98}{1.78045} = 16.84\ \mathrm{m}.$$

Units: $\Delta t$ in s (reported in $\mu$s), $\Delta r$ in m. A bandwidth of
$5\ \mathrm{MHz}$ therefore resolves $16.8\ \mathrm{m}$ in ice — the number that
any claim of "layering" from such a sounding must be judged against.

---

## ★2 — Fresnel radius versus frequency

$$r_f = \sqrt{\frac{\lambda h}{2}}, \qquad \lambda = \frac{c}{f}.$$

At $5\ \mathrm{MHz}$: $\lambda = 59.958\ \mathrm{m}$,

$$r_f = \sqrt{\frac{59.958 \times 3\times10^{5}}{2}} = \sqrt{8.9937\times10^{6}}
= 2\,999\ \mathrm{m}.$$

At $20\ \mathrm{MHz}$: $\lambda = 14.990\ \mathrm{m}$,

$$r_f = \sqrt{\frac{14.990 \times 3\times10^{5}}{2}} = \sqrt{2.2484\times10^{6}}
= 1\,499\ \mathrm{m}.$$

Ratio: $2999/1499 = 2.000$.

**Frequency dependence.** $\lambda \propto 1/f$, so
$r_f \propto \sqrt{\lambda} \propto f^{-1/2}$: quadrupling the frequency (from
$5$ to $20\ \mathrm{MHz}$) halves the footprint. It is worth being explicit that
this is *not* the $1/f$ scaling that the range resolution has
($\Delta r = c/(2B\sqrt{\varepsilon_r})$ is independent of frequency and depends
only on the bandwidth): a narrow-band high-frequency radar can have a small
footprint and a coarse range resolution at the same time, because the two are
governed by different parameters.

---

## ★3 — Clutter geometry

$$x = \sqrt{2hd\sqrt{\varepsilon_r}}
= \sqrt{2(3\times10^{5})(50)(1.78045)}
= \sqrt{5.3414\times10^{7}} = 7\,309\ \mathrm{m} \approx 7.31\ \mathrm{km}.$$

A surface echo from $7.3\ \mathrm{km}$ off nadir arrives at the same time as the
subsurface interface at $50\ \mathrm{m}$, so **delay alone cannot distinguish a
$50\ \mathrm{m}$ depth from a $7.3\ \mathrm{km}$ horizontal distance.** The
discrimination has to come from where the echo focuses (along-track Doppler) and
from its statistics (specular versus speckled).

---

## ★4 — Two models, one observation

$$d_A = \frac{c\,\Delta t}{2\sqrt{\varepsilon_A}}
= \frac{(2.99792458\times10^{8})(30.0\times10^{-6})}{2(1.78045)}
= \frac{8\,993.8}{3.5609} = 2\,525.7\ \mathrm{m},$$

$$d_B = \frac{8\,993.8}{2\sqrt{4.00}} = \frac{8\,993.8}{4} = 2\,248.4\ \mathrm{m}.$$

Difference: $2\,525.7 - 2\,248.4 = 277.3\ \mathrm{m}$, i.e. $10.98\%$ of model A.

**Matching the amplitude.** The two-way loss is $2\alpha d$, so equal amplitudes
require $\alpha_B d_B = \alpha_A d_A$:

$$\alpha_B = \alpha_A\frac{d_A}{d_B} = 0.005 \times \frac{2\,525.7}{2\,248.4}
= 0.005617\ \mathrm{dB\,m^{-1}}.$$

So the pair (3.17, 2525.7 m, 0.00500 dB/m) and (4.00, 2248.4 m, 0.00562 dB/m)
produce identical two-way times **and** identical echo amplitudes, and their
depths differ by $277\ \mathrm{m}$. This is the central non-uniqueness of
planetary sounding: the time gives $d\sqrt{\varepsilon_r}$, the amplitude gives
$\alpha d$, and neither gives $d$ alone.

**What breaks it.** An independent constraint on $\varepsilon_r$: an absolutely
calibrated surface echo (which gives the surface permittivity from
$R = (1-\sqrt{\varepsilon_r})/(1+\sqrt{\varepsilon_r})$), a laboratory analogue
material measured at the relevant frequency and temperature, or a known thickness
from an independent measurement.

---

## ★5 — Ionospheric delay

$$\Delta\ell = \frac{40.3\,\mathrm{TEC}}{f^{2}}
= \frac{40.3 \times 5\times10^{15}}{(2\times10^{7})^{2}}
= \frac{2.015\times10^{17}}{4\times10^{14}}
= 503.75\ \mathrm{m}.$$

That is the excess path **per leg**, so:

- the one-way range bias is $503.75\ \mathrm{m}$ — an altitude derived from the
  surface echo is wrong by half a kilometre;
- the round-trip time delay is
  $2(503.75)/c = 3.36\ \mu\mathrm{s}$.

**Differential delay across the band.**

$$\Delta(\Delta\ell) = 40.3\,\mathrm{TEC}
\left(\frac{1}{f_1^{2}}-\frac{1}{f_2^{2}}\right)
= 2.015\times10^{17}\left(\frac{1}{2.25\times10^{14}}
- \frac{1}{6.25\times10^{14}}\right),$$

$$\frac{1}{15^{2}} - \frac{1}{25^{2}} = 4.4444\times10^{-15}
- 1.6000\times10^{-15} = 2.8444\times10^{-15}\ \mathrm{Hz^{-2}},$$

$$\Delta(\Delta\ell) = 2.015\times10^{17} \times 2.8444\times10^{-15}
= 573.2\ \mathrm{m}.$$

**Comparison.** The range resolution of a $10\ \mathrm{MHz}$ bandwidth in ice is
$8.42\ \mathrm{m}$, so the differential delay is

$$\frac{573.2}{8.42} = 68.1$$

times the resolution. **An uncorrected interface is smeared over $68$ resolution
elements**, i.e. it is not a delayed event but a longer, weaker ramp. This is why
the correction is not a refinement but a precondition: without it, a $10\
\mathrm{MHz}$ sounding of a dispersive plasma produces no interpretable echo at
all, however good the hardware.

---

## ★6 — Which limit binds?

**Attenuation limit:**

$$d = \frac{60}{2\alpha} = \frac{60}{2(0.02)} = 1\,500\ \mathrm{m}.$$

**Clutter limit** within an along-track window $W = 500\ \mathrm{m}$:

$$d = \frac{W^{2}}{2h\sqrt{\varepsilon_r}}
= \frac{(500)^{2}}{2(3\times10^{5})(1.78045)}
= \frac{2.5\times10^{5}}{1.0683\times10^{6}} = 0.234\ \mathrm{m}.$$

**Which binds?** The clutter limit, by three orders of magnitude. The reading is
subtle and worth stating carefully: it does *not* mean clutter prevents sounding
below $0.23\ \mathrm{m}$; it means that **range alone** cannot distinguish a
subsurface echo from off-nadir surface clutter beyond that depth, so every deeper
interpretation depends on the along-track (Doppler) discrimination working. If the
sounder is coherent and the clutter is spatially incoherent, the effective
clutter-free depth is far greater than $0.23\ \mathrm{m}$ — but that is a property
of the processing and of the terrain, not of the range geometry, and it must be
demonstrated rather than assumed. With a warmer, wetter target
($\alpha \gg 0.02\ \mathrm{dB\,m^{-1}}$) the attenuation limit falls below the
clutter limit and the absorption becomes the binding constraint instead.

---

## ★7 — A discrimination test for a $200\ \mathrm{m}$ echo

**The candidate.** A subsurface interface at $200\ \mathrm{m}$ in ice implies a
clutter-equivalent off-nadir distance

$$x = \sqrt{2hd\sqrt{\varepsilon_r}}
= \sqrt{2(3\times10^{5})(200)(1.78045)}
= \sqrt{2.1365\times10^{8}} = 14\,617\ \mathrm{m} \approx 14.6\ \mathrm{km}.$$

**Observable 1 — along-track focusing.** A nadir subsurface interface has zero
Doppler at the closest-approach point and a range-rate history set by the
orbiter's motion relative to a *fixed* target in the body-fixed frame. An off-nadir
surface patch at $14.6\ \mathrm{km}$ has a different range-rate history (larger,
and of opposite sign on the other side of nadir) and, critically, it moves with the
surface while a subsurface interface does not. The test: migrate/coherently
integrate each candidate separately with the two hypotheses and compare the
resulting peak amplitudes. A correct hypothesis focuses; a wrong one does not.

**Observable 2 — scattering statistics.** A specular interface produces a
*coherent* echo whose power is stable from orbit pass to pass and whose amplitude
does not fluctuate much within a footprint. Surface clutter is a sum of many
independent scatterers, so its amplitude is Rayleigh-distributed: at any single
look the power varies by a factor of several, and averaging reduces it
predictably. The test: compare the amplitude's variance with the two hypotheses'
predictions.

**Sample size.** For a Rayleigh amplitude, a power estimate has a relative
standard deviation $1/\sqrt{N}$ for $N$ independent looks. To distinguish a coherent
return (whose fluctuation is set by the system's SNR, say $10\%$) from a Rayleigh
one (relative standard deviation $52\%$ for a single look) at $5\sigma$, with a
$30\%$ difference to resolve, requires of order

$$N \approx \left(\frac{5 \times 0.52}{0.30}\right)^{2} \approx 75$$

independent looks, i.e. roughly $75$ independent footprints — not $75$ samples,
since adjacent samples within a footprint are correlated. At a $1.5\
\mathrm{km}$ footprint this means of the order of $100\ \mathrm{km}$ of along-track
data, which is a realistic single-pass requirement and an unrealistic one for a
single short segment.

**Two ways the test fails.**
1. **A rough subsurface interface.** If the interface itself is rough (a
   subglacial bed is), it is also Rayleigh-distributed and both hypotheses look
   alike. The failure is fundamental, not statistical.
2. **Focused clutter.** If the surface topography contains a facet whose range-rate
   accidentally matches the subsurface hypothesis within the integration time, the
   focus test alone is fooled. This is why the geometry ($x = 14.6\
\mathrm{km}$ here) and the geology of that annulus — is there a scarp, a ridge, a
   crater rim? — must be examined before an amplitude-based conclusion is accepted.

---

## ★8 — The dispersion constant, derived

$$\omega_p^{2} = \frac{n_e e^{2}}{\varepsilon_0 m_e},$$

$$\frac{e^{2}}{\varepsilon_0 m_e}
= \frac{(1.602176634\times10^{-19})^{2}}
{(8.8541878128\times10^{-12})(9.1093837015\times10^{-31})}
= \frac{2.56697\times10^{-38}}{8.06536\times10^{-42}}
= 3.1827\times10^{3}\ \mathrm{m^{3}\,s^{-2}},$$

$$\omega_p = \sqrt{3.1827\times10^{3}\,n_e} = 56.405\sqrt{n_e}
\ \mathrm{rad\,s^{-1}},$$

$$f_p = \frac{\omega_p}{2\pi} = \frac{56.405}{6.28319}\sqrt{n_e}
= 8.9772\sqrt{n_e}\ \mathrm{Hz} \approx 8.98\sqrt{n_e}.$$

Then the group-index expansion $n_g \simeq 1 + \tfrac{1}{2}(f_p/f)^{2}$ gives an
excess path

$$\Delta\ell = \frac{1}{2}\frac{f_p^{2}}{f^{2}}L
= \frac{1}{2}\frac{(8.98)^{2}n_e L}{f^{2}}
= \frac{(1/2)(8.98)^{2}\,\mathrm{TEC}}{f^{2}}
= \frac{40.32\,\mathrm{TEC}}{f^{2}},$$

which is the standard $40.3\,\mathrm{TEC}/f^{2}$ to the rounding of the constant.
**Agreement.** With $f_p/f = 2.840/20 = 0.14200$ and $L = 100\ \mathrm{km}$:

$$\text{slab form: } \frac{1}{2}(0.14200)^{2}(10^{5}) = 1\,008.0\ \mathrm{m},$$

$$\text{TEC form using } 40.3:\ \frac{40.3(10^{16})}{(2\times10^{7})^{2}}
= 1\,007.5\ \mathrm{m},$$

a difference of $0.05\%$, which is exactly the difference between $40.30$ and
$40.32$ — i.e. the agreement measures the constants, not the plasma.

**Next term.** $(3/8)(f_p/f)^{4}L = 0.375 \times (0.14200)^{4} \times 10^{5}
= 0.375(4.0650\times10^{-4})(10^{5}) = 15.2\ \mathrm{m}$.

Against a $15.0\ \mathrm{m}$ range resolution **this is exactly one resolution
element**: the neglected term in the ionospheric model is the same size as the
resolution of the instrument, so it cannot be dismissed as "second order and
therefore irrelevant". It is 1.5% of the delay but 100% of a resolution cell —
a good illustration that an error is judged against the requirement, not against
the size of the thing it corrects.

---

## ★9 — Assessing a reported $30\ \mathrm{m}$ layer

**Resolution.** At $B = 10\ \mathrm{MHz}$ in ice:

$$\Delta r = \frac{c}{2B\sqrt{\varepsilon_r}} = \frac{2.99792458\times10^{8}}
{2(10^{7})(1.78045)} = 8.42\ \mathrm{m}.$$

So the reported $30\ \mathrm{m}$ is $3.6$ resolution elements. That is *not*
automatically wrong: two interfaces $30\ \mathrm{m}$ apart are resolvable in
principle. But three things must hold, and each is a condition rather than a
property of the number:

1. **Both interfaces must actually produce detectable echoes.** A weak internal
   reflection $30\ \mathrm{m}$ below a strong one may be visible; $30\ \mathrm{m}$
   below a *very* strong one is inside its sidelobe structure, and the second event
   may be a wavelet sidelobe rather than a layer.
2. **The wavelet must be short enough in time.** $\Delta r = 8.42\ \mathrm{m}$
   corresponds to a two-way time of
   $2(8.42)/v = 2(8.42)/(1.6838\times10^{8}) = 100\ \mathrm{ns}$; a "four-sample"
   wavelet of a $10\ \mathrm{MHz}$ band is about $400\ \mathrm{ns}$, i.e.
   $34\ \mathrm{m}$ — so the reported layer is barely longer than the wavelet
   itself. That is precisely the regime where a thickness must come from
   waveform modelling.
3. **The permittivity must be right**, or the thickness scales with
   $1/\sqrt{\varepsilon_r}$: a $5\%$ error in $\varepsilon_r$ moves $30\ \mathrm{m}$
   by $0.74\ \mathrm{m}$, which is small here, but the same $5\%$ error also
   validates the resolution statement.

**What the detection actually rests on.** A composite waveform whose shape differs
from a single-interface response, fitted with the exact layered forward model of
the previous lessons, with the source wavelet known and the permittivity
constrained. The $30\ \mathrm{m}$ number is then a *model parameter*, with an
admitted range that comes from the fit's correlation structure (thickness and
contrast trade, as in the pavement thin-layer case) — not a measurement.

**What would raise it to a measurement.** Either a wider bandwidth (to push
$\Delta r$ well below $30\ \mathrm{m}$, at the cost of penetration), or an
independent constraint on the layer thickness from a second geometry — a
bistatic or off-nadir sounding whose path length through the layer differs, so the
two geometries separate thickness from contrast. Short of one of those, the honest
statement is a range: for example "$20$–$45\ \mathrm{m}$, conditional on
$\varepsilon_r = 3.17$ and on the assumed base contrast".
