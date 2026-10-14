# Solutions — 02-07-07 Magnetisation, Susceptibility and Magnetic Materials

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Constants: $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A²,
$R_\oplus = 6.371\times10^{6}$ m (mean radius, nominal),
$H = 50\ \mu\mathrm T/\mu_0 = 39.7887$ A/m for the ambient field used below.

---

## ★1 — The three fields

**(a)** $H = 50\times10^{-6}/1.2566\times10^{-6} = 39.7887$ A/m. Units:
$[\mathbf B] = \mathrm T = \mathrm{kg\,s^{-2}A^{-1}}$,
$[\mathbf H] = [\mathbf M] = \mathrm{A/m}$.

**(b)** $M = \chi H$ and $B = \mu_0(1+\chi)H$, so the anomaly is simply
$\chi B_{\text{ambient}}$ in the linear regime:

| $\chi$ | $M$ (A/m) | $B$ (µT) | anomaly (nT) | $\mu_r$ |
|---|---|---|---|---|
| $10^{-3}$ | 0.0398 | 50.05 | 50.0 | 1.001 |
| $10^{-2}$ | 0.3979 | 50.50 | 500.0 | 1.010 |
| $10^{-1}$ | 3.9789 | 55.00 | 5000.0 | 1.100 |

These are exactly the demo's rows (it lists $10^{-4}$, $10^{-3}$, $10^{-2}$,
$10^{-1}$, 1 and $-10^{-5}$).

**(c)** $\mu_r = 1+\chi$: 1.001, 1.010, 1.100.

**(d)** Because the anomaly is a *relative* perturbation: 500 nT is 1 % of a 50 000
nT field but 100 % of a 500 nT field, and a survey's ability to see it depends on
the ambient field and on the noise, not on the anomaly alone. $\mathbf B$ and
$\mathbf H$ cannot be added because they have different dimensions; the relation
between them is the constitutive relation $\mathbf B = \mu_0(\mathbf H+\mathbf M)$,
not a unit conversion.

---

## ★2 — Curie depth

**(a)** $z_C = (580-10)/\text{gradient}$: 38.0 km at 15 °C/km; 22.8 km at
25 °C/km; 14.25 km at 40 °C/km — the demo's table.

**(b)** Assumptions: (i) the Curie temperature is 580 °C *for the actual magnetic
mineral assemblage*, whereas titanomagnetite in a basalt has a lower value and
hematite a higher one; (ii) the geotherm is linear; (iii) the surface temperature is
10 °C; (iv) magnetic minerals are present throughout the interval. None of the four
is exact, and (i) and (ii) are the weakest.

**(c)** Below that depth the rock is above the Curie temperature, so no spontaneous
magnetisation can exist and the rock contributes nothing to a magnetic anomaly. The
observable consequence: long-wavelength magnetic anomalies must originate in the
magnetic crust *above* $z_C$, so the depth extent of any anomaly source is bounded
by it — and if the anomaly is very long-wavelength, the *bottom* of the source
layer is the dominant control, which is why Curie-depth estimation works at all.

**(d)** It is an output of a model whose inputs are assumed. The test is a direct
thermal and magnetic measurement at depth — a deep borehole with a temperature log
and a susceptibility/Curie-temperature determination on core — or a heat-flow
measurement that independently fixes the geotherm. Both are expensive and rare,
which is exactly why Curie-depth estimates are reported with wide uncertainty and
why they are used as a reconnaissance rather than a definitive tool.

---

## ★3 — Demagnetising factors

**(a)** $\chi_{\text{eff}} = \chi/(1+N\chi)$ with $\chi = 0.05$: $N = 0$ →
0.050 00; $N = 1/3$ → 0.049 18; $N = 1$ → 0.047 62. For a weakly magnetic rock the
correction is under 5 %.

**(b)** $\chi = 5$: $N = 0$ → 5.000; $N = 1/3$ → $5/(1+1.667) = 1.875$;
$N = 1$ → 2.500. Now the correction is a factor of 2.7 — the demagnetising field
dominates the applied field.

**(c)** As $\chi\to\infty$, $\chi_{\text{eff}}\to1/N$: 3 for a sphere, 1 for a thin
sheet, unbounded for a needle ($N = 0$). Proof: divide numerator and denominator by
$\chi$: $\chi_{\text{eff}} = 1/(1/\chi + N)\to1/N$.

