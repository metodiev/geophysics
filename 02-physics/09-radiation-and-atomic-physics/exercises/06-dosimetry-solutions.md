# Solutions — 02-09-06 Dosimetry, Radiation Safety and Regulatory Limits

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

**No dose limit appears in these solutions as a number.** Where a limit is needed
it is written $L$, and the answer states which document must supply it. Every
conversion coefficient is either declared as a model input or identified as a
committee recommendation that must be cited.

---

## ★1 — Activity, atoms and mass

**(a)** $\lambda = \ln 2/(30.08 \times 3.155\,76 \times 10^7) = 7.3020 \times
10^{-10}$ s⁻¹; $N = A/\lambda = 10^9/7.3020 \times 10^{-10} =
\mathbf{1.3695 \times 10^{18}}$ atoms.

**(b)** $m = NM/N_A = 1.3695 \times 10^{18} \times 136.907/6.022\,140\,76 \times
10^{23} = 3.113 \times 10^{-4}$ g = $\mathbf{0.311\ mg}$.

**(c)** $10^9/3.7 \times 10^{10} = \mathbf{0.027\,03\ Ci}$, i.e. 27.0 mCi.

**(d)** Because the hazard is proportional to the *number of decays per second*,
and the same mass of a short-lived nuclide carries millions of times the activity
of a long-lived one. An inventory that records mass rather than activity and a
reference date cannot be converted into a dose rate without knowing how old the
source is, which is the one thing that changes.

---

## ★2 — Fluence and the inverse-square law

**(a)** $\varphi = Ay/4\pi r^2 = 500 \times 10^6 \times 0.85/(4\pi \times 200^2)
= 4.25 \times 10^8/5.0265 \times 10^5 = \mathbf{845.5}$ photons cm⁻² s⁻¹.

**(b)** At 4.00 m the distance has doubled, so the fluence is quartered:
$\mathbf{211.4}$ photons cm⁻² s⁻¹.

**(c)** The dose rate falls by a factor of **4**. This is the factor-of-two
rule, and it is worth stating it in the form that is actually useful: the dose
rate is proportional to $1/r^2$, so doubling the distance quarters it, and one
may therefore stay **four times as long** at twice the distance for the same
dose. Halving the distance multiplies the dose rate by four, which is why a
factor-of-two error in a distance is a factor-of-four error in a dose estimate,
and why distances in a dose assessment are measured rather than estimated.

**(d)** For a contaminated floor the source is a **plane** rather than a point.
In the limit where the plane is large compared with the distance, the fluence
does not fall off at all — every extra ring of source at greater radius
contributes less per unit area but there is more of it, and the two effects
cancel exactly. The practical consequences are that surface contamination cannot
be managed by distance, that it must be removed or shielded, and that it is
measured with a large-area probe in contact with the surface.

---

## ★3 — Shielding arithmetic

**(a)** $\mathrm{HVL} = \ln 2/\mu = \mathbf{0.5545}$ cm.

**(b)** $\ln 10/\mu = 2.302\,585/1.25 = \mathbf{1.842}$ cm.

**(c)** $x = \ln 1000/\mu = 6.907\,755/1.25 = \mathbf{5.526}$ cm.

**(d)** It is a **lower bound** on the thickness if the coefficient is right,
because the narrow-beam exponential law ignores the photons scattered back into
the beam, and the build-up factor makes the true transmission larger than the
exponential prediction. It is *also* subject to the opposite error from the
coefficient itself: at an energy where the photoelectric term is significant for
the absorber, the tabulated total coefficient is larger than the Compton-only
value a quick calculation might use, and the thickness is then over-estimated.
Both directions must be stated; a design that names only the safe one is not a
design.

---

## ★★4 — Dose rate and occupancy time

**(a)** $\varphi = 10^9 \times 0.85/(4\pi \times 1.00^2) = 8.5 \times 10^8/12.566 =
\mathbf{6.764 \times 10^7}$ photons m⁻² s⁻¹.

**(b)** 4.0 pSv cm² per photon is $4.0 \times 10^{-12}$ Sv per photon cm⁻², so
per photon m⁻² it is $4.0 \times 10^{-12} \times 10^{-4} =
4.0 \times 10^{-16}$ Sv m². Then
$\dot H = 6.764 \times 10^7 \times 4.0 \times 10^{-16} = 2.706 \times 10^{-8}$
Sv s⁻¹ = $2.706 \times 10^{-2}$ µSv s⁻¹ = $\mathbf{0.0974}$ mSv h⁻¹ (using
$3.6 \times 10^6$ to convert Sv s⁻¹ to mSv h⁻¹). The demo prints the same.

