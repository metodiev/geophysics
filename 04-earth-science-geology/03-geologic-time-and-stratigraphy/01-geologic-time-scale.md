---
id: 04-03-01
title: "The Geologic Time Scale and Deep Time"
level: beginner
prereqs: ["04-02-01"]
estimated_minutes: 75
tags: [geologic-time, time-scale, gssp, deep-time, stratigraphy]
---

# The Geologic Time Scale and Deep Time

Deep time is not a large number. It is a number so far outside the range that
human intuition calibrates against that the intuition does not degrade
gracefully — it fails completely, and it fails silently. A student who can recite
that the Earth is about 4.5 billion years old still cannot say whether a
particular event was early or late in that history, because there is no
experience to attach the quantity to.

So this lesson does two things. It builds the **arithmetic of deep time**, so
that statements about it can be checked rather than felt. And it describes the
**time scale itself** — not as a table of numbers to memorise, but as a nested
hierarchy of names whose boundaries are *defined* at specified reference points
in specified rock sections, and whose *ages* are assigned by measurements and
revised as the measurements improve. That distinction between definition and
number is the single most useful thing to take from this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compress** an anchor age onto human scales (a day, a calendar year, a
   walked metre) and explain why every such graphic is only as good as the input
   age and the compression it chose.
2. **Reason in ratios** rather than in differences about deep time, and state
   why a linear axis cannot display the Phanerozoic and the Precambrian together
   with any resolution in the younger part.
3. **Propagate** uncertainty through a *duration*, which is a difference of two
   ages, and explain why a duration can be far better determined than either age
   and why a rate is worse determined still.
4. **Describe** the hierarchy of eon, era, period, epoch and age, and name the
   Phanerozoic periods without attaching boundary ages to them.
5. **Distinguish** a GSSP from a GSSA, and explain why a boundary is defined at
   a physical point in a rock section rather than by a number of years.
6. **State** the discipline this module imposes on numbers: boundary ages come
   from a dated version of an authoritative chart, and tabulated anchors carry
   their uncertainty and their compilation.

## Prerequisites

- [04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail](../02-plate-tectonics/01-tectonic-theory.md)
  — the historical and tectonic frame in which the time scale was built and is
  still being refined.
- The decay law is not derived here; where this lesson needs it, it points to
  [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md).

## 1. The problem with the number

Take an anchor age: the age of the Earth is commonly quoted as
$4.54 \times 10^9$ a, with an uncertainty of order $5 \times 10^7$ a in that
quoting, that is, about one per cent. These are tabulated values from a
compilation, not facts of nature, and a serious statement of them carries the
reference. But suppose you accept them for the moment. What does one per cent
mean here?

It means $4.5 \times 10^7$ a. That is 45 million years — an interval long enough
to hold the entire Cenozoic, an interval that no human measurement can
comprehend as an error bar. **The uncertainty on the number is itself larger than
any time interval a person can picture.** That is the first reason deep time
resists intuition: it is not that the number is big, it is that even its error
bar is big.

The second reason is the resolution of a linear axis. Suppose you draw Earth
history as a bar 4.54 m long, one metre per billion years, which is about the
width of a doorway. Then one millimetre of the bar is

$$\frac{4.54 \times 10^9 \text{ a}}{4540 \text{ mm}} = 1.0 \times 10^6 \text{ a}
= 1 \text{ Ma}. \tag{1}$$

All of recorded history, call it $5 \times 10^3$ a, occupies

$$5 \times 10^3 \text{ a} \times \frac{4540 \text{ mm}}{4.54 \times 10^9 \text{
a}} = 5.0 \times 10^{-3} \text{ mm} = 5 \text{ µm}, \tag{2}$$

which is a fifth of the width of a printed line. On a linear axis that can show
the whole planet, the whole of human history is not merely small: it is beneath
the resolution of the drawing. This is why every serious deep-time figure uses a
logarithmic axis, or compresses the recent past into a separate inset, or abandons
proportionality altogether and lists durations. The demo computes exactly these
numbers; its output is quoted in §7.

