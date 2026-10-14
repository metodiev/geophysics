# Solutions — 11-02-01 Geophysical Signatures of Major Deposit Types

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All contrasts, geometries and noise levels are **SYNTHETIC**.

Lesson: [01 Geophysical Signatures](../01-deposit-signatures.md).

---

## ★1 — Gravity anomaly

$$V = \frac{4}{3}\pi(150)^{3} = 1.4137\times10^{7}\ \mathrm{m^{3}},$$

$$\Delta g = \frac{4}{3}\pi G \Delta\rho \frac{R^{3}}{z^{2}}
= \frac{4}{3}\pi(6.67430\times10^{-11})(250)
\frac{3.375\times10^{6}}{9\times10^{4}} = 2.6210\times10^{-6}\ \mathrm{m\,s^{-2}}
= 0.2621\ \mathrm{mGal}.$$

Unit: m s⁻², reported in mGal ($1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$).

---

## ★2 — Magnetic anomaly

$$m = \kappa\frac{B_0}{\mu_0}V = 0.02 \times \frac{50\times10^{-6}}{4\pi\times10^{-7}}
\times 1.4137\times10^{7} = 0.02 \times 39.789 \times 1.4137\times10^{7}
= 1.1250\times10^{7}\ \mathrm{A\,m^{2}},$$

$$\Delta B = 10^{-7}\frac{2m}{z^{3}} = 10^{-7}
\frac{2(1.1250\times10^{7})}{2.7\times10^{7}} = 8.333\times10^{-8}\ \mathrm{T}
= 83.33\ \mathrm{nT}.$$

---

## ★3 — Radioelement contrasts

$$\Delta\text{K} = \frac{1.0-2.0}{2.0} = -50.0\%, \quad
\Delta\text{U} = \frac{1.5-2.0}{2.0} = -25.0\%, \quad
\Delta\text{Th} = \frac{4.0-10.0}{10.0} = -60.0\% .$$

---

## ★4 — Two structural questions

**(a)** The EM index contains $(R/z)^{3}$ **and** $e^{-2z/\delta}\frac{\omega\tau}
{\sqrt{1+(\omega\tau)^{2}}}$; the second factor is an exponential of the ratio of
depth to skin depth, and skin depth depends on resistivity as $\sqrt{\rho}$. A
factor-4000 change in resistivity moves $\delta$ by a factor of 63 and therefore
moves $e^{-2z/\delta}$ by many orders of magnitude. Gravity contains only
$\Delta\rho$, which varies by a factor of $\sim20$ across the table.

**(b)** Because the surface gamma flux depends on the *absolute* concentration,
source geometry, soil moisture, vegetation and the instrument's sensitivity; the
ratio of a body's concentration to the local background cancels all of those
nuisance factors at once, leaving the geologically meaningful quantity. The cost
is that the ratio is dimensionless and carries no tonnage information.

---

## ★5 — Signature direction of the ★1–★3 body

$$\mathbf{s} = (0.2621,\;83.33,\;0.00340,\;-50.0,\;-25.0,\;-60.0),
\qquad \|\mathbf{s}\| = 83.83 .$$

$$\mathbf{u} = (0.003126,\;0.99408,\;4.06\times10^{-5},\;-0.5964,\;-0.2982,\;-0.7157).$$

Cosines against the lesson's rows:

| class | cosine |
|---|---|
| VMS (massive sulphide) | **+0.9724** |
| magmatic Ni–Cu sulphide | +0.8968 |
| graphite schist (barren) | +0.6409 |
| porphyry Cu (disseminated) | −0.1496 |

**Most resembles VMS** by direction, although the magnetic amplitude ($83$ nT) is
closer to the Ni–Cu row's $417$ nT scaled down than to the VMS value $208$ nT at
the reference geometry. This is the lesson's central point in one calculation: the
direction is driven by the radioelements and the density, which point at VMS, while
the magnetic magnitude is ambiguous between classes because the body could be
smaller or deeper.

---

## ★6 — Known versus unknown amplitude

**Amplitude known.** Purely magnetic discrimination with
$\|\mathbf{s}_i-\mathbf{s}_j\| = 0.0354\|\mathbf{s}_i\| = 0.0354(1458) = 51.6$ nT
and $\sigma = 0.2$ nT:

