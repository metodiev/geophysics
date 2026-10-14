# Solutions — 04-08-03 Planetary Geophysics from Orbiters and Landers

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — A single-station distance

**(a)** $D = 15 \times \dfrac{5.5\times3.0}{5.5-3.0} = 15 \times 6.6 = 99$ km.

**(b)** $\dfrac{v_S}{v_P-v_S} = \dfrac{3.0}{2.5} = 1.20$ and
$\dfrac{v_P}{v_P-v_S} = \dfrac{5.5}{2.5} = 2.20$.

**(c)** A 1 per cent error in $v_S$ is a 2.2 per cent error in the distance (and
a 1 per cent error in $v_P$ is a 1.2 per cent error). A distance error of
$X$ per cent displaces the estimated epicentre by the same fraction of the
distance, because the only geometric information the station has is "the event is
somewhere on a circle of radius $D$".

**(d)** Everything. A single station gives one distance and one back-azimuth, so
the origin is constrained to a point on a circle; origin time, depth and distance
trade off against each other exactly along that circle. Several stations give
several circles, and it is their *intersection* that determines the location. The
limitation is geometric, not instrumental: a perfect clock cannot remove it.

---

## ★2 — Crustal thickness from a converted phase

**(a)** $v_S = 6.0/1.667 = 3.599$ km s⁻¹, so

$$H = \frac{3.0}{1/3.599 - 1/6.0} = \frac{3.0}{0.27786 - 0.16667}
= \frac{3.0}{0.11119} = 27.0\ \mathrm{km}.$$

**(b)** $v_S = 6.0/1.90 = 3.158$ km s⁻¹, so
$H = 3.0/(0.31667-0.16667) = 3.0/0.15 = 20.0$ km.

**(c)** The velocity ratio differs by 14 per cent and the thickness by **35 per
cent**. The amplification comes from the fact that $H$ depends on the *difference*
of the reciprocals, and a difference of two nearly equal numbers is poorly
determined by either of them.

**(d)** A second phase whose delay depends on $H$ and $v_P/v_S$ differently — a
crustal multiple, or the PpSs pair. Two delays give two equations in two
unknowns, which is what the H–k stacking method formalises on Earth. Without it,
a single conversion delay traces a curve in the $(H, v_P/v_S)$ plane and every
point on it fits the data equally well.

---

## ★3 — Doppler sensitivity

**(a)** $\dfrac{\Delta f}{f} = \dfrac{2\dot r}{c}
= \dfrac{2(0.002)}{3\times10^8} = 1.333\times10^{-11}$, so
$\Delta f = 1.333\times10^{-11}\times8.4\times10^9 = 0.112$ Hz.

**(b)** $\dot r = \dfrac{c}{2}\dfrac{\Delta f}{f}
= \dfrac{3\times10^8}{2}\times\dfrac{0.01}{8.4\times10^9}
= 1.79\times10^{-4}$ m s⁻¹ $= 0.179$ mm s⁻¹.

**(c)** $\Delta v = (2\times10^{-4})(60) = 1.2\times10^{-2}$ m s⁻¹
$= 12$ mm s⁻¹, so $\Delta f = \dfrac{2(0.012)}{3\times10^8}\times8.4\times10^9
= 0.672$ Hz.

**(d)** 0.672 Hz against a 0.01 Hz floor is a signal-to-noise of **67**. The
instrument is therefore nowhere near the limiting factor. What limits an orbiter
gravity field is the **geometry** (altitude and ground-track spacing set the
resolution at the surface) and the **non-gravitational accelerations** (drag,
radiation pressure, thruster activity) that must be modelled and removed before
the residual can be inverted. A measurement that is easy is not the same as an
inference that is easy.

---

## ★4 — Radar sounding

**(a)** $\Delta z = \dfrac{c}{2B\sqrt{\varepsilon_r}}
= \dfrac{3\times10^8}{2(2\times10^7)\sqrt{3.2}} = \dfrac{3\times10^8}{7.155\times10^7}
= 4.19$ m.

**(b)** $z = \dfrac{ct}{2\sqrt{\varepsilon_r}}
= \dfrac{(3\times10^8)(8\times10^{-6})}{2\sqrt{3.2}} = \dfrac{2400}{3.5777}
= 670.8$ m.

