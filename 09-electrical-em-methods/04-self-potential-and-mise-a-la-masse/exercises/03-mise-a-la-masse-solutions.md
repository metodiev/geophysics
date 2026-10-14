# Solutions — 09-04-03 Mise-a-la-Masse and Induced Polarisation Mapping

> **Read after attempting.** Lesson:
> [03 Mise-a-la-Masse](../03-mise-a-la-masse.md). All models **SYNTHETIC**.

---

## ★1 — The buried electrode

$$V(0) = \frac{\rho I}{2\pi z} = \frac{50 \times 1.0}{2\pi \times 60}
= \frac{50}{376.99} = 0.13263\ \mathrm{V} = 132.63\ \mathrm{mV},$$

$$V(100) = \frac{50}{2\pi\sqrt{100^{2}+60^{2}}}
= \frac{50}{2\pi \times 116.619} = 0.068237\ \mathrm{V} = 68.24\ \mathrm{mV}.$$

Note that $V(100)/V(0) = 0.5145$, whereas a *surface* electrode pair would give
$100/(100+60)$-type ratios — the depth is what makes the profile wide.

---

## ★2 — The apparent-resistivity identity

At $x = 0$: $r = \sqrt{0+60^{2}} = 60$ m, so
$\rho_a = 2\pi \times 60 \times 0.13263/1.0 = 50.00\ \Omega$ m.

At $x = 100$ m: $r = 116.619$ m, so
$\rho_a = 2\pi \times 116.619 \times 0.068237/1.0 = 50.00\ \Omega$ m.

Both are the true resistivity, which is the identity of the lesson's Section 2.2:
**in a homogeneous half-space a buried electrode produces no apparent-resistivity
anomaly**, so any variation of $\rho_a$ along a profile is the signature of a
heterogeneity.

---

## ★3 — The sphere coefficient in its limits

- $\sigma_1 = \sigma_0$ (no body): $A = a^{3}E_0 \times 0/3 = 0$. The sphere
  disappears from the external field, as it must, since the potential of a
  uniform medium is undisturbed by an inclusion with the same conductivity.
- $\sigma_1 \to \infty$ (perfect conductor): $A \to a^{3}E_0$. This is the standard
  result that a perfectly conducting sphere in a uniform field behaves as a dipole
  of that strength, and it is what makes the sphere's surface an equipotential —
  the demonstration verifies that the potential on $r = a$ is within
  $3\times10^{-5}$ V of zero at every angle for $k = 10^{6}$.

---

## ★4 — Deriving $A$

Inside the sphere the potential must be finite at the origin and cannot contain
$l = 1$ multipoles of order $l \geq 2$ in a uniform applied field, so
$\varphi_{\text{in}} = -B r\cos\theta$. Outside, the primary is $-E_0 r\cos\theta$
and the sphere adds a dipole term $\varphi_{\text{anom}} = A\cos\theta/r^{2}$.

**Condition 1 — potential continuity at $r = a$.**

$$-Ba = -E_0a + \frac{A}{a^{2}} .$$

**Condition 2 — normal current continuity at $r = a$**
($\sigma_1\partial_r\varphi_{\text{in}} = \sigma_0\partial_r\varphi_{\text{out}}$):

$$-\sigma_1B = -\sigma_0E_0 - \frac{2\sigma_0A}{a^{3}} .$$

From condition 1, $B = E_0 - A/a^{3}$. Substituting into condition 2:

$$-\sigma_1\left(E_0 - \frac{A}{a^{3}}\right)
= -\sigma_0E_0 - \frac{2\sigma_0A}{a^{3}},$$

$$\frac{A}{a^{3}}\left(\sigma_1 + 2\sigma_0\right)
= E_0\left(\sigma_1 - \sigma_0\right)
\;\Longrightarrow\;
A = a^{3}E_0\,\frac{\sigma_1-\sigma_0}{\sigma_1+2\sigma_0}
= a^{3}E_0\,\frac{k-1}{k+2}. \qquad\blacksquare$$

---

## ★5 — Why the anomaly saturates

The anomaly is proportional to $A \propto (k-1)/(k+2)$, which tends to $1$ as
$k\to\infty$. From the measured table at $4.63$ radii the anomaly is $2.011\%$ at
$k = 10$, $2.602\%$ at $k = 100$ and $2.673\%$ at $k = 1000$:

- from $10$ to $100$: $+29.4\%$ of the value;
- from $100$ to $1000$: $+2.73\%$.

The ratio $(k-1)/(k+2)$ explains both: at $k = 10$ it is $9/12 = 0.75$, at
$k = 100$ it is $99/102 = 0.9706$ and at $k = 1000$ it is $999/1002 = 0.99701$ —
so $2.673$ is already $99.7\%$ of the asymptote.

**The surface array is different** because it measures a *spatial derivative* of
the potential: its anomaly scales with $A$ as well but is compared against the
primary *dipole* field of the array, which changes with the geometry and does not
saturate in the same way. The measured array anomalies grow with contrast at fixed
spacing, and their magnitude falls with spacing ($-5.25\%$, $-3.30\%$, $-0.70\%$
for $30$, $60$ and $120$ m) as the sensitivity moves deeper and past the body.

---

## ★6 — Increments in the saturation table

- $2.011 \to 2.602$: $(2.602-2.011)/2.011 = +29.39\%$ for a factor $10$ in
  contrast;
- $2.602 \to 2.673$: $(2.673-2.602)/2.602 = +2.73\%$ for a further factor $10$.

The trend is **decelerating**: each decade of contrast buys a smaller increment,
as $A/(a^{3}E_0) = (k-1)/(k+2)$ approaches $1$. The table is therefore a
measurement of the saturation of the underlying coefficient, and it means that an
anomaly amplitude cannot be inverted for a conductivity contrast once the body is
clearly conductive — the amplitude has stopped carrying that information.

---

## ★7 — Separating the two bodies (specification)

Both bodies produce a $0.10\%$ anomaly, so the amplitude alone cannot separate
them. Three procedures can.

1. **Extend the offset range.** The two bodies sit at different radii, so their
   anomaly *patterns* have different widths: the nearer body's anomaly decays
   faster with offset than the farther one's. Measure the anomaly on a profile
   spanning several times the larger radius, fit both models, and compare
   $\chi^{2}$ (require $\Delta\chi^{2} > 9$).
2. **Change the source position.** Move the current electrode (a borehole
   electrode can be moved between depths) and repeat: the anomaly depends on the
   source-to-body distance, which differs between the two candidates, so a
   second geometry adds an independent equation.
3. **Add a measurement that is not a single potential**: an IP measurement, which
   responds to the body's polarisability rather than to the contrast, or a
   borehole log that intersects one of the candidates.

**Statistic.** The joint $\chi^{2}$ of the two-model comparison over all
geometries, with the number of independent geometries stated. With one profile
and one source position the two candidates are formally indistinguishable, and
that should be the reported conclusion.

---

## ★8 — The divergence and what replaces the model

**Why it grows.** The sphere model uses the *locally uniform field*
approximation: the induced dipole is computed from the field at the body's centre,
$E_0 \propto 1/R^{2}$ with $R$ the source-to-centre distance. As the source
approaches the centre, $E_0 \to \infty$, so $A = a^{3}E_0(k-1)/(k+2)$ diverges,
and with it the modelled anomaly ($7987\%$ at a distance of $0.07$ radii). The
divergence is not physics: it is the model being asked a question outside its
assumptions. At the centre itself the numerical gradient vanishes — the same
singularity seen from the other side, and another symptom that the geometry is
invalid for this model.

**What replaces it.** Physically the current is injected *into* a conductor, which
then becomes an extended electrode: a large part of its surface is at nearly one
potential, and the current leaves from the whole surface. The correct model is the
potential field of a body with a prescribed (nearly constant) surface potential —
an **equipotential-body** problem, solved by boundary-element or integral-equation
methods, or by a finite-element solution of $\nabla\cdot(\sigma\nabla V) = 0$ with
the body and the host as two media of very different conductivity.

**What the survey should measure instead.** With the electrode inside the body,
the useful measurements are the *outline* of the energised body (the surface
equipotential pattern, its width and its offset dependence), a second electrode
position to add a geometry equation, and an IP measurement for the body's
polarisability — none of which require the polarised-sphere coefficient that
diverges here.
