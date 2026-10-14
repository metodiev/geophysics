# Solutions — 02-07-06 EM Fields in Conductors: Skin Depth and Diffusion

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Constants: $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A²,
$\varepsilon_0 = 8.854\,187\,812\,8\times10^{-12}$ F/m. The skin-depth constant
$\sqrt{\rho T/(\pi\mu_0)} = 503.2921$ m Ω$^{-1/2}$ s$^{-1/2}$.

---

## ★1 — Skin depths at 100 Ω·m

**(a)** $\delta = 503.292\sqrt{100/f} = 5032.92/\sqrt f$ m:
$f = 0.01$ Hz → 50 329 m; $f = 1$ Hz → 5032.9 m; $f = 100$ Hz → 503.29 m.

**(b)** $\delta\sqrt f = 5032.92$ m Hz$^{1/2}$ in every case. The demo prints
5032.921209 at seven frequencies spanning six decades, to seven figures — the
invariance is exact, not approximate.

**(c)** $\delta(f/100)/\delta(f) = 1/10$ for $f/100$; more generally
$\delta(f/100)/\delta(f) = 1/\sqrt{100} = 0.1$ when the frequency is *divided* by
100 (i.e. period multiplied by 100). The demo's rows show
$\delta(T = 1/10\ \mathrm s)/\delta(T = 1\ \mathrm s) = 0.316\,228$ (which is
$1/\sqrt{10}$) and $0.100\,000$ for a factor 100 — as expected.

**(d)** Because $\delta\propto f^{-1/2}$: a decade of frequency gives
$\sqrt{10} = 3.162$ of depth, not 10. To double the depth you must quadruple the
period; to gain two decades of depth (say 0.5 km to 50 km) you need four decades of
period. The practical response is *broadband* acquisition — that is, extending the
period range at both ends — rather than more power or more precision at a few
frequencies.

---

## ★2 — Deriving $\delta$

**(a)** With $\mathbf E\propto e^{i(\omega t-kz)}$, $\nabla^2\mathbf E = -k^2\mathbf E$
and the quasi-static Helmholtz equation gives $-k^2 = i\omega\mu\sigma$, so
$k^2 = -i\omega\mu\sigma$ and $k = \sqrt{\omega\mu\sigma}\sqrt{-i}$. Since
$-i = e^{-i\pi/2}$, $\sqrt{-i} = e^{-i\pi/4} = (1-i)/\sqrt2$.

**(b)** $k = \sqrt{\omega\mu\sigma/2}(1-i) = (1-i)/\delta$ with
$\delta = \sqrt{2/(\omega\mu\sigma)}$. Then

$$-ikz = -(1-i)z/\delta = -(z/\delta) - i(z/\delta) ,$$

so

$$\mathbf E(z,t) = \mathbf E_0\,e^{-z/\delta}\,\big[\cos(\omega t - z/\delta)
+ i\sin(\omega t - z/\delta)\big] ,$$

i.e. amplitude decay $e^{-z/\delta}$ and phase lag $z/\delta$.

**(c)** $[\mu\sigma\omega] = (\mathrm{H/m})(\mathrm{S/m})(\mathrm{s^{-1}}) =
(\Omega\,\mathrm s/\mathrm m)(\Omega^{-1}/\mathrm m)(\mathrm{s^{-1}})
= \mathrm{m^{-2}}$, because $\mathrm{H\,S} = (\Omega\,\mathrm s)(\Omega^{-1}) =
\mathrm s$ and $\mathrm{s\,s^{-1}} = 1$ ✓. Hence $\sqrt{2/(\mu\sigma\omega)}$ is in
metres.

**(d)** $\delta$ is the depth over which the amplitude falls by $e^{-1}$. The
nominal wavelength $2\pi\delta$ is the spatial period of the phase oscillation, but
over one such period the amplitude falls by $e^{-2\pi} = 1/535$: the field does not
complete anything resembling a cycle. Calling $2\pi\delta$ a wavelength invites the
mistake of treating the diffusive field as a propagating wave with that wavelength
and a phase velocity $\omega\delta$ — a quantity that depends on frequency and is
not a property of the medium.

---

## ★3 — The $\rho T$ form

**(a)** With $\omega = 2\pi/T$ and $\sigma = 1/\rho$:

$$\delta = \sqrt{\frac{2}{\mu_0(1/\rho)(2\pi/T)}} = \sqrt{\frac{2\rho T}{2\pi\mu_0}}
= \sqrt{\frac{\rho T}{\pi\mu_0}} ,$$

and $1/\sqrt{\pi\mu_0} = 1/\sqrt{\pi\times1.2566\times10^{-6}} = 503.2921$.

