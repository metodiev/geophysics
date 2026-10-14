# Solutions — 05-08-02 Natural Gamma and Spectral Gamma Logging

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Concentrations are labelled SYNTHETIC.

---

## ★1 — What the tool measures

It measures a **count rate of gamma photons** emitted by the natural decay of
$^{40}$K, the $^{238}$U series and the $^{232}$Th series and their daughters. It
does not measure clay content, shale volume, lithology, porosity, permeability,
density or heat production — each of those is an inference through a stated model.

---

## ★2 — Volume of investigation

$\lambda = 8$ cm:

$$d_{50} = -\lambda\ln 0.5 = 0.693(8) = 5.54\ \mathrm{cm}, \qquad
d_{90} = -\lambda\ln 0.1 = 2.303(8) = 18.4\ \mathrm{cm}.$$

---

## ★3 — Indices and shale volume

$I_{\mathrm{GR}} = (74-25)/(130-25) = 0.467$.

(a) Linear: $V_{\mathrm{sh}} = 0.467$.

(b) Non-linear: $V_{\mathrm{sh}} = 0.33(2^{0.933}-1) = 0.33(1.9097-1) = 0.300$.

The two differ by 56 per cent relative. **The relation is a model choice and must
be stated**, because the same reading gives two substantially different shale
volumes.

---

## ★4 — Heat-production coefficients

**(a)** Derived: $c_K = 3.61$, $c_U = 10.23$, $c_{\mathrm{Th}} = 2.77$. Conventional:
$3.48$, $9.52$, $2.56$. Differences $+3.7$, $+7.4$, $+8.2$ per cent.

**(b)** From

$$A\ [\mu\mathrm{W\,m^{-3}}] = 10^{-5}\rho
\left(c_K \mathrm{K} + c_U \mathrm{U} + c_{\mathrm{Th}}\mathrm{Th}\right),$$

derived: $A = 10^{-5}(2650)(3.61\times3.0 + 10.23\times2.0 + 2.77\times8.0)
= 10^{-5}(2650)(10.83 + 20.46 + 22.16) = 10^{-5}(2650)(53.45) = 1.416$ µW m⁻³.
Conventional: $10^{-5}(2650)(3.48\times3.0 + 9.52\times2.0 + 2.56\times8.0)
= 10^{-5}(2650)(51.36) = 1.361$ µW m⁻³.

**(c)** The conventional set is more defensible for reporting, because it is the one
in the literature and therefore comparable with other studies; the derivation
verifies that you have understood and can reproduce it. Quote one set, name it, and
state the 4 per cent difference from the other.

---

## ★5 — A thin-bed shale volume

**(a)** The demonstration measures $-53.5$ per cent attenuation for a 0.50 m bed and
$-27.5$ per cent for 1.00 m, so a 0.60 m bed interpolates to about $-47$ per cent:
a logged peak of roughly $0.53\times140 = 74$ API above the background, i.e. about
$25 + 0.53(140-25) = 86$ API.

**(b)** Using ★3's baselines, the true $I_{\mathrm{GR}}$ is $(140-25)/105 = 1.095$
(clipped to 1, $V_{\mathrm{sh,true}} = 0.99$) against the logged
$I_{\mathrm{GR}} = (86-25)/105 = 0.581$ and $V_{\mathrm{sh,logged}} = 0.33(2^{1.162}-1)
= 0.33(1.238) = 0.409$. The error is **0.58 in shale volume** — from amplitude loss
alone, before any question of mineralogy arises.

**(c)** The bias is towards **under-calling shale**, always, because a thin bed is
always attenuated and never amplified.

---

## ★6 — Why the uranium window is slower

Two reasons, both from the physics. First, the $^{214}$Bi gamma at 1.76 MeV sits
between the K (1.46 MeV) and Th (2.62 MeV) peaks, so the window must be narrow and
well-separated, discarding counts. Second, uranium concentrations are typically
lower than potassium concentrations by an order of magnitude in common rocks, so
the count rate in its window is lower and the relative statistical precision poorer
for the same counting time. The precision improves only as $\sqrt{t}$, so matching
the potassium window's precision in the uranium window costs tens of times the
counting time — which is why spectral gamma logs are run slowly or stacked.

---

## ★7 — Disequilibrium

Model: radon (half-life 3.82 days) is produced in the rock and partially expelled.

1. The count rate in the uranium window comes from $^{214}$Bi, which sits below
   $^{222}$Rn in the chain. If a fraction $f$ of the radon escapes, the Bi activity
   is reduced by approximately $f$ (in the steady state of a closed box with
   leakage).
2. The reported "uranium" is therefore low by a factor $(1-f)$ relative to the true
   uranium content, and the deficit can be tens of per cent in a fractured,
   gas-prone or highly permeable organic mudstone.
3. **Detection:** compare the uranium-window reading with the Ra-226 activity from a
   laboratory gamma spectrometry measurement on core or cuttings from the same
   interval; disequilibrium shows as a mismatch between the two, and the ratio
   quantifies $f$.
4. **Reporting:** state the uranium reading as an *equivalent* uranium from the
   $^{214}$Bi window, and state that equilibrium was not verified unless it was
   measured.

---

## ★8 — Integrating a crustal column

Method: define a layered column (say 0–2 km shale, 2–10 km mixed, 10–30 km
granulite), assign each layer a **stated synthetic** K, U and Th content and a
density, compute $A(z)$ with the derived coefficients, and integrate

$$q_{\text{radiogenic}} = \int_0^{30\,\mathrm{km}} A(z)\,\mathrm{d}z .$$

Worked estimate for a simple three-layer case with $A = 2.18$, 1.50 and
0.40 µW m⁻³ over 0–2, 2–10 and 10–30 km gives
$2.18(2000) + 1.50(8000) + 0.40(20000) = 4360 + 12000 + 8000 = 24360$
mW m⁻²… which is $24.4$ mW m⁻² after dividing by 1000 µm→mm... the arithmetic must
be done in consistent units: $A$ in µW m⁻³ times thickness in m gives
$\mu$W m⁻², so divide by 1000 for mW m⁻²: $(4360+12000+8000)/1000 = 24.4$ mW m⁻².

Comparing with a typical continental measured heat flow of 65 mW m⁻² leaves
about 40 mW m⁻² to come from the mantle and the deeper crust — the same partition
computed in [12-03-01](../../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md).
**Largest assumption:** the deep-crustal concentration, which is not measured by any
well and is uncertain by a factor of two; it alone moves the result by several
mW m⁻². This is why crustal heat-production budgets are quoted as ranges.
