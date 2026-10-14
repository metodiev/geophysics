# Solutions — 06-10-04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [04 MASW/SASW: Surface-Wave Dispersion and Vs Profiles](../04-masw-sasw.md).
All models are SYNTHETIC.

---

## ★1 — The bracket on the fundamental mode

A trapped Love mode requires $k_1$ real in the layer and $k_2$ real in the
half-space, which is exactly the pair of inequalities
$v_{s1} < c < v_{s2}$:

$$200\ \mathrm{m\,s^{-1}} < c < 800\ \mathrm{m\,s^{-1}}.$$

The demonstration comes within $0.0010\%$ of the upper bound at
$f = 0.01\ \mathrm{Hz}$ ($c = 799.992\ \mathrm{m\,s^{-1}}$) and within
$0.0012\%$ of the lower bound at $f = 1000\ \mathrm{Hz}$
($c = 200.002\ \mathrm{m\,s^{-1}}$).

The bound is exact because it is a *condition for the mode to exist*: outside it,
$k_1$ or $k_2$ becomes imaginary, the field stops being a decaying trapped mode, and
the dispersion relation has no root at all. A dispersion curve therefore constrains a
*shape inside a bracket*; the two bracket edges are the two body-wave velocities, and
no accuracy of measurement can push a phase velocity outside them.

---

## ★2 — Wavelength and the depth conventions

$\lambda = c/f$ is exact:

$$\lambda = \frac{790.98\ \mathrm{m\,s^{-1}}}{2\ \mathrm{Hz}} = 395.49\ \mathrm{m},$$

$$\frac{\lambda}{3} = 131.83\ \mathrm{m}, \qquad
\frac{c}{2f} = \frac{790.98}{4} = 197.74\ \mathrm{m}.$$

Units: $(\mathrm{m\,s^{-1}})/(\mathrm{s^{-1}}) = \mathrm{m}$ for all three.

**Only $\lambda = c/f$ is an identity.** $\lambda/3$ is the conventional depth at
which the mode's sensitivity to a thin perturbation peaks, and $c/2f$ is the other
common convention; they differ by a factor $1.5$ by construction and neither is a
measurement. At $2\ \mathrm{Hz}$ the site would be described as
$132\ \mathrm{m}$ deep by one convention and $198\ \mathrm{m}$ by the other — the
reason a depth from a dispersion curve must always name its convention.

---

## ★3 — Checking one point of the curve

$$x = \omega H\sqrt{\frac{1}{v_{s1}^{2}} - \frac{1}{c^{2}}}
= 2\pi(20)(10)\sqrt{\frac{1}{200^{2}} - \frac{1}{206.4294^{2}}}.$$

The two slownesses: $1/200^{2} = 2.500000\times10^{-5}$ and
$1/206.4294^{2} = 2.346696\times10^{-5}$, so the difference is
$1.533036\times10^{-6}$, its square root $1.238158\times10^{-3}$, and

$$x = 2\pi(20)(10) \times 1.238158\times10^{-3} = 1256.637 \times
1.238158\times10^{-3} = 1.555916\ \mathrm{rad}.$$

Left side: $\tan 1.555916 = 67.1971$.

Right side:
$\sqrt{1/c^{2} - 1/v_{s2}^{2}} = \sqrt{2.346696\times10^{-5} -
1.562500\times10^{-6}} = \sqrt{2.190446\times10^{-5}} = 4.680221\times10^{-3}$;
dividing by $1.238158\times10^{-3}$ gives $3.779985$; multiplying by
$\mu_2/\mu_1 = 17.7778$ gives

$$\frac{\mu_2}{\mu_1}\frac{k_2}{k_1} = 67.1997.$$

**The two sides agree to four significant figures** ($67.1971$ against $67.1997$, a
relative difference of $3.9\times10^{-5}$), which is the precision of the printed
root $c = 206.4294\ \mathrm{m\,s^{-1}}$ rather than a physical discrepancy — the
run in the lesson uses the unrounded root and agrees to five digits. Four or five
digits is the right expectation: the curve is a transcendental root, so the check
verifies the algebra and the numerical solver together, not one or the other.

---

## ★★4 — Sensitivity to the layer velocity

$$50\ \mathrm{Hz}:\quad \frac{\partial\ln c}{\partial\ln v_{s1}} = 1.00999
\;\Rightarrow\; \delta c = 1.00999 \times 5\% = +5.05\%.$$

$$2\ \mathrm{Hz}:\quad \frac{\partial\ln c}{\partial\ln v_{s1}} = 0.05453
\;\Rightarrow\; \delta c = 0.05453 \times 5\% = +0.27\%.$$

At $50\ \mathrm{Hz}$ a velocity change maps almost one-for-one into a phase-velocity
change, because at that frequency the mode lives entirely in the layer and its speed
*is* $v_{s1}$. Those frequencies are the ones that measure **the layer velocity** and
are therefore the ones a survey must record accurately if $V_S$ is the deliverable.

At $2\ \mathrm{Hz}$ the layer velocity is nearly irrelevant, and the same row of the
table attributes $0.97416$ of the sensitivity to $v_{s2}$: the low frequencies
measure **the half-space**. A survey that misses the low frequencies cannot report
the deeper material at all, and the demonstration's offset table makes that concrete
— a $5\ \mathrm{m}$ offset reaches down to only $f_{\min} = 20.67\ \mathrm{Hz}$.

