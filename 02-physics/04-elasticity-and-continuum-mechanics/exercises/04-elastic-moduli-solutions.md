# Solutions — 02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — From $K$ and $\mu$

**(a)** $\lambda = K-2\mu/3 = 40-16.666667 = 23.333333$ GPa;
$M = K+4\mu/3 = 40+33.333333 = 73.333333$ GPa;
$E = 9K\mu/(3K+\mu) = 9\times40\times25/(120+25) = 9000/145 = 62.068966$ GPa;
$\nu = (3K-2\mu)/(2(3K+\mu)) = (120-50)/290 = 0.241379$.

**(b)** $v_p = \sqrt{73.333333\times10^9/2600} = \sqrt{2.820513\times10^7} =
5310.85$ m s⁻¹; $v_s = \sqrt{25\times10^9/2600} = \sqrt{9.615385\times10^6} =
3100.87$ m s⁻¹.

**(c)** $v_p/v_s = 5310.85/3100.87 = 1.712703$;
$\sqrt{M/\mu} = \sqrt{2.933333} = 1.712668$;
$\sqrt{2(1-\nu)/(1-2\nu)} = \sqrt{2\times0.758621/0.517241} = \sqrt{2.933333} =
1.712668$ ✓ (the tiny difference from the first form is printed rounding).

**(d)** $\nu = 0.2414$ is just below 0.25, so this material is very close to a
Poisson solid ($v_p/v_s = 1.7127$ against $\sqrt3 = 1.7321$).

---

## ★2 — Sensitivity of $K$ to $\nu$

**(a)** $\mu = E/[2(1+\nu)] = 50/2.6 = 19.230769$ GPa;
$K = E/[3(1-2\nu)] = 50/(3\times0.4) = 41.666667$ GPa.

**(b)** $\mu$ depends on $1/(1+\nu)$, whose fractional change for a change in
$\nu$ is $\Delta\nu/(1+\nu)$: for $\Delta\nu = 0.01$ that is 0.00769, i.e.
0.77 per cent. $K$ depends on $1/(1-2\nu)$, whose fractional change is
$2\Delta\nu/(1-2\nu) = 0.02/0.4 = 0.05$, i.e. **5 per cent** — 6.5 times larger.
With $\nu = 0.31$, $K = 50/(3\times0.38) = 43.859649$ GPa, a 5.3 per cent
increase, while $\mu$ becomes 19.083969 GPa, a 0.76 per cent decrease. Confirmed.

**(c)** $v_p/v_s = \sqrt{2(1-\nu)/(1-2\nu)} = \sqrt{1.4/0.4} = \sqrt{3.5} =
1.870829$.

**(d)** $v_p/v_s = \sqrt2$ requires $2(1-\nu) = 1-2\nu$, which holds only at
$\nu = 0$... substituting gives $2-2\nu = 1-2\nu$, i.e. $2 = 1$: no solution.
Recheck: the ratio squared is $2(1-\nu)/(1-2\nu)$; setting it to 2 gives
$2(1-\nu) = 2(1-2\nu)$, i.e. $1-\nu = 1-2\nu$, i.e. $\nu = 0$ ✓. So the minimum of
$\sqrt2$ occurs at $\nu = 0$, where $\lambda = 0$ — the material has no volumetric
stiffness beyond what the shear modulus provides, and the ratio reaches its
conditional floor.

---

## ★3 — $v_p > v_s$ always

**(a)** $v_p^2-v_s^2 = [(\lambda+2\mu)-\mu]/\rho = (\lambda+\mu)/\rho$.

**(b)** $\lambda+\mu = (K-\frac23\mu)+\mu = K+\frac13\mu > 0$ since $K>0$ and
$\mu>0$ ✓.

**(c)** The smallest ratio is $\sqrt{(\lambda+2\mu)/\mu}$, which is minimised by
making $\lambda$ as negative as stability allows: $\lambda > -\frac23\mu$, giving
$(\lambda+2\mu)/\mu > \frac43$, so $v_p/v_s > 2/\sqrt3 = 1.154701$ ✓.

**(d)** With $\lambda\ge0$, $\lambda+2\mu\ge2\mu$ so $v_p/v_s\ge\sqrt2$. The
difference is that the first bound holds for auxetic materials ($\nu<0$) and the
second does not; the *existence* of a positive lower bound in both cases is what
makes $v_p > v_s$ unconditional.

---

## ★4 — A saturated sandstone

