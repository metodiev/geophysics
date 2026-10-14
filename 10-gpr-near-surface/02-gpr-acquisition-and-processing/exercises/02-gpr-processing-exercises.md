# Exercises — 10-02-02 Processing Steps

Attempt before the [solutions](./02-gpr-processing-solutions.md). Lesson:
[02 Processing Steps](../02-gpr-processing.md). All models **SYNTHETIC**.

## ★ Foundational

**★1.** A trace contains a drift of peak-to-peak amplitude $0.15$ and a first
reflection of amplitude $1.00$. Estimate the fractional amplitude bias on a
reflection of amplitude $0.40$ and state the sign of the bias.

**★2.** State the difference between a constant gain and AGC in one sentence, and
name one quantity that AGC destroys.

**★3.** A band-pass filter raises the signal-to-noise ratio by $12\ \mathrm{dB}$
and widens the pulse from $2.0$ to $3.0\ \mathrm{ns}$. Express the resolution
change in centimetres at $v = 0.075\ \mathrm{m\,ns^{-1}}$.

## ★★ Applied

**★★4.** A reflector dips $25^\circ$ in $v = 0.09993\ \mathrm{m\,ns^{-1}}$.
Compute the time dip, the depth-converted apparent dip, and the imaged dip after
migration with a velocity $5\%$ low.

**★★5.** After migration with the correct velocity, the reflector of ★★4 is
$1.80\ \mathrm{m}$ deep at $x = 0$ against a true $1.75\ \mathrm{m}$. State two
possible causes and how you would distinguish them.

**★★6.** A background-removal filter with a 5-trace window raises the
target-to-clutter ratio from $18$ to $26\ \mathrm{dB}$ while reducing the target
peak from $0.90$ to $0.45$. Compute the implied clutter reduction in dB and state
what this filter would do to a flat-lying target.

## ★★★ Research-oriented

**★★★7.** Design a processing sequence for a $400\ \mathrm{MHz}$ grid survey
with strong horizontal ringing, a drift, and a $6\ \mathrm{dB}$ amplitude
difference between two survey days. Justify each step's position in the sequence
and state which steps must be omitted from a time-lapse comparison.

**★★★8.** Using the tangency relation
$\sin\theta_{\text{mig}} = (v_{\text{mig}}/v)\sin\theta$, compute the velocity
error that would make a $40^\circ$ interface appear vertical, and explain why that
never happens in practice.
