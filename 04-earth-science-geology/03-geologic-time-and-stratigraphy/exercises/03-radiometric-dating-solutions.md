# Solutions — 04-03-03 Radiometric Dating Methods and Their Assumptions

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Every age below is tied to the stated set of
> decay constants, which is a tabulated set and differs between compilations.

---

## ★1 — Concordia ratios at 2000 Ma

With $t = 2.0 \times 10^9$ a:

**(a)** $x = e^{\lambda_{238}t} - 1 = e^{0.31025} - 1 = 0.36371$.

**(b)** $y = e^{\lambda_{235}t} - 1 = e^{1.9697} - 1 = 6.1683$.

**(c)** $^{207}\mathrm{Pb}/^{206}\mathrm{Pb} = y/x = 6.1683/0.36371 = 16.96$,
which sits between the demo's tabulated 15.17 at 1800 Ma and 25.54 at 2700 Ma as
it should.

**(d)** Because $^{235}\mathrm{U}$ decays about six times faster than
$^{238}\mathrm{U}$, the $^{207}\mathrm{Pb}$ inventory grows quickly even in young
rocks while the $^{238}\mathrm{U}$ inventory barely changes. The *ratio* is
therefore dominated by a numerator that is nearly constant at low age, and its
logarithmic sensitivity to age grows as the $^{235}\mathrm{U}$ reservoir is
consumed.

---

## ★2 — A single ratio

**(a)** $t = \ln(1.20)/\lambda_{238} = 0.182\,322/1.551\,25 \times 10^{-10} =
1.1753 \times 10^9$ a $= 1175.3$ Ma.

**(b)** With 0.199: $\ln(1.199)/\lambda_{238} = 0.181\,488/1.551\,25 \times
10^{-10} = 1.1699 \times 10^9$ a. The change is $-5.4$ Ma for a ratio change of
$-0.001$.

**(c)** For a young rock the ratio itself is small, so a fixed offset is a larger
fraction of it. Quantitatively, $\mathrm{d}t/\mathrm{d}x =
1/(\lambda(1+x))$, and the relative age change is
$\mathrm{d}t/t = \mathrm{d}x/[(\lambda t)(1+x)]$; at 100 Ma the product
$\lambda t$ is six times smaller than at 1000 Ma, so the same $\mathrm{d}x$
produces six times the *relative* age error. The demo states the same result:
`the same offset shifts a 100 Ma age by 63.2 Ma (63.2% of its age) against 5.5% at
1000 Ma`.

---

## ★3 — Concordant and discordant

A sample is **concordant** when its two daughter/parent ratios define a point on
the concordia curve, so a single value of $t$ satisfies both decay equations.
A sample is **discordant** when it plots off the curve, so the two chains disagree
and no single age explains the measurement. The diagram is the **concordia**
diagram, with $^{206}\mathrm{Pb}^{*}/^{238}\mathrm{U}$ on the abscissa and
$^{207}\mathrm{Pb}^{*}/^{235}\mathrm{U}$ on the ordinate.

---

## ★4 — Common-lead contamination

**(a)** $x_{\text{meas}} = 0.0806 + 0.005 = 0.0856$, so
$t = \ln(1.0856)/\lambda_{238} = 0.082\,109/1.551\,25 \times 10^{-10} =
5.293 \times 10^8$ a $= 529.3$ Ma.

**(b)** The error is $+29.3$ Ma, which is $+5.9$ per cent of the 500 Ma age.

**(c)** $x_{\text{meas}} = 0.0156 + 0.005 = 0.0206$, so
$t = \ln(1.0206)/\lambda_{238} = 0.020\,390/1.551\,25 \times 10^{-10} =
1.3143 \times 10^8$ a $= 131.4$ Ma, an error of $+31.4$ Ma $= +31.4$ per cent of
the 100 Ma age.

**(d)** The 100 Ma analysis is far worse *relative to its age*: the same absolute
offset in the ratio is a much larger fraction of a small ratio. The demo's
diagnostic differs because it uses a slightly different 100 Ma ratio, but the
conclusion is the same and the demo prints it: the offset "shifts a 100 Ma age by
63.2 Ma (63.2% of its age) against 5.5% at 1000 Ma". The lesson: common-Pb
correction matters most exactly where the ages are youngest.

---

## ★5 — The demo

**(a)** `SYNTHETIC true age 1,800 Ma, disturbance at 300 Ma`.

**(b)** `discordia fit:  207/235 = 16.552657 * (206/238) + -0.444787` and
`max chord residual over the 7 analyses: 2.665e-15 (a single-stage loss gives a
mathematically exact line)`.

**(c)** `intersections with concordia: 300.00, 1,800.00 Ma`, with
`upper intercept 1,800.00 Ma vs true age 1,800.00 Ma   -> error +0.000 Ma` and
`lower intercept 300.00 Ma vs disturbance 300.00 Ma -> error +0.000 Ma`.

**(d)** `mean of the seven 206/238 ages = 1,147.7 Ma, spread 1,500.0 Ma` and
`true age = 1,800.0 Ma; error -652.3 Ma (-36.2%)`. The spread is the diagnostic
because it is the direct evidence that the population is discordant: the seven
analyses span 1500 Ma, so no single age describes them, and averaging produces a
number that describes none of them.

---

## ★6 — A line with a slope

**(a)** $t = \ln(1.07)/\lambda_{\mathrm{Rb}} = 0.067\,659/1.42 \times 10^{-11} =
4.764 \times 10^9$ a $= 4765$ Ma. The demo prints 4,764.7 Ma for the same slope.

