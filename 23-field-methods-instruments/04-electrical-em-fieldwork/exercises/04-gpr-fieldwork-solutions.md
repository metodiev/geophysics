# Solutions — 23-04-04 GPR Fieldwork: Antenna Choice, Grids, Coupling, Calibration

> Read after attempting. Lesson:
> [04 GPR Fieldwork](../04-gpr-fieldwork.md). All values are **SYNTHETIC**.

---

## ★1 — Velocity, wavelength and resolution at $\varepsilon_r = 6$, 400 MHz

$$v = \frac{c}{\sqrt{\varepsilon_r}} = \frac{0.299792458}{\sqrt{6}}
= \frac{0.299792458}{2.449490} = 0.122389\ \mathrm{m/ns}.$$

$$\lambda = \frac{v}{f} = \frac{0.122389 \times 10^{9}\ \mathrm{m/s}}{400\times10^{6}\ \mathrm{Hz}}
= 0.305972\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 0.076493\ \mathrm{m}.$$

Units: $v$ in m/ns (equivalently $10^{9}$ m/s), $\lambda$ and $\lambda/4$ in metres.
The shortcut worth carrying in the field: $\lambda\,[\mathrm{m}] = 1000\,v\,[\mathrm{m/ns}]/f\,[\mathrm{MHz}]$.

---

## ★2 — Hyperbola velocity and depth

$$v = \frac{2x}{\sqrt{t^{2}-t_0^{2}}}
= \frac{2 \times 0.75}{\sqrt{11.3^{2} - 8.0^{2}}}
= \frac{1.50}{\sqrt{127.69 - 64.00}} = \frac{1.50}{7.98060}
= 0.187956\ \mathrm{m/ns}.$$

$$\varepsilon_r = \left(\frac{c}{v}\right)^{2}
= \left(\frac{0.299792458}{0.187956}\right)^{2} = (1.595019)^{2} = 2.54409 .$$

$$d = \frac{v\,t_0}{2} = \frac{0.187956 \times 8.0}{2} = 0.751824\ \mathrm{m}.$$

So the target is 0.75 m deep in a material of $\varepsilon_r = 2.54$ — dry soil or
rock, consistent with the fast velocity. Note how much the answer depends on the
measured offset: a 10 cm error in $x$ changes $v$ by 13 %.

---

## ★★3 — Trace spacing, trace count and time

$$\text{spacing} = \frac{\lambda}{4} = \frac{0.187956 \times 10^{9}/250\times10^{6}}{4}
= \frac{0.751824}{4} = 0.187956\ \mathrm{m}$$

(wait: the wavelength at 250 MHz with $v = 0.187956$ m/ns is
$\lambda = 1000 \times 0.187956/250 = 0.751824$ m, so $\lambda/4 =
0.187956\ \mathrm{m}$). At a 250 MHz antenna this site tolerates a 0.19 m trace
spacing; at 400 MHz it would be $\lambda = 0.469872$ m and $\lambda/4 = 0.117468$ m.

**Traces on a 30 m line** at the 250 MHz spacing:

$$N = \frac{30}{0.187956} + 1 = 159.6 + 1 = 160.6 \;\Rightarrow\; 161 \text{ traces}.$$

**Time** at 4 s per trace: $161 \times 4 = 644\ \mathrm{s} = 10.7$ minutes per line.
A 30 m × 30 m grid with lines at that spacing in both directions is
$161 \times 161 = 25\,921$ traces, or **28.8 hours** — which is why a grid survey is
planned around an acceptable spacing rather than the theoretical one, and why the
antenna frequency and the survey area are chosen together.

---

## ★★4 — Attenuation budget at 2.5 dB/m

$$d_{\max} = \frac{\text{range}}{2\alpha} = \frac{90}{2 \times 2.5} = 18.0\ \mathrm{m}.$$

**Depth at which the two-way loss is 60 dB:**

$$2\alpha d = 60 \;\Rightarrow\; d = \frac{60}{5.0} = 12.0\ \mathrm{m}.$$

So at 12 m the signal has lost 60 dB of the 90 dB available, leaving 30 dB of
signal-to-noise before the system's own floor — a usable but not generous margin,
and the reason the instrument's dynamic range, not the antenna, is often the
limiting factor at depth. Doubling the dynamic range to 180 dB would extend
$d_{\max}$ to 36 m, but only if the *noise* stayed constant, which it does not: the
late-time record at depth is contaminated by everything from surface reflections to
the antenna's own ringing.

---

## ★★5 — Calibration and the cost of a wrong permittivity

$$v_{\text{true}} = \frac{2d}{t} = \frac{4.00}{26.0} = 0.153846\ \mathrm{m/ns},
\qquad
\varepsilon_r = \left(\frac{0.299792458}{0.153846}\right)^{2} = (1.948652)^{2}
= 3.797 .$$

