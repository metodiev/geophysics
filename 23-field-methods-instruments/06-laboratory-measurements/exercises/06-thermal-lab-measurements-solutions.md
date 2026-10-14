# Solutions — 23-06-06 Thermal Conductivity, Diffusivity and Specific Heat

The lesson is [06 Thermal Laboratory Measurements](../06-thermal-lab-measurements.md). All
values are **SYNTHETIC**.

## ★1

$$q = K_{\text{ref}}\frac{\Delta T_{\text{ref}}}{\Delta x_{\text{ref}}}
= 2.00 \times \frac{5.0}{0.0120} = 833.33\ \mathrm{W/m^{2}},$$

$$K = \frac{q\,\Delta x}{\Delta T} = \frac{833.33 \times 0.0200}{7.5}
= 2.2222\ \mathrm{W/(m\,K)} .$$

A 0.5 K error on a 7.5 K drop is $0.5/7.5 = 6.667$ %, so
$\delta K = 0.0667 \times 2.2222 = 0.1481$ W/(m·K). This is the lesson's central point in
one number: the *apparatus* may be excellent and the result still carry 6.7 % because the
temperature drop across a short specimen is small. The fix is a larger drop (a bigger
specimen or a higher flux), not a better voltmeter.

## ★2

$$K(0) = 2.5000,\qquad K(100) = 2.5000 - 0.2000 = 2.3000,\qquad
K(300) = 2.5000 - 0.6000 = 1.9000\ \mathrm{W/(m\,K)} ,$$

i.e. **−8.00 %** at 100 °C and **−24.00 %** at 300 °C. A heat-flow calculation that uses the
surface value over a section reaching 300 °C therefore overestimates the flux by roughly the
average of those reductions, which is why the conductivity is fitted as a function and
integrated rather than quoted as a single number.

## ★3

$$c_p = \frac{Q}{m\Delta T} = \frac{95.0}{0.150 \times 2.10}
= 301.587\ \mathrm{J/(kg\,K)},$$

$$\alpha = \frac{K}{\rho c_p} = \frac{2.30}{2700 \times 301.587}
= 2.8246\times10^{-6}\ \mathrm{m^{2}/s},$$

$$e = \sqrt{K\rho c_p} = \sqrt{2.30 \times 2700 \times 301.587}
= 1368.5\ \mathrm{J/(m^{2}\,K\,s^{0.5})} .$$

Because $\alpha = K/(\rho c_p)$ is a product and a quotient, the relative uncertainties
combine in quadrature:

$$\frac{\delta\alpha}{\alpha} = \sqrt{1.0^{2} + 0.2^{2} + 1.428^{2}}\ \%
= \sqrt{3.079}\ \% = 1.755\ \% .$$

So a diffusivity quoted as "2.82 × 10⁻⁶ m²/s" should carry ±1.8 %, dominated by the
specific heat. Note that $\alpha$ is *more* uncertain than the best of its inputs and *less*
than the worst: quadrature is not a licence to quote a single term.

## ★4

$$\mathrm{erfc}\left(\frac{z}{2\sqrt{\alpha t}}\right) :$$

| $t$ | $2\sqrt{\alpha t}$ | Argument | erfc | Perturbation (4.0 K step) |
|---|---|---|---|---|
| 200 yr | 158.9 m | 0.9440 | 0.1818 | 0.7274 K |
| 1000 yr | 355.3 m | 0.4222 | 0.5505 | 2.2018 K |

The **200-year** perturbation (0.73 K at 150 m) is the one that matters for a heat-flow
interpretation, because it is small in absolute terms but *is* the residual of a recent
surface change; it must be modelled or the profile interpreted with a larger uncertainty. The
**1000-year** perturbation (2.20 K) is a climate signal in its own right and, more
importantly, it means the profile's shape at 150 m is dominated by the surface history
rather than by the deep flux. Both are the same calculation with different times, which is
why a borehole is simultaneously a heat-flow instrument and a palaeothermometer, and why a
study must state which of the two it is interpreting.

## ★5

$$\text{arithmetic} = (1-\phi)K_m + \phi K_f = 0.85(4.0) + 0.15(0.6) = 3.4900,$$

$$\text{geometric} = K_m^{1-\phi}K_f^{\phi} = 4.0^{0.85} \times 0.6^{0.15}
= 3.0094,$$

