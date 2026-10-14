# Exercises — 07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties

Attempt these before reading the
[solutions](./03-survey-procedures-solutions.md). The lesson is
[03 Survey Procedures: Loops, Drift, Repeatability and Ties](../03-survey-procedures.md).
All models are **SYNTHETIC**. Use $1\ \mathrm{\mu Gal} = 10^{-8}\
\mathrm{m\,s^{-2}}$ and the lesson's measured relations where they apply.

## ★ Foundational

**★1.** A SYNTHETIC base reads $+2.5\ \mathrm{\mu Gal}$ above its known value at
$t = 0$. A station read $0.50\ \mathrm{h}$ later shows $+14.0\ \mathrm{\mu Gal}$
above the same known value. With a drift rate of $12\ \mathrm{\mu Gal\,h^{-1}}$
known from the base occupations, compute the station's anomaly. State what you would
compute if the drift rate were not known.

**★2.** A closed loop has 8 readings with $2.0\ \mathrm{\mu Gal}$ of noise each.
Compute the expected closure rms, then state whether an observed closure of
$7.2\ \mathrm{\mu Gal}$ is consistent with it.

**★3.** Ten repeated occupations of one station give a standard deviation of
$2.5\ \mathrm{\mu Gal}$. Compute the standard error of the mean for 1, 4 and 25
repeats, and the number of repeats needed for a $0.5\ \mathrm{\mu Gal}$
repeatability.

## ★★ Applied

**★★4.** A drift step of $S\ \mathrm{\mu Gal}$ occurs inside a loop of duration
$T$ hours, and a single linear bracket is fitted. Derive the apparent drift-rate
error $S/T$ and evaluate it for (a) $S = 20$, $T = 2.0\ \mathrm{h}$ and (b)
$S = 40$, $T = 4.0\ \mathrm{h}$. State what the two cases have in common and what
that implies for detecting a step from a fitted rate alone.

**★★5.** A SYNTHETIC instrument drifts at $30\ \mathrm{\mu Gal\,h^{-1}}$ and the
survey target is $2\ \mathrm{\mu Gal}$. Using the lesson's SYNTHETIC model-error
fraction of $8\%$ of the accumulated drift, compute the maximum base-occupation
interval. Then compute it for a target of $5\ \mathrm{\mu Gal}$ and state how the
answer would change if the model-error fraction were $20\%$.

**★★6.** A survey's error budget is: absolute tie $4.0\ \mathrm{\mu Gal}$
(correlated), calibration scale $1.5\ \mathrm{\mu Gal}$ (correlated), drift model
$3.0\ \mathrm{\mu Gal}$ (partly correlated), reading noise $1.0\ \mathrm{\mu Gal}$
(independent). Compute (a) the total uncertainty of a station's *absolute* value and
(b) the total uncertainty of a *difference between two stations within the survey*,
stating which terms cancel and why the two answers differ.

## ★★★ Research-oriented

**★★★7.** Design a survey that claims $3\ \mathrm{\mu Gal}$ (1σ) per station over
$30\ \mathrm{km^{2}}$, using an instrument with $0.5\ \mathrm{\mu Gal}$ per-reading
noise and a specified drift rate that you choose. Specify the loop structure, the
base-occupation interval, the samples per station and the tie strategy; show the
budget; and state the two cheapest changes that would improve the result.

**★★★8.** Design the observation scheme and the statistical test that would let you
distinguish a gradual drift from a step using base occupations alone. Give the
minimum number of occupations, the test statistic, the false-alarm rate you accept,
and the sensitivity (smallest step detectable) as a function of the noise and the
number of occupations.

**★★★9.** A repeat survey occupies 15% of the stations two months later, with a
different instrument and a *different* absolute tie. Specify the analysis that
separates (i) a datum difference, (ii) a survey-wide error, and (iii) a
station-specific difference. State what each signature looks like on a map of the
differences.