**(b)** $\delta = 503.2921\sqrt{\rho}$ at $T = 1$ s: 1591.5 m (10 Ω·m),
5032.9 m (100 Ω·m), 15 915.5 m (1000 Ω·m).

**(c)** $T = \pi\mu_0\delta^2/\rho$: for $\delta = 1$ km, $T = 0.0395$ s; for 10 km,
$T = 3.9478$ s; for 100 km, $T = 394.78$ s.

**(d)** $\rho$ in Ω·m and $T$ in **seconds**. If $T$ is given in milliseconds the
computed depth is too small by $\sqrt{1000} = 31.6$; if a frequency in Hz is
substituted for $1/T$, the answer is wrong by $\sqrt{2\pi}$ in the opposite
direction. The demo prints the unit-bearing constant (503.2921 m Ω$^{-1/2}$
s$^{-1/2}$) precisely so that this cannot be forgotten.

---

## ★4 — Phase

**(a)** From ★2(b), the argument is $\omega t - z/\delta$, so at depth $z$ the
phase lags the surface by $z/\delta$ radians — the same number as the natural
logarithm of the amplitude ratio.

**(b)** $\delta = \sqrt{100\times10/(\pi\mu_0)} = 503.2921\sqrt{1000} = 15\,915.5$ m.
A $180°$ lag is $\pi$ radians, so $z = \pi\delta = 50\,000.0$ m.

**(c)** $\pi$ skin depths — and at that depth the amplitude is $e^{-\pi} = 0.043$,
so the signal is 4.3 % of the surface value.

**(d)** A wave equation's solution has *independent* amplitude and phase structure:
the phase advance is $kz$ with $k$ real and the amplitude constant (or decaying for
an independent reason, e.g. attenuation with its own coefficient). A diffusion
equation ties them together because the single complex $k$ has equal real and
imaginary parts: $k = (1-i)/\delta$. Observing equal decay and lag is therefore
direct evidence that you are looking at a diffusion equation, and it is exactly why
the half-space MT impedance has equal real and imaginary parts (45° phase).

---

## ★5 — Sounding-depth conventions

**(a)** $T = \pi\mu_0\delta^2/\rho = \pi(1.2566\times10^{-6})(10^4)^2/100
= 3.9478$ s.

**(b)** $\delta$ is the amplitude-$1/e$ depth. If the *nominal* depth of 10 km is
defined as $\delta$ itself, $T = 3.9478$ s (as in (a)). If it is defined as
$\delta/\sqrt2$, then $\delta = \sqrt2\times10\,000 = 14\,142$ m and, because
$T\propto\delta^2$,

$$T = \frac{\pi\mu_0\delta^2}{\rho} = 2\times3.9478 = 7.8957\ \mathrm s .$$

If it is defined as $0.5\delta$, then $\delta = 20\,000$ m and
$T = 4\times3.9478 = 15.7914$ s. These are exactly the three numbers the demo
prints.

**(c)** A nominal 10 km depth therefore corresponds to a period anywhere between
3.95 s and 15.8 s depending on the convention — a factor of four, which for a field
programme is a factor of four in recording time or in the number of sites that can
be occupied. The convention must be fixed *before* the survey, not reconciled
afterwards.

**(d)** Because the mapping from period to depth is $\delta\propto\sqrt{\rho T}$
and every published "depth" is some multiple of $\delta$ that varies between
authors. Without the convention, two papers using the same physics appear to
disagree by a factor of 2–4 in period, which in practice is a factor of 2–4 in the
cost of the survey.

---

## ★6 — Attenuation in the lossy-dielectric regime

**(a)** $f_c = \sigma/(2\pi\varepsilon) = 0.01/(2\pi\times20\times8.8542\times10^{-12})
= 8.9876\times10^{6}$ Hz $\approx9.0$ MHz.

**(b)**

| $f$ (Hz) | $\sigma/(\omega\varepsilon)$ | $\alpha$ exact (Np/m) | $\alpha_{\text{LL}}$ (Np/m) | $1/\delta$ (Np/m) |
|---|---|---|---|---|
| $10^{6}$ | 8.99 | $1.8796\times10^{-1}$ | $4.2120\times10^{-1}$ | $1.9869\times10^{-1}$ |
| $10^{7}$ | 0.899 | $3.8902\times10^{-1}$ | $4.2120\times10^{-1}$ | $6.2832\times10^{-1}$ |
| $10^{8}$ | 0.0899 | $4.2077\times10^{-1}$ | $4.2120\times10^{-1}$ | $1.9869\times10^{0}$ |

