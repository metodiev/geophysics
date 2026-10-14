# Solutions — 08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [07 Rock Magnetism](../07-rock-magnetism.md).

---

## ★1 — Coercivity in field units

$$\mu_0H_c = 4\pi\times10^{-7}\times1.5\times10^{4}
= 1.8849556\times10^{-2}\ \mathrm{T}
= 1.8850\times10^{4}\ \mu\mathrm{T}.$$

Dividing by $\mu_0$ is a physical conversion, not a unit prefix change: the
"same" number in $\mathrm{A\,m^{-1}}$ and in $\mu$T differs by a factor
$1.2566\times10^{6}\ \mu\mathrm{T}$ per $(\mathrm{A\,m^{-1}})$.

---

## ★2 — Induced magnetisation

$$H = \frac{B}{\mu_0} = \frac{48000\times10^{-9}}{4\pi\times10^{-7}}
= 38.1972\ \mathrm{A\,m^{-1}},$$
$$J = \kappa H = 0.02\times38.1972 = 0.763943\ \mathrm{A\,m^{-1}},$$
$$\mu_0J = 1.256637\times10^{-6}\times0.763943 = 9.6000\times10^{-7}\ \mathrm{T}
= 960.00\ \mathrm{nT},$$
$$\frac{\mu_0J}{B} = \frac{960.00}{48000} = 0.0200 = 2.00\%.$$

The percentage equals $\kappa$: that identity is a useful check, since a
susceptibility of 0.02 predicting a 2% induced field is exactly what the
definition says.

---

## ★3 — Remanence ratio

$$\frac{J_{rs}}{J_s} = \frac{1.5\times10^{5}}{5.0\times10^{5}} = 0.30.$$

---

## ★4 — Koenigsberger ratio and its crossover field

$$Q = \frac{J_r}{|\kappa H|} = \frac{0.8}{0.02\times38.1972}
= \frac{0.8}{0.763943} = 1.0472.$$

$Q > 1$, so the rock is **remanence-dominated** at this field — but only just.

For $Q = 1$ at fixed $J_r$ and $\kappa$:

$$H^{*} = \frac{J_r}{\kappa} = \frac{0.8}{0.02}
= 40.000\ \mathrm{A\,m^{-1}}, \qquad
B^{*} = \mu_0H^{*} = 1.256637\times10^{-6}\times40.000
= 5.0265\times10^{-5}\ \mathrm{T} = 50265\ \mathrm{nT}.$$

So the rock switches from remanence-dominated to induced-dominated if the ambient
field rises above about 50.3 $\mu$T. Nothing about the rock has changed; only the
field has.

---

## ★5 — Blocking volume and its time dependence

$$\ln\frac{\tau}{\tau_0} = \ln 10^{11} = 25.3284
\quad (\text{laboratory}),$$
$$\ln\frac{10^{15}}{10^{-9}} = \ln 10^{24} = 55.2620
\quad (\text{geological}).$$

$$V_b^{\text{lab}} = \frac{k_BT\ln(\tau/\tau_0)}{K}
= \frac{1.380649\times10^{-23}\times650\times25.3284}
{3.0\times10^{4}}$$
$$= \frac{2.27303\times10^{-19}}{3.0\times10^{4}}
= 7.5768\times10^{-24}\ \mathrm{m^{3}},$$

$$d^{\text{lab}} = \left(\frac{6V_b}{\pi}\right)^{1/3}
= \left(\frac{6\times7.5768\times10^{-24}}{\pi}\right)^{1/3}
= (1.44697\times10^{-23})^{1/3} = 2.43685\times10^{-8}\ \mathrm{m}
= 24.368\ \mathrm{nm}.$$

$$V_b^{\text{geo}} = 7.5768\times10^{-24}\times\frac{55.2620}{25.3284}
= 1.65311\times10^{-23}\ \mathrm{m^{3}},$$

$$d^{\text{geo}} = (6\times1.65311\times10^{-23}/\pi)^{1/3}
= 3.16059\times10^{-8}\ \mathrm{m} = 31.606\ \mathrm{nm},$$

$$\frac{d^{\text{geo}}}{d^{\text{lab}}}
= \frac{31.606}{24.368} = 1.2970.$$

Raising the observation time from $100\ \mathrm{s}$ to $10^{15}\ \mathrm{s}$
($10^{13}$ times longer) raises the blocking diameter by only 29.7%, because the
time enters logarithmically. **That is the entire justification for treating
magnetic blocking as a sharp, measurable threshold — and the entire size of the
extrapolation error if the log argument is wrong.**

---

## ★6 — Which material controls the anomaly?

Ambient field at which the induced magnetisation equals $J_r = 5\
\mathrm{A\,m^{-1}}$, with $\kappa = 0.03$:

$$H^{*} = \frac{J_r}{\kappa} = \frac{5}{0.03} = 166.667\ \mathrm{A\,m^{-1}},
\qquad B^{*} = 209.440\ \mu\mathrm{T} = 209440\ \mathrm{nT}.$$

