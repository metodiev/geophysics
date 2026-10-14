# Solutions — 07-05-02 GOCE, Gravity Gradients and the Static Field

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are **SYNTHETIC** teaching values.

Lesson: [02 GOCE, Gravity Gradients and the Static Field](../02-goce.md).

---

## ★1 — Monopole tensor at $h = 300\ \mathrm{km}$

$$r = R + h = 6371 + 300 = 6671\ \mathrm{km} = 6.671\times10^{6}\ \mathrm{m},$$
$$r^{3} = 2.96874\times10^{20}\ \mathrm{m^{3}},$$
$$\frac{GM}{r^{3}} = \frac{3.986004418\times10^{14}}{2.96874\times10^{20}}
= 1.342657\times10^{-6}\ \mathrm{s^{-2}} = 1342.66\ \mathrm{E},$$
$$\Gamma_{rr} = +\frac{2GM}{r^{3}} = +2.68531\times10^{-6}\ \mathrm{s^{-2}}
= +2685.31\ \mathrm{E},$$
$$\Gamma_{tt} = \Gamma_{cc} = -\frac{GM}{r^{3}}
= -1.342657\times10^{-6}\ \mathrm{s^{-2}} = -1342.66\ \mathrm{E}.$$

**Trace:** $2685.31 - 1342.66 - 1342.66 = -0.01\ \mathrm{E}$, i.e. zero to the
rounding of the printed values ($2.68531 - 2\times1.342657 = -4\times10^{-9}$
in $\mathrm{s^{-2}}$ units of $10^{-6}$, i.e. exact to the digits given).

---

## ★2 — Trace of a point-mass Hessian

With $\mathbf{q} = \mathbf{r} - \mathbf{r}_m$ and $q = |\mathbf{q}|$,

$$\frac{\partial \phi}{\partial x_i} = Gm\,\frac{q_i}{q^{3}},$$

$$\frac{\partial^{2}\phi}{\partial x_i\partial x_j}
= Gm\left[\frac{\delta_{ij}}{q^{3}} - \frac{3q_i q_j}{q^{5}}\right].$$

Setting $i = j$ and summing,

$$\nabla^{2}\phi = Gm\left[\frac{3}{q^{3}} - \frac{3q^{2}}{q^{5}}\right]
= Gm\left[\frac{3}{q^{3}} - \frac{3}{q^{3}}\right] = 0 . \qquad\blacksquare$$

The result is valid for $q \ne 0$: **the use of $\boldsymbol{q} \ne \mathbf{0}$ is
the assumption**. At the mass itself the field is singular, and Laplace's
equation is a statement about the *vacuum region* only — which is why a satellite
must be outside the Earth, and why a gradiometer flying *through* a dense body
would measure a nonzero trace proportional to the local mass density
($\nabla^{2}U = -4\pi G\rho$).

---

## ★3 — Reading the synthetic tensor

Largest component: $8.5566\times10^{-10}\ \mathrm{s^{-2}}
= 8.5566\times10^{-10}/10^{-9}\ \mathrm{E} = 0.85566\ \mathrm{E}$.

Trace: $8.5566 - 3.6890 - 4.8676 = 0.0000$ (units $10^{-10}\ \mathrm{s^{-2}}$),
so the trace is $0$ to the printed precision — the finite-difference construction
that produced it is consistent. (The demonstration reports the residual
explicitly: $3.4\times10^{-17}\ \mathrm{s^{-2}}$, i.e. $3.4\times10^{-8}\
\mathrm{E}$, a ratio of $4.0\times10^{-8}$ to the largest component.)

**The off-diagonal $G_{xz}$:** a nonzero $G_{xz}$ means the principal axes of the
curvature are *not* aligned with the coordinate axes — here the synthetic mass is
a zonal (rotationally symmetric) term evaluated at co-latitude $40^\circ$, so the
tilt is the geometric consequence of being off the equator. A nonzero $G_{xz}$
therefore contains information about the *angular* structure of the field, and it
is one of the five independent components.

---

## ★4 — Peak of $T(l)$ at $h = 400\ \mathrm{km}$

$a = 6771\ \mathrm{km}$, $a/R = 1.062785$, $\ln(a/R) = 0.060892$.

**Exact.** Solve $\dfrac{1}{l+1} + \dfrac{1}{l+2} = 0.060892$:
$$\frac{2l+3}{(l+1)(l+2)} = c
\;\Longrightarrow\; c\,l^{2} + (3c-2)l + (2c-3) = 0,$$
$$0.060892\,l^{2} - 1.817324\,l - 2.878216 = 0
\;\Longrightarrow\; l^{*} = 31.35 .$$

**Crude.** $l^{*} \approx 2/\ln(a/R) = 2/0.060892 = 32.84$.

The crude approximation is **high by $1.5$ degrees ($+4.8\%$)**, because it
replaces the sum $\frac{1}{l+1}+\frac{1}{l+2}$ by $\frac{2}{l}$, which
overestimates the derivative for small $l$. At $250\ \mathrm{km}$ the same
comparison was $52.0$ against $50.5$ ($+3\%$); the crude form is always high.

---

## ★5 — Usable degree at $h = 350\ \mathrm{km}$

$a/R = 6721/6371 = 1.054937$, $\ln(a/R) = 0.053481$. Evaluating
$T(l) = (l+1)(l+2)(R/a)^{l+2}$, $A_s(l) = 10^{-10}(2/l)^{1.5}$,
$\sigma_l = 0.10\,\mathrm{E}/\sqrt{2l+1}$ and requiring
$A_s T/\sigma_l > 1$:

