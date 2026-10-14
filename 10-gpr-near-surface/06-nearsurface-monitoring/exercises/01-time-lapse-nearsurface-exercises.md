# Exercises — 10-06-01 Time-Lapse Near-Surface Geophysics

Attempt these before reading the
[solutions](./01-time-lapse-nearsurface-solutions.md). The lesson is
[01 Time-Lapse Near-Surface Geophysics](../01-time-lapse-nearsurface.md). All
models are **SYNTHETIC** teaching values; reference numbers come from
`code/time_lapse_demo.py`. Teaching environmental sensitivity
$\mathrm dv/\mathrm dT = -0.5\ \mathrm{m\,s^{-1}\,K^{-1}}$ at
$v = 400\ \mathrm{m\,s^{-1}}$.

## ★ Foundational

**★1.** Two baseline repeats give $\mathrm{NRMS} = 3.0\%$. What noise level does
that imply, and how does the answer change if the second repeat is twice as noisy
as the first (an extension of Section 3.1)?

**★2.** A path has $t = 40\ \mathrm{ms}$ and the pick is good to
$0.5\ \mathrm{ms}$. Compute the smallest relative velocity change it can resolve,
and the arrival-time shift produced by a $0.4\%$ change.

**★3.** State in three sentences the difference between a 4-D difference, a 4-D
ratio and a 4-D inversion, and give one observables that suits each.

## ★★ Applied

**★★4.** Using the measured scatters ($0.355$ and $0.058\times10^{-4}$ at 20%
noise for 1 s and 4 s codas), compute the precision ratio and compare it with the
$T^{3/2}$ prediction of Section 3.3. State one reason the measured ratio is
smaller.

**★★5.** A monitoring survey spans six months with a $6\ \mathrm{K}$ temperature
change. Using the teaching sensitivity, compute the aliased $\delta v/v$, and
decide whether a $0.3\%$ target change is measurable without a reference site.
State what the reference site must match to make the correction work.

**★★6.** The wrong-hypothesis $\chi^2$ at unit amplitude is $497$ for a given path
set with a $0.5\ \mathrm{ms}$ pick. Compute the change amplitude needed for
rejection at the 95% point ($\chi^2 = 5.99$), and state how the requirement scales
with the picking error.

## ★★★ Research-oriented

**★★★7.** Design a four-path monitoring layout for a 25 m deep embankment that
must reject the uniform-change hypothesis at 95% when a $0.25\ \mathrm{ms}$ pick is
available. State the path depths, the expected $\chi^2$ of the wrong hypothesis,
and the smallest localised change you could detect. A specification that could not
be executed is a failed answer.

**★★★8.** A colleague reports a $2\%$ velocity decrease between two epochs with no
repeatability figure, no temperature record and no baseline repeat. Specify the
three measurements that would test the claim and the falsification test for each.
