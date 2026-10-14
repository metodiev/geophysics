---
id: 02-07-06
title: "EM Fields in Conductors: Skin Depth and Diffusion"
level: graduate
prereqs: ["02-07-03", "02-07-04", "02-07-05"]
estimated_minutes: 90
tags: [skin-depth, diffusion, magnetotellurics, sounding-depth, attenuation]
---

# EM Fields in Conductors: Skin Depth and Diffusion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth $\delta = \sqrt{2/(\mu\sigma\omega)}$ from the
   frequency-domain Maxwell equations, showing every substitution.
2. **Interpret** $\delta$ physically: the amplitude decay length, the phase-lag
   length (both equal), and why the nominal wavelength $2\pi\delta$ describes
   decay rather than oscillation.
3. **Demonstrate** the $\delta\propto f^{-1/2}$ and $\delta\propto\sqrt\rho$
   scalings, and use them to explain why a decade of frequency buys only a factor
   3.16 in depth.
4. **Compute** the period required to sound to 10 km in a 100 Ω·m half-space and
   state how the answer depends on the definition of sounding depth.
5. **Verify** $\delta$ against a direct numerical solution of the governing
   differential equation, not just against itself.
6. **Evaluate** the exact attenuation constant of a lossy dielectric and identify
   where the low-loss and strong-conductor approximations are valid, with numbers.
7. **State** the regimes of validity of the whole skin-depth framework, including
   where the half-space model and the real-$\sigma$ assumption fail.

## Prerequisites

- [02-07-03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — the Helmholtz equation (8) and the ratio $\sigma/(\omega\varepsilon)$.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md)
  — eddy currents and the time-domain face of the same physics.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](./05-em-waves.md)
  — the impedance whose phase of 45° is a restatement of the result derived here.

## 1. The governing equation in a conductor

Start from the Helmholtz form of Maxwell's equations for a time dependence
$e^{i\omega t}$, in a uniform, isotropic, non-magnetic medium with conductivity
$\sigma$ and permittivity $\varepsilon$ (lesson
[02-07-03](./03-maxwell-equations.md), equation 8):

$$\nabla^2\mathbf E = \left(i\omega\mu_0\sigma - \omega^2\mu_0\varepsilon\right)\mathbf E
\equiv -k^2\mathbf E ,
\qquad
k^2 = \omega^2\mu_0\varepsilon - i\omega\mu_0\sigma . \tag{1}$$

For the geophysical diffusive regime, $\sigma/\omega\varepsilon \gg 1$, the first
term on the right of the definition of $k^2$ is negligible and

$$k^2 \simeq -i\omega\mu_0\sigma . \tag{2}$$

**A note on the two terms, because they are not of the same order and it matters.**
$\omega^2\mu_0\varepsilon$ is the displacement-current contribution and
$i\omega\mu_0\sigma$ the conduction-current contribution; their ratio is
$\sigma/(\omega\varepsilon)$, which lesson [02-07-03](./03-maxwell-equations.md)
tabulated as $9\times10^{9}$ for wet soil at 1 mHz and 0.09 at 100 MHz. The
approximation (2) is therefore excellent for magnetotellurics and wrong for GPR;
Section 6 handles the general case.

## 2. Deriving the skin depth

Take a plane wave propagating in the $+z$ direction, $\mathbf E = \mathbf E_0e^{-ikz}$
(the $e^{i\omega t}$ factor is suppressed). From (2),

$$k = \sqrt{-i\omega\mu_0\sigma} = \sqrt{\omega\mu_0\sigma}\,\sqrt{-i}
= \sqrt{\omega\mu_0\sigma}\;e^{-i\pi/4}
= \sqrt{\frac{\omega\mu_0\sigma}{2}}\,(1-i) . \tag{3}$$

Using $\sqrt{-i} = e^{-i\pi/4} = (1-i)/\sqrt2$, which is worth checking once by
hand. Therefore

$$-ikz = -\frac{(1-i)}{\delta}z = -\frac{z}{\delta} - i\frac{z}{\delta},
\qquad
\delta \equiv \sqrt{\frac{2}{\omega\mu_0\sigma}} , \tag{4}$$

and the field becomes

