# Exercises — 04-08-03 Planetary Geophysics from Orbiters and Landers

Attempt these **closed-book** before opening the
[solutions](./03-planetary-geophysics-missions-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Take $c = 3.0\times10^8$ m s⁻¹ and $\mu_0 = 1.2566\times10^{-6}$ N A⁻².

Problems referring to
[`../code/planetary_geophysics_missions_demo.py`](../code/planetary_geophysics_missions_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** A single seismic station records a P arrival and, 15 s later, an S
arrival. Take $v_P = 5.5$ km s⁻¹ and $v_S = 3.0$ km s⁻¹.

(a) Compute the epicentral distance under the straight-ray, homogeneous
assumption.
(b) Compute the logarithmic sensitivity of that distance to $v_P$ and to $v_S$.
(c) State what a 1 per cent error in $v_S$ does to the distance, and what a
distance error does to the estimated origin.
(d) State what the number of stations has to do with the answer to (c).

---

**★2.** A Ps conversion is recorded 3.0 s after the direct P arrival.

(a) Compute the crustal thickness for $v_P/v_S = 1.667$ with $v_P = 6.0$
km s⁻¹.
(b) Compute it for $v_P/v_S = 1.90$.
(c) State the percentage difference in thickness and in velocity ratio.
(d) State what a second phase would add.

---

**★3.** A spacecraft is tracked at X-band, $f = 8.4$ GHz.

(a) Compute the two-way Doppler shift for a range rate of 2 mm s⁻¹.
(b) Compute the range rate corresponding to a Doppler measurement stable to
0.01 Hz.
(c) A 20 mGal anomaly ($2\times10^{-4}$ m s⁻²) acts for 60 s. Compute the
accumulated velocity change and the Doppler shift.
(d) Compare (c) with (b) and state what the comparison implies about the
limiting factor for orbiter gravity.

---

**★4.** A radar sounder operates at 20 MHz in ice with
$\varepsilon_r = 3.2$.

(a) Compute the vertical resolution.
(b) Compute the depth corresponding to a two-way delay of 8 µs.
(c) Compute the power reflection coefficient for an ice–rock interface with
$\varepsilon_r = 7$ and for an ice–water interface with $\varepsilon_r = 81$.
(d) State the ratio of the two and what it implies for detecting water.

---

## ★★ Applied

**★★5.** Run the demo's section 1.

(a) Report the conversion factor and the two sensitivities.
(b) Report the thicknesses at $v_P/v_S = 1.71$, 1.80 and 1.90 for a 4 s delay.
(c) State whether the observed 4 s delay can be explained with $v_P = 6$ km s⁻¹
and $v_S = 3.5$ km s⁻¹ in a 30 km crust, showing your arithmetic.
(d) State three things a single station *can* determine, in contrast to the two
it cannot.

---

**★★6.** Run the demo's section 2.

(a) Report the Doppler shift for 1 mm s⁻¹ and the noise-floor range rate.
(b) Report the accumulated velocity change and the signal-to-noise for durations
of 10, 30, 60 and 300 s.
(c) Compute the gravity anomaly that would give a signal-to-noise of 1 over a
60 s pass.
(d) State the two factors that actually limit the resolution of an orbiter
gravity field, and why (c) does not.

---

**★★7.** Run the demo's sections 3 and 4.

(a) Report the vertical resolution at 10 and 60 MHz.
(b) Report the reflectivity of an ice–water and an ice–dry-rock interface, and
the ratio of their reflected powers.
(c) Report the penetration depth at 10 MHz for $\tan\delta = 10^{-4}$ and
$10^{-3}$, with the two-way loss per kilometre.
(d) State which of the two failure modes — no contrast or too much absorption —
each of the two interfaces in (b) would suffer from in a warm, lossy ice.

---

## ★★★ Research-oriented

**★★★8.** A radar sounder has a two-way system margin of 30 dB, and the ice has
a loss tangent of $10^{-3}$ at 10 MHz.

(a) Using the demo's loss table, compute the maximum sounding depth.
(b) Compute the two-way loss for a target at 3 km depth and compare it with the
margin.
(c) State what this implies about where the limit on sounding actually lies, and
name two other effects that reduce the achievable depth in practice.
(d) Design the bandwidth you would choose for a target that is a 50 m thick layer
at 3 km depth, and state the trade-off you are making.

---

**★★★9.** A magnetometer is flown over a magnetised crust at two altitudes, and
the ratio of the anomaly at the surface to the anomaly at 50 km altitude is
$1331$ for one source and $42.9$ for another.

(a) Derive the ratio $B_z(0)/B_z(h)$ for a point dipole at depth $d$ directly
beneath the spacecraft.
(b) Invert the two measured ratios for the two source depths.
(c) State the anomaly amplitude ratio, in decibels, between the two sources at
the surface if they had equal magnetisation, and explain why the inversion of (b)
does not need the magnetisation.
(d) Discuss, in no more than five sentences, why a real crustal source does not
obey this inversion exactly, and what a mission does about it.