**(c)** At $10^{8}$ Hz, $\alpha = 0.420\,77$ Np/m. Using
$1\ \mathrm{Np} = 8.685\,89$ dB, this is **3.655 dB/m one-way**, so a two-way path
to 5 m loses $2\times5\times3.655 = 36.5$ dB — the demo's number. (For comparison,
a typical GPR system's usable dynamic range is of order 100 dB, giving a few metres
of penetration in this material.)

**(d)** The strong-conductor (skin-depth) result is correct for
$\sigma/(\omega\varepsilon)\gtrsim100$ — the MT band; the low-loss result is correct
for $\sigma/(\omega\varepsilon)\lesssim0.01$ — resistive rock at high frequency; and
between them, only the exact form is safe. At 100 MHz in wet soil
($x = 0.09$) $1/\delta$ is **4.7 times too large** and the low-loss formula is
0.1 % too small, so the low-loss form is usable there — but at 10 MHz
($x = 0.9$) the low-loss form is 8 % too large and $1/\delta$ 62 % too large, and
neither should be trusted. The rule of thumb: compute $x$ first, always.

---

## ★7 — Depth windows

**(a)** $\rho = 0.25$ Ω·m, $T = 1$ s: $\delta = 503.2921\sqrt{0.25} = 251.6$ m.
Sea water is penetrated hundreds of metres at 1 Hz — enough for marine MT, not
enough for radio communication (which is why submarines use ELF or acoustics).

**(b)** $\rho = 1000$ Ω·m: $T = 1$ s → 15 915 m; $T = 1000$ s → 503 292 m
(503 km).

**(c)** $\rho = 10$ Ω·m at $T = 86\,400$ s:
$\delta = 503.2921\sqrt{10\times86\,400} = 467\,800$ m ≈ 468 km — the
asthenosphere. This is the depth window of geomagnetic depth sounding.

**(d)** $\rho = 100$ Ω·m at $T = 3.156\times10^{7}$ s:
$\delta = 503.2921\sqrt{100\times3.156\times10^{7}} = 2.827\times10^{7}$ m
= 28 270 km — larger than the Earth's radius. The answer is not physically
sensible, and the reason is that the half-space model has failed: the conductivity
is not uniform to 28 000 km, and once $\delta$ exceeds the thickness of the
conducting region the *layer thickness* controls the response (see ★10). The
half-space formula is then an upper bound on the depth of sensitivity, not a
prediction of it.

---

## ★8 — Time-domain versus frequency-domain

**(a)** $\tau = \mu_0\sigma L^2 = (1.2566\times10^{-6})(0.01)(10^4)^2
= 1.2566$ s.

**(b)** $T = \pi\mu_0\delta^2/\rho = 3.9478$ s.

**(c)** They share the same ingredients ($\mu_0$, $\sigma$, $L^2$) and differ by
the factor $\pi$ (from $\omega = 2\pi/T$ versus the $\sqrt{t}$ similarity scaling
constant). The equality of the two scales is not a coincidence: both express
"how long diffusion takes to cover a distance $L$", and the numerical coefficient
depends on the definition (a $1/e$ decay, a half-amplitude, a fundamental mode, a
$\sqrt{Dt}$ reach).

**(d)** (i) The relaxation of a crustal field perturbation: use $\tau\sim\mu_0\sigma L^2$
(1.3 s for 10 km). (ii) The period an MT sounding needs to sense 10 km: use
$T = \pi\mu_0\delta^2/\rho$ (3.9 s). Quoting the wrong one is a factor-of-3 error in
bandwidth planning — not fatal, but avoidable.

---

## ★9 — Exact propagation

**(a)** With $k^2 = \omega^2\mu\varepsilon - i\omega\mu\sigma
= \omega^2\mu\varepsilon(1-ix)$, $x = \sigma/\omega\varepsilon$, writing
$k = \beta - i\alpha$ and matching $\beta^2-\alpha^2 = \omega^2\mu\varepsilon$ and
$2\alpha\beta = \omega\mu\sigma$ gives, after algebra,

$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1+x^2}-1\right]^{1/2},
\qquad
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1+x^2}+1\right]^{1/2} .$$

**(b)**

$$\frac{\alpha}{\beta} =
\sqrt{\frac{\sqrt{1+x^2}-1}{\sqrt{1+x^2}+1}} .$$

At $x\to0$: $\alpha/\beta\to0$ (a wave). At $x = 1$:
$\sqrt{(\sqrt2-1)/(\sqrt2+1)} = 0.414\,214$. At $x\to\infty$:
$\alpha/\beta\to1$ (a diffusive field with equal decay and lag).