$$P_{\text{err}} = \Phi\!\left(-\frac{51.6}{2(0.2)}\right) = \Phi(-129.0)
\approx 0 \quad\text{(zero to double precision)}.$$

**Amplitude unknown, $A = 1$.** With $\mathbf{s}_i \cdot (\mathbf{u}_i-\mathbf{u}_j)
= \|\mathbf{s}_i\|(1-\cos) = 1458(5.6\times10^{-4}) = 0.817$ and the projected
noise $\sqrt{\sum\sigma_k^{2}(u_{ik}-u_{jk})^{2}} = 0.177$ nT:

$$P_{\text{err}} = \Phi\!\left(-\frac{0.817}{0.177}\right) = \Phi(-4.61)
= 2.0\times10^{-6}.$$

The discrimination here is **not** carried by the magnetic channel — the two
magnetic directions differ by $0.06\%$ — but by the radioelement directions, which
is why the answer is good and also why it evaporates under cover.

**Amplitude unknown, $A = 0.1$** (a body ten times weaker, i.e. smaller or
deeper): the numerator scales with $A$ while the noise does not, giving
$P_{\text{err}} = 0.3027$ from the demonstration.

**Practical conclusion:** with the amplitude known, even a $0.06\%$ directional gap
is separable in principle; with the amplitude unknown, the same pair is separable
only by an *independent* channel, and only while the body outcrops. The dominant
assumption is not the noise level but **whether the size and depth are known and
whether the surface channels are available**.

---

## ★7 — Unknown depth

Magnetics scales as $z^{-3}$; with $R = 150\ \mathrm{m}$ and $B_0 = 50\
\mathrm{\mu T}$:

| $z$ (m) | VMS ($\kappa = 0.05$) | Ni–Cu ($\kappa = 0.10$) |
|---|---|---|
| 250 | 360.0 nT | 720.0 nT |
| 300 | 208.3 nT | 416.7 nT |
| 400 | 87.9 nT | 175.8 nT |
| 500 | 45.0 nT | 90.0 nT |

Every Ni–Cu value is exactly twice the VMS value at the same depth, because the
ratio is the susceptibility ratio. The **observed** $195\ \mathrm{nT}$ is consistent
with VMS at $\approx 307\ \mathrm{m}$ **and** with Ni–Cu at $\approx 387\
\mathrm{m}$: the observed amplitude alone cannot separate them once the depth is
free. The discrimination in the lesson's worked example survived only because the
depth was fixed by the target model.

What does separate them at fixed depth is the *simultaneous* fit of three channels:
VMS predicts $(0.629, 208.3, 0.03656)$ and Ni–Cu $(0.472, 416.7, 0.03317)$, so the
gravity-to-magnetic ratio differs by a factor $0.629/208.3 = 3.02\times10^{-3}$
against $0.472/416.7 = 1.13\times10^{-3}$ — a factor $2.7$. **A ratio of two
anomalies is amplitude-free**, and it is the discriminator that survives an unknown
depth. This is the practical form of the lesson's direction rule.

---

## ★8 — Singular values of a reduced signature matrix

Reduced matrix: gravity, magnetics, EM and K for the first four classes
(porphyry, IOCG, VMS, Ni–Cu), rows normalised:

$$\sigma = (1.82403,\; 0.82032,\; 2.032\times10^{-3},\; 1.112\times10^{-5}),$$

$$\text{condition number} = \sigma_1/\sigma_4 = 1.64\times10^{5}.$$

The weakest direction is

$$\mathbf{v}_4 = (-0.0556,\;1.2\times10^{-6},\;0.99845,\;4.9\times10^{-5}),$$

i.e. **$99.85\%$ on the EM channel**. Interpretation: after normalisation the EM
column is nearly a constant multiple of the other columns' small residual — the
classes differ in EM mostly by *magnitude*, not by pattern, so the EM axis carries
almost no class information. A condition number of $1.6\times10^{5}$ means that
projecting the observations onto the weakest direction amplifies noise by a factor
of $1.6\times10^{5}$, so any classifier that relies on it is numerically
unreliable.

---

## ★9 — Choosing weights, and what the choice asserts

**Scheme.** Weight channel $k$ by $1/\sigma_k$, with
$\sigma = (0.02\ \mathrm{mGal}, 0.2\ \mathrm{nT}, 0.02, 5\%, 5\%, 5\%)$, so
$\mathbf{w} = (50, 5, 50, 0.2, 0.2, 0.2)$, then normalise each row.

