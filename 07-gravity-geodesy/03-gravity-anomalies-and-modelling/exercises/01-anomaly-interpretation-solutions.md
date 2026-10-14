# Solutions — 07-03-01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [01 Interpreting Anomalies](../01-anomaly-interpretation.md).

---

## ★1 — The sphere half-width

$$g_z(x) = \frac{GMz}{\left(x^{2}+z^{2}\right)^{3/2}},\qquad
g_{z,\max} = \frac{GM}{z^{2}}.$$

Setting $g_z(x_{1/2}) = \tfrac{1}{2}g_{z,\max}$:

$$\frac{z}{\left(x_{1/2}^{2}+z^{2}\right)^{3/2}} = \frac{1}{2z^{2}}
\;\Rightarrow\; x_{1/2}^{2}+z^{2} = 2^{2/3}z^{2}
\;\Rightarrow\; x_{1/2} = z\sqrt{2^{2/3}-1}.$$

$2^{2/3} = 1.587401$, so $\sqrt{0.587401} = 0.766421$.

For the cylinder, $g_z \propto z/(x^{2}+z^{2})$, so half the peak requires
$x^{2}+z^{2} = 2z^{2}$, giving $x_{1/2} = z$ **exactly**: the kernel's
denominator is linear in $x^{2}$, so the factor is $1$. No geometric constant can
appear because the profile is a Lorentzian, not a power of a quadratic sum raised
to $3/2$.

---

## ★2 — Depth from a $300\ \mathrm{m}$ half-width

- Cylinder rule: $z = x_{1/2} = \mathbf{300.0\ m}$.
- Sphere rule: $z = 300/0.766421 = \mathbf{391.4\ m}$.

Difference: $(391.43-300)/300 = +30.5\%$. Same profile, two legitimate-looking
answers: the body shape must be stated.

---

## ★3 — Amplitude exponents

Sphere $g \propto z^{-2}$ (mass fixed), cylinder $g \propto z^{-1}$ (line mass
fixed), infinite sheet $g = 2\pi G\Delta\rho t$, independent of $z$. The sheet has
no exponent because the geometry makes every depth contribute equally: doubling
the depth does not change the solid angle subtended by an infinite plane.

---

## ★4 — Sphere at $900\ \mathrm{m}$

$$M = \tfrac{4}{3}\pi R^{3}\Delta\rho
= \tfrac{4}{3}\pi(400)^{3}(250) = 6.7021\times10^{10}\ \mathrm{kg}.$$

Peak:

$$g_{z,\max} = \frac{GM}{z^{2}}
= \frac{(6.67430\times10^{-11})(6.7021\times10^{10})}{810000}
= 5.5224\times10^{-6}\ \mathrm{m\,s^{-2}}
= \mathbf{0.55224\ mGal}.$$

Half-width: $x_{1/2} = 0.766421\times900 = \mathbf{689.78\ m}$.

Derivative: the maximum of $\left|\mathrm{d}g/\mathrm{d}x\right|$ lies at
$x = z/2 = 450\ \mathrm{m}$, with

$$\left|\frac{\mathrm{d}g_z}{\mathrm{d}x}\right|_{\max}
= \frac{3MG}{2\,(5/4)^{5/2}z^{3}}
= \frac{3(6.7021\times10^{10})(6.67430\times10^{-11})}
{2(1.74693)(7.29\times10^{8})}
= 5.269\times10^{-9}\ \mathrm{m\,s^{-2}\,m^{-1}}
= \mathbf{5.269\times10^{-4}\ mGal\,m^{-1}},$$

confirmed numerically in the lesson's demonstration
($5.269\times10^{-4}\ \mathrm{mGal\,m^{-1}}$ at $x = 450.0\ \mathrm{m}$).

---

## ★5 — $0.30\ \mathrm{mGal}$ from $8\ \mathrm{km}$

$$M = \frac{g z^{2}}{G}
= \frac{(3.0\times10^{-6})(8000)^{2}}{6.67430\times10^{-11}}
= \frac{192}{6.67430\times10^{-11}}
= 2.8767\times10^{12}\ \mathrm{kg}.$$

Radius at $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$:

$$R = \left(\frac{3M}{4\pi\Delta\rho}\right)^{1/3}
= \left(\frac{3\times2.8767\times10^{12}}{4\pi\times300}\right)^{1/3}
= \left(2.289\times10^{9}\right)^{1/3} = \mathbf{1318\ m}.$$

