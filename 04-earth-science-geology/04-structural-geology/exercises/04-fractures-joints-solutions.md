# Solutions — 04-04-04 Fractures, Joints and Their Geophysical Signature

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All material parameters are TYPICAL values.

---

## ★1 — Griffith and Irwin

**(a)** For $a = 10^{-3}$ m:
$\sigma_c = \sqrt{2 \times 50 \times 10^9 \times 10/(\pi \times 10^{-3})} =
\sqrt{3.183 \times 10^{14}} = 1.784 \times 10^7$ Pa $= 17.84$ MPa. For
$a = 0.1$ m: $\sqrt{3.183 \times 10^{11}} = 5.64 \times 10^5$ Pa $= 0.564$ MPa.
The demo prints `17.84` and `0.56`.

**(b)** $K_I = 17.84 \times 10^6\sqrt{\pi \times 10^{-3}} = 1.000 \times 10^6$
Pa m$^{0.5}$, and $0.564 \times 10^6\sqrt{\pi \times 0.1} = 1.000 \times 10^6$.
The demo's third column is `1.0000` on every row, which is the point: the two
criteria are the same statement.

**(c)** $K_{Ic} = \sqrt{2E\gamma_s} = \sqrt{2 \times 50 \times 10^9 \times 10} =
1.000 \times 10^6$ Pa m$^{0.5} = 1.00$ MPa m$^{0.5}$, against the tabulated
`1.50` MPa m$^{0.5}$.

**(d)** The discrepancy is the **process zone**. Around a real crack tip, rock
microcracks before the main crack advances, and the energy dissipated in
producing that microcrack population is not captured by the ideal surface energy
$\gamma_s$. The measured toughness is therefore larger than $\sqrt{2E\gamma_s}$
computed from surface energy alone — a factor of 1.5 here, and larger for coarser
or more porous rocks. This is also why the strength of a laboratory specimen
usually exceeds the Griffith prediction, and why strength is scale-dependent.

---

## ★2 — The isotropic background

**(a)** $c_{11} = 20 + 40 = 60$ GPa $= 6.0 \times 10^{10}$ Pa; $c_{44} = \mu =
20$ GPa.

**(b)** $V_p = \sqrt{6.0 \times 10^{10}/2600} = 4803.8$ m s$^{-1}$ and
$V_s = \sqrt{2.0 \times 10^{10}/2600} = 2773.5$ m s$^{-1}$, exactly the demo's
background values.

**(c)** For horizontal fractures, the S wave polarised in the plane containing the
fracture normal (S polarized vertically in a horizontal path, or in the
normal–path plane) is the **one affected**; the S wave polarised within the
fracture plane is not. Equivalently $C_{44} = C_{55}$ is reduced while $C_{66}$
is not.

**(d)** Because the two S modes then travel at different speeds over the same
path, so the S wave arrives as two pulses separated in time. The magnitude of that
separation is the splitting, and it is a direct measure of the excess compliance
$Z_T$.

---

## ★3 — Compliances

**(a)** $\Delta S_{NN} = 1/(50 \times 10^9 \times 10) = 2.0 \times 10^{-12}$
Pa$^{-1}$.

**(b)** $Z_N = c_{11}/(k_n s) = 60 \times 10^9/(50 \times 10^9 \times 10) =
0.12$. Dimensionless: c$_{11}$ is in Pa and $k_n s$ is in Pa m$^{-1} \times$ m
$=$ Pa, so the ratio is dimensionless. This is the demo's `0.12000` at spacing 10 m.

**(c)** $Z_T = 60 \times 10^9/(20 \times 10^9 \times 10) = 0.30$, the demo's
`0.30000`.

**(d)** The seismic wavelength must be much greater than the fracture spacing,
which at seismic frequencies (wavelengths of tens to hundreds of metres) is
usually satisfied and at ultrasonic frequencies in a centimetre-sized specimen is
usually not. Applying the model outside this regime is the most common
misapplication.

---

## ★4 — The demo

