# Solutions — 14-06-01 Integrated Catchment Characterisation

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [01 Integrated Catchment Characterisation](../01-catchment-characterisation.md).

---

## ★1 — Water balance

$$\mathrm{ET} = P - Q - \Delta S = 807.6 - 159.2 - 19.6 = 628.8\ \mathrm{mm},$$

$$\frac{Q}{P} = \frac{159.2}{807.6} = 0.1971,
\qquad
\frac{\mathrm{ET}}{P} = \frac{628.8}{807.6} = 0.7786.$$

The two ratios sum to $0.9757$; the remaining 2.4% is the storage change, as it
must be. ✔

---

## ★2 — Recharge from a rise

$$R = S_y\Delta h = 0.08 \times 0.72 = 0.0576\ \mathrm{m} = 57.6\ \mathrm{mm},
\qquad
R = 0.12 \times 0.72 = 0.0864\ \mathrm{m} = 86.4\ \mathrm{mm}.$$

The ratio is $86.4/57.6 = 1.50$, exactly the ratio of the specific yields: the
method is a multiplication and inherits the full error of $S_y$.

Note also that the answer is the water added during the *rise*; the annual
recharge additionally includes whatever recharge is balanced by drainage during
the rise (the correction term in the lesson), so the uncorrected value is a lower
bound.

---

## ★3 — A refraction sounding

$$v_2 = \frac{1}{0.4000\ \mathrm{ms\,m^{-1}}} = 2500\ \mathrm{m\,s^{-1}},$$

$$\sin i_c = \frac{600}{2500} = 0.240, \quad i_c = 13.887^\circ,
\quad \cos i_c = 0.97077,$$

$$h = \frac{t_i v_1}{2\cos i_c} = \frac{(5.00\times10^{-3})(600)}{2(0.97077)}
= \frac{3.000}{1.94154} = 1.545\ \mathrm{m}.$$

If the direct branch were mis-read as 630 m/s, then
$\sin i_c = 0.252$, $\cos i_c = 0.96774$ and $h = 3.150/1.93548
= 1.628\ \mathrm{m}$ — a $+5.4\%$ depth error for a $+5\%$ velocity error. ✔

---

## ★4 — BFI reporting

From the lesson's table, BFI runs from **0.4488** at $\alpha = 0.990$ to
**0.6387** at $\alpha = 0.900$ — a factor 1.42 at fixed data, with the separated
total (318.4 mm) unchanged.

A reporting template that a reader could reproduce:

1. the discharge series and the period used (with units and the gauge datum);
2. the filter named (Lyne–Hollick one-parameter), the number of passes (two, one
   each direction, averaged) and the value of $\alpha$ used for the headline;
3. the BFI at that $\alpha$, to two decimals, with the *range* over a stated
   interval of $\alpha$ (for example 0.90–0.99);
4. the separated baseflow volume in mm and as a fraction of $Q$;
5. the independent low-flow evidence (a seepage run, a low-flow gauging) that
   constrains $\alpha$, or an explicit statement that there is none.

Without items 2 and 5 the BFI is not reproducible and not falsifiable.

---

## ★5 — Storage and its error budget

$$V = A h S_y = 15.0\times10^6 \times 3.2 \times 0.08
= 3.84\times10^6\ \mathrm{m^3} = 3.84\ \mathrm{Mm^3}.$$

- Thickness: $\Delta V_h = A S_y \sigma_h = 15.0\times10^6 \times 0.08
  \times 0.10 = 1.20\times10^5\ \mathrm{m^3} = 0.120\ \mathrm{Mm^3}$ (3.1%).
- Specific yield: $\Delta V_{Sy} = A h \sigma_{Sy} = 15.0\times10^6 \times 3.2
  \times 0.03 = 1.44\times10^6\ \mathrm{m^3} = 1.44\ \mathrm{Mm^3}$ (37.5%).

Fractional uncertainty:

$$\frac{\sigma_V}{V} = \sqrt{\left(\frac{0.10}{3.2}\right)^2
  + \left(\frac{0.03}{0.08}\right)^2}
= \sqrt{9.766\times10^{-4} + 0.140625} = 0.3762,$$

i.e. $V = 3.84 \pm 1.44\ \mathrm{Mm^3}$: **38%**. The specific yield dominates by a
factor $1.44/0.120 = 12$.

---

