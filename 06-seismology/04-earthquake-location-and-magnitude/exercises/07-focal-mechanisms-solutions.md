# Solutions — 06-04-07 Focal Mechanisms from First Motions and Waveform Inversion

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [07 Focal Mechanisms](../07-focal-mechanisms.md).

---

## ★1 — One polarity

The tensor is proportional to
$\begin{pmatrix}1 & -1 & 0\\ -1 & 1 & 0\\ 0 & 0 & -2\end{pmatrix}$ in units of
$1.75\times10^{17}\ \mathrm{N\,m}$, so

$$
\mathbf{n}^{T}\mathbf{M}\mathbf{n}
= 1.75\times10^{17}\left[(n_N - n_E)^{2} - 2n_U^{2}\right].
$$

With $n_N - n_E = 0.058 + 0.280 = 0.338$ and $n_U = 0.958$:

$$
\mathbf{n}^{T}\mathbf{M}\mathbf{n}
= 1.75\times10^{17}\left[0.11424 - 1.83553\right]
= -3.01\times10^{17}\ \mathrm{N\,m},
$$

which is negative: the station records **dilatation**, matching the printed
$-3.0152\times10^{17}\ \mathrm{N\,m}$ (the small difference is rounding in the
printed direction cosines).

---

## ★2 — The trace

$$
M_{NN} + M_{EE} + M_{UU}
= 1.75\times10^{17} + 1.75\times10^{17} - 3.5\times10^{17}
= 0 .
$$

Zero trace means no volume change: the source is purely deviatoric.

---

## ★3 — The eigenvalues

$+M_0$ is the tension (T) axis, $-M_0$ the pressure (P) axis, and $0$ is the null
axis — the line where the two nodal planes intersect. The printed values are
$-3.5\times10^{17}$, $-1.26\times10^{1}$ and $+3.5\times10^{17}\ \mathrm{N\,m}$;
the middle one is zero to within $10^{-16}$ of $M_0$, i.e. round-off.

---

## ★4 — The nodal-plane equivalence

The two triples give the same tensor because they name the same mechanism
through its two nodal planes: if the fault plane is
$\phi = 225^\circ$, $\delta = 45^\circ$, $\lambda = -90^\circ$, then the
auxiliary plane is the converse fault with
$\phi' = 45^\circ$, $\delta' = 135^\circ$, $\lambda' = 90^\circ$, and the moment
tensor is unchanged. The demonstration verifies this to
$3.14\times10^{-16}$ in unit-moment terms.

**Implication:** a difference of $180^\circ$ in strike between two catalogue
entries can be agreement. Mechanisms must be compared through a
parameterisation-free distance (or by first resolving the equivalence), not by
subtracting angles.

---

## ★5 — How much of the grid fits

$$
\frac{20}{86\,904} = 2.30\times10^{-4} = 0.023\ \text{per cent}.
$$

A smaller percentage does **not** imply a better-determined mechanism, because the
percentage is measured against an arbitrary grid: refining the grid from 5° to 1°
steps multiplies the denominator by 125 while the acceptable *volume* in
parameter space barely changes, so the same physics appears as a much smaller
percentage. Counts and tensor distances must be reported with the grid they were
measured on.

---

## ★6 — The decomposition, by hand

With deviatoric eigenvalues $d = (0.3752, 0.1316, -0.5068)$:

$$
b = -d_2 = -0.1316 ,
\qquad
a = d_1 + 2d_2 = 0.3752 + 0.2632 = 0.6384 .
$$

Check the reconstruction:

$$
a(1,0,-1) + b(2,-1,-1)
= (0.6384, 0, -0.6384) + (-0.2632, 0.1316, 0.1316)
= (0.3752,\ 0.1316,\ -0.5068) = d . \ ✔
$$

The magnitudes entering the percentages are
$\sqrt{2}|a| = 0.9028$, $\sqrt{6}|b| = 0.3223$ and
$\sqrt{3}(0.15) = 0.2598$, so DC $= 60.8\ \%$, CLVD $= 21.7\ \%$ and
ISO $= 17.5\ \%$ — the printed row.

---

## ★7 — Testing a 15° strike difference

**Test:** compute the moment tensors of both solutions, normalise each to unit
maximum eigenvalue, and evaluate the tensor distance (or a rotation angle such as
the Kagan angle) *after* resolving the nodal-plane equivalence. Then compare that
distance with the spread of mechanisms in each method's own admissible set.

**Data needed:** the polarity set with its station geometry for the first-motion
inversion, and the waveforms with their Green's functions for the waveform
inversion, plus a common hypocentre and velocity model, since a differing depth
alone rotates a mechanism. The difference is significant only if it exceeds the
two admissible spreads; with 24 stations the admissible spread was already 0.17
in unit-tensor terms on exact data, so a 15° strike difference is usually inside
the noise.

---

## ★8 — How station distribution inflates the set

**Experiment:** hold the mechanism, the number of stations and the noise fixed;
generate many station distributions, from uniform coverage of the focal sphere to
a realistic one-sided, azimuthally clustered network; for each, run the same grid
search and record the number of acceptable mechanisms and the tensor distance
range within the family.

**Prediction:** the admissible set grows when the stations leave part of the focal
sphere unobserved, because the misfit becomes insensitive to rotations that move
nodal planes through that unobserved region. The uniform case of the lesson is
therefore a *lower bound* on real focal-mechanism uncertainty, and the growth is
strongest when the gap contains a nodal plane.
