# Solutions — 14-02-07 Borehole Geophysics for Aquifer Characterisation

> **Read after attempting the exercises.** Arithmetic is shown in full. All logs,
> units and calibrations are **SYNTHETIC**.

Lesson: [07 Borehole Geophysics for Aquifer Characterisation](../07-borehole-hydrogeophysics.md).

Constants: $\rho_{\text{matrix}} = 2650$, $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$;
the conversion from permeability in m² to hydraulic conductivity in m s$^{-1}$ is
$$\frac{\rho_w g}{\mu} = \frac{(1000)(9.81)}{1.002 \times 10^{-3}}
= 9.79 \times 10^{6}\ \mathrm{m^{-1}\,s^{-1}}$$
(equivalently $k\ [\mathrm{m\,d^{-1}}] = k\ [\mathrm{m^2}] \times 9.79 \times 10^{6}
\times 86\,400$).

---

## ★1 — Clay volume from gamma

$$V_{\text{clay}} = \frac{\mathrm{GR} - 30}{150}.$$

| unit | GR (API) | $V_{\text{clay}}$ |
|---|---|---|
| 1 | 45 | $(45-30)/150 = \mathbf{0.10}$ |
| 2 | 60 | $(60-30)/150 = \mathbf{0.20}$ |
| 3 | 190 | $(190-30)/150 = 1.067 \rightarrow$ **clipped to 1.0** |

**Which is the confining layer.** Unit 3 retains only water held on clay surfaces and
in micropores, has negligible permeability, and is the confining layer.

**What the third value means physically.** The computed 1.067 is **outside the
calibration's physical range**: the unit emits *more* gamma radiation than the pure-clay
end member used to define the 0-1 scale, so the linear mapping cannot describe it.
Physically the unit is not "107% clay"; rather, it either (i) contains more
potassium/thorium per unit volume than the calibration end member (heavy minerals,
mica, or a different clay mineralogy such as illite versus kaolinite), or (ii) the
logging calibration's scale is slightly off. The lesson's own demo makes the same
point from the other direction: a gamma *response* and its *inversion* must be
scale-matched (`GR = 30 + 150 Vclay` against `(GR-30)/150`), because a mismatched
scale makes every estimate saturate at 0 or 1 — and saturation is therefore the
signature of a calibration error, not of an extreme lithology. The correct response
is to cap the value, plot it, and then recalibrate against cores or cross-check with
a spectral gamma log, not to report 1.067.

---

## ★2 — Density porosity

$$\phi = \frac{\rho_{\text{matrix}} - \rho_b}{\rho_{\text{matrix}} - \rho_w}
= \frac{2650 - \rho_b}{2650 - 1000} = \frac{2650 - \rho_b}{1650}.$$

| unit | $\rho_b$ (kg m$^{-3}$) | numerator | $\phi$ |
|---|---|---|---|
| 1 | 2130 | 520 | $520/1650 = \mathbf{0.3152}$ |
| 2 | 2200 | 450 | $450/1650 = \mathbf{0.2727}$ |
| 3 | 2450 | 200 | $200/1650 = \mathbf{0.1212}$ |

**Most pore volume: unit 1** ($\phi = 0.3152$), with unit 3 by far the least
(0.1212) — consistent with unit 3 being clay-rich but dense because its pores are
filled with bound water and its grains are platy and tightly packed.

**Caveats worth stating.** The density porosity assumes (i) a known matrix density
(2650 is a convention for quartz-rich rock; a calcite-cemented unit would be 2710 and
the porosities would shift by up to 0.06), (ii) water-filled pores — any gas lowers
$\rho_b$ and inflates $\phi$, and (iii) no heavy minerals, which raise $\rho_b$ and
shrink $\phi$. This is exactly the assumption a cross-check against an independent
porosity is designed to test.

---

## ★3 — SDR permeability and the screening decision

$$k_{\text{SDR}} = C\phi^{4}T_2^{2}, \qquad C = 4.0 \times 10^{-9}\ \mathrm{m^2\,s^{-3}},
\qquad T_2\ \text{in seconds}.$$

