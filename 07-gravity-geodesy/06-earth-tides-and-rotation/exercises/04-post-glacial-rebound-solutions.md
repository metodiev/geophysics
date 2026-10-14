# Solutions — 07-06-04 Post-Glacial Rebound: Viscosity and Ice History Inference

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values or stated standard constants.

Lesson: [04 Post-Glacial Rebound](../04-post-glacial-rebound.md).

Constants: $R = 6371\ \mathrm{km}$, $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$,
$\rho_i = 917\ \mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$\tau_l = 2\eta k_l/(\rho_mg)$, $k_l = l/R$.

---

## ★1 — Two relaxation times

$$k_3 = \frac{3}{6.371\times10^{6}} = 4.7088\times10^{-7}\ \mathrm{m^{-1}},
\qquad
\tau_3 = \frac{2(5\times10^{21})(4.7088\times10^{-7})}{32373}
= 1.4546\times10^{11}\ \mathrm{s} = 4609.2\ \mathrm{yr}.$$

$$k_{30} = \frac{30}{6.371\times10^{6}} = 4.7088\times10^{-6}\ \mathrm{m^{-1}},
\qquad
\tau_{30} = 10\,\tau_3 = 46092.1\ \mathrm{yr}.$$

The exact factor of ten follows because $\tau \propto l$ in this model: the
relaxation time is proportional to $1/\lambda \propto l$ for an unconfined
half-space. **Units check:** $\mathrm{Pa\,s}\times\mathrm{m^{-1}} /
(\mathrm{kg\,m^{-3}}\times\mathrm{m\,s^{-2}}) =
(\mathrm{kg\,m^{-1}s^{-1}}\times\mathrm{m^{-1}})/(\mathrm{kg\,m^{-2}s^{-2}})
= \mathrm{s}$ ✔.

---

## ★2 — Equilibrium deflection

$$w_\infty = L\frac{\rho_i}{\rho_m} = 2000 \times \frac{917}{3300}
= 2000 \times 0.27788 = 555.8\ \mathrm{m}.$$

**Why a ratio of densities:** the deflection stops growing when the load's weight
is supported by the buoyancy of the mantle material it displaces. Per unit area
the load's weight is $\rho_i gL$ and the buoyancy is $\rho_m gw$, so equilibrium
requires $\rho_mgw = \rho_igL$ and therefore $w = L\rho_i/\rho_m$ — **independent
of $g$** and independent of the rheology. (With a surface water load instead of
ice, the relevant ratio would use the water density and, for a load emplaced in
the ocean, the density contrast $\rho_m-\rho_w$; the model's assumption of an
"air" surface for the load must be stated.)

---

## ★3 — Decay and uplift rates

$$w(t) = w_0e^{-t/\tau}.$$

At $5\ \mathrm{kyr}$: $w = 150e^{-5000/6146} = 150 \times 0.4433
= 66.49\ \mathrm{m}$; mean rate over the interval
$(150-66.49)/5000 = 0.0167\ \mathrm{m\,yr^{-1}} = 16.70\ \mathrm{mm\,yr^{-1}}$.

At $20\ \mathrm{kyr}$: $w = 150e^{-20000/6146} = 150\times0.03862 = 5.79\
\mathrm{m}$; mean rate
$(150-5.79)/20000 = 0.00721\ \mathrm{m\,yr^{-1}} = 7.21\ \mathrm{mm\,yr^{-1}}$.

**Comment.** The *mean* rate over 20 kyr is smaller than over 5 kyr, but the
interesting quantity is the *instantaneous* rate at the end of the interval:
$|w_0e^{-t/\tau}/\tau|$, which falls as $e^{-t/\tau}$. This is the well-known
difficulty of rebound inference: the signal decays exponentially away and the
most informative data sit in the first few thousand years after deglaciation.

---

## ★4 — Ice scale versus viscosity

Write the rate at $t = 10\ \mathrm{kyr}$ as