## ★6 — Implied storage for $b = 1.5$

$$S = \frac{Q^{2-b}}{a(2-b)}
= \frac{1.496^{0.5}}{3.7305\times10^{-2} \times 0.5}
= \frac{1.22311}{1.86525\times10^{-2}} = 65.58\ \mathrm{mm},$$

against 53.56 mm for the linear member — a factor 1.22 at the same data fit
(rms 0.23362 against 0.25866 mm/d, both within 7.5% of the initial flow).

$b = 1.5$ corresponds to $m = 2 - b = 0.5$, i.e. $S \propto \sqrt{Q}$ — a
reservoir whose outflow rises more slowly than linearly with storage. Physically
this is the signature of a **discharge that is throttled** rather than linear:
flow through a widening or deepening channel system, drainage of a profile with
strongly decreasing conductivity with depth, or outflow controlled by a
transmissivity that grows with the saturated thickness (a linearised Boussinesq
aquifer drains with an effective $b$ above 1). A homogeneous, unconfined,
constant-transmissivity aquifer with a deep water table behaves closer to the
linear member.

---

## ★7 — A storage volume to 10% (specification)

**Target.** $\sigma_V/V \le 0.10$ with
$(\sigma_V/V)^2 = (\sigma_h/h)^2 + (\sigma_{Sy}/S_y)^2$.

**Allocation.** If the two contributions are made equal, each must be
$0.10/\sqrt{2} = 0.0707$:

- thickness: $\sigma_h \le 0.0707 \times 3.2 = 0.23$ m if $h = 3.2$ m — trivially
  achievable by a refraction or MASW survey (the lesson's picking-limited sd was
  0.097 m) *provided* the spatial sampling is adequate;
- specific yield: $\sigma_{Sy} \le 0.0707 \times 0.08 = 0.0057$ — a 7%
  accuracy on $S_y$, which is the hard requirement.

**Methods for $S_y$.** Long-duration (multi-day to multi-week) pumping tests with
observation wells, interpreted for an unconfined aquifer's late-time behaviour;
a gravity or InSAR measurement of the storage change accompanying a measured
water-level change (the most direct route,
[14-02-06](../../02-hydrogeophysics-methods/06-gravity-for-groundwater.md));
laboratory drainage measurements on cores for the *shape* of the relation, tied
to field-scale values by the water-balance constraint. Expect two to four
multi-day tests, with the storage coefficient from each agreeing to better than
10%.

**Number of thickness sites.** For $h$ to be known to 0.23 m as a *catchment
mean*, the number of soundings is set by the lateral variance, not by the picking
error: with a point-to-point standard deviation of 1.2 m, about
$(1.2/0.23)^2 \approx 27$ sites are needed for the mean, spread over the
catchment's geomorphic units, unless a covariate (slope, topography, regolith
map) is used to stratify them.

**Residual risk.** The dominant remaining uncertainty is *support*: $S_y$ is
measured at the scale of a pump test, $h$ at the scale of a sounding, and the
product is quoted at the scale of the catchment. The specification should include
one independent check of the product — a catchment water balance over several
years, or a repeat gravity survey — even if it cannot be made to 10%.

---

## ★8 — Critique of a three-figure storage volume (model answer)

**The three quantities that would have to be independent.** (i) The regolith
thickness, with a *spatial* sampling error small compared with its temporal
variability; (ii) the specific yield, measured at the timescale of the process
being assessed (seasonal drainage is not the same $S_y$ as a multi-year average);
(iii) the saturated *thickness*, which in an unconfined aquifer that fluctuates
seasonally is not a constant — which thickness the volume refers to must be
stated.

**Why the precision is unjustified.** The reported number carries the precision of
its *arithmetic* (three figures) and the accuracy of its weakest *input* (38% in
the lesson's example). Reporting 3.84 Mm³ rather than $3.8 \pm 1.4$ Mm³ implies a
precision 12 times better than the evidence supports, and in a water-allocation
context that overstatement is the number that gets used.

**The one most diagnostic observation.** A **direct measurement of storage
change**: repeated microgravity (or, at larger scale, satellite gravimetry)
across a season with a measured water-level change. Storage change is $A\Delta h
S_y$, so a gravity measurement that resolves the mass change, combined with the
measured $\Delta h$, yields $S_y$ at the catchment scale — the term that dominates
the uncertainty — without needing a pump test at every location.
