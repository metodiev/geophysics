# Exercises — 04-08-02 Planetary Interiors and Magnetic Fields

Attempt these **closed-book** before opening the
[solutions](./02-planetary-interiors-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Take $G = 6.6743\times10^{-11}$ m³ kg⁻¹ s⁻², $\mu_0 = 1.2566\times10^{-6}$
N A⁻², $R_\oplus = 6.371\times10^6$ m, $M_\oplus = 5.9722\times10^{24}$ kg and
$k_B = 1.380\,649\times10^{-23}$ J K⁻¹.

Problems referring to
[`../code/planetary_interiors_demo.py`](../code/planetary_interiors_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Write the three equations of hydrostatic equilibrium for a spherically
symmetric body.

(a) State which equation is geometry, which is Newton's theorem, and which is
force balance.
(b) Derive the uniform-sphere central pressure $P_\mathrm{centre}
= \tfrac23\pi G\rho^2R^2$ by integrating the equations analytically.
(c) Evaluate it for a body with an uncompressed mean density of 3934 kg m⁻³ and
a radius of $3.3895\times10^6$ m.
(d) State which of the three quantities in (c) is measured.

---

**★2.** A body has a core of radius $0.5R$ and density $2\rho_m$, surrounded by a
uniform mantle of density $\rho_m$.

(a) Compute the mass and the moment of inertia in units of $\rho_mR^3$ and
$\rho_mR^5$.
(b) Compute the moment-of-inertia factor $\alpha = C/(MR^2)$.
(c) Compare it with the uniform-sphere value of 0.4 and state what the comparison
means.
(d) State what additional measurement would be needed to determine the core
radius rather than assume it.

---

**★3.** A conducting core has $\sigma = 3\times10^5$ S m⁻¹, a flow speed of
$5\times10^{-4}$ m s⁻¹ and a length scale of $2\times10^6$ m.

(a) Compute the magnetic Reynolds number.
(b) Compute the magnetic diffusion time in seconds and in years.
(c) State what the diffusion time means physically.
(d) State the three requirements a dynamo imposes on a body.

---

**★4.** A body has an equatorial surface field of $2.5\times10^{-5}$ T and a
radius of $6.371\times10^6$ m.

(a) Compute the dipole moment using (9).
(b) Compute the magnetisation that would be required if the moment were spread
uniformly through a core of radius 3480 km.
(c) Compare the answer to (b) with the saturation magnetisation of iron, and
state why the comparison does not settle whether the field is generated.
(d) State the two arguments that do.

---

## ★★ Applied

**★★5.** Run the demo's section 1.

(a) Report the uniform-sphere central pressure from the analytic formula and from
the numerical integration, and the mean density used.
(b) Report the two-layer mass, the tabulated Earth mass and the percentage
difference, and the central pressure.
(c) Report the four rows of the profile-sensitivity table and state what they
show about the identifiability of a central pressure.
(d) Explain, in two sentences, why matching the seismological central pressure
with a two-parameter model is not a validation.

---

**★★6.** Run the demo's section 2.

(a) Report the uniform-sphere $\alpha$ and the analytic limit.
(b) Report $\alpha$ and the mass for the four two-layer density pairs.
(c) Report the geodetic value and the required core density from the inversion,
with the mass it implies.
(d) Explain what the failure of the inversion says about the model, and state
which physical feature of the real mantle is missing.

---

**★★7.** Run the demo's section 5.

(a) Report the skin depth at an 11.2-hour period for conductivities of 0.1, 1, 3
and 10 S m⁻¹.
(b) Compute the conductivity that gives a skin depth of exactly 100 km at that
period.
(c) Report the corresponding depths at a 3.55-day period and explain why the
longer period is a poorer discriminator.
(d) State what quantity an induction measurement actually determines, and what
else must be assumed to report it as a thickness.

---

## ★★★ Research-oriented

**★★★8.** The moment-of-inertia inversion of ★★6 produced one solution per core
radius, but the core radius itself was fixed from seismology. Take the density
contrast as unknown instead.

(a) Using the demo's functions (or your own integration), find the core density
that reproduces $\alpha = 0.3308$ at core radii of 2500, 3000, 3480 and 4000 km,
with the mantle at 4500 kg m⁻³.
(b) Tabulate the mass implied by each solution and compare it with the tabulated
Earth mass.
(c) State what the pattern of solutions shows about the uniqueness of the
inversion.
(d) Explain, in no more than six sentences, what additional measurement would
break the degeneracy, and why.

---

**★★★9.** A small body has a conducting liquid layer of thickness 50 km and
conductivity 1 S m⁻¹, and it orbits its parent at a distance where the external
field varies with the orbital period.

(a) Compute the skin depth at the orbital period, taking the period as 3 days.
(b) State whether the layer is thin or thick compared with the skin depth, and
what that implies for the amplitude of the induced field.
(c) Repeat for a period of 12 hours and compare the two responses.
(d) Discuss, in no more than five sentences, why a detection of an induced field
constrains the *conductance* rather than the thickness, and what additional
information would be needed to convert one into the other.
