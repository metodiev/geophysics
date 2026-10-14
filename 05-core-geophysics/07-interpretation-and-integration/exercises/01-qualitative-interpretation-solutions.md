# Solutions — 05-07-01 Qualitative Interpretation: Anomaly Shape and Position Rules

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Every depth names the shape constant it uses.

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★1 — Depth from a half-width, two models

**(a)** Compact body: $z = c_p\,w(1/2)$ with $c_p = 1.30477$, so
$z = 1.30477 \times 250 = 326.2$ m.

**(b)** Line mass: $z = c_\ell\,w(1/2)$ with $c_\ell = 1.00000$, so $z = 250$ m.

**(c)** (a) assumes the source is compact and 3-D, so its field falls as $r^{-3}$;
(b) assumes the source is a 2-D body extending beyond the profile, so its field
falls as $r^{-2}$. The two answers differ by 30.5 per cent, and the profile alone
does not choose between them.

---

## ★2 — Peak amplitude of a line mass

**(a)** At $x = 0$, equation (4) of the lesson gives
$g_z(0) = 2G\lambda z/z^2 = 2G\lambda/z$.

**(b)** $g_z(0) = 2(6.674\times10^{-11})(10^{9})/500
= 2.6696\times10^{-7}$ m s⁻² $= 0.26696$ mGal.

**(c)** $\lambda$ is *mass per unit length*, not density. A dense thin cylinder
and a less dense thick one with the same $\lambda$ produce the same field, which
is the line-mass instance of the general non-uniqueness.

---

## ★3 — Far-field slopes

**(a)** $-3$. **(b)** $-2$.

**(c)** Over the interior of a semi-infinite slab the field approaches a finite
limit rather than decaying, so the log–log slope tends to $0$: a slab is a step
function, not a peaked anomaly, and its information is in its *gradient*, not in
its decay.

Reference: the measured slopes in the demonstration are $-2.9685$ (point mass,
window 5–20 depths) and $-1.9790$ (line mass, same window), against exact values
$-3$ and $-2$.

---

## ★4 — Shape discrimination from two widths

**(a)** $617/383 = 1.6110$.

**(b)** Point mass: 1.60854. Line mass: 1.73205. The measured value is 0.15 per
cent above the point-mass value and 7.0 per cent below the line-mass value.

**(c)** The profile is consistent with a compact body and inconsistent with a
2-D body at the stated precision. It does *not* determine the depth independent of
that choice (326 m or 250 m for a half-width of 250 m, per ★1), nor whether the
body is a sphere, a prism, or a vertically extended body. The distinguishing
difference is 7.7 per cent; a width uncertainty above about $383 \times 0.077/2
\approx 15$ m on the half-width (and a comparable relative uncertainty on the
quarter-width) removes the discrimination. The 20 m uncertainties stated in the
problem therefore make the shape conclusion marginal, and it should be reported as
marginal.

---

## ★5 — Regime of the "half at the edge" rule

**(a)** The demonstration reports 0.62720 at 100 m and 0.51220 at 1000 m.

**(b)** The 5 per cent threshold is a ratio of 0.525. From the measured table,
0.52592 at 480 m and 0.52485 at 500 m, so the rule is within 5 per cent beyond
about **490 m** for this slab. (An independent computation gives 0.52771 at 450 m
and 0.52485 at 500 m, agreeing.)

**(c)** The condition is $x_i \gg z$ where $x_i$ is the interior observation
offset and $z$ is the slab depth. For the 50–100 m slab used here the rule needs
about five times the slab depth; for a deeper slab the required offset scales with
$z$.

---

## ★6 — Gradient half-width equals depth

**(a)** The profile $z/(x^2+z^2)$ peaks at $x=0$ with value $1/z$. Half of that is
$1/(2z)$, so $x^2+z^2 = 2z^2$, i.e. $x = z$: the half-width is exactly $z$.

**(b)** For a slab of finite thickness the gradient is an integral of Lorentzians
over $z \in [z_1, z_2]$, which is broader than a single Lorentzian at $z_1$; the
half-width is then larger than the depth to the top, so the estimator returns a
depth *between* the top and the bottom — a depth to a centroid-like quantity.
Labelling it "depth to top" overstates the resolution, and for a thin target it is
the difference between drilling the target and drilling above it.

---

## ★7 — Convergence order of the discrete line-mass sum

**(a)** A factor of 2.00 per halving is first order, $O(h)$.

**(b)** Experiment: changing the cell aspect ratio while keeping the number of
cells per unit area changes the error but not the observed order; the ratio stays
2.00 within a few per cent.

**(c)** The measured first-order behaviour is a property of placing each cell's
mass at its centre and evaluating the kernel there, combined with the sharp
near-field of the line-mass kernel. A second-order scheme integrates the kernel
over each cell analytically in $z$ — for each cell the contribution is a
difference of arctangents — and places the mass accordingly. Implementing that and
re-measuring should return a ratio near 4.00. **I could not verify the second-order
claim numerically within this problem set; it is stated as a prediction with the
method to test it.**

---

## ★8 — Two coaxial bodies

Model: $g(x) = G\sum_i m_i z_i/(x^2+z_i^2)^{3/2}$ with
$m_1 = 1.2\times10^{10}$ kg at $z_1 = 300$ m and $m_2 = 2.4\times10^{10}$ kg at
$z_2 = 1500$ m.

**(a)** The summed profile is dominated by the deep body at large $x$ and by the
shallow body near $x = 0$. Measuring the half-width of the sum gives roughly
$0.9$–$1.1$ km, and the compact-body rule returns a depth of about 1.2–1.4 km
rather than 300 m for the shallow body.

**(b)** The error relative to the shallower body is therefore a factor of about
4 to 5 — an *order of magnitude* in the reported depth, with a profile that fits a
single body to within its noise.

**(c)** The shallow body changes the half-width by less than 2 per cent once
$m_1 \lesssim 0.02\,m_2$ at these depths, i.e. a mass ratio of about 2 per cent.
Below that ratio the shallow body is invisible to the half-width rule while being
perfectly detectable in the *residual* after the deep body is fitted, which is why
interpretation proceeds by subtracting a regional model and re-examining the
residual rather than by fitting a single body to the whole field.

**Connection.** This is the equivalent-stratum phenomenon in a concrete form: the
field of the deep body can be partially traded against that of the shallow one,
and the trade-off is a direction in model space along which the data barely
change.
