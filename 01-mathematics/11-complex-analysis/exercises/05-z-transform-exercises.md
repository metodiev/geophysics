# Exercises — 01-11-05 The z-Transform and Discrete Linear Systems

Attempt these **closed-book**, then open the
[solutions](./05-z-transform-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

For every transform you write down, state the region of convergence, and for
every filter state whether it is stable and why.

---

## ★ Foundational

**★1.** Write $X(z)$ for each sequence and give its region of convergence.

(a) $x[n] = \delta[n]$
(b) $x[n] = \{1, 2, 3\}$ with $x[0]=1$ (i.e. $x[1]=2$, $x[2]=3$, zero elsewhere)
(c) $x[n] = u[n]$
(d) $x[n] = 0.5^{n}u[n]$

---

**★2.** Invert $X(z) = \dfrac{1}{1-0.5z^{-1}}$ for each region of convergence,
and explain what changes.

(a) $|z| > 0.5$
(b) $|z| < 0.5$

---

**★3.** A filter is described by
$y[n] = 0.8\,y[n-1] + x[n] - 0.5\,x[n-1]$.

(a) Find $H(z)$ and express it as a ratio of polynomials in $z$.
(b) List its poles and zeros, and state whether it is stable.
(c) Give the first four values of the impulse response by running the recursion.

---

**★4.** For the FIR filter $y[n] = x[n] - 0.5\,x[n-1]$, write $H(z)$, find the
impulse response, and compute the magnitude response at DC, at
$\omega = \pi/2$ and at Nyquist. Describe the filter in one phrase.

---

## ★★ Applied

**★★5.** A two-point moving average has $H(z) = (1+z^{-1})/2$.

(a) Show that $|H(e^{i\omega})| = |\cos(\omega/2)|$.
(b) At which frequencies does the filter have exact nulls?
(c) The filter is applied twice in series. What is the new transfer function, and
where are its zeros?
(d) Give one geophysical reason to prefer a longer moving average to a two-point
one, and one reason to avoid it.

---

**★★6.** A two-pole resonator has poles at $r e^{\pm i\pi/4}$ with $r = 0.98$, and
samples are taken once per second.

(a) Write $H(z)$ and give the resonance frequency in hertz.
(b) Estimate the peak height with $1/[(1-r)2\sin\omega_{0}]$ and state the
polarity of the error.
(c) Estimate the $-3$ dB bandwidth and $Q$, and compare with the scaling
$Q\approx\omega_{0}/[2(1-r)]$.
(d) Explain what happens to the peak and to $Q$ if $r$ is reduced to $0.9$.

---

**★★7.** Design a two-tap (three-coefficient) non-recursive filter that removes
both DC and the Nyquist frequency.

(a) Write $H(z)$ and locate its zeros.
(b) Give the magnitude response in closed form.
(c) Where is the peak of the magnitude response, and what is its value?
(d) State one situation in seismic processing where a DC null is mandatory, and
one where a Nyquist null would destroy the signal you want.

---

**★★8.** Consider $x = \{1,2,3,4\}$ and $h = \{1,-1\}$.

(a) Compute the linear convolution.
(b) Compute the 4-point circular convolution by hand.
(c) Identify the wrapped samples and check them against your linear answer.
(d) State the smallest transform length that gives the linear result.

---

## ★★★ Research-oriented

**★★★9.** A recursive filter has a single pole at $r = 1.01$ and a record of
5000 samples.

(a) How much has the impulse response grown by the end of the record?
(b) What is the largest pole radius consistent with a growth of at most a factor
of 100 over the record? Express the answer both as a radius and as a percentage
error in the pole position.
(c) A colleague reports the pole as $0.99$ from the same data. Give two
independent diagnostics that would distinguish $0.99$ from $1.01$, given the
impulse response.
(d) Explain why a pole at exactly unity is "marginal" rather than "stable", and
give a geophysical example of a system with a unit-circle pole.

---

**★★★10.** A first-order analogue low-pass with corner frequency $f_{c} = 10$ Hz
is to be discretised at $f_{s} = 100$ Hz by the bilinear transform.

(a) Write the mapping from analogue $\Omega$ to digital $\omega$ and sketch its
behaviour.
(b) Compute the pre-warped analogue corner $\Omega_{c}$ that places the digital
corner exactly at 10 Hz.
(c) Compute where the corner lands if no pre-warping is used.
(d) State the size of the error as a fraction of $f_{c}$, and say whether it
would be acceptable in an anti-alias filter for a 100 Hz-sampled seismic
recording.
(e) A different designer uses the impulse-invariant method instead. Explain what
it preserves and what it aliases, and why pre-warping is not the relevant question
there.

---

## Self-assessment before the solutions

- [ ] I gave a region of convergence for each transform in ★1 and ★2.
- [ ] I checked stability against the unit circle in ★3, ★6 and ★9.
- [ ] I computed ★★8(b) by hand rather than by running a transform.
- [ ] I stated the direction of the bilinear warping (which way the corner moves)
      from the formula, not from memory.