**(a)** $M = \rho v_p^2 = 2250\times3300^2 = 2.45025\times10^{10}$ Pa = 24.503 GPa;
$\mu = \rho v_s^2 = 2250\times1900^2 = 8.1225\times10^9$ Pa = 8.123 GPa;
$\lambda = M-2\mu = 24.503-16.245 = 8.258$ GPa;
$K = \lambda+2\mu/3 = 8.258+5.415 = 13.673$ GPa;
$\nu = (M-2\mu)/(2(M-\mu)) = 8.258/(2\times16.380) = 0.252$. (Equivalently
$\nu = \frac12(M-2\mu)/(M-\mu)$.)

**(b)** $E = \mu(3\lambda+2\mu)/(\lambda+\mu) = 8.123(24.774+16.245)/24.380 =
8.123\times41.019/24.380 = 13.666$ GPa.

**(c)** The measurement determines $M$ and $\mu$ directly (two equations, two
unknowns); $\lambda$, $K$, $E$ and $\nu$ are all derived from those two — and none
of them is independently measured by a P- and S-velocity determination.

**(d)** With $\mu$ unchanged at 8.123 GPa and $\rho = 2100+0.2\times1000 = 2300$
kg m⁻³... careful: the problem gives a dry density of 2100 and a fluid density of
1000; if the porosity is 0.2, the saturated density is
$2100+0.2\times1000 = 2300$ kg m⁻³, giving
$v_s = \sqrt{8.123\times10^9/2300} = 1879.5$ m s⁻¹. That is 1.1 per cent below
the observed 1900 m s⁻¹, and the discrepancy is a reminder that the *stated* dry
density and porosity must be mutually consistent with the mineral density
($\rho_{\text{dry}} = (1-\phi)\rho_{\min}$ gives $\rho_{\min} = 2625$
kg m⁻³ here, which is consistent to a few per cent).

---

## ★5 — Reading the demo

**(a)** $E = 73.636364$ GPa, $\nu = 0.227272727$, $K = 45.000000$ GPa,
$M = 85.000000$ GPa, $\lambda = 25.000000$ GPa, $\mu = 30.000000$ GPa;
$v_p = 5610.836077$ m s⁻¹, $v_s = 3333.333333$ m s⁻¹.

**(b)** The uniaxial test gives $\varepsilon_{11} = 1.358024691\times10^{-4}$
against $\sigma_{11}/E = 1.358024691\times10^{-4}$, and
$\varepsilon_{22} = -3.086419753\times10^{-5}$ against $-\nu\sigma_{11}/E$, and the
implied ratio $-\varepsilon_{22}/\varepsilon_{11} = 0.227272727$ recovered as
$\nu$. These test the definitions of $E$ and $\nu$ (equation (3)) via the
compliance.

**(c)** $\nu = -0.9$: 1.164965 (above $2/\sqrt3 = 1.154701$ ✓, below $\sqrt2$ as
expected since $\lambda<0$); $\nu = 0$: 1.414214 (exactly $\sqrt2$);
$\nu = 0.25$: 1.732051 ($\sqrt3$); $\nu = 0.49$: 7.141428.

**(d)** $\sqrt{M/K} = \sqrt{85/45} = \sqrt{1.888889} = 1.374369$; using $K$
instead of $M$ underestimates $v_p$ by 27.2 per cent.

---

## ★6 — Gas versus water in a clean sand

**(a)** For gas: $K_f = 0.02$ GPa,
$\phi/K_f = 0.25/0.02 = 12.5$;
$(1-\phi)/K_{\min} = 0.75/36 = 0.020833$;
$K_{\text{dry}}/K_{\min}^2 = 8/1296 = 0.006173$;
denominator $= 12.51466$; numerator $= (1-8/36)^2 = 0.604938$;
$K_{\text{sat}} = 8+0.048342 = 8.048$ GPa. $\rho = 0.75\times2650+0.25\times100 =
2012.5$ kg m⁻³.
$v_p = \sqrt{(8.048+8)/2012.5\times10^9}$ with $4\mu/3 = 8$:
$\sqrt{16.048\times10^9/2012.5} = \sqrt{7.974\times10^6} = 2823.8$ m s⁻¹.
$v_s = \sqrt{6\times10^9/2012.5} = \sqrt{2.981\times10^6} = 1726.6$ m s⁻¹.

For water: $K_f = 2.2$ GPa, $\phi/K_f = 0.113636$; denominator
$= 0.113636+0.020833-0.006173 = 0.128296$;
$K_{\text{sat}} = 8+4.713 = 12.713$ GPa; $\rho = 0.75\times2650+0.25\times1000 =
2237.5$ kg m⁻³; $v_p = \sqrt{(12.713+8)\times10^9/2237.5} =
\sqrt{9.256\times10^6} = 3042.4$ m s⁻¹;
$v_s = \sqrt{6\times10^9/2237.5} = \sqrt{2.681\times10^6} = 1637.6$ m s⁻¹.

