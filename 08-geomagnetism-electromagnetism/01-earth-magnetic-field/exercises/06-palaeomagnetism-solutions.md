# Solutions — 08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [06 Palaeomagnetism, Reversals and Magnetostratigraphy](../06-palaeomagnetism.md).

---

## ★1 — Fisher precision and confidence cone

$$\hat k = \frac{N-1}{N-R} = \frac{20-1}{20-18.5} = \frac{19}{1.5} = 12.6667.$$

$$\alpha_{95} = \arccos\left[1-\frac{N-R}{R}
\left(\left(\tfrac{1}{0.05}\right)^{1/(N-1)}-1\right)\right].$$

The inner bracket: $(20)^{1/19} = e^{\ln 20/19} = e^{0.157635} = 1.170728$, so
$1.170728-1 = 0.170728$. Then

$$\frac{N-R}{R} = \frac{1.5}{18.5} = 0.081081, \qquad
0.081081\times0.170728 = 0.013845,$$

$$\alpha_{95} = \arccos(1-0.013845) = \arccos(0.986155)
= 9.5460^{\circ}.$$

The argument $0.986155$ is inside $[-1,1]$ ✔. (Had $R$ been used as the *mean*
unit vector, $R/N = 0.925$, the argument would have fallen below $-1$ and
`arccos` would have returned `nan`. That is the failure mode the lesson warns
about.)

---

## ★2 — Palaeolatitude and its error

$$\lambda = \arctan\!\left(\frac{\tan I}{2}\right).$$

$I = 38^{\circ}$: $\tan 38^{\circ} = 0.781286$, half is $0.390643$,

$$\lambda = \arctan(0.390643) = 21.3377^{\circ}.$$

$I = 43^{\circ}$: $\tan 43^{\circ} = 0.932515$, half is $0.466258$,

$$\lambda = \arctan(0.466258) = 24.9976^{\circ}.$$

So a $5^{\circ}$ inclination error at this latitude moves the palaeolatitude by
$24.9976-21.3377 = 3.6599^{\circ}$, i.e. about 400 km of north–south distance on
a sphere of radius 6371 km ($3.6599^{\circ}\times111.195\ \mathrm{km\,deg^{-1}}
= 407\ \mathrm{km}$). The lesson's table gives the same order
($3.19^{\circ}$ near $I = 30^{\circ}$ and $4.22^{\circ}$ near $45^{\circ}$).

---

## ★3 — Magnetic colatitude

$$p = \arctan\!\left(\frac{2}{\tan I}\right)
= \arctan\!\left(\frac{2}{\tan 65^{\circ}}\right)
= \arctan\!\left(\frac{2}{2.144507}\right) = \arctan(0.932616)
= 43.0031^{\circ}.$$

Physical meaning: $p$ is the angular distance from the site to the pole implied by
the inclination. $p = 0$ means the site is at the pole and the field is vertical;
$p = 90^{\circ}$ means the site is at the magnetic equator and the field is
horizontal. Since $I = 65^{\circ}$ would be the inclination at latitude
$\arctan(\tan 65^{\circ}/2) = 46.9969^{\circ}$, the two angles are complementary
($43.0031+46.9969 = 90$) ✔.

---

## ★4 — A virtual geomagnetic pole

Site: $\lambda_s = 30^{\circ}$, $\phi_s = 100^{\circ}$, $D = -10^{\circ}$
(i.e. $10^{\circ}$ west), $I = 45^{\circ}$.

$$p = \arctan\!\left(\frac{2}{\tan 45^{\circ}}\right) = \arctan 2
= 63.4349^{\circ}.$$

$$\sin\lambda_p = \sin 30^{\circ}\cos 63.4349^{\circ}
+ \cos 30^{\circ}\sin 63.4349^{\circ}\cos(-10^{\circ}),$$
$$= 0.5\times0.447214 + 0.866025\times0.894427\times0.984808
= 0.223607 + 0.762829 = 0.986436,$$

$$\lambda_p = 80.5522^{\circ}.$$

$$\phi_p = 100^{\circ} + \arctan\!\left(
\frac{\sin 63.4349^{\circ}\sin(-10^{\circ})}
{\cos 30^{\circ}\cos 63.4349^{\circ}
- \sin 30^{\circ}\sin 63.4349^{\circ}\cos(-10^{\circ})}\right)$$
$$= 100^{\circ} + \arctan\!\left(\frac{-0.155316}{0.387298-0.440419}\right)
= 100^{\circ} + \arctan(2.92380) = 100^{\circ} + 71.1183^{\circ}
= 171.1183^{\circ}.$$

Wrapped to $[-180^{\circ},180^{\circ}]$: $\phi_p = 171.1183^{\circ}$ or,
equivalently, $-8.8817^{\circ}$ (the antipodal representation is the south pole,
not the same pole).

**Distance from the geographic pole:** $90^{\circ}-80.5522^{\circ}
= 9.4478^{\circ}$.

