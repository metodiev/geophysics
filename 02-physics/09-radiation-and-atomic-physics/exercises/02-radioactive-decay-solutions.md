# Solutions — 02-09-02 Radioactive Decay, Half-Life and Dating

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every answer below names the decay constant it used. The half-lives are commonly
tabulated values that differ between compilations; the paper they came from must
be cited in a report. All conversion factors below were recomputed from the
constants stated, not copied.

---

## ★1 — Half-life, decay constant, mean life

**(a)** $\lambda = \ln 2/T_{1/2} = 0.693\,147/30.08$ a $= 0.023\,043$ a⁻¹.
Dividing by the Julian year, $3.155\,76 \times 10^7$ s, gives
$7.3020 \times 10^{-10}$ s⁻¹.

**(b)** $\tau = 1/\lambda = 43.40$ a. The ratio
$\tau/T_{1/2} = 1/\ln 2 = 1.4427$.

**(c)** $\lambda T_{1/2} = 0.023\,043 \times 30.08 = 0.693\,147 = \ln 2$ in
per-year units, and $7.3020 \times 10^{-10} \times 30.08 \times 3.155\,76 \times
10^7 = 0.693\,147$ in SI. The check is unit-free, which is why it catches a
half-life entered in the wrong unit.

**(d)** $A = \lambda N = 7.3020 \times 10^{-10} \times 1.00 \times 10^{18}
= 7.30 \times 10^8$ Bq = 730 MBq.

---

## ★2 — Mass, activity, curie, decay

**(a)** $N = A/\lambda = 10^9/7.3020 \times 10^{-10} = 1.3695 \times 10^{18}$
atoms. Then $m = NM/N_A = 1.3695 \times 10^{18} \times 136.907/6.022\,14 \times
10^{23} = 3.113 \times 10^{-4}$ g = **0.311 mg**.

**(b)** $1.000$ GBq $= 10^9/3.7 \times 10^{10} = 0.027\,03$ Ci (27.03 mCi),
using the exact definition $1\ \mathrm{Ci} = 3.7 \times 10^{10}$ Bq.

**(c)** $A(100\ \mathrm{a}) = 1.000 \times e^{-0.023\,043 \times 100} =
1.000 \times e^{-2.3043} = 0.0998$ GBq. A 100-year-old source retains 10 per cent
of its activity, so an "unsealed, date unknown" caesium source is a factor of ten
uncertainty in any dose estimate made from its label.

**(d)** Because the *hazard* is the decay rate, and the decay rate changes with
time. A source's identity is its activity at a reference date, its nuclide and
its serial number; the mass of the nuclide is a derived quantity that nobody
measures.

---

## ★3 — Specific activity and the survey conversion factor

**(a)** $N$ per gram of $^{238}$U $= N_A/238.0508 = 2.5301 \times 10^{21}$
atoms; $\lambda = 4.915\,960 \times 10^{-18}$ s⁻¹; so
$A_s = 1.2436 \times 10^4$ Bq g⁻¹ = 12.436 kBq g⁻¹ = 12.44 MBq kg⁻¹.

**(b)** 1 ppm of natural uranium is a mass fraction $10^{-6}$ of which 99.2745 %
is $^{238}$U, so per kilogram of rock
$N = 0.992\,745 \times 10^{-6} \times 6.022\,14 \times 10^{23} \times 10^3/
238.0508$ g mol⁻¹ $= 2.5116 \times 10^{18}$ atoms, and
$A = 4.915\,960 \times 10^{-18} \times 2.5116 \times 10^{18}$ = **12.3472** Bq
per kg of rock, in secular equilibrium.

**(c)** The quoted factor 12.4 Bq kg⁻¹ per ppm agrees with (b) to 0.4 per cent.
The residual is entirely in the half-life and the abundance used: 12.3472 is what
*this* pair of tabulated values gives. The practical conclusion is not that
either number is wrong but that a conversion factor must be recomputed from the
compilation cited rather than copied, because otherwise a survey's concentrations
are quoted relative to a half-life nobody can find.

**(d)** Activity is $\lambda N$, so the ratio is
$(\lambda_{235}/\lambda_{238})(N_{235}/N_{238})$. The decay constants differ by a
factor of 6.35 ($T_{1/2}$ 7.038 × 10⁸ a against 4.468 × 10⁹ a) and the abundance
ratio is 1/137.9, so the activity ratio is $1/137.9 \times 6.35 = 1/21.72 =
0.0460$. The demo confirms 0.046042. The consequence for spectrometry is that the
185.7 keV $^{235}$U line is a 4.6 per cent contribution to the low-energy region,
sitting under the $^{238}$U series, and neither negligible nor dominant.

---

## ★★4 — The Bateman solution

