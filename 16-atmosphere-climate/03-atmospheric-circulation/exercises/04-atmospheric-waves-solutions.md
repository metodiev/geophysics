# Solutions — 16-03-04 Atmospheric Waves: Rossby, Kelvin, Gravity Waves

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [04 Atmospheric Waves](../04-atmospheric-waves.md).

---

## ★1 — Rossby frequency at two latitudes

$$\beta = \frac{2\Omega\cos\phi}{a}.$$

- $30^\circ$: $\beta = 2(7.292115\times10^{-5})(0.866025)/6.371\times10^6
  = 1.98247\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$.
- $60^\circ$: $\beta = 2(7.292115\times10^{-5})(0.5)/6.371\times10^6
  = 1.14458\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$.

With $\lambda_x = 4000$ km, $k = 2\pi/4\times10^6 = 1.57080\times10^{-6}$
m⁻¹, and $\omega = -\beta/k$:

- $30^\circ$: $\omega = -1.98247\times10^{-11}/1.57080\times10^{-6}
  = -1.26208\times10^{-5}\ \mathrm{s^{-1}}$; period
  $2\pi/|\omega| = 4.978\times10^5$ s $= 5.76$ d; $c_x = \omega/k
  = -8.03\ \mathrm{m\,s^{-1}}$.
- $60^\circ$: $\omega = -7.28662\times10^{-6}\ \mathrm{s^{-1}}$; period
  $8.623\times10^5$ s $= 9.98$ d; $c_x = -4.64\ \mathrm{m\,s^{-1}}$.

**$30^\circ$ has the shorter period**, because $\beta$ is larger there and
$\omega\propto\beta$. The same wave is slower at high latitude — which is one
reason the midlatitude waveguide narrows poleward.

---

## ★2 — Kelvin wave on a 200 m equivalent depth

$$c = \sqrt{gH} = \sqrt{9.81\times200} = 44.29\ \mathrm{m\,s^{-1}},$$

$$\sqrt{\frac{c}{\beta}} = \sqrt{\frac{44.29}{2.2892\times10^{-11}}}
= \sqrt{1.9347\times10^{12}} = 1.391\times10^6\ \mathrm{m} = 1391\ \mathrm{km}.$$

Period at $k = 1/a = 1.5698\times10^{-7}$ m⁻¹:
$2\pi/(ck) = 2\pi/(44.29\times1.5698\times10^{-7}) = 9.037\times10^5$ s
$= 10.46$ d.

**Unit of the trapping scale:** $c/\beta$ is (m s⁻¹)/(m⁻¹ s⁻¹) = m², so its
square root is a **length**, and the exponent $-\beta y^2/(2c)$ is
dimensionless. ✔

---

## ★3 — A 45° gravity wave

$$\omega = N\cos45^\circ = 10^{-2}\times0.707107 = 7.07107\times10^{-3}\
\mathrm{s^{-1}},$$

period $= 2\pi/\omega = 888.6$ s $= 0.247$ h $= 14.8$ min.

**The mode exists**, because $\omega<N$; it would cease to exist (become
evanescent) only at $\theta = 0$, where $\omega = N$ exactly. Note that the
period has nothing to do with the wavelength: any wavenumber magnitude with this
direction has the same frequency.

---

## ★4 — The $n = 0$ equatorial roots

Substituting $\omega = -ck$ into
$\omega^3 - \omega(c^2k^2+\beta c) - \beta c^2k$:

$$-c^3k^3 + ck(c^2k^2+\beta c) - \beta c^2k
= -c^3k^3 + c^3k^3 + \beta c^2k - \beta c^2k = 0 . ✔$$

So $\omega = -ck$ is always a root. Dividing it out leaves

$$\omega^2 - ck\,\omega - \beta c = 0
\;\Longrightarrow\;
\omega = \frac{ck \pm \sqrt{c^2k^2 + 4\beta c}}{2}.$$

With $c = 62.64$ m s⁻¹, $\beta = 2.2892\times10^{-11}$,
$k = 1.5696\times10^{-7}$ m⁻¹:

$$ck = 9.8323\times10^{-6},\qquad
\sqrt{c^2k^2+4\beta c} = 7.6372\times10^{-5},$$

$$\omega = -9.8323\times10^{-6},\qquad
\omega = \frac{9.8323\times10^{-6}+7.6372\times10^{-5}}{2}
= +4.3102\times10^{-5},$$

$$\omega = \frac{9.8323\times10^{-6}-7.6372\times10^{-5}}{2}
= -3.3270\times10^{-5}.$$

