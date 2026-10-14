# Solutions — 12-01-04 Lower-Mantle Heterogeneity and LLSVPs

Worked solutions for
[04-lower-mantle-heterogeneity-exercises.md](./04-lower-mantle-heterogeneity-exercises.md).
The lesson is
[04 Lower-Mantle Heterogeneity and LLSVPs](../04-lower-mantle-heterogeneity.md).
All models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — A residual from an anomaly

$$\delta u = -\frac{\delta v}{v^{2}} = -\frac{-0.115}{11.5^{2}}
= \frac{0.115}{132.25} = +8.696\times10^{-4}\ \mathrm{s\,km^{-1}},$$
$$\delta t = \delta u \times L = 8.696\times10^{-4} \times 1500
= +1.304\ \mathrm{s}.$$

The sign is **positive**: a slower-than-reference segment adds slowness, and a
positive residual means the arrival is later than the reference prediction. Note
the unit chain: $\mathrm{km\,s^{-1}}$ divided by $\mathrm{km^{2}\,s^{-2}}$ is
$\mathrm{s\,km^{-1}}$; multiplied by km gives s. Getting the sign wrong here is
the single commonest error in tomography, and the cure is to remember that
"positive $m$ = slow = delay".

### ★2 — Why one residual cannot be assigned to one depth

$$+0.40 + 0.55 - 0.25 = +0.70\ \mathrm{s}.$$

The residual is the *sum* of contributions along the whole path. A single number
therefore cannot say whether the 0.70 s came from one 3 % anomaly, three 1 %
anomalies, or a 0.7 % anomaly spread over the entire path. This is exactly the
non-uniqueness that the matrix formulation in Section 2 of the lesson makes
explicit: the data constrain the *integral* of slowness along each path, and
different models with the same integrals are indistinguishable. Distinguishing
them requires paths that cross, so that a cell's contribution is weighted
differently by different rays.

### ★3 — Anomaly to temperature

$$\Delta T = \frac{\delta\ln v_s}{\partial\ln v_s/\partial T}
= \frac{x/100}{-1.2\times10^{-5}}\ \mathrm{K},$$

| anomaly (slow) | $\delta\ln v_s$ | $\Delta T$ (K) |
|---|---|---|
| 0.25 % | $2.5\times10^{-3}$ | 208 |
| 1.00 % | $1.00\times10^{-2}$ | 833 |
| 2.00 % | $2.00\times10^{-2}$ | 1667 |

The sensitivity is **833 K per 1 %**, so even a tenth-of-a-percent anomaly
corresponds to ~83 K. The practical consequence is the reverse of the intuitive
one: because the conversion factor is so large, *small* errors in the recovered
velocity become *large* errors in temperature, which is why the temperature is the
least robust output of the chain.

---

## ★★ Applied

### ★★4 — A two-cell resolution matrix in closed form

$\mathbf{G}^{T}\mathbf{G} = \begin{pmatrix}2&2\\2&2\end{pmatrix}$, so with
$\mathbf{A} = \mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I}$ and
$\lambda^{2}=2$:

$$\mathbf{A} = \begin{pmatrix}4&2\\2&4\end{pmatrix},\qquad
\mathbf{A}^{-1} = \frac{1}{16-4}\begin{pmatrix}4&-2\\-2&4\end{pmatrix}
= \frac{1}{12}\begin{pmatrix}4&-2\\-2&4\end{pmatrix},$$
$$\mathbf{R} = \mathbf{A}^{-1}\mathbf{G}^{T}\mathbf{G}
= \frac{1}{12}\begin{pmatrix}4&-2\\-2&4\end{pmatrix}
\begin{pmatrix}2&2\\2&2\end{pmatrix}
= \frac{1}{12}\begin{pmatrix}4&4\\4&4\end{pmatrix}
= \begin{pmatrix}1/3&1/3\\1/3&1/3\end{pmatrix}.$$

**Interpretation.** $R_{11} = 1/3$: of cell 1's estimated value, one third comes
from cell 1's truth and one third from cell 2's; the remaining third is "lost" to
damping (the estimate is biased low). $R_{12} = 1/3$: the leakage between the
cells is as large as the retention. In general

