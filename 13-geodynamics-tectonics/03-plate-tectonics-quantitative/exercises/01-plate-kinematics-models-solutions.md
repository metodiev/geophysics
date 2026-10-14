# Solutions — 13-03-01 Plate Kinematic Models and Euler Pole Inversion

> **Read after attempting the exercises.** Where more than one answer is
> defensible, that is said so. Numbers below were computed, not estimated by
> hand.

Lesson: [01 Plate Kinematic Models and Euler Pole Inversion](../01-plate-kinematics-models.md).

---

## ★1 — Euler vector to pole

$$
|\omega| = \sqrt{0.006^2 + 0.003^2 + 0.008^2}
= \sqrt{3.6\times10^{-5} + 9\times10^{-6} + 6.4\times10^{-5}}
= \sqrt{1.09\times10^{-4}} = 0.010440\ \mathrm{rad\,Myr^{-1}}.
$$

In degrees per Myr: $0.010440 \times (180/\pi) = 0.5982\
\mathrm{deg\,Myr^{-1}}$.

Pole: $\varphi_p = \arcsin(0.008/0.010440) = \arcsin(0.7663) = 50.01^\circ$;
$\lambda_p = \operatorname{atan2}(-0.003, 0.006) = -26.57^\circ$.

---

## ★2 — Velocity at $(0^\circ, 0^\circ)$

$n = (\cos 0\cos 0,\ \cos 0\sin 0,\ \sin 0) = (1, 0, 0)$, so
$r = (6371,\ 0,\ 0)\ \mathrm{km}$.

$$
\omega \times r = \begin{vmatrix}
\hat x & \hat y & \hat z \\ 0.006 & -0.003 & 0.008 \\ 6371 & 0 & 0
\end{vmatrix}
= \big(\underbrace{-0.003\cdot0 - 0.008\cdot0}_{0},\
\underbrace{0.008\cdot 6371 - 0.006\cdot0}_{50.968},\
\underbrace{0.006\cdot0 - (-0.003)(6371)}_{19.113}\big)
$$

so $v = (0,\ 50.968,\ 19.113)\ \mathrm{km\,Myr^{-1}}$.

Resolve: at $(0^\circ,0^\circ)$ east is $(0,1,0)$ and north is $(0,0,1)$, so
$v_{\text{east}} = 50.97\ \mathrm{mm\,yr^{-1}}$ and
$v_{\text{north}} = 19.11\ \mathrm{mm\,yr^{-1}}$, with
$|v| = 54.43\ \mathrm{mm\,yr^{-1}}$. (Using the exact numbers:
$\sqrt{50.968^2 + 19.113^2} = 54.43$.)

---

## ★3 — Design matrix check

For $n = (1,0,0)$,

$$
[n]_\times = \begin{pmatrix} 0 & -0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0
\end{pmatrix}, \qquad
-R[n]_\times \omega = -6371 \begin{pmatrix} 0 \\ -\omega_z \\ \omega_y
\end{pmatrix}
= \begin{pmatrix} 0 \\ 6371(0.008) \\ -6371(-0.003) \end{pmatrix}
= \begin{pmatrix} 0 \\ 50.968 \\ 19.113 \end{pmatrix}
$$

which is the velocity of ★2. ✔ The sign pattern is the reason the $y$ and $z$
components swap roles between $\omega$ and $v$.

---

## ★4 — Aperture ratio from two network errors

$1/L$ scaling predicts
$L_{\text{two-cap}}/L_{\text{one-cap}} =
3.599/0.218 = 16.5$.

Geometric spans: the one-cap network spans about $445\ \mathrm{km}$. Two caps
centred $70^\circ$ apart span, at minimum, the chord between them,
$2R\sin(35^\circ) = 2(6371)(0.5736) = 7309\ \mathrm{km}$; adding the cap radii
gives essentially the same number to three figures.

The predicted ratio is $16.5$ and the geometric ratio is
$7309/445 = 16.4$. **Agreement is excellent**, which is a genuine confirmation
of the $1/L$ rule rather than a coincidence: both networks have $15$–$16$ sites,
so the only variable is the span.

---

## ★5 — Where the $\sqrt N$ goes

Let the network have aperture $L$ and $N$ sites, with independent velocity noise
$\sigma$ per component. The angular rate is estimated from the *spread* of
velocities across the network. Two views:

- **Difference of two ends.** One velocity difference across $L$ has error
  $\sigma\sqrt2$, so $\delta\omega \approx \sigma\sqrt2/L$. Independent of $N$.
