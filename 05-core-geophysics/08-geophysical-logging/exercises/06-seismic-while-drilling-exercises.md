# Exercises — 05-08-06 Vertical Seismic Profiling and Check Shots

Attempt these **closed-book** before opening the
[solutions](./06-seismic-while-drilling-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/vsp_demo.py`](../code/vsp_demo.py) require you to
run it and report its actual output. **State the velocity type and the receiver
spacing for every velocity you quote.**

---

## ★ Foundational

**★1.** Distinguish a check shot, a VSP and a surface seismic survey by what each
physically measures.

**★2.** Convert 2500 m s⁻¹ to slowness in µs m⁻¹ and compute the two-way time over
a 1 km interval at that velocity.

**★3.** State the difference between $v_{\\text{int}}$, $v_{\\text{avg}}$ and
$v_{\\text{rms}}$, and which one a depth conversion requires.

---

## ★★ Applied

**★★4.** Run [`../code/vsp_demo.py`](../code/vsp_demo.py).

(a) Report the interval velocities implied by 250 m receiver spacing.
(b) Recompute the precision argument of the lesson's equation (3) for 100 m spacing
at 4200 m s⁻¹ and a 1 ms timing error.
(c) State the design rule it implies.

---

**★★5.** A tie shows a smooth drift of $+8$ ms at 2500 m relative to the check-shot
time.

(a) Compute the implied average-velocity error.
(b) Compute the depth shift it causes at 2500 m.
(c) State whether the sign of the shift means the section is too deep or too
shallow.

---

**★★6.** For the demonstration's model, compute the two-way time to 2000 m and the
depth at which the two-way time is exactly 1.500 s.

---

## ★★★ Research-oriented

**★★★7.** Implement a ray-bending (ray-traced) direct arrival for the
demonstration's model at three offsets and compare it with the straight-ray times.
Report the offset at which the error exceeds 1 ms and state what that means for
shallow-target VSP design.

---

**★★★8.** Build a synthetic VSP with downgoing and upgoing arrivals for a stated
reflectivity model, form a corridor stack, and compare it with a convolutional
surface-seismic model. Report the residual after the tie and identify which
assumption dominates it.

---

## Reference list used in this problem set

- [05-08-06 lesson](../06-seismic-while-drilling.md)
- [05-08-04 Density, Neutron and Sonic Porosity Logs](../04-porosity-logs.md)
- [Solutions](./06-seismic-while-drilling-solutions.md)