**(b)** $v_p$ rises by 7.7 per cent from gas to water; $v_s$ falls by 5.2 per
cent.

**(c)** $Z_{\text{gas}} = 2012.5\times2823.8 = 5.683$ MRayl;
$Z_{\text{water}} = 2237.5\times3042.4 = 6.808$ MRayl. Against a shale of
$Z_1 = 6.0$ MRayl: $R_{\text{gas}} = (5.683-6.0)/11.683 = -0.02714$;
$R_{\text{water}} = (6.808-6.0)/12.808 = +0.06308$. The *polarity reverses*: the
gas sand gives a negative (trough) response and the water sand a positive (peak)
one, exactly the bright-spot polarity discrimination of lesson 02-03-08.

**(d)** Under uniform saturation, the $v_s$ change is driven only by density and
is monotonic, so it is a reliable indicator of fluid substitution; the $v_p$ change
can be small or of either sign because of the Gassmann dip of §3.4 of the lesson.
Under patchy saturation the $v_p$ change is large and positive (the patchy
modulus exceeds Gassmann), while $v_s$ is the same as in the uniform case — so the
$v_p$ signal becomes the better discriminator. Which regime applies is a
measurement, not an assumption.

---

## ★7 — Reading the ratio table

**(a)** $\nu = -0.5$: 1.224745; $-0.2$: 1.309307; $0$: 1.414214; $0.2$: 1.632993;
$0.4$: 2.449490; $0.49$: 7.141428.

**(b)** Each satisfies $\sqrt{2(1-\nu)/(1-2\nu)}$ exactly as printed in the demo's
verification column.

**(c)** The smallest value in the tabulated range is 1.164965 at $\nu = -0.9$
(the table in the lesson extends further), which is above $2/\sqrt3 = 1.154701$ as
required by stability; a value below $2/\sqrt3$ would imply $K<0$.

**(d)** A negative Poisson's ratio means the material *expands* laterally when
stretched. This requires a microstructure with hinges, re-entrant corners or a
fibrillar network that unfolds — engineered foams and some auxetic crystals do it.
It is not observed in ordinary rocks, but it is not forbidden by the stability
conditions, which only require $\nu > -1$.

---

## ★8 — Uncertainty propagation

**(a)** $\delta v_p/v_p = \frac12\sqrt{(\delta M/M)^2+(\delta\rho/\rho)^2}$;
$\delta M = \frac12\sqrt{(3\%)^2}$... more carefully,
$\delta M/M = \sqrt{(\delta K/K)^2 + (\frac{4\mu}{3M})^2(\delta\mu/\mu)^2}$.
With $K = 40$, $\mu = 25$, $M = 73.33$: $4\mu/(3M) = 100/220 = 0.454545$;
$\delta M/M = \sqrt{0.03^2+(0.454545\times0.02)^2} = \sqrt{9\times10^{-4}+8.26
\times10^{-5}} = 0.03134$. Then
$\delta v_p/v_p = 0.5\sqrt{0.03134^2+0.01^2} = 0.01645$, i.e. 1.6 per cent.
For $v_s$: $\delta v_s/v_s = 0.5\sqrt{0.02^2+0.01^2} = 0.011180$, i.e. 1.1 per
cent.

**(b)** $v_p$ is dominated by $K$ (3 per cent versus 2 per cent on $\mu$, and
$K$ enters with a larger weight); $v_s$ is dominated by $\mu$ and by density about
equally.

**(c)** $\nu$ depends on $K/\mu$ with weight $\frac{4}{3}$ on the ratio; the
propagated uncertainty is of order 2–4 per cent in $\nu$, i.e. of order 0.008
absolute for $\nu \approx 0.25$ — and since $v_p/v_s$ changes by only about 0.01
per 0.01 change in $\nu$ near $\nu = 0.25$, the two lithologies differing by 0.05
in $v_p/v_s$ are separated by roughly a factor of five relative to the 1σ
uncertainty, i.e. detectable but requiring care with systematics.

**(d)** The practical statement: a 1σ uncertainty of about 0.01 in $v_p/v_s$ means a
0.05 difference is a 5σ separation in principle, but systematic errors (anisotropy,
shale content, pressure sensitivity) usually dominate, so lithology discrimination
should always be presented with a rock-physics template and an uncertainty
envelope rather than a single threshold.

