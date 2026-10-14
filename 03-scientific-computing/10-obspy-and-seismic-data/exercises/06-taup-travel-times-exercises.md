# Exercises — 03-10-06 Travel Times with TauP and Phase Naming

Attempt these **closed-book** before opening the
[solutions](./06-taup-travel-times-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first; several answers require its printed values:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/taup_travel_times_demo.py
```

---

## ★ Foundational

**★1.** Give the depth of the Moho, the core–mantle boundary and the inner-core
boundary in iasp91, and the model radius.

**★2.** Expand `PKIKP`, `SKS`, `PcP` and `Pdiff` into their legs and state which
one demonstrates that the outer core is liquid.

**★3.** State the units of the ray parameter in s/rad and in s/deg, and give the
conversion factor. Convert 6.873217 s/deg to s/rad.

**★4.** At 60° the P ray parameter is 6.873217 s/deg. Compute the travel-time
change for a 0.5° increase in distance.

**★5.** State whether the S velocity in the outer core is small or exactly
zero, and give the measured values at 2890 km and 4000 km.

---

## ★★ Applied

**★★6.** Verify the measured difference between TauP's ray parameter and the
central difference $\mathrm{d}T/\mathrm{d}\Delta$ at 45°: state the expected
truncation error for a 0.01° step and reconcile it with the measured
$-3.50\times10^{-4}$ s/deg.

**★★7.** From the depth table, compute the depth change equivalent to a 1°
change in distance at 60°. State the implication for hypocentre location and
name a second observable that constrains depth.

**★★8.** An S−P time of 900.0 s is measured at one station. State the distance
found by the demonstration's search, the resolution of the grid, and why the
solution set is a circle rather than a point.

**★★9.** Explain why six arrivals are named `P` at 20°, identify the
discontinuities responsible, and state the total time span of the set.

**★★10.** A catalog lists a phase as `P` at 120°. State what the first arrival
actually is and why the mislabelling is a problem for a location code.

---

## ★★★ Research-oriented

**★★★11.** Compare iasp91, prem and ak135 for P and S at 60° and 90°. Report
the spreads in seconds, convert them to equivalent distance errors, and state
whether the model choice matters more for location or for tomography.

**★★★12.** Scan source depths from 0 to 600 km and report the distance at which
direct P disappears and at which PKIKP becomes the first arrival. Explain both
trends in terms of the ray's turning depth near the core–mantle boundary, and
state why the shadow boundary is a joint constraint on source depth and core
radius.

**★★★13.** Build a single-station location from three observables: an S−P
time, a P–pP time (depth phase) and a back-azimuth from polarisation. State the
required accuracy of each to fix a hypocentre to 5 km, and report how much of
that budget the velocity-model uncertainty consumes.
