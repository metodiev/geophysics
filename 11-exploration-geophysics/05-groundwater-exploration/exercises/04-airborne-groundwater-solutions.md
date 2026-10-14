# Solutions — 11-05-04 Airborne EM for Regional Aquifer Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [04 Airborne EM for Regional Aquifer Mapping](../04-airborne-groundwater.md).

---

## ★1 — Diffusion depth

$$ d = 1261.6\sqrt{\rho t}, \qquad \rho = 30\ \Omega\,\mathrm{m}: $$

| $t$ | $d$ |
|---|---|
| $0.1\ \mathrm{ms} = 10^{-4}\ \mathrm{s}$ | $1261.6\sqrt{3\times10^{-3}} = 69.1\ \mathrm{m}$ |
| $1\ \mathrm{ms}$ | $1261.6\sqrt{0.03} = 218.5\ \mathrm{m}$ |
| $10\ \mathrm{ms}$ | $1261.6\sqrt{0.3} = 691.0\ \mathrm{m}$ |

Units: $[\rho t] = \Omega\,\mathrm{m}\,\mathrm{s}
= \mathrm{kg\,m^{3}\,s^{-3}\,A^{-2}}\cdot\mathrm{m\,s}
= \mathrm{kg\,m^{4}\,s^{-2}\,A^{-2}}$, and $\sqrt{\rho t/\mu_0}$ has units of
metres because $[\mu_0] = \mathrm{kg\,m\,A^{-2}\,s^{-2}}$. ✔ The prefactor
$1261.6 = \sqrt{2/\mu_0}$ carries the conversion.

---

## ★2 — Kernel normalisation and peak

$$ \int_0^{\infty}K\,\mathrm{d}z = \int_0^{\infty}\frac{z}{2Dt}
e^{-z^{2}/(4Dt)}\,\mathrm{d}z. $$

Substitute $u = z^{2}/(4Dt)$, so $\mathrm{d}u = \dfrac{z}{2Dt}\,\mathrm{d}z$:

$$ \int_0^{\infty}e^{-u}\,\mathrm{d}u = 1. \qquad\checkmark $$

For the peak, set $\mathrm{d}K/\mathrm{d}z = 0$:

$$ \frac{\mathrm{d}}{\mathrm{d}z}\left[z\,e^{-z^{2}/(4Dt)}\right]
= e^{-z^{2}/(4Dt)}\left[1 - \frac{z^{2}}{2Dt}\right] = 0
\;\Longrightarrow\; z^{2} = 2Dt
\;\Longrightarrow\; z = \sqrt{2Dt} = d(t). \qquad\checkmark $$

---

## ★3 — Equivalent thicknesses

$$ h = S/\sigma: \quad S = 2.5\ \mathrm{S}
\;\Rightarrow\; h = 50.0\ \mathrm{m}\ (\sigma = 0.05\
\mathrm{S\,m^{-1}}),\ 10.0\ \mathrm{m}\ (0.25),\ 2.5\ \mathrm{m}\ (1.0). $$

Only the $10\ \mathrm{m}$ of $0.25\ \mathrm{S\,m^{-1}}$ is plausible as a
*usable* aquifer: $50\ \mathrm{m}$ of $0.05\ \mathrm{S\,m^{-1}}$ is a fresh but
low-conductance section (possible, but the conductance is spread over a great
thickness), and $2.5\ \mathrm{m}$ of $1.0\ \mathrm{S\,m^{-1}}$ is a thin
conductive clay or a saline seam. **The conductance alone does not decide which;**
the hydrogeological prior and a borehole do.

---

## ★4 — Gate and DOI for a target at 80 m

$$ d = 1261.6\sqrt{\rho t} = 80
\;\Longrightarrow\;
t = \frac{(80/1261.6)^{2}}{\rho}
= \frac{0.004021}{50} = 8.04\times10^{-5}\ \mathrm{s} = 80.4\ \mu\mathrm{s}. $$

$$ z_{\text{DOI}} = 1.55\,d = 1.55(80) = 124.0\ \mathrm{m}. $$

The target at 80 m is inside the depth of investigation, and the gate that *peaks*
at 80 m is the earliest usable one — a reminder that shallow targets need very
early gates.

---

## ★5 — Depth limit at 50 m altitude

The lesson's altitude table normalises the coupling to a surface layer at 30 m
altitude. Interpolating between the printed rows is unsafe, so evaluate the
coupling directly. The detection condition is

$$ \frac{C(h,z)}{C(30,0)} > 3\times0.02 = 0.06,
\qquad C(h,z) = \frac{1}{\left((h+z)^{2}+a^{2}\right)^{3/2}},\ a = 10\
\mathrm{m}. $$

At $h = 50\ \mathrm{m}$ the largest depth satisfying it is $z \approx 30\
\mathrm{m}$ (verified by solving
$\left((50+z)^{2}+100\right)^{3/2} = 16667$). So the depth limit is about
**30 m** — between the $50\ \mathrm{m}$ at 30 m altitude and the $20\ \mathrm{m}$
at 60 m altitude, and closer to the higher-altitude value because the coupling is
a steep function of the total distance.

**Assumption.** This uses the stated synthetic geometric coupling model with a
$10\ \mathrm{m}$ loop and a $2\%$ noise floor; a real system's numbers differ, but
the direction of the trade — altitude costs penetration — does not.

---