These are the three roots the demonstration prints: the $-ck$ branch, the
eastward inertia-gravity mode and the westward mixed Rossby-gravity mode. The
mixed mode is the one drawn from the *minus* branch, and for large $k$ it
behaves as $-\beta/k$, i.e. like a Rossby mode — which is why it is called
mixed.

---

## ★5 — Group velocity perpendicular to the wavevector

$$\omega = N\frac{k}{\sqrt{k^2+m^2}}
\quad (k \equiv k_h, \text{ two dimensions}),$$

$$\frac{\partial\omega}{\partial k}
= N\frac{\sqrt{k^2+m^2} - k\cdot k/\sqrt{k^2+m^2}}{k^2+m^2}
= \frac{N m^2}{(k^2+m^2)^{3/2}},$$

$$\frac{\partial\omega}{\partial m}
= Nk\cdot\left(-\tfrac12\right)\frac{2m}{(k^2+m^2)^{3/2}}
= -\frac{N k m}{(k^2+m^2)^{3/2}} .$$

Then

$$\mathbf{c}_g\cdot\mathbf{k}
= \frac{N m^2}{(k^2+m^2)^{3/2}}\,k
- \frac{N k m}{(k^2+m^2)^{3/2}}\,m
= \frac{Nkm^2 - Nkm^2}{(k^2+m^2)^{3/2}} = 0 . ✔$$

Numerically, $\lambda_h = 200$ km $\Rightarrow k = 3.14159\times10^{-5}$ m⁻¹;
$\lambda_z = 800$ km $\Rightarrow m = 7.85398\times10^{-6}$ m⁻¹;
$\omega = 9.7014\times10^{-3}$ s⁻¹;
$\mathbf{c}_g = (18.17, -72.66)$ m s⁻¹. Then

$$\mathbf{c}_g\cdot\mathbf{k} = 18.17\times3.14159\times10^{-5}
- 72.66\times7.85398\times10^{-6}
= 5.708\times10^{-4} - 5.707\times10^{-4} \approx 2\times10^{-7},$$

zero to the precision of the inputs. The energy flux is along the phase fronts:
a gravity wave deposits momentum where its fronts are, not where it appears to
be going.

---

## ★6 — Convergence of the finite-difference scheme

**(a)** Ratios: $3.215\times10^{-3}/8.033\times10^{-4} = 4.00$;
$8.033\times10^{-4}/2.008\times10^{-4} = 4.00$. A factor of 4 per halving of
$\Delta x$ means the error scales as $\Delta x^2$, the signature of a
**second-order** scheme.

**(b)** Extrapolating: $2.008\times10^{-4}/4 = 5.02\times10^{-5}$.

**(c)** What it does **not** verify: that the barotropic vorticity equation, the
$\beta$-plane approximation or the uniform background wind describe the
atmosphere. A convergence test validates the code and the discretisation; it
cannot validate the model. Only a comparison with observed wave frequencies,
together with an error budget on the observations, can do that — and even then
it tests the model only for the regime those observations sample.

---

## ★7 — Separating numerical from physical decay (specification)

**Diagnostic versus abscissa.** Plot the decay rate of the wave amplitude,
$\gamma = -\mathrm{d}\ln(\text{amplitude})/\mathrm{d}t$, against (i) the grid
spacing $\Delta x$ at fixed domain, and (ii) the wave frequency $\omega$ at
fixed grid. Also plot the amplitude profile along $x$ at several times: a
numerical cause usually distorts the shape (dispersion, trailing oscillations,
boundary reflection) while a physical cause scales the whole profile.

**Outcome for a numerical cause.** $\gamma$ falls as $\Delta x$ falls (roughly as
$\Delta x^2$ for a second-order scheme) and continues to fall; it depends on
$\omega$ in the way the scheme's damping does (numerical diffusion acts
strongest at the highest resolved frequencies); and the profile shows
short-wavelength structure or a phase error. Convergence to zero as
$\Delta x\to0$ is the decisive evidence.

**Outcome for a physical cause.** $\gamma$ is independent of $\Delta x$ across
several refinements, and the profile stays a clean Gaussian of the same shape
with its amplitude falling. A physical damping has a mechanism to state (eddy
diffusion in the model, radiative relaxation, surface drag) and a rate that
depends on a physical parameter rather than on the grid.

**The boundary experiment.** Run with (1) a sponge layer of increasing width and
strength, (2) a rigid wall, and (3) a radiation (open) condition, and compare the
reflected energy in each. If the decay is caused by the outflow boundary, the
apparent decay rate will change with sponge width and strong reflections will
appear in case (2). Propagating the wave *without* reaching the boundary — for
example by stopping the run before the leading edge arrives, or by using a
domain long enough — isolates the interior scheme from the boundary and must be
part of the design.
