# Solutions — 02-09-01 Atomic Structure and Energy Levels

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every tabulated value is named where it is used. In a report, each of them needs
a compilation and an edition; the lesson's standard is the NIST X-ray
transition-energy tables and the evaluated atomic data, confirmed at the time of
use.

---

## ★1 — Bohr radius, energy and Lyman-alpha

**(a)** With $\hbar = h/2\pi = 1.054\,571\,817 \times 10^{-34}$ J s,
$k_e = 1/(4\pi\varepsilon_0) = 8.987\,551\,79 \times 10^{9}$ N m² C⁻², $e =
1.602\,176\,634 \times 10^{-19}$ C and $m_e = 9.109\,383\,7 \times 10^{-31}$ kg:

$$a_0 = \frac{\hbar^2}{m_ek_ee^2} = 5.291\,772\,11 \times 10^{-11}\ \mathrm{m}
= 52.9177\ \mathrm{pm}.$$

The measured CODATA value is 52.9177 pm. Note which inputs were **exact** — $h$,
$e$, $\varepsilon_0$ by the SI — and which was **measured**, namely $m_e$. The
agreement to seven figures is therefore a check of the arithmetic and of the
exactness of $h$ and $e$, not of $m_e$.

**(b)** $E_1 = -\tfrac12 m_ec^2\alpha^2 = -\tfrac12(510\,998.95\ \mathrm{eV})
(7.297\,352 \times 10^{-3})^2 = -13.5983$ eV. The hartree $e^4m_e/
((4\pi\varepsilon_0)^2\hbar^2)$ evaluates to 27.2114 eV, so $E_1 = -E_h/2$. Both
routes agree, which is the dimensional check of §7.

**(c)** $E = 13.5983(1 - 1/4) = 10.1987$ eV. Then
$\lambda = 1239.841984/10.1987 = 121.568$ nm. The tabulated value is 121.567 nm,
a difference of 0.001 nm or $1.2 \times 10^{-5}$ relative. The residual is the
part of the hydrogen spectrum the model does not contain: the finite nuclear mass
is already included, and the remainder is the Lamb shift, the relativistic
correction and the finite nuclear size — of order $10^{-5}$ relative, which is
exactly the size of the discrepancy.

**(d)** $m_e$ is **measured** (CODATA). $a_0$ and $E_1$ follow from $m_e$ and
exact constants and so carry $m_e$'s uncertainty; $hc = 1239.841984$ eV nm is
**exact**, since $h$, $c$ and $e$ are exact. A calculation that quotes $a_0$ to
nine figures without saying that it inherits the uncertainty in $m_e$ has
mistaken derivation for measurement.

---

## ★2 — Hydrogen lines

**(a)** $\lambda^{-1} = R_\mathrm{H}(1/4 - 1/16) = 109\,677.58 \times 0.1875 =
20\,564.5$ cm⁻¹, so $\lambda = 486.2738$ nm in vacuum.

**(b)** $486.2738/1.000\,277 = 486.1391$ nm against a tabulated 486.133 nm — a
difference of 0.006 nm, or $1.26 \times 10^{-5}$ relative. The residual is the
dispersive index of air approximated by a single number, not a defect of the
Rydberg formula.

**(c)** The series limit is $n \to \infty$ at $n_l = 2$:
$\lambda^{-1} = R_\mathrm{H}/4 = 27\,419.4$ cm⁻¹, so $\lambda = 364.705$ nm.
Beyond this wavelength there are no further Balmer lines; the spectrum becomes
continuous. This limit is the ionisation energy of the $n = 2$ level expressed as
a wavelength, $3.3996$ eV, and it is measured as the convergence of the line
series — historically the most precise determination of the Rydberg constant
before the quantum theory existed.

**(d)** The Hα vacuum wavelength is 656.4696 nm, so $E = 1239.841984/656.4696 =
1.8887$ eV. In air the wavelength is 656.2878 nm and $hc/\lambda$ would give
1.8892 eV; the *photon* energy is set by the vacuum wavelength, and the air value
is a different (shorter) length for the same energy because light slows in air.
Mixing the two conventions is worth 0.03 per cent — invisible in most
spectroscopy and decisive when the energy is compared with an atomic level.

---

## ★3 — Levels, edges and lines

