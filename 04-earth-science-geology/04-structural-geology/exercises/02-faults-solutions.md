# Solutions — 04-04-02 Fault Geometry, Kinematics and Fault Classification

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Conventions as stated in the exercises.

---

## ★1 — A normal fault

**(a)** With $\phi = 0$ and $\delta = 60^\circ$, equation (3) gives
$\mathbf{n} = (\cos 0 \sin 60^\circ, 0, \cos 60^\circ) = (0.8660, 0, 0.5000)$ —
the demo's first row of `nx`, `ny`, `nz`. The pole leans east, so the plane dips
east, as the right-hand rule requires.

**(b)** $\mathbf{d} = (\sin 0, \cos 0, 0) = (0, 1, 0)$, pointing north, which is
strike 000. $\mathbf{u} = (-\cos\phi\cos\delta, \sin\phi\cos\delta,
\sin\delta) = (-0.5, 0, 0.8660)$ — pointing west and up, which is up-dip for an
east-dipping plane. The three checks: $\mathbf{d}\cdot\mathbf{u} = 0$;
$\mathbf{u}\cdot\mathbf{n} = -0.5 \times 0.8660 + 0.8660 \times 0.5 = 0$; and
$\mathbf{d}\times\mathbf{u} = (1 \times 0.8660 - 0, 0, 0 - 1 \times (-0.5))
= (0.8660, 0, 0.5) = \mathbf{n}$. This last identity is the one that catches a
sign error, because it does not hold if $\mathbf{u}$ is replaced by its
down-dip opposite.

**(c)** $\mathbf{s} = \cos 270^\circ\,\mathbf{d} + \sin 270^\circ\,\mathbf{u} =
0 \cdot \mathbf{d} - \mathbf{u} = (0.5, 0, -0.8660)$, which is what the demo
prints: `0.5000  -0.0000  -0.8660`.

**(d)** Normal. The vertical component of $\mathbf{s}$ is $-0.866 < 0$, i.e. the
hanging wall moved **down**, which is the definition of a normal fault.

---

## ★2 — Projection and classification

**(a)** $s_{ss} = \mathbf{s}\cdot\mathbf{d} = 0$ and
$s_{ds} = \mathbf{s}\cdot\mathbf{u} = 0.5 \times (-0.5) + (-0.8660)(0.8660)
= -0.25 - 0.75 = -1.0000$. Dip-slip dominated with $s_{ds} < 0$, so the fault is
**normal**, matching the demo's `-1.0000      -0.0000                          normal`.

**(b)** $s_{ss} = 1$, $s_{ds} = 0$: pure **left-lateral strike-slip**.

**(c)** $s_{ss} = 0.7071$, $s_{ds} = 0.3536 \times (-0.5) + 0.6124 \times 0.8660
= -0.1768 + 0.5303 = 0.3535$: both components are comparable, so **oblique**. The
demo's analogous case ($45^\circ$, $45^\circ$, rake $135^\circ$) gives
`0.7071      -0.7071                         oblique`.

**(d)** The demo uses the convention that a fault is strike-slip when
$|s_{ss}| \ge \cos 30^\circ = 0.866$, dip-slip on the same rule, and oblique
otherwise. It must be stated because the components vary continuously and the
label changes exactly where the threshold is placed: a report that says "oblique"
without the threshold cannot be compared with a report that uses a different one,
even though both may be describing the same fault.

---

## ★3 — Throw and heave

**(a)** throw $= 100\sin 60^\circ = 86.6$ m; heave $= 100\cos 60^\circ = 50.0$ m.
The demo prints exactly these.

**(b)** $86.6/50.0 = 1.732$, and $\tan 60^\circ = 1.732$. The demo's `throw/heave`
and `tan(dip)` columns agree row by row.

**(c)** $\sqrt{86.6^2 + 50.0^2} = \sqrt{7500 + 2500} = \sqrt{10\,000} = 100$ m,
recovering the net slip. The demo prints
`dip 60: sqrt(throw^2 + heave^2) = 100.000000 m (net slip 100)`.

