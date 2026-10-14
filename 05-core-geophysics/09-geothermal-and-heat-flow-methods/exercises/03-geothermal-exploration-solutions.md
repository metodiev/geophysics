# Solutions — 05-09-03 Geothermal Exploration Geophysics

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Three requirements

| Requirement | Measured directly by geophysics? |
|---|---|
| Heat | Yes — temperature logs, heat-flow maps, geotherms |
| Fluid | Partly — inferred from resistivity, seismics and wells |
| **Permeability** | **No** — nothing at the surface resolves it at reservoir scale |

Microseismicity and structural mapping give proxies for permeability (movement, and
geometry), but neither measures it.

---

## ★2 — The clay cap

Hot fluids ascending along fractures alter the rock above the reservoir, forming
smectite and other clays in the temperature range where they are stable; those clays
are **electrically conductive**. Deeper, higher-temperature alteration forms illite,
chlorite and epidote, which are **resistive**. The result is a conductive cap over a
resistive reservoir, and MT maps it — but the association between the cap's base and
the reservoir top is an empirical correlation, not a measurement.

---

## ★3 — Heat in place

$$\frac{H}{A} = (2.4\times10^{6})(200)(0.04)(150)
= 2.88\times10^{9}\ \mathrm{J\,m^{-2}} .$$

It is **not a resource**. It assumes every joule is produced, which is what a
recovery factor parameterises; recovery depends on permeability, fluid, well design,
reinjection and economics, none of which appears in the equation.

---

## ★4 — The demonstration's stability results

**(a)** Free-slip: $Ra_c = 657.5110$ at $N = 28$ and $N = 32$, against the closed
form $27\pi^4/4 = 657.5114$, i.e. agreement to **0.0001 per cent**. Rigid:
$Ra_c = 1707.7616$ at $N = 24$, 28 and 32, against the reference 1707.762,
i.e. agreement to **better than 0.0001 per cent**.

**(b)** The script reports that at $N \ge 36$ the eigenvalue *selection* (the
smallest positive real eigenvalue) picks a spurious mode and the rigid value
degrades by about 0.4 per cent. So the numerical method has a working range, and
"more resolution" is not automatically better without checking which eigenmode is
being reported.

**(c)** They are quoted **only because they are re-derived here**. The repository's
rule is that no remembered constant is presented as fact, and the way to satisfy it
for these two numbers is to measure them — which the demonstration does, with the
closed form available as an independent check for the free-slip case.

---

## ★5 — Temperature at depth

**(a)** $k_\perp = (0.40/1.5 + 0.40/3.5 + 0.20/2.8)^{-1}
= (0.2667 + 0.1143 + 0.0714)^{-1} = (0.4524)^{-1}
= 2.211\ \mathrm{W\,m^{-1}\,K^{-1}}$.

**(b)** The gradient is $q/k_\perp = 75/2.211 = 33.9$ K km⁻¹, so
$T(2\ \mathrm{km}) = 12 + 2 \times 33.9 = 79.8$ °C.

**(c)** With 60 per cent sandstone and 20 per cent shale (keeping 20 per cent
limestone): $k_\perp = (0.20/1.5 + 0.60/3.5 + 0.20/2.8)^{-1}
= (0.1333+0.1714+0.0714)^{-1} = (0.3761)^{-1} = 2.659$ W m⁻¹ K⁻¹; the gradient falls
to 28.2 K km⁻¹ and $T(2\ \mathrm{km}) = 68.4$ °C.

**A change of 20 percentage points in the sandstone fraction moves the temperature at
2 km by 11.4 K, or 17 per cent of the temperature rise.** That is why, in a
conductive play, mapping lithology (seismic, gravity) is more valuable than mapping
heat.

---

## ★6 — What an MT cap establishes

**Establishes:** that a conductive (clay-altered) interval exists between 300 and
900 m, and that a more resistive interval lies below it. That is consistent with a
clay cap over a possible reservoir.

**Does not establish:** that the resistive zone is permeable; that it is connected
to a heat source; that fluid is present; or that the cap's base is the reservoir top.

**The two measurements that would most reduce the risk:**

1. **A temperature-gradient hole** (or a temperature log in any existing hole) to
   establish the heat and the geotherm — cheap, decisive about the heat, silent
   about permeability.
2. **A structural/mechanical dataset that constrains which faults are open** — 3-D
   seismic or structural mapping plus a geomechanical argument, potentially with
   microseismic monitoring during a flow test.

Ultimately, only a **flow test in a well** settles the decisive variable, which is
why exploration programmes budget for two to four wells before substantiation.

---

## ★7 — A fault-hosted conductive–convective model

Method: solve the steady advection–conduction equation in 2-D with a prescribed
vertical Darcy velocity in a narrow conduit (say 200 m wide) embedded in a
conductive half-space; compute the surface heat flow and the temperature along a
vertical line 500 m from the conduit axis.

Expected results:

- the surface heat flow peaks over the conduit (by a factor of several for a
  realistic flux) and decays to the regional value within a few conduit widths;
- the temperature profile 500 m from the fault is elevated relative to the purely
  conductive profile, with a **convex-up** curvature in the upper few hundred metres
  (a higher gradient near the surface) — the classic advection signature;
- within the conduit, the profile is nearly isothermal at depth (well-mixed) with a
  very high gradient near the surface.

**Diagnostic:** curvature. A purely conductive profile is a straight line (for
constant $k$ and $q$); advection bends it. The magnitude of the bend, and its
characteristic length $k/(\rho_f c_f v)$, give the flux if $k$ is known — and the
ambiguity with a depth-dependent $k$ must be stated, as in
[05-09-01 ★★★8](./01-heat-flow-measurement-solutions.md).

---

## ★8 — A greenfield programme

**Methods and why:**

| Stage | Method | Decision it supports |
|---|---|---|
| Reconnaissance | Regional heat-flow and geology; existing wells | Is the heat there? |
| Targeting | MT/CSEM | Where is the clay cap and the resistive zone? |
| Structure | Gravity, magnetics, structural mapping | Where are the faults, and which are young/active? |
| Activity | Microseismic monitoring | Is fluid moving now? |
| Heat | Temperature-gradient holes (2–3, 200–500 m) | The local geotherm and the conductivity |
| Test | Exploration well with a flow test | **Permeability** — the decisive measurement |

**Interpretation chain:** MT inversion with its own uncertainty; the clay cap
mapped with its base as an *inferred* horizon; structural model with fault
kinematics; heat-flow model with a lithological conductivity column; a conceptual
model that states which elements are measurement-supported and which are inference.

**Decision points:** after MT (is there a cap and a resistive zone?); after the
temperature holes (is the heat sufficient?); after the structural model (is there a
plausible plumbing geometry?); and the well decision, which is taken with the risk
concentrated in permeability.

**Uncertainty to state:** heat in place with the volume uncertainty from the mapped
cap geometry, and the recovery factor left symbolic; the probability of permeability
stated as a judgement with its basis, not as a number derived from the geophysics.

**Which decisions rest on geophysics:** where to drill, how deep, and what
temperature to expect. **Which require a well:** whether it will produce.
