# Solutions — 25-03-06 Project: Gravity Inversion with Uncertainty Quantification

> Read after attempting. Lesson:
> [06 Gravity Inversion](../06-gravity-inversion-uq.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/gravity_inversion_uq.py`](../code/gravity_inversion_uq.py).

---

## ★1 — Order-of-magnitude kernel check

$$g \approx \frac{2G\Delta\rho A}{d}
= \frac{2 \times 6.6743\times10^{-11} \times 1 \times 6.25\times10^{6}}
{2.5\times10^{3}}
= \frac{8.3429\times10^{-4}}{2.5\times10^{3}}
= 3.337\times10^{-7}\ \mathrm{m\,s^{-2}}.$$

In mGal: $3.337\times10^{-7}/10^{-5} = \mathbf{0.0334\ mGal}$ per
$\mathrm{kg\,m^{-3}}$ of density contrast.

Unit check: $[\mathrm{m^{3}\,kg^{-1}\,s^{-2}}][\mathrm{kg\,m^{-3}}][\mathrm{m^{2}}]
/[\mathrm{m}] = \mathrm{m\,s^{-2}}$ ✔.

The computed maximum kernel entry is $0.0672\ \mathrm{mGal}$ per
$\mathrm{kg\,m^{-3}}$ — larger by a factor of two because the shallowest block
(section $6.25\ \mathrm{km}\times1\ \mathrm{km}$, centroid at 0.5 km depth) is
closer to the stations than the 2.5 km assumed here, and its field falls off as
$1/r$ rather than as the crude $1/d$. A one-line estimate agreeing to a factor of
two is a useful check; a factor of ten would mean a unit or a quadrature error.

---

## ★2 — Reading the χ² scan

$$\frac{\chi^{2}}{n} = 0.0001 \text{ at } \alpha = 10^{-6}
\quad\Longrightarrow\quad \text{the model fits the data far better than the noise}
\text{ level},$$

$$\frac{\chi^{2}}{n} = 27.38 \text{ at } \alpha = 10^{-2}
\quad\Longrightarrow\quad \text{the model fits far worse than the noise}.$$

**Below 1** means the residuals are smaller than the stated data uncertainty, which
is possible only by fitting the noise — the estimator has consumed the 32
parameters to reproduce 25 random numbers. **Above 1** means the residual structure
is being suppressed by the penalty: the model is too smooth to explain a signal
that is really there.

The discrepancy principle picks $\alpha = 3.16\times10^{-4}$ with
$\chi^{2}/n = 0.8641$: the largest penalty whose misfit is still comparable to the
noise, i.e. the smoothest model that does not under-fit. Note that the chosen value
sits between the two extremes by **four and a half orders of magnitude** — the
regularisation choice is not a detail.

---

## ★3 — The resolution matrix

$$R = C_m\,A^{\mathsf T}W_d A,
\qquad
C_m = \left(A^{\mathsf T}W_dA + \alpha L^{\mathsf T}L\right)^{-1}.$$

$R$ maps a true model into the estimated one: $\mathbb{E}[\hat m] \approx R\,m_\text{true}$.

- $R_{ii} = 1$: the estimate of parameter $i$ responds to parameter $i$ and to
  nothing else — the parameter is **perfectly resolved**, its averaging kernel is a
  delta function.
- $R_{ii} = 0$: the estimate of parameter $i$ does not respond to parameter $i$ at
  all — the parameter is **unresolved**, and the value returned is supplied entirely
  by the prior (here, by the smoothness penalty and the neighbourhood).

For an over-determined problem with no penalty and full column rank, $R = I$; with
32 parameters and 25 data, full resolution is impossible and
$\operatorname{tr}R = 21.42$ is the quantitative statement of that impossibility.

---

## ★★4 — What the trace means

$$\frac{\operatorname{tr}R}{n_\text{params}} = \frac{21.42}{32} = 0.669,
\qquad
\frac{\operatorname{tr}R}{n_\text{data}} = \frac{21.42}{25} = 0.857.$$

**The meaningful ratio is the first.** $\operatorname{tr}R$ counts *parameters*
resolved: it answers "how many of my 32 blocks does the data determine?", and the
answer is the equivalent of $21.4$. The ratio to the number of data has no
interpretation at all — a single gravity datum carries information about a
combination of blocks, not about one block, so "0.857 resolved parameters per
datum" is a category error. This is the trap the item is written to expose: the
data count and the parameter count are not commensurate, and the resolution matrix
is the only object that relates them correctly.

The complementary statement is that $32 - 21.42 = 10.58$ parameters' worth of model
space lies in directions the data do not constrain, and those directions are, by
construction of the kernel, the deep long-wavelength combinations.

---

## ★★5 — Why the covariance is smaller than the error

$$\frac{\text{mean error}}{\text{mean 1}\sigma} = \frac{24.43}{15.09} = 1.62.$$

The error decomposes as

$$m - m_\text{true} = \underbrace{(m - \mathbb{E}[m])}_{\text{random}}
+ \underbrace{(\mathbb{E}[m]-m_\text{true})}_{\text{bias}},$$

and $C_m$ describes only the first term: it is the covariance of the *estimator*
around its own mean, propagated from the data noise through the linear operator. The
second term is the regularisation bias, produced by the penalty's assumption that
neighbouring blocks have similar densities.

**Why it cannot be estimated from the data alone.** The bias is
$(\alpha L^{\mathsf T}L)$-shaped and depends on the **true** model, which is what
the inversion is trying to find. Estimating it requires assuming a model class — a
simulation study, a bound, or independent information. This is why a covariance
quoted as "the uncertainty" is systematically optimistic in a regularised
inversion, and why the honest report gives both the covariance and a
bias/error assessment (a synthetic recovery test, or the equivalence class of §7
of the lesson, which measures the total spread including the prior's influence).

---

## ★★6 — What the ensemble establishes

$$\frac{\text{predicted-data spread}}{\text{data noise}} = \frac{0.0459}{0.05}
= 0.918.$$

A ratio **below 1** means that the whole ensemble of 2000 models generates
predicted data that agree with the observed ones to better than the stated
measurement error: the models are mutually indistinguishable at the data's own
precision. That is the operational definition of an equivalence class, and it is
why "the data cannot distinguish these models" is a *measurement* rather than a
rhetorical claim.

The $16.8\%$ sign-flip rate then says something stronger and more useful than the
spread alone: the **magnitude** of the deep anomaly is undetermined to the point
that one posterior draw in six gives it the opposite sign. A spread alone
($21.08\ \mathrm{kg\,m^{-3}}$ on a true $-250$) could be read as "well determined
to within 10%"; the sign-flip rate shows that reading to be wrong.

Together the two numbers establish the exact shape of the claim: **the class is
tight enough in data space to be an equivalence class, and loose enough in model
space that individual deep parameters — and even their signs — are not
determined.** The report must say both, and a single best-fit section says neither.

---

## ★★★7 — Reducing the unresolved directions

**The problem.** $\operatorname{tr}R = 21.42$ of 32, with the unresolved directions
being the deep, long-wavelength combinations of blocks. Gravity's kernel is
$1/r^{2}$-like and smooth, so a deep broad body and a shallower narrow body produce
nearly the same surface profile: the two are almost collinear in data space.

**New observation, and its kernel.** Use a **gravity gradiometry / second-derivative
observation** — the vertical gradient of gravity
$\partial g_z/\partial z$, or a tensor component such as $V_{zz}$.

- Gravity kernel: $\partial g_z/\partial\rho$ involves
  $\int z'/((x-x')^{2}+z'^{2})\,\mathrm{d}x'\mathrm{d}z'$ — a slow $1/r$ decay of
  the integrand with distance.
- Vertical-gradient kernel:
  the integrand contains an extra factor of order $z'/r^{2}$, so it decays as
  $1/r^{3}$.

Higher powers of $1/r$ weight the **shallow** part of the model much more strongly
and suppress the deep, broad contributions, so the shallow/deep degeneracy is
broken: the shallow blocks become individually resolvable while the deep
combination remains in the null space — exactly the trade the inversion needs.

**How many data.** Each independent tensor component at a station supplies one
additional combination of blocks. Raising $\operatorname{tr}R$ from $21.42$ to
$29$ requires about $7.6$ new resolved directions, and each new measurement adds to
the trace by roughly the fraction of its sensitivity that is orthogonal to the
existing rows — for a gradient field at the same 25 stations, that is of order
half a unit of trace per station-row. Realistically, add **10–15 gradient
stations** (or a continuous gradient profile at 1–2 km spacing along the same
line, which is the practical form) on the same 50 km aperture, and verify the trace
numerically rather than trusting this estimate.

**The test that the improvement is real, not a prior effect.** The trap is that
changing the dataset tempts a change of $\alpha$, of $L$, or of the grid, and any
of those moves $\operatorname{tr}R$ without adding information. The test is a
**controlled comparison**: hold the grid, the prior $L$ and the $\alpha$-selection
rule fixed, run both inversions (gravity only, gravity + gradient), and compare
$\operatorname{tr}R$ and the mean absolute model error on **identical synthetic
data** with identical noise. The claim is that the trace rises and the model error
falls *at the same priors*; if the trace rises only after relaxing the prior, the
experiment has measured the prior, not the data.