**Unit 1** ($\phi = 0.315152$, $T_2 = 0.085$ s):
$$\phi^{2} = 0.0993207,\quad \phi^{4} = 9.86460 \times 10^{-3},\quad
T_2^{2} = 7.225 \times 10^{-3},$$
$$k = (4.0 \times 10^{-9})(9.86460 \times 10^{-3})(7.225 \times 10^{-3})
= 2.8509 \times 10^{-13}\ \mathrm{m^2},$$
$$k = (2.8509 \times 10^{-13})(9.7904 \times 10^{6})
= 2.7911 \times 10^{-6}\ \mathrm{m\,s^{-1}} = \mathbf{0.241\ m\,d^{-1}}.$$

**Unit 2** ($\phi = 0.272727$, $T_2 = 0.018$ s):
$$\phi^{4} = 5.53241 \times 10^{-3},\quad T_2^{2} = 3.24 \times 10^{-4},$$
$$k = (4.0 \times 10^{-9})(5.53241 \times 10^{-3})(3.24 \times 10^{-4})
= 7.1700 \times 10^{-15}\ \mathrm{m^2}
= 7.0197 \times 10^{-8}\ \mathrm{m\,s^{-1}} = \mathbf{0.00607\ m\,d^{-1}}.$$

**Unit 3** ($\phi = 0.121212$, $T_2 = 0.004$ s):
$$\phi^{4} = 2.15858 \times 10^{-4},\quad T_2^{2} = 1.6 \times 10^{-5},$$
$$k = (4.0 \times 10^{-9})(2.15858 \times 10^{-4})(1.6 \times 10^{-5})
= 1.3815 \times 10^{-17}\ \mathrm{m^2}
= 1.3526 \times 10^{-10}\ \mathrm{m\,s^{-1}} = \mathbf{1.17 \times 10^{-5}\ m\,d^{-1}}.$$

**Ratios:** unit 1 / unit 2 $= 39.8$; unit 1 / unit 3 $= 20\,640$.

**Screen unit 1.** Note *why*: it wins on both factors, the highest $\phi$ **and** the
longest $T_2$. $T_2$ enters squared while $\phi$ enters to the fourth power, so the
two are of comparable weight and a unit can lose on either — which is the point of the
lesson's silty-aquitard example, where the second-largest porosity in the suite
contributes almost nothing to the transmissivity because its pores are small.

**What the number is not.** $C = 4.0 \times 10^{-9}$ is a synthetic calibration. The
*ratios* (39.8, 20 640) are what the log delivers without calibration; the absolute
permeability requires $C$ to be fixed by a core or a pumping test, so the screen
decision is robust while the predicted yield is not.

---

## ★★4 — Archie saturation and the clipped clay

$$S_w = \sqrt{\frac{R_w}{\phi^{2}R_t}}, \qquad R_w = 5\ \Omega\,\mathrm{m},\
m = n = 2.$$

**Unit 1** ($\phi^{2} = 0.0993207$, $R_t = 220$):
$$\phi^{2}R_t = 21.8508,\qquad S_w = \sqrt{\frac{5}{21.8508}}
= \sqrt{0.228825} = \mathbf{0.478}.$$

**Unit 2** ($\phi^{2} = 0.0743802$, $R_t = 95$):
$$\phi^{2}R_t = 7.06612,\qquad S_w = \sqrt{\frac{5}{7.06612}}
= \sqrt{0.707601} = \mathbf{0.841}.$$

**Unit 3** ($\phi^{2} = 0.0146921$, $R_t = 18$):
$$\phi^{2}R_t = 0.264458,\qquad S_w = \sqrt{\frac{5}{0.264458}}
= \sqrt{18.9066} = \mathbf{4.35} \ \longrightarrow\ \text{clipped to } 1.0.$$

**Why 4.35 is not a saturation.** Water saturation cannot exceed 1; a value of 4.35
is a statement that the model is wrong, and the reason is the **physics of clay**
that Archie's equation omits. Archie assumes the only conducting path is the pore
water. In a clay, the mineral surfaces carry an excess negative charge balanced by a
mobile cation cloud (the cation-exchange capacity), and that cloud conducts *in
parallel* with the pore water. The measured $R_t$ is therefore far lower than the
Archie prediction, so the inversion, forced to blame the excess conductivity on more
water, returns an impossible saturation. The correct model adds a clay-conductivity or
exchange term (a shale-corrected saturation model) and uses a clay-volume estimate —
which for a clay unit is exactly the gamma reading from ★1.

