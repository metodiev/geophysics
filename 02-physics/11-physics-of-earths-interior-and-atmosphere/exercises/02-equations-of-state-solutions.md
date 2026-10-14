# Solutions — 02-11-02 Equations of State and High-Pressure Mineral Physics

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Mineral parameters are **nominal, illustrative**
> anchors and are used as such.

---

## ★1 — The second-order equation of state

**(a)** $x = (1/0.9)^{1/3} = 1.035\,744$, so
$x^5 = 1.191\,963$, $x^7 = 1.278\,692$ and
$P_2 = 1.5\times128\times(1.278\,692-1.191\,963) = 1.5\times128\times0.086\,729
= \mathbf{16.65}$ GPa. Note that $P_2$ does not involve $K_0'$, so this is the
second-order value whatever $K_0'$ is.

**(b)** At $V = V_0$, $x = 1$ and $x^7-x^5 = 0$, so $P_2 = 0$.

**(c)** Write $P_2 = \tfrac32K_0\left[(V_0/V)^{7/3}-(V_0/V)^{5/3}\right]$, i.e. with
$c = V/V_0$, $P_2 = \tfrac32K_0(c^{-7/3}-c^{-5/3})$. Differentiating,
$\mathrm{d}P_2/\mathrm{d}c = -\tfrac32K_0\left(\tfrac73c^{-10/3}-\tfrac53c^{-8/3}\right)$,
and at $c=1$ this is $\tfrac32K_0(-7/3+5/3) = -K_0$. Hence
$-V_0(\mathrm{d}P_2/\mathrm{d}V)_{V_0} = K_0$ ✓. It must hold because
$K_0 = -V(\partial P/\partial V)_{V_0}$ is the *definition* of the zero-pressure
bulk modulus; any equation of state that failed this test would be inconsistent
with the parameter it claims to use.

**(d)** A cleaner route than re-differentiating is to use the identity
$-c\,\mathrm{d}P_2/\mathrm{d}c = \tfrac12K_0(7x^7-5x^5)$, which follows from
$\mathrm{d}c/\mathrm{d}x = -3x^{-4}$. At $V/V_0 = 0.9$:

$$K = \tfrac12\times128\times(7\times1.278\,692-5\times1.191\,963)
= 64\times(8.950\,844-5.959\,815) = 64\times2.991\,029
= \mathbf{191.4}\ \text{GPa},$$

i.e. $1.50\,K_0$ — **larger** than $K_0$. Compression stiffens the material: a
cross-check using the approximate identity $K \approx K_0 + K_0'P$ with $K_0'=4$
gives $128+4\times16.65 = 194.6$ GPa, against the exact 191.4 GPa, so the identity
is good to about 2 per cent at this compression.

---

## ★2 — The third-order term and $K_0' = 4$

**(a)** If $K_0'=4$ the bracket is $1+\tfrac34(0)(x^2-1) = 1$, so $P_3 = P_2$
identically, for every $x$. The demo confirms this numerically: the difference is
$0.000\times10^0$ GPa at both $V/V_0 = 0.95$ and $0.85$ for $K_0 = 160$ and
$K_0 = 260$ GPa.

