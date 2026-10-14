# Solutions — 07-02-04 Practical Correction Workflow and Processing Sequence

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Practical Correction Workflow and Processing Sequence](../04-corrections-workflow.md).

---

## ★1 — The sequence, its inputs and its diagnostics

| # | step | main input | diagnostic |
|---|---|---|---|
| 1 | drift correction | base-occupation times and readings | drift-model residual rms, loop closure, per-segment slopes |
| 2 | tie to absolute | an absolute value with its uncertainty | constant offset between independent ties |
| 3 | coordinates and heights | GNSS/levelling, datum definition | sensitivity of the anomaly to position and height |
| 4 | normal gravity | adopted ellipsoid and gravity formula | latitude spread of the raw data; the formula's convention |
| 5 | free air | the coefficient at the station's latitude | slope of anomaly versus elevation (should be removed) |
| 6 | Bouguer slab | the assumed density | correlation of the anomaly with relief |
| 7 | terrain | DEM product, cell size and vertical datum | convergence with cell size and model extent |
| 8 | isostasy (optional) | a compensation model | correlation of the residual with topography, at long wavelength |

**Comment.** Every "diagnostic" above is a *residual-versus-something* plot or
statistic. A step that has no diagnostic cannot be verified, and a step that cannot
be verified should not be trusted — this is the operational form of the lesson's
theme that the workflow is a chain of model comparisons.

---

## ★2 — Three terms for a $400\ \mathrm{m}$ station

$$\mathrm{FA} = 0.308555\times400 = +123.422\ \mathrm{mGal},$$

$$\text{slab} = 2\pi G\rho h = 0.111969\times400 = 44.788\ \mathrm{mGal}
\quad\text{(subtracted in the reduction)},$$

$$\text{terrain} = 0.5\ \mathrm{mGal}
\quad\text{(added, in the convention slab minus topography)}.$$

**Net effect on the anomaly** (as corrections applied to
$g_{\text{obs}} - \gamma$):

$$+123.422 - 44.788 + 0.5 = +79.134\ \mathrm{mGal}.$$

So the three corrections *do not cancel*: the free-air and Bouguer terms differ by a
factor of $2.76$, and their difference is the $0.1966\ \mathrm{mGal\,m^{-1}}$
elevation dependence of the simple Bouguer anomaly derived in lesson
[07-01-04](../../01-gravity-fundamentals/04-gravity-reduction.md): here
$0.196586\times400 = 78.634\ \mathrm{mGal}$, plus the terrain term, gives the
$79.134\ \mathrm{mGal}$ above. Getting this arithmetic wrong by a sign changes the
anomaly by $160\ \mathrm{mGal}$.

---

## ★3 — Plate approximation versus a real prism

**Plate approximation.** For a compartment of mean thickness
$\bar{h} = 20\ \mathrm{m}$:

$$g_{\text{plate}} = 2\pi G\rho\,\bar{h}
= 0.111969\times20 = 2.2394\ \mathrm{mGal}.$$

(The plate value is independent of the compartment's horizontal size — that is the
property that makes the Hammer method fast, and the property that limits it.)

**Exact prism.** The prism is $100\times100\ \mathrm{m}$ with the observation $50\
\mathrm{m}$ from its edge, i.e. the nearest material is at a horizontal offset of
about $50\ \mathrm{m}$, comparable to the $20\ \mathrm{m}$ thickness. The exact
attraction is *less* than the plate value because

1. **the vertical component factor** $z/\sqrt{s^{2}+z^{2}}$ is below unity for the
   material away from the station, and it falls off with horizontal distance; and
2. **the finite extent** removes the infinite ring of material that the plate
   assumes.

Both effects reduce the attraction, so

$$g_{\text{prism}} < g_{\text{plate}} = 2.2394\ \mathrm{mGal},$$

and the difference $g_{\text{plate}} - g_{\text{prism}}$ is *exactly the terrain
correction of that compartment*. The lesson's own check gives the magnitude of the
geometric reduction: a flat $200\times200\times50\ \mathrm{m}$ prism at $100\
\mathrm{m}$ offset attracts $0.047871\ \mathrm{mGal}$ against a plate value of
$0.111969\times50 = 5.598\ \mathrm{mGal}$ — a factor of 117 smaller, because the
compartment is small compared with its distance. **This is why a terrain correction
must be computed compartment by compartment and summed numerically**: the plate
formula is not a small correction to the prism, it is a different quantity.

---

## ★★4 — Density error at $900\ \mathrm{m}$ of relief

The lesson measured that a $270\ \mathrm{kg\,m^{-3}}$ density error produces a
terrain-correlated anomaly with a fitted slope of $0.00980\ \mathrm{mGal\,m^{-1}}$
(against the plate prediction $0.01132$). Scaling linearly in the density error:

$$\text{error} \approx 0.00980 \times \frac{\Delta\rho}{270} \times h_{\max}.$$

With $h_{\max} = 900\ \mathrm{m}$:

| $\Delta\rho$ ($\mathrm{kg\,m^{-3}}$) | error at maximum relief (mGal) |
|---|---|
| 100 | $0.00980\times0.370\times900 = 3.27$ |
| 400 | $0.00980\times1.481\times900 = 13.07$ |

