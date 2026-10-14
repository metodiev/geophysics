# Exercises — 04-05-02 Glacial and Periglacial Landforms and Sediments

Attempt these **closed-book** before opening the
[solutions](./02-glacial-landforms-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/glacial_landforms_demo.py`](../code/glacial_landforms_demo.py) require
you to run it and report its actual output. **Every velocity must be reported with
the thickness and temperature it assumes, and every property value you use is a
nominal range unless the problem says it is measured.**

Values to use: $\rho_i = 917$ kg m⁻³; $g = 9.81$ m s⁻²; Glen's flow law
$\dot\varepsilon = A\tau^{n}$ with $n = 3$ and $A(0\,^\circ\mathrm{C}) =
2.4\times10^{-24}$ Pa⁻³ s⁻¹; $Q = 6.0\times10^{4}$ J mol⁻¹;
$R = 8.314$ J mol⁻¹ K⁻¹; $\rho_m = 3300$ kg m⁻³; $1$ yr $= 3.15576\times10^{7}$ s.

---

## ★ Foundational

**★1.** An ice mass is $H = 800$ m thick with a uniform surface slope of
$\alpha = 0.5^\circ$.

(a) Compute the basal driving stress $\tau_b = \rho_i g H\sin\alpha$ in Pa.
(b) Compute the depth-averaged internal deformation velocity
$\bar u_d = \frac{2A}{n+1}\tau_b^{n}H$ at 0 °C, in m s⁻¹ and in m yr⁻¹.
(c) Compute the same velocity at $-20\,^\circ$C using
$A(T) = A_0\exp[\frac{Q}{R}(\frac{1}{T_0} - \frac{1}{T})]$ with
$T_0 = 273.15$ K.
(d) State the ratio of (b) to (c).

---

**★2.** The perfect-plasticity model sets
$H = \tau_0/(\rho_i g\sin\alpha)$ with $\tau_0 = 1\times10^{5}$ Pa.

(a) Compute $H$ for a surface slope of $0.3^\circ$.
(b) Compute $H$ for $1.0^\circ$.
(c) Compute $H$ for $3.0^\circ$.
(d) State, in one sentence, what the model reproduces and what it ignores.

---

**★3.** An ice sheet is $H = 1500$ m thick.

(a) Compute its Airy isostatic depression
$\Delta h = (\rho_i/\rho_m)H$ in metres.
(b) Compute the relaxation time
$\tau = 2\eta k/(\rho_m g)$ for a load of wavelength $\lambda = 500$ km with
$\eta = 1\times10^{21}$ Pa s and $k = 2\pi/\lambda$; give the answer in years.
(c) Recompute for $\eta = 5\times10^{20}$ Pa s.
(d) State the scaling of $\tau$ with $\eta$ and with $\lambda$.

---

## ★★ Applied

**★★4.** Take a saturated till with $\rho = 2000$ kg m⁻³ and $v_P = 1700$
m s⁻¹ over granite with $\rho = 2650$ kg m⁻³ and $v_P = 5500$ m s⁻¹.

(a) Compute the acoustic impedances and the normal-incidence reflection
coefficient $R = (Z_2 - Z_1)/(Z_2 + Z_1)$.
(b) Compute the *energy* reflection coefficient $R^{2}$ as a percentage, and
compare it with a typical deep crustal reflection of $R = 0.05$.
(c) Compute $R$ for the water table *inside* the same till, taking the dry till as
$\rho = 1900$ kg m⁻³, $v_P = 900$ m s⁻¹ and the saturated till as in (a).
(d) The till-over-ice contact gives $R = 0.043$ with these properties. Explain in
two sentences why an ice bed is nevertheless mapped with radar rather than with
seismic reflection.

---

**★★5.** The Stefan solution for the active layer is
$X = \sqrt{2k\Delta T t/(L\rho_w)}$ with $k = 1.8$ W m⁻¹ K⁻¹,
$\Delta T = 18$ K, $L = 3.34\times10^{5}$ J kg⁻¹, $\rho_w = 1000$ kg m⁻³,
and a freezing season of 5 months.

(a) Compute $X$.
(b) Recompute for an 8-month season.
(c) Recompute for $\Delta T = 12$ K with the original 5 months.
(d) State the scaling of $X$ with $t$ and with $\Delta T$, and name two
assumptions of the solution that are violated in a real soil.

---

**★★6.** Cold ice has a relative permittivity of 3.17 and
$c = 2.99792458\times10^{8}$ m s⁻¹.

(a) Compute the radar velocity in ice.
(b) Compute the two-way travel time to a bed at 250 m depth.
(c) Compute the wavelength at 50 MHz and the quarter-wavelength vertical
resolution.
(d) Explain the trade-off between resolution and penetration for a radar survey
on an ice sheet, and say which of the two numbers in (b) and (c) that trade-off
controls.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/glacial_landforms_demo.py`](../code/glacial_landforms_demo.py)
and report:

(a) the driving stress and the deformation velocity for the reference case, and
the velocity at 0, $-10$, $-20$ and $-30\,^\circ$C;
(b) the perfect-plasticity thickness at 0.25, 0.5, 1, 2 and 5 degrees;
(c) the Airy depression for 1000, 2000 and 3000 m of ice, and the constant
percentage;
(d) the relaxation time for 100, 1000 and 3000 km load wavelengths;
(e) the reflection coefficients for till over shale, limestone, granite and ice,
and for the dry-versus-saturated till;
(f) the GPR velocity, the travel time at 100, 500 and 2000 m, and the
quarter-wavelength resolution at 100 MHz;
(g) the Stefan depth and the frost-heave upper bounds.

(h) In three sentences say which of these outputs are computed from a derived
formula, which are parameterisations, and which are nominal literature ranges.

---

**★★★8.** Interpretation and its limits.

(a) A survey in glaciated terrain finds an isolated 60 m deep, 400 m wide,
elongate depression in the bedrock surface beneath 30 m of till. List three
plausible glacial origins and, for each, the additional observation that would
discriminate.
(b) The same survey images a sand-and-gravel unit overlain by clay. Explain why a
P-wave reflection survey may fail to resolve the sand while a resistivity or
electromagnetic survey succeeds, and name the contrast each method uses.
(c) A till sheet is mapped as a single unit. Give two reasons its *internal*
architecture matters more than its total thickness for groundwater, and name one
geophysical method that could resolve the architecture.
(d) A moraine crest is dated from its degradation using a hillslope diffusivity
calibrated on a nearby sand plain. State whether the resulting age is likely to
be too old or too young, and justify the sign.