$$\mathbf{R} = \frac{2\lambda^{2}}{(2+\lambda^{2})^{2}-4}
\begin{pmatrix}1&1\\1&1\end{pmatrix}
= \frac{2}{\lambda^{2}+4}\begin{pmatrix}1&1\\1&1\end{pmatrix},$$

which is **monotonically decreasing in $\lambda$ with the limit 1/2** as
$\lambda \to 0$. So the best possible diagonal for this experiment is 0.5, not 1:
the two cells can never be separated, because every ray samples them identically.
The null-space direction is $m_1 - m_2$ (the difference), and the determined
direction is $m_1 + m_2$ (the average). The lesson for real inversions: reducing
damping recovers the *average* of a poorly-resolved pair, not the pair.

### ★★5 — Choosing $\lambda$ and reporting a range

**(a)** The noise level is 0.05 s. Comparing the misfits:

| $\lambda$ | rms misfit (s) | $\lvert$misfit − 0.05$\rvert$ |
|---|---|---|
| 5 | 0.002 | 0.048 |
| 20 | 0.010 | 0.040 |
| **60** | **0.048** | **0.002** |
| 150 | 0.210 | 0.160 |
| 400 | 0.900 | 0.850 |

The discrepancy principle selects **$\lambda = 60$**, whose misfit matches the
noise level: the model is complex enough to explain the data, but not complex
enough to explain the noise.

**(b)** Temperatures:

$$\Delta T(\lambda = 60) = \frac{1.10/100}{1.2\times10^{-5}} = 917\ \mathrm{K},
\qquad
\Delta T(\lambda = 150) = \frac{0.80/100}{1.2\times10^{-5}} = 667\ \mathrm{K}.$$

The range over defensible damping is **667–917 K**, a factor of 1.4. Note that
$\lambda = 150$ gives a misfit four times the stated noise — an argument for
preferring 60, but not a proof, since the *stated* noise may itself be an
underestimate.

**(c)** With 240 data and 1200 cells, the normal matrix has rank at most 240, so
**at least 960 of the 1200 model directions are unconstrained** — 80 % of the
model space. Damping does not reduce that count; it merely chooses the
smallest-norm member of the unconstrained family.

### ★★6 — Bounding a reported anomaly

The estimate is a weighted average of the truth and its neighbours, shrunk by
damping. Two effects must be separated:

- **Resolution lower bound.** The estimate is biased low by construction: with
  $R_{ii} = 0.35$, the cell retains 35 % of its own amplitude, and the remaining
  65 % is a weighted mixture of neighbours. If the neighbours are *less*
  anomalous, the estimate under-reports, so the truth is **larger** than 1.5 %. A
  crude correction that divides by the diagonal gives
  $1.5/0.35 = 4.3$ % — usually too aggressive, because it amplifies noise
  (the mapped-noise rms scales as $R_{ii}^{-1}$).
- **Damping upper bound from noise.** Dividing by the diagonal multiplies the
  noise term by the same factor. A defensible bound is therefore
  $1.5\ \% \times (1 + 1/R_{ii}) = 1.5 \times (1 + 2.86) = 5.8\ \%$ at the extreme,
  which is far beyond any plausible mantle anomaly.

**The honest statement** is that the data support "a large slow anomaly at this
depth, of order 1.5 % as imaged, with the true amplitude likely larger by up to a
factor of about 3 and possibly much less", together with the *comparison* to other
regions of the same model. Reporting a single number of 1.5 % is defensible only
if it is labelled "as imaged under the stated regularisation".

---

## ★★★ Research-oriented

### ★★★7 — Raising the resolution at the base of the mantle

**Diagnosis.** The demonstration's resolution diagonal falls to 0.065 in the
deepest layer because every deep ray traverses the layer at a shallow angle near
its turning point, so a shift of the anomaly in *depth* changes the travel time
only weakly, and neighbouring cells trade off against each other.

**Data to add.** Three complementary additions:

1. **Deep-turning phases with steeper incidence at the base** — for example
   core-reflected and core-transmitted phases that approach the CMB nearly
   vertically (this is precisely the geometry used for ULVZ studies in
   lesson [05](../05-core-mantle-boundary.md)). Steep paths make the travel time
   sensitive to depth because the path length within a thin layer changes
   strongly with depth.