**(c)** $v = \omega/\beta$:

$$\frac{v}{c/\sqrt{\varepsilon_r}} = \frac{\omega/\beta}{\omega\sqrt{\mu\varepsilon}}
= \sqrt{\frac{2}{\sqrt{1+x^2}+1}} ,$$

which equals 1 at $x = 0$, **0.9102** at $x = 1$ (the demo's value) and tends to
$\sqrt{2}/(1+x^2)^{1/4}\to0$ as $x\to\infty$: monotonically decreasing.

**(d)** For $x\gg1$: $\sqrt{1+x^2}\pm1\to x$, so
$\alpha\to\omega\sqrt{\mu\varepsilon x/2} = \sqrt{\omega\mu\sigma/2} = 1/\delta$
and $\beta\to1/\delta$ likewise. For $x\ll1$: $\sqrt{1+x^2}-1\to x^2/2$, so
$\alpha\to\omega\sqrt{\mu\varepsilon/2}\cdot x/\sqrt2 =
(\sigma/2)\sqrt{\mu/\varepsilon}$, the low-loss value, while $\beta\to\omega\sqrt{\mu\varepsilon}$.
Hence the amplitude *crosses over* only when $x\sim1$, but the phase velocity
departs from the lossless value as soon as $x$ is appreciable: at $x = 1$ it is
already 9 % low, even though $\alpha$ (the amplitude behaviour) is a genuine hybrid
there. That asymmetry — phase sensitive to a smaller loss than amplitude — is
well known in seismology as well (velocity dispersion versus attenuation) and is a
direct consequence of causality.

---

## ★10 — The conductance effect

**(a)** $S = h/\rho = 100/10 = 10$ S. Skin depth in the sheet:
$\delta = 503.2921\sqrt{10T}$: 1591.5 m at $T = 1$ s; 15 915 m at $T = 100$ s;
159 155 m at $T = 10^{4}$ s.

**(b)** The half-space formula gives 50 329 m at $T = 1000$ s and 159 155 m at
$T = 10^{4}$ s — hundreds to thousands of times the 100 m layer thickness. A
formula that predicts penetration to 159 km through a 100 m layer is not an
estimate; it is a category error. The layer, not $\delta$, must control the
response.

**(c)** Using the two-layer recursion with $\tanh(\gamma h)\approx\gamma h$ (valid
since $h\ll\delta$) and $Z_2 = \eta_2\to\infty$ for an insulator:
$Z = \eta_1/(\gamma_1h)$; and since $\eta_1 = i\omega\mu_0/\gamma_1$, this is
$Z = i\omega\mu_0/(\gamma_1^2h) = i\omega\mu_0/(i\omega\mu_0\sigma h) = 1/(\sigma h)
= 1/S$ ✓ real. Hence $\rho_a = |Z|^2/(\omega\mu_0) = 1/(\omega\mu_0S^2)$, which
grows linearly with $T$ and has **zero phase**.

**(d)** The demo's impedance recursion gives:

| $T$ (s) | $\rho_a$ (Ω·m) | phase (°) | $1/(\omega\mu_0S^2)$ (Ω·m) | $\rho_a$ / asymptote |
|---|---|---|---|---|
| 1 | $1.260\times10^{3}$ | 0.295 | $1.267\times10^{3}$ | 0.994 |
| 100 | $1.204\times10^{5}$ | 1.408 | $1.267\times10^{5}$ | 0.950 |
| $10^{4}$ | $7.770\times10^{6}$ | 11.368 | $1.267\times10^{7}$ | 0.613 |

The agreement with $1/(\omega\mu_0S^2)$ is excellent at short periods and degrades
at long periods as the basement begins to be felt. The sheet controls the response
when $\omega\mu_0S^2\rho_b\gg1$, i.e. when
$\rho_b \gg 1/(\omega\mu_0S^2)$ — for $T = 1000$ s that threshold is
$1.27\times10^{6}$ Ω·m, which is why the chosen $10^{8}$ Ω·m basement is well into
the sheet-controlled regime at short period and only marginally so at $10^{4}$ s.

**Consequence for interpretation.** Over a sedimentary basin, long-period data do
not measure a "depth" at all: they measure the *conductance* $S$ of the basin, and
$\rho_a$ rises with period rather than saturating. Inverting such data for a
resistivity–depth pair is non-unique in exactly the way that interpreting a
half-space skin depth would hide. This is the most common practical failure of the
half-space picture in real MT work, and it is why the correct first question about
any sounding is not "how deep is $\delta$?" but "is the responding structure
thicker or thinner than $\delta$?"