$$\dot w = -\frac{w_0}{\tau}e^{-t/\tau}, \qquad w_0 \propto sL .$$

**Baseline** ($s = 1$, $\tau = 6146\ \mathrm{yr}$):

$$\dot w = -\frac{150}{6146}e^{-10000/6146}
= -0.02441 \times 0.1962 = -4.796\ \mathrm{mm\,yr^{-1}}.$$

**Doubling the ice scale and halving the viscosity** ($s = 2$ so
$w_0 = 300\ \mathrm{m}$; $\eta \to \eta/2$ so $\tau = 3073\ \mathrm{yr}$):

$$\dot w = -\frac{300}{3073}e^{-10000/3073}
= -0.09762 \times 0.03862 = -3.770\ \mathrm{mm\,yr^{-1}}.$$

The ratio is $3.770/4.796 = 0.786$: the two effects **do not cancel**. Doubling
the scale is undone only partly by halving $\eta$, because the viscosity also
shortens the relaxation time and therefore shrinks the residual deflection.
The compensating change in $\eta$ is *larger* than a factor of two — which is
exactly why the accepted region in the $(\log_{10}\eta, s)$ plane is a broad
region with a curved shape rather than a straight ridge with a slope of $-1$.

**Which effect wins:** at fixed load, halving the viscosity *reduces* the
present-day rate here (from $4.80$ to $3.77\ \mathrm{mm\,yr^{-1}}$ for the
doubled load, and to about half that for the original load), because the residual
deflection decays faster than the rate constant grows once $\tau < t$. So for a
given observation, a larger present-day rate requires *either* a thicker load or a
mantle whose relaxation time is closer to the elapsed time — the second effect is
non-monotonic, which is exactly what makes the accepted region curved rather than
a straight line.

---

## ★5 — Ranking the observables

| data used | acceptable fraction | narrowing relative to the previous row |
|---|---|---|
| A rate alone | $5.1\%$ | — |
| A $+$ B rates | $2.7\%$ | $1.9\times$ |
| A RSL curve alone | $0.36\%$ | $7.5\times$ vs two rates |
| A rate $+$ A RSL curve | $0.30\%$ | $1.2\times$ |
| A rate $+$ A RSL curve $+$ B rate | $0.24\%$ | $1.25\times$ |

**Ranking, best first:** (1) the RSL curve in time, (2) a second site's rate,
(3) the first site's rate. And each *additional* observable contributes less than
the last.

**Interpretation.** A rate is one number whose prediction depends on the product
of the load and the inverse relaxation time; a curve measures the relaxation time
through its *shape*, which the load cannot mimic. That is why the field's
practice is to build RSL databases with many dated sea-level indicators rather
than to measure one uplift rate more precisely.

**Note on the arithmetic of "narrowing":** using fractions of a grid is a coarse
measure. A better statistic is the *range* of $\eta$ in the accepted set, which
the demonstration also prints: from $6.3\times10^{21}$–$2.8\times10^{22}\
\mathrm{Pa\,s}$ for one rate to $1.1\times10^{22}$–$2.8\times10^{22}\
\mathrm{Pa\,s}$ for two. Both statistics should be reported.

---

## ★6 — Why gravity and height are not independent

For a single degree and epoch, the gravity change produced by a deflection $w$ is
proportional to it, because the mass redistribution that raises the surface also
changes the field. In this model

$$\dot g = \frac{\rho_m\,g}{R}\,\dot w ,$$

so $\dot g$ and $\dot w$ are **the same number multiplied by a constant**. Two
measurements with different noise but the same sensitivity give a
noise-weighted average, not a new constraint: the uncertainty would improve by at
most $\sqrt{2}$, never resolving a degeneracy.

**What space gravimetry does add:**

1. **A spectrum.** One solution contains degrees 2 to $L$, whose relaxation times
   differ by a factor of tens — a set of observables with genuinely different
   sensitivities, which is what breaks the degeneracy.