**(b)** $P_2 = \mathbf{16.65}$ GPa (unchanged by $K_0'$). The bracket is
$1+\tfrac34(4.2-4)(1.035\,744^2-1) = 1+0.15\times(1.072\,766-1) = 1.010\,915$,
so $P_3 = 16.65\times1.010\,915 = \mathbf{16.83}$ GPa. Difference: **0.18 GPa**,
about 1.1 per cent.

**(c)** Because the strain expansion's third-order coefficient is fixed by the
requirement that the resulting equation of state reproduce the *measured* $K_0'$.
Subtracting 4 is what expresses "the second-order form already gives $K_0'=4$", so
the residual term must be proportional to the departure from that value. It is a
statement about the reference, not about iron or silicates.

**(d)** For hcp iron. The correction factor is linear in $K_0'-4$, so at the same
$K_0$ and the same compression, $K_0'=5.0$ gives $0.75\times1.0\times(x^2-1)$
against $0.75\times0.2\times(x^2-1)$ — a factor of five larger correction. This is
why $K_0'$ is treated as a serious fitting parameter for core materials and can
often be fixed at 4 for mantle minerals.

---

## ★3 — Seismic parameter and the Adams–Williamson gradient

**(a)** $\phi = 8.1^2-\tfrac43(4.5)^2 = 65.61-27.00 = 38.61$ km² s⁻².

**(b)** Converting, $\phi = 3.861\times10^7$ m² s⁻² — the factor is $10^6$.
Then $K = 3300\times3.861\times10^7 = 1.274\times10^{11}$ Pa $= \mathbf{127.4}$ GPa.

**(c)** $\dfrac{\rho g}{\phi} = \dfrac{3300\times9.81}{3.861\times10^7}
= 8.38\times10^{-4}$ kg m⁻³ m⁻¹ $= \mathbf{0.838}$ kg m⁻³ km⁻¹.

**(d)** Chemical homogeneity of the layer, and adiabatic (isentropic) compression.
The first is what the method is designed to test, and the second follows from a
convecting, well-mixed layer.

---

## ★4 — The adiabatic gradient

**(a)** With $\mathrm{d}S = 0$:
$\dfrac{c_p}{T}\mathrm{d}T = \alpha V\,\mathrm{d}P$, so
$\left(\dfrac{\mathrm{d}T}{\mathrm{d}P}\right)_S = \dfrac{\alpha TV}{c_p}
= \dfrac{\alpha T}{\rho c_p}$ (using $V = 1/\rho$ per unit mass).

**(b)** From $\gamma = \alpha K/(\rho c_p)$ we have
$\alpha/(\rho c_p) = \gamma/K$, so
$(\mathrm{d}T/\mathrm{d}P)_S = \gamma T/K$ ✓.

**(c)** Multiplying by $\mathrm{d}P/\mathrm{d}z = \rho g$:

$$\left(\frac{\mathrm{d}T}{\mathrm{d}z}\right)_S
= \frac{\gamma T}{K}\rho g = \frac{\gamma gT}{K/\rho} = \frac{\gamma gT}{\phi}.$$

**(d)** $\dfrac{1.5\times9.9\times1700}{3.861\times10^7} = 6.538\times10^{-4}$
K m⁻¹ $= \mathbf{0.654}$ K km⁻¹. Over 375 km: $0.654\times375 = \mathbf{245}$ K.

---

## ★5 — Thermal pressure

**(a)** $P(V,T) \approx P(V,T_{\text{ref}}) + \alpha K (T - T_{\text{ref}})$, where
$\alpha$ is the volumetric thermal expansion coefficient, $K$ the bulk modulus (at
the same volume), $T_{\text{ref}}$ a reference temperature such as 300 K, and the
second term is the pressure the material would exert at temperature $T$ if it were
held at the volume $V$.

**(b)** $\alpha K\Delta T = 2.5\times10^{-5}\times650\times10^9\times2525
= 4.10\times10^{10}$ Pa $= \mathbf{41.0}$ GPa.

**(c)** $41.0/135 = \mathbf{30}$ per cent.

**(d)** Because a 30 per cent contribution is a leading term, not a perturbation.
Any comparison between a laboratory equation of state and a seismological model in
the deep Earth that ignores it is wrong at the level of the quantity being
measured — which is why every serious mantle model carries an explicit thermal
term.

---

## ★6 — Inverting the equation of state

**(a)** $\mathrm{d}P/\mathrm{d}V = -K/V < 0$ always, because $K > 0$ for a stable
material. A monotonically decreasing $P(V)$ has a unique $V$ for each $P$, so
bisection — which requires only a bracketing interval and a sign — is guaranteed
to converge.

**(b)** Solve $x^7-x^5 = 10/(1.5\times128) = 0.052\,083$. Bracketing
$[0.3, 1.0]$:

| Step | Midpoint $V/V_0$ | $P_2$ (GPa) | New bracket |
|---|---|---|---|
| 1 | 0.650 000 | 130.96 | $[0.650\,000,\ 1.000\,000]$ |
| 2 | 0.825 000 | 36.20 | $[0.825\,000,\ 1.000\,000]$ |
| 3 | 0.912 500 | 14.08 | $[0.912\,500,\ 1.000\,000]$ |
| 4 | 0.956 250 | 6.26 | $[0.912\,500,\ 0.956\,250]$ |
| 5 | 0.934 375 | 9.95 | $[0.912\,500,\ 0.934\,375]$ |
| 6 | 0.923 437 | 11.96 | $[0.923\,437,\ 0.934\,375]$ |

The converged answer is $V/V_0 = \mathbf{0.9341}$.

**(c)** $x = (1/0.9341)^{1/3} = 1.022\,94$;
$x^5 = 1.120\,14$, $x^7 = 1.172\,22$;
$P_2 = 1.5\times128\times0.052\,08 = 10.00$ GPa ✓.

**(d)** Because 200 bisection steps on a bracket of width 0.7 reduce the interval
by a factor $2^{-200}$, which is far below machine precision: the iteration
terminates at the smallest representable difference between adjacent
floating-point numbers, so the residual reflects the representation of $V/V_0$ and
not any approximation in $P(V)$. A larger residual would indicate an equation of
state whose inversion is ill-conditioned, e.g. one with
$\mathrm{d}P/\mathrm{d}V\to0$.

---

## ★7 — Third-order sensitivity at 100 GPa

**(a)** For periclase $K_0 = 160$ GPa: $V/V_0 = \mathbf{0.722\,25}$ from
$P_2 = 100$ GPa and $V/V_0 = \mathbf{0.743\,51}$ from $P_3 = 100$ GPa with
$K_0' = 5$.

**(b)** $100\times(0.743\,51-0.722\,25)/0.722\,25 = \mathbf{2.94}$ per cent. The
third-order form predicts a *larger* volume at the same pressure, i.e. a softer
material.

**(c)** At $V/V_0 = 0.722\,25$ with $K_0' = 5$: $P_2 = 100.0$ GPa and
$P_3 = 118.2$ GPa, so $P_3-P_2 = \mathbf{18.2}$ GPa.

**(d)** A diffraction experiment measures the volume; the pressure is then
*inferred*. If the wrong $K_0'$ is used, the inferred pressure is wrong by
18 GPa at the 100 GPa point — 18 per cent — and every pressure in the experiment
inherits that error. This is why pressure-calibrating standards (gold, platinum,
MgO) have their equations of state determined with great care, and why an
experimental paper's pressures are only as good as its calibration.

---

## ★8 — Seismic parameters across the CMB

**(a)** Above: $\phi = 13.7^2-\tfrac43(7.3)^2 = 187.69-71.05 = 116.64$ km² s⁻²;
$K = 5570\times116.64\times10^6 = 6.497\times10^{11}$ Pa $= \mathbf{649.7}$ GPa.

**(b)** Below: $v_s = 0$ so $\phi = 8.0^2 = 64.00$ km² s⁻²;
$K = 9900\times64.00\times10^6 = 6.336\times10^{11}$ Pa $= \mathbf{633.6}$ GPa.

**(c)** Density ratio $9900/5570 = \mathbf{1.777}$; $\phi$ ratio
$64.00/116.64 = \mathbf{0.549}$.

**(d)** A change of temperature alone can raise density and *lowers* the bulk
modulus only through thermal expansion, and it cannot change $\phi$ by a factor of
1.8 with a density change of 1.78: a hot material is both less dense and slower, so
the two effects are correlated, not anti-correlated. Density up by 1.8 with
$K/\rho$ down by 1.8 requires $K$ to be roughly unchanged while $\rho$ nearly
doubles, which at a pressure that is continuous across the boundary can only be a
different material.

---

## ★9 — The isothermal shortfall

**(a)** $V/V_0 = 4400/5570 = 0.789\,95$; $x = (1/0.789\,95)^{1/3} = 1.081\,67$;
$x^5 = 1.480\,71$, $x^7 = 1.732\,47$; $P_2 = P_3 = 1.5\times283\times0.251\,76
= 106.9$ GPa (they coincide because $K_0'=4$). The demo reports 107.0 GPa.

**(b)** $100\times(134.6-107.0)/134.6 = \mathbf{20.5}$ per cent short.

**(c)** *Temperature*, pushing the required pressure **up**: a hotter material is
less dense at a given pressure, so more pressure is needed to reach 5570 kg m⁻³.
*Phase change*, also pushing the required pressure **up**: part of the density
increase at depth is mineralogical (bridgmanite replacing ringwoodite) and requires
no pressure, so excluding it from an isothermal single-phase compression inflates
the apparent compression needed.

**(d)** Because taking the reference state just below 660 km places both the
reference and the target inside the same mineral assemblage, so the assemblage
difference across the interval is removed from the comparison and only the
compression of one assemblage remains. The exercise then isolates the thermal
term by itself.

---

## ★10 — Integrating an adiabat

**(a)** Step 1, 660–1000 km: at $T = 1900$ K,
$\mathrm{d}T/\mathrm{d}z = 1.5\times9.947\times1900/6.428\times10^7
= 4.410\times10^{-4}$ K m⁻¹ $= 0.441$ K km⁻¹, so over 340 km
$\Delta T = +150.0$ K.

Step 2, 1000–2000 km: at $T = 2050$ K,
$\mathrm{d}T/\mathrm{d}z = 1.5\times9.883\times2050/7.126\times10^7
= 4.266\times10^{-4}$ K m⁻¹ $= 0.4266$ K km⁻¹, so over 1000 km
$\Delta T = +426.6$ K.

**(b)** $T(1000\ \text{km}) = \mathbf{2050}$ K;
$T(2000\ \text{km}) = 2050+426.6 = \mathbf{2477}$ K.

**(c)** The demo gives 2476 K, essentially identical; the 1 K difference is
whether the temperature is advanced before or after the gradient is recomputed,
i.e. a discretisation choice of the same order as the interval width. This is the
expected agreement between two implementations of the same trapezoidal-style
integration.

**(d)** It does not determine the *absolute* temperature, because an adiabat is a
one-parameter family and the 1900 K anchor is an input. What would determine it: a
melting-point estimate at some depth, a core heat-flow budget, or a laboratory
determination of a phase boundary's temperature. What the calculation *does* fix
is the shape — the gradient and hence temperature *differences*.

---

## ★★★11 — Verification of an equation-of-state implementation

**(a)** *Value test*: reproduce a published $P(V)$ point for a standard material
within its stated uncertainty. *Derivative test*: check
$-V\mathrm{d}P/\mathrm{d}V = K_0$ at $V_0$ **and** that
$\mathrm{d}K/\mathrm{d}P = K_0'$ at $V_0$ — the second is the test most
implementations fail when the third-order bracket is mis-coded. *Consistency
test*: the bulk modulus computed as $-V\mathrm{d}P/\mathrm{d}V$ numerically must
equal the $K(\rho)$ implied by the same parameters through $\phi = K/\rho$ with the
reference-model velocities.

**(b)** A one-line modification that passes the round trip: replace $x$ by $1/x$
in the pressure expression, i.e. invert the strain convention. The function would
still be monotonic and still invertible, so the round trip would still close; only
comparison with data or with $K_0$ would reveal the error. Round-trip tests check
*self*-consistency, never correctness.

**(c)** Thermodynamic consistency here means that a state function — the Helmholtz
or Gibbs energy — must exist, so that mixed second derivatives commute:
$\partial^2F/\partial V\partial T = \partial^2F/\partial T\partial V$. Practically,
the isothermal bulk modulus, the thermal expansion coefficient and the heat
capacity must satisfy $\alpha K_T = \gamma\rho c_V$ with a consistent $\gamma$.
The test is to compute a quantity two ways along different paths (e.g. $K$ from
$-V\partial P/\partial V$ at fixed $T$, and from the thermal equation of state) and
check agreement.

**(d)** A 5 per cent error in $K_0$ propagates into the pressure at 135 GPa
roughly proportionally at low compression but is amplified by the strain expansion
at high compression, where the sensitivity to $K_0'$ dominates: from ★7, at
100 GPa the $K_0'$ choice of 4 against 5 changes the pressure by 18 per cent,
against a 5 per cent change in $K_0$. So at deep-Earth pressures the dominant
uncertainty is $K_0'$, not $K_0$ — which is the practical reason mineral physicists
fight over $K_0'$.

---

## ★★★12 — Where the isothermal equation of state breaks down

**(a)** From ★5(b), the thermal pressure at the CMB scale is about 41 GPa, i.e.
about 30 per cent of the 135 GPa total and about 150 per cent of the 20 per cent
shortfall (which is 27.6 GPa). So the thermal term alone can account for the whole
shortfall *and more*, which means the attribution is not unique: part of the
20 per cent is thermal expansion and part is the phase-change density step, and
the two are not separable without additional information. The honest statement is
that the shortfall is of the same magnitude as the thermal term, and that both
missing effects act in the same direction.

**(b)** A *smaller* $\alpha$ makes the thermal contribution smaller, in which case
the phase-change term must be carrying more of the shortfall. The distinguishing
test is a *seismological* one rather than a thermal one: a phase change produces a
sharp velocity discontinuity at a depth that moves with temperature with the sign
of its Clapeyron slope, whereas a purely thermal effect produces a smooth
gradient. The 660 km discontinuity's sharpness and its anti-correlated depth shift
relative to the 410 km discontinuity are that test.

**(c)** "The fit is calibrated at 300 K and the CMB is at roughly 2500–3000 K, so
the comparison is between a room-temperature compression curve and a hot state.
At 135 GPa the thermal pressure is tens of gigapascals, which is 30 per cent of the
total; ignoring it makes the predicted density too high for a given pressure, by
about the same magnitude as the compositional signals you are trying to detect."

**(d)** Because comparing two assemblages at the *same* $(P,T)$ means the thermal
term is common to both and cancels in the difference. The isothermal equation of
state is being used as a comparative instrument, not as an absolute one, and the
systematic error that matters for absolute densities is irrelevant for a
comparison.

---

## ★★★13 — The observational test of a compositional core

**(a)** Velocities 5 per cent too high with density 1 per cent too low. From
$\phi = v_p^2-\tfrac43v_s^2$ the predicted $\phi$ is about 10 per cent too high,
while $\rho$ is slightly too low, so the predicted $K = \rho\phi$ is about
9 per cent too high: the candidate is too *stiff*. Because the density misfit is
small and the modulus misfit is large, the likely error is in the elastic
parameters — a wrong $K_0$ or a missing phase — rather than in the molar mass, and
the fix is to a stiffer or a lighter-modulus assemblage.

**(b)** $v_p$ correct, $v_s$ 2 per cent low, $\rho$ correct. Then $\mu = \rho v_s^2$
is 4 per cent low and, since $v_p^2 = (K+\tfrac43\mu)/\rho$ is unchanged while
$\tfrac43\mu$ has fallen by 4 per cent of $\mu$, $K$ must be *higher* to
compensate: the shear modulus has been misjudged, not the bulk modulus. In
practice this pattern points at iron content or at a phase with anomalous shear
behaviour.

**(c)** Because a scalar misfit can be produced by many combinations of
composition, temperature and phase, and the combinations are not distinguishable
from one number. The pattern across three observables — and especially the *sign*
of the density misfit relative to the modulus misfits — is what selects among
them. This is the same argument as lesson
[03](../03-seismic-parameter-relations.md) §3.1's degeneracy, applied to the
residual rather than to the model.

**(d)** The falsifying observation would be a *continuous* transition in $\rho$,
$v_p$ and $v_s$ at the CMB, or a density jump accompanied by a *rise* in $v_p$ —
either of which would mean that compression alone could bridge the boundary and no
compositional change would be needed. Neither is observed: the density nearly
doubles while $v_p$ drops by 42 per cent, and the transition is sharp on a seismic
wavelength. That combination has no isothermal or thermal explanation, which
leaves composition.