**Why the appearance is still diagnostic.** $S_w > 1$ is a *useful alarm*: it says
the interpreter has supplied either (i) clay-rich rock, (ii) an $R_w$ that is too
high, (iii) a porosity that is too low (cement exponent $m$ wrong), or (iv) a
measurement problem. It cannot mean the formation is over-saturated. The demo makes
this concrete: with $R_w = 20\ \Omega$ m and $\phi = 0.32$ the *upper* row of the
$R_w$ sensitivity table clips at $S_w = 1.0000$, and the lesson's comment is that "a
log that reports full saturation almost always has the wrong $R_w$". Here the same
alarm fires one step further: **three** of the four candidate causes are visible in
the log suite itself (the gamma of ★1 says clay), so the inconsistency is resolved by
cross-referencing logs rather than by trusting either one.

---

## ★★5 — Packer test and the radius of influence

$$K = \frac{Q\ln(R/r_w)}{2\pi L\,\Delta h}, \qquad Q = 0.08\ \mathrm{L\,s^{-1}}
= 8.0 \times 10^{-5}\ \mathrm{m^3\,s^{-1}}.$$

**With $R = 50$ m, $r_w = 0.075$ m:**
$$\frac{R}{r_w} = \frac{50}{0.075} = 666.67,\qquad \ln 666.67 = 6.5023,$$
$$K = \frac{(8.0 \times 10^{-5})(6.5023)}{2\pi(3.0)(10.0)}
= \frac{5.2018 \times 10^{-4}}{188.496}
= 2.7597 \times 10^{-6}\ \mathrm{m\,s^{-1}} = \mathbf{0.238\ m\,d^{-1}}.$$

**Recomputing for other radii (everything else fixed):**

| $R$ (m) | $R/r_w$ | $\ln(R/r_w)$ | $K$ (m s$^{-1}$) | $K$ (m d$^{-1}$) | change vs $R = 50$ |
|---|---|---|---|---|---|
| 10 | 133.3 | 4.8929 | $2.0766 \times 10^{-6}$ | 0.1794 | $-24.8\%$ |
| 30 | 400.0 | 5.9915 | $2.5429 \times 10^{-6}$ | 0.2197 | $-7.9\%$ |
| 50 | 666.7 | 6.5023 | $2.7597 \times 10^{-6}$ | 0.2384 | — |
| 200 | 2666.7 | 7.8886 | $3.3480 \times 10^{-6}$ | 0.2893 | $+21.3\%$ |
| 1000 | 13 333 | 9.4980 | $4.0311 \times 10^{-6}$ | 0.3483 | $+46.1\%$ |

**Fractional error from the wrong radius.** Because $K$ is proportional to
$\ln(R/r_w)$, the fractional error is the ratio of the logarithms:
using $R = 10$ m instead of 50 m gives $4.8929/6.5023 = 0.7525$, i.e. $-24.8\%$; using
$R = 200$ m gives $7.8886/6.5023 = 1.213$, i.e. $+21.3\%$. A factor of 4 in $R$
(50 → 200 m) is worth about 21% here; in general the sensitivity depends on both
$R$ and $r_w$ through the ratio of logarithms (the classic illustration,
$\ln 400 = 5.99$ against $\ln 100 = 4.61$, gives 30%).

**What that implies for reporting.** The result must be reported as a *line*:
$K = 2.76 \times 10^{-6}\ \mathrm{m\,s^{-1}}$ **for the assumed $R = 50$ m**, with the
assumption stated, and with a sensitivity range of roughly
$2.1$–$3.3 \times 10^{-6}\ \mathrm{m\,s^{-1}}$ for $R$ between 10 and 200 m. Reporting
a bare number to three significant figures implies a precision the method does not
have (as the lesson puts it, the value "should be reported as a line"). Two further
points matter more than $R$: (i) the test must be **repeated at several heads** and
the plot of $Q$ against $\Delta h$ must be linear through the origin, because
curvature indicates non-Darcy flow near the hole or a leaking packer; and (ii) where
the formation is too tight for a steady test, a **slug test** should be used instead —
its analysis has no radius of influence at all.

---

## ★★6 — Temperature, $z^{*}$ and the flow detection

$$z^{*} = \frac{k_{\text{th}}}{\rho_w c_w v_z}
= \frac{2.0}{(4.18 \times 10^{6})(2.0 \times 10^{-8})}
= \frac{2.0}{0.0836} = \mathbf{23.92\ m},$$
and the velocity is $2.0 \times 10^{-8} \times 86\,400 = 1.73 \times 10^{-3}$ m d$^{-1}$
$= \mathbf{1.73\ mm\,d^{-1}}$ — a plausible regional recharge or drainage velocity.