**Reported depth using $\varepsilon_r = 9$** (velocity
$0.09993\ \mathrm{m/ns}$):

$$d_{\text{reported}} = \frac{v\,t}{2} = \frac{0.09993 \times 26.0}{2}
= 1.29909\ \mathrm{m},$$

$$\text{error} = \frac{1.29909 - 2.00}{2.00} = -35.0\ \%.$$

A 35 % depth error — 70 cm on a 2 m target — is enough to miss a utility, to
mislocate a foundation, or to make a stratigraphic interpretation wrong. It arises
from a difference between an *assumed* $\varepsilon_r$ of 9 and a real one of 3.8,
i.e. from assuming a wet material where the material is dry. The lesson is
quantitative: **measure the velocity at the site** (a known target or a hyperbola)
rather than assuming a textbook permittivity for the material type.

---

## ★★★6 — A buried-utility survey over 30 m × 30 m, 0.5–2.5 m depth

**Antenna frequency.** The shallowest target sets the resolution requirement and the
deepest sets the penetration requirement. Take $\varepsilon_r = 9$ as a planning
value (moist soil), so $v = 0.09993$ m/ns:

- To resolve a target 0.5 m deep with a $\lambda/4$ criterion, allow the resolution
  to be coarser than the target scale: the requirement is $\lambda/4 \le 0.25$ m,
  i.e. $\lambda \le 1.0$ m, i.e. $f \ge 100$ MHz.
- To reach 2.5 m with, say, 1.5 dB/m one-way attenuation, the two-way loss is
  $2 \times 1.5 \times 2.5 = 7.5$ dB — comfortable, so penetration is not the
  binding constraint.

Choose a **250 MHz** antenna: $\lambda = 0.3997$ m, resolution 0.0999 m, which
resolves a 100 mm pipe and still reaches several metres in moist soil. Carry a
100 MHz antenna as the fallback for a wet or clayey area.

**Trace spacing.** Migration requires $\lambda/4 = 0.0999$ m ≈ 0.10 m at 250 MHz.
For utility mapping, where the target is a *linear* feature and the requirement is
positional rather than vertical, a **0.10 m** spacing in the direction across the
lines is the design value, with lines at **0.50 m** spacing along the corridor —
giving 0.10 m sampling along each line and 0.50 m between lines.

**Traces and time.** A 30 m × 30 m block with crossing line sets at 0.50 m spacing:

- 61 lines in each direction at 0.50 m spacing;
- $30/0.10 + 1 = 301$ traces per line;
- $61 \times 301 \times 2 = 36\,722$ traces;
- at 4 s per trace: $146\,888\ \mathrm{s} = 40.8$ hours of continuous work.

That is a five-day survey for a 30 m × 30 m site at the theoretical spacing, which
is the honest number to put in the plan. The reductions available: survey only the
corridor rather than the whole block; use 0.20 m along-line spacing where the
target is a pipe (the migration requirement is relaxed for a linear target if the
position is picked from the apex rather than migrated); use a single line
orientation plus a few cross-lines if the utility directions are known.

**Velocity calibration.** Method 1: a **known target** — a plate buried by the team
at a measured 1.0 m depth, or a known pipe whose depth is on the service drawings.
Method 2: a **hyperbola** from an isolated small object (a single stone, a
boundary marker), with the offset measured on the ground. Method 3: **wide-angle
reflection** on a horizontal reflector if a suitable one exists. Take the value from
at least two methods and reconcile them; if they disagree by more than 5 %, find out
why (different materials along the line, a mis-measured offset, a mis-identified
target).

**Records to keep.** The antenna frequency and model, the trace spacing (measured,
not assumed), the line azimuth and the grid coordinates, the surface condition
along each line (paved, grass, tarmac, wet), the antenna height and whether a
survey wheel or a skid was used, the operator, the time, and the calibration
measurement with its analysis. Coupling changes are the most common cause of a
line that looks different from its neighbours, and the record is what allows the
difference to be explained rather than discovered later.

**Two situations that would force a change of frequency.**

1. **A wet or clayey area** where the penetration at 250 MHz is inadequate: the
   high-frequency signal is attenuated before reaching 2.5 m, and the survey must
   drop to 100 MHz (coarser resolution, more depth) or wait for drier conditions.
   The diagnostic is the *absence of the deep reflector* on the record while the
   shallow ones remain.
2. **A requirement for finer than 0.10 m vertical resolution**, for example to
   separate two closely spaced pipes or to resolve thin pavement layers. That
   forces a 500 MHz or 900 MHz antenna and therefore a shallow-only survey, which
   is a different survey with a different grid and a different time budget.
