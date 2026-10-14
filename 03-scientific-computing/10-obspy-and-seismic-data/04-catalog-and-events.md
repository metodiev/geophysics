---
id: 03-10-04
title: "Event Catalogs, QuakeML and Phase Metadata"
level: intermediate
prereqs: ["03-10-01", "03-10-02"]
tags: [obspy, quakeml, catalogs, magnitudes, geodesy]
---

# Event Catalogs, QuakeML and Phase Metadata

A waveform tells you that the ground moved. A catalog tells you when, where,
how big, and how well anyone knows. The two are joined by the **origin** — a
hypocentre and an origin time — and by **arrivals** and **picks** that connect
the origin to specific phases on specific channels. This lesson covers the
`Catalog` object, the QuakeML format it is exchanged in, and the geodesy that
converts between the degrees that travel-time routines want and the metres that
catalogues store.

Run the demonstration before reading on.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/catalog_and_events_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** an event with an origin, a magnitude and picks, and **write** it
   as QuakeML and read it back.
2. **State** the units of every field in an origin — latitude and longitude in
   degrees, depth in metres, times as `UTCDateTime` — and identify the
   thousand-fold trap.
3. **Carry** uncertainties through a catalog record and explain what a
   90 % confidence level means for a location.
4. **Convert** between angular distance, great-circle distance on the WGS84
   ellipsoid, and spherical mean-radius distance, and quantify the difference.
5. **Convert** between $M_L$, $m_b$ and $M_w$ and explain why averaging
   magnitude scales is meaningless.
6. **Use** the Gutenberg–Richter relation to reason about catalog
   completeness.

## Prerequisites

- [03-10-01 ObsPy Architecture and Data Models](./01-obspy-overview.md) —
  `UTCDateTime`.
- [03-10-02 Reading MiniSEED/SAC](./02-reading-waveforms.md) — the waveform
  side of the same event.

## 1. Intuition: a catalog is a set of claims

A hypocentre is not a measurement of a point in the Earth. It is the output of
an inversion, and like every inversion it comes with a resolution and a
null space. The catalog format therefore carries, for each quantity, both a
value and an uncertainty, and the honest reader treats the value as
meaningless without the uncertainty. QuakeML — the XML schema for earthquake
catalogs — encodes both.

The demonstration reports, for a synthetic local event,

```
time error                    : 0.0500 s
latitude error (90% conf.)    : 1.1000 deg
depth error                   : 2.0 m
1 deg of latitude             : 111.195 km
so 1.1 deg is                 : 122.3 km
```

A latitude uncertainty of 1.1° is 122 km: this is a regional location at best,
whatever the origin's latitude is printed to. The *value* is 48.1043°; the
*meaning* is "somewhere inside a 122 km circle". A catalog that stripped the
uncertainty would turn the second into the first.

## 2. Precise definitions

### 2.1 The object hierarchy

```
Catalog
└── Event
    ├── Origin        (time, latitude, longitude, depth, uncertainties, method)
    │   └── Arrival   (phase name, pick reference, residual, distance, azimuth)
    ├── Pick          (time, phase hint, waveform id, onset quality)
    ├── Magnitude     (value, type, station count)
    └── FocalMechanism
```

The demonstration's catalog contains one event with one origin, three picks
and three arrivals. Quantities and units:

| Field | Type | Unit |
|---|---|---|
| `origin.time` | `UTCDateTime` | UTC instant |
| `origin.latitude`, `origin.longitude` | float | degrees, −90..90 and −180..180 |
| `origin.depth` | float | **metres** |
| `magnitude.mag` | float | dimensionless |
| `arrival.time_residual` | float | seconds |
| `arrival.distance` | float | degrees (per QuakeML convention) |
| `arrival.azimuth` | float | degrees clockwise from north |
| `pick.time` | `UTCDateTime` | UTC instant |

The depth unit is the single most consequential detail in the table:
`depth=11500.0` in QuakeML means 11.5 km. A code path that treats it as
kilometres puts the event 11 500 km deep, which silently removes it from every
depth-filtered selection and produces a location plot that looks like a
mistake in the colour bar.

### 2.2 Precision and confidence levels