The solution with $N_2(0) = 0$ is
$N_2(t) = N_1(0)\frac{\lambda_1}{\lambda_2-\lambda_1}(e^{-\lambda_1t} -
e^{-\lambda_2t})$. With $\lambda_1 = 0.069\,3147$ a⁻¹,
$\lambda_2 = 0.693\,147$ a⁻¹, $\lambda_1/(\lambda_2 - \lambda_1) = 0.111\,111$:

**(a)** $t = 5$ a: $e^{-0.3466} = 0.7071$, $e^{-3.4657} = 0.03125$, difference
$0.675\,87$, times $0.111\,111$ = **0.075 096**. The demo gives
$7.5095 \times 10^{-2}$: agreement to five figures.

**(b)** $t = 1$ a: $e^{-0.0693} = 0.9330$, $e^{-0.6931} = 0.5000$, difference
$0.4330$, times $0.111\,111$ = **0.048 115**. The demo gives
$4.8115 \times 10^{-2}$.

**(c)** Agreement in both cases, which is the verification that the code
implements the equation rather than something near it.

**(d)** At 30 a the parent has decayed to $e^{-2.079} = 0.125$ of its initial
value and the daughter, whose own half-life is 1 a, has been decaying for 30 of
its half-lives. The chain as a whole is in **transient equilibrium**, with the
activity ratio $\lambda_2N_2/(\lambda_1N_1)$ approaching
$\lambda_2/(\lambda_2-\lambda_1) = 1.111$. The daughter population is smaller than
at 5 a because it is following the parent down; what is constant in this limit is
the ratio, not either population.

---

## ★★5 — An isochron age

**(a)** $t = \ln(1 + \text{slope})/\lambda =
\ln(1.004\,965\,2)/1.420\,384 \times 10^{-11} = 4.953\,86 \times 10^{-3}/
1.420\,384 \times 10^{-11} = 3.4870 \times 10^8$ a = **348.70 Ma**.

**(b)** With $\lambda = 1.39 \times 10^{-11}$ a⁻¹:
$4.953\,86 \times 10^{-3}/1.39 \times 10^{-11} = 3.5632 \times 10^8$ a =
356.32 Ma. The age changes by **+7.62 Ma**, or **+2.19 per cent** — exactly the
ratio of the decay constants, $1.420\,384/1.39$. This is why ages published
before the IUGS convention are not directly comparable with later ones, and why
the decay constant must be stated.

**(c)** $t = \frac1\lambda\ln(1 + \text{slope})$. The slope is the ratio of two
concentration ratios and dimensionless; $1 + \text{slope}$ is dimensionless, so
its logarithm is; therefore $1/\lambda$ must carry the unit of time, and $t$ comes
out in whatever unit $\lambda$ was expressed in. Note that the *age* is a
duration and that no unit conversion enters if $\lambda$ is per year and $t$ is
wanted in years.

**(d)** The intercept is the initial
$^{87}\mathrm{Sr}/^{86}\mathrm{Sr}$ of the rock at the time the samples closed.
Fitting it rather than assuming it is the entire advantage of an isochron over a
model age: the initial ratio is a measured quantity of that rock, and its
uncertainty propagates into the age properly. It is also a diagnostic — an
intercept far outside the plausible range for the rock type indicates that the
samples were not cogenetic.

---

## ★★6 — A model age and its assumptions

$t = \ln\left(1 + \frac{y - r_0}{x}\right)/\lambda$ with $x = 1.60$,
$y = 0.714\,274$, $\lambda = 1.420\,384 \times 10^{-11}$ a⁻¹.

**(a)** $r_0 = 0.7040$: $(y - r_0)/x = 0.010\,274/1.60 = 6.42125 \times 10^{-3}$,
so $t = \ln(1.006\,421)/\lambda = 6.400\,7 \times 10^{-3}/1.420\,384 \times
10^{-11} = 4.506 \times 10^8$ a = **450.6 Ma**.

**(b)** $r_0 = 0.7100$: $(y - r_0)/x = 2.67125 \times 10^{-3}$,
$\ln(1.002\,671) = 2.667\,7 \times 10^{-3}$, so $t = 1.878 \times 10^8$ a =
**187.8 Ma**.

**(c)** The two assumptions span 450.6 to 187.8 Ma, a range of 263 Ma, against
the isochron age of the same dataset, which the demo reports as
$3.487 \times 10^8$ a = 348.7 Ma with a standard error of 3.8 Ma. The true age
used to generate the data was 350 Ma. So the isochron is right to 0.4 per cent
while the two model ages are wrong by 29 per cent and 46 per cent — and both were
computed from entirely defensible assumptions.

**(d)** A report must say: "This is a **model age** computed on the assumption
that the initial $^{87}$Sr/$^{86}$Sr ratio was 0.7040, appropriate for a
mantle-derived mafic rock; the isochron intercept for cogenetic samples from the
same unit is required to test that assumption." A model age without its assumed
initial ratio is not a reproducible measurement, and the number is meaningless to
anyone who does not know the assumption.

