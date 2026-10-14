# Solutions — 07-04-05 ITRF, Plate Motion Models and Frame Transformations

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [05 ITRF and Plate Motion Models](../05-itrf-and-plate-models.md).

---

## ★1 — Converting a rotation rate

$$2.5^{\circ}\,\mathrm{Myr^{-1}}
= 2.5\times1.745329\times10^{-8}
= \mathbf{4.3633\times10^{-8}\ rad\,yr^{-1}} .$$

With the pole on the equator and the station on the equator at $90^{\circ}$ from
the pole, the velocity is tangential with magnitude

$$v = \omega R = 4.3633\times10^{-8}\times6.371\times10^{6}
= 0.2780\ \mathrm{m\,yr^{-1}} = \mathbf{278.0\ mm\,yr^{-1}},$$

i.e. the great-circle speed $\omega R$. A station at the pole would not move at
all relative to a frame fixed to the other plate — the geometric factor
$\sin(\text{angular distance from pole})$ multiplies this value everywhere.

---

## ★2 — Perpendicularity

$$\boldsymbol{\Omega}\times\mathbf{r}
= \begin{pmatrix}
\Omega_y r_z - \Omega_z r_y \\
\Omega_z r_x - \Omega_x r_z \\
\Omega_x r_y - \Omega_y r_x
\end{pmatrix},
\qquad
\left(\boldsymbol{\Omega}\times\mathbf{r}\right)\cdot\mathbf{r}
= \Omega_y r_z r_x - \Omega_z r_y r_x + \Omega_z r_x r_y - \Omega_x r_z r_y
+ \Omega_x r_y r_z - \Omega_y r_x r_z .$$

Every term cancels in pairs, so the dot product is **identically zero** — no
trigonometry required. The geometric meaning is that a rigid rotation produces no
radial motion, which is exactly why the demonstration's vertical column is
$0.00\ \mathrm{mm\,yr^{-1}}$ at every station. The corollary for interpretation:
observed vertical motion is direct evidence against a purely rigid plate motion.

---

## ★3 — Three parameters and what residuals mean

A rigid rotation has an angular velocity vector with three components, and the
predicted velocity at every point is a linear function of those three components.
Two million stations therefore supply $2n$ observations for $3$ unknowns, and a
perfectly rigid plate is fitted exactly by a single vector. The residuals of a fit
are therefore the **non-rigid part**: internal deformation, elastic strain
accumulation (which is what makes continental interiors interesting), post-seismic
transients, and noise. A residual of $1.5\ \mathrm{mm\,yr^{-1}}$ is not "small" or
"large" in the abstract — it must be compared with the formal uncertainty of the
velocities and with the strain rate it implies over the network's aperture.

---

## ★4 — Pole $(50^{\circ},-120^{\circ})$ at $0.90^{\circ}\,\mathrm{Myr^{-1}}$

$$\left|\boldsymbol{\Omega}\right| = 0.90\times1.745329\times10^{-8}
= 1.5708\times10^{-8}\ \mathrm{rad\,yr^{-1}},$$

$$\boldsymbol{\Omega} = 1.5708\times10^{-8}
\begin{pmatrix}
\cos50^{\circ}\cos(-120^{\circ}) \\
\cos50^{\circ}\sin(-120^{\circ}) \\
\sin50^{\circ}
\end{pmatrix}
= 1.5708\times10^{-8}
\begin{pmatrix}
-0.3214 \\
-0.5566 \\
0.7660
\end{pmatrix}.$$

At $(0^{\circ}, 0^{\circ})$, $\mathbf{r} = (6.371\times10^{6}, 0, 0)\ \mathrm{m}$, so

$$\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r}
= 1.5708\times10^{-8}\times6.371\times10^{6}
\begin{pmatrix} 0 \\ 0.7660 \\ 0.5566 \end{pmatrix}
= \begin{pmatrix} 0 \\ 76.66 \\ 55.71 \end{pmatrix}\ \mathrm{mm\,yr^{-1}},$$

using the standard cross-product expansion. In the local ENU frame at the equator
on the prime meridian, $\hat{\mathbf{e}} = (0,1,0)$ and
$\hat{\mathbf{n}} = (0,0,1)$, giving

$$v_{\text{east}} = 76.66\ \mathrm{mm\,yr^{-1}},\qquad
v_{\text{north}} = 55.71\ \mathrm{mm\,yr^{-1}},$$