---

## ★★5 — Reading the ridge

$$H:\quad \frac{9.00\text{–}11.00\ \mathrm{m}}{10.0\ \mathrm{m}}
= \pm 10.0\%, \qquad
v_{s1}:\quad \frac{195.0\text{–}200.0}{200.0} = 2.5\%.$$

The layer velocity is pinned to $2.5\%$ while the thickness is pinned only to
$10\%$ — an asymmetry of a factor of four in favour of the velocity, at a noise
level of $3\%$. That is the opposite of what a reader might guess from the fact
that the curve's amplitude dependence is on the layer thickness.

Two points of interpretation. First, the asymmetry is *not* because thickness is
unimportant but because of the specific trade: the $v_{s1}$ range is bounded on one
side only (the accepted set runs to $200.0$, not beyond), so the "2.5%" is a
one-sided bound rather than a symmetric error bar. Second, the correlation of
$+0.7016$ between the accepted $H$ and $v_{s1}$ is what makes the pair uncertain:
the ridge is a *line* of good fits, and quoting the midpoint of the thickness range
together with the midpoint of the velocity range quotes a model that is not on the
ridge at all.

---

## ★★6 — What r² = 0.875 means

$$r^{2} = (-0.9356)^{2} = 0.8753.$$

**$87.5\%$ of the variance of the $H$-sensitivity column is explained by the
$v_{s1}$ column** (equivalently, the two columns are almost the same vector with a
sign flip). In practice: a change in thickness and a compensating change in velocity
produce nearly the same change in the whole dispersion curve, so the data cannot
distinguish them, and the $12.5\%$ that is left is the only information the curve
carries about thickness as opposed to velocity.

The consequences are concrete. The acceptable set is a ridge, not a point (Section 6
of the lesson); the $H$ half-width is $1.00\ \mathrm{m}$ at $3\%$ noise; and any
independent information — a borehole, a refraction velocity for the layer, a
geological bound on thickness — is worth more to the answer than additional
frequency samples inside the same band.

---

## ★★★7 — Testing whether a wider band breaks the ridge

**Model.** The demonstration's Love model, fixed at $H = 10.0\ \mathrm{m}$,
$v_{s1} = 200\ \mathrm{m\,s^{-1}}$, $v_{s2} = 800\ \mathrm{m\,s^{-1}}$,
$\rho_1 = 1800$, $\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$.

**Noise realisations.** Draw one set of $3\%$ independent relative errors per
frequency from a fixed seed, then evaluate the misfit of every trial model against
the *same* perturbed target in all three bands (8–40 Hz, 1–10 Hz, 1–40 Hz).
Sharing the realisations is essential: if each band gets its own noise draw, a
difference in ridge width could be a difference in the errors rather than a
difference in the information content, and the experiment would not be controlled.

**Grid.** $H$ from 4 to 20 m in 0.5 m steps, $v_{s1}$ from 140 to
$300\ \mathrm{m\,s^{-1}}$ in 5 m/s steps (1089 cells), as in the demonstration.

**Metric.** The half-width of the accepted $H$ set, defined as
(accepted $H_{\max}$ − accepted $H_{\min}$)/2, with "accepted" meaning RMS misfit
below the $3\%$ noise level; plus the correlation between the accepted $H$ and
$v_{s1}$ values.

**Predicted outcome.** The half-width should shrink from $1.00\ \mathrm{m}$ (short
spread, 8–40 Hz) to $0.25\ \mathrm{m}$ (both bands) — a factor of four — while the
correlation should rise to $+1.00$, because the low frequencies, which sample the
whole layer, are what break the trade. The best-fitting model in the widest band is
predicted to be $H = 10.50\ \mathrm{m}$ at an RMS of $2.533\%$: still inside the
acceptable set, and still $5\%$ wrong. **The experiment's real conclusion is that a
wider band narrows the ridge without removing it**, which is why the answer is a set
at any bandwidth.

---

## ★★★8 — The density that a velocity error would hide

The dispersion relation depends on the rigidities, so what the curve measures is
$\mu = \rho v_s^{2}$, not $v_s$ alone. Logarithmically,

$$\frac{\delta\mu}{\mu} = \frac{\delta\rho}{\rho} + 2\frac{\delta v_s}{v_s}.$$

A $5\%$ velocity error is compensated ($\delta\mu = 0$) by
$\delta\rho/\rho = -2(0.05) = -10\%$.

So a $10\%$ error in the assumed density is exactly equivalent, in its effect on the
dispersion curve, to a $5\%$ error in the velocity — and the inversion, which
parametrises $v_s$ and holds $\rho$ fixed, will absorb the whole of it into $v_s$.
The sign is what matters practically: if the true density is *higher* than assumed
(a saturated soil, or a coarse gravel below a shallow water table), the fitted
$v_s$ comes out *lower* than the truth by about half the density error, and vice
versa. Densities of near-surface materials commonly span $1600$ to
$2200\ \mathrm{kg\,m^{-3}}$, i.e. $\pm 15\%$ around $1900$, which is $\pm 7.5\%$ of
velocity — larger than the $2.5\%$ ridge width of ★★5. **The density assumption,
not the dispersion measurement, is the dominant term in a shallow $v_s$ profile**,
and the honest response is to state the assumed density, to measure it where
possible, or to invert for it and report the resulting expansion of the acceptable
set.
