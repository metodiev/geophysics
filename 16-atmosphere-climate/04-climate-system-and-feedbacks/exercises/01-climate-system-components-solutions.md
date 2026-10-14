# Solutions — 16-04-01 Components of the Climate System and Their Timescales

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [01 Components of the Climate System and Their Timescales](../01-climate-system-components.md).

---

## ★1 — A 300 m ocean layer

$$C = \rho_wc_{p,w}h = 1025\times3985\times300 = 1.2254\times10^9\
\mathrm{J\,m^{-2}K^{-1}},$$

$$\lambda_0 = 4\sigma T^3 = 4(5.670374419\times10^{-8})(288)^3
= 5.418\ \mathrm{W\,m^{-2}K^{-1}},$$

$$\tau = \frac{C}{\lambda_0} = \frac{1.2254\times10^9}{5.418}
= 2.2616\times10^8\ \mathrm{s} = 7.17\ \mathrm{yr}.$$

Multiple of the atmospheric column:

$$\frac{C}{C_\text{atm}} = \frac{1.2254\times10^9}{1.0368\times10^7}
= 118.2 .$$

**Sanity check.** The lesson's 100 m layer gave 39.40× and the 200 m layer
78.80×; these scale linearly in $h$, and $118.2 = 1.5\times78.80$. ✔

---

## ★2 — Energy and time for a 0.6 K mixed-layer anomaly

$$Q = C_{50}\Delta T = (2.0423\times10^8)(0.6) = 1.2254\times10^8\
\mathrm{J\,m^{-2}}.$$

The instantaneous Planck flux at that anomaly is

$$F = \lambda_0\Delta T = 5.418\times0.6 = 3.251\ \mathrm{W\,m^{-2}},$$

and because the flux falls as the anomaly falls, the decay is exponential with

$$\tau = \frac{C_{50}}{\lambda_0} = \frac{2.0423\times10^8}{5.418}
= 3.769\times10^7\ \mathrm{s} = 1.20\ \mathrm{yr}.$$

So the anomaly is *not* removed in $Q/F = 1.2254\times10^8/3.251 = 3.77\times10^7$
s = 1.20 yr *of constant flux* — that coincidence holds because both are
$\Delta T$ times the same ratio: the linear-response time is the same for any
amplitude.

---

## ★3 — The Planck parameter at two temperatures

$$\lambda_0(273) = 4(5.670374419\times10^{-8})(273)^3
= 4.6149\ \mathrm{W\,m^{-2}K^{-1}},$$

$$\lambda_0(300) = 4(5.670374419\times10^{-8})(300)^3
= 6.1240\ \mathrm{W\,m^{-2}K^{-1}}.$$

Since $\tau = C/\lambda_0$, the **lower** temperature gives the longer
relaxation time: for a 50 m layer, 1.403 yr at 273 K against 1.057 yr at 300 K.
This is the blackbody part of the reason polar regions and high-altitude
surfaces respond more slowly, and it is a purely radiative effect that operates
before any feedback is considered.

---

## ★4 — The fast fraction

Hold the deep ocean fixed ($T_d = \text{constant}$, and take it as zero for a
perturbation problem). Then the mixed-layer budget has no storage term left
because we are asking for the quasi-steady state:

$$0 = F - \lambda T_m - \gamma T_m
\;\Longrightarrow\;
T_m = \frac{F}{\lambda+\gamma},
\qquad
\frac{T_m}{T_\text{eq}} = \frac{F/(\lambda+\gamma)}{F/\lambda}
= \frac{\lambda}{\lambda+\gamma}.$$

- $\gamma = 1.0$: fraction $= 5.418/6.418 = 0.8442$; $T_m = 0.5765$ K.
- $\gamma = 0.4$: fraction $= 5.418/5.818 = 0.9312$; $T_m = 0.6359$ K.