**(d)** Because a rock with $\chi = 5$ (SI) has enough magnetite for the induced
field it produces to be comparable with the applied field, so the body's own field
materially reduces the internal field that drives the magnetisation. In a sediment
with $\chi = 10^{-4}$ the induced field is five orders of magnitude below the
ambient field, so the internal field is the ambient field to within a part in
$10^{4}$ and $N$ is irrelevant — which is why the demagnetising factor is
negligible for sediment-hosted palaeomagnetism and essential for magnetite ore
bodies.

---

## ★4 — Induced versus remanent

**(a)** $M_i = \chi H = 0.05\times39.7887 = 1.989$ A/m.

**(b)** $Q = M_r/M_i = 5/1.989 = 2.51$ — remanence-dominated.

**(c)** $M_i = 10^{-4}\times39.7887 = 3.98\times10^{-3}$ A/m, so
$Q = 10^{-3}/3.98\times10^{-3} = 0.25$ — induced-dominated.

**(d)** For the basalt, $Q>1$ means the anomaly records the field direction at the
time of cooling, i.e. geological history, and that an induced-only interpretation
will be systematically wrong. For the sediment, $Q<1$ means the anomaly maps the
present field and hence the distribution of magnetic mineral content — i.e.
geology and structure. Both values are for *nominal* parameters; the real ratio is
determined by measuring susceptibility and remanence in the laboratory, which is
the standard rock-magnetic procedure.

---

## ★5 — Dipole anomalies

**(a)** $m = MV = 1\times10^{9}$ A m² (1 km³ = $10^{9}$ m³). Directly above:

$$B_z = \frac{\mu_0\,2m}{4\pi d^3}
= \frac{(1.2566\times10^{-6})(2\times10^{9})}{4\pi(2000)^3}
= 2.500\times10^{-8}\ \mathrm T = 25.0\ \mathrm{nT} .$$

**(b)** Inverting, $m = \frac{4\pi d^3B}{2\mu_0}
= \frac{4\pi(3000)^3(100\times10^{-9})}{2(1.2566\times10^{-6})}
= 1.350\times10^{10}$ A m².

**(c)** At $M = 1$ A/m that is a volume of $1.35\times10^{10}$ m³
= **13.5 km³**, i.e. a cube about 2.4 km on a side.

**(d)** $B\propto d^{-3}$, so the same body at 4 km gives $25/8 = 3.1$ nT instead of
25 nT. Because amplitude and depth trade off so steeply — and because the *shape* of
the anomaly also changes with depth — magnetic depth estimation from a single
profile is notoriously non-unique, and it is the reason aeromagnetic interpretation
uses the anomaly *wavelength* (which is depth-controlled) as much as the amplitude
(which is not).

---

## ★6 — SI and cgs susceptibility

**(a)** SI: $\mathbf B = \mu_0(\mathbf H+\mathbf M) = \mu_0(1+\chi_{\text{SI}})\mathbf H$.
cgs: $\mathbf B = \mathbf H + 4\pi\mathbf M = (1+4\pi\chi_{\text{cgs}})\mathbf H$ in
gauss/oersted. Matching the physics term by term, the magnetisation term is
$\mu_0\chi_{\text{SI}}H$ in one system and $4\pi\chi_{\text{cgs}}H$ in the other
(with $\mathbf B$ in tesla versus gauss and the appropriate unit factors), which
gives $\chi_{\text{SI}} = 4\pi\chi_{\text{cgs}}$ — the practical rule, and the
reason a cgs table's "magnetic" threshold of $\chi_{\text{cgs}} = 1$ is
$\chi_{\text{SI}} = 12.6$.

**(b)** $4\pi\times0.001 = 0.012\,57$; $4\pi\times0.01 = 0.125\,66$;
$4\pi\times1 = 12.566$.

**(c)** In a 50 µT field ($H = 39.7887$ A/m):

| $\chi_{\text{cgs}}$ | $\chi_{\text{SI}}$ | $M_i$ (A/m) | anomaly (nT) | $\mu_r$ |
|---|---|---|---|---|
| 0.001 | 0.01257 | 0.500 | 628.3 | 1.0126 |
| 0.01 | 0.12566 | 5.000 | 6283.2 | 1.1257 |
| 1 | 12.566 | 500.0 | $6.283\times10^{5}$ | 13.57 |

