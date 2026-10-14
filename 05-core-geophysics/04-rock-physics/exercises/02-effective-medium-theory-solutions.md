# Solutions — 05-04-02 Effective-Medium Theories

> Numbers marked *verified* were computed.

---

## ★1

$K_V = (1-\phi)K_s+\phi K_f$ (isostrain: all constituents share the strain);
$1/K_R = (1-\phi)/K_s+\phi/K_f$ (isostress: all constituents share the stress).

---

## ★2

$K_\pm = K_1 + f_2/[1/(K_2-K_1) + f_1\cdot3/(3K_1+4G_1)]$;
$G_\pm = G_1 + f_2/[1/(G_2-G_1) + f_1\cdot2(K_1+2G_1)/(5G_1(K_1+\frac43G_1))]$.
Phase 1 is the host: the stiffer phase gives the upper bounds, the weaker the
lower.

---

## ★3

Because they use the *variational* structure of the elasticity equations: the
HS result is the extremal energy for a two-phase mixture with one phase as a
coated-sphere host, so it is attainable by some geometry and hence cannot be
improved using only volume fractions and isotropy. Voigt and Reuss correspond to
the two trivial geometries (fully parallel, fully series) and are therefore
weaker.

---

## ★★4 *(verified)*

At $\phi = 0.25$: $K_V = 0.75(37)+0.25(2.2) = 27.75+0.55 = 28.30$ GPa;
$G_V = 0.75(44)+0 = 33.00$ GPa.
$K_R = 1/(0.25/2.2+0.75/37) = 1/(0.11364+0.020270) = 1/0.133907 = 7.4679$ GPa;
$G_R = 0$.
Hill: $K = 17.884$ GPa, $G = 16.500$ GPa.

---

## ★★5

$1/G_R = (1-\phi)/G_s + \phi/G_f$; with $G_f = 0$ the second term diverges, so
$G_R = 0$ for any $\phi>0$. Reporting "the Reuss shear modulus" of a
fluid-saturated rock therefore reports zero — a bound, not a prediction, and a
useless one.

---

## ★★6 *(verified)*

Host = solid: $K_{HS+} = 37 + 0.25/[1/(2.2-37) + 0.75\cdot3/(3(37)+4(44))]$
$= 37 + 0.25/[\,-0.028736 + 2.25/287\,] = 37 + 0.25/[-0.028736+0.007840]$
$= 37 + 0.25/(-0.020896) = 37 - 11.964 = 25.036$ GPa.
Host = fluid: $K_{HS-} = 2.2 + 0.75/[1/(37-2.2) + 0.25\cdot3/(3(2.2))]$
$= 2.2 + 0.75/[0.028736+0.113636] = 2.2+0.75/0.142372 = 2.2+5.268 = 7.468$ GPa.
The bracket $[7.47, 25.04]$ GPa is much narrower than $[7.47, 28.30]$ GPa.

---

## ★★7

Set $G_f = 0$ in the fluid-host formula:
$K_{HS-} = K_f + (1-\phi)/[1/(K_s-K_f) + \phi\cdot3/(3K_f)]$.
Simplify the second term: $1/(K_s-K_f) + \phi/K_f
= [K_f + \phi(K_s-K_f)]/[K_f(K_s-K_f)]
= [(1-\phi)K_f + \phi K_s]/[K_f(K_s-K_f)]$.
Then $(1-\phi)/[\ldots] = (1-\phi)K_f(K_s-K_f)/[(1-\phi)K_f+\phi K_s]$.
Adding $K_f$ and putting over a common denominator gives
$K_f[(1-\phi)K_f+\phi K_s] + (1-\phi)K_f(K_s-K_f)$ all over
$[(1-\phi)K_f+\phi K_s]$, i.e.
$K_fK_s(1-\phi+\phi)/[(1-\phi)K_f+\phi K_s] = K_fK_s/[(1-\phi)K_f+\phi K_s]$.
And the Reuss bound is $1/((1-\phi)/K_s+\phi/K_f)
= K_sK_f/[\,(1-\phi)K_f+\phi K_s\,]$. **Identical.** ✓

---

## ★★★8 *(verified)*

Measured: series assembly 8.886463 GPa against harmonic mean 8.886463 GPa
(relative difference $1.33\times10^{-14}$); parallel assembly 30.040000 GPa
against arithmetic mean 30.040000 GPa (relative difference $0.00\times10^{0}$)
for the $\phi = 0.20$ synthetic case.

What it proves: the *algebra* of the harmonic and arithmetic means is correctly
implemented, via an independent code path (assembling and solving linear
systems). What it does **not** prove: which average a real rock obeys, or that
either is physically correct for a given pore geometry. A series bar and a
parallel bank are two specific geometries that happen to *attain* the two bounds;
real rocks lie between them.

---

## ★★★9

The tool computes $\rho_b$, then the HS bounds, and checks whether
$K_\text{measured}\in[K_{HS-},K_{HS+}]$ and similarly for $G$. A measurement
outside the bounds is physically inadmissible *given the inputs*.

A violation is far more likely to mean: (i) wrong $\phi$; (ii) wrong constituent
moduli (e.g. a mineral modulus taken for the wrong mineral); (iii) anisotropy, so
the isotropic bound does not apply; or (iv) a measurement scale mismatch (an
ultrasonic measurement in the high-frequency regime, where Gassmann-style
relaxed moduli are not expected). Claiming a new mechanism should be the last
resort, after all four have been excluded — and the exclusion must be reported,
not assumed.
