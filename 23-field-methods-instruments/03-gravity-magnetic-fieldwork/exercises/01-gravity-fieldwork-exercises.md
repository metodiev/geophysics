# Exercises — 23-03-01 Gravity Fieldwork: Loops, Drift, Base Stations, Ties

Attempt these before reading the
[solutions](./01-gravity-fieldwork-solutions.md). The lesson is
[01 Gravity Fieldwork](../01-gravity-fieldwork.md). All values are **SYNTHETIC**.
Free-air gradient: $0.3086\ \mathrm{mGal/m}$.

## ★ Foundational

**★1.** A gravimeter drifts linearly at $0.012\ \mathrm{mGal/h}$ and a loop lasts
4 h. Compute the drift accumulated over the loop and the correction that a two-tie
linear drift correction applies to a station read 2.5 h into the loop. State the
unit of each quantity.

**★2.** A loop's base readings are 1000.000 mGal at the start and 1000.150 mGal at
the end, 3 h later. Compute the closure error. State whether it is consistent with
the drift and tide of the lesson's model, and give two other causes a closure error
of that size could indicate.

## ★★ Applied

**★★3.** Ten repeats of one station give a standard deviation of
$0.004\ \mathrm{mGal}$. Compute the standard error of a three-reading station
value, the 95 % repeatability of a single reading for $n = 10$ (use 2.23 as the
coverage factor), and the free-air equivalent in metres of the standard error.

**★★4.** A tidal term has amplitude $0.08\ \mathrm{mGal}$ and period
$12.4\ \mathrm{h}$. Using the lesson's residual table for $A = 0.10\ \mathrm{mGal}$
(scaled by $0.08/0.10$), compute the worst-case linear-fit residual for intervals
of 2 h and 4 h, and state the longest interval that keeps the residual below
$0.01\ \mathrm{mGal}$.

## ★★★ Research-oriented

**★★★5.** Design a looping schedule for a microgravity survey with a target
accuracy of $0.01\ \mathrm{mGal}$: state the drift rate and tidal amplitude you
would assume and how you would measure them, the loop duration, the number of base
ties, the number of stations per loop given 8 minutes of measurement and 6 minutes
of travel per station, and the check that decides whether the day's data are
acceptable. Show the arithmetic.

**★★★6.** Specify an experiment that would detect an unstable base station:
state the measurement, the frequency of occupation, the metric with units, the
duration needed to detect a drift of $0.02\ \mathrm{mGal}$ per month, and two
things the experiment cannot distinguish. A specification that could not be
executed with a gravimeter and a vehicle is a failed answer.
