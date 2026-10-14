# Solutions — 12-02-01 Mantle Composition and Peridotite Models

Worked solutions for
[01-mantle-composition-exercises.md](./01-mantle-composition-exercises.md). The
lesson is
[01 Mantle Composition and Peridotite Models](../01-mantle-composition.md). All
models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — The aggregate density, and the one exact step

$$\rho = 0.62(3.24) + 0.20(3.22) + 0.10(3.29) + 0.08(3.60)
= 2.0088 + 0.6440 + 0.3290 + 0.2880 = 3.2698\ \mathrm{g\,cm^{-3}}.$$

The **density step is exact** given the modes and the mineral densities: mass and
volume both add, so no averaging theory is involved. Every subsequent step — the
moduli, and therefore the velocities — is a model, because the elastic response of a
mixture depends on the *geometry* of the phases, which seismology cannot measure.
This is why a mineralogical interpretation of a velocity carries a mixing-model
uncertainty that a mineralogical interpretation of a *density* does not.

### ★2 — The three averages and their spread

$$G_V = 0.62(82) + 0.20(77) + 0.10(67) + 0.08(94)
= 50.84 + 15.40 + 6.70 + 7.52 = 80.46\ \mathrm{GPa},$$
$$\frac{1}{G_R} = \frac{0.62}{82} + \frac{0.20}{77} + \frac{0.10}{67}
+ \frac{0.08}{94}
= 7.5610 + 2.5974 + 1.4925 + 0.8511 = 12.5020\ \mathrm{GPa^{-1}},$$
$$G_R = 79.99\ \mathrm{GPa}, \qquad G_\text{Hill} = 80.22\ \mathrm{GPa}.$$

Velocities with $\rho = 3.2698$:

| average | $G$ (GPa) | $v_s$ (km s$^{-1}$) |
|---|---|---|
| Voigt | 80.46 | 4.9605 |
| Hill | 80.22 | 4.9533 |
| Reuss | 79.99 | 4.9460 |

Spread: $(4.9605 - 4.9460)/4.9533 = 0.29\ \%$. Note it is *smaller* than the spread
in $G$ itself (0.59 %) because $v_s \propto \sqrt{G}$. Half a per cent in shear
modulus is a third of a per cent in $v_s$ — worth remembering when comparing a
mixing-model uncertainty with a seismic one.

### ★3 — Velocities and Poisson's ratio

$$v_p = \sqrt{\frac{130 + \tfrac43(80)}{3.30}}
= \sqrt{\frac{236.67}{3.30}} = \sqrt{71.717} = 8.469\ \mathrm{km\,s^{-1}},$$
$$v_s = \sqrt{\frac{80}{3.30}} = \sqrt{24.242} = 4.924\ \mathrm{km\,s^{-1}},$$
$$\frac{v_p}{v_s} = 1.7200,\qquad
\nu = \frac{v_p^2 - 2v_s^2}{2\left(v_p^2-v_s^2\right)}
= \frac{71.72 - 48.48}{2(71.72-24.24)} = \frac{23.24}{95.03} = 0.2447.$$

(Using squared velocities in km$^2$ s$^{-2}$: $v_p^2 = 71.72$, $v_s^2 = 24.24$.) A
Poisson's ratio of 0.245 is the low end of the mantle range — consistent with a
pyroxene- or garnet-rich, or a relatively dry, assemblage.

---

## ★★ Applied

### ★★4 — A violated ordering, and what it means

The reported values give Reuss = 130.2, HS⁻ = 128.4, Hill = 129.0, Voigt = 127.8.
The correct ordering for any mixture is

$$\text{Reuss} \;\le\; \text{HS}^- \;\le\; \text{Hill} \;\le\; \text{HS}^+ \;\le\;
\text{Voigt}.$$

Here Voigt (127.8) < Reuss (130.2), which is impossible: uniform strain can never be
*softer* than uniform stress. So at least one of the two must be miscomputed, and
since Hill = 129.0 lies between them, the mean is internally consistent with neither
extreme. The most likely error is a **sign or inversion error in the Reuss sum**:
the Reuss average requires $\left(\sum f_i/K_i\right)^{-1}$, and forgetting the
inversion (i.e. reporting the sum instead) gives a number in entirely the wrong
range. The second most likely is that Voigt and Reuss were computed for *different*
mode vectors — a classic copy-paste error in a script with several aggregates.