**(b)** The slope is $(0.7600 - 0.7110)/(0.90 - 0.20) = 0.049/0.70 = 0.070$, with
intercept $0.7110 - 0.070 \times 0.20 = 0.6970$. It must **not** be read as an
initial ratio: it is the value the mixing line reaches at $x = 0$, which is
determined by the two end-member compositions and by nothing else. Whether it
happens to resemble a plausible mantle value is a coincidence of the numbers
chosen here.

**(c)** Tests: (i) whether the line extrapolates through the compositions of
plausible end members, which a mixing array does and an isochron need not;
(ii) whether the isotope ratio correlates with an element ratio that has no place
in the isochron, such as $1/\mathrm{Sr}$;
(iii) whether adding a third component bends the line — the demo finds a maximum
departure of 0.00950 in $^{87}\mathrm{Sr}/^{86}\mathrm{Sr}$, orders of magnitude
above modern precision.

**(d)** Because a mixing line is *exactly* straight by construction. $r^2$
measures departure from a line, and there is none. No goodness-of-fit statistic
can distinguish an isochron from a mixing array, and that is the whole difficulty
of the problem.

---

## ★7 — One chain, and an assumption

**(a)** The age requires an assumed initial (common) Pb composition, since the
single ratio does not determine both $t$ and the common-Pb contribution.

**(b)** From §4 of the lesson, a 0.002 offset on a 1000 Ma analysis
(ratio 0.167804) gives an apparent age of 1011.0 Ma, an error of $+11$ Ma.

**(c)** An isochron age is a *joint* property of several cogenetic samples whose
slope and intercept are both fitted, so the initial ratio is a result rather than
a premise; a model age from one ratio assumes the initial composition and is
exactly as good as that assumption.

---

## ★8 — The discordia relation

Take the crystallisation at $t_1$ before present, a disturbance at $t_2$ before
present ($t_2 < t_1$), and closure since. Write the ratio of radiogenic Pb to
**present** uranium. Before the disturbance the sample has
$x_{\text{before}} = e^{\lambda t_1} - 1$. At the moment of disturbance the
radiogenic Pb present is a ratio to the uranium *then*, which is
$e^{\lambda(t_1 - t_2)} - 1$ times that uranium, so in terms of present uranium it
is $e^{\lambda t_2}\left(e^{\lambda(t_1 - t_2)} - 1\right) = e^{\lambda t_1} -
e^{\lambda t_2}$. **This is where the uranium decay between $t_1$ and $t_2$
enters**: the surviving older Pb must be re-expressed as a ratio to the uranium
that decayed in the meantime. After the disturbance, growth adds
$e^{\lambda t_2} - 1$, and the total is

$$x_{\text{now}} = (1 - f)\left(e^{\lambda t_1} - e^{\lambda t_2}\right) +
\left(e^{\lambda t_2} - 1\right) = x_1 - f\left(x_1 - x_2\right).$$

**(a)** As $f$ runs from 0 to 1, $x_{\text{now}}$ runs linearly from $x_1$ to
$x_2$, and identically in the $^{235}\mathrm{U}$ chain. The points therefore lie
on the chord joining the concordia points at $t_1$ and $t_2$.

**(b)** and **(c)** A numerical check with $t_1 = 2000$ Ma, $t_2 = 400$ Ma,
$f \in \{0, 0.25, 0.5, 0.75, 1\}$ gives points that are collinear by construction,
so the chord residual is at the round-off floor (of order $10^{-15}$, as the demo
reports for its own case), and intersecting the fitted chord with concordia
returns 2000 Ma and 400 Ma. The demo's analogous run reports
`max chord residual over the 7 analyses: 2.665e-15` and both intercepts recovered
with zero error.

---

## ★9 — Pb loss against U loss

**(a)** **Pb loss** removes daughter, so the ratios fall below concordia: the
points plot **below** the curve (normal discordance). **U loss** removes parent,
so the ratios rise above concordia: the points plot **above** the curve (reverse
discordance). The sign of the displacement is the primary diagnostic, and it is a
direct consequence of which nuclide was lost.

**(b)** A 3 per cent U loss means the measured ratio is larger by a factor
$1/(1 - 0.03) = 1.0309$. For $t_1 = 1500$ Ma,
$x_1 = e^{0.232\,688} - 1 = 0.262\,03$; the measured value is
$0.262\,03 \times 1.0309 = 0.270\,13$, and the apparent single-chain age is
$\ln(1.270\,13)/\lambda_{238} = 0.239\,19/1.551\,25 \times 10^{-10} = 1542$ Ma.
The displacement is $+42$ Ma on the one chain, and the sign is upward — which is
the point: a U deficit produces an age that is too old, and the analysis plots
above concordia.

**(c)** A two-stage history produces a single straight chord with concordant
endpoints. A multi-stage history produces a curved or segmented array: the points
do not fall on one line, and the departure from a straight line is the evidence
for more than one disturbance. The additional observation is therefore the
**goodness of the chord fit itself** — in this one case, unlike the mixing-line
problem, the residual carries real information.

**(d)** The analysis cannot determine *when* the disturbance happened in a
two-stage history without the second intercept, and it cannot determine whether
the disturbance was a Pb loss, a U loss or a diffusive exchange at all: those are
different physical processes that can produce the same chord. The interpretation
is a geological statement about what happened to the rock, and it has to be
stated as such.
