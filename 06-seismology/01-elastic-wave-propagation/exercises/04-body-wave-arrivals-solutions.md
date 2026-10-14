# Solutions — 06-01-04 Reflected, Refracted and Converted Body Waves

> **Read after attempting the exercises.** Numbers were computed, not estimated;
> demonstration values are quoted directly.

Lesson: [04 Body-Wave Arrivals](../04-body-wave-arrivals.md).

---

## ★1 — Impedances and coefficients

$$Z_1 = \rho_1v_{p1} = 2400 \times 3000 = 7.2000\times10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$
$$Z_2 = \rho_2v_{p2} = 2600 \times 4500 = 1.1700\times10^{7}\
\mathrm{kg\,m^{-2}\,s^{-1}}.$$

Potential convention:

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1} = \frac{1.17 - 0.72}{1.17 + 0.72}
= \frac{0.45}{1.89} = +0.2380952381,$$

displacement convention: $R_u = -0.2380952381$, and

$$T = \frac{2Z_1}{Z_1 + Z_2} = \frac{1.44}{1.89} = +0.7619047619 .$$

The unit of $Z$ is a mass per unit area per unit time,
$\mathrm{kg\,m^{-2}\,s^{-1}}$ — impedance, not velocity. All three printed values
are reproduced exactly.

---

## ★2 — Energy balance

$$\frac{Z_2}{Z_1} = \frac{1.17\times10^{7}}{7.2\times10^{6}} = 1.625,$$

$$R^2 + \frac{Z_2}{Z_1}T^2 = 0.2380952381^2 + 1.625(0.7619047619^2)
= 0.05668934 + 0.94331066 = 1.00000000 .$$

The demonstration prints $0.9999999999999998$, i.e. the identity holds to machine
precision ($2.22\times10^{-16}$).

The factor $Z_2/Z_1$ appears because the energy flux carried by a wave is
proportional to **impedance** $\times$ amplitude$^2$, not to velocity
$\times$ amplitude$^2$. A displacement amplitude transmitted into a higher-impedance
medium carries more energy per unit amplitude, and the balance must account for it.
Replacing the factor by $v_1/v_2$ or by 1 is a real physical error, not a
rearrangement.

---

## ★3 — Critical angle

$$\theta_c = \arcsin\!\left(\frac{v_{p1}}{v_{p2}}\right)
= \arcsin\!\left(\frac{3000}{4500}\right) = \arcsin(0.666667)
= 41.81^\circ .$$