$$\boxed{\ \mathbf E(z,t) = \mathbf E_0\,e^{-z/\delta}\,e^{i(\omega t - z/\delta)}\ }
\qquad\text{with}\qquad
\boxed{\ \delta = \sqrt{\frac{2}{\mu_0\sigma\omega}} = \sqrt{\frac{2\rho}{\mu_0\omega}}
= \sqrt{\frac{\rho T}{\pi\mu_0}}\ } . \tag{5}$$

The two boxed results are the whole lesson. Read them line by line:

- The **amplitude** decays as $e^{-z/\delta}$. At $z = \delta$ it is $1/e = 0.368$
  of the surface value; at $z = 2\delta$, 0.135; at $5\delta$, 0.0067. Beyond about
  three skin depths, nothing useful survives.
- The **phase** lags by exactly $z/\delta$ radians — the *same* number as the
  logarithmic decay. Decay and lag are not merely both present; they are equal.
  This is the structural signature of a diffusion equation, and it is why the MT
  impedance is complex with equal real and imaginary parts (a 45° phase).
- The **magnetic field** is obtained from $\nabla\times\mathbf E = -i\omega\mu_0\mathbf H$:
  $|\mathbf H| = |\mathbf E|/\sqrt{\omega\mu_0\rho}$, so in a good conductor the
  magnetic field is much larger relative to $E$ than it would be in vacuum
  ($\sqrt{\omega\mu_0\rho}$ can be far below 377 Ω). The ratio is still an
  impedance, but a small one.

**The $\rho T$ form and the constant.** Writing $\omega = 2\pi/T$ and $\sigma = 1/\rho$,

$$\delta = \sqrt{\frac{2\rho T}{2\pi\mu_0}} = \sqrt{\frac{\rho T}{\pi\mu_0}}
= 503.2921\,\sqrt{\rho T}\ \ \mathrm{m}
\qquad (\rho\ \text{in}\ \Omega\,\mathrm m,\ T\ \text{in s}) . \tag{6}$$

The constant is $1/\sqrt{\pi\mu_0}$, and with the measured
$\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A² it is 503.2921 m Ω$^{-1/2}$ s$^{-1/2}$.
(The commonly quoted 503.3 comes from the pre-2019 exact $\mu_0 = 4\pi\times10^{-7}$;
the two agree to five significant figures, which is why the historical constant is
still safe to use — but the correct *reason* is that $\mu_0$ is now measured, not
defined.)

## 3. Physical interpretation: what $\delta$ is, and what it is not

| Quantity | Value | Meaning |
|---|---|---|
| $\delta$ | $\sqrt{2/(\mu\sigma\omega)}$ | depth at which the **amplitude** falls to $1/e = 0.368$ |
| $\delta/2$ | | depth at which the **power** falls to $1/e$ (power $\propto$ amplitude²) |
| $2\pi\delta$ | | the nominal wavelength, i.e. the spatial period of the phase oscillation |
| $\omega\delta$ | | a nominal phase velocity $\omega/\beta$ |
| $\pi\delta$ | | the depth at which the phase has lagged by 180° |
| $3\delta$–$5\delta$ | | the practical limit: amplitude $0.05$–$0.007$ of the surface value |

**The nominal wavelength is not a wavelength you should use for anything.** In a
good conductor the amplitude falls by $e^{-2\pi}$ — a factor 535 — over one
"wavelength". A field that decays by a factor 500 per cycle is not oscillating in
any useful sense; it is diffusing, and the phase structure is a by-product of the
diffusion, not evidence of propagation. Likewise $\omega\delta$ is not a
propagation speed: it is proportional to $\sqrt\omega$ and therefore not a
constant of the medium. Any report that quotes a "velocity" from a diffusive EM
delay is reporting an artefact of the frequency at which it was measured.

**Why $3\delta$–$5\delta$ is the practical range.** A surface EM system measures
a two-way effect: the field that migrates out to the target and comes back. The
amplitude of a round trip through depth $z$ is $e^{-2z/\delta}$, so a target at
depth $\delta$ returns $e^{-2} = 0.135$, one at $2\delta$ returns 0.018, and one at
$3\delta$ returns $2.5\times10^{-3}$. Instrumentation with 100 dB of usable
dynamic range therefore stops seeing a two-way signal somewhere between $2\delta$
and $4\delta$ — which is why the working rule of thumb is $3\delta$–$5\delta$, and
why it is a statement about instrumentation as much as about physics.

