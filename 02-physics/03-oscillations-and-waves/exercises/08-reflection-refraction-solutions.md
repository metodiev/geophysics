# Solutions — 02-03-08 Reflection, Refraction and Snell's Law for Waves

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Snell's law

**(a)** $\sin\theta_2 = (c_2/c_1)\sin20^\circ = 2\times0.342020 = 0.684040$, so
$\theta_2 = 43.1616^\circ$.

**(b)** $\sin\theta_c = c_1/c_2 = 0.5$, so $\theta_c = 30.0000^\circ$.

**(c)** $p = \sin20^\circ/1500 = 2.28013\times10^{-4}$ s m⁻¹; on the other side
$\sin\theta_2/3000 = 0.684040/3000 = 2.28013\times10^{-4}$ s m⁻¹ ✓.

**(d)** 45° exceeds the critical angle, so there is no propagating transmitted
wave: the field in the lower medium is evanescent, all energy is reflected, and
the reflected wave carries an angle-dependent phase shift.

---

## ★2 — Coefficients

**(a)** $R_v = (Z_1-Z_2)/(Z_1+Z_2) = -3.5/11.5 = -0.304348$;
$R_p = +0.304348$.

**(b)** $T_v = 2Z_1/(Z_1+Z_2) = 8/11.5 = 0.695652$;
$T_p = 2Z_2/(Z_1+Z_2) = 15/11.5 = 1.304348 = 1 + R_p$ ✓.

**(c)** $\mathcal{R} = R^2 = 0.092628$ (9.2628 %);
$\mathcal{T} = (Z_2/Z_1)T_v^2 = 1.875\times0.483932 = 0.907372$ (90.7372 %);
sum $= 1.000000$ ✓ (and the demo prints 1.000000000000).

**(d)** A velocity geophone (or a displacement seismogram) shows a *negative*
(trough-first) reflection, because $R_v < 0$: the reflected particle motion is
opposite to the incident. A hydrophone measures pressure and shows a
*positive* (peak-first) reflection, $R_p = +0.304348$. They are the same physical
event; the sign difference is a convention about what is being measured.

---

## ★3 — The law of reflection

**(a)** Incident: $e^{i(kx\sin\theta_1 + kz\cos\theta_1 - \omega t)}$; reflected:
$e^{i(kx\sin\theta_r - kz\cos\theta_r - \omega t)}$ (the $z$-component of the
wavevector reverses).

**(b)** Both fields exist in the same medium, so both have the same $k$ and
$\omega$. Along $z=0$ the total field must be continuous, which requires the
$x$-dependences to be identical for all $x$: $k\sin\theta_1 = k\sin\theta_r$, so
$\theta_r = \theta_1$ (taking the acute solution).

**(c)** Because the argument uses only the *phases*; the amplitudes enter the
boundary conditions separately, and the law of reflection is independent of them.

---

## ★4 — A layered velocity sequence

**(a)** Interfaces: 1500/2000 → $\theta_c = \sin^{-1}(0.75) = 48.5904^\circ$;
2000/2500 → $\sin^{-1}(0.80) = 53.1301^\circ$; 2500/3000 →
$\sin^{-1}(0.8333) = 56.4427^\circ$.

**(b)** The deepest critically refracted ray corresponds to the largest ray
parameter that is still critically refracted somewhere: $p = 1/3000 =
3.33333\times10^{-4}$ s m⁻¹, i.e. grazing incidence in the top layer
($\theta_1 = 90^\circ$).

**(c)** Yes: with $\theta_1 = 48.5904^\circ$ the ray is critically refracted at the
first interface and travels along it at 2000 m s⁻¹. Note that this is *not*
enough to refract it into the third layer.

**(d)** $p = 1/2000 = 5\times10^{-4}$ s m⁻¹ gives
$\sin\theta_4 = 3000\times5\times10^{-4} = 1.5 > 1$: no propagating ray reaches
the deepest layer at that ray parameter. This is the geometric statement behind
the hidden-layer problem: rays with a given $p$ may be trapped above a
low-velocity zone.

---

## ★5 — Reading the normal-incidence measurement

