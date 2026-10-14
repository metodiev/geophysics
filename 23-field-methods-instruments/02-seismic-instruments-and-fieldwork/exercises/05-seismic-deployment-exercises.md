# Exercises — 23-02-05 Deployment, Orientation, Timing and Metadata

Attempt these before reading the
[solutions](./05-seismic-deployment-solutions.md). The lesson is
[05 Seismic Deployment](../05-seismic-deployment.md). All values are
**SYNTHETIC**.

## ★ Foundational

**★1.** A station's north component is oriented with an error of 8°. Compute
$\sin\delta$ and the transverse-to-radial ratio in dB. State whether a signal of
that size could be mistaken for shear-wave splitting.

**★2.** A 40-station deployment runs for 60 days with a per-station-day
probability of losing clock lock of 0.02. Compute the expected number of
station-days with a loss and the expected number of *stations* affected.

## ★★ Applied

**★★3.** A clock with a fractional error of $2.0\times10^{-6}$ runs unlocked for
36 hours. Compute the accumulated timing error in seconds and in samples at a
200 sps sample rate. Then compute the drift over the whole 60-day deployment if
the lock were never re-acquired, and state whether such a station is usable for
absolute-time work.

**★★4.** A ground-coupling resonance sits at $f_c = 15\ \mathrm{Hz}$ with damping
$h_c = 0.6$. Compute $|H_c|$ and the deviation in dB at 5 Hz, and state the
frequency below which the deviation is smaller than 1 dB.

## ★★★ Research-oriented

**★★★5.** You are deploying a three-component broadband station on soft ground in
a site with cultural noise. Specify the installation, the orientation measurement
with its method and uncertainty, the clock protocol including what is logged and
when, the levelling tolerance you will work to, and the acceptance test that
decides whether the station is good enough to keep. Justify each number with the
arithmetic of this lesson.

**★★★6.** Specify a field audit of the metadata of 20 already-deployed stations:
state the items you would check, how you would verify each (measurement versus
document), the scoring rule, the metrics you would report, and the two classes of
error the audit cannot detect. A specification that could not be executed during a
maintenance visit is a failed answer.