**(c)** $R_{i/r} = \dfrac{\sqrt{3.2}-\sqrt{7}}{\sqrt{3.2}+\sqrt{7}}
= \dfrac{1.7889-2.6458}{1.7889+2.6458} = -0.1932$, so $|R|^2 = 0.0373$.
$R_{i/w} = \dfrac{1.7889-9.0}{1.7889+9.0} = -0.6684$, so $|R|^2 = 0.4467$.

**(d)** The ratio is $0.4467/0.0373 = 12.0$ in power, i.e. 10.8 dB. An ice–water
interface returns twelve times the power of an ice–rock interface with the same
geometry, which is why a subglacial lake is detectable as an anomalously bright
and specular reflector: the interpretation rests on the *contrast between
interfaces*, not on the echo amplitude itself.

---

## ★★5 — Running the seismology section

**(a)** Conversion factor 8.40 km per second of S-minus-P time; sensitivities
1.40 per cent per per cent in $v_P$ and 2.40 per cent per per cent in $v_S$.

**(b)** 33.80, 30.00 and 26.67 km for a 4 s delay at $v_P/v_S = 1.71$, 1.80 and
1.90.

**(c)** With $v_P = 6.0$ and $v_S = 3.5$ km s⁻¹,
$1/v_S - 1/v_P = 0.28571 - 0.16667 = 0.11905$ s km⁻¹, so
$H = 4.0/0.11905 = 33.6$ km. A 30 km crust would require
$1/v_S - 1/v_P = 4/30 = 0.13333$ s km⁻¹, i.e. a *smaller* $v_S$ (4 s at 30 km
implies a larger velocity contrast). So the observed delay and the assumed
velocities are inconsistent with a 30 km crust, and the discrepancy could be
absorbed by a modest change in either velocity — which is exactly the trade-off.

**(d)** A single station can determine: the *presence* of a seismically active
body; the polarisation of an arrival, which distinguishes P from S and constrains
the source depth; the existence of a core, from a core-reflected or
core-transmitted phase; the amplitude and the spectrum of the signal, which
constrain attenuation; and the presence of a low-velocity layer, from a converted
or a reverberating phase. It cannot determine a well-constrained epicentre or a
unique thickness.

---

## ★★6 — Running the radio-tracking section

**(a)** 0.056 Hz for 1 mm s⁻¹; the noise floor corresponds to 0.178 mm s⁻¹.

**(b)**

| duration (s) | $\Delta v$ (mm s⁻¹) | $\Delta f$ (Hz) | S/N |
|---|---|---|---|
| 10 | 1.00 | 0.056 | 5.6 |
| 30 | 3.00 | 0.168 | 16.8 |
| 60 | 6.00 | 0.336 | 33.6 |
| 300 | 30.00 | 1.681 | 168.1 |

**(c)** $10^{-4}/33.6 = 2.98\times10^{-6}$ m s⁻² $= 0.298$ mGal. So **a 0.3 mGal
anomaly** is detectable at unit signal-to-noise in a 60 s pass, which is below
the anomaly produced by almost any interesting subsurface structure.

**(d)** The geometry and the non-gravitational accelerations. Part (c) shows that
the *signal* is not the problem; the problem is knowing precisely where the
spacecraft was and what other forces acted on it. Adding instruments cannot fix
either, which is why gravity missions are built around drag-free systems,
accelerometers and precise orbit determination.

---

## ★★7 — Running the radar sections

**(a)** 8.45 m at 10 MHz and 1.41 m at 60 MHz.

**(b)** Ice over water: $R = -0.6688$, $|R|^2 = 0.4474$. Ice over dry rock:
$R = -0.1597$, $|R|^2 = 0.0255$. The ratio is **17.5 in power**, about 12.4 dB.

**(c)** At 10 MHz: 26 883 m for $\tan\delta = 10^{-4}$ with 0.32 dB of two-way
loss per kilometre of depth; 2688 m for $\tan\delta = 10^{-3}$ with 3.23 dB per
kilometre.

**(d)** The dry-rock interface suffers from **no contrast**: 0.0255 is close to
the detection limit for a single echo and comparable with the clutter from
internal layering, so it may simply not be seen. The water interface has an
excellent contrast (0.447) but a lossy ice column attenuates the wave before it
arrives: at 3.23 dB per kilometre of depth, a 3 km target costs 9.7 dB and a 9 km
target costs the whole 30 dB margin. So the two failure modes are independent, and
a survey can fail for either reason.

