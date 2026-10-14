# Exercises — 05-05-04 Positioning with GNSS/DGPS and Static Corrections

Attempt these **closed-book** before opening the
[solutions](./04-positioning-gnss-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement: the free-air gradient derived as
$2g/a$ = 0.30785 mGal/m; vertical error → gravity error of 0.0092 (RTK, 0.03 m),
0.1539 (DGPS, 0.50 m) and 0.9236 mGal (autonomous, 3.00 m); maximum horizontal
gradient of a point-mass anomaly $0.8587\,g^{\max}/h$ at $x = h/2$; measured
gradients 0.00089, 0.00011, 0.00019 and 0.00019 mGal/m for the four synthetic
spheres; magnetic dipole gradients 2742.8, 33.9 and 0.3 nT/m at 10, 30 and 100 m.

Use $g = 9.80665\ \mathrm{m\,s^{-2}}$, $a = 6371$ km, $1\ \mathrm{mGal} = 10^{-5}$
m/s², $\mu_0/4\pi = 10^{-7}$ exactly.

---

## ★ Foundational

**★1.** Derive $\mathrm{d}g/\mathrm{d}z = -2g/a$ from Newton's law, and evaluate it
for $g = 9.80665$ and $a = 6371$ km. Give the answer in mGal/m and in s⁻².

---

**★2.** A station height is in error by (a) 0.01 m, (b) 0.5 m, (c) 5 m. Convert
each to a gravity error in mGal.

---

**★3.** State the relation between ellipsoidal height, orthometric height and the
geoid undulation, and state which of the three a GNSS receiver measures directly.

---

**★4.** A point-mass anomaly has a peak of 0.20 mGal at 400 m depth. Compute its
maximum horizontal gradient.

---

**★5.** State one positioning error that averages out with repeated occupations and
one that does not, and explain the difference in one sentence.

---

## ★★ Applied

**★★6.** A survey targets 0.08 mGal anomalies and allows 20 % of that for
positioning.

(a) What vertical accuracy is required?
(b) What horizontal accuracy is required, for a body at 500 m depth with a peak of
0.08 mGal?
(c) Which requirement binds, and by roughly what factor?

---

**★★7.** A microgravity monitoring survey re-occupies the same stations every
month. The 4-D signal is 0.015 mGal. The stations are monuments whose positions are
re-occupied to 5 mm horizontally and 2 mm vertically.

(a) Compute the vertical positioning contribution.
(b) Compute the horizontal contribution for a body at 100 m depth with a 0.5 mGal
peak.
(c) Which term dominates the 4-D error budget, and what does that imply about
survey design?

---

**★★8.** A magnetic survey over a shallow dyke records gradients of 50 nT/m.

(a) What horizontal positioning accuracy keeps the positioning contribution below
2 nT?
(b) State whether RTK or DGPS suffices.
(c) If the pole height is measured to ±1 cm, what is the gravity-equivalent error,
and does it matter for a *magnetic* survey?

---

**★★9.** A gravity survey is positioned with autonomous GNSS (assumed 3 m vertical).
The measured noise budget reports a repeatability of 0.02 mGal from repeated
occupations of one station.

(a) Explain how both statements can be true.
(b) Compute the survey's real anomaly threshold.
(c) What single field procedure would have revealed the problem?

---

## ★★★ Research-oriented

**★★★10.** Derive the *quadratic* term in the Taylor expansion of the anomaly about
a mislocated position and show that the linear estimate of equation (1) of the lesson
is a lower bound on the error. Estimate the displacement at which the quadratic term
reaches 10 % of the linear term, for a body at depth $h$.

---

**★★★11.** Design a numerical experiment that measures the effect of a *spatially
correlated* horizontal positioning error (a random walk along a profile, rather than
independent jitter) on a synthetic anomaly profile. Report how the correlation length
changes the error's appearance in the map, and state why this failure mode is more
dangerous than uncorrelated noise.

---

**★★★12.** A survey's positioning is a mix of a constant vertical bias
$\delta z_0$, a random per-station error $\eta_i$, and a long-wavelength tilt in the
height field. Construct a synthetic example, reduce the data with each error present
and absent, and report the anomaly error map for each. State which of the three
cannot be detected by any amount of repeating, and how a base station would detect
it.