- **Least squares over $N$ sites.** The design matrix columns scale with the
  site offsets, so $A^{\mathsf T}A \propto N\langle x^2\rangle$ where
  $\langle x^2\rangle \sim L^2/3$. Then
  $\sigma_\omega = \sigma\sqrt{(A^{\mathsf T}A)^{-1}} \sim \sigma/(L\sqrt N)$.
  The $\sqrt N$ is real: it comes from averaging many independent measurements
  of the same gradient.

The demonstration holds $N = 20$ fixed and varies $L$, so it measures the
$1/L$ part only. Both statements are correct; they answer different questions.
A network with $N$ sites in an aperture $L$ does improve as $\sqrt N$, but the
improvement is bounded by how well the sites sample the aperture: doubling $L$
helps linearly, doubling $N$ helps only as a square root.

---

## ★6 — Formal versus realised rms

For $k = 200$ independent realisations of a zero-mean normal error with standard
deviation $s$, the realised rms $\hat s$ has fractional standard deviation
$1/\sqrt{2k} = 1/\sqrt{400} = 0.05$, i.e. $5\%$.

Observed ratio: $3.599/3.475 = 1.036$, that is $3.6\%$ high. Well inside one
standard deviation. **Consistent** — the formal error is neither optimistic nor
pessimistic at this realisation count. Note also that a single realisation can
sit many percent away from $s$; the check only becomes sharp with many
realisations.

---

## ★7 — Is $3\times10^{-8}$ a signal?

No. The demonstration's four closure tests give $2.2\times10^{-16}$,
$2.0\times10^{-18}$, $2.5\times10^{-16}$ and $1.9\times10^{-16}$: all at the
level of double-precision round-off in a product of three $3\times3$ matrices
(machine epsilon is $2.2\times10^{-16}$).

$3\times10^{-8}$ is eight orders of magnitude larger, which cannot come from
round-off in a $3\times3$ product. It is either (i) a genuine inconsistency — for
example the three rotations are not all in the same frame, or a plate circuit is
closed with the wrong sense — or (ii) a numerical error such as using single
precision or a truncated series. **Either way it is a defect, not physics.**

---

## ★8 — Experiment specification (one defensible design)

**Metric.** $\varepsilon_\omega = \operatorname{rms}$ over realisations of
$(\hat\omega - \omega_{\text{true}})$, resolved into pole-latitude error,
pole-longitude error and rate error, plus $\operatorname{cond}(A)$ for each
network.

**Design.** Two families, each with 200 realisations at
$\sigma = 1\ \mathrm{mm\,yr^{-1}}$:
(i) fixed $N = 20$, aperture $20,40,80,160,320\ \mathrm{km}$;
(ii) fixed aperture $160\ \mathrm{km}$, $N = 5,10,20,40,80$ sites drawn
uniformly in the square.

**Predictions.** Family (i): pole-latitude error $\propto 1/L$. Family (ii):
error $\propto 1/\sqrt N$ until the sampling of the aperture saturates, after
which it flattens (a fixed aperture cannot support more independent gradient
information than its own size allows).

**Outcome that would falsify the model.** Family (ii) flattening *below*
$\sqrt N$ scaling for small $N$ would indicate that the noise, not the geometry,
dominates; family (i) failing the $1/L$ law would indicate a conditioning
problem appearing at large apertures (possible if the sphere's curvature becomes
important, i.e. $L \gtrsim 1000\ \mathrm{km}$).

---

## ★9 — Correlated noise

Correlated noise means the errors share a common component, so the effective
number of independent measurements is smaller than $N$.

- **(a) Global network.** Sites on different plates are far apart, so a
  correlation length of, say, $500\ \mathrm{km}$ leaves the between-plate
  differences nearly independent. The formal error inflates modestly, roughly by
  the ratio of the correlation length to the network span, which is small.
  The pole direction is barely affected; the common-mode part is largely
  absorbed by the reference-frame (translation) parameters.
- **(b) One cluster.** Almost all sites share the same error, so the velocity
  *difference* across the network — which is the only thing that carries
  information about $\omega$ — is largely destroyed. The formal error should
  inflate by a factor approaching the ratio of correlation length to aperture,
  which for a $445\ \mathrm{km}$ cap with a $500\ \mathrm{km}$ correlation length
  is of order unity or worse. The pole becomes nearly undetermined however many
  sites the cluster contains.

**Residual test.** Compute the residual covariance between station pairs as a
function of separation (a semivariogram of the residuals). White noise gives a
flat semivariogram; correlated noise gives one that rises with separation up to
the correlation length and then flattens. This test is decisive because it uses
only the residuals, not the estimated pole.