## 4. Scaling: the square root, and its consequences

The demo computes $\delta(f)\sqrt f$ = 5032.921209 m Hz$^{1/2}$ for
$\rho = 100$ Ω·m at every frequency from 1 mHz to 1 kHz — constant to seven
figures. The exact statements are

$$\delta \propto \frac{1}{\sqrt f}, \qquad \delta \propto \sqrt\rho,
\qquad \delta \propto \frac{1}{\sqrt\mu}, \qquad
\delta \propto \frac{1}{\sqrt\sigma} . \tag{7}$$

Each has a practical consequence:

- **$\delta \propto f^{-1/2}$.** A decade of frequency buys a factor 3.16 in
  depth, not 10. To double the depth you must quadruple the period. To sound from 1 km to
  100 km (two decades of depth) requires *four* decades of period — which is why
  broadband MT uses periods from $10^{-3}$ s to $10^{4}$ s and why it is a
  wide-bandwidth method.
- **$\delta \propto \sqrt\rho$.** To see deeper at the same period you need more
  resistive ground. This cuts both ways: a resistive basement is easy to see
  (its own skin depth is large), but a conductive layer *above* it screens it.
- **$\delta \propto 1/\sqrt\sigma$.** A tenfold increase in conductivity reduces
  the depth by 3.16. The enormous conductivity contrast between a massive sulphide
  body and its host is what makes EM the method of choice for sulphide
  exploration; and the equally enormous contrast between seawater and rock is what
  makes marine MT hard.
- **$\delta \propto 1/\sqrt\mu$.** Because rocks are weakly magnetic, $\mu_r\approx1$
  and this factor is almost always ignored. For magnetite-rich rock with
  $\mu_r = 1.1$, the skin depth is 4.7 % smaller — small, but systematic, and one
  of the reasons lesson [02-07-07](./07-magnetisation-materials.md) exists.

## 5. How deep can you sound? The required period

**The 10 km question.** To reach 10 km in a 100 Ω·m half-space, set
$\delta = 10\,000$ m in (6) and solve for the period:

$$T = \frac{\pi\mu_0\delta^2}{\rho}
= \frac{\pi(1.25663706212\times10^{-6})(10^4)^2}{100}
= 3.9478\ \mathrm s . \tag{8}$$

The demo verifies by back-substitution: $\delta(100\ \Omega\,\mathrm m,
3.9478\ \mathrm s) = 10\,000.000$ m. **A period of about 4 s reaches 10 km in
100 Ω·m rock.** For comparison, the same criterion gives 39.5 s at 10 Ω·m and
0.395 s at 1000 Ω·m. This is exactly the frequency band in which MT is most
productive, and it is why short-period MT (0.001–1 s) images the upper crust while
long-period MT (10–10⁴ s) images the lithosphere.

**The convention trap.** "Sounding depth" is defined differently in different
papers, and because $T\propto\delta_{\text{nominal}}^2$ the difference is squared
into the period:

| Convention for the nominal 10 km depth | $\delta$ needed | Period |
|---|---|---|
| depth $= \delta$ (amplitude $1/e$) | 10 000 m | **3.9478 s** |
| depth $= \delta/\sqrt2$ | 14 142 m | **7.8957 s** |
| depth $= 0.5\delta$ (power $1/e$ at $z=\delta/2$; also used as a crude resolution depth) | 20 000 m | **15.7914 s** |

A factor of four in required period, and hence in the required data bandwidth, is
hidden in a definition. Note also that the depth at which the *power* falls to
$1/e$ is $\delta/2$, not $\delta/\sqrt2$ — the two are different conventions and
both appear in the literature. Whenever you read or write a "sounding depth", state
the convention and the corresponding period.

## 6. Beyond the strong-conductor limit: attenuation in lossy dielectrics

When $\sigma/(\omega\varepsilon)$ is not large, equations (5) and (6) are wrong and
the general result (lesson [02-07-03](./03-maxwell-equations.md), equation 9)
applies. For $k = \beta - i\alpha$:

