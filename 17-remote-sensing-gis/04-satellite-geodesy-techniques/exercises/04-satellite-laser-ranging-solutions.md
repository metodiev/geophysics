# Solutions — 17-04-04 Satellite Laser Ranging, DORIS and VLBI

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [04 Satellite Laser Ranging, DORIS and VLBI](../04-satellite-laser-ranging.md).

---

## ★1 — Timing to millimetres

$$r = \frac{c\,\Delta t}{2}
= \frac{299\,792\,458\times250\times10^{-12}}{2} = 3.7474\times10^{-2}\ \mathrm{m}
= 37.474\ \mathrm{mm}.$$

(*Check against the lesson table:* 250 ps is 2.5 times the 100 ps entry
(14.9896 mm), and $2.5\times14.9896 = 37.474$ ✓.)

**Besides the time of flight**, a laser range must be corrected for:

1. the **atmospheric delay** (several metres at zenith, larger at low elevation);
2. the **target's centre-of-mass offset** from the reflecting array, which depends
   on the array geometry and the viewing direction;
3. the **station's own reference-point offset** from the instrument and any
   eccentricities;
4. relativistic and (small) calibration scale errors.

Only the first is a propagation effect; the others are geometry of the hardware,
which is why they are systematic and are modelled rather than averaged.

---

## ★2 — Doppler shift

$$f_d = -\frac{f_0}{c}\dot\rho
= -\frac{2.0\times10^{9}}{299\,792\,458}\times5\times10^{3}
= -6.6713\times10^{3}\ \mathrm{Hz} = -6.6713\ \mathrm{kHz}.$$

**Sign:** the shift is negative for a *positive* range rate, so a negative Doppler
means the satellite is **receding**. A positive shift means approaching. This is
the opposite of the everyday Doppler intuition for sound (approaching → higher
pitch), and it is a fixed source of sign errors; the lesson's table makes it
explicit.

---

## ★3 — Baseline delay and angular precision

$$\tau_{\max} = \frac{B}{c} = \frac{3.0\times10^{6}}{299\,792\,458}
= 1.0007\times10^{-2}\ \mathrm{s} \approx 10.007\ \mathrm{ms}.$$

Angular precision:
$$\sigma_\theta \approx \frac{c\,\sigma_\tau}{B}
= \frac{299\,792\,458\times5\times10^{-12}}{3.0\times10^{6}}
= 5.00\times10^{-10}\ \mathrm{rad}.$$

In milliarcseconds:
$$\frac{5.00\times10^{-10}}{4.8481\times10^{-9}} = 0.103\ \mathrm{mas}.$$

**Comment:** the maximum delay is ten *milliseconds* while the measurement
precision is five *picoseconds* — a fractional precision of $5\times10^{-10}$. The
angular precision is that fraction of a radian, which is why a baseline of
continental length, with a bandwidth of order a gigahertz, defines a reference
frame at the hundred-microarcsecond level and better.

---

## ★4 — Velocity from a laser series

**(a)** Formal scatter of a straight line through $N$ points of noise $\sigma$ over
a span $\Delta t$:
$$\sigma_v \approx \frac{\sigma\sqrt{12}}{N^{1/2}\,\Delta t}
= \frac{5\ \mathrm{mm}\times3.464}{44.72\times8\ \mathrm{yr}}
= \frac{17.32\ \mathrm{mm}}{357.8\ \mathrm{yr}}
= 0.0484\ \mathrm{mm\,yr^{-1}}.$$

**(b)** Two systematic errors that would dominate:

1. The **target's centre-of-mass offset**: a constant range bias of a few
   millimetres shifts every range by the same amount. For a *rate* that constant
   cancels, but any change in the array's effective offset — from satellite
   rotation, thermal deformation or a change of tracking strategy — appears as a
   spurious trend over years. Averaging cannot remove it because it is correlated
   with time, not random.
2. The **atmospheric delay model**: the zenith delay and its mapping function
   change with the weather and with the observation elevations used. If the
   elevation distribution drifts over the years (a different tracking schedule), a
   slanted, time-correlated error appears — again not removable by averaging.

Also relevant: monument instability, which is a real ground motion and cannot be
distinguished from tectonics by the ranging data alone.

---

## ★5 — The bias/scale degeneracy

**(a)** Every station is at essentially the same radius, so a uniform radial shift
and a uniform radial *scaling* are the same transformation to within the tiny
fractional radius spread; the design matrix columns $\mathbf{1}$ and
$\mathbf{r}/R_E$ are therefore nearly parallel, and the two estimates are
correlated to $-1$ to six decimals.

**(b)** Fractional radius spread:
$$\frac{2.9\ \mathrm{km}}{6371\ \mathrm{km}} = 4.55\times10^{-4}.$$

