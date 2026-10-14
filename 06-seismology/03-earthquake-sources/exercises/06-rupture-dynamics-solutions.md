# Solutions — 06-03-06 Rupture Dynamics, Fracture Energy and Scaling Laws

> **Read after attempting the exercises.** All values are SYNTHETIC. Arithmetic is
> shown; where a hand value is compared with a demo measurement, the reason for
> any difference is given.

Lesson: [06 Rupture Dynamics, Fracture Energy and Scaling Laws](../06-rupture-dynamics.md).

Constants: $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $k = 0.37$,
$k\beta = 1295\ \mathrm{m\,s^{-1}}$, $W_{\max} = 15\ \mathrm{km}$.

---

## ★1 — Circular rupture at $a = 100\ \mathrm{m}$

$$M_0 = \tfrac{16}{7}\Delta\sigma a^{3}
= 2.28571\times3.0\times10^{6}\times(100)^{3}
= 2.28571\times3.0\times10^{6}\times10^{6} = 6.8571\times10^{12}\ \mathrm{N\,m}.$$

$$f_c = \frac{k\beta}{a} = \frac{1295}{100} = 12.95\ \mathrm{Hz}.$$

$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a
= 0.727575\times\frac{3.0\times10^{6}}{3.0\times10^{10}}\times100
= 0.727575\times10^{-4}\times100 = 7.2758\times10^{-3}\ \mathrm{m}.$$

**Units:** $M_0$ in $\mathrm{N\,m}$; $f_c$ in Hz $= \mathrm{s^{-1}}$; $\bar D$ in m.
Check: $\mathrm{Pa\,m^{3}} = \mathrm{N\,m}$; a radius times a strain is a length. ✔

---

## ★2 — Saturation corner frequency

$$f_{c,\text{sat}} = \frac{2k\beta}{W_{\max}}
= \frac{2\times0.37\times3500}{15\,000} = \frac{2590}{15\,000}
= 0.17267\ \mathrm{Hz}.$$

**Which length sets it:** the **seismogenic (brittle) thickness** $W_{\max}$. Once
the rupture spans the brittle layer it cannot grow deeper, so the smallest
dimension — the width — stops growing and the corner frequency stops falling.
(The factor $2$ comes from $a = W_{\max}/2$, i.e. the half-width as the
small-dimension radiation length scale.)

---

## ★3 — Fracture energy

$$G_c = \tfrac12(\tau_p-\tau_r)D_c = \tfrac12(80-40)\times10^{6}\times2.0
= \tfrac12\times40\times10^{6}\times2.0 = 4.0\times10^{7}\ \mathrm{J\,m^{-2}}.$$

**Unit** $\mathrm{J\,m^{-2}}$ (energy per unit fault area). **Geometrically** it is
the **area under the strength-versus-slip curve** above the residual level
$\tau_r$: the triangle with base $D_c$ and height $(\tau_p-\tau_r)$.

---

## ★4 — A saturated rupture

$$a = \frac{\min(L,W_{\max})}{2} = \frac{15\,000}{2} = 7500\ \mathrm{m},$$
$$f_c = \frac{k\beta}{a} = \frac{1295}{7500} = 0.17267\ \mathrm{Hz}
= f_{c,\text{sat}},$$
$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a
= 0.727575\times10^{-4}\times7500 = 0.54567\ \mathrm{m},$$
$$\text{area} = L\,W = 100\,000\times15\,000 = 1.5\times10^{9}\ \mathrm{m^{2}},$$
$$M_0 = \mu\,\bar D\times\text{area}
= 3.0\times10^{10}\times0.54567\times1.5\times10^{9} = 2.4555\times10^{19}\ \mathrm{N\,m}.$$

**Branch:** saturated. $L = 100\ \mathrm{km} > W_{\max} = 15\ \mathrm{km}$, so
$a$ is pinned at half the seismogenic thickness and $f_c$ sits exactly at
$f_{c,\text{sat}}$. Note that the direct $M_0 = (16/7)\Delta\sigma a^{3}$ formula
does **not** apply here: it describes a **circular** crack, whereas this rupture
is a rectangle of area $L\,W$ much larger than $\pi a^{2}$. Using it would give
$(16/7)\times3.0\times10^{6}\times7.5^{3}\times10^{9} = 2.89\times10^{18}\ \mathrm{N\,m}$,
nearly an order of magnitude too small — a good illustration of why the area used
for $M_0$ must match the rupture geometry.