$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}
\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}-1\right]^{1/2},
\qquad
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}
\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}+1\right]^{1/2}. \tag{9}$$

The demo evaluates this for a wet-soil model ($\sigma = 0.01$ S/m,
$\varepsilon_r = 20$, so $f_c = \sigma/(2\pi\varepsilon) = 9.0$ MHz):

| $f$ (Hz) | $\sigma/(\omega\varepsilon)$ | $\alpha$ exact (Np/m) | $\alpha$ low-loss (Np/m) | $1/\delta$ (Np/m) | $v$ (m/s) |
|---|---|---|---|---|---|
| $10^{-3}$ (MT) | $9.0\times10^{9}$ | $6.28\times10^{-6}$ | $4.21\times10^{-1}$ | $6.28\times10^{-6}$ | (diffusive) |
| $10^{6}$ | 9.0 | $1.88\times10^{-1}$ | $4.21\times10^{-1}$ | $1.99\times10^{-1}$ | $2.99\times10^{7}$ |
| $10^{7}$ | 0.90 | $3.89\times10^{-1}$ | $4.21\times10^{-1}$ | $6.28\times10^{-1}$ | $6.19\times10^{7}$ |
| $10^{8}$ (GPR) | 0.090 | $4.21\times10^{-1}$ | $4.21\times10^{-1}$ | $1.99\times10^{0}$ | $6.70\times10^{7}$ |
| $10^{9}$ | 0.0090 | $4.21\times10^{-1}$ | $4.21\times10^{-1}$ | $6.28\times10^{0}$ | $6.70\times10^{7}$ |

Read the table across, not down:

- **Left column (MT).** $1/\delta$ agrees with the exact $\alpha$ to all printed
  digits, and the low-loss formula is 67 000 times too large. The strong-conductor
  limit is the right one.
- **Right columns (GPR).** The low-loss formula converges to the exact value
  (both $4.2119\times10^{-1}$ Np/m by $10^{9}$ Hz), while $1/\delta$ is 15 times
  too large at $10^{9}$ Hz and 4.7 times too large at $10^{8}$ Hz. The
  strong-conductor limit is now the *wrong* one, quantitatively and qualitatively:
  the field propagates, with $v = 6.70\times10^{7}$ m/s $\approx c/\sqrt{20}$ and
  $\lambda = 0.67$ m.
- **Middle.** At $\sigma/(\omega\varepsilon)\sim1$ both approximations fail, and
  neither is even qualitatively right. This is the regime of *lossy-dielectric*
  GPR and of cross-hole radar, and only (9) is safe.

At 100 MHz the exact attenuation is 0.4208 Np/m = **3.65 dB/m one-way**. A
two-way path to 5 m therefore loses about 36.5 dB, which is consistent with the
few-metre penetration of high-frequency GPR in wet soil and with the strong
improvement seen in drier, more resistive ground.

## 7. What period reaches what depth

The demo tabulates $\delta$ for nominal earth materials:

| Medium (nominal) | $T$ | $\delta$ |
|---|---|---|
| sea water, 0.25 Ω·m | 1 s | 0.25 km |
| wet soil, 100 Ω·m | 1 s | 5.0 km |
| crustal basement, 1000 Ω·m | 1 s | 15.9 km |
| crustal basement, 1000 Ω·m | 1000 s | 503 km |
| mantle, 10 Ω·m (0.1 S/m) | 1 day | 468 km |
| mantle, 100 Ω·m (0.01 S/m) | 1 yr | 28 300 km |

The last row gives a depth larger than the Earth's radius, which is the clearest
possible signal that the model has failed: with $\delta$ comparable to or larger
than the thickness of the conducting region, the half-space formula stops being an
estimate and becomes a nonsense. In that limit the *layer thickness* controls the
response, exactly as in the two-layer MT example of lesson
[02-07-05](./05-em-waves.md): the measured impedance saturates toward the
resistivity of the layer below, and no amount of extra period recovers the
deep structure.

The practical depth windows, stated as nominal rules of thumb:

- **Magnetotellurics, 10⁻³–10⁴ s:** tens of metres (in conductive ground) to
  hundreds of kilometres. The workhorse for crustal and mantle conductivity.
- **Geomagnetic depth sounding, 10²–10⁵ s:** the mantle, using only the magnetic
  field and its relation to a remote reference.
- **Controlled-source EM, 10⁻⁵–10³ s after switch-off:** metres to a few hundred
  metres, set by the transmitter moment as well as by $\delta$.
- **GPR, 10–1000 MHz:** centimetres to tens of metres, set by attenuation, with
  the skin depth a poor guide because the regime is propagation-dominated.

## 8. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| $\sigma/(\omega\varepsilon)\gg1$ | Equation (2) | The wave regime; use (9) |
| $\sigma$ real, frequency-independent | Ohm's law $\mathbf J = \sigma\mathbf E$ | Induced polarisation and dielectric relaxation make $\sigma$ complex; the phase of $\sigma$ carries information the real model cannot reproduce |
| Uniform half-space | Equations (5)–(6) | Layered ground: use the impedance recursion; the *local* skin depth is still a useful scale but is not the sounding depth |
| Plane wave, vertical incidence | Free-space propagation to the surface | Source effects; the plane-wave assumption fails near the auroral electrojet, near the coastline (the ocean–continent boundary), and for controlled sources closer than a few skin depths |
| Non-magnetic ground | $\mu = \mu_0$ | Magnetite-rich rock with appreciable $\mu_r$ |
| Homogeneous isotropy | Scalar $\sigma$ | Anisotropy: a tensor conductivity, and $\delta$ becomes direction-dependent |
| No self-induction of the source | The measured field is the Earth's response | A transmitter coil close to the ground loads the system; the primary field must be modelled or removed |
| The recorded fields are the Earth's response alone | Throughout | Anthropogenic noise (power lines, pipelines, railways), which is the dominant practical limitation of MT below 1 s in populated regions |

The most important entry is the third: **in real ground there is no single skin
depth.** The formula gives the decay length *at a locally uniform conductivity*;
in a layered or 3-D Earth the response is a superposition of diffusive modes and
the depth sensitivity is a broad, frequency-dependent kernel. The skin depth is
an order-of-magnitude aid, not an inversion.

## 9. Units and dimensional analysis

- $[\mu_0\sigma\omega] = (\mathrm{H/m})(\mathrm{S/m})(\mathrm{s^{-1}})$.
  Using $\mathrm{H\,S} = \mathrm{(\Omega\,s)(\Omega^{-1})} = \mathrm s$, this is
  $\mathrm{s/(m^2\,s)} = \mathrm{m^{-2}}$, so
  $\sqrt{2/(\mu_0\sigma\omega)}$ has units of metres ✓.
- $[\rho T/(\pi\mu_0)]$: $\Omega\,\mathrm{s\cdot m/(H)} = \Omega\,\mathrm{s\,m/(\Omega\,s)} = \mathrm{m^2}$ ✓,
  so its square root is metres, and the constant 503.2921 has units
  $\mathrm{m\,\Omega^{-1/2}\,s^{-1/2}}$ ✓ — which is why the formula must be used
  with $\rho$ in Ω·m and $T$ in seconds and no other units.
- $[1/\delta] = \mathrm{m^{-1}} = \mathrm{Np/m}$ ✓, the same units as $\alpha$:
  this is why comparing $1/\delta$ with $\alpha$ is a legitimate check, and Section
  6 shows it is a check that fails outside its regime.
- $[2\delta] = \mathrm m$, and the "dB" form of attenuation is
  $1\ \mathrm{Np} = 20\log_{10}e = 8.685\,889\,638$ dB, so
  $\alpha\ [\mathrm{dB/m}] = 8.685889638/\delta$ when $\alpha = 1/\delta$ ✓.

## 10. Python demonstration

[`code/em_in_conductors_demo.py`](./code/em_in_conductors_demo.py) verifies every
claim above. Observed output:

```text
rho = 100 ohm m, sigma = 0.0100 S/m
     T (s)        f (Hz)       delta (m)     delta sqrt(f)
 1000.0000    1.0000e-03     159154.9430       5032.921209
    1.0000    1.0000e+00       5032.9212       5032.921209
    0.0010    1.0000e+03        159.1549       5032.921209
  delta(T = 1/10 s)/delta(T = 1 s) = 0.316228   (1/sqrt(10) = 0.316228)
  delta(T = 1/100 s)/delta(T = 1 s) = 0.100000   (1/sqrt(100) = 0.100000)
  delta(T = 1/10000 s)/delta(T = 1 s) = 0.010000   (1/sqrt(10000) = 0.010000)
```

```text
     T (s)   delta formula (m)  delta measured (m)    rel. error
   1.0e-04           50.329212           50.329196     3.189e-07
   1.0e-02          503.292121          503.291960     3.189e-07
   1.0e+00         5032.921209         5032.919604     3.189e-07

     T (s)     |Z| numeric   sqrt(omega mu0 rho)   rho_a numeric   phase (deg)
   1.0e-04    2.809926e+00          2.809926e+00      100.000001       45.0002
   1.0e-02    2.809926e-01          2.809926e-01      100.000001       45.0002
   1.0e+00    2.809926e-02          2.809926e-02      100.000001       45.0002
```

```text
  Set delta = 10000 m: T = pi mu0 delta^2/rho = 3.947842 s (3947.8 ms)
  check: delta(100 ohm m, 3.9478 s) = 10000.000 m
  The convention matters: if a nominal depth of 10 km is defined as
    delta          : T = 3.9478 s
    delta/sqrt(2)  : delta = 14 142 m, T = 7.8957 s
    0.5 delta      : delta = 20 000 m, T = 15.7914 s
    rho =      10 ohm m: T =    39.4784 s
    rho =     100 ohm m: T =     3.9478 s
    rho =    1000 ohm m: T =     0.3948 s
```

```text
wet-soil model: sigma = 0.01 S/m, eps_r = 20, mu = mu0
crossover frequency f_c = sigma/(2 pi eps) = 8.9876e+06 Hz
    f (Hz) sigma/(omega eps)   alpha exact  alpha low-loss     1/delta       v (m/s)  lambda (m)
     0.001        8.9876e+09   6.28319e-06     4.21197e-01 6.28319e-06   1.00000e+03 1.00000e+06
     1e+06        8.9876e+00   1.87961e-01     4.21197e-01 1.98692e-01   2.99150e+07 2.99150e+01
     1e+07        8.9876e-01   3.89021e-01     4.21197e-01 6.28319e-01   6.19146e+07 6.19146e+00
     1e+08        8.9876e-02   4.20774e-01     4.21197e-01 1.98692e+00   6.69682e+07 6.69682e-01
     1e+09        8.9876e-03   4.21193e-01     4.21197e-01 6.28319e+00   6.70350e+07 6.70350e-02
  At f = 1e8 Hz the exact alpha is 4.207735e-01 Np/m = 3.6548 dB/m one-way.
  A two-way GPR path to 5 m loses 36.5 dB
```

### What to observe

| Observation | Consequence |
|---|---|
| $\delta\sqrt f = 5032.921209$ m Hz$^{1/2}$ at every frequency from 1 mHz to 1 kHz | Equation (7) holds to seven figures; the square-root law is exact, not approximate |
| The ratios 0.316228, 0.100000, 0.010000 equal $1/\sqrt{10}$, $1/\sqrt{100}$, $1/\sqrt{10^4}$ to six decimals | The scaling is *precisely* inverse-square-root in frequency, and the demo's arithmetic agrees with the analytic $1/\sqrt n$ |
| A direct complex tridiagonal solution of $E'' = i\omega\mu_0\sigma E$ — which assumes no exponential form — reproduces $\delta$ to $3.2\times10^{-7}$ relative at three frequencies | $\delta$ is verified against the differential equation itself, not against a second evaluation of its own formula |
| The same numerical solution gives $\rho_a = 100.000001$ Ω·m and a phase of 45.0002° | Two independent routes (decay length and surface impedance) recover the input resistivity |
| $T = 3.9478$ s for $\delta = 10$ km at 100 Ω·m, and the back-substitution returns exactly 10 000.000 m | Equation (8) is internally consistent; this is the period a crustal MT sounding needs |
| Under the $\delta/\sqrt2$ and $0.5\delta$ conventions the same nominal 10 km needs 7.8957 s and 15.7914 s | Since $T\propto\delta^2$, a factor of two in the depth convention is a factor of four in the required period — a bandwidth decision, not a detail |
| At 1 mHz the exact $\alpha$ equals $1/\delta$ to all printed digits, and the low-loss formula is 67 000 times too large | The strong-conductor limit is the correct one for MT, and the "low-loss" formula is catastrophically wrong there |
| At $10^{9}$ Hz the low-loss formula and the exact result agree to five figures, while $1/\delta$ is 15 times too large | The low-loss limit is the correct one for GPR in resistive ground, and it is the skin-depth formula that is wrong there |
| $v\to 6.70\times10^{7}$ m/s $= c/\sqrt{20.0}$ at high frequency | In the wave regime the velocity is set by permittivity, exactly as lesson 02-07-05 says |
| The 100 MHz attenuation, 3.65 dB/m one-way, gives 36.5 dB for a 5 m two-way path | GPR penetration in wet soil is a few metres, as observed — the regime table is not academic |