Note that **the answer is the same for both materials**: $H_{cr}/H_c$ and
$J_{rs}/J_s$ describe the *remanence's* stability and efficiency, not the
susceptibility, so they do not enter this particular comparison. The relevant
statement is:

- If the rock carries $J_r = 5\ \mathrm{A\,m^{-1}}$ in a 50000 nT ambient
  ($H = 39.79\ \mathrm{A\,m^{-1}}$, $\kappa H = 1.194\ \mathrm{A\,m^{-1}}$), then
  $Q = 4.19$ and the anomaly is remanence controlled.
- The *material with the high $J_{rs}/J_s$ and high $H_{cr}/H_c$* is the one whose
  remanence is more likely to survive to the present day: a fine, single-domain
  assemblage retains $J_r$ through geological time, while a coarse assemblage's
  $J_r$ decays viscously. So the discrimination is about whether $J_r$ is still
  there, not about the ratio of forces.

**Conclusion.** The material with $(H_{cr}/H_c, J_{rs}/J_s) = (2.5, 0.90)$ is the
one expected to show a *stable* remanence-controlled anomaly; the other may show
$Q > 1$ in the laboratory and none in the field.

---

## ★7 — Thermal versus chemical remanence (specification)

**Measurements, in order.**

1. **Stepwise thermal demagnetisation** of a pilot specimen from room temperature
   to the highest temperature that does not change the sample, in a
   magnetically shielded space, measuring the direction and intensity after each
   step and monitoring susceptibility after every step.
2. **Stepwise alternating-field demagnetisation** on a sister specimen, to give an
   independent coercivity spectrum.
3. **Low-temperature treatment** (cooling in zero field to a low temperature and
   warming in zero field) on a third specimen, which moves the remanence of some
   carriers and not others.
4. **Susceptibility versus temperature** on a fourth specimen, repeated over two
   cycles, to detect alteration (a change between the cycles invalidates the
   heating experiment).

**Diagnostic.** A **thermal** remanence is acquired while cooling through a
blocking temperature, so its unblocking spectrum is the mirror image of the
blocking spectrum and it is destroyed by heating without any change in
susceptibility. A **chemical** remanence is acquired as new grains grow at a
temperature below their blocking temperature, so its unblocking temperatures bear
no simple relation to the cooling history and it typically coexists with growth
of new susceptibility.

**How the experiment can mislead.** Heating creates and destroys magnetic
minerals. A pTRM acquired during the experiment (by cooling in the residual
laboratory field) or new oxidation products can produce a "component" that is an
artefact of the measurement, and it will have a plausible unblocking spectrum. The
two-cycle susceptibility check and a shielded furnace are the standard guards; if
they fail, the experiment is inconclusive, not merely noisy.

---

## ★8 — Two mixtures with the same bulk ratio

Let phase A have $(J_{rs}/J_s)_A = 0.9$, $H_{c,A} = 5\times10^{4}\
\mathrm{A\,m^{-1}}$ and phase B have $(J_{rs}/J_s)_B = 0.1$,
$H_{c,B} = 5\times10^{3}\ \mathrm{A\,m^{-1}}$. Write $f$ for the fraction of A.
The bulk saturation remanence and saturation magnetisation are

$$J_{rs} = f\,J_{s,A}(0.9) + (1-f)\,J_{s,B}(0.1), \qquad
J_s = f\,J_{s,A} + (1-f)\,J_{s,B}.$$

Set $(J_{rs}/J_s)_{\text{bulk}} = 0.5$:

$$\frac{0.9fJ_{s,A}+0.1(1-f)J_{s,B}}{fJ_{s,A}+(1-f)J_{s,B}} = 0.5
\;\Longrightarrow\;
0.9fJ_{s,A}+0.1(1-f)J_{s,B} = 0.5fJ_{s,A}+0.5(1-f)J_{s,B}.$$

Rearranging:

$$0.4\,fJ_{s,A} = 0.4(1-f)J_{s,B}
\;\Longrightarrow\;
fJ_{s,A} = (1-f)J_{s,B}
\;\Longrightarrow\;
f = \frac{J_{s,B}}{J_{s,A}+J_{s,B}}.$$

So the bulk ratio 0.5 is achieved **whenever the two phases contribute equally to
$J_s$**, whatever the individual $J_s$ values are: $f = 0.9$ if
$J_{s,A} = 0.11J_{s,B}$, or $f = 0.5$ if the two saturations are equal, or
$f = 0.01$ if $J_{s,A} = 99J_{s,B}$. Infinitely many mixtures give the same bulk
ratio.

**Implication.** A bulk hysteresis ratio is a *constraint* on the mixture, not an
identification. Additional independent information — the shape of the
acquisition curve, the unblocking spectrum, a measured $H_c$ that is not a
weighted mean because of the non-linear mixing — is needed to break the
degeneracy, and even then the solution is a family unless the number of phases is
assumed. This is the mixture version of the non-uniqueness that
[08-01-03](../03-spherical-harmonic-magnetic.md) §7.1 exhibits for potential fields.