---

## ★5 — Radiation efficiency

$$\eta_R = \frac{E_R}{E_R+G_c}.$$

**(a)** $\eta_R = \dfrac{4.1674\times10^{9}}{4.1674\times10^{9}+1.75\times10^{7}}
= \dfrac{4.1674}{4.1849} = 0.9958.$

**(b)** $\eta_R = \dfrac{1.6673\times10^{9}}{1.6673\times10^{9}+5.00\times10^{8}}
= \dfrac{1.6673}{2.1673} = 0.7693.$

**Which is more efficient and why:** case (a). Its fracture energy is only
$0.42\%$ of the radiated energy, whereas in (b) the fracture term is $30\%$ of the
total budget, so a much larger share of the available energy went into creating
the new surface rather than radiating waves. Physically, case (b) is a
larger-$D_c$ event: the same strength drop spread over a longer weakening
distance.

Both values match the demo's $\eta_R$ column ($0.9958$ and $0.7693$).

---

## ★6 — The integration window

$$\eta = \frac{\mu}{2\beta} = \frac{3.0\times10^{10}}{2\times3500}
= 4.2857\times10^{6}\ \mathrm{Pa\,s\,m^{-1}},$$
$$\tau_{\text{relax}} = \frac{\eta}{\kappa} = \frac{4.2857\times10^{6}}{6.0\times10^{5}}
= 7.1429\ \mathrm{s}.$$

The window is $2\times10^{6}$ steps $\times\,10^{-5}\ \mathrm{s} = 20\ \mathrm{s}$,
i.e. $20/7.1429 = 2.80$ relaxation times. The slip approaches its arrest value
exponentially, so the fractional shortfall is

$$e^{-2.80} = 0.0608 \approx 6.1\%.$$

The demo's measured shortfall, $D_f/D_{\text{arrest}} = 0.9364$–$0.9383$, is
$6.2$–$6.4\%$ — the same number, the extra $0.1$–$0.3\%$ being the time spent in
the weakening phase before the exponential approach begins. **The shortfall is
the window, not the physics.**

---

## ★7 — Apparent stress

With $E_R^{\text{total}} = E_R\cdot A$ (per-unit-area energy times fault area) and
$M_0 = \mu A\bar D$,

$$\tau_a = \frac{\mu E_R^{\text{total}}}{M_0}
= \frac{\mu E_R A}{\mu A\bar D} = \frac{E_R}{\bar D}. ☑$$

For the demo's $\tau_r = 10\ \mathrm{MPa}$ row:

$$\tau_a = \frac{4.1674\times10^{9}}{111.0353} = 3.7532\times10^{7}\ \mathrm{Pa}
= 37.53\ \mathrm{MPa}.$$

**Note the slip used.** If the arrest slip $118.33\ \mathrm{m}$ is used instead,
$\tau_a = 4.1674\times10^{9}/118.33 = 3.5217\times10^{7} = 35.22\ \mathrm{MPa}$ —
a $6\%$ difference, entirely from the same truncated window as in ★6. Because
$\tau_a$ is a ratio of two quantities affected identically by the window's
truncation *only if both are taken to the same slip*, the honest practice is to
use the slip that actually corresponds to the accumulated $E_R$.

A second caveat: definitions of apparent stress differ by a factor of 2 between
authors (some write $\tau_a = \mu E_R/(2M_0)$ and others
$\tau_a = \mu E_R/M_0$). The convention must be stated, exactly as with $k$ in
lesson [05](../05-source-spectra.md).

---

## ★8 — Detecting the saturated branch (specification)

**Observable.** For each event, $M_0$ (from the low-frequency plateau) and $f_c$
(from the spectrum), analysed identically, with uncertainties. Plot
$\log_{10}M_0$ against $\log_{10}f_c$.

**Predicted kink.** A line of slope $-3$ at small moments (self-similar) meeting a
vertical branch at $f_{c,\text{sat}} = 2k\beta/W_{\max}$. In a real catalogue the
vertical branch is not literally vertical because $f_c$ estimates scatter; the
signature is a **flattening of the trend** above a moment where
$f_c$ stops falling, with the flattening moment increasing with $W_{\max}$ (and
hence with tectonic setting).