> **Breaking exercise.** Set $\varepsilon_r = 4$ (drier ground) with the same
> $\sigma = 0.01$ S/m and recompute $f_c$, $\alpha$ at 100 MHz, and the two-way
> loss to 5 m. Then set $\sigma = 10^{-4}$ S/m (very resistive granite) and repeat.
> Explain, with the ratio $\sigma/(\omega\varepsilon)$ in hand, why penetration in
> a dry granite environment can exceed that in wet soil by an order of magnitude.

## 11. Common mistakes

1. **Using $\delta = 503\sqrt{\rho T}$ with $\rho$ in Ω·m but $T$ in milliseconds
   or frequency in Hz.** The formula needs $T$ in seconds; a frequency in Hz gives
   an answer wrong by $\sqrt{2\pi}$ in one direction or $1/\sqrt{2\pi}$ in the
   other, depending on the mistake. Write the units down.
2. **Treating $\delta$ as the depth of investigation.** It is the depth of $1/e$
   amplitude decay in a *uniform half-space*. The depth of investigation of a real
   survey is a sensitivity kernel, and in resistive ground it exceeds $\delta$;
   in layered ground it can be much smaller.
3. **Quoting a "velocity" from a diffusive arrival.** There is none; the phase
   velocity $\omega\delta$ depends on frequency, and the penetration law is
   $z\sim\sqrt{Dt}$.
4. **Using the skin-depth formula for GPR.** Section 6's table shows it is a
   factor 4.7 wrong at 100 MHz in wet soil and gets worse at higher frequency.
5. **Forgetting that $\delta\propto1/\sqrt\sigma$ is what makes a conductor both a
   good target and a good screen.** The same property that gives a sulphide body
   its enormous EM response screens everything below it.
6. **Assuming a real, frequency-independent conductivity.** Induced polarisation
   is precisely the statement that it is not; the imaginary part of $\sigma$ is the
   measurable signal of the IP method.
7. **Neglecting the loading of the transmitter by a conductive ground.** A coil
   close to the ground has its effective impedance changed by the eddy currents;
   the source field is not the free-space field.
8. **Reporting $\rho_a$ as "the resistivity".** It is a model-dependent equivalent
   value that can lie outside the range spanned by the true layered model.

## 12. Real-world applications

- **Magnetotelluric depth soundings.** The 4 s period for 10 km in 100 Ω·m is the
  design criterion for a crustal MT survey; the bandwidth is chosen from equation
  (8), not from habit.
- **Geomagnetic depth sounding and long-period MT.** Periods of hours to a day
  reach the asthenosphere; the half-space formula is an upper bound there, and
  layer thicknesses control the response.
- **Induction logging.** The sonde's operating frequency is chosen so that the
  skin depth is comparable to the radius of investigation; too high a frequency
  and the tool sees only the mudcake.
- **Airborne EM systems.** The bird's geometry and frequency are chosen together,
  because the target depth, the system height and the conductivity set three
  different length scales that must be commensurate.