2. **A second azimuth in the same region**, to break the lateral smearing: the
   point-spread function in the demonstration is elongated along the ray
   direction.
3. **A different observable with a different kernel** — a reflection amplitude
   from the base-of-mantle region, whose sensitivity is concentrated in the last
   few tens of kilometres rather than integrated over the whole column.

**Predicted effect.** In a damped least-squares setting, adding independent data
multiplies the corresponding entries of $\mathbf{G}^{T}\mathbf{G}$ without scaling
the diagonal damping, so the effective $\lambda$ seen by those directions,
$\lambda/\sqrt{N}$, falls. If the number of *independent* deep constraints rises
by a factor $k$, the diagonal rises approximately as
$R_{ii} \to R_{ii}\,k/(k + \text{const})$. Concretely, to move 0.065 to 0.2 the
deep data must be made roughly four times as informative; with 12 deep turning
points in the demonstration, that means ~50 independent deep measurements,
or the equivalent in steep-path coverage.

**Verification without knowing the truth.** Two standard checks:
(i) a **resolution test** — invert synthetic data generated from a spike at the
target depth and measure the recovered peak and its spread (this is exactly what
the point-spread function formalises); (ii) a **checkerboard or two-model test** —
invert two different synthetic models that differ only at that depth and confirm
that the two recovered images differ. Neither uses the real Earth, so both are
available in any study.

### ★★★8 — Resolution or noise?

The two candidate explanations make different predictions, and both quantities can
be computed from $\mathbf{G}$, $\lambda$ and $\sigma$ alone:

1. **Noise-mapped model error.** $\mathbf{C}_m =
   \sigma^{2}\mathbf{A}^{-1}\mathbf{G}^{T}\mathbf{G}\mathbf{A}^{-1}$, so the
   per-cell standard deviation is $\sqrt{\mathrm{diag}(\mathbf{C}_m)}$. If noise
   were responsible for the shallow-layer "over-recovery", this term would be of
   the same size as the excess.
2. **Noise-free resolution prediction.** $\mathbf{R}\mathbf{m}_\text{true}$: the
   estimate the inversion would return from noise-free data. If resolution were
   responsible, this would already show the same pattern.

**What the demonstration shows.** In the shallowest layer (763 km) the true rms is
0.0717 %, the noise-mapped rms is only **0.0214 %**, and the noise-free
prediction $\mathbf{R}\mathbf{m}_\text{true}$ has an rms of **0.1325 %**, which
reproduces the actual recovered 0.1379 % almost exactly. So the noise term is a
factor of six too small to explain the pattern, and the resolution term explains
it completely.

**Interpretation.** A shallow layer sitting above two 1.2 % deep bodies acquires
apparent amplitude because the resolution matrix has off-diagonal weights of order
0.02–0.03 linking deep cells to shallow ones, and each shallow cell is linked to
many deep cells. If the truth were responsible instead, the noise column would
dominate and the truth column would be the one matching the estimate — the
opposite of what is observed. The general rule: **compute both; the comparison
tells you which fix is needed** (more data for resolution, less damping or better
picking for noise).

### ★★★9 — How large an anomaly breaks the linearisation?

**Transverse displacement.** In a medium with a velocity perturbation, the ray
bends. For a ray travelling distance $L$ through a region where the relative
velocity change is $\epsilon$ spread over a transverse extent $\sim L$, the
deflection angle is of order $\epsilon$ (in radians) — the same statement as
Snell's law for a smooth medium — so the transverse displacement at the far end is

$$\delta y \sim \epsilon L.$$

For $\epsilon = 10^{-2}$ and $L = 1000\ \mathrm{km}$:
$\delta y \sim 10\ \mathrm{km}$.