Beyond $\theta_c$ the transmitted P leg is **evanescent**: its vertical slowness
becomes imaginary, so $T_{pp}$ and the associated amplitude become complex. The
demonstration notes this explicitly at $45^\circ$ and $55^\circ$ ("P leg
evanescent") and prints magnitudes there.

---

## ★4 — The two wrong flux factors

With $v_1/v_2 = 3000/4500 = 0.666667$:

$$R^2 + \frac{v_1}{v_2}T^2 = 0.05668934 + 0.666667(0.58049887)
= 0.05668934 + 0.38699925 = 0.44368859 .$$

Error: $1 - 0.44368859 = 0.5563$ ✔ matches the demonstration.

Omitting the density factor:

$$R^2 + T^2 = 0.05668934 + 0.58049887 = 0.63718821 .$$

Error: $1 - 0.63718821 = 0.3628$ ✔ matches.

The ratio of the two candidate flux factors is

$$\frac{Z_2/Z_1}{v_1/v_2} = \frac{1.625}{0.666667} = 2.4375
= \frac{\rho_2}{\rho_1}\left(\frac{v_2}{v_1}\right)^{2}
= 1.083333 \times 1.5^{2} = 2.4375,$$

which the demonstration reports as
`(Z2/Z1)/(v1/v2) = 2.437500`. The discrepancy between the two candidate factors
is therefore the **density contrast times the velocity ratio squared**, not the
density contrast alone. Equivalently, dropping the density factor entirely
multiplies the flux factor by $(v_2/v_1) = 1.5$:

$$\frac{Z_2/Z_1}{1} = 1.625 = 1.083333 \times 1.5 .$$

Both comparisons carry the same lesson: the velocity ratio cannot substitute for
the impedance ratio at any density contrast other than zero, and the size of the
error is set by *both* the density and the velocity contrast.

---

## ★5 — Snell's law for the three oblique angles

Horizontal slowness:

$$p = \frac{\sin 25^\circ}{v_{p1}} = \frac{0.4226183}{3000}
= 1.4087275\times10^{-4}\ \mathrm{s\,m^{-1}} .$$

Transmitted P in medium 2:

$$\sin\theta_{p2} = p\,v_{p2} = 1.4087275\times10^{-4} \times 4500 = 0.6339274
\;\Longrightarrow\; \theta_{p2} = 39.340477^\circ ✔$$

Reflected S in medium 1 ($v_{s1} = 1732\ \mathrm{m\,s^{-1}}$):

$$\sin\theta_{s1} = 1.4087275\times10^{-4}\times 1732 = 0.2440316
\;\Longrightarrow\; \theta_{s1} = 14.122249^\circ ✔$$

Transmitted S in medium 2 ($v_{s2} = 2600\ \mathrm{m\,s^{-1}}$):

$$\sin\theta_{s2} = 1.4087275\times10^{-4}\times 2600 = 0.3662691
\;\Longrightarrow\; \theta_{s2} = 21.485710^\circ ✔$$

All three match the printed values, which confirms that the driver is Snell's law
alone: the Zoeppritz solution supplies amplitudes, never angles.

---

## ★6 — Energy partition and the critical angle

At $25^\circ$: $R_{pp} = -0.182556$, $R_{ps} = 0.173164$,
$T_{pp} = 0.810644$, $T_{ps} = -0.195646$, flux sum $1.000000$.
At $45^\circ$: $R_{pp} = -0.830438$, $R_{ps} = 0.436592$,
$T_{pp} = 1.409691$, $T_{ps} = 0.400503$, flux sum $1.000000$.

Beyond the critical angle the transmitted P leg is evanescent and carries **no net
vertical energy flux**. All the incident energy must therefore be returned by the
reflected P and the converted S, which is why $|R_{pp}|$ grows from $0.18$ to
$0.83$ and why the *displacement* amplitude $T_{pp}$ can exceed 1: with no real
propagating P wave to carry energy downward, the "transmitted" coefficient
describes an evanescent field whose amplitude is not flux-limited. The flux-sum
column staying exactly 1.000000 is the statement that the full solution still
conserves energy once the evanescent term is excluded — a stronger check than
checking the partition alone, because it would also fail if a term were dropped
that *does* carry flux.

---

## ★★★7 — The normal-incidence limit (worked derivation)

Write the four Zoeppritz equations for continuities of $u_x$, $u_z$,
$\sigma_{zz}$, $\sigma_{xz}$ at an interface with ray parameter $p$. Every
coefficient multiplying an S amplitude contains a factor $p$ or a factor
$\sin\theta_s = p\,v_s$; every coefficient multiplying a P amplitude contains a
$\cos\theta$ which tends to 1 as $p \to 0$, while the coupling terms between P and
S contain $p$ (for $u_x$) or $p^{2}$ (for the traction equations).

At $p = 0$:

- $u_x$ continuity becomes trivial for P motion ($u_x = 0$ on both sides);
- $\sigma_{xz}$ continuity likewise gives $0 = 0$;
- the two remaining equations are the P system
  $u_z^{(1)} = u_z^{(2)}$, $\sigma_{zz}^{(1)} = \sigma_{zz}^{(2)}$;
- the S amplitude columns have zero coefficient, so $R_{ps} = T_{ps} = 0$.

Solving the two-equation P system with stresses $\sigma_{zz} = Z\,\dot u_z$ gives
$R_{pp}^{\text{pot}} = (Z_2 - Z_1)/(Z_2 + Z_1)$. The demonstration confirms this
limit: at $p\to0$ it prints
$R_{pp} = +0.2380952381$, identical to the closed form, and reflected and
transmitted SV amplitudes of $0.00\times10^{0}$.

**Insensitivity to overall sign.** If every transmitted amplitude were multiplied
by $-1$, then at normal incidence $|R|$ would be unchanged (it depends on $Z_1$,
$Z_2$ only) and the energy sum would still be satisfied — only the *relative*
phase of the transmitted wave would be wrong. That is precisely why this limit
cannot certify the transmitted columns' signs.

---

## ★★★8 — Two further independent checks (design)

**Check A — independent evaluation of the boundary fields.** Assemble each side's
$u_x$, $u_z$, $\sigma_{zz}$, $\sigma_{xz}$ *directly from that side's own
potential form* and difference them across the interface without using the
coefficient table the matrix was built from. This is what the demonstration does,
and it is the check that caught the sign error. It measures physical continuity,
nothing else.

**Check B — reciprocity of the converted amplitudes.** For a planar interface,
the conversion coefficients must satisfy reciprocity relations between the
$P\to S$ and $S\to P$ problems with the appropriate impedance weighting. Shoot the
same interface twice, once from each side, and compare the computed conversion
amplitudes with the reciprocity requirement. This measures a symmetry of the
*solution*, which is independent of how the matrix was assembled.

**Which to trust more.**
Check A, because it is a direct statement of the boundary conditions and it fails
for exactly one kind of error (a wrong sign or coefficient in the matrix assembly)
with no modelling assumptions beyond those of the problem. Reciprocity is also
powerful, but it is a *consequence* of the equations and can, in principle, be
satisfied by a consistently mis-normalised but wrong solution.

---

## ★★★9 — `Pn` and the core reflections

**`Pn`.** `Pn` is the head wave along the Moho. It exists only where the Moho is a
velocity *increase* and the ray can run along it, which is a statement about the
**velocity contrast** of the model. Beyond the critical distance the head wave is
the first arrival; at short distances the direct P arrives first and the `Pn`
branch either coincides with it (as at $2^\circ$, where both are
$33.827\ \mathrm{s}$) or is not separated by the tabulated phases. At
$30^\circ$ and $60^\circ$ the demonstration's `Pn` column is blank because the
reference model's own phase list does not return `Pn` as a distinct arrival there:
the Moho-refracted leg is overtaken in the phase list by the direct/refracted
upper-mantle P.

**`PcP` and `ScS`.** These are reflections from the core–mantle boundary. A
reflection always arrives *later* than the direct phase that shares its
geometrical path, because it travels an extra leg; that is a statement about
**geometry**, and it holds at every distance. The demonstration's table confirms
it at every row: e.g. at $2^\circ$ `P` $= 33.827\ \mathrm{s}$ against
`PcP` $= 509.736\ \mathrm{s}$, and at $60^\circ$ `P` $= 606.671\ \mathrm{s}$
against `PcP` $= 652.518\ \mathrm{s}$.

The contrast is instructive: the existence of an arrival is a statement about a
contrast, while its *ordering* is a statement about geometry. A pipeline that
flags a reflection as arriving earlier than its direct phase is using the
geometric rule, which is safe; one that infers a reflector's existence from a
travel-time ordering alone is not.