**(d)** The first two are attainable by magnetite-bearing rock (the second is
strongly magnetic but plausible for a basalt or a skarn). The third is **not
attainable by any natural rock**: linear theory would give $B = 13.57\times50
= 678$ µT, and no rock can carry that (saturation magnetisation of magnetite itself
is of order $4.8\times10^{5}$ A/m, and a rock contains a few per cent of it). A
$4\pi$ slip therefore turns a plausible rock into an impossible one — a slip of
that kind is visible as an impossibility check, which is worth doing on every
susceptibility number before using it.

---

## ★7 — The core

**(a)** $m = 4\pi R^3B_{\text{eq}}/\mu_0
= 4\pi(6.371\times10^{6})^3(3.0\times10^{-5})/1.2566\times10^{-6}
= 7.758\times10^{22}$ A m².

**(b)** $V_{\text{core}} = \tfrac43\pi(3.48\times10^{6})^3 = 1.765\times10^{20}$ m³;
$M = m/V = 439.5$ A/m — the demo's numbers.

**(c)** $B_{\text{core}} = \mu_0M = (1.2566\times10^{-6})(439.5)
= 5.522\times10^{-4}$ T $= 0.552$ mT $= 552$ µT, which is 18.4 times the 30 µT
equatorial surface field.

**(d)** **Measured**: nothing about the core directly. The *surface* field, its
spatial structure and its time variation are measured. **Inferred**: that the
source is a centred dipole and that it lies in the core. **Nominal**: the equatorial
field value (30 µT), the core radius (3.48 × 10⁶ m), and the assumption that the
core is uniformly magnetised. The result is therefore entitled to claim only that
"a dipole of this moment, if produced by the core's volume, would require a mean
magnetisation of a few hundred A/m and a mean internal field of order 0.5 mT" — a
consistency statement at the factor-of-a-few level, not a measurement.

---

## ★8 — Blocking and TRM

**(a)** $(580-500)/25 = 3.2$ km: the blocking interval spans about 3 km of crust in
a 25 °C/km geotherm (for a *stationary* geotherm, which for a cooling intrusion is
itself an idealisation).

**(b)** As the rock cools through the blocking temperature range, the magnetic
grains acquire a thermal remanence that records the *direction and intensity of the
ambient field at that moment*. What is fixed — permanently, to the extent the
grains are chemically and magnetically stable — is the field direction during the
blocking interval, averaged over the interval's duration. This is the palaeomagnetic
record: a field-direction measurement, time-stamped geologically rather than
chronologically.

**(c)** A rapidly cooled lava passes through the blocking range in a short time, so
it records essentially an instantaneous field direction — good fidelity to the
field, but vulnerable to secular variation if the cooling is not fast enough, and to
lightning and weathering afterwards. A slowly cooled pluton averages the field over
a longer interval (potentially including reversals) and is vulnerable to chemical
alteration and to acquisition of secondary components (VRM, CRM). Both are used, and
the choice depends on the question: lavas for magnetostratigraphy, plutons for
long-term averages.

**(d)** The evidence is the observation that palaeomagnetic directions from rocks of
the same age on different continents fail to agree with the present field direction
and *do* agree with each other after a tectonic reconstruction, and that some rocks
carry a magnetisation antiparallel to the present field on the same continent (the
reversed polarity record). If remanence were simply induced magnetisation, all
rocks would point along the present field and the continental reconstructions would
be impossible.

---

## ★9 — Demagnetisation and non-uniqueness

**(a)** For a uniformly magnetised ellipsoid the internal field is
$\mathbf H_{\text{in}} = \mathbf H_0 - \mathbf N\mathbf M$ with
$N_x+N_y+N_z = 1$. The argument: for *any* convex
body the average of the demagnetising field over its interior is exactly
$-\mathbf M/3$ (a classical magnetostatic result, obtained by integrating
$\mathbf H_{\text{in}}\cdot\mathbf r$ over the body and using
$\nabla\cdot\mathbf H_{\text{in}} = 0$ inside plus the surface conditions).
For an ellipsoid, where $\mathbf H_{\text{in}} = \mathbf H_0-\mathbf N\mathbf M$
with $\mathbf N$ constant, that average is $\mathbf H_0 - \mathbf N\mathbf M$, so
matching the two expressions requires $\mathrm{tr}\,\mathbf N = 1$ independently
of shape. A sphere then has $N_x = N_y = N_z$ by symmetry, hence $N = 1/3$; a very
flat disc magnetised normal to its plane has $N\to1$ with
$N_x = N_y\to0$; and a long needle along its axis has $N\to0$.

