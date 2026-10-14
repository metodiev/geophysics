# Solutions — 02-07-05 Electromagnetic Waves, Impedance and Polarisation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Convention: $e^{+i\omega t}$, so a downgoing wave
> is $\propto e^{-ikz}$ and the half-space impedance is $\propto(1+i)$.

Constants: $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A²,
$\varepsilon_0 = 8.854\,187\,812\,8\times10^{-12}$ F/m,
$c = 299\,792\,458$ m/s, $\eta_0 = 376.730\,314$ Ω.

---

## ★1 — Plane wave in vacuum

**(a)** $k = \omega/c = 2\pi\times10^{8}/2.997\,924\,58\times10^{8}
= 2.095\,845$ rad/m, $\lambda = 2\pi/k = 2.9979$ m — the demo prints exactly these.

**(b)** From Faraday, $\mathbf B = \mathbf k\times\mathbf E/\omega$, so
$\mathbf B = B_0\hat{\mathbf y}e^{i(kz-\omega t)}$ with
$B_0 = E_0/c = 10/2.997\,924\,58\times10^{8} = 3.335\,64\times10^{-8}$ T
(33.4 nT). Same phase as $\mathbf E$.

**(c)** $E/B = 10/3.335\,64\times10^{-8} = 2.998\times10^{8}$ m/s $= c$ ✓. Units:
$\mathrm{(V/m)/T = V\,s/m^2}$; since $\mathrm{T = V\,s/m^2}$, the ratio is in m/s.

**(d)** $\mathbf E\perp\mathbf B\perp\hat{\mathbf k}$: all three mutually
orthogonal. Right-handedness means $\mathbf E\times\mathbf B$ points along
$\hat{\mathbf k}$ (the direction of energy flow, $\mathbf S = \mathbf E\times\mathbf H$),
so specifying $(\mathbf E,\mathbf B)$ fixes the propagation direction and there is
no ambiguity in the sign of $\mathbf k$.

---

## ★2 — Wave impedance

**(a)** $\eta_0 = \sqrt{1.256\,637\,062\,12\times10^{-6}/8.854\,187\,812\,8\times10^{-12}}
= 376.730\,314$ Ω, and $\mu_0c = (1.256\,637\,062\,12\times10^{-6})
(2.997\,924\,58\times10^{8}) = 376.730\,314$ Ω. The demo prints the two numbers and
their difference, $8.2\times10^{-12}$ Ω — an identity to within the rounding of the
tabulated constants.

**(b)** $\eta = \eta_0/\sqrt{\varepsilon_r}$:

| $\varepsilon_r$ | 1 | 4 | 20 | 81 |
|---|---|---|---|---|
| $\eta$ (Ω) | 376.7303 | 188.3652 | 84.2395 | 41.8589 |
| $H_0$ for $E_0 = 1$ V/m (A/m) | $2.6544\times10^{-3}$ | $5.3088\times10^{-3}$ | $1.1871\times10^{-2}$ | $2.3890\times10^{-2}$ |

The impedance falls as $1/\sqrt{\varepsilon_r}$; a denser dielectric carries a
larger magnetic field for the same electric field.

**(c)** See the table above: $H_0 = E_0/\eta$.

**(d)** $[\mathbf E/\mathbf H] = \mathrm{(V/m)/(A/m) = V/A = \Omega}$ ✓.
$[\mathbf E/\mathbf B] = \mathrm{(V/m)/T} = \mathrm{(V/m)/(V\,s\,m^{-2})} =
\mathrm{m/s}$ ✓. The two ratios differ by $\mu$, which is why "the ratio of E to B
is c" and "the ratio of E to H is the wave impedance" are different statements.

---

## ★3 — Half-space MT

**(a)** $\delta = \sqrt{\rho T/(\pi\mu_0)} = 503.292\sqrt{\rho T}$ m with $\rho$ in
Ω·m and $T$ in s: $\delta(1\ \mathrm s) = 5033$ m, $\delta(10\ \mathrm s) = 15\,915$ m,
$\delta(100\ \mathrm s) = 50\,329$ m — the demo's values.