---

## ★★★8 — Designing a sounding experiment

**(a)** With $\tan\delta = 10^{-3}$ the two-way loss is 3.23 dB per kilometre of
depth, so a 30 dB margin allows $30/3.23 = 9.3$ km of ice.

**(b)** A target at 3 km depth costs $3\times3.23 = 9.7$ dB — a third of the
margin, leaving 20 dB for everything else.

**(c)** The limit does not lie in the absorption: with a cold-ice loss tangent the
sounder could reach many kilometres. It lies in the **contrast** (a weak interface
returns a small fraction of the incident power, as in ★★7(d)), in the **surface
and internal clutter** (the transmitted pulse is reflected by every internal
layer, and a rough surface scatters energy out of the specular direction), in the
**geometric spreading** of the wavefront over a two-way path, and in the
**roughness of the interface** (a rough base scatters diffusely rather than
specularly, reducing the coherent echo). Each of these is a separate engineering
and analysis problem, and the absorption budget is usually the least of them.

**(d)** A 50 m layer at 3 km depth needs a vertical resolution well below 50 m —
say 10 to 20 m to resolve the layer and its two bounding interfaces. From
$\Delta z = c/(2B\sqrt{\varepsilon_r})$ with $\sqrt{3.2} = 1.789$ and
$\Delta z = 20$ m:

$$B = \frac{c}{2\Delta z\sqrt{\varepsilon_r}}
= \frac{3\times10^8}{2(20)(1.789)} = 4.19\ \mathrm{MHz}.$$

Choosing 20 MHz would give 4.2 m of resolution and a much clearer layer, at the
cost of a higher loss tangent (attenuation rises roughly linearly with frequency)
and therefore less penetration. So the trade-off is **resolution against
penetration**, and both are set by the same physical quantity, the wavelength in
the medium. A sounder designed for a deep, thick, bright target uses a low
frequency; a sounder designed for a shallow, thin layer uses a high one; and a
mission that needs both flies two radars.

---

## ★★★9 — Depth from two altitudes

**(a)** Directly above a point dipole, $r = 0$, so (8) reduces to
$B_z(0) = (\mu_0m/4\pi)\cdot 2/d^3$. At altitude $h$ the distance from the dipole
is $d+h$, and the same formula gives
$B_z(h) = (\mu_0m/4\pi)\cdot 2/(d+h)^3$. The ratio is therefore

$$\frac{B_z(0)}{B_z(h)} = \left(\frac{d+h}{d}\right)^3 ,$$

which contains **no magnetisation and no moment** — only the depth and the known
altitude. That is what makes the two-altitude measurement work.

**(b)** With $h = 50$ km and a ratio of 1331: $\dfrac{d+50}{d} = 1331^{1/3} = 11$,
so $d = 50/10 = 5$ km. With a ratio of 42.875:
$42.875^{1/3} = 3.5$, so $d = 50/2.5 = 20$ km.

**(c)** At equal magnetisation the surface amplitudes go as $1/d^3$, so the ratio
is $(20/5)^3 = 64$, i.e. $10\log_{10}64 = 18.1$ dB. The inversion in (b) does not
need the magnetisation because it is a *ratio* at two altitudes for the same
source: whatever the moment is, it cancels. This is the practical value of a
two-altitude survey, and it is why the altitude history of a magnetic mission is
part of the data product.

**(d)** A real crustal source is an extended layer rather than a point dipole, so
its field is the sum over a distribution of dipoles with varying depths,
magnetisations and directions; the half-width and the altitude ratio then depend
on the thickness and the depth distribution together, and a single ratio
over-constrains the model. The magnetisation is also not uniform — it is acquired
during cooling through the Curie temperature and can vary by an order of magnitude
across a province — and remanent directions record the field at the time of
cooling rather than the present one. A mission's response is to fly several
altitudes (including a very low pass where the short-wavelength field dominates),
to combine the magnetic field with gravity and topography to separate source
geometry from magnetisation, and to report a *range* of depths and magnetisations
consistent with the data rather than a single "depth to the top".