$$\sigma_{\text{weighted}} = (2.57504,\;0.46073,\;0.39380,\;0.04239,\;
0.00285,\;1.60\times10^{-4}),$$

$$\text{condition number} = 1.60\times10^{4} \quad (\text{from }1.29\times10^{5}).$$

The weakest direction becomes mixed:
$(0.059,\;0.000,\;0.934,\;0.049,\;-0.208,\;0.280)$ — still EM-dominated, but with
real radioelement content. **The weighting improves the conditioning by a factor of
about 8 without any new data**, because it stops a channel with an irrelevant
absolute scale from dominating the norm.

**What the choice asserts.** $1/\sigma$ weighting asserts that the noise is
independent Gaussian with the stated variances and that the cost of an error is the
same in every channel. Both are false in detail: noise is correlated between
channels (one bad line moves all of them), the variances depend on the flight and
the terrain, and an error in the radioelement ratio is not as costly as an error in
the magnetic amplitude. It also asserts that the *class separabilities* are what
matter, which is a statement about this table of classes — a different table would
give different weights. **Weights encode a prior about classes, not a measurement
of the ground**, and they must be reported with the result.

---

## ★10 — A benchmark with an unknown alternative

**Generation.** Take the seven-class table as the training set. Generate a held-out
class by perturbing a property vector off the convex hull of the table — for
example $\Delta\rho = 200$, $\kappa = 0.02$, $\rho = 8\ \Omega\,\mathrm{m}$,
K/U/Th $= 1.2/1.0/6.0$ — and simulate observations of it with the standard noise.

**Decision rule.** For a measurement $\mathbf{x}$, classify to the nearest class
**only if** the Mahalanobis distance to that class is below a threshold
$\tau$; otherwise return "unclassified". The threshold is calibrated by simulation
so that $\mathbb{P}(\text{unclassified} \mid \text{in-class}) = 0.1$.

**Metrics to report.** (1) the full confusion matrix over the seven training
classes; (2) the **open-set** quantities: the false-acceptance rate
$\mathbb{P}(\text{classified} \mid \text{held-out class})$ and the false-rejection
rate $\mathbb{P}(\text{unclassified} \mid \text{in-class})$, as a
receiver-operating-characteristic pair; (3) the class-conditional distribution of
the distance-to-nearest-class for in-class against held-out data, since a
confusion matrix alone is undefined for a class it has never seen.

**Expected failure mode.** The held-out class is nearest to whichever training
class has the largest magnetic signature (the perturbation keeps $\kappa = 0.02$,
which is small), so the false-acceptance rate is dominated by the magnetic channel
and is high unless the radioelement channels carry the discrimination. In a covered
terrain, expect false acceptance near 1: the classifier will confidently assign
every held-out body to an existing class. Reporting a confusion matrix without the
open-set numbers is exactly the overclaim this benchmark is designed to expose.

---

## ★11 — Remanence and the direction rule

Reverse the sign of the magnetic component of one class (a fully reversed remanent
magnetisation dominating the induced one), then renormalise:

| pair | cosine, induced only | cosine, one class reversed |
|---|---|---|
| IOCG / banded iron formation | +0.9994 | **−0.9959** |
| VMS / magmatic Ni–Cu sulphide | +0.9751 | **−0.6367** |

The magnetic channel is $>91\%$ of the dominant singular direction, so flipping its
sign flips the largest component of the signature vector: two classes that were
nearly identical become nearly antipodal, and two that were merely similar become
moderately anti-correlated.

**Consequence for prospecting.** The decision rule must not be "the class with the
largest cosine similarity", because a remanent body will be assigned to the
*worst*-fitting class. The rule must be symmetric in the sign of the magnetic
channel: either (i) search over a class-specific **magnetisation direction** as a
nuisance parameter, fitting a signed amplitude and reporting the best-fitting
combination of class and direction; or (ii) restrict the discrimination to
remanence-immune channels (gravity, EM, radioelements) and use magnetics only for
detection. In a terrain with known remanence — and the demonstration shows how
large the effect is — option (i) is compulsory, because otherwise a strongly
remanent orebody is systematically classified as barren.