**(b)** $|Z| = \sqrt{\omega\mu_0\rho}$: at $T = 1$ s,
$|Z| = \sqrt{(2\pi)(1.2566\times10^{-6})(100)} = 2.8099\times10^{-2}$ Ω; at 10 s,
$8.8858\times10^{-3}$ Ω; at 100 s, $2.8099\times10^{-3}$ Ω. In every case the phase
is $+45.0000°$ (the demo prints exactly this).

**(c)** $\rho_a = |Z|^2/(\omega\mu_0)$: at $T = 1$ s,
$(2.8099\times10^{-2})^2/((2\pi)(1.2566\times10^{-6})) = 100.000\,000$ Ω·m; the
demo reports 100.000000 at all seven periods from 1 ms to 1000 s.

**(d)** A uniform half-space gives no depth information: the response is the same
shape at every period, differing only by the $\omega^{-1/2}$ scaling of $|Z|$. The
information in an MT sounding lies *entirely* in the departures of
$(\rho_a,\phi)$ from a constant–45° pair, and the depth comes from the *period* at
which each departure occurs, through $\delta(T)$.

---

## ★4 — Normal-incidence reflection

**(a)** Continuity of tangential $\mathbf E$ and $\mathbf H$ across the interface
gives $E_i+E_r = E_t$ and $(E_i-E_r)/\eta_1 = E_t/\eta_2$, hence
$r = E_r/E_i = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and $t = 1+r$. For lossless
non-magnetic dielectrics $\eta = \eta_0/\sqrt{\varepsilon_r}$, so

$$r = \frac{1/\sqrt{\varepsilon_2}-1/\sqrt{\varepsilon_1}}
{1/\sqrt{\varepsilon_2}+1/\sqrt{\varepsilon_1}}
= \frac{\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2}} .$$

**(b)** $4\to25$: $r = (2-5)/(2+5) = -0.428\,571$; $R = 0.183\,673$, i.e. **18.4 %**
of the incident energy reflected, with a phase of $180°$ (a sign inversion, so the
reflected pulse has inverted polarity in the record).

**(c)** $4\to1$: $r = (2-1)/(2+1) = +0.333\,333$; $R = 0.111\,111$, 11.1 %, no
inversion.

**(d)** The $4\to25$ contrast is both stronger in amplitude and phase-inverted,
which makes it the most recognisable event in a near-surface GPR section (the water
table). The $4\to1$ reflection is the ground–air interface: it is in every record,
it is what antenna shielding suppresses, and it is the reason the first arrival is
usually dominated by an artefact rather than a geological interface.

---

## ★5 — Polarisation

**(a)** With $a_x = 1$, $a_y = 0.5$, $\phi = 45°$:

$$S_0 = 1^2+0.5^2 = 1.25, \quad S_1 = 1^2-0.5^2 = 0.75, \quad
S_2 = 2(1)(0.5)\cos45° = 0.707\,107, \quad S_3 = 2(1)(0.5)\sin45° = 0.707\,107 .$$

**(b)** $0.75^2+0.707\,107^2+0.707\,107^2 = 0.5625+0.5+0.5 = 1.5625 = 1.25^2$ ✓.
The demo verifies this identity to $0.00\times10^{0}$ for all five test states.

**(c)** $S_3\neq0$ and $|S_3| < S_0$, so the state is **elliptical**. The polarisation
angle is $\psi = \tfrac12\arctan(S_2/S_1) = \tfrac12\arctan(0.9428) = 21.66°$, and
the ellipticity angle is $\chi = \tfrac12\arcsin(S_3/S_0)
= \tfrac12\arcsin(0.5657) = 17.22°$ (the axial ratio is
$\tan\chi = 0.31$, so about 3.2:1).

**(d)** The incident natural field is only partially coherent and its polarisation
carries no information about the ground. The *response* polarisation does: an
isotropic 1-D Earth returns a response independent of the incident polarisation,
whereas a 2-D or 3-D Earth couples the components, so the same incident field
produces different responses in different polarisations. That dependence — the
impedance tensor, the tipper, the skew — is the diagnostic of lateral
heterogeneity, and it is why MT practice collects two orthogonal horizontal
components of both fields.