$$T(z) = T_0 + Gz^{*}\left(1 - e^{-z/z^{*}}\right),\qquad
T_0 = 12.0\ ^\circ\mathrm{C},\ G = 0.025\ ^\circ\mathrm{C\,m^{-1}}.$$

**At 20 m** ($z/z^{*} = 20/23.92 = 0.83612$):
$$T = 12.0 + (0.025)(23.92)\left(1 - e^{-0.83612}\right)
= 12.0 + 0.5980\,(1 - 0.43343)
= 12.0 + 0.33881 = \mathbf{12.339\ ^\circ C}.$$

**At 50 m** ($z/z^{*} = 50/23.92 = 2.0903$):
$$T = 12.0 + 0.5980\,(1 - 0.12366) = 12.0 + 0.52405 = \mathbf{12.524\ ^\circ C}.$$

**Gradient at 20 m.** Differentiating,
$$\frac{\mathrm{d}T}{\mathrm{d}z} = G\,e^{-z/z^{*}}
= 0.025 \times 0.43343 = \mathbf{0.01084\ ^\circ C\,m^{-1}},$$
i.e. **43% of the no-flow gradient**.

**Sensitivity comparison.** With no flow the gradient is exactly
$0.0250\ ^\circ\mathrm{C\,m^{-1}}$; with 1.73 mm d$^{-1}$ of downward flow it is
0.01084, a **57% reduction** — a change far larger than a temperature log's
resolution (better than 0.01 °C with a calibrated probe). The suppression sets in
within one $z^{*}$, so a velocity an order of magnitude smaller raises $z^{*}$ to
239 m and halves the gradient only over hundreds of metres, while an order of
magnitude larger drops $z^{*}$ to 2.4 m and suppresses it within a few metres. The
diagnostic rule is therefore: **the depth over which the geothermal gradient is
suppressed measures $z^{*}$, and hence $v_z = k_{\text{th}}/(\rho_w c_w z^{*})$** —
but only if the thermal conductivity is known, since $z^{*}$ is proportional to it.
The log adds no survey cost because it runs in the same pass as the others, which is
why a temperature log is standard in any borehole hydrogeophysical programme.

---

## ★★★7 — Cross-hole monitoring: water content versus salinity

**Water content in the travel time.** From the lesson's table (12 m separation, CRIM
mixing with $\varepsilon_s = 4.5$, $\varepsilon_w = 81$, $\phi = 0.30$):

| water content | $\varepsilon_{\text{eff}}$ | $v$ (m ns$^{-1}$) | travel time over 12 m (ns) |
|---|---|---|---|
| 0.10 | 6.682 | 0.1160 | 103.47 |
| 0.30 | 17.514 | 0.0716 | 167.51 |

$$\frac{v_{0.30}}{v_{0.10}} = \frac{0.0716}{0.1160} = 0.6172
\Longrightarrow \textbf{velocity change} = -38.3\%,$$
$$\frac{t_{0.30}}{t_{0.10}} = \frac{167.51}{103.47} = 1.6189
\Longrightarrow \textbf{travel-time change} = +61.9\%.$$

So a 0.20 change in water content is a ~62% travel-time change — three orders of
magnitude larger than a typical arrival-time picking uncertainty of a fraction of a
percent, so **the travel time determines the water content, and it does so easily.**

**Salinity in the amplitude.** Salinity barely changes the permittivity of water but
raises its conductivity; the effect appears in the attenuation (exact lossy-dielectric
form, $\sigma_w = 0.15\,\mathrm{TDS}$ [g L$^{-1}$] S m$^{-1}$):

| TDS (mg L$^{-1}$) | $\sigma_w$ (S m$^{-1}$) | $\alpha$ at 50 MHz (dB m$^{-1}$) | one-way loss over 12 m (dB) | depth for 60 dB (m) |
|---|---|---|---|---|
| 500 | 0.075 | 24.6 | 295 | 2.44 |
| 5 000 | 0.750 | 102.3 | 1228 | 0.59 |
| 35 000 | 5.250 | 278.3 | 3340 | 0.22 |

For the 5 000 mg L$^{-1}$ case: $102.3\ \mathrm{dB\,m^{-1}} \times 12\ \mathrm{m}
= \mathbf{1227.7\ dB}$ of one-way loss across the inter-borehole interval, against a
realistic system dynamic range of about 60 dB. The depth over which 60 dB is consumed
is $60/102.3 = \mathbf{0.59\ m}$. **The radius of investigation is therefore measured
in centimetres**, and the recorded amplitude is a statement about the borehole wall,
not about the interval.

