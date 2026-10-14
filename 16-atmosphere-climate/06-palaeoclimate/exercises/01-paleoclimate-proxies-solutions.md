# Solutions — 16-06-01 Palaeoclimate Proxies: Ice Cores, Sediments, Isotopes

> Read after attempting the exercises. Lesson:
> [01 Palaeoclimate Proxies](../01-paleoclimate-proxies.md).

---

## ★1 — Delta notation

$$\delta = \left(\frac{R}{R_{\text{std}}}-1\right)\times1000
= (0.98-1)\times1000 = -20\ \text{per mil}.$$

The unit is parts per thousand (per mil), i.e. $10^{-3}$; $\delta$ is
dimensionless and is reported in per mil by convention.

---

## ★2 — Rayleigh distillation at $f = 0.5$

$$f^{\alpha-1} = 0.5^{\,0.00953} = e^{0.00953\ln 0.5}
= e^{-0.006606} = 0.993415.$$

$$\delta_v = (\delta_0+1000)f^{\alpha-1}-1000
= 988 \times 0.993415 - 1000 = 981.49 - 1000 = -18.51\ \text{per mil}.$$

$$\delta_c = \alpha(\delta_0+1000)f^{\alpha-1}-1000
= 1.00953 \times 981.49 - 1000 = 990.84 - 1000 = -9.16\ \text{per mil}.$$

Equivalently $\delta_c = \alpha(\delta_v+1000)-1000$. The demonstration's table
brackets this value between $f = 0.6$ ($-7.427$) and $f = 0.4$ ($-11.256$), which
is consistent with $-9.16$ at $f = 0.5$.

---

## ★3 — Checking the fractionation identity

$$\delta_c - \delta_v = (\alpha-1)(\delta_v+1000).$$

Right-hand side: $0.00953 \times 981.49 = 9.35$ per mil.
Left-hand side: $-9.16 - (-18.51) = 9.35$ per mil. ✔

The difference is the **equilibrium enrichment of the condensate over the
vapour**, and it is proportional to how heavy the vapour still is: as distillation
proceeds, $\delta_v$ becomes more negative, the vapour becomes isotopically
lighter, and each successive condensate is less enriched. That is precisely the
nonlinearity that makes a linear calibration range-dependent.

---

## ★4 — Calibration disagreement

Anchored at a reference point $(\delta_{\text{ref}}, T_{\text{ref}})$, a linear
calibration gives $T - T_{\text{ref}} = (\delta-\delta_{\text{ref}})/\text{slope}$.
For $\delta-\delta_{\text{ref}} = -10$ per mil:

$$T_A - T_{\text{ref}} = \frac{-10}{0.7863} = -12.72\ \mathrm{K},\qquad
T_B - T_{\text{ref}} = \frac{-10}{1.1329} = -8.83\ \mathrm{K}.$$

Difference: $12.72 - 8.83 = 3.89\ \mathrm{K}$ (equivalently
$10\,(1/0.7863 - 1/1.1329) = 10(1.2718-0.8827) = 3.89$). The two calibrations
disagree by nearly four kelvin on the same measurement, and the disagreement
grows linearly with the size of the excursion from the reference point.

---

## ★5 — Temperature uncertainty from source composition

$$\sigma_T = 8.33\ \frac{\mathrm{K}}{\text{per mil}} \times 1.5\ \text{per mil}
= 12.5\ \mathrm{K}.$$

That is two orders of magnitude larger than a typical regression standard error.
It is the reason a single-isotope temperature is a weak result unless the source
composition is independently constrained: in this synthetic model the source term
dominates the error budget entirely.

---

## ★6 — Curvature of the calibration

$$\frac{9.04}{4.58} = 1.97.$$

The isotope change per equal temperature step nearly **doubles** across the
cooling range. A single linear calibration must therefore be biased at both ends:
fitted in the middle, it over-states the temperature change in the warm part and
under-states it in the cold part (or the reverse, depending on the anchor). The
practical consequence is that a calibration's valid range must be reported, and
that applying a calibration outside the range over which it was fitted produces a
bias that grows with the extrapolation distance — see the same effect in
[16-05-04 Downscaling](../../05-climate-models/04-downscaling.md).

---

## ★7 — Reducing structural uncertainty (specification)

**Independent information needed.** A laboratory or field determination of
$\alpha(T)$ that does not rely on the same condensation-path assumption as the
calibration. Two routes: (i) laboratory equilibration experiments measuring the
fractionation factor between vapour and liquid (or ice) over a temperature range;
(ii) a natural site where temperature can be measured independently at the time
of deposition and the condensation path can be constrained — for example a
well-instrumented station with precipitation sampling and co-located
thermometry.

**How it would be used.** Replace the synthetic $\alpha(T)$ by the measured
relation, refit the calibration, and recompute the implied temperatures. The
demonstration's two parameterisations give a $5.07\ \mathrm{K}$ disagreement;
an independent $\alpha(T)$ collapses that particular term.

**Residual uncertainty.** The condensation-path assumption (immediate versus
partial removal of condensate), kinetic effects during rapid deposition,
post-depositional exchange, and the source composition all remain. Removing one
structural term does not make the calibration an instrument; it moves the
dominant uncertainty to the next item in the list.

---

## ★8 — Critique of a $\pm0.2\ \mathrm{K}$ uncertainty

**Omitted terms, in order of likely magnitude.**

1. **Fractionation-parameterisation (structural) uncertainty.** The
   demonstration measures $5.07\ \mathrm{K}$ between two internally consistent
   parameterisations — about $25$ times the quoted uncertainty.
2. **Source-composition uncertainty.** With a measured sensitivity of
   $8.33\ \mathrm{K}$ per per mil, even $\pm0.5$ per mil of source uncertainty
   contributes $\pm4.2\ \mathrm{K}$.
3. **Condensation-path assumption.** Whether the condensate is removed
   immediately, partly retained or re-evaporated changes the effective slope.
4. **Nonlinearity within the calibration range.** Section ★6 shows the per-kelvin
   response nearly doubling across a cooling range; a single slope mis-fits both
   ends.
5. **Age-model uncertainty.** Usually larger than the regression error and
   independent of it.
6. **Regression standard error.** The $\pm0.2\ \mathrm{K}$ quoted — a measure of
   how well the line fitted the training scatter, and not a measure of how well
   the model represents the process.

The correct statement therefore has a range of several kelvin and is dominated by
the modelling assumptions, not by the fit. Reporting $\pm0.2\ \mathrm{K}$ is not
merely optimistic; it asserts the wrong *kind* of uncertainty, because the
dominant term is structural and will not shrink with more samples.