## ★6 — Posterior probability

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR}+(1-p)\,\mathrm{FPR}}
= \frac{0.12(0.70)}{0.12(0.70)+0.88(0.40)}
= \frac{0.084}{0.084+0.352} = 0.1927. $$

Of 50 anomalies, $50\times0.1927 = 9.6$, i.e. about **10** are expected to be
usable aquifers and about 40 are not. The test has lifted the odds from $12\%$ to
$19\%$; it has not made the anomaly a resource.

---

## ★7 — Two-stage survey design (specification)

**Stage 1 (AEM).** Fly at $h = 45$-$60\ \mathrm{m}$: low enough to keep the
coupling to a $50\ \mathrm{m}$ target above the noise (the $30\ \mathrm{m}$
altitude limit is $50\ \mathrm{m}$; $60\ \mathrm{m}$ altitude only reaches
$20\ \mathrm{m}$), high enough for terrain clearance. Use a large transmitter
moment, because Section 4 shows altitude cannot be paid back any other way. Gates
from $50\ \mu\mathrm{s}$ (a $60\ \mathrm{m}$ target in $30\
\Omega\,\mathrm{m}$ ground peaks at $75\ \mu\mathrm{s}$) to the latest gate whose
signal still exceeds the noise — do not trust a fixed late gate, compute the DOI
from the achieved noise. Line spacing: choose it smaller than the expected target
width, because the footprint already smears narrow channels; a line spacing larger
than the channel width guarantees aliasing.

**Stage 2 (ground follow-up).** Ground TDEM or ERT to confirm the conductance and
place it in a layered model, plus seismic refraction or MASW for an independent
porosity estimate (the equivalence of Section 3.3 requires a second observable to
break). Then a borehole at the best target.

**Decision rule.** Convert the AEM anomaly to a conductance, add the ground
follow-up constraint, then apply Bayes with the *regional* prior $p$. Drill when
the posterior exceeds the break-even probability set by the drilling cost and the
value of a successful well, not when the anomaly is merely strong. Report the
expected number of dry holes at that threshold.

---

## ★8 — What a deep gate does and does not constrain

Take $\rho = 50\ \Omega\,\mathrm{m}$ and the gate whose diffusion depth is
$150\ \mathrm{m}$. Then $t = (150/1261.6)^{2}/50 = 2.83\times10^{-4}\
\mathrm{s}$ ($283\ \mu\mathrm{s}$). The cumulative kernel is
$F(z) = 1-e^{-z^{2}/(4Dt)}$ with $Dt = d^{2}/2 = 1.126\times10^{4}\
\mathrm{m^{2}}$:

$$ F(100) = 1 - e^{-100^{2}/(4 \times 1.126\times10^{4})}
= 1 - e^{-0.222} = 0.199, $$
$$ F(150) = 1 - e^{-22500/45040} = 0.394. $$

So $19.9\%$ of the kernel's weight lies **above 100 m** and $39.4\%$ lies above
the peak itself: the kernel is skewed *deeper* than its peak, with a long tail.

**What the observation constrains.** The measured response is a weighted average
with about one fifth of its weight in the top 100 m and four fifths below. A
change in the shallow section therefore changes the deep-gate reading, and two
different conductivity profiles — one with a deep conductor, one with a shallower
thicker conductor — can fit it. The gate constrains a **conductance distribution
over a window**, not "the aquifer at 150 m". Attributing a depth requires either
an inversion with an explicit regularisation and its resolution attached, or an
independent measurement. The peak depth is a convention of the kernel, not a
measurement of where the water is.

---

## Worked mastery checkpoint

**(a) Diffusion depth and DOI** at $\rho = 40\ \Omega\,\mathrm{m}$,
$t = 0.5\ \mathrm{ms} = 5\times10^{-4}\ \mathrm{s}$:

$$ d = 1261.6\sqrt{40 \times 5\times10^{-4}} = 1261.6\sqrt{0.02}
= 1261.6(0.14142) = 178.4\ \mathrm{m}, $$
$$ z_{\mathrm{DOI}} = 1.55\,d = 276.5\ \mathrm{m}. $$

The anomaly at 20-55 m is therefore well inside the investigation depth of this
gate — the target is shallow relative to what the latest usable gate reaches.

**(b) Two models with the same conductance $S = 3.0\ \mathrm{S}$:**

- $10\ \mathrm{m}$ of $0.30\ \mathrm{S\,m^{-1}}$,
- $40\ \mathrm{m}$ of $0.075\ \mathrm{S\,m^{-1}}$ (equivalently $15\ \mathrm{m}$
  of $0.20\ \mathrm{S\,m^{-1}}$).

The data cannot choose between them because a thin high-conductivity layer and a
thick low-conductivity one with the same conductance produce the same
kernel-weighted average; only the product survives. The hydrogeological reading
differs (a 10 m aquifer versus a 40 m brackish interval), so a borehole is
needed.

**(c) Posterior.**

$$ \mathrm{PPV} = \frac{0.10(0.75)}{0.10(0.75)+0.90(0.35)}
= \frac{0.075}{0.075+0.315} = 0.192. $$

**(d) The single next measurement that would most improve the decision:** a
borehole (or at least a ground TDEM sounding plus a water sample) at the ranked
top target. It improves the *decision* rather than the dataset because it
supplies the two things the survey cannot — the layer thickness and the water
quality — which are exactly the quantities that separate a usable aquifer from a
clay or a saline interval.