**Population needed.** The kink is only visible where the population actually
crosses it, so the sample must span at least two decades of moment *straddling*
$f_{c,\text{sat}}$ — several hundred events if $f_c$ scatter is $\sim0.15$ in
$\log_{10}$ (a typical figure), because the scatter must be averaged down by
$\sqrt{N}$ to reveal a break of order a factor of $2$ in $f_c$.

**Two model assumptions that must hold.**

1. $\Delta\sigma$ is not itself a function of event size. If large events
   systematically have smaller stress drop, the "kink" may be a $\Delta\sigma$
   trend, not a width saturation.
2. $k$ and the spectral model are the same for all events. A change in the
   slip-pulse shape with size would move $f_c$ with no change in geometry.

If either fails, the kink is uninterpretable as a seismogenic-width effect.

---

## ★9 — Inferring $D_c$ and its trade-off (specification)

**Inversion.** Use a slip-weakening forward model of the same form as the demo,
with radiation damping, and fit it to observables that depend on both the slip
history and the energy partition: the radiated-energy estimate $E_R$ (from
spectral integration), the final slip $\bar D$ (from geodesy or a finite-fault
inversion), and the duration of $\dot M(t)$ (which constrains $\kappa$ and
$\eta$). Parameters: $\{D_c, \tau_p-\tau_r, \tau_0, \kappa\}$ with $\eta$ fixed by
$\mu/(2\beta)$.

**The trade-off.** Substitute the friction law into the energy balance at fixed
final slip $D_f$ and fixed $E_R$. The radiated energy per unit area is

$$E_R = \int \left(\tau_e-\tau_s\right)\mathrm{d}D,$$

so it depends on the strength *difference*, while the fracture energy
$G_c = \tfrac12(\tau_p-\tau_r)D_c$ depends on the *product* of the strength drop
and the weakening distance. Enlarging $D_c$ and reducing $(\tau_p-\tau_r)$
proportionally leaves $G_c$ (and thus, at fixed total work, $E_R$) nearly
unchanged. The two cannot be separated from the energy partition alone; the slip
*history* — the rise time and the shape of $\dot M(t)$ — is what breaks the
degeneracy, and it requires a broadband, well-deconvolved spectrum.

**Why relative is better.** At fixed $\mu$ and $\beta$, the shape of $\dot M(t)$
for a family of events differs mainly through the ratio $D_c/D_f$. If $D_c$ is
unknown but the *same* for the family, then a monotone relation between the
observed duration and $\bar D/D_c$ is preserved, and comparisons of the trend are
robust even though the absolute $D_c$ is not.

---

## ★10 — Why the printed $D_f$ cannot support the claim

The claim requires $D_f \approx (\tau_0-\tau_r)/\kappa$. The printed values are
$111.0353$, $79.7383$, $48.4457$, $17.1664\ \mathrm{m}$ against arrest values
$118.33$, $85.00$, $51.67$, $18.33\ \mathrm{m}$ — shortfalls of $6.2$, $6.2$,
$6.3$ and $6.4\%$. Two facts rule out a physical explanation:

1. The ratios $D_f/D_{\text{arrest}} = 0.9383, 0.9381, 0.9377, 0.9364$ are
   **the same to three parts in a thousand** across rows whose physics differs
   (different residual stress $\tau_r$, different stress drop, different slip).
2. That common constant equals $e^{-t_{\text{window}}/\tau_{\text{relax}}}$ for
   the demo's window ($20\ \mathrm{s}$) and relaxation time
   ($\eta/\kappa = 7.14\ \mathrm{s}$): $e^{-2.80} = 0.061$, i.e. a ratio of
   $0.939$.

So the shortfall is the **finite integration window** stopping the approach to
arrest, not a physical arrest before $(\tau_0-\tau_r)/\kappa$.

**The single diagnostic:** form the ratio of the measured quantity to its
closed-form prediction **for every row** and check whether the ratio is constant.
A constant fractional offset across a physically varied population points at the
computation (window, tolerance, time step), not at the model. The second demo loop
confirms it: doubling the number of steps to $4\times10^{6}$ ($40\ \mathrm{s}$)
brings the final slips to within $0.4$–$0.9\%$ of $85.00\ \mathrm{m}$ with the
same physics untouched.