## 2. Reasoning in ratios

Because differences are useless at this scale, comparisons have to be
multiplicative. The question "how much longer" is answerable; "how much longer
in years" is not meaningful without a division.

The working rule is: **divide, then take a logarithm, then interpret the
logarithm as an order of magnitude.** A human lifetime of 80 a inside
$4.54 \times 10^9$ a gives a ratio of $5.7 \times 10^7$, or 7.75 orders of
magnitude. Recorded history of about $5 \times 10^3$ a gives $9.1 \times 10^5$,
or 5.96 orders of magnitude. Those two logarithms differ by 1.8, which is a
factor of about 60: a human lifetime and the whole of written history are closer
to each other, in logarithmic terms, than written history is to the age of the
Earth. That is a statement you can verify with two divisions, and it is the kind
of statement that survives the failure of intuition.

## 3. What the time scale actually is

The geologic time scale is a **hierarchy of names**. From largest to smallest:
eon, era, period, epoch, age (also called chron). The names nest: the
Phanerozoic eon contains the Paleozoic, Mesozoic and Cenozoic eras; the Paleozoic
contains the Cambrian, Ordovician, Silurian, Devonian, Carboniferous and Permian
periods; the Cenozoic contains the Paleogene, Neogene and Quaternary. The names
are stable and they are what geological communication is actually built on — a
phrase such as "the Cretaceous" is unambiguous internationally and always has
been.

What is *not* stable is the set of ages attached to the boundaries. Two things
about that deserve separate statements.

**Boundaries are defined, not measured.** A boundary between two units is
defined by a **Global Boundary Stratotype Section and Point (GSSP)**: a specific
level in a specific, accessible rock section, chosen by an international working
group, marked physically with a permanent marker, and ratified by the
International Union of Geological Sciences. The boundary is *that level*. It is
not "541 million years ago"; it is a place in the rock. The age in years is a
property of the GSSP that is then measured as well as the measurement can manage.
Older parts of the time scale, where suitable sections are rare, use a **Global
Standard Stratigraphic Age (GSSA)**: a boundary defined *by a number*, agreed by
vote, precisely because no section can serve. Both mechanisms exist and they
exist for the same reason: an international community needs a boundary that
cannot drift when somebody remeasures it.

**Ages are assigned to boundaries by dating.** The usual route is a
high-precision U–Pb zircon age from an ash bed that lies as close as possible to
the boundary level, with the agreement between the boundary and the dated horizon
assessed separately. Each revision of the chart moves some ages by amounts larger
than their quoted uncertainties, because the revisions come from changed decay
constants, changed interlaboratory calibration and changed stratigraphic
correlations — not only from better measurements of the same thing. This is the
reason this module does not print boundary ages: **an age printed here would be an
age of a specific version of the chart, and it would go stale.**