`QuantityError(uncertainty=1.1, confidence_level=90.0)` means: the 90 %
confidence interval half-width is 1.1°. Two things follow.

- **An uncertainty without a confidence level is not a number you can use.**
  A 1σ statement and a 90 % statement differ by a factor of 1.64 for a normal
  distribution.
- **Uncertainties are correlated across fields.** A poorly constrained depth
  and a poorly constrained origin time trade off against each other in a
  location inversion; quoting them independently is a simplification that the
  `Origin` object permits but does not endorse.

### 2.3 Magnitude scales are different measurements

| Scale | Measured from | Period band | Saturates near |
|---|---|---|---|
| $M_L$ (local/Richter) | peak amplitude on a Wood–Anderson-equivalent instrument | ~1 Hz | 6–7 |
| $m_b$ (body wave) | P-wave amplitude in the first few seconds | ~1 Hz | 6–7 |
| $M_s$ (surface wave) | Rayleigh amplitude at 20 s | 0.05 Hz | 8 |
| $M_w$ (moment) | seismic moment from the source spectrum | broadband | no |

They agree near their calibration range and diverge outside it. The
demonstration computes

```
seismic moment M0             : 1.000e+18 N m
Mw = (log10 M0 - 9.1)/1.5     : 5.9333
reported ML                   : 3.8400
difference Mw - ML            : +2.0933 magnitude units
energy ratio Mw vs ML         : 1380.384
```

Two magnitude estimates of the same event differ by a factor of 1380 in
radiated energy. Neither is wrong; they are different measurements, and the
one you quote must be named.

## 3. Derivations and worked reasoning

### 3.1 The moment-magnitude relation

Kanamori's relation is

$$M_w = \frac{\log_{10} M_0 - 9.1}{1.5}, \qquad [M_0] = \mathrm{N\,m},$$

which is dimensionless by construction: the logarithm of a dimensional quantity
is only defined if the reference value is stated, and here it is $1\ \mathrm{N\,m}$.
Inverting on the demonstration's numbers:
$\log_{10} M_0 = 1.5 \times 5.9333 + 9.1 = 18.0$, so $M_0 = 10^{18}$ N·m.

The energy relation is separate:

$$\log_{10} E = 1.5 M_s + 4.8, \qquad [E] = \mathrm{J},$$

so one unit of magnitude is $10^{1.5} = 31.62$ times the energy — which the
demonstration prints as 31.6228 for the moment and, using the same slope for
energy, 177.8279 for the 1.5-unit difference. The energy ratio for the
2.0933-unit difference between $M_w$ and $M_L$ is
$10^{1.5 \times 2.0933} = 1380.4$: two descriptions of one event that differ by
three orders of magnitude in a physically meaningful quantity.

### 3.2 Three kinds of distance

The demonstration measures, between an event at 48.1043° N, 11.2058° E and a
station at 48.95° N, 11.60° E:

```
angular distance              : 0.885075 deg
great-circle distance (WGS84) : 98.4461 km
spherical mean-radius convert : 98.4158 km
difference WGS84 vs sphere    : 0.0303 km (+0.0003 relative)
```

- `locations2degrees` uses a spherical Earth and returns **degrees** — the
  input every travel-time routine wants.
- `gps2dist_azimuth` uses the **WGS84 ellipsoid** (a Vincenty inverse
  solution) and returns **metres**, plus the azimuth and back-azimuth.
- `degrees2kilometers` multiplies by $\pi R/180$ with $R = 6371$ km, giving
  $111.195$ km per degree.

The relative difference here is $3\times10^{-4}$, i.e. 30 m in 98 km. At
regional distances that is negligible for phase identification and
significant for geodesy. The demonstration's printed warning is the useful
form of the statement: a 0.3 % radius difference is about 5 s of P travel time
at 100 km, so a catalog that mixes ellipsoidal and spherical distances will
show systematic residuals that look like a velocity-model problem.

### 3.3 Uncertainty propagation into a depth

