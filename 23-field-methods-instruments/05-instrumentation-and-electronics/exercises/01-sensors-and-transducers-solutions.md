# Solutions — 23-05-01 Sensors and Transducers: Principles and Selection

The lesson is [01 Sensors and Transducers](../01-sensors-and-transducers.md). All
values are **SYNTHETIC**.

## ★1

$$\text{range} = 20\log_{10}\frac{2\times10^{-3}}{5\times10^{-9}}
= 20\log_{10}(4\times10^{5}) = 112.04\ \mathrm{dB},$$

$$\text{bits} = \frac{112.04}{6.0206} = 18.61 \;\Rightarrow\; \log_2(4\times10^{5}) = 18.61 .$$

A real system needs more because the equivalent-bit count is a *resolution* claim,
not an *accuracy* claim: noise, non-linearity, gain drift and the sensor's own offset
all consume range, and the converter must have headroom above the signal. The 33-bit
entry in the demonstration's table is a good example of a number that cannot be
delivered by any single converter and must be built by a ratiometric or locked
measurement.

## ★2

$$\Delta R = G_F R \varepsilon = 2.1 \times 120 \times 50\times10^{-6}
= 0.0126\ \Omega,$$

$$V_{\text{out}} = \frac{V\,\Delta R}{4R}
= \frac{2.5 \times 0.0126}{4 \times 120} = 6.5625\times10^{-5}\ \mathrm{V}
= 65.6\ \mathrm{\mu V}.$$

This matches the demonstration's scaling: 1000 µε at $G_F = 2$ and 5.0 V gives
2.5 mV, and here 50 µε at $G_F = 2.1$ and 2.5 V is 20× smaller in strain, 2× smaller
in excitation and 1.05× larger in $G_F$.

## ★3

A full bridge puts all four arms active with alternating signs, so the four
$\pm V\Delta R/(4R)$ contributions add:

$$V_{\text{out}} = \frac{V\,G_F\varepsilon}{1} = 2.5 \times 2.1 \times 50\times10^{-6}
= 2.625\times10^{-4}\ \mathrm{V} = 262.5\ \mathrm{\mu V},$$

exactly **4×** the quarter-bridge output of 65.6 µV. The factor comes from the fact
that a quarter bridge wastes three arms on fixed resistors: the bridge subtracts
opposite arms, so with one active arm only one quarter of $\Delta R/R$ appears at the
output. A half bridge (two active, opposite) gives 2×. In practice the four gauges must
be identical and the strain field must have the required signs, which is why full
bridges are standard for load cells and pressure diaphragms but not for arbitrary
field surfaces.

## ★4

$$f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi \times 5\times10^{8} \times 2\times10^{-9}}
= \frac{1}{2\pi \times 1.0\ \mathrm{s}} = 0.1592\ \mathrm{Hz}.$$

The high-pass magnitude of the transimpedance stage is

$$\left|\frac{j f/f_c}{1 + j f/f_c}\right| = \frac{f/f_c}{\sqrt{1+(f/f_c)^{2}}} ,$$

so at 0.05 Hz ($f/f_c = 0.3142$): $0.3142/\sqrt{1.0987} = 0.2997$, i.e. **29.97 %**;
at 1 Hz ($f/f_c = 6.2832$): $6.2832/\sqrt{40.48} = 0.9876$, i.e. **98.76 %**. These
are the $0.2997$ and $0.9876$ values in the demonstration's table.

A 0.01 Hz signal would be at $f/f_c = 0.0628$, a response of 6.27 % and −24 dB: the
sensor **cannot** measure it usefully. The conclusion is that a piezoelectric sensor
measures *changes* above its corner, and the corner is a property of the *cable and
amplifier* as much as of the crystal — lengthening the cable adds capacitance, which
raises the corner and destroys the low-frequency response.

## ★5

$$v_n = \sqrt{4kTRB}
= \sqrt{4(1.380649\times10^{-23})(290)(5000)(100)}
= 8.949\times10^{-8}\ \mathrm{V} = 89.5\ \mathrm{nV}.$$

The quarter-bridge channel of ★2 has $V_{\text{out}}/V = G_F\varepsilon/4$, so at
$V = 2.5$ V the sensitivity in volts per unit strain is
$2.1 \times 2.5/4 = 1.3125$ V. Setting $1.3125\,\varepsilon_{\min} = 89.5\times10^{-9}$
gives

$$\varepsilon_{\min} = 6.82\times10^{-8} = 0.068\ \mathrm{\mu\varepsilon}.$$

The resistor here is the gauge itself (120 Ω), so the 89.5 nV figure belongs to a
5 kΩ resistor and is *not* the gauge's noise: a 120 Ω resistor in the same band is
$\sqrt{120/5000} = 0.155\times$ smaller, i.e. 13.9 nV. The dominant term is therefore
**not** the gauge's own Johnson noise but the amplifier's input voltage noise and the
bridge's excitation noise; the calculation shows that a 100 Hz-band strain channel can
in principle resolve ~0.01 µε, and that real performance is set by everything else in
the chain. Compare the lesson's point that high-resistance sensors need low input
noise *voltage* while low-resistance sensors draw more current noise.

## ★6

A model answer:

| Item | Choice | Justification |
|---|---|---|
| Principle | capacitive (or piezoresistive) diaphragm pressure sensor with a temperature-compensated reference | DC response is required (the static head), so piezoelectric is excluded |
| Band | DC to ~1 Hz, sampled at ≥10 Hz | the science is the static and tidal head |
| Full scale | 40 m of water ≈ 0.4 MPa; use a 0.6 MPa range for headroom | 0.6/0.4 gives room for the atmospheric reference and the tidal range |
| Dynamic range | $20\log_{10}(6\times10^{5}/1) = 115.6$ dB, i.e. 19.2 bits | the resolution requirement is 1 Pa |
| Environmental threat | temperature, through the diaphragm stiffness, the fluid density and the reference cavity | the governing quantity is the temperature coefficient of the zero and span |
| Calibration | two points at the deployment temperature: ambient pressure and a known head, recorded with the sensor installed | the offset dominates a pressure measurement |
| Service check | repeat the ambient-pressure zero check at each visit and log the temperature | it detects zero drift and temperature dependence together |

Alternatives rejected: **piezoelectric** cannot hold DC; **optical fibre pressure**
sensors are attractive for long-term stability and EMI immunity but require a
readout whose own temperature drift must then be characterised, and the cost is
higher. The answer must state which term dominates the budget and how the service
check detects it.
