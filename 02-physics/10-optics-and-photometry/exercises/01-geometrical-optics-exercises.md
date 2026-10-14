# Exercises — 02-10-01 Geometrical Optics, Refraction and Lenses

Attempt these **closed-book** before opening the
[solutions](./01-geometrical-optics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/geometrical_optics_demo.py`](../code/geometrical_optics_demo.py)
require you to run it and report its actual output.

Use $n_{\text{air}} = 1.000293$ when an air path is part of the problem, and
state which value of $n$ you used for each material. All angles are in degrees
unless a radian answer is requested.

---

## ★ Foundational

**★1.** Light inside water ($n = 1.333$) strikes the water–air surface from
below at (a) 30°, (b) 45°, (c) 50°, (d) 48.6°.

For each case compute the refraction angle in air, or state that total internal
reflection occurs. Then compute the critical angle using $n_{\text{air}} = 1.333$
and again using $n_{\text{air}} = 1.000293$, and comment on the size of the
difference.

---

**★2.** A step-index fibre has a core index of 1.470 and a cladding index of
1.455, a core radius of 3.0 µm and is operated at 1300 nm.

(a) Compute the numerical aperture.
(b) Compute the acceptance half-angle in air.
(c) Compute the V number and the approximate mode count.
(d) Compute the single-mode cutoff wavelength and state whether the fibre is
single-mode at 1300 nm.

---

**★3.** A camera lens has a focal length of 35 mm and is focused on an object
2.0 m away. Its aperture diameter at full opening is 25 mm.

(a) Compute the image distance.
(b) Compute the magnification.
(c) Compute the image size of a 1 m object.
(d) Compute the f-number and the diameter of the diffraction-limited spot at
550 nm.

---

**★4.** A 12 mm thick glass window ($n = 1.52$) sits in front of a detector.
A ray enters at 30° from the normal.

(a) Compute the refraction angle inside the glass.
(b) Compute the lateral displacement of the emerging ray.
(c) Compute the displacement at normal incidence and explain the result.
(d) Compute the apparent depth of a 3.0 m deep pool of water as seen from
directly above.

---

## ★★ Applied

**★★5.** Run section 1 and section 3 of
[`../code/geometrical_optics_demo.py`](../code/geometrical_optics_demo.py).

(a) Report the normal-incidence reflectance at the air–water interface and the
refracted angle for 30° of incidence.
(b) Report the Brewster angle and the values of $R_s$ and $R_p$ there.
(c) Report the fibre's numerical aperture, acceptance angle, V number and cutoff
wavelength.
(d) State why a polarising filter suppresses water glint but does not suppress
the transmitted signal.

---

**★★6.** A fibre is designed with a numerical aperture of 0.20, a core radius of
50 µm and is operated at 850 nm.

(a) Compute the V number.
(b) Compute the approximate mode count.
(c) Compute the cutoff wavelength.
(d) Explain in one sentence why this fibre cannot be used for a phase-based
distributed acoustic sensing measurement.

---

**★★7.** A satellite imager has an aperture of 0.30 m and observes at 550 nm
from an altitude of 700 km.

(a) Compute the diffraction-limited angular resolution.
(b) Compute the corresponding ground sample distance.
(c) The instrument's actual pixel pitch projects to 10 m on the ground. State
whether it is diffraction-limited or pixel-limited, and justify the answer
numerically.
(d) Compute the ground sample distance at 500 km for a 0.25 m aperture.

---

**★★8.** Run section 5 of
[`../code/geometrical_optics_demo.py`](../code/geometrical_optics_demo.py).

(a) Report the displacement at 45° for the 10 mm glass slab.
(b) Report the apparent-depth factor for water.
(c) Using the file's printed constant, compute the apparent depth of a 4.5 m pool
and compare it with the answer to ★4(d).
(d) State one instrument in which the displacement of (a) would corrupt a
measurement if it were not calibrated.

---

## ★★★ Research-oriented

**★★★9.** Derive the normal-incidence intensity reflectance of a single
interface from the electromagnetic wave impedance of each medium, and use it to
compute the throughput of a lens system.

(a) Starting from the wave impedance $Z = \sqrt{\mu/\varepsilon} = Z_0/n$,
derive $R = ((n_1-n_2)/(n_1+n_2))^2$ by equating the voltage reflection
coefficient to an impedance mismatch.
(b) Compute $R$ for an uncoated air–glass interface with $n = 1.52$.
(c) Compute the transmitted fraction through a lens with 12 air–glass surfaces,
stating the assumption you made about multiple reflections.
(d) Explain in one sentence why the answer to (c) is the reason every serious
optical system is coated, and cross-check with
[02-10-02](../02-interference-diffraction-optics.md) §1.3.

---

**★★★10.** The atmosphere is a plane-parallel medium with a refractive index
decreasing from 1.000293 at sea level to 1 in space.

(a) Using the flat-layer invariant $n\sin\theta = \text{const}$, compute the
largest zenith angle at sea level from which a ray can reach space, and state
what the flat-layer model predicts happens to rays steeper than that.
(b) Explain why the real atmosphere does not trap grazing rays, naming the
geometric quantity that must be included in the invariant.
(c) Compute the critical value of that invariant for the Earth's surface using
the mean radius 6371 km, and state whether it exceeds $n$ at sea level.
(d) Using your answers, explain why astronomical refraction at the horizon
depends on the temperature and pressure profile and cannot be a material
constant.

---

**★★★11.** Design a single-mode fibre for operation at 1550 nm with a
single-mode cutoff at 1300 nm.

(a) Derive the numerical aperture required, taking the core radius as 4.5 µm.
(b) Compute the fractional index step $\Delta = (n_1-n_2)/n_1$ required, using
the small-index-difference approximation $\mathrm{NA} \approx n_1\sqrt{2\Delta}$.
(c) Compute the V number at the operating wavelength and confirm that the fibre
is single-mode.
(d) Estimate the number of modes this fibre would support at 400 nm, and state
whether that matters for the intended application.