**Comparison with the cell size.** The demonstration's cells are 185 km deep and
500 km wide, so a 10 km deflection is 2 % of a cell width: negligible. A 500 km
grid (as in ★★★9's premise) has the same conclusion, and even a 100 km grid is
barely affected.

**Where it breaks down.** The linearisation fails when the path change alters the
*integrated slowness* by an amount comparable to the anomaly signal. The
path-integral correction is second order in $\epsilon$:
$\delta^{2}t \sim \epsilon^{2}\,t_\text{segment}$. For a 100 s segment,
$\epsilon = 10^{-2}$ gives $10^{-4} \times 100 = 10\ \mathrm{ms}$ — comparable to
a good pick. So at $\epsilon = 1$ % the second-order term is at the level of the
best data, and at $\epsilon = 3$ % (0.09 s for the same segment) it exceeds the
picking error. In addition, the *kernel* itself is wrong: the true sensitivity of
a travel time to a finite-frequency anomaly is a banana–doughnut kernel rather than
a line, whose width is the Fresnel zone
$\sqrt{\lambda L}$ — for $\lambda \approx 100\ \mathrm{km}$ and
$L \approx 1000\ \mathrm{km}$ that is ~300 km, larger than a 100 km cell. So the
practical rule is:

- the **ray-path linearisation** is adequate for anomalies of a few per cent;
- the **delta-function kernel** is not adequate when the cell size falls below the
  Fresnel zone, and a finite-frequency kernel must be used;
- and neither issue excuses the analyst from reporting the damping, which changes
  the answer by more than either.

---

## Mastery checkpoint — worked version

> 300 rays, 2000 cells, $\lambda = 50$ chosen so the rms misfit equals a stated
> 0.04 s noise level; recovered peak 1.4 % slow.

**(a) Unconstrained directions.** The normal matrix $\mathbf{G}^{T}\mathbf{G}$ is
2000×2000 with rank at most 300, so **at least 1700 of the 2000 model directions
(85 %) are unconstrained**. Damping selects a particular member of that family; it
does not add information.

**(b) Why 1.4 % is a lower bound only conditionally.** The estimate is
$\hat{\mathbf{m}} = \mathbf{R}\mathbf{m}_\text{true}$ in the noise-free case, so
$\hat{m}_i = R_{ii}m_i^{\text{true}} + \sum_{j\neq i}R_{ij}m_j^{\text{true}}$. The
first term alone would say $m^{\text{true}} = 1.4/R_{ii} \ge 1.4$ %, i.e. the
estimate is a lower bound — but only if the leakage term
$\sum_{j\neq i}R_{ij}m_j^{\text{true}}$ is non-negative. If the neighbours are
*faster* than the reference (negative anomalies), the leakage subtracts and 1.4 %
is an *over*estimate. To check, you need the **point-spread function row**
$\mathbf{R}_{i\cdot}$ together with an estimate of the neighbouring anomalies —
that is, you need to know the sign of the surroundings, which is exactly what the
model's own map shows only if the neighbours are resolved.

**(c) Temperature.** With
$\partial\ln v_s/\partial T = -1.2\times10^{-5}\ \mathrm{K^{-1}}$:

$$\Delta T\big|_{\text{as imaged}} = \frac{0.014}{1.2\times10^{-5}}
= 1167\ \mathrm{K}.$$

Correcting for a resolution diagonal of 0.5 by dividing the amplitude by $R_{ii}$
(a crude but standard correction):

$$m^{\text{true}} \approx \frac{1.4\ \%}{0.5} = 2.8\ \%,
\qquad \Delta T \approx \frac{0.028}{1.2\times10^{-5}} = 2333\ \mathrm{K}.$$

The correction doubles the temperature. Two cautions make this a bound rather than
a value: the division also doubles any noise in the cell, and the linear
correction is exact only if the leakage is zero. The defensible report is
"$\ge 1167$ K as imaged; the true anomaly is likely larger, with the correction
factor set by $R_{ii}$ and the sign of the surroundings."

**(d) Tightening the vertical extent.** Two observations:

1. **Steep-incidence, core-reflected phases** (e.g. a core-reflected S phase and
   its multiples) whose path through the lowermost mantle is nearly vertical, so
   the travel time responds to a *thin* layer rather than to the whole column;
2. **A separate observable with a different kernel** — a reflection amplitude from
   the base-of-mantle region, or the waveform distortion of a grazing phase, both
   of which are sensitive to a layer a few tens of kilometres thick and therefore
   constrain the *thickness* rather than the depth-integrated anomaly.

Both work because they change the shape of the sensitivity kernel, not because
they add more of the same data: adding more long, shallow-angle paths would lower
the variance but not the vertical smearing.
