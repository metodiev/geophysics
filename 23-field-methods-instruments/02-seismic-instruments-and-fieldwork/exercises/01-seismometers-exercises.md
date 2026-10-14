# Exercises — 23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS

Attempt these before reading the
[solutions](./01-seismometers-solutions.md). The lesson is
[01 Seismometers](../01-seismometers.md). All sensor parameters, noise levels and
ambient values are **SYNTHETIC**.

Use $|H(f)| = r^{2}/\sqrt{(1-r^{2})^{2} + (2hr)^{2}}$ with $r = f/f_0$ for a
velocity sensor normalised to 1 at high frequency.

## ★ Foundational

**★1.** A velocity sensor has $f_0 = 2.0\ \mathrm{Hz}$ and $h = 0.6$. Compute
$|H|$ at $f = 0.5\ \mathrm{Hz}$, as an absolute number and in dB. State what the
number means physically.

**★2.** For the same sensor, compute the frequency at which $|H| = 1/\sqrt{2}$
on the low-frequency flank (the −3 dB corner). Evaluate $|H|$ at $f_0$ itself,
state whether that value is a peak or a notch, and compute the maximum of the
*displacement* response $|H_d| = |H|/r^{2}$ and the frequency at which it occurs.

## ★★ Applied

**★★3.** The sensor of ★1 has an output noise of
$2.0\times10^{-7}\ \mathrm{V/\sqrt{Hz}}$ and a generator constant
$G = 100\ \mathrm{V/(m/s)}$. Compute the input-referred self-noise at 0.5 Hz.
Then compute the frequency at which the input-referred self-noise equals an
ambient level of $1.0\times10^{-7}\ \mathrm{m/s/\sqrt{Hz}}$, and say what that
frequency means.

**★★4.** The sensor is connected to a $\pm5\ \mathrm{V}$, 24-bit digitizer with
$G = 200\ \mathrm{V/(m/s)}$. Compute the clip velocity, the LSB, the quantisation
noise, the quantisation noise referred to ground velocity, and the resulting
electronic dynamic range in velocity units in dB. Explain why this range is not
the range available for real ground motion.

## ★★★ Research-oriented

**★★★5.** A MEMS accelerometer has an acceleration noise of
$1.0\times10^{-4}\ \mathrm{m/s^{2}/\sqrt{Hz}}$ and a flat acceleration response.
Convert its noise to an equivalent ground-velocity noise at 0.01 Hz and at 1 Hz,
compare each with the ambient model of the lesson
($2.236\times10^{-5}$ and $5.958\times10^{-8}\ \mathrm{m/s/\sqrt{Hz}}$
respectively), and state the band in which this sensor can and cannot resolve
ambient noise.

**★★★6.** Design a field verification test that would detect a deployed sensor
whose response differs from its recorded response: state the measurement, the
reference, the metric with units, the acceptance threshold, the failure modes it
detects, and the two things it cannot test. A specification that could not be
executed during a deployment is a failed answer.