**The correct ordering** for the reported numbers cannot be determined from the list
alone, but the fix is to recompute both from the same modes and check that
Voigt ≥ Hill ≥ Reuss; if that fails, the code is wrong, because it cannot fail
mathematically for positive moduli and fractions summing to one.

### ★★5 — Two composition changes and their density signatures

**(a) Moving 0.05 of the mode from garnet to olivine** (so olivine 0.62, garnet
0.03), from the demonstration's grid:

$$\Delta\rho = -0.55\ \%\ (\rho: 3.2698 \to 3.2518), \qquad
\Delta v_s = -0.066\ \%\ (4.9533 \to 4.9500).$$

The velocity change is tiny because olivine and garnet have similar shear moduli in
this parameter set ($G = 82$ against 94 GPa) while the *density* difference is large
(3.24 against 3.60). So this change is an almost pure density change.

**(b) Lowering Mg# by 0.03** applies the chosen Fe slopes to every mineral:

$$\Delta\rho = +0.096\ \%\ (3.2698 \to 3.2729), \qquad
\Delta v_s = -0.145\ \%\ (4.9533 \to 4.9460).$$

**Signs.** Both changes lower $v_s$, but (a) lowers the density while (b) raises it.
A **hot anomaly** lowers $v_s$ *and* lowers $\rho$, so it mimics (a) in sign, not (b).
The arithmetic check: $+250$ K gives
$\mathrm{d}\ln v_s = -1.2\times10^{-5} \times 250 = -0.30\ \%$ and
$\mathrm{d}\ln\rho = -\alpha\Delta T = -2.5\times10^{-5}\times250 = -0.63\ \%$ — a
much larger density drop than (a)'s $0.55\ \%$ for a comparable velocity change. So
the lever is not just the sign but the *ratio* $|\mathrm{d}\ln\rho /
\mathrm{d}\ln v_s|$: about 2.5 for a thermal anomaly, 8.3 for change (a) and 0.66 for
change (b), all at these chosen sensitivities. Measuring that ratio is what a joint
seismic–geodetic inversion does.

### ★★6 — Do the two compositions differ in density?