and $v_{\text{up}} = 0$ by the perpendicularity of ★2. The resulting horizontal
speed is $\sqrt{76.66^{2}+55.71^{2}} = \mathbf{94.77\ mm\,yr^{-1}}$, matching the
lesson's table exactly.

---

## ★5 — Relative pole of two plates

$$\boldsymbol{\Omega}_A = 0.60\times1.745329\times10^{-8}
\begin{pmatrix}\cos30\cos10 \\ \cos30\sin10 \\ \sin30\end{pmatrix}
= 1.0472\times10^{-8}\begin{pmatrix}0.8529\\0.1504\\0.5\end{pmatrix},$$

$$\boldsymbol{\Omega}_B = 0.40\times1.745329\times10^{-8}
\begin{pmatrix}\cos60\cos(-170)\\ \cos60\sin(-170)\\ \sin60\end{pmatrix}
= 6.9813\times10^{-9}\begin{pmatrix}-0.4924\\-0.0868\\0.8660\end{pmatrix}.$$

Subtracting,

$$\boldsymbol{\Omega}_{\text{rel}} = \boldsymbol{\Omega}_A-\boldsymbol{\Omega}_B
= \begin{pmatrix}
0.8931-(-0.3438)\\ 0.1575-(-0.0606)\\ 0.5236-0.6046
\end{pmatrix}\times10^{-8}
= \begin{pmatrix}1.2369\\0.2181\\-0.0810\end{pmatrix}\times10^{-8},$$

$$\left|\boldsymbol{\Omega}_{\text{rel}}\right| = 1.2586\times10^{-8}
\ \mathrm{rad\,yr^{-1}}
= \frac{1.2586\times10^{-8}}{1.745329\times10^{-8}}
= \mathbf{0.7211^{\circ}\,Myr^{-1}},$$

$$\text{latitude} = \arcsin\frac{-0.0810}{1.2586} = -3.7^{\circ},\qquad
\text{longitude} = \arctan2\left(0.2181,\;1.2369\right) = 10.0^{\circ}.$$

**Relative pole: $(-3.69^{\circ}, 10.00^{\circ})$ at $0.7211^{\circ}\,
\mathrm{Myr^{-1}}$** — the demonstration's values. The relative speed per Earth
radius is
$\left|\boldsymbol{\Omega}_{\text{rel}}\right|R = 1.2586\times10^{-8}\times6.371\times10^{6}
= \mathbf{80.2\ mm\,yr^{-1}}$, reached only at $90^{\circ}$ from the relative pole.

---

## ★6 — An unmodelled $0.05\ \mathrm{mas\,yr^{-1}}$ frame rotation

$$0.05\ \mathrm{mas\,yr^{-1}} = 0.05\times\frac{10^{-3}}{3600}\times\frac{\pi}{180}
= 2.424\times10^{-10}\ \mathrm{rad\,yr^{-1}},$$

so the induced speed is $\omega R\cos(\text{latitude})$ for a rotation about the
polar axis:

- at the equator: $2.424\times10^{-10}\times6.371\times10^{6} = 1.54\
  \mathrm{mm\,yr^{-1}}$;
- at $60^{\circ}$: $1.54\times\cos60^{\circ} = 0.77\ \mathrm{mm\,yr^{-1}}$.

**Is it mistaken for strain?** The velocity field of a rigid rotation has an
antisymmetric gradient and **zero strain**; if the analysis separates strain from
rotation properly (four or more well-spread stations, as in
[04 ★7](04-gnss-geodesy-applications-solutions.md)), a frame rotation lands only in
the rotation parameter and is harmless. If the analysis is naive — a
finite-difference shear estimate from a three-station array — the rotation enters
the shear directly as $+\omega = 2.4\times10^{-10}\ \mathrm{yr^{-1}}$, i.e.
$0.24\ \mathrm{nstrain\,yr^{-1}}$, which is small compared with typical tectonic
rates ($10$–$100\ \mathrm{nstrain\,yr^{-1}}$) but comparable with the noise floor
of a very good network. **The size is therefore not alarming; the risk is the
*attribution*.**

---

## ★7 — Distinguishing plate rotation from $10\ \mathrm{nstrain\,yr^{-1}}$

**The test.** Fit the Euler vector to the five station velocities; the residuals
are the non-rigid part. The strain implied by those residuals over the network
aperture $L$ is

