# Solutions — 05-02-02 Units and Conventions

> Numbers marked *verified* were computed.

---

## ★1 *(verified)*

$1\ \mathrm{Gal} = 10^{-2}$ m/s², $1\ \mathrm{mGal} = 10^{-5}$ m/s².
$30\ \mathrm{mGal} = 3\times10^{-4}\ \mathrm{m\,s^{-2}} = 300\ \mathrm{\mu m\,s^{-2}}$.

---

## ★2 *(verified)*

(a) $1.2\times10^{-6}$ T; (b) 5 mS/m; (c) 2.67 g/cm³; (d) 3.5 km/s. All four are
exact unit conversions. Only the input digits carry measurement precision.

---

## ★3

Gravity is taken positive downward, toward the attracting mass, because that is
the direction an instrument is pulled. Since $\Phi = -Gm/r$ is defined negative
(attractive), the field is $\mathbf{g} = -\nabla\Phi$; the negative sign converts
a *decreasing* potential toward the mass into a field *toward* the mass.

---

## ★4

The cgs system defines $\mathbf{B} = \mathbf{H} + 4\pi\mathbf{M}$ while SI uses
$\mathbf{B} = \mu_0(\mathbf{H}+\mathbf{M})$, so the susceptibility
$\mathbf{M}/\mathbf{H}$ acquires a $4\pi$ in one system. A factor-of-12.6 error
in susceptibility propagates linearly into magnetisation and hence into predicted
anomaly amplitude: a body thought to give 100 nT would give 1257 nT. It is
detected by comparing predicted anomalies with observations, or by checking the
numerical range: SI susceptibilities of common rocks are typically $\lesssim
10^{-2}$, whereas cgs values of the same rocks are $\lesssim 10^{-3}$.

---

## ★★5 *(verified)*

Axial dipole: $|\mathbf{B}| = \frac{\mu_0}{4\pi}\cdot\frac{2m}{r^3}$. Setting
$|\mathbf{B}| = 10^{-9}$ T and $r = 200$ m:

$$m = \frac{10^{-9}\cdot8\times10^{6}\cdot4\pi}{2\cdot1.2566\times10^{-6}}
= 4.00\times10^{4}\ \mathrm{A\,m^2}.$$

For a 20 m cube, $V = 8000$ m³, so $M = m/V = 5.0$ A/m — a substantial but
entirely ordinary magnetisation. This is why compact bodies are readily detected.

---

## ★★6

$8\ \mathrm{mV/V} = 0.8\%$. It is a ratio of two voltages, so it is
dimensionless; the units cancel. (The "mV/V" notation is a reminder of how the
number was obtained.)

---

## ★★7

Unit: Ω·m. It is **derived**, not measured: it is computed from measured
impedance ratios through a formula that assumes a specific layered or
homogeneous model. Converting it to a true resistivity requires the model
assumptions and, for a layered earth, an inversion.

---

## ★★8 *(verified)*

$B_a/B_0 = 400/48000 = 8.33\times10^{-3}$. Second-order term
$\approx\frac12 B_a^2/B_0 = 0.5\cdot(4\times10^{-7})^2/4.8\times10^{-5}
= 1.67\times10^{-9}$ T $= 1.67$ nT. **It matters at the 1 nT level** for a
400 nT anomaly: the naive linearisation is off by more than the instrument
resolution. Practical remedy: work with components, or iterate.

---

## ★★★9

A good solution stores the conversion factors *as derivations* in comments,
converts everything to SI, and implements a small dimensional-consistency check
by carrying exponent tuples $(m^a kg^b s^c A^d)$. It should flag at least:
$g_z = Gm/d^2$, $\mathbf{B} = \mu_0\mathbf{m}/4\pi r^3$, $R = (Z_2-Z_1)/(Z_2+Z_1)$,
$\delta = \sqrt{2/\mu\sigma\omega}$, and $\Delta z = v/4B$. Formulas containing
susceptibility, or any empirically fitted constant, cannot be checked
dimensionally and should be flagged as such rather than silently passed.

---

## ★★★10 *(verified)*

Induced magnetisation $M = \chi H$. Taking $H = B_0/\mu_0 =
50000\times10^{-9}/1.2566\times10^{-6} = 39.8$ A/m:
- SI, $\chi = 5\times10^{-3}$: $M = 0.199$ A/m.
- Treating the same number as a cgs susceptibility (convert by dividing by
  $4\pi$ to get SI): $\chi_\text{SI} = 5\times10^{-3}/(4\pi) =
  3.98\times10^{-4}$, giving $M = 0.0158$ A/m.

The SI interpretation gives a magnetisation **12.57 times larger** (i.e.
$4\pi$). Detection in a real dataset without knowing the convention: check the
ratio of the predicted anomaly to the observed one; if the misfit is
systematically $\approx 4\pi$ or $\approx 1/4\pi$ across several bodies of
different sizes, the convention is the cause. Also check the magnitude range
against the physical plausibility of the rock.