- highest degree with S/N $> 1$: $l = 112$
- half-wavelength: $\pi R/l = \pi(6371)/112 = 179\ \mathrm{km}$
- S/N at $l = 50$: $13.21$; at $l = 100$: $1.77$.

Compare with $h = 250\ \mathrm{km}$: $l_{\max} = 167$ ($120\ \mathrm{km}$) and
S/N at $l = 100$ of $8.2$.

**Reason for the difference:** the extra $100\ \mathrm{km}$ of altitude
attenuates every degree by a further factor $(R/a)^{l}$, which at $l = 100$ is
$(1.03924/1.05494)^{100} = e^{100(-0.0150)} = 0.22$ — a factor $4.6$ of signal
lost for the same instrument, so the degree at which S/N falls below 1 drops from
$167$ to $112$.

---

## ★6 — A quoted degree 200 is not information at degree 200

With $a/R = 1.03924$ ($h = 250\ \mathrm{km}$):

$$T(50) = (51)(52)(1.03924)^{-52} = 2652 \times 0.13514 = 358.4,$$
$$T(200) = (201)(202)(1.03924)^{-202} = 40602 \times 4.20\times10^{-4}
= 17.06 .$$

Ratio: $358.4/17.06 = 21.0$, so a surface coefficient at degree $200$ produces
$1/21$ of the curvature that the *same* coefficient would produce at degree
$50$. (The demonstration's tabulated values, $347.8$ at $l = 60$ and $17.1$ at
$l = 200$, are the same statement on its slightly different sampling.)

**Why a quoted degree is not evidence:** a solution can be *formally* complete to
degree $200$ while the coefficients above the noise crossover (measured here as
$l \approx 167$ at $250\ \mathrm{km}$, from $4.19$ at $l = 50$ downward) are
determined almost entirely by the regularisation, not by data. The correct
reading of "degree 200" is "the model space extends to degree 200"; the correct
question is "at what degree does the signal-to-noise ratio fall below 1 for
*this* spectrum and *this* noise?", and that number must be computed.

---

## ★7 — Altitude versus noise (specification)

1. **Grid.** Altitudes $h \in \{225, 250, 275, 300, 350, 400, 450, 500\}\
   \mathrm{km}$; per-component noise
   $\sigma \in \{0.01, 0.03, 0.1, 0.3, 1.0\}\ \mathrm{E}$.
2. **Metric.** $l_{\max}(\text{S/N} > 1)$ for a *fixed* synthetic surface
   spectrum (hold $A_s(l)$ constant across the grid, so that only the two
   manipulated variables change), and the half-wavelength $\pi R/l_{\max}$.
3. **Prediction.** $\ln l_{\max}$ is approximately linear in
   $\ln \sigma$ with a small slope, and strongly dependent on $h$: a factor of
   $10$ in noise moves $l_{\max}$ by only a few degrees, while $100\ \mathrm{km}$
   of altitude moves it by $50$ degrees. The contours of constant $l_{\max}$ in
   the $(h,\sigma)$ plane are therefore nearly horizontal: **altitude buys
   resolution, noise does not.**
4. **What a single mission leaves undetermined.** With one altitude and one noise
   level you measure a single point in that plane. You cannot distinguish "this
   instrument is noise-limited at degree 170" from "this orbit is
   attenuation-limited at degree 170", and you have no way to check whether the
   surface spectrum you assumed is the right one — a wrong $A_s(l)$ shifts the
   whole answer. Two missions at different altitudes, or one mission with a
   varying altitude, are what break the degeneracy.

---

## ★8 — Separating a scale error from a force-model error

The trace alone cannot separate the two because both contribute additively:

$$\operatorname{tr}\boldsymbol{\Gamma}_{\text{meas}}
= \underbrace{\sum_i \epsilon_i \Gamma_{ii}}_{\text{scale errors}}
+ \underbrace{\text{(modelled non-gravitational terms)}}_{\text{force-model error}} .$$

**A separating measurement:** the non-gravitational part of the tensor is *not*
trace-free in the satellite frame — a linear acceleration $\mathbf{f}$ projected
onto the three instrument axes contributes a diagonal term proportional to
$\mathbf{f}$ and the boom geometry — whereas a *scale* error multiplies the
already trace-free quantity. So:

1. **Regress the measured trace against an independently measured
   non-gravitational acceleration.** A satellite carries accelerometers (or can
   infer drag/radiation from orbit dynamics). Project the measured acceleration
   onto the three gradient axes and fit the trace against those three
   components.
2. **What distinguishes them:** the part of the trace *explained* by the
   independently measured acceleration is a force-model error and can be
   modelled out component by component; the residual part that survives, and
   that scales with the *signal* ($\Gamma_{rr}$), is a scale error.
3. **The decisive observation:** a scale error is proportional to the true
   diagonal components, so it varies with the orbital position exactly as
   $\Gamma_{rr}$ does (maximum at the equator... in fact as the monopole term,
   which is nearly constant in radius but has a known orientation signature),
   while a force-model error varies with the *attitude and density*, i.e. with a
   different and largely independent time signature. Fitting the trace against
   both sets of basis functions separates them.
4. **Residual test:** after removing the fitted force model, the remaining trace
   should be at the $\sqrt{2}\sigma$ level of Section 8 of the lesson. If it is
   not, the model is still incomplete — and this is a test the data can always
   perform.