**(a)** $E_K = 13.6057\ \mathrm{eV} \times 26^2 = 9197.4$ eV $= 9.197$ keV.

**(b)** $E_{K\alpha} = \tfrac34 \times 13.6057 \times 26^2\ \mathrm{eV} =
6898.1$ eV $= 6.898$ keV.

**(c)** The Kα transition starts from the L shell, which is itself bound, so the
energy released is the K binding energy minus the L binding energy. The
difference is the L-shell binding energy — a few hundred eV for iron, several keV
for lead — and it is the reason a characteristic line always lies below its
absorption edge in energy.

**(d)** The tabulated edge is 7.112 keV against the model's 9.197 keV: the model
is 29 per cent too high, so the real atom binds its 1s electron **less** strongly
than a bare Coulomb potential would. The reason is screening: the second K
electron and the L-shell electrons reduce the effective charge seen by the 1s
electron from 26 to about 23 ($Z - \sigma$ with $\sigma \approx 3.1$). The sign
of the effect is therefore fixed by physics, and the size is what makes the
screened model a trend law rather than a prediction.

---

## ★★4 — The isotope shift

**(a)** $R_\mathrm{H} = R_\infty/(1 + m_e/m_p)$ with $m_e/m_p = 1/1836.15$ gives
109 677.583 cm⁻¹, and with $m_e/m_d = 1/3670.5$ gives 109 707.427 cm⁻¹. The
fractional shifts are $-2.721 \times 10^{-4}$ for hydrogen and $-1.362 \times
10^{-4}$ for deuterium, relative to $R_\infty$.

**(b)** Hα is at 656.2878 nm in air for hydrogen and 656.1093 nm for deuterium, a
shift of 178.53 pm. The line width of a good grating spectrograph is a few
picometres, so the shift is a resolution question of the 1930s and trivial
today.

**(c)** Tritium Hα is at 656.0499 nm, so the D–T shift is 59.38 pm — about
one-third of the H–D shift. The reason is that the reduced-mass correction
depends on $1/M$, so the difference between successive isotopes falls as the
mass rises: $1/1 - 1/2 = 0.5$ against $1/2 - 1/3 = 0.167$.

**(d)** The shift is not relativistic. It is the **finite nuclear mass**: the
electron and nucleus orbit their common centre of mass, which replaces $m_e$ by
the reduced mass $\mu = m_eM/(m_e + M)$ in every energy expression. A
relativistic effect would scale with $Z^4$ and would be larger for heavy elements
than for hydrogen, which is the opposite of what is observed.

---

## ★★5 — Moseley's law

**(a)** $\sqrt E$ = 2.5306 (Fe), 2.8369 (Cu), 8.6585 (Pb), in keV^½.

**(b)** The Fe–Pb slope is $(8.6585 - 2.5306)/(82 - 26) = 0.109\,43$
keV^½ per unit $Z$. The model's slope is
$\sqrt{0.75 \times 13.6057\ \mathrm{eV}/1000} = 0.101\,016$ keV^½. The measured
slope is 8.3 per cent above the model's.

**(c)** The screening constant must be extracted from the *binding* energies,
because the factor $\tfrac34$ belongs to the transition: for a K edge,
$\sigma = Z - \sqrt{E_\mathrm{edge}[\mathrm{keV}] \times 1000/13.6057}$. For iron,
$\sqrt{7112/13.6057} = \sqrt{522.72} = 22.863$, so $\sigma = 26 - 22.863 = 3.14$;
for lead, $\sqrt{88005/13.6057} = 80.425$, so $\sigma = 1.58$. A single straight
line through all six elements gives $\sigma = 3.32$, the demo's least-squares
value. The spread from 1.6 to 3.3 is the point of ★★★8: $\sigma$ is a fitting
parameter, not a constant of nature. Note also how easy the unit slip is here: a
$\sigma$ computed as $26 - \sqrt{7.112/13.6057}$ without converting keV to eV is
25.3, and it is a plausible-looking number that means nothing.

**(d)** Moseley's law demonstrated that the X-ray frequencies order by integer
**atomic number** rather than by atomic weight, which settled the ordering
principle of the periodic table and gave "atomic number" a physical meaning a
decade before the nucleus was understood. It does not predict absolute energies
for light elements, and it does not predict the *intensities* of the Kα and Kβ
lines at all.