The correlation between the two estimates is approximately
$$\rho \approx -\frac{1}{\sqrt{1+\epsilon^{2}}} \quad\text{with}\quad
\epsilon \propto \frac{\text{spread of } r/R_E}{\text{mean}}.$$

To reduce $|\rho|$ from $\approx1$ to $0.99$ requires
$\epsilon \approx \sqrt{1/0.99^{2}-1} = 0.1425$ — i.e. a fractional radius spread
of order $14\%$, which would mean stations spanning $\pm900\ \mathrm{km}$ in
radius: geophysically impossible for a ground network (and the reason the
degeneracy is fundamentally geometric, not a matter of better data). The scale
must instead come from geometry that is not radial at all — VLBI, GNSS, or the
varying radius of a satellite's orbit.

---

## ★6 — UT1 versus delay precision

$$\Delta\theta = \Omega\,\Delta t = 7.292\,115\times10^{-5}\times0.05\times10^{-3}
= 3.6461\times10^{-9}\ \mathrm{rad},$$
$$\Delta\tau = \frac{B}{c}\Delta\theta
= \frac{6.0\times10^{6}}{299\,792\,458}\times3.6461\times10^{-9}
= 7.2972\times10^{-11}\ \mathrm{s} = 72.972\ \mathrm{ps}.$$

Compare with $5\ \mathrm{ps}$ of delay precision: the UT1-induced delay is
**$14.6$ times larger**. So the comparison implies that a $0.05\ \mathrm{ms}$ UT1
error would already be visible in the delay, i.e. that the interferometer is
sensitive to UT1 at the $0.003\ \mathrm{ms}$ level. The measurement is therefore
not "corrupted by unknown Earth rotation": it *determines* Earth rotation, and
the Earth-orientation parameters published by the geodetic services are a product
of this technique (combined with GNSS, laser ranging and DORIS). The analyst's
obligation is to state whether those parameters were estimated or fixed.

---

## ★7 — Tying the three techniques at one site (specification)

**Local survey.** A high-precision local tie survey between the *reference points*
of the three instruments: the VLBI antenna's invariant point (the intersection of
the azimuth and elevation axes, found by a dedicated survey rather than by
measurement of the structure), the laser telescope's invariant point, and the GNSS
antenna's reference point (typically the antenna's phase centre, with its offset
from the mechanical reference measured or modelled). The survey uses a local
network of pillars observed with a total station or a terrestrial laser scanner at
sub-millimetre level, and it is repeated after any change of hardware.

**Systematic effects to model.** (i) Antenna deformation: a large VLBI dish flexes
with elevation, so its reference point moves with pointing — a millimetre-class
effect that must be modelled as a function of elevation, not measured once. (ii)
Thermal expansion of the telescope and the pillars. (iii) GNSS antenna phase-centre
offsets and variations, which are elevation- and azimuth-dependent. (iv) The
difference between a *local* survey frame and the global frame: the tie must be
expressed as a vector in the terrestrial frame, with its own covariance, not as a
set of distances.

**Validation.** Compute the site's position from each technique independently and
compare; the residuals must be consistent with the *tie*'s covariance, not with
the techniques' individual formal errors. A systematic offset appearing in all
three is a frame realisation difference; one appearing in only one is a local
problem (survey error, hardware model, or a technique-specific bias). The check
that matters is the closure of the three: any inconsistency larger than the tie's
error bar invalidates the $1\ \mathrm{mm}$ claim, regardless of how good the
individual solutions look.

---

## ★8 — Two interpretations of the same DORIS data

**(a)** Orbit determination solves for the *satellite's* trajectory (and usually
the beacon and tropospheric parameters) while treating the ground station
coordinates as known and fixed. Geodetic positioning does the opposite: it fixes
the orbits (from a preliminary precise solution) and solves for the *station*
coordinates. Both are the same least-squares system with different parameter
partitions: the observation equation is symmetric in "satellite position" and
"station position" because only their *difference* enters the geometric range.

**(b)** Using orbit-mode coordinates as if they were geodetic coordinates is
circular: the coordinates in that product were *assumed*, not estimated, so they
contain whatever errors the assumed values had, and their formal errors are
meaningless. The consequence is a set of station coordinates no better — and
sometimes worse — than the a priori values they were derived from, dressed in
new uncertainties. This is a real and recurring failure mode of automated
processing chains.

**(c)** The general rule, and the reason this example belongs in the lesson:
**any parameter whose signature mimics the error you are estimating will absorb
it**, and the resulting estimate will look well-determined while being
circular. In this case the "error" (the assumed station position) has exactly the
same signature as the parameter (the station position). In the radial-bias/scale
example the two parameters' signatures are identical to within the fractional
radius spread; in the altimetric geoid example of module 17-03 the same structure
appears between the geoid error and the ocean dynamic topography. The remedy is
always the same: break the degeneracy with a measurement whose signature differs —
a different technique, a different geometry, or a different time scale — and
report the *correlation* as the measure of what was separated.