**Which parameter each measurement determines, and the design rule.**

| observable | sensitive to | determines |
|---|---|---|
| travel time | permittivity (through water content) | **water content** |
| attenuation/amplitude | conductivity | **salinity** (qualitatively, and only for very fresh contrasts) |
| cross-hole ERT (resistance) | conductivity | salinity, quantitatively, at the resolution of the electrode array |
| low-frequency cross-hole EM | conductivity | salinity, quantitatively |

The design rule follows from *which* parameter enters *which* quantity: water content
enters the velocity and therefore the travel time; salinity enters the loss term and
therefore the amplitude. Two consequences are worth stating explicitly.

1. **A monotonic but non-unique equivalence.** Lowering the water content and raising
   the salinity both raise the seismic/radar velocity contrast in *some* configurations
   — a dry, saline interval can mimic a wet, fresh one in the arrival time. Salinity
   must therefore be measured (by ERT or EM, or by sampling) rather than inferred from
   the amplitude alone, and caliper/borehole-fluid corrections applied.
2. **Method choice is set by frequency.** At 50 MHz a brine is opaque within 0.6 m;
   the *same* conductivity that makes salinity an easy electrical target makes it an
   impossible radar one. Salinity between boreholes is monitored with **cross-hole ERT
   and low-frequency cross-hole EM**, not with radar.

---

## ★★★8 — Verification versus validation

**(a) Density-porosity inversion** ($\rho_b = 2122.0$ kg m$^{-3}
\rightarrow \phi = 0.3200000000$, difference $0.00 \times 10^{0}$). *Verifies:* that
the forward and inverse density relations are algebraically consistent for a
water-saturated unit of known matrix density, i.e. that no term was dropped or
mis-signed in the implementation. *Does not verify:* that the matrix density of 2650
is the right value for the rock, nor that the pores contain water — the check uses the
same assumptions on both sides, so it is blind to all of them.

**(b) Temperature solution against its ODE** ($\max|k_{\text{th}}T'' -
\rho_w c_w v T'| = 6.8 \times 10^{-10}$ W m$^{-3}$ against a term magnitude of
$9.4 \times 10^{-4}$ W m$^{-3}$, a relative residual of $7.3 \times 10^{-7}$, set by
the second-order finite difference). *Verifies:* that the analytic solution printed in
the demo really satisfies the steady advection-diffusion equation being quoted — the
derivation and the code agree. *Does not verify:* that the equation is the right model
of the borehole's thermal state (it assumes steady state, no radiogenic production, a
single vertical velocity and a constant $k_{\text{th}}$).

**(c) Flowmeter closure** (increments sum to the pumped 5.00 L s$^{-1}$ at a 1.0%
error, and each increment is non-negative). *Verifies:* that the cumulation is
consistent with the pumped rate, and — the informative part — that the *increments*
are physically admissible. A negative increment is impossible and flags a noisy
spinner calibration, a changing hole diameter, or a packer/flow bypass. *Does not
verify:* that the spinner's depth is correct, or that the flow is radial; it closes by
construction if the increments are accumulated, so the closure test is a weak
consistency check and the sign test is the strong one.

**What none of the three can verify.** They are all internal-consistency checks of
models against their own algebra. None can establish that the *interpretation* — that
this interval is the aquifer, that its $K$ is what the packer says, that the
resistivity-derived saturation is meaningful — is true. The physical non-uniqueness is
not numerical: the same gamma, density, resistivity and NMR readings are produced by a
family of (clay content, salinity, porosity, $S_y$) combinations, as ★★4 shows in the
most brutal possible way (three of four candidate causes for one impossible number).

**A validation: a pumping test with observation wells.** Pump the well completed in
the candidate interval at a known rate for several days and measure drawdown in two or
three observation piezometers at different distances. This validates the
*interpretation* rather than the code, and it catches what (a)–(c) cannot:

- **the wrong screen interval** — if the drawdown response is that of a much thinner
  or much less permeable interval than the logs predicted, the flowmeter's inflow
  distribution and the NMR permeability ranking were misread;
- **an absolute permeability error** — the pumping test measures $T$ over tens of
  metres, so it calibrates the SDR constant $C$ in situ, converting the log's *ratio*
  information into an absolute prediction and exposing any bias (in this synthetic
  suite the flowmeter shows 61% of the inflow arriving between 10 and 22 m, so a well
  screened over the whole logged interval would systematically underpredict
  transmissivity);