$$\Delta\rho = \Delta f_\text{ol}\left(-0.131\right)
+ \Delta\text{Mg\#}\left(-0.100\right)
= (0.12)(-0.131) + (-0.05)(-0.100) = -0.01572 + 0.00500
= -0.0107\ \mathrm{g\,cm^{-3}}.$$

As a fraction of $\rho \approx 3.27$: **−0.33 %**. A density measurement good to
0.2 % therefore separates them with a margin of about 1.7σ, whereas a 0.5 %
measurement does not separate them at all. This is the arithmetic behind the
lesson's Section 5 result: the *same* velocity data admit compositions differing by
0.33 % in density, and only a density better than that closes the ridge. It also sets
the requirement on the density: **it must be better than the ridge width, not better
than the velocity uncertainty.**

### ★★7 — Thermal or compositional?

**Test the thermal hypothesis first.** If the $-0.30\ \%$ in $v_s$ were thermal:

$$\Delta T = \frac{-0.30\ \%}{-1.2\times10^{-5}\ \mathrm{K^{-1}}}
= \frac{-0.0030}{-1.2\times10^{-5}} = +250\ \mathrm{K}.$$

That predicts a density change of

$$\mathrm{d}\ln\rho = -\alpha\,\Delta T = -2.5\times10^{-5} \times 250
= -0.63\ \%,$$

but the measured density change is $+0.05\ \%$. The thermal hypothesis is therefore
**excluded by a factor of about 12 in density** — the velocity could be thermal, but
the density cannot be.

**Now test the compositional hypothesis.** An Fe-rich (more fertile) anomaly lowers
$v_s$ and *raises* $\rho$, which matches the observed signs. Sizing it: from the
chosen slopes, $+0.05\ \%$ in density corresponds to
$\Delta\text{Mg\#} = -0.05/3.2 = -0.0156$ (per unit Mg#, $\mathrm{d}\ln\rho =
+0.032$), which predicts
$\mathrm{d}\ln v_s = -0.049 \times 0.0156 = -0.077\ \%$ — only a quarter of the
observed $-0.30\ \%$. So the anomaly is *not* a pure Fe-content change either: it
needs a roughly four-fold additional velocity reduction at constant density, which is
what a mode change (more garnet, less olivine) provides — from ★★5(a), a mode change
lowers $v_s$ slightly and lowers the density, so combined with the Fe change (which
raises it) the two can cancel in density while adding in velocity.

**The assumption the decision rests on** is the pair of sensitivities themselves:
$\partial\ln v_s/\partial T$ and $\alpha$ are *chosen* values here. If the true
thermal sensitivity were four times larger (a wider range is defensible for real
mantle minerals, especially when anelastic effects are included), the thermal
hypothesis would need only 62 K and would predict a −0.16 % density change — still
the wrong sign but only 3× off. **The discrimination is therefore quantitative, not
qualitative: the sign is decisive, the magnitude is only as good as the
sensitivities.**

---

## ★★★ Research-oriented

### ★★★8 — Separating thermal from compositional at 1500 km depth

**Observables, in order of expected discriminating power.**

1. **Density.** The primary discriminator, because thermal and compositional
   anomalies have *opposite* density signatures at fixed velocity (Section 6 of the
   lesson). At 1500 km depth the density must come from an inversion that combines
   normal modes, tidal and nutation parameters, and the geoid — i.e. from the
   long-wavelength part of the seismic-plus-geodetic data set, not from body waves.
   Practical resolution: about 0.3–0.5 % at degree 2–6, which is marginal against the
   0.33 % ridge width computed in ★★6. **This is the weakest link**, and any claim
   that separates thermal from compositional at these depths rests on it.
2. **$v_s$ and $v_p$, jointly.** The ratio $v_p/v_s$ (or equivalently
   $\mathrm{d}\ln v_s$ against $\mathrm{d}\ln v_p$) responds differently to
   temperature and to Fe content, so it carries compositional information *without* a
   density. The discrimination is weaker than the density test but more reliably
   measured: a 0.5 % $v_p$ and 0.5 % $v_s$ determination gives a $v_p/v_s$
   constraint with a few tenths of a per cent precision over large regions.
3. **Attenuation.** Temperature and Fe content affect attenuation differently — hot
   material attenuates more strongly for a given velocity — so $Q$ provides an
   independent axis. At 1500 km depth $Q$ is poorly resolved, which is why this is a
   supporting rather than a primary observable.
4. **Anisotropy.** The strength and the orientation of anisotropy are affected by
   deformation and by phase assemblage; a strong anisotropy is evidence for a
   mechanism (lattice-preferred orientation) that a purely thermal interpretation
   does not require.

**Forward model.** A joint inversion with the parameter vector
$(\Delta T, \Delta\text{Mg\#}, \Delta f_\text{phase}, \Delta Q)$ in each cell, using
sensitivities exactly like the demonstration's, and *with the mixing-model bounds of
Section 3 carried into the forward calculation* — otherwise the mixing uncertainty
(0.3 % in $v_s$) is mistaken for resolvable structure.

**Expected trade-offs.** $(\Delta T, \Delta\text{Mg\#})$ is the dominant one: they
enter $v_s$ with the same sign, so a ridge again. The ridge is cut by the density (or
by $v_p/v_s$), exactly as the composition ridge of the lesson's Section 5 is cut.
A second trade-off is between $\Delta f_\text{phase}$ and $\Delta\text{Mg\#}$,
because both change density and velocity in correlated ways (★★5).

**Quantitative prediction.** With $v_s$ known to 0.5 %, $v_p$ to 0.5 % and $\rho$ to
0.4 % (optimistic), the temperature is determined to about

$$\sigma_T \approx \frac{0.004}{\left|\partial\ln v_s/\partial T\right|}
= \frac{0.004}{1.2\times10^{-5}} \approx 330\ \mathrm{K}$$

if the density constraint is what limits it — i.e. a factor-of-a-few determination
of $\Delta T$, not a precision measurement. Quoting a temperature to ±100 K at
1500 km depth requires both a better density and an explicit statement of the mixing
model used to convert composition to density.

### ★★★9 — The incremental HS construction

**Two phases.** Take phase 1 as the host with fraction $f_1$ and phase 2 as the
inclusion with fraction $f_2 = 0.4$, with $K_1 = 129$, $G_1 = 82$, $K_2 = 175$,
$G_2 = 94$ GPa (olivine in garnet's presence, or the reverse depending on which bound
is wanted). Because phase 2 is stiffer, this is the lower-bound configuration and the
formula

$$K = K_1 + \frac{f_2}{\dfrac{1}{K_2-K_1} + \dfrac{1-f_2}{K_1 + \frac43 G_1}}$$

applies with $f_2$ *already relative to the current composite*. For two phases the
relative fraction is the absolute fraction, so the incremental scheme and the
closed form coincide exactly — which is the point of the exercise: the construction
must reproduce the known answer before it is trusted for three phases.

Numerically: $K = 129 + 0.4/[1/46 + 0.6/238.33] = 129 + 0.4/(0.021739 + 0.002517) =
129 + 16.49 = 145.49$ GPa. The Voigt and Reuss values for the same pair are
$K_V = 0.6(129) + 0.4(175) = 147.4$ and $K_R = 1/(0.6/129+0.4/175) = 143.4$ GPa.
Since $K_R = 143.4 \le 145.49 \le K_V = 147.4$, the value lies inside the bracket as
required, and the ordering test passes.

**Three phases.** Add a third phase with absolute fraction $f_3$. The incremental
recipe: peel phases in increasing stiffness order, starting with the softest as the
"host" composite and adding each subsequent phase with the fraction *relative to what
remains*, i.e. $f_i^\text{rel} = f_i/(1-\sum_{j<i}f_j)$, applying the two-phase
formula at each step. With $f_1 = 0.5$, $f_2 = 0.3$, $f_3 = 0.2$ (moduli 105, 129,
175 GPa): step 1 gives $f_2^\text{rel} = 0.3/0.5 = 0.6$;
step 2 gives $f_3^\text{rel} = 0.2/0.2 = 1.0$. The final step with a relative
fraction of 1.0 makes the composite *equal* to the last phase's modulus — the
degeneracy noted in the lesson: the recursion's answer converges to the stiffest
phase as the shell thicknesses shrink. **That is the diagnostic**: a correct
incremental implementation must track the *absolute* fraction remaining and stop
adding when the shell would be a full sphere; the widely published algorithm
therefore uses the absolute fractions of the remaining phases rather than the naive
relative ones, and the exercise's real content is discovering that the bookkeeping,
not the formula, is the difficulty. The practical route for three or more phases is
the closed-form pair applied to a *collapsed* matrix (as in the lesson) or the
variational formulation of 05-04-02.

### ★★★10 — Pressure and temperature corrections

**Pressure.** With a lithostatic gradient of 0.033 GPa km$^{-1}$, 200 km depth
corresponds to 6.60 GPa. At a chosen $\mathrm{d}\ln v_p/\mathrm{d}P = 0.6\ \%
\mathrm{GPa^{-1}}$:

$$\Delta\ln v_p\big|_P = +0.6 \times 6.60 = +3.96\ \%.$$

**Temperature.** With $\partial\ln v_s/\partial T = -1.2\times10^{-5}$ K$^{-1}$ and
a 1300 K difference between ambient and 200 km:

$$\Delta\ln v_s\big|_T = -1.2\times10^{-5} \times 1300 = -1.56\ \%.$$

**Do they add or cancel?** They **cancel**: compression stiffens, heating softens,
and here the net is $+3.96 - 1.56 = +2.40\ \%$. This is not a coincidence — it is the
same competition that makes mantle velocities so nearly flat with depth over the
upper few hundred kilometres.

**Comparison with the compositional signal.** The compositional changes of ★★5 move
$v_s$ by **0.07–0.15 %**. The *net* $P$–$T$ correction is 2.40 %, i.e. **16 to 34
times larger**, and even the two corrections individually (1.6 % and 4.0 %) dwarf the
compositional signal by an order of magnitude. Two conclusions follow, and they are
the operational content of this exercise:

1. **An ambient-condition mineral velocity cannot be compared with a seismic
   velocity at depth** without the $P$–$T$ correction; the correction exceeds the
   quantity being measured.
2. **The corrections must be applied together.** If only the pressure correction is
   applied, velocities come out ~1.6 % too high, which would be interpreted as a
   compositional difference of ten times the size of the real one. Because the two
   corrections partly cancel, the *error in the net correction* is what propagates
   into the composition, and an uncertainty of 10 % in either coefficient leaves a
   0.4 % residual — still several times the compositional signal.

The honest way to report a mineralogical interpretation of a seismic velocity is
therefore to state the equation of state and the thermal model used to bring the
mineral data to the seismic conditions, not just the mineral data.

---

## Mastery checkpoint — worked version

> Modes 0.62 / 0.20 / 0.10 / 0.08 with $\rho = (3.24, 3.22, 3.29, 3.60)$ and
> $G = (82, 77, 67, 94)$ GPa. Reported: $v_s = 4.90\ \mathrm{km\,s^{-1}}$,
> $\rho$ 1 % higher.

**(a) Density and moduli.**

$$\rho = 0.62(3.24)+0.20(3.22)+0.10(3.29)+0.08(3.60) = 3.2698\
\mathrm{g\,cm^{-3}},$$
$$G_V = 0.62(82)+0.20(77)+0.10(67)+0.08(94) = 80.46\ \mathrm{GPa},$$
$$G_R = \left(\frac{0.62}{82}+\frac{0.20}{77}+\frac{0.10}{67}
+\frac{0.08}{94}\right)^{-1} = \left(12.5020\ \mathrm{GPa^{-1}}\right)^{-1}
= 79.99\ \mathrm{GPa},$$
$$G_\text{Hill} = 80.22\ \mathrm{GPa}.$$

**(b) Shear velocity.**

$$v_s = \sqrt{\frac{80.22}{3.2698}} = \sqrt{24.533} = 4.953\ \mathrm{km\,s^{-1}}.$$

**(c) Can one Fe change do it?** The reported velocity is
$\mathrm{d}\ln v_s = \ln(4.90/4.953) = -1.08\ \%$, and the reported density is
$\mathrm{d}\ln\rho = +1.00\ \%$.

*Single-Fe test:* to produce the density, $|\Delta\text{Mg\#}| = 0.0100/0.032 =
0.3125$, which predicts $\mathrm{d}\ln v_s = -0.049 \times 0.3125 = -1.53\ \%$ —
considerably *more* velocity drop than the reported $-1.08\ \%$. Conversely, to
produce the velocity, $|\Delta\text{Mg\#}| = 0.0108/0.049 = 0.2204$, which predicts
$\mathrm{d}\ln\rho = +0.032 \times 0.2204 = +0.71\ \%$ — less than the reported
+1.00 %. **So no single Fe-content change explains both**: the observed ratio
$|\mathrm{d}\ln v_s|/\mathrm{d}\ln\rho = 1.08$ is *smaller* than the Fe ratio
$0.049/0.032 = 1.53$, so a second mechanism with a smaller ratio is required.

*Two-parameter solution.* A mode change (less olivine) has ratio
$0.039/0.040 = 0.98$, so a combination can reach 1.08. Solve

$$0.032\,x + 0.040\,y = 0.0100 \quad (\text{density}),$$
$$0.049\,x + 0.039\,y = 0.0108 \quad (\text{velocity}),$$

with $x = |\Delta\text{Mg\#}|$ and $y = -\Delta f_\text{ol}$. From the first,
$x = 0.3125 - 1.25y$; substituting,

$$0.049\left(0.3125-1.25y\right) + 0.039y = 0.0108
\;\Longrightarrow\; y = 0.200, \quad x = 0.0625 .$$

**Answer:** $\Delta\text{Mg\#} = -0.063$ and $\Delta f_\text{ol} = -0.20$ — a more
Fe-rich, more pyroxene-rich (more fertile) rock, with the density check
$0.032(0.0625) + 0.040(0.200) = 0.0100$ ✓. Both numbers are petrologically
plausible, which is the point: a joint velocity–density constraint *determines* a
two-parameter composition where velocity alone left a ridge.

**(d) The measurement that would tighten it most.** An independent density to better
than 0.2 % (from normal modes, satellite gravity, or the moment of inertia), because
the density is what cuts the composition ridge: the velocity pair alone admits
$f_\text{ol}$ from 0.38 to 0.85 in the demonstration's grid, while velocity plus a
0.2 % density narrows it to 0.49–0.75. The second most valuable measurement is
$v_p/v_s$ at comparable precision, because it constrains the composition without
needing a density at all.