$$\text{harmonic} = \left(\frac{1-\phi}{K_m} + \frac{\phi}{K_f}\right)^{-1}
= \left(\frac{0.85}{4.0} + \frac{0.15}{0.6}\right)^{-1} = 2.1622\ \mathrm{W/(m\,K)} .$$

The bounds span $3.4900/2.1622 = 1.6141$, i.e. **61.41 %**, while the geometric mean lies
only **24.77 %** below the matrix value. The spread is therefore **2.48 times** the effect
the porosity produces — the same conclusion as the lesson: for an unmeasured rock the honest
statement is the *range*, and the choice of mixing law must be justified by a measurement on
a similar rock, not by convention.

## ★6

A model answer.

**Conductivity measurement.** Use the **divided bar with a thickness series** (two or three
specimens of the same material at 10, 15 and 20 mm) so that the contact resistance is
eliminated by extrapolation to zero thickness — the thermal analogue of the two-length
ultrasonic calibration. Measure at **20, 60, 100 and 150 °C** so that the temperature
dependence is fitted, not assumed, and guard the stack thermally. Specimen diameter large
compared with the grain size; faces ground parallel. A separate check measurement by a
transient method on two plugs is worth it as an independent route.

**How many specimens.** Twelve plugs give a between-specimen standard deviation (for a
sedimentary section, realistically 10–20 % of the value, because lithology varies). That
variability, not the instrument, sets the achievable precision: with 12 plugs the standard
error is $\sigma/\sqrt{12}$. If $\sigma$ is 15 % of the mean, the standard error is 4.3 % —
already near the 5 % requirement — so **the 5 % target is a statement about the *section
mean* and not about individual plugs**, and that must be said. More plugs, or a
lithology-weighted sampling design, is what would improve it, not a better instrument.

**$c_p$ and $\alpha$.** Not needed for a steady-state heat-flow calculation, which requires
only $K$ and the gradient: $q = K\,\mathrm{d}T/\mathrm{d}z$. They are needed if the
temperature field is *transient* (a surface-history correction, a basin thermal history) and
then $\alpha$ is the governing parameter. The deliverable for this project is $K(T)$ and the
gradient; $c_p$ on 3 plugs is enough for the auxiliary modelling, and it must be measured on
the same lithologies.

**Temperature gradient.** A 0.02 K resolution over 1 m spacing is 0.02 K/m per interval; if
the gradient is 25 K/mK (25 mK/m), a single interval carries 0.8 % — but the *real*
uncertainty comes from (i) the log's depth calibration, (ii) the borehole's thermal
perturbation from drilling and circulation, and (iii) the interval selection. The standard
practice is a **least-squares gradient over multiple intervals** in a "gradient interval" free
of convection and of obvious lithological contrast, giving a gradient uncertainty of a few
percent, reported with the interval.

**Budget for the heat flow.** $q = K\,\mathrm{d}T/\mathrm{d}z$:

| Term | Relative | Note |
|---|---|---|
| conductivity (instrument) | 2.0 % | temperature, geometry, contact series |
| conductivity (between specimens) | 4.3 % | 15 % variability over 12 plugs |
| gradient | 3.0 % | log resolution, interval choice |
| temperature-dependence of $K$ | 2.45 % | if $K(T)$ were ignored |
| **combined** | **≈6.2 %** | quadrature |

So the **5 % (95 %) target is not met by the budget as stated**: a 95 % half-width of
$2 \times 6.2 = 12.4$ % is the honest report, and to reach 5 % (95 %) — i.e. 2.5 % standard —
the between-specimen term must fall to about 2 %, which means **40–50 plugs** or a
lithology-weighted design, and the gradient interval must be chosen more carefully.

**The temperature dependence.** Over 2.5 km at 25 mK/m the section spans about 62 K; with a
−8 % per 100 °C coefficient the effect on $q$ is a couple of percent, i.e. comparable with
the requirement. It must be integrated, and measuring at four temperatures is enough to fit
a linear coefficient with a defensible uncertainty.

**What cannot be supported.** The **in-situ** heat flow as a single formation property: the
laboratory measures dry plugs at atmospheric pressure and room temperature; the formation is
saturated, under stress, and at temperature. Fluid saturation alone changes $K$ by tens of
percent, so the reported value is a matrix value with a stated saturation, and the in-situ
flux requires either in-situ measurements or a saturation correction that the programme has
not made. The honest deliverable is "$q = 62 \pm 8$ mW/m², from a matrix conductivity
measured dry, with the saturation correction not applied".