Note the declination is *west* here, so the pole lies west of the site's meridian
by $71.1^{\circ}$ despite the small $10^{\circ}$ declination — a useful reminder
that a VGP is severely nonlinear in $D$ at low site latitude.

---

## ★5 — Sites needed for $\alpha_{95} = 2^{\circ}$

$\alpha_{95}$ scales approximately as $1/\sqrt{N}$, and the table gives
$\alpha_{95} = 2.5951^{\circ}$ at $N = 100$. Then

$$N \approx 100\left(\frac{2.5951}{2.0}\right)^{2} = 100\times1.6836
= 168.4 \quad\Longrightarrow\quad N \approx 170.$$

**Why the estimate is optimistic.** (i) The measured $\alpha_{95}$ does not follow
$1/\sqrt N$ perfectly: the lesson's own numbers give a factor 10.41 from
$N=5$ to $N=400$ against the predicted 8.94, so the small-$N$ values are
inflated and the extrapolation from $N=100$ inherits the curvature. (ii) A real
study cannot add sites without adding geological scatter, so the measured
$\alpha_{95}$ eventually stops falling at all — the angular dispersion of the
field, not the counting statistics, becomes the limit.

---

## ★6 — Reversal rate in different windows

The synthetic chronology of the lesson has 50 reversals in 10 Myr, a mean rate of
$5.000\ \mathrm{Myr^{-1}}$. In the first 5 Myr (windows 0–2, 2–4 and the first
half of 4–6) the count is $11+16+\text{(part)}$; taking the tabulated windows of
the lesson, the 0–2 and 2–4 windows contain $11+16 = 27$ reversals in 4 Myr,
a rate of $6.75\ \mathrm{Myr^{-1}}$, while the 6–8 and 8–10 windows contain
$10+6 = 16$ in 4 Myr, a rate of $4.00\ \mathrm{Myr^{-1}}$ — a 69% difference
between two disjoint halves of the same synthetic record.

**Why a longer window is not five times more reliable.** The counts are Poisson
distributed with mean $\lambda = rT$, so the *relative* standard error is
$1/\sqrt{\lambda} = 1/\sqrt{rT}$. Going from a 2 Myr to a 5 Myr window reduces
the relative error only by $\sqrt{2.5} = 1.58$, not by 5 or 2.5. To halve the
error you need four times the duration. And a longer window buys its precision at
the cost of resolution: it can no longer detect a real change of rate inside it.

---

## ★7 — Testing GAD (specification)

**Sampling design.** Collect $N \ge 100$ independent palaeomagnetic sites from a
single geological period, spread in latitude from the equator to at least
$70^{\circ}$ and in longitude around the globe. Independence means no two sites
from the same lava flow or the same sedimentary section; the unit is the
"palaeomagnetic site", and dependent sites inflate confidence for free.

**Age control.** Restrict to a period short compared with the timescale of
plate motion relative to the axis (so the pole is fixed) and long compared with
the secular-variation timescale (so the time average is meaningful). Radiometric
dates or a magnetostratigraphic correlation with dated intervals are needed for
each site; without ages the test confounds secular variation with motion.

**Statistic.** For each site compute the VGP. Then test:
the mean VGP latitude and longitude, and the scatter in VGP latitude as a
function of site latitude.

**Null hypothesis.** The VGPs cluster about a single pole coincident with the
rotation axis, with latitude-independent scatter.

**Alternative.** The scatter about the axis grows towards low site latitudes,
which is the classic signature of a dipole *offset* from the axis (an
axial-octupole component), or a non-dipolar field at low latitude.

**Falsification.** GAD is falsified if the mean VGP is significantly displaced
from the rotation axis (the displacement must exceed the bootstrap confidence
region of the mean), or if the latitude-dependence of the VGP scatter has the
wrong shape. A single continent is not a test: the test requires global coverage,
because a displaced dipole can be mimicked by a wrongly assumed plate motion if
all sites move together.

---

## ★8 — Coincidence probability, with and without a date

**Without dates.** Each of the $n$ polarity intervals is binary, so there are
$2^{n}$ possible patterns. If all are equally likely a priori, the probability
that a random pattern equals a given one is $2^{-n}$: $6.25\times10^{-2}$ at
$n=4$, $9.77\times10^{-4}$ at $n=10$, $2.44\times10^{-4}$ at $n=12$.

**With one independently dated interval.** Fixing the position of one interval in
the reference chronology removes the freedom to *slide* the section along it. The
shift freedom is what makes short patterns so ambiguous: with $n$ intervals a
pattern can be slid to about $n$ positions in a long reference sequence, so the
chance of *some* match is roughly $n\,2^{-n}$ rather than $2^{-n}$. A single date
pins the shift, so the coincidence probability returns to $2^{-n}$ — and, more
importantly, it converts the procedure from "correlation" into "prediction": the
remaining intervals are now *predicted* by the reference chronology and can be
tested.

**Assumption used.** That the reference chronology is itself correct at the
resolution of the test. If the reference has reversed intervals whose durations
are uncertain by more than the section's interval lengths, the exercise measures
the reference chronology's errors, not the section's age.