**(c)** $0.0974 \times 1.25 = \mathbf{0.1218}$ mSv h⁻¹. The dose rate is exactly
linear in the coefficient.

**(d)** $t = L/\dot H$. At 1.00 m with $\dot H = 0.0974$ mSv h⁻¹:
$t = L/0.0974$ hours; for $L = 1.0$ mSv a⁻¹, $t = \mathbf{10.27}$ h a⁻¹. At
1.50 m the dose rate is smaller by $(1.5)^2 = 2.25$, so
$t = 2.25L/0.0974$ hours; for $L = 1.0$ mSv a⁻¹, $t = \mathbf{23.10}$ h a⁻¹. The
demo prints 10.27 and 23.10.

The limits: $L$ must be taken from the **national regulation in force**, which
implements the current recommendations of the International Commission on
Radiological Protection and the IAEA safety standards, and the citation must name
the publication and the year. The coefficient must be taken from the current
**ICRP conversion-coefficient publication** appropriate to the quantity being
computed (an ambient dose equivalent per unit fluence, or an effective dose per
unit fluence for a stated geometry and exposure orientation). Neither may be
supplied from memory, and the two are items of different kinds: one is a legal
instrument that changes with jurisdiction, the other is a recommendation that
changes with radiobiology.

---

## ★★5 — Counting statistics and detection limits

**(a)** $\sigma_\mathrm{net} = \sqrt{R_b/t_b + R_b/t_s} = \sqrt{2/3600 +
2/600} = \sqrt{5.556 \times 10^{-4} + 3.333 \times 10^{-3}} = \sqrt{3.889 \times
10^{-3}} = \mathbf{0.0624}$ s⁻¹.

**(b)** $\mathrm{MDA} = 3\sigma_\mathrm{net}/(\epsilon y) = 3 \times 0.0624/
(0.05 \times 0.85) = 0.1871/0.0425 = \mathbf{4.40}$ Bq.

**(c)** $\sigma_\mathrm{net} = \sqrt{5.556 \times 10^{-4} + 5.556 \times 10^{-4}}
= 0.0333$ s⁻¹, giving $\mathrm{MDA} = \mathbf{2.35}$ Bq. The demo prints 4.4 and
2.4 for 600 s and 3600 s.

**(d)** As $t_s \to \infty$, $\sigma_\mathrm{net} \to \sqrt{R_b/t_b}$ and
$\mathrm{MDA} \to 3\sqrt{2/3600}/(0.0425) = \mathbf{1.66}$ Bq. The floor is set
by the **background counting time** — by how well the background rate itself is
known, not by how long the sample is counted. This is why a measurement campaign
that wants a lower detection limit must spend its time on the background as well
as on the samples, and why a limit quoted with a 60 s background is not the same
number as the same limit quoted with an hour of background.

---

## ★★6 — Beta shielding

**(a)** Aluminium: $13 \times 2.28/3000 = 9.88 \times 10^{-3}$, i.e.
**0.99 per cent** of betas produce a photon. Lead:
$82 \times 2.28/3000 = 6.23 \times 10^{-2}$, i.e. **6.2 per cent**. The demo
prints 9.88 and 62.32 photons per 1000 betas.

**(b)** The ratio is $6.23 \times 10^{-2}/9.88 \times 10^{-3} = \mathbf{6.3}$,
i.e. $82/13$.

**(c)** Because the lead itself converts the beta energy into hard bremsstrahlung
photons at six times the rate aluminium would, and lead must then attenuate a
photon flux that the aluminium arrangement never created. The shield has become a
source. The fix is to put a few millimetres of plastic or aluminium against the
source first, so that the betas are stopped where their radiative yield is small
and the bremsstrahlung they do produce is soft; the lead then sees a much weaker
and softer photon field.

**(d)** The estimate ignores **self-absorption in the source and in the
absorber**: a beta that is stopped within the encapsulation never reaches the
shield, and a bremsstrahlung photon produced deep inside the lead must itself
escape. It also uses a single average yield rather than the energy- and
angle-dependent spectrum, and it treats the production as isotropic when it is
forward-peaked. Use it to decide the *ordering* of layers, and use a transport
calculation for a thickness.

---

## ★★★7 — Running the demo

**(a)** 1 GBq of caesium-137: $1.3695 \times 10^{18}$ atoms and
$3.1134 \times 10^{-1}$ mg of nuclide.