The origin's depth error is 2.0 m and the depth itself 11 500 m, a relative
uncertainty of 0.017 %. That is implausibly small for a local event and is a
good illustration of a real hazard: a reported error is only as good as the
error model behind it. If the inversion assumed picking errors of 0.01 s and
stations at 100 km, the depth uncertainty it returns will be small and wrong.
The catalog stores what the inversion claimed, not what the data support. The
demonstration prints the fraction precisely so that the reader can judge
whether to believe it.

### 3.4 Gutenberg–Richter and completeness

$$\log_{10} N(\ge M) = a - bM.$$

The demonstration tabulates $N$ for $a = 4$, $b = 1$:

| $M$ | $N(\ge M)$ | spacing to the next 10× |
|---|---|---|
| 1 | 1000.0 | 0.001 |
| 2 | 100.0 | 0.010 |
| 3 | 10.0 | 0.100 |
| 4 | 1.0 | 1.000 |
| 5 | 0.1 | 10.000 |

With $b = 1$ each magnitude unit is a factor of 10 in event count. The
consequence for practice is that the **magnitude of completeness** $M_c$
controls everything: if a network detects only events above $M = 2.5$ and the
true distribution continues below, then every rate estimate extrapolated from
the catalog is an under-estimate of the seismicity rate. The standard test —
fitting $b$ to the largest events and checking where the observed count falls
below the extrapolation — is the subject of
[06-11-01 Earthquake Statistics](../../06-seismology/11-earthquake-statistics-and-hazard/README.md).

### 3.5 What survives a round trip

```
file size                     : 3260 bytes
origin time identical         : True
latitude identical            : True
depth identical               : True
magnitude identical           : True
pick phase hints              : ['P', 'P', 'S']
arrival residuals             : [0.12, -0.07, 0.31]
first pick minus origin time  : 2.655 s
```

Every field survives, including the residuals and the resource identifiers.
QuakeML is verbose — 3260 bytes for one event — and complete. The verbosity is
the price of carrying provenance: the file records which algorithm located the
event, which agency reported the magnitude, and which pick each arrival refers
to. That is what makes a catalog auditable years later.

## 3b. Worked examples

### 3b.1 Turning a depth error into a map

**Problem.** An origin has latitude 48.1043°, an east–west latitude uncertainty
of 1.1° at 90 % confidence, and the same uncertainty in longitude. What area
does that cover, and what does it imply about the interpretation?

1.1° of latitude is $1.1 \times 111.195 = 122.3$ km of north–south distance.
Because 1° of longitude at 48° N is $111.195\cos(48°) = 74.4$ km, the same 1.1°
covers $1.1 \times 74.4 = 81.8$ km east–west. The 90 % region is therefore an
ellipse with semi-axes roughly 61 km and 41 km — an area of

$$A \approx \pi \times 61 \times 41 = 7\,860\ \mathrm{km^2}.$$

Compare that with the depth: 11.5 km. **The horizontal uncertainty is 5–10 times
the depth of the event.** Any statement about the event's relationship to a
surface feature — a fault trace, a mapped basin, a geothermal field — must carry
that 7860 km² circle with it, and a map that shows a single dot without it is
misleading even though every number on it is correct.

### 3b.2 A magnitude that does not average

**Problem.** Three agencies report $M_L = 3.8$, $m_b = 4.2$ and $M_w = 5.9$ for
the same event. What is the event's magnitude?

The question has no answer as posed. Converting each to a common scale requires
a relation between scales, and those relations are empirical, valid over
restricted ranges, and have their own scatter. What can be said:

- Convert the moment magnitude to a moment: $M_0 = 10^{1.5M_w + 9.1} =
  10^{17.95} = 8.9\times10^{17}$ N·m.
- $M_L = 3.8$ and $m_b = 4.2$ are consistent with each other and *inconsistent*
  with $M_w = 5.9$: at the same event size, short-period scales (measured around
  1 Hz) sit 1.5–2 units below the moment scale when the source is a slow rupture
  or the event is deep. The 1.5-unit difference corresponds to a factor
  $10^{2.25} = 178$ in radiated energy — the difference between a felt event and
  a damaging one.

The correct report names the scale: "the event was $M_w$ 5.9; short-period
estimates were 1.5–2 units lower, consistent with a slow, deep source." Averaging
the three numbers to 4.6 would describe no physical quantity at all.