**(d)** The throw is the vertical component of the slip. The stratigraphic
separation is the distance between the same marker on the two sides, measured in a
stated direction, and it equals the throw only for pure dip-slip motion on a
section perpendicular to strike. With an oblique slip component, or on an oblique
section, the two differ — and since a seismic interpreter measures throw while a
stratigrapher measures separation, confusing them causes persistent disagreement.

---

## ★4 — Apparent dip

Equation (7): $\tan\delta_{\text{app}} = \tan\delta\sin\beta$.

**(a)** $\beta = 90 - 60 = 30^\circ$:
$\tan^{-1}(0.8391 \times 0.5) = \tan^{-1}0.4196 = 22.76^\circ$, the demo's
`22.7605`.

**(b)** $\beta = 60^\circ$: $\tan^{-1}(0.8391 \times 0.8660) =
\tan^{-1}0.7267 = 36.01^\circ$. $\beta = 90^\circ$:
$\tan^{-1}(0.8391) = 40.00^\circ$, the true dip, as it must be for a section
perpendicular to strike.

**(c)** $\beta = 180^\circ$: $\sin 180^\circ = 0$, so the apparent dip is
$0.0000^\circ$. The demo's 240° azimuth row (which is $\beta = 180^\circ$ for a
strike of 060) prints `0.0000` in both columns. For $\beta$ between 180° and 360°
the sine is negative and the apparent dip **reverses its sense**, because the
section is looking at the back of the plane.

**(d)** Because the relation is $\tan^{-1}(\tan\delta\sin\beta)$, which is
nonlinear in both arguments. For $\delta = 40^\circ$ and $\beta = 45^\circ$:
$\tan^{-1}(0.8391 \times 0.7071) = \tan^{-1}0.5934 = 30.68^\circ$, whereas
$40^\circ \times \sin 45^\circ = 28.28^\circ$. The naive multiplication is wrong by
2.4°, which is a fifth of the dip being estimated. The demo prints the same
comparison in its §4 commentary.

---

## ★5 — The demo

**(a)** The `rake back` column reproduces the input exactly for all four cases:
`270.0000`, `90.0000`, `0.0000`, `315.0000`.

**(b)** `normal        slip tendency                  0.0   58.0       0.4869`
and `Coulomb function               0.0   65.0       -31.47 MPa`. The two dips
differ: 58.0° and 65.0°.

**(c)** The closed-form table gives `slip tendency, dip (deg)  57.98` against a
scan of 58.0 (difference +0.02, within the 1° dip grid) and
`Coulomb, dip at 45 +/- phi/2  65.18` against 65.0 (difference −0.18).

**(d)** `normal 0.0 65.0 270.0 normal`, `strike-slip 65.0 90.0 180.0
right-lateral strike-slip`, `reverse 90.0 25.0 90.0 reverse`. Each regime
produces the fault type it is named after, which is Anderson's theory.

---

## ★6 — Two criteria, two optima

**(a)** $\sigma_1' = 264.9 - 100.7 = 164.2$ MPa (vertical), and with
$\Delta\sigma = 100$ MPa, $\sigma_3 = 264.9 - 100 = 164.9$ MPa so
$\sigma_3' = 164.9 - 100.7 = 64.2$ MPa.

**(b)** $\tan\alpha = \sqrt{164.2/64.2} = \sqrt{2.5576} = 1.5993$, so
$\alpha = 57.98^\circ$. Since $\sigma_1$ is vertical here, the *dip* equals
$\alpha$: 58.0°, matching the demo's scanned value.

**(c)** $45^\circ + 40.365^\circ/2 = 65.18^\circ$.

**(d)** Slip tendency answers "which of these mapped faults is most likely to
move", because it ranks faults within one stress field and is dimensionless.
The Coulomb function answers "does this fault fail at all", because it compares a
stress difference with a strength. They rank differently because dividing by
$\sigma_n'$ makes slip tendency depend on the stress ratio as well as on the
friction coefficient, while the Coulomb optimum depends only on $\mu$.

---

## ★7 — The strike-slip optimum