---

## ★★6 — Edges and lines

**(a)** The hydrogen-like model gives 6.898 keV for $Z = 26$ (from ★3b).

**(b)** Using 7.112 keV as though it were the line energy gives an error of
$(7.112 - 6.4038)/6.4038 = 11.1$ per cent relative to the tabulated Kα₁.

**(c)** The difference between the edge and the line is the L-shell binding
energy: 7.112 − 6.404 = 0.708 keV for iron. That is the energy that must be
supplied to remove the L electron as well, and it is the reason a photon at
6.5 keV cannot remove a K electron (it is below the edge) while a photon at
6.4 keV emitted by the same atom can exist (it is the transition energy).

**(d)** The L-shell binding energy is a roughly constant number of atomic
*electrons*' worth of energy while the K energy grows as $Z^2$, so the ratio
$B_L/B_K$ falls as $Z$ rises. For iron it is 10 per cent; for lead it is a few
per cent. The consequence is that a spectroscopist's K-edge/Kα confusion is worst
for light elements, which is also where the K lines are hardest to measure,
making the error easy to commit and hard to catch.

---

## ★★★7 — Running the demo

**(a)** Hδ: model 410.17988 nm in air, tabulated 410.174 nm, difference
0.0059 nm, relative $1.43 \times 10^{-5}$ — the largest relative difference in
the table, at the shortest visible wavelength where the dispersion of air is
strongest.

**(b)** The fitted screening constant is 3.3178, from the Moseley fit. The
per-element values recovered from the tabulated K edges are 3.137 (Fe), 3.311
(Cu), 3.660 (Mo), 3.696 (Ag), 2.516 (W) and 1.575 (Pb). Largest 3.696, smallest
1.575 — a spread of a factor of 2.3 across the periodic table.

**(c)** Fitted slope 0.109308 keV^½ per unit $Z$; model slope 0.101016;
agreement to 8.21 per cent, with an rms residual in $\sqrt E$ of
$4.86 \times 10^{-2}$ keV^½, i.e. 0.95 per cent of the mean.

**(d)** The model's barium Kα energy is 32.00 keV against a commonly tabulated
value of about 32.19 keV, a difference of 0.6 per cent — the same order as the
line's own natural width and far better than any binding-energy estimate the
model can produce.

**(e)** The screened one-electron model is usable for **interpolation of
transition energies** between elements whose lines have been measured, where the
screening largely cancels, and it is not usable for **absolute binding energies**,
where the 4 to 29 per cent systematic error is larger than the quantity of
interest in any shielding calculation near an edge. A report that quotes a
binding energy from the model has not looked it up.

---

## ★★★8 — The screening constant is not constant

**(a)** $\sigma = Z - \sqrt{E[\mathrm{keV}] \times 1000/13.6057}$ gives
$\sigma = 3.137$ for iron and $\sigma = 1.575$ for lead.

**(b)** With $\sigma = 2$: Fe, $24^2 \times 0.013\,6057 = 7.837$ keV, which is
$+10.2$ per cent on the tabulated 7.112 keV; Pb, $80^2 \times 0.013\,6057 =
87.076$ keV, which is $-1.06$ per cent on the tabulated 88.005 keV. One constant
gives a 10 per cent error for iron and a 1 per cent error for lead.

**(c)** Screening is produced by electrons that spend time near the nucleus. In
a heavy atom the inner shells are contracted and the K-shell electrons see
almost the full nuclear charge; the outer electrons, which are the ones that
screen, are far outside the K shell and shield it poorly. As $Z$ rises the K
shell contracts faster than the outer shells, so the effective screening of the
K electron falls. In light atoms the K and L shells overlap substantially and the
single remaining K electron is shielded appreciably by the L electrons.

**(d)** Two things are wrong. First, the coefficient is 13.6 eV for hydrogen and
the expression $13.6Z^2$ eV omits screening entirely, so it overestimates real
K-edge energies by 4 to 30 per cent across the periodic table. Second, and worse,
$13.6Z^2$ eV is a *binding* energy while an absorption edge position is also
affected by the chemical environment and by relativity, so even with screening
included the formula is a trend rather than an energy. The correct procedure is
to look the edge up, state the compilation, and use the model only to explain the
trend.