**(a)** Measured $R_v = -0.302777$ against $-0.304348$ (difference
$1.57\times10^{-3}$); measured $T_v = 0.694611$ against $0.695652$ (difference
$1.04\times10^{-3}$).

**(b)** Measured arrivals at 0.0248, 0.0746 and 0.0666 s against predictions
0.0250, 0.0750 and 0.0667 s.

**(c)** The initial condition is a Gaussian *displacement* with zero velocity,
which splits into two pulses of half the amplitude travelling in opposite
directions (lesson 02-03-05, §3.6). Since $R$ and $T$ are ratios of the reflected
and transmitted amplitudes to the incident amplitude measured in the same record,
the factor of one half cancels exactly.

**(d)** The peak-picking resolution, limited by the pulse width (8 m spatial
sigma) and the grid dispersion of the scheme. Reducing $\Delta x$, using a
higher-order stencil, or measuring the amplitude by a least-squares fit of the
known pulse shape rather than by taking the maximum would each improve it.

---

## ★6 — Shale over sand

**(a)** $Z_1 = 2400\times2500 = 6.00$ MRayl;
$Z_2 = 2300\times2800 = 6.44$ MRayl; $R_p = (6.44-6.00)/12.44 = +0.035369$.

**(b)** $Z_2 = 2000\times2200 = 4.40$ MRayl;
$R_p = (4.40-6.00)/10.40 = -0.153846$.

**(c)** Reflections: brine-sand case $\mathcal{R} = 0.1251$ %; gas-sand case
$\mathcal{R} = 2.3669$ %. The gas sand is the bright spot: about nineteen times
more reflected energy, in this synthetic model.

**(d)** The amplitude depends on the absolute impedances and on the source,
spreading, transmission losses and recording gain — all of which are usually
unknown to better than tens of per cent. The polarity depends only on whether the
impedance *decreases* or *increases* across the interface, which is a robust
qualitative signature that survives all those amplitude uncertainties. In
practice, both are used, with polarity as the discriminator and amplitude as the
quantitative measure (AVO analysis).

---

## ★7 — Refraction survey

**(a)** $\theta_c = \sin^{-1}(1500/3000) = 30.0000^\circ$.

**(b)** The crossover distance is where the direct arrival's travel time
$x/v_1$ equals the head wave's travel time
$2h\sqrt{v_2^2-v_1^2}/(v_1v_2) + x/v_2$. Equating and solving gives
$x_c = 2h\sqrt{(v_2+v_1)/(v_2-v_1)}$. With $x_c = 60$ m,
$\sqrt{(3000+1500)/(3000-1500)} = \sqrt3 = 1.732051$, so
$h = 60/(2\times1.732051) = 17.320$ m.

**(c)** The intercept time is
$t_i = 2h\sqrt{v_2^2-v_1^2}/(v_1v_2) = 2\times17.320\times2598.076/
(1500\times3000) = 0.020000$ s. It constrains $h$ through the same product, so
it is an independent (but correlated) measurement; using both $x_c$ and $t_i$ and
checking consistency is the standard quality control.

**(d)** $h \propto 1/\sqrt{(v_2+v_1)/(v_2-v_1)}$; differentiating with respect to
$v_1$ at the given values, a 5 per cent overestimate of $v_1$ changes $h$ by
about $-3$ per cent — but the dominant error in field practice is usually the
assumption of a horizontal, sharp interface, not the velocity.

---

## ★8 — The oblique check

**(a)** Residuals: $1.059\times10^{-16}$ at 0°, $0.000$ at 30°,
$4.162\times10^{-17}$ near the critical angle.

**(b)** They prove that the algebraic three-wave solution satisfies the pressure
and normal-velocity boundary conditions to machine precision at those angles —
i.e. that the algebra (including the coefficient formula) is correct. They do not
prove that the *boundary conditions themselves* are the right ones for a real
interface, nor that a real medium is a fluid; those are physical assumptions to be
justified separately.

**(c)** $R_p = 0.304348$ at 0°, 0.325523 at 15°, 0.421121 at 30°, 0.998909 at
41.81°. It increases with angle here, because the transmitted angle grows rapidly
and the $Z_2\cos\theta_1$ term in the numerator dominates; this is the opposite of
the common case in which the impedance contrast decreases with angle. The
direction of the trend depends on the ratio $Z_2/Z_1$ and on the velocity ratio,
which is precisely why AVO interpretation requires the elastic formulation.