**(a)** `Vp(vertical) = 4803.844614 m/s`, `Vp(horizontal) = 4803.844614 m/s`,
`Vs(vh) = 2773.500981 m/s`, `Vs(h) = 2773.500981 m/s`, with the anisotropy at
`+2.220e-16` (round-off). This verifies that the tensor bookkeeping returns the
isotropic background when there is no excess compliance — any error would appear
as a spurious anisotropy in an unfractured rock.

**(b)** At 100 m: $Z_N = 0.012$, $Z_T = 0.030$, P anisotropy $-0.634$ per cent. At
10 m: $0.12$, $0.30$, $-5.845$ per cent. At 1 m: $1.2$, $3.0$, $-33.773$ per cent.
Both compliances and the anisotropy grow in proportion to $1/s$; the anisotropy
magnitude grows faster than linearly because it is a ratio of velocities obtained
by inverting a compliance that is itself increasing.

**(c)** `gamma exact 0.075000` and `gamma computed 0.075000` at spacing 20 m
($Z_T = 0.15$), with a splitting of `0.026097 ms/m`.

**(d)** $Z_N$ goes on $S_{33}$, $Z_T$ on $S_{44}$ and $S_{55}$. The normal
compliance reduces $C_{33}$ (the vertical stiffness) while $C_{11}$ is reduced
much less, so the vertical velocity falls more than the horizontal and
$V_p(\text{v})/V_p(\text{h}) - 1$ is negative — the sign the table shows. A set of
vertical fractures puts the excess compliance on $S_{11}$, $S_{55}$ and $S_{66}$
instead, reversing the sign for a vertical-well measurement.

---

## ★5 — The cubic law

**(a)** $k = (0.5 \times 10^{-3})^3/(12 \times 1) = 1.25 \times 10^{-10}/12 =
1.042 \times 10^{-11}$ m², which is the demo's `1.042e-11`, equal to
`10.5547` darcy.

**(b)** $b = 1$ mm: $k = 8.333 \times 10^{-11}$ m², larger by a factor of 8.
Doubling the aperture multiplies the permeability by eight.

**(c)** $s = 0.1$ m: $k = 1.042 \times 10^{-10}$ m², larger by a factor of 10 —
the permeability is inversely proportional to spacing, which is a much weaker
dependence than the cube.

**(d)** First, fracture permeability is dominated by the largest apertures, so a
mean aperture carries almost no information about transport. Second, a
core-scale measurement cannot be extrapolated to a reservoir, because the
transport is carried by the part of the aperture distribution that a core is least
likely to sample.

---

## ★6 — Spacing statistics

**(a)** An **empirical relation**. Its form — proportionality — follows from the
mechanical argument that a layer stops cracking when the stress transferred to the
interface can no longer break the next site, but the constant depends on the
formation, the loading history and the stiffness contrast between the layer and
its neighbours, and must be calibrated locally.

**(b)** Because the fit quality describes the trend and the range describes the
predictive error. A worker who uses "0.8 times the thickness" and does not know
that the ratio spans 0.52 to 1.02 will be wrong by a factor of two in the worst
case, while $r^2 = 0.99$ gives a false impression of reliability.

**(c)** Perfectly regular: $\sigma = 0$, so $C_v = 0$. Poisson with unit mean:
$\sigma = \mu = 1$, so $C_v = 1$. The demo's synthetic sets give
`0.046`, `0.946` and `0.748` for the regular, Poisson and clustered populations.
$C_v$ indicates the *shape* of the spacing distribution and nothing more; a value
below about 0.5 is conventionally read as "saturated", and that reading cannot
distinguish a saturated set from one whose spacing was inherited.

**(d)** Poisson: $\exp(-2/1) = 0.135$. Regular: $\max(0, 1 - 1/2) = 0.500$. Same
mean spacing, different connectivity — and connectivity is what a permeability or
block-size calculation depends on, because a flow path that must cross intact rock
is a different problem from one that does not. This is why the distribution, not
the mean, is the input.

---

## ★7 — Deriving the compliances

**(a)** A fracture behaves as a spring of stiffness $k_n$ per unit area, so under a
normal stress $\sigma_n$ it closes by $u = \sigma_n/k_n$. A stack of fractures
spaced $s$ apart transmits its displacement through the medium; the total
displacement across a length $L$ containing $N = L/s$ fractures is
$u_{\text{total}} = N\sigma_n/k_n = \sigma_n L/(k_n s)$, so the added strain is
$\sigma_n/(k_n s)$ and the added compliance is $1/(k_n s)$. The fracture strains
add because they are in series along the stress path.