- **GPR penetration planning.** Section 6's exact attenuation, not the skin
  depth, sets the achievable depth; the 36.5 dB figure for 5 m in wet soil is the
  kind of number quoted in survey design.
- **Seawater, ice and permafrost.** Nominal conductivities differ by orders of
  magnitude across these media, and the corresponding skin depths explain why
  radar works in ice (very resistive, metres to tens of metres) and not in
  seawater (very conductive, millimetres at radar frequencies).
- **Anisotropy and fractured rock.** Where $\sigma$ is a tensor, $\delta$ is
  direction-dependent; the measured MT impedance tensor is how that anisotropy is
  mapped.

## 13. Further reading

- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** §5.18 and
  §7.7 give the skin-depth derivation and the exact lossy-dielectric relations
  used in Section 6. Level: graduate.
- **Ward, S. H., & Hohmann, G. W. "Electromagnetic theory for geophysical
  applications", in Nabighian, M. N. (ed.) *Electromagnetic Methods in Applied
  Geophysics*, Vol. 1 (SEG, 1988).** The standard geophysical statement of the
  skin depth, the quasi-static approximation and their domains. Level: advanced.
- **Simpson, F., & Bahr, K. *Practical Magnetotellurics* (Cambridge University
  Press, 2005).** Sounding depth, the $\delta$ versus $\delta/\sqrt2$ convention
  and the depth of investigation discussion. Level: advanced.
- **Chave, A. D., & Jones, A. G. (eds) *The Magnetotelluric Method: Theory and
  Practice* (Cambridge University Press, 2012).** Sensitivity kernels that
  replace the naive skin-depth depth of investigation. Level: graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics* (2nd
  ed., Cambridge University Press, 1990).** The EM chapter's tables of nominal
  conductivities and the field numbers that go with them. Level: intermediate.
- **Daniels, D. J. *Ground Penetrating Radar* (2nd ed., IET, 2004).** Attenuation
  and penetration windows in the lossy-dielectric regime. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — the derivation of the Helmholtz equation and the wave/diffusion dichotomy.
- [05 Electromagnetic Waves, Impedance and Polarisation](./05-em-waves.md) — the
  45° half-space phase derived from the impedance side, and the layered response.
- [04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) — the
  time-domain face: $\operatorname{erfc}$ and the absence of a wavefront.
- [02-07-07 Magnetisation, Susceptibility and Magnetic Materials](./07-magnetisation-materials.md)
  — when $\mu_r\neq1$ and the skin depth changes.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) — the
  survey practice that these formulas size.
- [10 GPR and Near-Surface](../../10-gpr-near-surface/README.md) — the other side
  of the dichotomy, where this lesson's approximation fails.

Exercises:
[`exercises/06-em-in-conductors-exercises.md`](./exercises/06-em-in-conductors-exercises.md)
and
[`exercises/06-em-in-conductors-solutions.md`](./exercises/06-em-in-conductors-solutions.md).

## Self-assessment checklist

Work through this without notes. Every item should be a clear "yes".

- [ ] I can derive $\delta$ from the Helmholtz equation, showing the evaluation of
      $\sqrt{-i}$. (Section 2)
- [ ] I can explain why decay and phase lag are the same number, and what that
      implies for the MT phase. (Section 2)
- [ ] I can state the five equivalent forms and the constant in the $\rho T$ form,
      with its units. (Section 2)
- [ ] I can say what $\delta$, $\delta/2$ and $2\pi\delta$ mean, and why the
      nominal wavelength should not be used as a wavelength. (Section 3)
- [ ] I can state the four square-root scalings and one practical consequence of
      each. (Section 4)
- [ ] I can compute the period needed for a stated sounding depth and state the
      convention. (Section 5)
- [ ] I can write the exact attenuation of a lossy dielectric and say which
      approximation is valid in which regime, with the ratio evaluated.
      (Section 6)
- [ ] I can explain why a half-space skin depth larger than the layer thickness
      signals model failure. (Section 7)
- [ ] I can list six assumptions of the skin-depth framework and name an
      observation that violates each. (Section 8)
- [ ] I can verify $\delta$ against a direct numerical solution and confirm the
      $\sqrt f$ scaling numerically. (Section 10)
