# Solutions — 05-08-06 Vertical Seismic Profiling and Check Shots

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Three measurements

| Measurement | What it physically measures |
|---|---|
| Check shot | Travel time from a surface source to a receiver at a few fixed depths |
| VSP | The full wavefield (downgoing and upgoing) at many receiver depths |
| Surface seismic | Reflection travel times along a dense surface grid |

Only the first two have a known receiver depth; only the VSP separates the
wavefields.

---

## ★2 — Slowness and time

$\\Delta t = 10^{6}/2500 = 400$ µs m⁻¹. Two-way time over 1 km:
$2(400\\times10^{-6})(1000) = 0.800$ s.

---

## ★3 — The three velocities

- $v_{\\text{int}} = \\Delta z/\\Delta t$ for one interval.
- $v_{\\text{avg}} = z/t(z)$, the ratio for the whole path.
- $v_{\\text{rms}} = \\sqrt{\\sum v_i^2\\Delta t_i/\\sum\\Delta t_i}$, the velocity that
  governs normal-moveout.

Depth conversion requires the **average** velocity along the path (or a
ray-traced time); using $v_{\\text{rms}}$ is a standard and expensive error.

---

## ★4 — Interval velocities and precision

**(a)** From the measured differences: 2000.0, 2400.0, 2638.3, 3100.0, 3100.0,
4200.0, 4200.0, 4200.0, 4200.0, 4200.0 m s⁻¹ for successive 250 m intervals from
500 to 3000 m.

**(b)** $\\delta v = v^2\\delta t/\\Delta z = (4200^2)(0.001)/100 = 176.4$ m s⁻¹, i.e.
4.2 per cent at 4200 m s⁻¹.

**(c)** The design rule: **choose the receiver spacing so that the timing precision
gives the velocity precision you need.** For 1 per cent at 4200 m s⁻¹ with 1 ms
timing, $\\Delta z \\ge v^2\\delta t/(0.01v) = v\\delta t/0.01 = 420$ m. A tighter
spacing is only useful if the timing improves, which is why VSPs use first-break
picking with sub-millisecond precision rather than simply adding receivers.

---

## ★5 — A tie drift of +8 ms at 2500 m

**(a)** The measured time to 2500 m is 0.8622 s one-way. A drift of $+8$ ms two-way
is $+4$ ms one-way, i.e. $+0.46$ per cent in time and therefore $-0.46$ per cent in
average velocity: $v_{\\text{avg}}$ must be reduced by about 0.46 per cent.

**(b)** $0.0046\\times2500 = 11.6$ m at 2500 m.

**(c)** The section's *travelled time* is larger than the check shot implies, so
with a fixed velocity the section's depth is too *deep* by 11.6 m at that level; the
correction is to lower the velocity, which returns the reflector to the well's
depth.

---

## ★6 — Two-way times

One-way to 2000 m is 0.7432 s (measured), so two-way is **1.4864 s**. For a
two-way time of exactly 1.500 s, one-way is 0.7500 s, which lies between 0.7432 s
(2000 m) and 0.8027 s (2250 m) in the 4200 m s⁻¹ layer:
$z = 2000 + 4200(0.7500-0.7432) = 2000 + 28.6 = 2028.6$ m.

---

## ★7 — Ray-bending versus straight rays

Method: solve the ray equation in a layered medium (Snell's law with
$\\sin\\theta_i/v_i = p$ constant), iterating the take-off angle until the ray
reaches the receiver. Compare with the straight-ray sum of the lesson's §3.4.

Expected result: the differences are largest at shallow receiver depths and long
offsets, where the straight-ray path crosses a fast layer at an unphysical angle. At
1200 m offset the error is a few milliseconds at 250 m depth and falls below 1 ms
beyond roughly 1000 m of receiver depth. **Design consequence:** for a shallow
target (say the first few hundred metres) the offset must be small — of order the
target depth — or the direct arrival must be ray-traced rather than approximated.
This is why shallow VSPs use near-offset sources and why the old rule of thumb
"offset ≈ target depth" exists.

---

## ★8 — Synthetic VSP, corridor stack, and the residual

Method: define a reflectivity series; compute downgoing arrivals as the direct
arrival convolved with the source wavelet; compute upgoing arrivals by convolving
the reflectivity with the two-way transmission and the wavelet; stack a corridor
around the direct arrival after separating upgoing and downgoing fields by
$f$–$k$ or median filtering.

Expected residual sources, in order of importance:

1. **The corridor window and the separation filter** — the upgoing field is never
   perfectly separated, so the stack inherits downgoing energy;
2. **Attenuation and dispersion**, absent from the convolutional model, which
   change the wavelet with depth;
3. **Internal multiples** between strong reflectors, which the 1-D model may or may
   not include;
4. **The velocity model**, which sets the corridor alignment.

The dominant one in a real dataset is usually the **separation filter** for shallow
targets and **attenuation** for deep ones. Report which you found, and note that
the residual is what a tie's uncertainty actually is.