- **a boundary or leakage effect** — a confining unit that leaks, or constant-head
  recharge at a nearby river, changes the drawdown shape and would invalidate the
  steady-state packer interpretation;
- **an $R_w$/Archie bias**, since the test's fitted storativity and the observed
  drawdown are compared with the saturation-weighted porosity from the logs.

The honest caveat: even a pumping test validates only the *volume* it samples. An
aquifer whose properties change by an order of magnitude laterally — the common case —
requires the geophysics to interpolate between wells, which is exactly why the
borehole interpretation must be tied to the surface methods of this module rather than
being read on its own.

---

## Module mastery checkpoint, parts (d)–(f)

**Part (d).** The two observations are **consistent and mutually reinforcing**. The
flowmeter puts 61% of the inflow in 10–22 m, i.e. in the sandy aquifer identified by
the gamma log ($V_{\text{clay}} \approx 0.05$–$0.08$), while the 24–32 m unit is
clay-rich ($V_{\text{clay}} \approx 0.45$) and contributes almost nothing to the
transmissivity despite having the second-largest porosity in the suite — the lesson's
SDR integration gives 5.17 m² d$^{-1}$ for the 6–24 m sand against 0.08 m² d$^{-1}$ for
the 24–32 m aquitard.

A well screened across the whole logged interval would **over-estimate the effective
thickness of the producing aquifer** and therefore **under-estimate the permeability**
attributed to it: the same total yield would have to be carried by a screen length
several times the 12 m that actually produces. Concretely, if the specific capacity of
a fully screened well were inverted with the full screen length, the inferred $K$ would
be too low by roughly the ratio of the screen length to the effective producing length
(here about 42 m of screen against 12 m of producer), and the design would look
marginal when it is not. This is the practical reason the flowmeter log is the arbiter:
it is the only measurement that says **which** interval produces water, and therefore
which interval the completion should isolate.

**Part (e).** Water content 0.10 → 0.30 over a 12 m separation:
$$\frac{v_{0.30}}{v_{0.10}} = \frac{0.0716}{0.1160} = 0.6172
\ (\text{velocity} - 38.3\%),$$
$$\frac{t_{0.30}}{t_{0.10}} = \frac{167.51}{103.47} = 1.6189
\Longrightarrow \textbf{travel time} + 61.9\%.$$

For salinity (5 000 mg L$^{-1}$, $\sigma_w = 0.75$ S m$^{-1}$) at 50 MHz:
$$\alpha = 102.3\ \mathrm{dB\,m^{-1}}
\Longrightarrow \text{one-way loss over 12 m} = 102.3 \times 12
= \mathbf{1227.7\ dB},$$
against a realistic 60 dB dynamic range — the 60 dB depth is only 0.59 m.

**Method for the salinity: cross-hole ERT** (with low-frequency cross-hole EM as the
alternative). Radar fails because the same conductivity that makes the brine an easy
electrical target makes it an absorbing medium; the travel time, being controlled by
permittivity, is blind to it.

**Part (f).** An Archie saturation above 1 has four candidate causes:

1. **clay conduction** (surface/cation-exchange conduction in parallel with the pore
   water), which is the most likely in a unit the gamma log calls clay-rich;
2. an **$R_w$ that is too high** (the classic case — the lesson's demonstration shows a
   log reporting full saturation when $R_w$ is doubled);
3. a **porosity that is too low**, i.e. a wrong matrix density or a wrong cementation
   exponent $m$;
4. a **measurement problem** — a bad $R_t$ from an uncalibrated tool, an uncorrected
   borehole-fluid or invasion effect, or an interval that is not water-filled at all
   (gas or hydrocarbon).

**The measurement that decides between them:** a **water sample for $R_w$** (with a
temperature measurement, since $R_w$ is strongly temperature-dependent) together with
the **gamma log** that says whether the unit is clay-rich. If $R_w$ from the sample is
consistent with the log and the unit has high gamma, the cause is clay conduction and
the fix is a clay-corrected saturation model using the $V_{\text{clay}}$ from ★1; if
the unit has low gamma and $R_w$ differs from the assumed value, the cause is the
wrong $R_w$ and the fix is the sample. Either way the answer comes from a *different*
measurement, not from re-fitting the same resistivity data — the theme of this module.