**(b)** The external field is set by the *effective* magnetisation
$\mathbf M_{\text{eff}} = \chi_{\text{eff}}\mathbf H_0$ with
$\chi_{\text{eff}} = \chi/(1+N\chi)$. Different combinations of $(\chi, N)$ give the
same product, so an anomaly amplitude (which depends only on
$\mathbf M_{\text{eff}}$) cannot separate them. Only the anomaly *shape* — the
aspect ratio and depth of the source — constrains $N$, and only weakly for
deep bodies.

**(c)** Sphere with $\chi = 1$: $\chi_{\text{eff}} = 1/(1+1/3) = 0.75$. Thin sheet
with $\chi = 1$: $\chi_{\text{eff}} = 1/(1+1) = 0.5$. Ratio of effective
magnetisations (same volume, same $H_0$): $0.75/0.5 = 1.5$. At the same distance,
the anomalies differ by a factor 1.5 — a 50 % difference in an inferred
magnetisation, obtained from two bodies with *identical* mineralogy and
susceptibility.

**(d)** It is resolved by independent constraints: the geometry of the body from
the anomaly's shape and from other data (seismic horizons, drilling, gravity);
laboratory measurement of susceptibility on samples (which fixes $\chi$, leaving
$N$); and rock-magnetic determination of the remanence so that the induced term can
be separated. None of these is magnetic-anomaly data, which is the point: the
magnetic data alone are insufficient, and a report that quotes a "magnetite
percentage" from an anomaly amplitude without stating the assumed shape and the
assumed $Q$ has hidden two free parameters inside one number.

---

## ★10 — Anisotropy of magnetic susceptibility

**(a)** $M_i = \chi_{ij}H_j$, with $\chi_{ij}$ a rank-2 tensor. It is symmetric
because the induced magnetisation is a gradient of a scalar magnetic energy
density, $M_i = -\partial U/\partial H_i$ with
$U = -\tfrac12\chi_{ij}H_iH_j$; the antisymmetric part contributes nothing to the
energy and would correspond to a dissipationless gyromagnetic response that is
negligible for induced magnetisation in rocks. (Symmetry is a statement about the
*induced*, reversible part; the remanent magnetisation is not described by a
susceptibility tensor at all.)

**(b)** In principal axes $\chi_{ij} = \mathrm{diag}(k_1,k_2,k_3)$ with
$k_1\ge k_2\ge k_3$, and $P = k_1/k_3$, $U = (2k_2-k_1-k_3)/(k_1-k_3)$. $U$ is
dimensionless because numerator and denominator are both susceptibilities; and
it is bounded because $2k_2-k_1-k_3$ is largest when $k_2 = k_1$ (giving
$(k_1-k_3)/(k_1-k_3) = 1$) and smallest when $k_2 = k_3$ (giving
$-1$). So $U\in[-1,1]$, with $U>0$ a linear (prolate) fabric, $U<0$ a planar
(oblate) one, and $U = 0$ neutral.

**(c)** Mean susceptibility $= (1.20+1.15+1.00)\times10^{-3}/3 = 1.117\times10^{-3}$;
$P = 1.20/1.00 = 1.20$; $U = (2.30-2.20)/0.20 = 0.50$. A moderately anisotropic
($P = 1.2$) prolate fabric — a weak linear alignment.

**(d)** Because the anisotropy reflects the *statistical alignment* of magnetic
grains, which is produced by the same processes that align the non-magnetic
framework: depositional settling, compaction, and tectonic strain. Measuring AMS
therefore measures a petrofabric, cheaply and on the same specimen used for other
work — which is why it is a standard tool in structural geology and in sedimentology.
The two mechanisms are (i) preferred orientation of grains (shape anisotropy: an
elongate grain is easier to magnetise along its long axis) and (ii) the intrinsic
magnetocrystalline anisotropy of the mineral itself (magnetite is easy to magnetise
along its cube edges, hematite within its basal plane). The two can be separated in
favour of one or the other by comparing low-field AMS with high-field measurements,
which is routine in modern rock-magnetic work.