---

## ★6 — Two-layer response

**(a)** From the demo (100 Ω·m to 5 km over 1000 Ω·m):

| $T$ (s) | $\delta_1$ (m) | $\rho_a$ (Ω·m) | $\phi$ (°) |
|---|---|---|---|
| 0.01 | 503.3 | 100.0000 | 45.0000 |
| 1 | 5032.9 | 89.1619 | 37.5384 |
| 10 | 15 915.5 | 242.7250 | 25.5616 |
| 100 | 50 329.2 | 582.1488 | 33.3941 |
| 1000 | 159 154.9 | 837.1178 | 40.4032 |

**(b)** $T_{\text{cross}} = \pi\mu_0d^2/\rho_1
= \pi(1.2566\times10^{-6})(5000)^2/100 = 0.9870$ s. The table shows the departure
beginning exactly there: at $T = 0.1$ s ($\delta_1 = 1591$ m, much less than the
5000 m layer) the response is still the half-space one; by $T = 1$ s
($\delta_1\approx d$) it has moved.

**(c)** The phase dips below 45° because the response is a *sum* of the contribution
from the conductive first layer (45°) and the deeper resistive half-space (also 45°
at its own frequencies, but the two are not in phase at the surface). Their
interference produces a total phase *less* than 45° in the transition. At long
period the field penetrates the layer almost without attenuation and the response
approaches the 45° of the resistive basement, but only asymptotically — at
$T = 1000$ s the phase is still only 40.4°.

**(d)** Because $\rho_a$ is an amplitude-only, non-unique combination: many
different layered models give the same $\rho_a(T)$ over a limited band, whereas the
phase constrains *where* in depth the change occurs. A practical rule: a resistivity
change produces a $\rho_a$ anomaly spread over a decade of period, but a phase
extremum at a period that locates the interface far more sharply. This is why MT
inversions weight the phase as heavily as the amplitude.

---

## ★7 — Lossy-medium impedance

**(a)** $\eta = \sqrt{i\omega\mu_0/(\sigma+i\omega\varepsilon)}$ with
$\sigma = 0.01$ S/m, $\varepsilon = 20\varepsilon_0$:

| $f$ (Hz) | $\omega\varepsilon/\sigma$ | $\eta$ (Ω) | $|\eta|$ (Ω) | phase (°) |
|---|---|---|---|---|
| $10^{3}$ | $1.1\times10^{-4}$ | $0.62835+0.62828i$ | 0.8886 | 44.9968 |
| $8.99\times10^{6}$ | 1.000 | $65.445+27.108i$ | 70.837 | 22.4999 |
| $10^{8}$ | 11.13 | $83.986+3.767i$ | 84.070 | 2.5678 |

**(b)** The lossless value is $\eta_0/\sqrt{20} = 84.2395$ Ω with phase 0. At
$10^{3}$ Hz the impedance is 0.8886 Ω — two orders of magnitude below it, because
the medium is a conductor at that frequency. At $8.99$ MHz it is 70.84 Ω, still
16 % below. At $10^{8}$ Hz it is 84.07 Ω, within 0.2 % of lossless, and the phase
has fallen to 2.6°.

**(c)** $10^{3}$ Hz:
$\sigma/(\omega\varepsilon) = 1.1\times10^{4}\gg1$ — strongly diffusive, phase
$\to45°$. $8.99$ MHz: $\sigma/(\omega\varepsilon) = 1$ — the crossover. $10^{8}$ Hz:
$\sigma/(\omega\varepsilon) = 0.09\ll1$ — wave-like, phase $\to0$. At the crossover
the phase is **22.5°**, exactly half of 45°, because
$\eta\propto\sqrt i/\sqrt{1+i}$ contributes $45°-22.5°$. So the phase of the
impedance is a continuous, monotonic indicator of regime, going from 45° (diffusive)
to 0° (propagating).