---

## ★★★7 — Radiocarbon

**(a)** $\lambda_\mathrm{Libby} = \ln 2/(5568 \times 3.155\,76 \times 10^7) =
3.9448 \times 10^{-12}$ s⁻¹; $t = \ln(1/0.25)/\lambda = 1.386\,29/1.244\,88
\times 10^{-4}$ a⁻¹ = **11 136 a**.

**(b)** With 5730 a, $\lambda = 1.209\,68 \times 10^{-4}$ a⁻¹, giving
**11 460 a**.

**(c)** The difference is **324 a** — 2.9 per cent of the age, exactly the
half-life difference.

**(d)** Neither is a calendar age because the method assumes the atmospheric
$^{14}$C/$^{12}$C ratio was constant, and it was not: it varies with the
geomagnetic field, solar activity, and (since the industrial era) fossil-fuel
burning and nuclear testing. A **conventional radiocarbon age** is a defined
quantity: the decay-law age computed with the Libby half-life and a fixed
standard. To quote a *calendar* age, one must calibrate the conventional age
against a measured curve — and state which curve, which version of it, and
whether the material was terrestrial or marine.

---

## ★★★8 — Closure temperature

Dodson's equation is implicit in $T_c$ and is solved by iteration. With
$A = 55$, $a = 5 \times 10^{-4}$ m, $E_a = 2 \times 10^5$ J mol⁻¹,
$D_0 = 10^{-4}$ m² s⁻¹ and $R = 8.3145$ J mol⁻¹ K⁻¹:

**(a)** $\dot T = 1\ \mathrm{K\,Ma^{-1}} = 1/(10^6 \times 3.155\,76 \times 10^7)
= 3.169 \times 10^{-14}$ K s⁻¹. Iterating gives $T_c = 551.5$ K =
**278.3 °C**. The demo reports the same value.

**(b)** At 100 K Ma⁻¹, $T_c = 613.2$ K = **340.1 °C**.

**(c)** Faster cooling gives a **higher** closure temperature. The grain has less
time at each temperature, so it must reach a higher temperature before diffusion
becomes fast enough to keep the daughter mobile; equivalently, it retains the
daughter from higher up on the cooling path. The direction is the opposite of the
intuitive "cool faster, close sooner", which is why the equation is worth
solving rather than guessing.

**(d)** The mineral with $T_c = 500$ °C passes through its blocking temperature
*earlier* in the cooling history, so it records the **older** age. With a
constant cooling rate of 100 K Ma⁻¹, the difference in the time at which the two
minerals crossed their closure temperatures is
$(500 - 340)/100 = \mathbf{1.6\ Ma}$. A real cooling history is not linear, which
is why the pair of ages is inverted through a thermal model rather than
subtracted.

---

## ★★★9 — Running the demo

**(a)** At 400 steps the Euler order is 1.002 and the RK4 order is 4.003. First
order and fourth order as expected; the collapse of the last RK4 entry to 1.918
is the round-off floor.

**(b)** $N(2T_{1/2})/N_0 = \exp(-2\ln 2)$ = 0.250000000000000, and the absolute
difference from 0.25 is 0.000e+00. The numerical solutions converge on the
analytic value to double precision.

**(c)** 1 ppm U: 12.3472 Bq kg⁻¹ (quoted 12.4); 1 ppm Th: 4.0573 (quoted 4.1);
1 % K: 317.1654 (quoted 313). The differences are 0.4, 1.0 and 1.3 per cent,
entirely from the tabulated half-lives and abundances.

**(d)** The activity ratio $^{235}\mathrm{U}/^{238}\mathrm{U}$ is 0.046042, i.e.
1/21.719; the abundance ratio is $0.0072/0.992\,745 = 1/137.88$. They differ
because the decay constants differ.

**(e)** Recovered age $3.487\,013 \times 10^8$ a with a standard error of
$3.76 \times 10^6$ a; true age $3.5 \times 10^8$ a; relative error
$3.710 \times 10^{-3}$ (0.37 per cent). The true age lies within one standard
error.

**(f)** The measured ratio is 0.999972, i.e. within $2.76 \times 10^{-5}$ of
unity, and the analytic prediction is $2^{-15.15} = 2.760 \times 10^{-5}$ where
15.15 is the number of $^{234}$Th half-lives in one year. The agreement to three
significant figures is the verification.

**(g)** Computed: the convergence orders, the located half-lives, the Bateman
comparison, the specific activities from the tabulated constants, the isochron
fit and the closure temperatures. Tabulated: every half-life, every molar mass,
every isotopic abundance, and the radiogenic heat-generation coefficients used in
lesson 04. The demo prints the word TABULATED beside each of them so that the two
categories are never confused in the output.
