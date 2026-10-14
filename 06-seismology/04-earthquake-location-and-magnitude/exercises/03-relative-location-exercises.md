# Exercises — 06-04-03 Relative Location: Master-Event, Double-Difference, HypoDD

Attempt these before reading the
[solutions](./03-relative-location-solutions.md). The lesson is
[03 Relative Location](../03-relative-location.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A pick has uncertainty $\sigma_{\text{pick}} = 20\ \mathrm{ms}$. Compute
the uncertainty of a differential time formed from two independent picks.

**★2.** Write the differential-time equation for event $j$ and master $0$ at
station $i$, and mark the term that cancels.

**★3.** State in one sentence why an absolute location absorbs a station delay
into position, whereas a differential time does not.

## ★★ Applied

**★★4.** Using the demonstration's table, compute the improvement factor of
"relative, measured difference" over "relative, difference of two picks", and
over "absolute locations, offsets taken".

**★★5.** The eight station delays of the demonstration are, in milliseconds,
$[67, -132, 141, -52, -136, -70, 69, 42]$. Compute their mean from the rounded
values, and compare with the printed $-8.95\ \mathrm{ms}$. Explain the
discrepancy.

**★★6.** The least-squares projection of the delay pattern onto the model space
is $(+869.7, -266.1, +1016.5)\ \mathrm{m}$. Compute its norm and compare with the
measured 3-D bias norm
$\sqrt{867.2^{2} + 210.0^{2} + 810.0^{2}}$.

## ★★★ Research-oriented

**★★★7.** Design a cross-correlation workflow that would reduce
$\sigma_{\text{dd}}$ from 2 ms to 0.5 ms, and predict the resulting cluster
geometry error using the measured scaling between $\sigma_{\text{dd}}$ and the
offset error. State every preprocessing step and the failure mode of each.

**★★★8.** Specify a numerical experiment that measures the *separation limit* of
the velocity-error cancellation: cluster size from 0.1 to 20 km, fixed network,
fixed 3 per cent velocity error, and a metric defined on relative offsets. Give
the expected shape of the curve and the observation that would falsify the
leading-order argument.