2. **A global integral.** The low-degree coefficients respond to the whole
   glacier inventory, not to the neighbourhood of one tide gauge.
3. **A modern time series**, filling the last two decades where RSL indicators
   are absent.
4. **A different spatial weighting**, which helps separate rebound from
   present-day surface mass change — a practical rather than a conceptual gain.

---

## ★7 — Recovering a layered viscosity (specification)

1. **Layered truth.** A three-layer model: an elastic lithosphere of stated
   thickness, an upper mantle with $\eta_1 = 10^{21}\ \mathrm{Pa\,s}$ to a stated
   depth, and a lower mantle with $\eta_2 = 10^{22}\ \mathrm{Pa\,s}$. Compute the
   synthetic degree-dependent response functions $\tau_l$ for this structure (a
   normal-mode or relaxation-spectrum calculation, or the demonstration's
   half-space form with an effective $\eta(l)$).
2. **Network.** Ten sites: four inside the former ice-sheet centre (large degree-2
   and degree-4 content), four on the periphery (higher degrees, thinner load) and
   two far-field (degree 2 only, dominated by the global ocean load). Each site
   gets 6–10 dated RSL indicators with $2$–$5\ \mathrm{m}$ errors, plus a
   present-day uplift rate with $0.2\ \mathrm{mm\,yr^{-1}}$ noise.
3. **Forward model.** A load history with a stated but uncertain amplitude and
   timing (parameterised with 3–4 numbers), plus the layered response.
4. **Inverse problem.** Fit ($\eta_1$, $\eta_2$, lithosphere thickness, load
   parameters) by a grid or MCMC, and report the marginal distributions and the
   correlation matrix.
5. **Diagnostic.** The posterior *correlations*: expect a strong trade-off between
   the lithosphere thickness and $\eta_1$ (both control the short-wavelength
   response) and between the load parameters and $\eta_2$.
6. **Degeneracy that remains with perfect data.** The degree-$l$ response of a
   layered model is a *sum of exponentials*; a set of curves at $N$ degrees
   determines at most $N$ independent numbers, so a 3-layer model fitted to 10
   degrees is determinable *in principle* but only if the load history is known
   exactly. With the load history free, the degeneracy returns at the level of
   "which layer absorbed the viscosity change". The specification should state
   which subset of the structure the network actually resolves, and acknowledge
   that beyond that subset the answer is the model's prior.

---

## ★8 — The size of the sea-level-equation omission (specification)

1. **Two forward models of the same ice history.** (a) The demonstration's "fixed
   ocean, no meltwater" model; (b) a self-consistent model in which meltwater is
   added uniformly to a *fixed-geometry* ocean, giving an added water load of
   height $\Delta h = \Delta V/A_{\text{ocean}}$ and an added ocean-load response
   computed with the same viscous kernel.
2. **Synthetic data.** Generate RSL curves at five sites from model (b) — the
   "truth" — with stated noise.
3. **Analysis.** Fit the viscosity and ice parameters using model (a).
4. **Diagnostic.** The bias in the inferred viscosity and in the inferred
   deglaciation timing, as a function of the ice volume. Report both, plus the
   residual pattern in the RSL curves (a spatially coherent misfit correlated with
   distance from the ice centre is the signature of the missing load).
5. **Prediction.** The omission biases the inferred viscosity *low* if the missing
   ocean load is a large-scale, long-wavelength addition that mimics a more
   compliant mantle; the bias grows with the ice volume and is largest for
   sites far from the ice sheet, where the ocean-load term is relatively larger.
6. **The observable that reveals it.** The **degree-2 rate from space gravity**,
   because the meltwater's redistribution dominates the low-degree mass budget
   globally while RSL at a single site sees it only through the local load — so
   comparing the degree-2 rebound signal with the site curves exposes a
   mismatch that a single-site fit cannot. A far-field RSL site (one with little
   local ice history) serves the same purpose with an independent measurement.