### 3b.3 Choosing a distance convention on purpose

**Problem.** A travel-time residual is 0.32 s at a station 98.4 km from the
event. Is the residual explained by the choice of distance convention?

From the measured numbers: the WGS84 great-circle distance is 98.4461 km and the
spherical mean-radius conversion gives 98.4158 km, a difference of 0.0303 km.
At a P slowness near the source of about $p = 0.16$ s/km (a typical upper-crustal
value), that distance difference is worth

$$0.0303\ \mathrm{km} \times 0.16\ \mathrm{s\,km^{-1}} = 0.0048\ \mathrm{s}.$$

So the convention difference accounts for 4.8 ms of the 320 ms residual — 1.5 % of
it. **The residual is not a convention artefact; it is real signal** (or a real
error), and the next question is whether it correlates with azimuth around the
event (location error) or with distance (velocity-model error).

Doing that arithmetic before asserting a cause is the difference between a
diagnosis and a guess, and it costs two lines.

### 3b.4 A catalog you can audit

**Problem.** Design the minimum catalog record for a study that will be
re-examined in five years.

Required per event:

- `resource_id` for the event, the origin, the magnitude and every pick;
- `time`, `latitude`, `longitude`, `depth` **with their uncertainties and the
  confidence level**;
- `method_id` (which algorithm), `creation_info.author` and `.agency_id`
  (which group, which analyst);
- `preferred_origin_id` and `preferred_magnitude_id`, so the choice is explicit
  rather than implied by ordering;
- the magnitude's `magnitude_type`;
- for every arrival, the `pick_id` it references and the residual that the
  location produced.

Every one of those fields survives a QuakeML round trip — measured: time,
latitude, depth and magnitude all compare identical, the phase hints and
residuals survive, and the file is 3260 bytes for one event with three picks.
**Verbosity is the price of auditability**, and 3 kB per event is not the
constraint: a million-event catalog is 3 GB, which is smaller than one hour of a
40-station array's raw data.

The field that most often goes missing in derived products is the confidence
level: `uncertainty=1.1` without `confidence_level=90` cannot be converted to a
σ, cannot be combined with another estimate, and cannot be compared with a
different study.

### 3b.5 A magnitude–energy budget that is 1400 times wrong

**Problem.** A report converts a catalog magnitude to energy using the
Gutenberg–Richter relation. The catalog lists ML 3.84 for an event whose moment
tensor inversion gives $M_0 = 10^{18}$ N·m. What is the error?

First, the moment magnitude from the moment:

$$M_{\mathrm{w}} = \tfrac{2}{3}\left(\log_{10}M_0 - 9.1\right)
= \tfrac{2}{3}(18 - 9.1) = 5.9333 .$$

Measured: 5.9333, against the reported ML 3.84 — a difference of 2.09 magnitude
units. Then the radiated energy scales as $E \propto 10^{1.5M}$, so

$$\frac{E(M_{\mathrm{w}})}{E(M_{\mathrm{L}})}
= 10^{1.5(5.9333 - 3.84)} = 1380.384 .$$

Measured: **1380.384**, i.e. the report's energy is smaller than the inversion's
by a factor of about 1380. The lesson is not that one of the two numbers is
wrong — ML and Mw measure different things and are *expected* to disagree for a
given event — but that **a magnitude must never be used in an energy formula
without its type**. ML was calibrated on a particular instrument response and
distance range and saturates; Mw is derived from the moment and does not.

The practical rule: store the magnitude type with the value, and refuse to
combine a magnitude of unknown type with a physical relation. If a scalar is
needed, recompute it from the moment tensor rather than converting an ML.

### 3b.6 The metre trap, and what survives a round trip

**Problem.** A catalog is exported to QuakeML and re-imported. What is preserved,
and what is the most likely error a reader will make?

Measured, for a single event: the file is **3260 bytes**, the depth is stored in
**metres** (11500.0 means 11.5 km), and the round trip preserves the origin time,
the coordinates, the depth, the magnitudes and the arrivals exactly.