**(b)** The background strain for the same stress is $\sigma_n/c_{11}$, so the
ratio of added to background compliance is
$Z_N = (\sigma_n/(k_n s))/(\sigma_n/c_{11}) = c_{11}/(k_n s)$. Dimensions:
[Pa]/[Pa m$^{-1}$ m] $=$ [Pa]/[Pa] $= 1$, dimensionless, as a ratio of
compliances must be.

**(c)** For normals along axis 3: $Z_N$ on $S_{33}$, and $Z_T$ on $S_{44}$ and
$S_{55}$. For normals along axis 1 the roles rotate: $Z_N$ would go on $S_{11}$
and $Z_T$ on $S_{66}$ and $S_{55}$. The medium is no longer VTI but HTI, and the
Thomsen parameters are defined only after rotating into the symmetry frame.

**(d)** With $Z_N$ on $S_{33}$ only, the shear block $\{44, 55\}$ is modified
independently of the $\{66\}$ element, so $C_{66} = C_{66}^0$ is untouched while
$C_{44} = 1/(S_{44}^0(1 + Z_T)) = C_{44}^0/(1 + Z_T)$. Then

$$\gamma = \frac{C_{66} - C_{44}}{2C_{44}} =
\frac{C_{44}^0 - C_{44}^0/(1+Z_T)}{2C_{44}^0/(1+Z_T)} =
\frac{(1 + Z_T) - 1}{2} = \frac{Z_T}{2}.$$

The demo confirms this to six decimals at every spacing:
`0.1500      0.075000        0.075000`, and so on.

---

## ★8 — From splitting to stiffness

**(a)** Five per cent splitting means the fast and slow S velocities differ by
5 per cent. Over 50 m with $V_{S,\text{slow}} = 3000$ m s$^{-1}$, the fast is
$3150$ m s$^{-1}$ (or the slow is 5 per cent below the fast, depending on which is
taken as the reference — **state which**). The delay is

$$\Delta t = 50\left(\frac{1}{3000} - \frac{1}{3150}\right) = 50 \times
(3.3333 - 3.1746) \times 10^{-4} = 7.94 \times 10^{-3} \text{ s}
= 7.9 \text{ ms}.$$

**(b)** The splitting is
$(1/V_{\text{slow}} - 1/V_{\text{fast}})L = L(\sqrt{1+Z_T} - 1)/V_{S,0}$ for the
horizontal-fracture configuration, so

$$\sqrt{1 + Z_T} - 1 = \frac{3000 \times 7.94 \times 10^{-3}}{50} = 0.476,$$

giving $\sqrt{1+Z_T} = 1.476$, $Z_T = 1.179$. With $c_{11} = 60$ GPa,
$k_t s = c_{11}/Z_T = 5.09 \times 10^{10}$ Pa, so at $s = 1$ m the implied shear
stiffness is 51 GPa m$^{-1}$ — larger than the TYPICAL 20 GPa m$^{-1}$ assumed in
the demo, i.e. the observed splitting corresponds to a *less* compliant fracture
set than the demo's default.

**(c)** The chain is: measured delay → splitting → $Z_T$ (assuming a VTI single
set) → $k_t s$ (assuming $c_{11}$ from an isotropic background) → fracture
density (assuming a value of $k_t$). The largest uncertainty is the **assumed
$k_t$**, because fracture stiffness varies with aperture, roughness and infill by
orders of magnitude and is essentially never measured in situ. The background
$c_{11}$ is a smaller problem, because it is measurable from the same log.

**(d)** A direct measurement of fracture spacing and aperture — from a borehole
image log or a core — which constrains the product $k_t s$ and lets the inversion
be run in the direction it is actually determined: measure the geometry, and use
the splitting to constrain the stiffness rather than the reverse. Reporting a
fracture density from anisotropy alone is reporting a density for a stated but
unmeasured stiffness, and the lesson's §7 says so.
