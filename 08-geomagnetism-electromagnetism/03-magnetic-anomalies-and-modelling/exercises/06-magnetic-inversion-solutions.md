# Solutions — 08-03-06 Magnetic Inversion and Its Non-Uniqueness

> **Read after attempting the exercises.** The lesson is
> [06 Magnetic Inversion](../06-magnetic-inversion.md).

---

## ★1 — Counting the nullity

$$\text{nullity} = 4000 - 200 = 3800 .$$

Halving the cell size in three dimensions multiplies the model dimension by
$2^{3} = 8$, to 32000 cells, while the data are unchanged:

$$\text{nullity} = 32000 - 200 = 31800 .$$

The nullity is a property of the discretisation, not of the physics or the data:
a finer grid is a more underdetermined problem. This is why the regularisation
does not merely "smooth the answer" — it is the only thing making the problem
well posed.

---

## ★2 — The sensitivity ratio

$$\frac{1.6066\times10^{3}}{1.1764} = 1365.7 .$$

A cell at 8 km depth needs about 1366 times the magnetisation of a cell at 1 km to
produce the same anomaly. An unconstrained or unweighted inversion therefore
places magnetisation as shallow as it can, because that is the cheapest way to
match the data. The depth weighting is the statement that this behaviour is
unphysical, and it is a *prior*, not a correction.

---

## ★3 — What the penalty does

It replaces the underdetermined problem "find all $\mathbf{m}$ with
$\mathbf{G}\mathbf{m}=\mathbf{d}$" by the well-posed problem "find the
$\mathbf{m}$ minimising misfit $+\lambda\times$penalty", thereby **selecting** one
member of the family. It adds no data and no physics; it adds a preference, and
the preference has to be stated.

---

## ★4 — The recovered-peak error

$$\frac{4.950 - 4.00}{4.00} = +23.8\% .$$

Reducing $\lambda$ does not help: the first four rows of the trade-off table have
misfits of essentially zero with peaks of 4.864, 4.864, 4.866 and 4.876 A m$^{-1}$
— all about $+22\%$ high. The overshoot is produced by the projection of the true
model onto the well-resolved subspace together with the penalty's bias against
concentrated models, and it is not reducible by tuning a parameter that is
already at its minimum useful value. The honest response is to report the range
(roughly $4.8$–$5.1$ A m$^{-1}$ over the tested regularisations) rather than a
single number.

---

## ★5 — The null-space demonstration

It demonstrates that a **model change of 156% produces no measurable change in the
data**. As a fraction of the noise:

$$\frac{5.2\times10^{-15}\times\left\|\mathbf{d}\right\|}{0.50\ \mathrm{nT}} .$$

With $\left\|\mathbf{d}\right\|$ of order $10^{3}$ nT (41 stations with a peak of
548 nT), the data change is of order $5\times10^{-12}$ nT, i.e. $10^{-11}$ of the
noise. The data cannot distinguish the two models at all — not "poorly", but not
at all — within this parametrisation. The physical reading is that magnetisation
below about 5 km is invisible at these stations, so it can be chosen freely unless
a prior constrains it.

---

## ★6 — The effect of positivity

$$\frac{3.499 - 4.349}{4.349} = -19.5\% .$$

The non-negative solution has $19.5\%$ less total moment and slightly more misfit
($0.455$ against $0.252$ nT). It is not evidence that the true moment is smaller:
the constraint is a **prior**, and applying it removes models the data could not
exclude. What it does show is that the unconstrained family contained
*unphysical* members (negative magnetisation) whose presence allowed a larger
total moment. The honest conclusion is a range whose upper end is set by the
unconstrained family and whose lower end is set by the constrained one, with both
fits reported as acceptable at the stated noise level.

---

## ★★7 — Experiment design (specification)

**Metric.** The condition number of the reduced operator restricted to the
subspace of models that lie under the deeper body, or more simply the smallest
singular value that is still above the noise-determined threshold; and the
interquartile width of the depth estimate of the deeper body over an ensemble of
noise realisations.

**Parametrisation, both cases.** The same $21\times8$ cell section, the same cell
sizes, and the same two bodies. In case 1, the data are the 41 stations of one
profile; in case 2, the data are two such profiles, one along $x$ through the
bodies and one perpendicular to it, sharing the station at the crossing.

**Expected result.** The perpendicular profile adds little: a 2-D body with strike
along $y$ produces almost the same anomaly on both profiles. A *strike-parallel*
second profile at a different $y$ position is the useful addition, because it
constrains the body's extent in that direction, which the original profile
confounds with its depth. The deeper body's depth interquartile should shrink
noticeably; its *moment* will remain poorly constrained because of the
depth–moment trade-off.

---

## ★★8 — Smoothness versus total variation

**Agree on:** (i) the achieved data misfit at the chosen regularisation, and (ii)
the total moment to within the range admitted by the data — both penalties
penalise structure, not magnitude, so the gross quantity is similar.

**Differ on:** (i) the sharpness of interfaces (total variation reconstructs
blocky models, smoothness produces gradational ones), and (ii) the depth at which
the transition between two units is placed, since a blocky model attributes the
transition to one interface and a smooth model spreads it.

**What to report.** The misfit, the parametrisation and *both* models, with the
statement that the data do not distinguish them, plus whichever quantity is
stable across the two (typically the total moment and the depth range). Reporting
one model because it "looks more geological" is reporting a prior as a result.

---

## ★★9 — Three questions, with arithmetic

1. **What magnetisation direction was assumed, and what happens if it is rotated
   by $30^\circ$?** From
   [02 Koenigsberger Ratio and Remanence Dominance](../02-koenigsberger-and-remanence.md),
   an induced-only interpretation of a $Q = 10$ body inflates the susceptibility
   by a factor of 11.6; the direction assumption is usually the largest single
   error in a magnetic inversion.
2. **What is the range of admissible models at the stated noise level?** A null
   space of dimension $n_{\text{model}} - n_{\text{data}}$ exists by construction;
   for a sectional inversion that is typically 100+ directions. The peak
   susceptibility of $0.15$ is one number from a family.
3. **What is the misfit, and how does it compare with the data noise?** A misfit
   far below the noise means the model is fitting noise, and the reported peak
   susceptibility is then a noise artefact — with a magnitude set by the
   regularisation, not by the Earth.