**(d)** Because the phase is independent of the source amplitude and of any
frequency-independent calibration error, it is a *clean* observable; and because it
varies monotonically across the crossover, a single number tells you which physics
to use. This is why MT and controlled-source practitioners routinely plot phase
first, and why a GPR practitioner working at 100 MHz in wet soil should expect a
few degrees — not zero — of impedance phase, i.e. a slightly lossy wave.

---

## ★8 — Source cancellation

**(a)** If the incident field amplitude scales by a factor $\lambda$ (a stronger
ionospheric current system), then both $\mathbf E$ and $\mathbf H$ at the surface
scale by the same $\lambda$, because the surface fields are linearly related to the
source and the ground response is linear. Hence $Z = E/H$ is unchanged. More
formally, in the plane-wave decomposition the source enters only as an overall
amplitude of the mode, not in its spatial structure.

**(b)** $\rho_a\propto|Z|^2$, so
$\mathrm d\ln\rho_a/\mathrm d\ln|Z| = 2$: a 10 % error in $|Z|$ gives a **21 %**
error in $\rho_a$. (The demo's formula $\rho_a = |Z|^2/(\omega\mu_0)$ makes this
immediate.)

**(c)** A correlated error (both fields 10 % high, e.g. from a common gain error or
an underestimated sensor spacing) cancels exactly in the ratio. Uncorrelated errors
— independent noise on the two channels, sensor misorientation, or local
distortion of one field — propagate to $|Z|$ and hence to $\rho_a$ with the factor
2 of (b). This is why MT practice invests heavily in remote reference channels and
robust estimation rather than in absolute calibration.

**(d)** Two standard failures: (i) near a coastline, where the ocean–continent
boundary distorts the induced currents so that the fields are not a uniform plane
wave — ignoring it biases the apparent resistivity *downward* on land near the
coast (the "coast effect"); (ii) under the auroral electrojet at high latitude,
where the source has a finite width and a preferred direction — ignoring it biases
$\rho_a$ *upward*, the "source effect". Both are systematic, frequency-dependent and
correlated with period, which is what makes them dangerous: they look like
structure.

---

## ★9 — The impedance recursion

**(a)** In each layer the field is a sum of downgoing and upgoing waves,
$E_x = A_je^{-\gamma_jz}+B_je^{+\gamma_jz}$, with
$\gamma_j = \sqrt{i\omega\mu_0/\rho_j} = (1+i)/\delta_j$ taking the positive real
part. Faraday's law gives the companion magnetic field,
$\partial E_x/\partial z = -i\omega\mu_0H_y$, so the impedance is

$$Z_j \equiv \frac{E_x}{H_y} = -\frac{i\omega\mu_0E_x}{\partial E_x/\partial z} ,$$

and for a single downgoing wave ($\partial E_x/\partial z = -\gamma_jE_x$) this
reduces to $Z_j = i\omega\mu_0/\gamma_j = \sqrt{i\omega\mu_0\rho_j} \equiv \eta_j$
— the intrinsic impedance of the layer, with a 45° phase. Matching $E_x$ and $H_y$
at each interface (both tangential components are continuous when there is no
surface current) and eliminating $A_j$, $B_j$ gives the standard recursion

$$Z_j = \eta_j\frac{Z_{j+1}+\eta_j\tanh(\gamma_jh_j)}
{\eta_j+Z_{j+1}\tanh(\gamma_jh_j)},
\qquad
\eta_j = \sqrt{i\omega\mu_0\rho_j} ,$$

with the bottom layer initialised as $Z_N = \eta_N$ (a half-space admits only the
downgoing wave, so its impedance is its intrinsic impedance).

**(b)** At $T = 10$ s: $\omega = 0.6283$ rad/s,
$\gamma_1h_1 = (1+i)(h_1/\delta_1)$; numerically $\delta_1 = 15\,915.5$ m, so
$\gamma_1h_1 = (1+i)(5000/15\,915.5) = 0.3142+0.3142i$, whence
$\tanh(\gamma_1h_1) = 0.333\,079+0.291\,996i$.
$\eta_1 = \sqrt{i\omega\mu_0\rho_1} = 0.006\,2832+0.006\,2832i$ Ω and
$\eta_2 = \sqrt{i\omega\mu_0\rho_2} = 0.019\,8692+0.019\,8692i$ Ω. Substituting:

$$Z = 0.012\,489+0.005\,973i\ \Omega, \qquad |Z| = 0.013\,8437\ \Omega ,$$

so $\rho_a = |Z|^2/(\omega\mu_0) = 242.7250$ Ω·m and
$\phi = 25.5616°$ — matching the demo's two entries exactly.

**(c)** If the layer is very resistive or very thick, $\gamma_1h_1\to\infty$,
$\tanh\to1$, and for a *uniform* half-space the recursion returns $Z = \eta_1$
identically (the demo verifies $\rho_a = 100.000000$ and $\phi = 45.0000°$ for the
one-layer case at every period). If the layer is very conductive or very thin,
$\gamma_jh_j\to0$, $\tanh\to\gamma_jh_j$, and the layer acts as a thin sheet: its
effect enters through the combination $\sigma h$ (a conductance) rather than
through $\sigma$ and $h$ separately. That is the basis of the thin-sheet
approximation used for sedimentary basins and for the ocean layer in marine MT.

**(d)** The recursion is a fast, exact forward solver for 1-D models, so any
inversion — Monte Carlo, Occam, gradient-based — needs it (or an equivalent) as the
forward operator. Analytic inversion is not available in general because the same
$(\rho_a,\phi)$ curve can be produced by many different layered models: this is the
classical **equivalence** of MT (a thin conducting layer is equivalent to a thicker
or more conductive one to within a trade-off), and it is why MT results are
reported as an ensemble or with an explicit regularisation rather than as a unique
layer stack.

---

## ★10 — The impedance tensor

**(a)** $E_i = Z_{ij}H_j$ with $E_x = Z_{xx}H_x+Z_{xy}H_y$ and
$E_y = Z_{yx}H_x+Z_{yy}H_y$. The four elements are the impedance tensor components:
$Z_{xy}$, $Z_{yx}$ the "principal" (cross) elements that carry the layered response,
and $Z_{xx}$, $Z_{yy}$ the "diagonal" elements, zero for a 1-D Earth and a measure
of two- and three-dimensionality.

**(b)** A 1-D (layered) Earth has no preferred horizontal direction: the response
cannot distinguish an axis, so the linear map from $\mathbf H$ to $\mathbf E$ must
be a scalar multiple of the rotation matrix — i.e. $Z_{xx} = Z_{yy} = 0$ and
$Z_{xy} = -Z_{yx} = Z$. Physically: the induced currents form horizontal loops whose
geometry is set by the layering alone, so the field relations are unchanged when
the whole configuration is rotated.

**(c)** With strike along $y$: the **E-polarisation** (or TE) mode has
$\mathbf E$ parallel to strike, and is measured by $Z_{xy}$ (with $E_x$, $H_y$);
the **B-polarisation** (or TM) mode has $\mathbf H$ parallel to strike, measured by
$Z_{yx}$ (with $E_y$, $H_x$). They respond differently because in TE the
induced currents flow along strike (unaffected by the discontinuity) whereas in TM
the currents must cross the interface and charge piles up there, making TM far more
sensitive to the lateral boundary. That asymmetry — TE smooth, TM sharp — is the
signature of a 2-D structure and the basis of the standard 2-D inversion.

**(d)** The **tipper** $\mathbf T$ relates the vertical to the horizontal magnetic
components: $H_z = T_xH_x+T_yH_y$; a non-zero tipper means the horizontal field has
been rotated out of the horizontal plane, i.e. lateral gradients in conductivity,
and its real part indicates the direction of the lateral contrast. The **skew**
measures how much the diagonal elements break the 1-D/2-D symmetry, i.e. it
diagnoses three-dimensionality. The vertical field adds information because it is
not part of the $2\times2$ $E$–$H$ relation at all: it is a fourth independent
quantity that responds to gradients (rather than to absolute values) of
conductivity, and it is therefore the most sensitive indicator of small-scale
lateral structure — including, usefully, of buried metallic infrastructure that a
naive MT inversion would otherwise map into the Earth.
