# Exercises — 01-01-02 Orders of Magnitude and Fermi Estimation

Attempt these **closed-book**, on paper and without a calculator where you can,
before opening the [solutions](./02-orders-of-magnitude-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Write your estimate down **before** you compute the exact value. The estimates
you get wrong are the ones that teach you something. The demonstration
[`code/fermi_estimation.py`](../code/fermi_estimation.py) recomputes the numbers
quoted in the lesson; you may use it to check arithmetic, never to skip the
estimate.

---

## ★ Foundational

**★1.** For each value, (i) write it to **one significant figure** and (ii) state
its **order of magnitude** (the integer power of ten).

(a) $8.4\times10^{3}$
(b) $2.7\times10^{-5}$
(c) $6.02\times10^{23}$
(d) $9.81$

For (d), state which answer is right when the leading digit rounds up, and say
why care is needed.

---

**★2.** Give each to one significant figure, showing the one-line scaling you
used.

(a) The number of seconds in a century. Use $1\ \text{yr} \approx
3.15\times10^{7}\ \mathrm{s}$.
(b) The number of metres in one degree of latitude, using
$R = 6.371\times10^{6}$ m.

For (b), compare your two-step route (circumference, then divide by 360) with
the estimate's worst-case accuracy — is the answer good to a factor of 10, or
much better? Say which regime you are in.

---

**★3.** A compact body of mass $10^{12}$ kg sits $10^{3}$ m below a gravity
station, and the point-mass anomaly is $g_z = GM/d^{2}$.

(a) **Sketch the estimate first**: use $G \approx 6.7\times10^{-11}$
   $\mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and one significant figure throughout, and
   give $g_z$ in mGal. (Use $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$.)
(b) A survey detects anomalies down to 0.01 mGal. Is the body detectable? By
   what factor?
(c) Without redoing the constant arithmetic, scale your answer to a body of mass
   $10^{9}$ kg at 300 m, and check that the two results are consistent.

---

## ★★ Applied

**★★4.** Estimate the total mass of the Earth's atmosphere.

(a) Write the decomposition before you compute: how can the mean surface
   pressure, the Earth's surface area and $g$ give a mass? Name the balance you
   are invoking.
(b) Insert $p_s \approx 1.013\times10^{5}$ Pa, $R = 6.371\times10^{6}$ m and
   $g \approx 9.81\ \mathrm{m\,s^{-2}}$, and give the mass in kg.
(c) The commonly quoted value is about $5.15\times10^{18}$ kg. Report your
   percentage error, and explain why the estimate beat "one order of magnitude".
(d) Express the atmosphere's mass as a fraction of the Earth's mass
   ($5.97\times10^{24}$ kg).

---

**★★5.** A pressure change is introduced at the base of a permeable layer and
diffuses upward over a distance $L = 500$ m. Use the diffusive scaling
$\tau \sim L^{2}/\kappa$.

(a) Compute $\tau$ for $\kappa = 10^{-2}\ \mathrm{m^{2}\,s^{-1}}$, in seconds and
   in days.
(b) Repeat for $\kappa = 10^{-1}\ \mathrm{m^{2}\,s^{-1}}$.
(c) State how $\tau$ depends on $\kappa$, and explain in one sentence why that
   makes hydraulic diffusivity so difficult to constrain in induced-seismicity
   problems.

---

**★★6.** The electromagnetic skin depth is $\delta \approx
503\sqrt{\rho T}$ metres, with $\rho$ in $\Omega\cdot\mathrm{m}$ and $T$ in
seconds.

(a) Solve for the period $T$ that sounds to $\delta = 10$ km in a half-space of
   $\rho = 100\ \Omega\cdot\mathrm{m}$.
(b) Modern broadband instruments cover roughly $10^{-3}$ to $10^{3}$ s. Comment
   on whether the period is practical.
(c) Because $\delta \propto \sqrt{T}$, to sound **ten times deeper** you need how
   many times longer a period? State the consequence for deep sounding.

---

**★★7.** A 20 kg steel object (density $7800\ \mathrm{kg\,m^{-3}}$) is buried
3 m deep and magnetised with $M \approx 1\ \mathrm{A\,m^{-1}}$ in the Earth's
field. Its field at the surface is approximately
$B = \mu_0 m /(4\pi r^{3})$ with $m = MV$.

(a) Compute the volume and the dipole moment $m$.
(b) Compute $B$ at $r = 3$ m, in tesla and in nanotesla.
(c) A total-field magnetometer resolves 0.1 nT. Is the object detectable? State
   your conclusion as an inequality.
(d) The controlling assumption is $M$. Compute the minimum magnetisation
   $M_{\text{min}}$ for detection, and say what determines whether that value is
   plausible.
(e) List two further assumptions in this model and the direction each would move
   the answer.

---

## ★★★ Research-oriented

**★★★8.** A feasibility study of core cooling. Take CMB heat flow
$Q \approx 10\ \mathrm{TW} = 10^{13}$ W, outer-core mass
$M_{oc} \sim 10^{24}$ kg and specific heat capacity
$c_p \sim 10^{3}\ \mathrm{J\,kg^{-1}\,K^{-1}}$.

(a) Compute the timescale to lose enough heat to cool the outer core by 1 K.
   Report it in seconds and in years.
(b) Use a latent heat of fusion $L \sim 10^{6}$ J/kg to bound the time to
   solidify the whole outer core at $10^{13}$ W. State clearly why this is an
   **upper** bound and not a prediction.
(c) List at least three assumptions that control the answer, and say for each
   whether your estimate would rise or fall if the assumption is wrong.
(d) The geodynamo is constrained by palaeomagnetic evidence to have operated for
   at least ~3.5 Ga. Explain why this long-term requirement, rather than an
   instantaneous energy balance, is what actually fixes the parameters of core
   thermal evolution.

Write (c) and (d) as a short critical paragraph, not a list of guesses. Say which
numbers you would have to look up in the primary literature before publishing.

---

**★★★9.** **Numerical verification of the diffusion scaling.** Solve
$\partial_t T = \kappa\,\partial_{zz} T$ on the half-space $z \ge 0$ with
$T(z,0) = 0$ and $T(0,t) = T_0$ for $t > 0$, and measure the time
$t_{1/2}(L)$ at which $T(L,t) = T_0/2$.

(a) For depth $L$ varied at fixed $\kappa$, record $t_{1/2}$ and fit the
   exponent of $t_{1/2} \propto L^{a}$ on log–log axes. Report $a$.
(b) For $\kappa$ varied at fixed $L$, report the exponent of
   $t_{1/2} \propto \kappa^{b}$.
(c) Vary the amplitude $T_0$. Does $t_{1/2}$ change? Explain why the answer must
   be what you found.
(d) Compare your proportionality constant with the exact value
   $4x_{1/2}^{2} \approx 0.9098$, i.e. $t_{1/2} \approx 1.099\,L^{2}/\kappa$.
   State precisely what dimensional analysis could and could not have given you.
(e) **Numerical caution.** State the stability condition for an explicit scheme
   and explain why the grid must resolve the growing boundary layer
   $\sqrt{\kappa t}$. Halve $\Delta z$ and $\Delta t$ and confirm that
   $t_{1/2}$ stops changing; report the value before and after.

Write this up as a genuine numerical-experiment report: method, result with
uncertainty, and stated limitations.

---

## Extension ideas

- Redo ★4 for a different planet: estimate the mass of the Martian atmosphere
  from a mean surface pressure of ~600 Pa and $g \approx 3.7\ \mathrm{m\,s^{-2}}$,
  and compare with the Earth's in a single sentence.
- Repeat ★6 for a resistive half-space, $\rho = 1000\ \Omega\cdot\mathrm{m}$, and
  state how the required period changes.
- Turn ★7 into a function
  `detectable(mass_kg, depth_m, magnetisation, resolution_nt)` returning a
  boolean, and find the depth at which the 20 kg object drops below 0.1 nT at
  $M = 1\ \mathrm{A\,m^{-1}}$.