(Using the plate prediction instead gives $3.77$ and $15.09\ \mathrm{mGal}$; the
measured slope is the better estimate because it accounts for the hill's attraction
being broader than its relief.)

**Is the $1.0\ \mathrm{mGal}$ target achievable?** No, with either density error.
Even $\Delta\rho = 100\ \mathrm{kg\,m^{-3}}$ — a good regional average — leaves
$3.3\ \mathrm{mGal}$ at the highest station, more than three times the target. The
required density accuracy follows by inverting the relation:

$$\Delta\rho \le 270\times\frac{1.0}{0.00980\times900} = 30.6\
\mathrm{kg\,m^{-3}},$$

which is a sample-based or Nettleton-scan accuracy, not a guess. **In a survey with
$900\ \mathrm{m}$ of relief the density is the primary constraint on the achievable
anomaly accuracy, and this is an arithmetic fact, not a preference.**

---

## ★★5 — What cell size does a $100\ \mathrm{\mu Gal}$ target need?

**Assumed scaling.** A prism discretisation error scales with the *staircase* area of
the model's edges, which for a fixed topography is proportional to the cell size
$\Delta$: the error falls roughly as $\Delta$ (first order), not as $\Delta^{2}$,
because the terrain surface is misrepresented by triangular ripples of amplitude
$\propto\Delta$ and area $\propto1/\Delta$, so the two cancel.

**Scaling.**

$$\text{error}\left(\Delta\right) \approx 200\ \mathrm{\mu Gal}
\times\frac{\Delta}{100\ \mathrm{m}}.$$

For $100\ \mathrm{\mu Gal}$:

$$\Delta \le 100\ \mathrm{m}\times\frac{100}{200} = 50\ \mathrm{m}.$$

**Justification and test.** The assumed scaling must be *measured*, not asserted:
compute the terrain attraction with cells of 100, 75, 50 and 25 m and plot the
difference against the cell size on log–log axes. A slope of $-1$ confirms the
linear scaling; a slope steeper than $-1$ means the model has another error source
(for example a bilinear interpolation of the DEM, whose error scales differently),
and a slope shallower than $-1$ means the code is not even consistent.

**Practical note.** Halving the cell size quadruples the number of prisms and
therefore the computation; the convergence test above is what tells you when to stop
refining, because the remaining error is below the survey's own terms.

---

## ★★6 — Is the pipeline's residual explained?

$$\text{expected floor} = \sqrt{2.0^{2} + 2.5^{2} + 1.5^{2}}
= \sqrt{4 + 6.25 + 2.25} = \sqrt{12.5} = 3.536\ \mathrm{\mu Gal}.$$

Measured residual: $3.5\ \mathrm{\mu Gal}$ rms.

$$\frac{3.5}{3.536} = 0.99,$$

so the pipeline's residual is *consistent with* the quadratic sum of the three known
error sources, and there is no evidence for an unexplained term. Reporting this is
the correct outcome: a residual *below* the floor would be suspicious (over-fitting
or an error in the floor estimate), and a residual well above it would demand an
explanation.

**Caveat.** The comparison is meaningful only if the three terms are (i) independent
(if the drift residual and the terrain error were correlated the quadrature sum
would not apply) and (ii) estimated by independent means. Both are satisfied here:
the reading noise is measured from repeats, the drift residual from the loop, and
the terrain error from a cell-size comparison — three different experiments.

---

## ★★★7 — A $50\ \mathrm{\mu Gal}$ workflow for 500 stations (specification)

**Inputs and uncertainties.**

| input | specification | uncertainty | cost if wrong |
|---|---|---|---|
| instrument | relative meter, $2\ \mathrm{\mu Gal}$ per reading, drift $10\ \mathrm{\mu Gal\,h^{-1}}$ | — | see below |
| base occupations | every 30 min | drift model residual $0.08\times10\times0.5 = 0.40\ \mathrm{\mu Gal}$ | small |
| absolute tie | one absolute station, $4\ \mathrm{\mu Gal}$ | correlated | cancels in anomalies |
| positions | differential GNSS, $0.1\ \mathrm{m}$ horizontal | $0.08\ \mathrm{\mu Gal}$ | small |
| heights | differential GNSS, $0.03\ \mathrm{m}$ vertical | $0.03\times0.1995 = 0.006\ \mathrm{mGal}$ | small |
| density | $2670 \pm 30\ \mathrm{kg\,m^{-3}}$ from samples or a scan | $0.0098\times(30/270)\times h_{\max}$ | **dominant if relief is large** |
| terrain model | 25 m cells, extent $>20h$ | convergence-tested, target $<10\ \mathrm{\mu Gal}$ | moderate |
| reference system | one ellipsoid, one formula, stated tide system | convention | 0.5 µGal |

**Acceptance thresholds and diagnostics.** Loop closure $\le\sqrt{N}\sigma$;
drift-model residual rms $\le$ the reading noise; residual-versus-relief correlation
$\left|r\right| < 0.3$; terrain convergence difference $<10\ \mathrm{\mu Gal}$;
repeat-station differences consistent with the difference budget.