The metre trap deserves the emphasis it gets in the demonstration: a reader who
assumes kilometres and multiplies nothing will place a 11.5 km event at
11 500 km — deeper than the centre of the Earth, and beyond the deepest
earthquake ever recorded (about 700 km). Two defences, both cheap:

1. **Assert the range.** A depth in the range $[0, 700\,000]$ m is physical; a
   value of $1.15\times10^{7}$ m is not. One range check catches the error
   immediately, whereas the wrong number propagates into maps, travel-time
   computations and magnitude corrections without complaint.
2. **Carry the unit in the variable name**, e.g. `depth_m`. It costs four
   characters and prevents the error for the life of the code.

What the round trip also tells you: metadata *is* preserved when the interchange
format is used properly, so a discrepancy between an export and its re-import is
a bug in the writing or reading code, not an inherent loss. Compare that with
MiniSEED, which measures a silent loss of `calib` (5.1e8 → 1.0). **Different
formats lose different things; the test is to write, read back, and compare,
not to read the documentation.**

## 4. Physical and computational interpretation

A catalog is a *derived* product, and its design reflects that:

- **Resource identifiers** make every claim referenceable. An arrival points to
  a pick by ID, so a revised pick does not silently change the arrival's
  meaning.
- **Preferred-object pointers** (`preferred_origin_id`,
  `preferred_magnitude_id`) make the analyst's choice explicit. An event may
  carry five origins from five agencies; the catalog says which one it prefers
  and leaves the others available.
- **Creation information** (author, agency, software) is part of the record,
  which is unusual in scientific data formats and essential in a discipline
  where the same event is routinely located five times by five groups.

## 5. Python demonstration

[`code/catalog_and_events_demo.py`](./code/catalog_and_events_demo.py) builds
the catalog, round-trips it through QuakeML, measures the geodesy three ways,
converts magnitudes, tabulates Gutenberg–Richter and runs seven consistency
checks. It writes its scratch file into `code/_scratch_catalog/` and removes
it on exit.

## 6. Exercises

Full solutions:
[`exercises/04-catalog-and-events-solutions.md`](./exercises/04-catalog-and-events-solutions.md).

### ★ Foundational

**★1.** State the units of `origin.depth`, `origin.latitude`,
`arrival.distance` and `magnitude.mag` in QuakeML.

**★2.** An origin has `depth = 8000.0`. Give its depth in kilometres and
explain what a reader who assumed kilometres would infer.

**★3.** Using $M_w = (\log_{10} M_0 - 9.1)/1.5$, compute $M_w$ for
$M_0 = 3.2\times10^{19}$ N·m.

**★4.** Convert the angular distance 0.885075° to kilometres using the
spherical rule of thumb, and compare with the measured WGS84 value of
98.4461 km.

### ★★ Applied

**★★5.** From the measured magnitudes, compute the energy ratio implied by a
2.0933-unit difference using $\log_{10}E = 1.5M + 4.8$, and reconcile it with
the printed 1380.384.

**★★6.** Build an event with two origins from different methods and set the
preferred one. Write it to QuakeML, read it back, and verify that both origins
survive and that the preference is preserved. Report the file size.

**★★7.** The latitude uncertainty is 1.1° at 90 % confidence. Convert it to a
1σ uncertainty, state the conversion factor, and explain why the conversion is
only valid under a normality assumption.

**★★8.** An arrival has `time_residual = 0.31 s` for an S phase at 30°
distance. Compute the implied perturbation to the travel time as a percentage
and state whether the residual is more likely to indicate a source location
error or a velocity-model error, giving your reasoning.

### ★★★ Research-oriented

**★★★9.** Write a function that takes a `Catalog` and reports, for every
event, whether the origin's uncertainty ellipse is consistent with the station
geometry: specifically, whether the largest station–event distance is smaller
than the location uncertainty converted to kilometres. Apply it to a catalog
you build with both a tight and a loose uncertainty and report which flags.

**★★★10.** Compare the three distance conventions on a 5000 km baseline and
report the relative difference in metres. Then estimate the effect of that
difference on the P travel time at that distance, using
$p = \mathrm{d}T/\mathrm{d}\Delta \approx 5$ s/deg, and state whether a
catalog that mixes conventions can produce a systematic mislocation of more
than one kilometre.
