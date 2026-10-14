# Solutions — 09-05-03 Marine CSEM for Hydrocarbon and Gas Hydrate Exploration

> **Read after attempting.** Lesson: [03 Marine CSEM](../03-csem-marine.md).

---

## ★1 — Water diffusion depth and range

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma_w}}
= \sqrt{\frac{2}{2\pi\times0.1 \times 1.2566\times10^{-6}\times3}}
= \sqrt{\frac{2}{2.368\times10^{-6}}} = 918.9\ \mathrm{m},$$

matching the printed table. The $-40$ dB offset is
$2\delta\ln 10 = 2\times918.9\times2.3026 = 4232$ m — also printed. At $0.1$ Hz the
amplitude has fallen by four orders of magnitude at about $4.2$ km.

---

## ★2 — The largest signature

From the MVO table at $0.25$ Hz the largest relative change is at the shortest
offset: $-19.002\%$ at $500$ m, against $-2.958\%$ at $1$ km, $-3.325\%$ at
$2$ km and $\le0.5\%$ beyond $4$ km. The signature is **non-monotone** in offset,
with its maximum at the shortest offset for this target (a reservoir at $200$ m
depth under a $100$ m sediment layer).

---

## ★3 — Resistor against conductor

A hydrocarbon-bearing or hydrate-bearing interval has a non-conductive pore
fluid, so it is *more resistive* than the brine-saturated section around it;
detecting it is a search for a resistor inside a conductor. A sulphide body is a
*conductor* in a resistive host, the opposite contrast, and the two are seen by
the same measurement as opposite signs of the anomaly.

---

## ★4 — The $-20$ dB offset

$$\exp(-r/\delta) = 10^{-1}\ \Longrightarrow\
-\frac{r}{\delta} = \ln 0.1 = -\ln 10\ \Longrightarrow\ r = \delta\ln 10 = 2.3026\,\delta .$$

At $0.25$ Hz, $\delta = 581.2$ m, so $r_{-20\,\mathrm{dB}} = 1338$ m and
$r_{-40\,\mathrm{dB}} = 2676$ m, both printed. The limit is independent of the
target, which is why the water depth and not the target depth sets the offsets a
marine survey can use.

---

## ★5 — The design frequency at $2$ km

From the table, the signature magnitude is $0.983\%$ at $0.05$ Hz (attenuation
$-26.74$ dB), $0.623\%$ at $0.1$ Hz ($-37.81$ dB), $0.295\%$ at $0.25$ Hz
($-59.78$ dB), and smaller above. The *product* of signature and amplitude
factor:

- $0.05$ Hz: $0.983\times10^{-26.74/20} = 0.983\times0.0460 = 0.0452$;
- $0.10$ Hz: $0.623\times10^{-37.81/20} = 0.623\times0.01286 = 0.0080$;
- $0.25$ Hz: $0.295\times10^{-59.78/20} = 0.295\times0.00103 = 0.00030$.

So the largest product in this band is at $0.05$ Hz (the lowest frequency
tabulated): the design frequency lies **below** the band shown. The two
approximations: (i) that the signature and the attenuation factorise, which they
do not exactly because both come from the same secondary field; (ii) that the
detectability is proportional to their product, which ignores the phase of the
response and the noise's frequency dependence.

---

## ★6 — What a $3\%$ anomaly establishes

It establishes that a resistor of some conductance is present at a depth the band
can reach, since $3\%$ is several times the stated $1\%$ noise. It does **not**
establish a resistivity: the measured sensitivity table shows that a factor
$200$ change in reservoir resistivity moves the response by less than $0.1\%$, so
the resistivity is essentially unconstrained. It also does not establish a
thickness, for the same reason — the equivalence of a thin and a thick layer with
the same conductance holds within the noise.

---

## ★7 — Constraining the conductance (specification)

**Offsets.** Five offsets spanning $500$ m to $8$ km, log-spaced at roughly
$500$, $1000$, $2000$, $4000$, $8000$ m. Each adds an independent kernel; the
measured sensitivity says one offset constrains the conductance only to within
tens of per cent, so five reduce that to a few per cent by averaging.

**Statistic.** Invert for a layered model with a fixed section (sediment and
basement from an independent source, e.g. seismic or a prior well log) and report
the posterior on the reservoir conductance $S = \sigma h$. The constraint is
"$S$ within $25\%$" when the $\pm25\%$ contour of the posterior contains no other
structure with a different depth.

**Assumption accepted.** That the section is one-dimensional and that the
reflecting sea surface contributes negligibly at the chosen offsets — an
assumption that grows less safe as the offset increases, so the long offsets that
constrain the conductance most are also the ones most affected by the omission.

---

## ★8 — The omitted sea surface

The upper boundary of the water column is a strong contrast (water $3$ S/m
against air), so at low frequencies and long offsets the field that has travelled
up to the surface and back down arrives *without the diffusive attenuation of the
direct path*, because the air is an insulator. That guided path is coherent with
the earth response, adds a term that decays roughly geometrically rather than as
$\exp(-r/\delta)$, and is precisely the "airwave" that dominates long-offset
marine data. Including it requires a **two-sided layered solution**: reflection
coefficients for the stack below the source *and* for the water column and air
above it, combined by the multiple-reflection series between the two boundaries,
with source and receiver both inside the water layer. That model is standard in
marine EM work and is outside the one-sided formulation used in this lesson.