$$e \approx \frac{\Delta v}{L} = \frac{2\times1.5\ \mathrm{mm\,yr^{-1}}}{L},$$

(the factor 2 for a difference of two stations). For a $200\ \mathrm{km}$ network
this gives

$$e \approx \frac{3\times10^{-3}}{2\times10^{5}} = 1.5\times10^{-8}
= 15\ \mathrm{nstrain\,yr^{-1}},$$

which is larger than the $10\ \mathrm{nstrain\,yr^{-1}}$ hypothesis but only
marginally; for a $500\ \mathrm{km}$ network it is $6\ \mathrm{nstrain\,yr^{-1}}$,
smaller than the hypothesis.

**Conclusion.** With residuals of $1.5\ \mathrm{mm\,yr^{-1}}$ the network
*bounds* internal deformation at the few-nstrain level per year only if it is
large: the test is the ratio of $\Delta v$ to $L$, so a sparse network is more
sensitive to strain than a dense one — the opposite of the intuition that more
stations help. What is needed to *decide* rather than bound:

1. **A stated velocity uncertainty** — $1.5\ \mathrm{mm\,yr^{-1}}$ residuals are
   meaningless without knowing whether the formal errors are $0.3$ or
   $3\ \mathrm{mm\,yr^{-1}}$.
2. **A deformation model with a spatial pattern** (e.g. steady strain accumulation
   across a known boundary) rather than a single uniform-strain number.
3. **Enough stations to estimate the gradient** — at least four independent
   directions, as in [04 ★7](04-gnss-geodesy-applications-solutions.md), otherwise
   rotation and shear are entangled and the "residual" has no unique meaning.
4. **An independent check** — seismicity, geology, or a denser sub-network.

---

## ★8 — Designing a network for a $0.5\%$ rate accuracy

**Target.** Rate to $0.5\%$ and pole position to $1^{\circ}$, with
$1\ \mathrm{mm\,yr^{-1}}$ velocity noise.

**From the observability table** (lesson §4):

| stations | rate error (%) | $\sigma_{\boldsymbol{\Omega}}$ (rad/yr) |
|---|---|---|
| 1 | 1.698 | $2.891\times10^{-9}$ |
| 2 | 0.000 | $2.991\times10^{-10}$ |
| 3 | 0.000 | $1.853\times10^{-10}$ |
| 8 | 0.000 | $1.126\times10^{-10}$ |

Two stations already achieve better than $0.5\%$ in rate, because the rate is a
*global scale* of the velocity field and is well constrained as soon as the
stations are not at the pole. The binding requirement is the **pole position**,
which is set by the *spread*, not the count.

**Geometry condition.** The stations must span at least a hemisphere of azimuth
and a wide range of latitude, so that the three columns of the design matrix are
independent: formal statement — the matrix
$\mathbf{B} = [\mathbf{k}_1\times\mathbf{r}_i,\ \mathbf{k}_2\times\mathbf{r}_i,\
\mathbf{k}_3\times\mathbf{r}_i]$ must be well conditioned, which fails when all
stations share a common radius direction (the null direction measured in the
lesson's one-station row).

**Design:** $\ge8$ stations at sites separated by $\ge30^{\circ}$ of latitude and
spread over $\ge180^{\circ}$ of azimuth, all in the plate interior to minimise
internal deformation. From the table's noise scaling
($\sigma_{\boldsymbol{\Omega}}$ falls by $26\times$ from one to eight stations),
eight stations at $1\ \mathrm{mm\,yr^{-1}}$ noise are comfortably inside the
target, with margin to trade stations for record length.

**Frame requirements:**

1. **A stated realisation and epoch** for the velocities; an unmodelled frame
   rotation of even $0.05\ \mathrm{mas\,yr^{-1}}$ adds
   $1.5\ \mathrm{mm\,yr^{-1}}$ at the equator (★6), i.e. more than the noise.
2. **Consistency between the plate-motion solution and the frame's own
   definition** — if the same stations define the frame and the plate motion, the
   result is circular; use independent global stations or a published frame.
3. **A noise model** for each velocity, since the pole uncertainty scales with the
   velocity errors and not with their formal values.
4. **A published uncertainty** on the pole and rate, ideally as a covariance
   ellipse on the pole position, so others can propagate it.