**(a)** Because the intermediate principal stress $\sigma_2$ is vertical, and a
plane containing $\sigma_2$ is vertical. The fault plane must contain the
intermediate axis, so the optimum fault is vertical.

**(b)** $\phi = 40.365^\circ$, so $45^\circ - 20.18^\circ = 24.82^\circ$ and the
strike is $90^\circ - 24.82^\circ = 65.18^\circ$. The demo's scan gives 65.0,
within the 2.5° strike grid. The conjugate is at
$65.18^\circ - 90^\circ = -24.82^\circ \equiv 155.18^\circ$, with the opposite
sense of slip.

**(c)** $\beta = \arctan\sqrt{\sigma_1'/\sigma_3'}$. With
$\sigma_1' = (264.9 + 50) - 100.7 = 214.2$ MPa east and
$\sigma_3' = (264.9 - 50) - 100.7 = 114.2$ MPa north,
$\beta = \arctan\sqrt{214.2/114.2} = \arctan 1.3696 = 53.86^\circ$. The pole
therefore lies at azimuth $90^\circ - 53.86^\circ = 36.14^\circ$, and the strike
(perpendicular to the pole) is $36.14^\circ + 90^\circ = 126.14^\circ$. The demo's
scan gives 125.0 — a difference of 1.14°, within the strike grid.

**(d)** Because they are different functions of the same two stress invariants.
The Coulomb criterion is linear in the tractions, so its optimum is set by the
ratio of the criterion's coefficients and depends only on $\mu$. Slip tendency is a
*ratio*, so its optimum depends on the stress magnitudes through
$\sigma_1'/\sigma_3'$. Both are correct; they answer different questions, and a
report that mixes them will not be reproducible.

---

## ★8 — The double couple

**(a)** For unit, mutually orthogonal $\mathbf{n}$ and $\mathbf{s}$, the tensor
has rank 2 and trace zero, and acting on $\mathbf{n} + \mathbf{s}$ gives
$\tfrac12(\mathbf{s} + \mathbf{n}) = \tfrac12(\mathbf{n}+\mathbf{s})$, while on
$\mathbf{n} - \mathbf{s}$ it gives $-\tfrac12(\mathbf{n}-\mathbf{s})$; the third
eigenvector is $\mathbf{n}\times\mathbf{s}$ with eigenvalue 0. Hence the
eigenvalues are $+\tfrac12, 0, -\tfrac12$.

**(b)** From (a), $\mathbf{n} + \mathbf{s}$ is the eigenvector for $+\tfrac12$ and
$\mathbf{n} - \mathbf{s}$ for $-\tfrac12$. The T (tension) axis is
$(\mathbf{n}+\mathbf{s})/|\mathbf{n}+\mathbf{s}|$ and the P (compression) axis is
$(\mathbf{n}-\mathbf{s})/|\mathbf{n}-\mathbf{s}|$. The demo verifies both against
its eigen-decomposition with differences of `1.11e-16` and `8.33e-17`.

**(c)** $M\mathbf{n} = \tfrac12(\mathbf{s}(\mathbf{n}\cdot\mathbf{n}) +
\mathbf{n}(\mathbf{s}\cdot\mathbf{n})) = \tfrac12\mathbf{s}$, and symmetrically
$M\mathbf{s} = \tfrac12\mathbf{n}$. So the traction on the fault plane is parallel
to the slip direction, and vice versa — which is the statement that the two planes
are the **nodal planes** of the radiation pattern, and that neither is privileged
by the data. The demo's traction checks print `parallel to s: True` and
`parallel to n: True`.

**(d)** The round trip gives `input plane 30.00 55.00 300.00` and
`auxiliary plane 164.81 44.81 125.53`, recovering the input plane exactly and
producing a second, equally valid interpretation. A focal mechanism therefore
constrains the P, T and null axes and the two nodal planes, and **cannot determine
which of the nodal planes is the fault**. The ambiguity is resolved by geology: the
observed surface rupture, or the sense in which the plane offsets the
stratigraphy, or the alignment of aftershocks. A moment-tensor solution reported
as a single fault plane without that reasoning is a choice presented as a
measurement.