**Which input to improve first?** With $h_{\max}$ above a few hundred metres the
density term dominates: for $h_{\max} = 500\ \mathrm{m}$ and $\Delta\rho = 30\
\mathrm{kg\,m^{-3}}$ it is $0.0098\times0.111\times500 = 0.54\ \mathrm{mGal} =
544\ \mathrm{\mu Gal}$ — ten times the $50\ \mathrm{\mu Gal}$ target. So the first
investment is **a measured density** (samples, a borehole, or a Nettleton scan whose
residual correlation is reported), followed by **terrain resolution**, and only then
instrument time. If the relief is small ($<100\ \mathrm{m}$) the ordering changes:
then the drift model and the terrain model dominate, and denser base occupations come
first. **The budget decides, and it must be computed for the actual terrain.**

---

## ★★★8 — Validating a terrain-correction code (specification)

**Three independent checks.**

1. **Analytic benchmark against a brute-force integral.** One prism, or a small
   ensemble of prisms, compared with a direct point-mass summation over a refined
   grid. Expected agreement: the brute force's discretisation error, of order
   $\left(\Delta_{\text{cell}}/d\right)^{2}$ for a cell size $\Delta_{\text{cell}}$
   at distance $d$. In the lesson's run, agreement was $+0.016\%$ at $40^{3}$ cells,
   and refining the grid reduced it.
2. **Limit test.** A single prism of very large horizontal extent and thickness $h$,
   observed at its centre, must approach $2\pi G\rho h$ from below, with a deficit
   matching $2\pi G\rho h\left(1 - h/\sqrt{R^{2}+h^{2}}\right)$ for a disk-like
   extent $R$. Expected agreement: the difference between the square and circular
   footprints, of order the corner area fraction ($\sim20\%$ for a square of
   half-width $R$), so this test must be run with a *shape-aware* expectation, not
   with the disk formula alone.
3. **Independent numerical route.** The same hill integrated by Monte Carlo over the
   volume, with the estimator weighted by the local column height. Expected
   agreement: a few Monte-Carlo sigma; the lesson obtained $+0.58\sigma$ with
   $1.5\times10^{6}$ points.

**What to conclude from two passes and one failure.** It depends on *which* check
fails:

- Failing the Monte-Carlo check while passing 1 and 2 is most likely a Monte-Carlo
  estimator bias (for example, neglecting the correlation between the sampled height
  and the integrand), not a prism-code error — the internal checks would not pass
  otherwise. Remedy: fix the estimator and re-run.
- Failing the limit test alone points at the handling of the limiting cases
  ($x = 0$, $y = 0$, $z = 0$), i.e. at the observations that sit on a face or a
  corner of a prism — precisely the stations where a real survey computes a
  correction.
- Failing the brute-force check alone, with the failure *decreasing* as the brute
  force is refined, is a discretisation artefact of the reference, not an error.

**In every case the correct action is to say which check failed and why it cannot
be explained by the reference's own error**; "two out of three" is not a validation
result. A code that fails any check must be treated as unvalidated for the stations
where the failure occurs.

---

## ★★★9 — Questions for a map delivered as "standard corrections applied"

Ranked by how much the answer could change the map (largest first):

1. **What density was used for the Bouguer/terrain correction, and where did it come
   from?** From the lesson's sensitivity, a $270\ \mathrm{kg\,m^{-3}}$ error over
   $900\ \mathrm{m}$ of relief is $\sim13\ \mathrm{mGal}$ — larger than most
   anomalies being interpreted.
2. **Which anomaly is it?** Free-air, simple Bouguer, complete Bouguer or isostatic
   residual differ systematically by the slab and terrain terms; a "Bouguer"
   labelling error is a shift of tens to hundreds of milligal.
3. **What DEM, at what cell size and extent, and what vertical datum?** The
   cell-size error alone measured $156\ \mathrm{\mu Gal}$ between 100 and 200 m cells
   in this lesson, and a datum mismatch appears as a smooth trend.
4. **Which reference ellipsoid, gravity formula and tide system?** Conventions change
   the anomaly by up to a few milligal, and a tide-system mismatch is systematic.
5. **What is the tie, and which absolute datum?** It moves the map's level by several
   microgal to tens of microgal, and by more if a different global datum was used.
6. **How were the positions and heights obtained, and to what accuracy?** At
   $0.813\ \mathrm{mGal\,km^{-1}}$ of latitude gradient, a $1\ \mathrm{km}$ position
   error is $0.8\ \mathrm{mGal}$; a metre of height error is $0.2\ \mathrm{mGal}$.
7. **What is the drift model, the base-occupation interval and the closure
   statistics?** These set the short-wavelength reliability of the map.
8. **Which software and version, and can the reduction be re-run?** Without this the
   map is an assertion rather than a result.

**The two questions that matter most are 1 and 2.** They are also the two most often
left unstated, which is why a delivered Bouguer map should always carry them in its
metadata, and why the lesson insists that the workflow is part of the result.