**(d)** At $\theta_1 \to 90°$, $\cos\theta_1 \to 0$ and
$\cos\theta_2 = \sqrt{1-(c_2/c_1)^2}$ (finite only if $c_2 < c_1$; otherwise
the wave is beyond critical and the transmitted field is evanescent). With both
cosines small, $R_p \to -1$ (or $|R| \to 1$ in the evanescent case): a wave
travelling parallel to the interface cannot cross it.

---

## ★★★9 — The elastic interface

**(a)** Reflected P (compressional, carries normal stress at the interface),
reflected S (shear, carries tangential motion), transmitted P and transmitted S.
Each has its own angle, all related to the incident angle by the *same* ray
parameter: $p = \sin\theta_i/v_{p1} = \sin\theta'_{p}/v_{p1} =
\sin\theta'_{s}/v_{s1} = \sin\theta_{p}/v_{p2} = \sin\theta_{s}/v_{s2}$.

**(b)** Continuity of the three traction components $(t_z, t_x, t_y)$ and of the
three displacement components would give six conditions, but a P wave polarised in
the $x$–$z$ plane generates only in-plane waves (P and SV), so the $y$-polarised
SH problem decouples: four conditions remain for four unknown amplitudes
(reflected P, reflected SV, transmitted P, transmitted SV).

**(c)** At normal incidence $\theta = 0$: the S waves would require tangential
motion, which a normally incident P does not excite, so their amplitudes vanish
and the normal-traction and normal-displacement conditions reduce to the same
two-equation problem as in the acoustic case, with $Z = \rho v_p$. Hence
$R = (Z_1^p - Z_2^p)/(Z_1^p + Z_2^p)$ in the velocity convention.

**(d)** For the ★★6 cases with $v_p$ = 2500, 2800 and 2200 m s⁻¹ one obtains
$R_v$ values identical to the acoustic ones computed there, because the acoustic
and elastic normal-incidence formulas are the same with $Z = \rho v_p$. The
difference between the two models appears only off normal incidence: the acoustic
model omits mode conversion and therefore mispredicts amplitudes beyond about
10–20° of incidence for realistic contrasts.

---

## ★★★10 — The composite reflection of a thin layer

**(a)** Summing the geometric series of internal reflections: an incident wave hits
the top interface (coefficient $r_{12}$) and, partly transmitted, rattles inside
the layer; each round trip contributes a factor $r_{21}r_{23}e^{-i2k_2h}$. With
$r_{21} = -r_{12}$ the series sums to
$R = (r_{12}+r_{23}e^{-i2k_2h})/(1+r_{12}r_{23}e^{-i2k_2h})$ (sign conventions as
in the lesson's §3.2; write the derivation out with the signs you use).

**(b)** With $Z_1 = Z_3$ we have $r_{23} = -r_{12}$ and hence
$R = r_{12}(1-e^{-i2k_2h})/(1-r_{12}^2e^{-i2k_2h})$, whose magnitude oscillates
with $h$ with period $\lambda_2/2$ because the oscillating factor is
$e^{-i4\pi h/\lambda_2}$.

**(c)** The maximum of $|1-e^{-i2k_2h}|$ occurs at $2k_2h = \pi$, i.e.
$h = \lambda_2/4$ (the quarter-wave or tuning thickness), where
$|R| = 2|r_{12}|/(1+r_{12}^2)$. For $Z_1 = Z_3 = 6$, $Z_2 = 3$ MRayl:
$r_{12} = (6-3)/9 = 1/3$, so $|R_{\max}| = (2/3)/(1+1/9) = 0.6$.

**(d)** A program computing $|R(h)|$ should find the first maximum at
$h = \lambda_2/4$ to within the $h$-sampling; report your measured position and
the agreement. Note that the composite coefficient is *larger* than the
single-interface reflection coefficient $1/3$: a thin layer can reflect more than
a thick one because of constructive interference within it, which is exactly the
effect exploited by quarter-wave anti-reflection coatings (and, in reverse, by
tuning-thickness amplitude analysis in seismic interpretation).
