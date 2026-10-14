# Exercises — 05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling

Attempt these **closed-book** before opening the
[solutions](./02-geometry-and-coverage-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement (split spread, receiver interval
20 m, one station move per shot, CMP bin 10 m, 400 shots): fold = $N/2$ for
$N = 24, 48, 96, 192$; 706 of 891 bins at full fold; ramp length per end 925 m
measured against a predicted $N\Delta x/2 - \Delta s = 940$ m; two-body critical
separation measured 301.06 m against an analytic 300.00 m at 300 m depth.

---

## ★ Foundational

**★1.** Derive the fold formula
$\text{fold} = \dfrac{N\Delta x}{2\Delta s}\cdot\dfrac{\Delta x}{2b}$ and show that
it reduces to $N/2$ for $\Delta s = \Delta x$ and $b = \Delta x/2$.

---

**★2.** A spread has 120 channels at 25 m spacing, shots every 25 m, and bins of
12.5 m. Compute the fold, the maximum offset, and the number of traces per shot.

---

**★3.** State the three things that acquisition geometry decides, and name the
parameter that controls each.

---

**★4.** A reflector is at 1.2 s two-way time with an interval velocity of
3000 m/s. (a) What is its depth? (b) What is the maximum offset required by the
"offset $\approx$ depth" rule as stated in the lesson, $x_{\max}\gtrsim v t_0$?

---

**★5.** Explain in one sentence why doubling the fold does not halve the Fresnel
zone.

---

## ★★ Applied

**★★6.** Using the measured ramp behaviour of the lesson, a survey line is 12 km
long and the target is 500 m from the western end. The spread is 96 channels at
20 m. Quantify how much of the target lies in the taper, and state two remedies.

---

**★★7.** Two point masses of equal mass lie at 400 m depth, separated by 300 m.

(a) Using the lesson's measured result $s_{\text{crit}} = h$, state whether the
field shows two bodies or one.
(b) If the separation is 900 m instead, what is the midpoint-to-peak ratio
(interpolate from the measured table: $s/h = 2$ gives 0.648, $s/h = 3$ gives 0.331)?
(c) A processing sequence applies an upward continuation of 200 m. Does the pair
become easier or harder to separate? Justify with the physics, not with a formula.

---

**★★8.** A 3-D survey targets a body whose horizontal extent is comparable to its
depth at 800 m. Argue, using the lesson's criteria, whether a 2-D line is
sufficient, and name the specific artefact that will appear if a single line is used
and the body lies 300 m off-line.

---

**★★9.** For a wavefield with dominant wavelength 60 m and a reflector at 1500 m
depth: (a) compute the Fresnel-zone radius; (b) compute the diameter; (c) state the
receiver spacing needed to avoid aliasing the 60 m wavelength, and explain why that
requirement is different from the resolution requirement.

---

## ★★★ Research-oriented

**★★★10.** Write a short program (or specify one precisely) that builds a 3-D
constant-geometry template — a receiver patch, a shot line, and a bin grid — and
measures the fold and the offset/azimuth distribution in each bin over the survey
area. Report the fraction of bins that achieve the nominal fold and the shape of the
offset distribution. Then state the two design changes that would make the
distribution more uniform, and what each costs.

---

**★★★11.** The two-body critical separation was measured as 301.06 m against an
analytic 300.00 m at 300 m depth. Estimate the discretisation error of the
measurement (the scan used 4001 separations between 0.90h and 1.10h and a
120 001-point profile), and state whether the 1.06 m discrepancy is consistent with
it. Show the arithmetic.

---

**★★★12.** Design an experiment that distinguishes numerically between the two
claims "$s_{\text{crit}} = h$" and "$s_{\text{crit}} = \sqrt{2}h$" for equal point
masses, using only the curvature of the summed profile at the midpoint. Derive the
condition analytically, then verify it numerically by evaluating the second
derivative at $x = 0$ for $s = 0.9h$, $h$ and $1.1h$, and report the measured
sign changes.