The **smaller** $\gamma$ gives the larger transient warming, because less heat
is being buried in the deep ocean. The equilibrium is $F/\lambda = 0.6829$ K in
both cases: $\gamma$ redistributes warmth between reservoirs and between times,
but it cannot change the eventual temperature, because at equilibrium the
coupling term carries no net heat.

---

## ★5 — The equilibrium is $\gamma$-independent

Setting both derivatives to zero:

$$0 = F - \lambda T_m - \gamma(T_m - T_d),
\qquad
0 = +\gamma(T_m - T_d).$$

The second equation forces $T_m = T_d$ (for $\gamma>0$). Substituting into the
first removes the coupling term entirely and gives
$\lambda T_m = F$, so

$$T_m = T_d = \frac{F}{\lambda}
\quad\text{for every } \gamma>0 .$$

**Why the coupling must vanish there:** $\gamma(T_m-T_d)$ is a heat flux
proportional to a temperature *difference*. If a steady state has a nonzero
difference, the two reservoirs exchange energy at a constant rate and neither
temperature can be steady — so a steady state requires zero difference.

---

## ★6 — Ice-sheet timescales and melt

**(a)** Mass balance: $\tau_\text{mass} = H/\dot b = 2500/0.25
= 1.0\times10^4$ yr.

**(b)** Thermal: with $\kappa = 1.1424\times10^{-6}$ m² s⁻¹,

$$\tau_\text{therm} = \frac{H^2}{\kappa}
= \frac{(2500)^2}{1.1424\times10^{-6}}
= 5.471\times10^{12}\ \mathrm{s} = 1.735\times10^5\ \mathrm{yr}.$$

A factor of 17 longer than the mass-balance time: the ice sheet can change
shape long before its interior has finished adjusting its temperature.

**(c)** Melt heat:

$$L_f\rho_iH = (3.34\times10^5)(917)(2500) = 7.657\times10^{11}\
\mathrm{J\,m^{-2}},$$

which is

$$\frac{7.657\times10^{11}}{2.0423\times10^8} = 3749\ \mathrm{K}$$

worth of the 50 m mixed layer's heat capacity. Melting this ice by cooling the
mixed layer is therefore not merely slow — it is impossible by a factor of
thousands, which is the quantitative form of "melt is flux-limited, not
temperature-limited".

---

## ★7 — Testing the role of $\gamma$ (specification)

**Design.** Fix $F = 3.7$ W m⁻² and $\lambda = 5.418$ W m⁻² K⁻¹, so that the
equilibrium $F/\lambda$ is identical in every run. Vary
$\gamma \in \{0.2, 0.4, 0.8, 1.6\}$ W m⁻² K⁻¹ with $C_m = 2.0423\times10^8$ and
$C_d = 1.3683\times10^{10}$ J m⁻² K⁻¹, and solve each case with the exact matrix
exponential (or an implicit integrator — an explicit one cannot span the 660-fold
range of timescales).

**Diagnostic versus abscissa.** Plot $T_m(t)/T_\text{eq}$ against time on a
logarithmic abscissa, one curve per $\gamma$; overlay the horizontal line
$\lambda/(\lambda+\gamma)$. A second panel: the realised fraction at a fixed
time, say 50 yr, against $\gamma$.

**Expected result demonstrating the claim.** All curves converge to 1 (the same
equilibrium) but approach it differently: the 50-year fraction falls
monotonically with $\gamma$, and each curve's early plateau sits at
$\lambda/(\lambda+\gamma)$ — 0.965 at $\gamma = 0.2$ down to 0.772 at
$\gamma = 1.6$. If the transient were governed by $F$ rather than by $\gamma$,
the curves would be identical up to a common scaling and the plateau would not
move.

**What this design cannot test.** $\gamma$ here is a *prescribed constant*. The
experiment establishes only how the two-box solution depends on its parameters;
it says nothing about whether a real ocean's heat uptake is linear in the
temperature difference, which is the assumption embedded in the choice of a
constant $\gamma$. Testing that requires an ocean model, or observations of
ocean heat uptake and of the mixed-layer–deep-ocean temperature difference.
