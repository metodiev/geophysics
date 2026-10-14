# Exercises — 11-01-02 Targeting Strategy and Method Selection

Attempt these before reading the
[solutions](./02-targeting-and-strategy-solutions.md). The lesson is
[02 Targeting Strategy](../02-targeting-and-strategy.md). All models, contrasts,
noise levels and costs are **SYNTHETIC** teaching values.

Useful constants: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$\mu_0/4\pi = 10^{-7}\ \mathrm{H\,m^{-1}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, $1\ \mathrm{nT} = 10^{-9}$ T.

## ★ Foundational

**★1.** A sphere of radius $120\ \mathrm{m}$ with $\Delta\rho =
350\ \mathrm{kg\,m^{-3}}$ is centred at $z = 250\ \mathrm{m}$. Compute its excess
mass and its maximum gravity anomaly in mGal, then state what happens to the
anomaly if the same mass is redistributed into a cube.

**★2.** The same body has $\kappa = 0.03$ SI in an ambient field of
$48\ \mathrm{\mu T}$. Compute its induced dipole moment and the axial magnetic
anomaly in nT at $z = 250\ \mathrm{m}$.

**★3.** Compute the skin depth at $50$, $200$ and $800\ \mathrm{Hz}$ in a host of
$80\ \Omega\,\mathrm{m}$, and state the ratio by which it changes when the
frequency is multiplied by four.

**★4.** A gamma-ray spectrometer measures over soil of density
$1.5\ \mathrm{g\,cm^{-3}}$ and a cover of $25\ \mathrm{cm}$ of the same soil.
Using $\mu/\rho = 0.06\ \mathrm{cm^{2}\,g^{-1}}$, compute the half-value layer and
the transmitted fraction of the flux from beneath the cover.

## ★★ Applied

**★★5.** Two spheres are geometrically similar with $R/z = 0.5$: A has
$R = 80\ \mathrm{m}$ at $z = 160\ \mathrm{m}$, B has $R = 160\ \mathrm{m}$ at
$z = 320\ \mathrm{m}$, and both have $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$ and
$\kappa = 0.02$ SI in $B_0 = 50\ \mathrm{\mu T}$. Show that their maximum magnetic
anomalies are **equal** and that their maximum gravity anomalies differ, and give
the ratio. Then state which property of the anomaly is invariant under this
scaling and what that implies for the gravity inverse problem.

**★★6.** For the checkpoint target of the lesson (radius $100\ \mathrm{m}$,
$\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, $\kappa = 0.02$ SI, $B_0 = 52\
\mathrm{\mu T}$), find the depth at which the gravity and magnetic
signal-to-noise ratios are equal, given noise of $0.03$ mGal and $0.3$ nT. State
the crossover depth to the nearest $10\ \mathrm{m}$ and explain why such a depth
must always exist when $\Delta\rho \ne 0$ and $\kappa \ne 0$.

**★★7.** Using the lesson's EM index with a $100\ \Omega\,\mathrm{m}$ host,
compute the index at several frequencies and find the frequency that maximises it
for (i) a target of radius $150\ \mathrm{m}$ and resistivity $1\ \Omega\,\mathrm{m}$
at $z = 300\ \mathrm{m}$, and (ii) a target of radius $50\ \mathrm{m}$ and
resistivity $1\ \Omega\,\mathrm{m}$ at $z = 300\ \mathrm{m}$. Report both optima to
the nearest $10\ \mathrm{Hz}$, relate each to the target's time constant, and
state the practical difficulty this creates for survey design.

**★★8.** A detection threshold is set so that $P_{fa} = 0.01$. Recompute the
depth at which $P_d = 0.5$ for the *magnetic* method on T1 (radius $150\
\mathrm{m}$, $\kappa = 0.001$, $B_0 = 50\ \mathrm{\mu T}$, noise $0.2$ nT) and
compare it with the $P_{fa} = 0.05$ value of $699\ \mathrm{m}$. State the
consequence for a survey specification.

## ★★★ Research-oriented

**★★★9.** Design a targeting strategy (methods, order, geometry, and the decision
that ends each stage) for a SYNTHETIC target at $450\ \mathrm{m}$ depth with
$\Delta\rho = 250\ \mathrm{kg\,m^{-3}}$, $\kappa = 0.03$ SI and resistivity
$5\ \Omega\,\mathrm{m}$ in a $300\ \Omega\,\mathrm{m}$ host. Your answer must
state the target model, the predicted anomalies, the noise you assume and why,
the expected $P_d$, and the single measurement that would falsify the target
model most cheaply.

**★★★10.** The lesson's EM index is a product of a geometric factor, a host
attenuation and a one-parameter induction response. Identify precisely where this
product would break down for (a) a target thinner than its skin depth, (b) a
target in a conductive host where the host response is comparable to the target
response, and (c) a target whose conductivity varies internally. For each case
state the observable that would reveal the breakdown.

**★★★11.** A program has a budget of $3$ MUSD and three candidate methods with
SYNTHETIC costs of $250$, $60$ and $350$ USD/km² per $100\ \mathrm{km^2}$ and
detection probabilities $1.00$, $1.00$ and $0.51$ at the target depth. Before
surveying, the probability that the target exists is $0.10$. Two of the methods
are sensitive to the same physical property, so their results are correlated.
Compute the posterior probability that the target exists after two *positive*
results if the two tests are (a) independent with sensitivity and specificity
$0.9$, and (b) perfectly correlated so that they behave as a single test. State
where the $\rho = 0.8$ case lies, and explain why correlation alone does not
determine the joint distribution and therefore not the answer.