---

## ★★★9 — Pressure sensitivity

**(a)** A suitable choice: $a = 0.25$ (a 25 per cent crack-induced softening at
zero pressure) and $P^* = 20$ MPa, which produces most of the closure in the first
few tens of MPa — the observed behaviour of cracked crystalline rock. State
clearly that these are model values chosen to reproduce the qualitative
observation, not fitted measurements.

**(b)** $\mu(5) = 30[1-0.25e^{-0.25}] = 30\times[1-0.25\times0.778801] =
30\times0.805300 = 24.159$ GPa;
$\mu(10) = 30[1-0.25\times0.606531] = 30\times0.848367 = 25.451$ GPa;
$\mu(20) = 30[1-0.25\times0.367879] = 30\times0.908030 = 27.241$ GPa;
$\mu(40) = 30[1-0.25\times0.135335] = 30\times0.966166 = 28.985$ GPa.
With $\rho = 2600$: $v_s = 3048.3$, 3128.0, 3236.6 and 3339.2 m s⁻¹ — a 9.5 per
cent rise from 5 to 40 MPa, matching the assumed observation.

**(c)** At a lithostatic gradient of 26.5 MPa km⁻¹, 5 MPa corresponds to about
0.19 km and 40 MPa to about 1.5 km, and the model predicts a $v_s$ increase of
about 10 per cent over that interval. Compare with your chosen published
log-velocity profile: shallow crustal logs commonly show a rapid velocity increase
over the first kilometre, so the sense and rough size are plausible — but the
magnitude depends on lithology, fracture density and pore pressure, and the model
must be calibrated. State your source.

**(d)** A laboratory measurement is made at whatever confining pressure the
apparatus supplies, on a sample whose crack population may already have been
altered by coring. A field velocity is measured at the in-situ effective stress,
on a rock volume that includes fractures at all scales. Reconciling them requires
either (i) measuring the pressure dependence in the laboratory and extrapolating to
the in-situ effective stress, or (ii) using cross-plots of velocity against
porosity and clay content calibrated across many samples.

---

## ★★★10 — Frequency dependence of the moduli

**(a)** Low frequency: the pore fluid has time to equilibrate its pressure within
each cycle, so the saturated rock responds with the Gassmann modulus, which is the
softest saturated response. High frequency: the fluid cannot move between pores,
so each pore responds with its fluid *incompressible* (undrained locally), giving a
stiffer response. The crossover is set by the diffusion length
$\ell = \sqrt{D/\omega}$ compared with the distance over which the pore pressure
must equilibrate — the patch or grain size.

**(b)** $D \approx kK_f/(\eta\phi) = 100\times10^{-15}\times2.2\times10^9/
(10^{-3}\times0.2) = 2.2\times10^{-4}/2\times10^{-4} = 1.1$ m² s⁻¹. Hmm — this is
too large; the correct poroelastic hydraulic diffusivity is
$D = kK_f/(\eta\phi)$ with $k$ in m²: $100$ mD $= 9.87\times10^{-14}$ m², giving
$D = 9.87\times10^{-14}\times2.2\times10^9/(10^{-3}\times0.2) =
2.17\times10^{-4}/2\times10^{-4} = 1.09$ m² s⁻¹. Setting $\ell = 1$ mm (a
grain-scale equilibration length) to $1$ cm (a patch scale) gives
$\omega = D/\ell^2$: for $\ell = 1$ mm, $\omega = 1.09\times10^6$ rad s⁻¹
($f \approx 1.7\times10^5$ Hz); for $\ell = 1$ cm, $f \approx 1.7\times10^3$ Hz.
So the crossover sits between the seismic band and the ultrasonic band for
grain-scale patches, moving into the sonic band for centimetre-scale patches.

**(c)** Seismic frequencies (1–100 Hz) sample the low-frequency (Gassmann) limit;
ultrasonic measurements (0.1–5 MHz) can be in the high-frequency limit depending
on the patch size. Sonic logs (10–20 kHz) sit in between, which is one reason
laboratory and log velocities frequently disagree by a few per cent.

**(d)** A laboratory $v_p$ cannot be compared with a field $v_p$ without stating
and correcting for the frequency regime. The measurements that resolve the
ambiguity are (i) a frequency-dispersive laboratory measurement (forced
oscillation or a range of ultrasonic frequencies), and (ii) an independent
measurement of the pore-fluid mobility or patch geometry. Without one of those,
the comparison carries a systematic uncertainty of the size of the dispersion
itself — commonly a few per cent, and larger in partially saturated rocks.