**(b)** 0.3 m: $7.5157 \times 10^4$ cm⁻² s⁻¹; 1.0 m: $6.7641 \times 10^3$;
4.0 m: $4.2276 \times 10^2$.

**(c)** Water: $\mu = 0.0870$ cm⁻¹, HVL 7.967 cm, tenth-value 26.466 cm, 100×
52.933 cm. Concrete: 0.1800, 3.851, 12.792, 25.584. Iron: 0.5770, 1.201, 3.991,
7.981. Lead: 1.2500, 0.555, 1.842, 3.684.

**(d)** With $\mu$ 20 per cent larger, the 100× thickness becomes 3.0701 cm
against 3.6841 cm, a change of **−16.67 per cent**. The fractional thickness
change is $-d/(1+d)$ with $d = 0.2$, which is $-16.67$ per cent and not
$-20$ per cent.

**(e)** $0.0974$ mSv h⁻¹ at a coefficient multiplier of 1.0; 0.0487 at 0.5;
0.1948 at 2.0.

**(f)** MDA 13.0 Bq at 60 s, 2.4 Bq at 3600 s, 1.7 Bq at 36 000 s; floor
1.66 Bq.

**(g)** At 1.00 m: 10.27 h for $L = 1.0$ mSv a⁻¹, 51.33 h for 5.0, 205.33 h for
20.0.

**(h)** Computed: the atom count, the mass, the fluence rate, the attenuation
thicknesses, the dose rate (given the coefficient), the Poisson statistics, the
MDA and the occupancy times. Model inputs: the illustrative attenuation
coefficients, the fluence-to-dose coefficient, the detection efficiency, the
gamma yield, the background rate and the gas density. Tabulated: the half-life
and the molar mass. **Symbolic by design: the dose limit $L$**, which the script
prints as a column of values for the reader to select, because it is a
jurisdiction-specific legal quantity that must be taken from the regulation in
force.

---

## ★★★8 — Presenting an assessment

**(a)**

$$\dot H = \frac{Ayh}{4\pi r^2}, \qquad t = \frac{L}{\dot H} .$$

Inputs and their sources: $A$ (the source's declared activity at a reference
date, from its certificate); $y$ (the gamma yield, from a decay-data
compilation); $h$ (the fluence-to-dose coefficient, from the current ICRP
conversion-coefficient publication, with its energy and geometry conditions
stated); $r$ (a measured distance, with the geometry — point, line, plane — stated
because the exponent depends on it); and $L$ (the limit, from the national
regulation in force, which implements the current IAEA safety standards and ICRP
recommendations, cited by publication and year).

**(b)** Three reasons. First, no **limit** is cited, so "well within" has no
referent, and the limit depends on the worker category and the jurisdiction.
Second, no **conversion coefficient** is cited, and the dose rate is linear in it:
a factor of two in the coefficient is a factor of two in the number. Third, no
**geometry or distance** is stated, and the inverse-square law means the number
is meaningless without it; the sentence also omits the *time* at that dose rate,
which is what turns a dose rate into a dose.

**(c)** Because the hazard from uranium-bearing rock in an enclosed space is
dominated by **radon**, which is inhaled and whose progeny irradiate the
bronchial epithelium, and radon is a *gas* whose concentration depends on
ventilation rather than on the gamma flux. A normal gamma field is exactly what
one expects from a moderate uranium concentration; it says nothing about the
radon concentration, which is the quantity that can approach a limit in a shed.
The measurement to make is a **radon (and radon-progeny) concentration
measurement** with a suitable monitor, over a representative period, along with
an assessment of ventilation and occupancy; the assessment requires the current
national reference level and the current IAEA guidance on radon.

**(d)** Intake in becquerel → **activity**; multiply by a **dose coefficient per
unit intake** in sievert per becquerel (the "e(50)" or committed effective dose
coefficient, tabulated per radionuclide, per route of intake, and per chemical
form) to get the committed effective dose in sievert. That coefficient comes from
the current **ICRP dose-coefficient publication** for the appropriate age group
and integration period, and it is a recommendation rather than a measurement. An
**air concentration** in becquerel per cubic metre converts to an intake through
a **breathing rate**, whose value is a convention (a reference worker's rate for
the exposure scenario) that must be stated along with its source. Neither factor
may be supplied from memory, and the report must state the model — the particle
size distribution, the solubility class and the exposure duration — because the
coefficients are defined relative to a stated model.