The authoritative chart is published and periodically revised by the
International Commission on Stratigraphy, a body of the International Union of
Geological Sciences; the current version, its version number and its date are
obtained from the Commission. The [United States Geological Survey](https://www.usgs.gov)
and other national surveys publish derived versions and explanatory material.
Draw the hierarchy from any of them; draw the numbers from the one you cite.

## 4. Anchors, and the discipline for quoting them

Some numbers in this module cannot be avoided, because the arithmetic needs a
magnitude. They are called **anchors** and they are used as follows.

- Every anchor is labelled as a commonly tabulated value, and printed with an
  uncertainty.
- The compilation is cited by the user. The values below are the kind of number
  that appears in a reference work; they are not a measurement performed here.
- Anchors are used for orders of magnitude and for ratio arithmetic. No
  conclusion in this module depends on an anchor's last digit.

The anchors the demo uses are the age of the oldest Solar System solids
(commonly quoted near $4.57 \times 10^9$ a with an uncertainty of order
$10^6$ a), the age of the Earth (commonly quoted near $4.54 \times 10^9$ a with
an uncertainty of order $5 \times 10^7$ a) and the age of the Universe (commonly
quoted near $1.38 \times 10^{10}$ a with an uncertainty of order $2 \times 10^7$
a). Their relative uncertainties differ by two orders of magnitude, which is
itself instructive: the meteorite isochron that fixes the first is far more
precise than the accretion models that bracket the second.

## 5. Durations, rates, and where the uncertainty actually goes

A duration is the difference of two ages:

$$\Delta t = t_2 - t_1, \qquad \sigma_{\Delta t}^2 = \sigma_1^2 + \sigma_2^2 -
2\rho\sigma_1\sigma_2, \tag{3}$$

with $\rho$ the correlation between the two age determinations. Equation (3) is
the whole of the uncertainty analysis of a duration, and it has a consequence
that surprises people. If the two ages were determined from the *same* decay
constant calibration and the *same* interlaboratory standard — which is what
happens when one laboratory dates both boundaries — then $\rho$ is close to 1,
and the errors partially cancel. A pair of ages each known to one per cent can
define a duration known to much better than one per cent.

The demo makes the arithmetic concrete for a synthetic pair of boundaries at
400 Ma and 500 Ma with independent one-sigma uncertainties of 5 Ma each. The
duration is 100 Ma, and its uncertainty is 7.07 Ma if the errors are independent,
3.54 Ma if $\rho = 0.75$, and zero if they are perfectly correlated. Those three
numbers are the same data set under three different statements about correlation,
and the spread from 7 per cent to 0 per cent is the spread between a careless and
a careful reporting of the same measurement.

Now pass to a rate: sedimentation rate, subsidence rate, cooling rate. A rate is
a difference divided by a difference, so it inherits both uncertainties, and if
either difference is small the relative uncertainty of the rate is large. This is
why geological rates are quoted as inequalities as often as equalities, and why
the intervals chosen for a rate calculation matter more than the arithmetic.

## 6. Reading a time scale without being misled

Three habits make a time scale legible.

**Never add linear extrapolation to it.** The Phanerozoic occupies about 12 per
cent of Earth history in most current charts; the Precambrian occupies the rest,
and the Precambrian itself is not uniform in character. Any sentence of the form
"and then, for the first 88 per cent of Earth history, …" is hiding four eons of
structurally different history behind a single clause.

**Ask what the boundary is defined by.** If the answer is a GSSP, the boundary is
a level in a section and its age in years can be improved by measurement. If the
answer is a GSSA, the boundary is a number and its age cannot change without a
community vote. The distinction predicts which boundaries move between chart
versions and which do not.

**Ask which chart.** Every figure, every correlation and every rate that uses a
boundary age inherits the chart version. A correlation that is robust to a
hundred-thousand-year change in a boundary is a stronger statement than one that
is not, and only a reader who knows the chart version can tell them apart.

## 7. Python demonstration

[`code/01-deep_time_demo.py`](./code/01-deep_time_demo.py) computes the
compression arithmetic, the ratio arithmetic, the duration uncertainty and the
axis resolution. It asserts no boundary age: every anchor is labelled TABULATED
and printed with its uncertainty.

The anchors and their uncertainties:

```text
anchor                                        age (a)      +/- (a)   rel. unc.
Earth (oldest Solar System solids)         4.5670e+09     1.00e+06       0.02%
Earth (accretion/age of the planet)        4.5400e+09     5.00e+07       1.10%
Universe (cosmic microwave background)     1.3800e+10     2.00e+07       0.14%
```

Note that the relative uncertainty on the meteorite anchor is 0.02 per cent and
on the accretion anchor 1.10 per cent, a factor of 55: these are different kinds
of number and quoting them to the same precision would be a category error.

The compression, which is the arithmetic behind every "Earth history in a day"
graphic:

```text
  On the 24 h clock, 1 Ma of Earth history is 19.03 s.
  1 h of that clock is 1.892e+08 a = 189.17 Ma of Earth history.
  1 min of that clock is 3.153e+06 a = 3.15 Ma of Earth history.
  1 s of that clock is 5.255e+04 a.
  On the calendar-year compression, 1 Ma of Earth history is 6951.01 s; 1 day of that calendar is 12.43 Ma of Earth history.
```

The calendar-year line is worth reading twice: on that compression, **one day is
12.4 Ma**. A graphic of this kind is a legitimate teaching device and a terrible
basis for quantitative reasoning, because the compressions differ (a day, a
year, 100 m) and each one flattens a different part of the record.

The ratio arithmetic:

```text
interval                       length (a)    count in Earth age     log10
  recorded history (writing)   5.0000e+03            9.0800e+05      5.96
  a human lifetime             8.0000e+01            5.6750e+07      7.75
  one century                  1.0000e+02            4.5400e+07      7.66
  one million years            1.0000e+06            4.5400e+03      3.66
```

The duration uncertainty, with all three correlation assumptions computed:

```text
    top of interval  t1 = 4.0e+08 a +/- 5.0e+06 a
    base of interval t2 = 5.0e+08 a +/- 5.0e+06 a
    duration            = 1.0e+08 a

error model                          sigma(duration) (a)    relative
  independent (rho = 0)                       7.0711e+06       7.07%
  correlated, rho = 0.75                      3.5355e+06       3.54%
  fully correlated (rho = 1)                  0.0000e+00       0.00%
```

And the resolution of the linear axis, which is the geometric statement of §1:

```text
  A 1 m linear bar for the Earth age: 1 mm = 4.540e+06 a = 4.54 Ma
  On a 4.54 m bar, all of recorded history (5000 a) occupies 0.0050 mm = 5.000 micrometres.
  A printed line is about 0.1 mm wide, i.e. 1.000e+05 a of Earth history -- roughly 0.10 Ma.
```

The demo finishes with the hierarchy of names and the count of levels, with no
ages attached to any of them:

```text
  eons: 4 -> Hadean, Archean, Proterozoic, Phanerozoic
  eras of the Phanerozoic eon: 3 -> Paleozoic, Mesozoic, Cenozoic
    periods of the Paleozoic :  6 -> Cambrian, Ordovician, Silurian, Devonian, Carboniferous, Permian
    periods of the Mesozoic  :  3 -> Triassic, Jurassic, Cretaceous
    periods of the Cenozoic  :  3 -> Paleogene, Neogene, Quaternary
```

## 8. Common mistakes

1. **Quoting a boundary age as a fact.** It is an entry in a dated version of a
   chart. If the version is not stated, the number cannot be checked.
2. **Treating the uncertainty on an anchor as negligible** because it is "only
   one per cent". One per cent of $4.54 \times 10^9$ a is 45 Ma.
3. **Adding or subtracting ages before thinking about correlation.** Equation (3)
   gives three different answers for the same data.
4. **Reporting a rate without reporting the interval it was computed over.** A
   rate over 1 Ma and a rate over 100 Ma are different quantities with the same
   units.
5. **Reading a compressed timescale graphic quantitatively.** A "day", a
   "calendar year" and a "100 m walk" compress differently and each misleadingly
   in a different region.
6. **Assuming the hierarchy of names is also a hierarchy of durations.** Periods
   differ in length by more than a factor of ten, and the names carry no duration
   information at all.
7. **Forgetting that the Precambrian is most of the record.** A sentence that
   treats it as prologue discards the majority of the evidence.
8. **Confusing a GSSP with a date.** One is a physical marker in a rock section;
   the other is a measurement, revised as measurements improve.

## 9. Real-world applications

- **Correlation across a basin.** Two wells are correlated by the names on the
  chart, and the ages attached to those names let a subsidence history be built
  ([04](./04-sedimentary-basins.md)) — with the chart version recorded, because
  the numbers move.
- **Petroleum and mineral exploration.** Play fairways, source-rock maturity and
  reservoir quality are all framed in time-scale terms, and the age of a
  boundary decides whether a source rock had time to mature
  ([04-06-01](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Palaeoclimate.** A carbon-isotope excursion or a sea-level curve is only a
  global statement once its age is fixed against the chart, and the error bar on
  that age is often the limiting uncertainty in the correlation.
- **Hazard assessment.** Recurrence intervals for large earthquakes are built
  from dated events, and the duration between them is a difference of two ages —
  so its uncertainty is governed by equation (3), not by the precision of either
  age alone.
- **Planetary science.** Other bodies have their own time scales, defined by
  crater-density chronologies rather than by GSSPs, and the contrast with the
  Earth's mechanism is instructive
  ([04-08-01](../08-planetary-science/01-solar-system.md)).

## 10. Further reading

- **Gradstein, F. M., Ogg, J. G., Schmitz, M. D., & Ogg, G. M. (eds),
  *Geologic Time Scale 2020* (Elsevier).** The reference work behind the modern
  chart: the hierarchy, every boundary's definition, the radioisotopic
  calibration and the reasoning behind each revision. Level: reference.
- **International Commission on Stratigraphy, *International
  Chronostratigraphic Chart* (current version).** The authoritative chart itself,
  with its version number and date. Obtain the current version from the
  Commission; record the version whenever you use an age from it. Level:
  reference.
- **International Union of Geological Sciences, *Ratification procedure for
  GSSPs*.** The rules that make a boundary a defined place in the rock rather
  than a number. Level: reference.
- **Tucker, M. E. *Sedimentary Petrology* (Wiley-Blackwell).** The stratigraphic
  setting in which the time scale is read and used. Level: beginner to
  intermediate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  For the thermal and physical processes whose rates the time scale is used to
  measure. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md)
  — the deductive system that orders events without any numbers.
- [03 Radiometric Dating Methods and Their Assumptions](./03-radiometric-dating.md)
  — how the ages on the chart are obtained and what they assume.
- [04 Sedimentary Basins: Formation, Fill and Subsidence](./04-sedimentary-basins.md)
  — the archive in which the record is preserved.
- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md)
  — the decay law and the isochron, derived rather than quoted.
- [04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail](../02-plate-tectonics/01-tectonic-theory.md)
  — the historical episode in which the time scale was extended beyond the
  Phanerozoic.
- [26-02-02 Units Handbook, Conversions and Preferred Conventions](../../26-reference-library/02-symbols-and-units/02-units-handbook.md)
  — the year, the Ma and the convention for writing them.

Exercises:
[`exercises/01-geologic-time-scale-exercises.md`](./exercises/01-geologic-time-scale-exercises.md)
and
[`exercises/01-geologic-time-scale-solutions.md`](./exercises/01-geologic-time-scale-solutions.md).

## Self-assessment checklist

- [ ] I can compress an anchor age onto a 24-hour clock and onto a metre, and
      state what each compression hides. (§1, §7)
- [ ] I can compute the ratio and its logarithm for any interval inside an
      anchor age, and interpret the logarithm as an order of magnitude. (§2, §7)
- [ ] I can write down the propagation of uncertainty for a difference and say
      what changes when the errors are correlated. (§5, §7)
- [ ] I can list the hierarchy of the time scale and name the Phanerozoic
      periods. (§3, §7)
- [ ] I can explain what a GSSP is, why a boundary is defined at one, and when a
      GSSA is used instead. (§3)
- [ ] I can state why this module does not print boundary ages, and what a
      reader needs in order to check a quoted one. (§3, §4)
- [ ] I can explain why a linear time axis cannot display deep time with any
      resolution in the recent past. (§1, §7)
- [ ] I can state three habits that make a published time scale figure legible.
      (§6)
