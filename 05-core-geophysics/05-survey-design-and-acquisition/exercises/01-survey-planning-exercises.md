# Exercises — 05-05-01 Survey Planning: Objectives, Target Resolution, Budget

Attempt these **closed-book** before opening the
[solutions](./01-survey-planning-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Useful values: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}$ (CODATA
2018, relative standard uncertainty $2.2\times10^{-5}$);
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ (exact, by definition of the Gal).
A $3\sigma$ amplitude detection criterion is assumed unless a question says
otherwise. All target parameters are synthetic.

---

## ★ Foundational

**★1.** A sphere of density contrast $1000\ \mathrm{kg\,m^{-3}}$ and radius 50 m
has its centre at 200 m depth. Compute its peak vertical gravity anomaly in mGal.
State the formula you used and why the sphere's exterior field equals that of a
point mass.

---

**★2.** Using the same body, compute the amplitude signal-to-noise ratio for
instrument repeatabilities of (a) 0.010 mGal, (b) 0.005 mGal and (c) 0.050 mGal.
State in each case whether the body passes a $3\sigma$ detection test.

---

**★3.** Two targets have radii $R$ and $2R$ with the same density contrast. Using
$h_{\max} \propto R^{3/2}$, by what factor does the maximum detectable depth
change? Justify the exponent.

---

**★4.** A target produces a 0.030 mGal anomaly and the survey noise is
0.010 mGal. (a) What is the SNR? (b) How many repeated measurements $N$ are needed
to raise the SNR to 6? (c) What is the cost in acquisition time if one measurement
takes 90 s?

---

**★5.** State, in one sentence each, why resolution, spatial sampling and depth of
investigation are three separate budgets, and name the parameter that controls
each one.

---

## ★★ Applied

**★★6.** A survey area is $20\ \mathrm{km} \times 15\ \mathrm{km}$. The target is
a compact body at 300 m depth whose anomaly half-width is about 250 m.

(a) Choose a station spacing using the rule $\Delta x \le h/4$ and justify it.
(b) Compute the number of stations.
(c) If a station costs 4 minutes of field time (including positioning, reading and
walking), how many field days (8 h each) does the survey need?
(d) If the same area is surveyed at $\Delta x = 25$ m instead, what happens to the
station count and the field time?

---

**★★7.** Repeat question ★★6 with the *magnetic* method, where the anomaly of the
same body decays as the inverse cube of distance. Assume the target's magnetisation
is fixed by the same volume and a synthetic susceptibility contrast giving a moment
of $10^{8}\ \mathrm{A\,m^{2}}$, and a noise level of 1 nT.

(a) Compute the dipole peak anomaly at 300 m depth.
(b) Compute the SNR.
(c) Does this survey detect the body? If not, what would you change?

---

**★★8.** A feasibility study proposes a 0.02 mGal detection threshold. The noise
budget is dominated by a vertical positioning term of 0.154 mGal (free-air gradient
$0.30785\ \mathrm{mGal\,m^{-1}}$ at a DGPS-class height accuracy of 0.5 m).

(a) What height accuracy is needed to reach a total budget of 0.02 mGal, if all
other terms contribute 0.010 mGal in quadrature?
(b) Which positioning class does that require?
(c) What does this imply about the claim "our gravimeter can detect 0.02 mGal"?

---

**★★9.** The same profile used in the lesson's demonstration had 891 bins, of
which 706 were at full fold (48 traces) and 185 were below it.

(a) What fraction of the profile lost noise rejection?
(b) If the fold loss reduces the S/N by $\sqrt{\text{fold}}$ and the edge bins carry
a fold of 24 on average, how much worse is the S/N there than in the interior?
(c) What would you report to the client about the usable part of the profile?

---

## ★★★ Research-oriented

**★★★10.** Design and run an experiment that measures the *statistical* detection
limit rather than the amplitude limit of Section 3.3 of the lesson. Generate 2000
noisy profiles over a target at a range of SNRs, apply a simple matched filter for
the known anomaly shape, and determine the SNR at which detection is achieved 90 %
of the time at a 5 % false-alarm rate. Report the threshold you measure and compare
it with the $3\sigma$ amplitude rule. State clearly what your experiment does *not*
establish.

---

**★★★11.** The $3\sigma$ criterion was applied to a single anomaly. For a grid of
$10^{5}$ independent cells, compute the expected number of false positives at 3, 4
and 5 standard deviations using the Gaussian tail probability, and state how the
detection threshold must change if the false-alarm rate per *survey* is to be held
at 5 %. Then explain why the cells are not in fact independent, and in which
direction that changes your answer.

---

**★★★12.** A client asks for "a survey that can find anything larger than 20 m
radius at 100 m depth". Write a short technical memorandum (300–500 words) that
reframes the request into a decidable specification, computes whether it is
achievable with a stated noise level, and states one condition under which the
answer is "no". Use numbers throughout and state every assumption.
