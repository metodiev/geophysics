# Solutions — 08-04-05 MT Interpretation: Conductors, Fluids, Melts and Frontiers

> **Read after attempting the exercises.** The lesson is
> [05 MT Interpretation](../05-mt-interpretation.md).

---

## ★1 — Archie's law

$$\sigma_{\text{bulk}} = \sigma_{\text{water}}\phi^{m} = 3.0\times\left(0.02\right)^{2}
= 3.0\times4.0\times10^{-4} = 1.2\times10^{-3}\ \mathrm{S\,m^{-1}},$$
$$\rho = \frac{1}{1.2\times10^{-3}} = 833\ \Omega\mathrm{m}.$$

For comparison, dry granite ($10^{-5}$ S m$^{-1}$, $10^{5}\ \Omega$m) is two orders
of magnitude more resistive and sea-water-saturated sediment is three orders more
conductive: 2% of connected brine already spans a factor of $10^{2}$ in
resistivity.

---

## ★2 — Hashin–Shtrikman bounds at 2% melt

From the lesson's table: lower bound $1.061\times10^{-4}$ S m$^{-1}$, upper bound
$4.037\times10^{-2}$ S m$^{-1}$.

$$\text{ratio} = \frac{4.037\times10^{-2}}{1.061\times10^{-4}} = 380 .$$

Nearly **two and a half orders of magnitude** between the two geometries, at the
same melt fraction. The bounds are rigorous — no arrangement of the phases can
exceed the upper bound — so if the upper bound for a plausible melt fraction falls
short of the observation, melt alone is excluded, which is the most valuable use
of the calculation.

---

## ★3 — Connectivity

A phase conducts only if it forms a continuous path; a fraction of a per cent of
connected melt can dominate the bulk conductivity, while 20% of isolated melt
pockets in a resistive matrix change it hardly at all, because conduction requires
a path from one electrode to the other and isolated inclusions carry no current
across.

---

## ★4 — Conductance of the mantle conductor

$$S = \sigma h = 0.02\ \mathrm{S\,m^{-1}}\times10^{4}\ \mathrm{m} = 200\ \mathrm{S}.$$

The data constrain the product $\sigma h$ — the conductance — and the depth
interval over which it is distributed. They do not constrain the thickness and the
conductivity separately unless the period band includes the periods where the
thin-sheet equivalence breaks; for a conductor at 30–40 km that requires periods
near $\pi\mu_0\sigma L^{2}$ for $L = 10$ km and $\sigma = 0.02$:
$3.9478\times10^{-6}\times0.02\times10^{8} = 7.9\times10^{3}$ s.

---

## ★5 — Required connected-melt fraction

Check the scaling from the bound table: the upper bound is
$2.101\times10^{-3}$ S m$^{-1}$ at $f = 0.001$ and $2.017\times10^{-2}$ at
$f = 0.01$ — a factor of 9.6 for a factor of 10 in $f$, so in this range the upper
bound is very nearly proportional to the melt fraction, at about
$2.0\times10^{-2}$ S m$^{-1}$ per unit $f$ (the melt phase forms the connected
host, so the bound is close to a simple mixing law there).

$$f \approx \frac{0.02}{2.02} = 0.0099 \approx 1.0\% .$$

So a **connected** melt fraction of about 1% explains the conductor. The
unconnected bound at the same fraction is $1.03\times10^{-4}$ S m$^{-1}$ — a
factor of 200 too small — so an unconnected-melt interpretation would require a
fraction of essentially 1, which is not a physical rock. **The interpretation of
this conductor as melt requires connectivity, and connectivity is an assumption
about the geometry that MT cannot test.**

---

## ★6 — Detectable conductance

Linear interpolation between 0 S (0.000$^\circ$) and 10 S (0.453$^\circ$):

$$S_{\min} \approx 10\times\frac{0.2}{0.453} = 4.4\ \mathrm{S}.$$

So with a $0.2^\circ$ phase precision, a conductor of about 4 S at 20 km depth is
the detection threshold. Expressed as conductivity, 4 S in a 10 km layer is
$4\times10^{-4}$ S m$^{-1}$ ($2500\ \Omega$m) — a very modest increase over a
resistive mantle, which shows how sensitive the method is when the phase is
measured well.

---

## ★★7 — Interpretation section (model answer)

> A laterally continuous conductor, 100 km wide and about 5 km thick, is imaged
> at 25 km depth with a **conductance of $200\pm30$ S**. The thickness and
> conductivity are not separately resolved; the model permits $10^{-2}$ S m$^{-1}$
> over 20 km and $4\times10^{-2}$ S m$^{-1}$ over 5 km equally well.
>
> Candidate mechanisms, with the conditions each requires:
>
> 1. **Connected silicate melt**, $\approx1\%$ by volume with a connected network,
>    requiring temperatures above the solidus at 25 km (a high geotherm) and a
>    deformation state that keeps the melt connected.
> 2. **Aqueous fluid in a connected porosity of $\approx2\%$** ($m = 2$), requiring
>    a fluid source and permeability at that depth, and a salinity of sea-water
>    strength.
> 3. **Connected graphite or sulphide**, requiring only a fraction of a per cent,
>    and no thermal or fluid condition at all — which is why it is the hypothesis
>    that must be excluded first.
>
> Two observations would discriminate them: **heat flow** (a melt interpretation
> requires an elevated geotherm, and a conductive geotherm excludes it), and
> **seismic velocity and attenuation** (melt lowers $v_s$ and raises attenuation;
> graphite changes neither; fluids lower $v_p/v_s$). Either alone narrows the
> possibilities; both together usually decide.

---

## ★★8 — The source at long periods

For a conductor at 30–40 km with $\sigma = 0.02$ S m$^{-1}$, the periods needed to
sense it are $T \approx 7.9\times10^{3}$ s, and at that period

$$\delta = \sqrt{\frac{\rho T}{\pi\mu_0}}
= \sqrt{\frac{50\times7.9\times10^{3}}{3.9478\times10^{-6}}}
= \sqrt{1.0\times10^{11}} = 3.2\times10^{5}\ \mathrm{m} = 320\ \mathrm{km},$$

where $\rho = 50\ \Omega$m is representative of the upper mantle. For a source of
width 2000 km, $k = 2\pi/2.0\times10^{6} = 3.14\times10^{-6}$ rad m$^{-1}$, so

$$k\delta = 3.14\times10^{-6}\times3.2\times10^{5} = 1.01 .$$

The criterion $k\delta\ll1$ is **not satisfied**. The plane-wave interpretation is
therefore not justified at those periods for a source of that size, and the
actions are: restrict the periods (and accept a shallower depth limit); model the
source with a magnetospheric current system; or report the conductor as a
conductance with an explicit statement that its depth scale is conditional on the
source model.
