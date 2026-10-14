# Solutions — 05-08-04 Density, Neutron and Sonic Porosity Logs

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Four measurements

| Tool | Measurement | Assumption |
|---|---|---|
| Density | Compton attenuation of gamma rays | Known matrix and fluid densities; two-phase rock |
| Neutron | Moderation of fast neutrons by hydrogen | The apparent porosity equals the true one, i.e. the fluid is water-like |
| Sonic | Compressional slowness along the wall | Wyllie's relation (or a stated alternative) applies |
| NMR | Amplitude and $T_2$ of the proton signal | The fluid's $T_2$ is inside the tool's window |

---

## ★2 — Density porosity

**(a)** $\phi_D = (2650-2450)/(2650-1000) = 200/1650 = 0.1212$.

**(b)** $\phi_D = (2650-2450)/(2650-800) = 200/1850 = 0.1081$.

The same log reading gives 0.121 or 0.108 — a 12 per cent relative difference —
purely from the fluid assumption. This is the smallest version of the effect that
makes density porosity unreliable in an unknown fluid.

---

## ★3 — Slowness and time

$100\ \mathrm{\mu s\,ft^{-1}} = 100 \times 3.28084 = 328.1$ µs m⁻¹.

Two-way time over 1000 m: $2 \times 328.1 \times 10^{-6} \times 1000 = 0.6562$ s.

If the 3.28084 conversion is omitted, the answer is 0.200 s — a factor of 3.28
error, which is the exact size of the ft-to-m confusion and the commonest tie
error in the industry.

---

## ★4 — The crossover

**(a)** The apparent neutron porosity when the true fluid has hydrogen index $HI_f$
is

$$\phi_N = \frac{\phi\,HI_f + (1-\phi)HI_{\mathrm{ma}} - HI_{\mathrm{ma}}}
{HI_{\text{water}} - HI_{\mathrm{ma}}}
= \frac{\phi\,HI_f}{1-(-0.02)} .$$

For $\phi = 0.20$: $HI_f = 0.20 \Rightarrow \phi_N = 0.039$; $HI_f = 0.35
\Rightarrow 0.069$; $HI_f = 0.60 \Rightarrow 0.118$. The density apparent porosity
is $0.303$, so the crossovers are $-0.264$, $-0.230$ and $-0.185$ porosity units.

**(b)** Agreement requires $\phi_N = 0.303$, i.e. $HI_f = 0.303\times1.02/0.20 =
1.545$. That is *above* water's value, so no physically available fluid gives
agreement at this true porosity in quartz: the crossover is structurally
unavoidable when a low-density, low-hydrogen fluid is present. The existence is
guaranteed by the two different sensitivities, and that is exactly why the
difference is diagnostic.

---

## ★5 — A limestone layer, inverted with the wrong matrix

Forward with calcite matrix, water, $\phi = 0.08$:
$\rho_b = 0.08(1000) + 0.92(2710) = 2573.2$ kg m⁻³;
$\phi_N = 0.08(1.00) + 0.92(0.00) = 0.080$;
$\Delta t = 0.08(620) + 0.92(156) = 193.1$ µs m⁻¹.

Inversions with a **dolomite** assumption (2870 kg m⁻³, 143 µs m⁻¹):

- density: $\phi_D = (2870-2573.2)/(2870-1000) = 296.8/1870 = 0.159$
  ($+98$ per cent);
- sonic: $\phi_S = (193.1-143)/(620-143) = 50.1/477 = 0.105$ ($+31$ per cent);
- neutron: unchanged at 0.080 (the neutron matrix is the same), which is precisely
  why the neutron log is the one that constrains the *matrix-independent* porosity
  and why the three together identify the mineral.

---

## ★6 — A washed-out interval

Error per metre: $(660-250)\times10^{-6} = 4.10\times10^{-4}$ s one-way, so
$0.820$ ms two-way per metre, and **1.64 ms** over two metres. At 3000 m s⁻¹ that
is $0.5\times3000\times1.64\times10^{-3} = 2.46$ m of depth error — small in
absolute terms here, but it appears as a step in an otherwise smooth time–depth
curve, and a step is unambiguous. Detection: the caliper shows the enlargement, and
the integrated sonic time steps away from the check-shot trend at that depth. The
diagnostic is the *difference* between the sonic integral and the check shot, which
is exactly why the check shot is run.

---

## ★7 — Conditioning of the two-log solve

With the **matrix known** and the fluid's density $ho_f$ **treated as known**,
the system

$$\rho_b = \rho_{\mathrm{ma}} + \phi(\rho_f - \rho_{\mathrm{ma}}), \qquad
\phi_N = HI_{\mathrm{ma}} + \phi\,(HI_f - HI_{\mathrm{ma}})$$

is *triangular* in $(\phi, HI_f)$: the density equation gives $\phi$ directly

$$\phi = \frac{\rho_{\mathrm{ma}} - \rho_b}{\rho_{\mathrm{ma}} - \rho_f},$$

and the neutron equation then gives
$HI_f = HI_{\mathrm{ma}} + (\phi_N - HI_{\mathrm{ma}})/\phi$. The Jacobian
determinant is $(\rho_f - \rho_{\mathrm{ma}})\phi$, which is nonzero for any
physical $\rho_f$ and $\phi$: **with a known fluid density the two-log solve is
exact and well conditioned**, which is why the standard practice of "read density
porosity, then check the neutron" works.

The real problem is that $\rho_f$ is *not* separately known: for a hydrocarbon the
density and the hydrogen index are two properties of one fluid, and with three
unknowns and two equations the system is underdetermined. It becomes solvable only
with a third relation or measurement:

- a **petrophysical fluid relation** $\rho_f(HI_f)$ (a gas gravity/HI chart, or a
  PVT model), after which the system is determined but the answer inherits the
  relation's error;
- **NMR**, whose amplitude is a hydrogen-index measurement that does *not* depend
  on the density, giving an independent third equation;
- **core or a sample**, which fixes one fluid property directly.

The measured demonstration numbers show the stakes: at $\phi = 0.20$ with a gas of
$HI_f = 0.35$ the density reading implies 0.303 and the neutron 0.073 against a
truth of 0.200. **Whichever third relation you add, state it** — the interpretation
is otherwise three unknowns in two equations dressed up as an answer.

## ★8 — A complete synthetic well

Method: fix mineralogy and porosity by layer; use Gassmann to derive saturated
moduli for a changing fluid; convert to $V_p$ with a stated velocity–porosity model
(Raymer–Hunt–Gardner is a reasonable choice); then forward-model density (volume
balance), neutron (hydrogen index), sonic (slowness) and NMR (a $T_2$ spectrum
binned against a stated surface relaxivity). Add a 1 m bed and an invaded zone with
the weighting functions of lesson 01.

Report expected: the workflow recovers porosity exactly in thick, clean,
water-bearing layers; fails by 30–50 per cent in the 1 m bed (resolution, lesson
02 §3.2); fails by a factor in the invaded interval for the resistivity-derived
saturation (lesson 03 §3.4); and fails by tens of per cent where the fluid is gas.
The ranking — resolution, then fluid, then invasion, then matrix — is the result,
and it should be reported as a table rather than a sentence.
