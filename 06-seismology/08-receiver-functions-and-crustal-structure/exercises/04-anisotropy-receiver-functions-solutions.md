# Solutions — 06-08-04 Anisotropy from Receiver Functions and Shear-Wave Splitting

> Read after attempting. Lesson: [04 Anisotropy](../04-anisotropy-receiver-functions.md).

---

## ★1 — Speeds and splitting

$v_{\text{fast}} = 4.20(1.03) = 4.326\ \mathrm{km\,s^{-1}}$;
$v_{\text{slow}} = 4.20(0.97) = 4.074\ \mathrm{km\,s^{-1}}$.

$$\delta t = 80\left(\frac{1}{4.074}-\frac{1}{4.326}\right)
= 80(0.245459-0.231160) = 80(0.014299) = 1.144\ \mathrm{s}.$$

Small-$\gamma$ check: $2(0.03)(80)/4.20 = 1.143\ \mathrm{s}$ ✔.

---

## ★2 — Nodes and maxima of $\sin 2(\varphi-30^\circ)$

Zeros where $2(\varphi-30^\circ) = 0^\circ$ or $180^\circ$:
$\varphi = 30^\circ$ and $120^\circ$ (the fast and slow axes).
Maxima where $2(\varphi-30^\circ) = 90^\circ$: $\varphi = 75^\circ$ (+1).
Minima where $2(\varphi-30^\circ) = 270^\circ$: $\varphi = 165^\circ$ (−1).
Period $180^\circ$. ✔

---

## ★3 — Derivation

$$\delta t = L\left(\frac{1}{v_s(1-\gamma)}-\frac{1}{v_s(1+\gamma)}\right)
= \frac{L}{v_s}\cdot\frac{(1+\gamma)-(1-\gamma)}{(1-\gamma)(1+\gamma)}
= \frac{2\gamma L}{v_s(1-\gamma^{2})}.$$

Small-$\gamma$: $\delta t \approx 2\gamma L/v_s$. The neglected factor is
$1/(1-\gamma^{2}) \approx 1+\gamma^{2}$; for $\gamma = 0.03$ this is $+0.09\%$,
for $\gamma = 0.10$ it is $+1\%$.

---

## ★4 — The $\gamma L$ product

$$\gamma L = \frac{\delta t\,v_s}{2} = \frac{1.20\times4.40}{2}
= 2.64\ \mathrm{km}.$$

Three solutions: $(L,\gamma) = (100\ \mathrm{km}, 2.64\%)$,
$(66\ \mathrm{km}, 4.0\%)$, $(44\ \mathrm{km}, 6.0\%)$. The data cannot choose;
petrology or an independent depth constraint must.

---

## ★5 — What the condition number means

$\kappa(M)$ is the ratio of the largest to smallest singular value of the design
matrix: it bounds how much a relative perturbation in the data can be amplified
in the fitted parameters. A value of $319$ means the dip and anisotropy columns
are nearly linearly dependent over the clustered azimuths, so a $1\%$ data
perturbation can move a fitted coefficient by up to $\sim300\%$. A value near 1
means the columns are nearly orthogonal: the data determine each coefficient
independently, and the two model types are separable.

---

## ★6 — Careful versus over-claiming

**Careful:** "For the clustered back-azimuthal distribution available to this
station, the one-lobe (dip) amplitude is unconstrained ($0.84\pm0.67$, i.e.
consistent with zero and with large values); we therefore report only the
two-lobe signature, which is stable, and note that a dipping interface cannot be
excluded. Stations with full azimuthal coverage resolve the one-lobe term to
$\pm0.002$."

**Over-claiming:** "The station shows anisotropy of $X\%$ with a fast axis at
$Y^\circ$."

**The difference:** the careful version states the admitted range and the
coverage limitation; the over-claiming version converts a non-unique fit into a
unique physical model. The measurement does not support the second sentence.

---

## ★7 — Network argument (specification)

**Assumptions:** azimuthal coverage is the limiting factor; amplitudes are
measured to $\sigma\approx0.01$; the four-basis model is adequate; events are
evenly distributed in back-azimuth.

**Requirement:** the dip and anisotropy bases $\{\cos\varphi,\sin\varphi\}$ and
$\{\cos2\varphi,\sin2\varphi\}$ become nearly collinear when azimuths are
clustered. Full $360^\circ$ coverage gives $\kappa(M)=1$ (demonstration). A
practical target is $\kappa\lesssim5$, which requires azimuths spanning the full
circle with no large gap. **Specification:** at least $\sim12$ well-distributed
back-azimuths per station (30° spacing) and, because the collinearity depends on
the *union* of paths sampled, several stations within a few tens of kilometres so
that the anisotropy is sampled from different directions. The exact count depends
on $\sigma$ and on the true amplitudes; the design should be checked by
simulating $\kappa(M)$ for the proposed geometry before any data are collected.
