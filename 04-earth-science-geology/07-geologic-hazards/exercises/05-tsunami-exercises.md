# Exercises — 04-07-05 Tsunami Generation, Propagation and Warning

Attempt these **closed-book** before opening the
[solutions](./05-tsunami-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/tsunami_demo.py`](../code/tsunami_demo.py) require you to run it and
report its actual output.

---

## ★ Foundational

**★1.** Take $g = 9.80665$ m s⁻².

(a) Compute the shallow-water phase speed in 1000 m, 3000 m and 4000 m of water,
in m s⁻¹ and km h⁻¹.
(b) Compute the travel time for 2000 km at each depth.
(c) Compute the travel time over a route that is 1000 km at 4000 m and 1000 km
at 1000 m, and state which segment dominates.
(d) State why the deep segment dominates.

---

**★2.** A tsunami has a period of 900 s in water 4000 m deep.

(a) Compute its wavelength.
(b) Compute $h/L$ and state whether the shallow-water approximation applies.
(c) Compute the corresponding ratio for a 10 s wind wave in the same depth and
state the regime.
(d) State one observable consequence of the difference in regime.

---

**★3.** A tsunami has a deep-water amplitude of 0.4 m in 4000 m of water.

(a) State Green's law and derive its exponent from energy-flux conservation.
(b) Compute the amplitude at the 50 m depth contour.
(c) Compute the amplitude at 10 m.
(d) State two reasons the real amplitude in shallow water differs from (c).

---

**★4.** A bore advances into still water 2 m deep, leaving a water surface 2 m
higher behind it.

(a) Derive the bore speed from mass and momentum conservation.
(b) Compute the bore speed and the flow velocity behind the front.
(c) Repeat for a leaving height of 1 m and compare.
(d) Show that the expression reduces to $\sqrt{gh_1}$ when the height of the
bore tends to zero.

---

## ★★ Applied

**★★5.** Run the demo's sections 1 and 2.

(a) Report the exact and shallow-water phase speeds for $T = 300$, 600 and
1200 s in 4000 m, with the relative errors.
(b) Report the $(kh)^2/6$ column and state the relation between the two.
(c) State the period below which the relative error exceeds 1 per cent.
(d) Report the wavelengths at $T = 120$ and 1200 s and the corresponding $h/L$,
and state which is inside the shallow-water regime by the $1/20$ criterion.

---

**★★6.** Run the demo's section 6 for a still-water depth of 1 m.

(a) Report the bore speed and the flow behind the front for $H = 0.5$, 1, 2 and
4 m.
(b) State how the bore speed grows with $H$ for $H \gg h_1$, and verify it from
the table.
(c) Compute the advance time of the flow front over 200 m for $H = 2$ m.
(d) Explain why the answer to (c) is the number that matters for an evacuation
decision.

---

**★★7.** Run the demo's section 7.

(a) Report the seafloor pressure increment for sea-surface elevations of 0.1, 1
and 50 cm.
(b) Compute the elevation corresponding to a pressure resolution of 10 Pa.
(c) Report the transmitted fractions at wavelengths of 250 m, 1 km, 25 km and
100 km in 4000 m of water, and state the crossover wavelength.
(d) Explain why the same formula that makes a tsunami visible makes a wind sea
invisible.

---

## ★★★ Research-oriented

**★★★8.** A warning centre computes travel times on a bathymetric grid. A
particular great-circle path is approximated by three segments: 3000 km at
5000 m, 4000 km at 3000 m and 1000 km at 1000 m.

(a) Compute the travel time for each segment and the total.
(b) Compute the travel time that a single uniform depth of 3500 m would predict
for the same 8000 km path, and give the percentage difference.
(c) Compute the depth of a uniform ocean that would give the correct total
travel time, and explain why it is closer to the deepest segment than to the
arithmetic mean.
(d) State two reasons a real path would differ from this calculation, and which
of them changes the arrival time more.

---

**★★★9.** The Kajiura filter shows that the sea surface responds only to the
long-wavelength part of a seafloor displacement.

(a) Derive the filter from the statement that water must move horizontally for
the surface to move, and state the assumption about the timescale of the
seafloor motion.
(b) Compute the transmitted fraction for wavelengths of 10, 25 and 100 km in
4000 m of water.
(c) Two earthquakes have the same seismic moment, but one ruptures a 400 km long
fault and the other a 100 km long fault. Assuming the seafloor displacement is
concentrated at a wavelength comparable with the fault length, compute the ratio
of the initial sea-surface amplitudes of the two events.
(d) Discuss, in no more than six sentences, what this implies for the
reliability of a tsunami warning issued from a magnitude alone in the first ten
minutes after an earthquake.