Self-consistency: $R/z = 1318/8000 = 0.165 \ll 0.5$, so the point-mass
approximation is comfortable. Note the pattern in the family table: $R/z$ falls as
$z^{-1/3}$, so the deeper the body, the better the compact-source approximation —
which is why shallow anomalies are the ones where the shape matters most.

---

## ★6 — The same profile, both rules

Sphere rule: $800 = x_{1/2}/0.766421$, so
$x_{1/2} = 800\times0.766421 = 613.1\ \mathrm{m}$ ✔ consistent with the report.

Cylinder rule on the same profile: $z = x_{1/2} = \mathbf{613.1\ m}$, i.e. $23\%$
shallower than the sphere answer. The two rules differ by the constant
$0.766421$ — nothing in the profile can tell you which applies.

---

## ★7 — Cylinder versus sphere, when the peak agrees

Under the cylinder rule, the peak of a line mass is
$g_{\max} = 2G\lambda/z$ with $\lambda = \pi R^{2}\Delta\rho$; the depth is
$x_{1/2} = 500\ \mathrm{m}$ (the cylinder's half-width is its depth), and the peak
is the one measured.

For a sphere with the same peak:

$$z_{\text{sph}} = \frac{x_{1/2}}{0.766421}
\ \text{with the }\textbf{same}\ x_{1/2}\ \text{only if the shapes match}.$$

Since they do not, the correct procedure is to fix the peak and invert for the
depth that reproduces the *whole profile*. Using the profile's shape:

- Fit $\log g$ versus $\log z$ is not available from one profile; instead compare
  the ratio of the anomaly at $x = x_{1/2}$ to the peak (both rules give $0.5$ by
  definition — not discriminating), and use the anomaly at, say,
  $x = 2x_{1/2}$: the sphere gives $z/(x^{2}+z^{2})^{3/2}$ with
  $x = 1.5328z \Rightarrow 0.2065\,g_{\max}$, while the cylinder gives
  $z/(x^{2}+z^{2})$ with $x = 2z \Rightarrow 0.2000\,g_{\max}$. The **ratio
  $g(2x_{1/2})/g(0)$ is $0.2065$ for a sphere and $0.2000$ for a cylinder**.
- The discriminating measurement is therefore **the far flank amplitude**, whose
  difference is $3.2\%$ of the peak. With a peak of order $1\ \mathrm{mGal}$ that
  is a $0.03\ \mathrm{mGal}$ difference, so the survey needs flanks sampled to
  better than $0.01\ \mathrm{mGal}$ — a $5\ \mathrm{m}$ station spacing is more
  than adequate, and the line must extend to at least $3x_{1/2} = 1.5\ \mathrm{km}$
  on both sides so that the ratio is measured, not extrapolated.
- **Failure mode:** noise of $0.03\ \mathrm{mGal}$ rms on the far flank destroys
  the $3.2\%$ distinction; the discrimination is limited by the *signal-to-noise
  at $2x_{1/2}$*, not at the peak.

---

## ★8 — Half-width uncertainty from noise

With a $3\ \mathrm{km}$ line, $100\ \mathrm{m}$ spacing and
$0.03\ \mathrm{mGal}$ rms noise, an anomaly of peak $g_0$ has a flank gradient of
order

$$\left|\frac{\mathrm{d}g}{\mathrm{d}x}\right|
\approx \frac{g_0}{x_{1/2}}$$

near the half-amplitude point. The half-width error from noise alone is therefore

$$\sigma_{x_{1/2}} \approx \frac{\sigma_g}{\left|\mathrm{d}g/\mathrm{d}x\right|}
= \frac{x_{1/2}\,\sigma_g}{g_0}
= \frac{613\ \mathrm{m}\times0.03}{1.0} = 18\ \mathrm{m}
\quad\text{for a } 1.0\ \mathrm{mGal}\ \text{peak}.$$

Propagating through the rules:

- cylinder, $z = x_{1/2}$: $\sigma_z = 18\ \mathrm{m}$;
- sphere, $z = x_{1/2}/0.766421$: $\sigma_z = 18/0.766421 = 24\ \mathrm{m}$.

The result scales inversely with the peak: a $0.3\ \mathrm{mGal}$ anomaly with the
same noise gives $\sigma_z \approx 60$–$80\ \mathrm{m}$. **Assumption required:**
the regional field is flat and known, otherwise the "half of peak" reference level
is itself uncertain and the dominant error is no longer the noise — which is
exactly the problem the lesson's microgravity survey has to solve before the
half-width can be measured at all.
