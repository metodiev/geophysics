# Solutions — 20-03-05 Adaptive Filtering and Noise Cancellation

> **Read after attempting the exercises.** Lesson:
> [05 Adaptive Filtering](../05-adaptive-filtering.md).

---

## ★1 — One NLMS step

$$\mathbf{x} = [1,\,-1,\,0.5]^{\top},\quad w = [0,0,0]^{\top}.$$

1. Output: $y = w^{\top}\mathbf{x} = 0$.
2. Error: $e = d - y = 2 - 0 = 2$.
3. Energy: $\mathbf{x}^{\top}\mathbf{x} = 1^2 + (-1)^2 + 0.5^2 = 1 + 1 + 0.25 = 2.25$.
4. Update:
   $$w \leftarrow w + \mu\,\frac{e\,\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}+\varepsilon}
   = 0 + 0.5 \times \frac{2 \times [1,-1,0.5]^{\top}}{2.25}
   = \frac{[1,-1,0.5]^{\top}}{2.25}
   = [0.4444,\,-0.4444,\,0.2222]^{\top}.$$

(The $\varepsilon = 10^{-6}$ guard is negligible here.)

---

## ★2 — Convergence bound and normalisation

For NLMS the bound is $0 < \mu < 2$. The update divides by
$\mathbf{x}^{\top}\mathbf{x}$, so a step of size $\mu$ moves the coefficients by a
fixed *fraction* of the input energy rather than a fixed absolute amount. Scaling
the input by a constant $a$ scales both numerator and denominator, leaving the
update unchanged. Plain LMS, whose step is $\mu e \mathbf{x}$, scales the update by
$a^2$ and therefore has a power-dependent stability bound.

---

## ★3 — Which signal is the output

- **Noise canceller**: the output is the **error** $e = d - y$, because $y$
  estimates the interference and subtracting it leaves the signal.
- **Line enhancer**: the output is the **filter output** $y$, because $y$ estimates
  the predictable (periodic) part and the error is the residual noise.

Getting this backwards produces a plausible-looking but wrong result: a line
enhancer whose error is plotted shows the *noise*, which looks like a failure.

---

## ★4 — Why improvement is not monotonic in $\mu$

Two effects compete:

- **Convergence speed** improves with $\mu$: the coefficients reach the optimal
  vector sooner, so the average error over the record falls. This explains the rise
  from 3.47 dB at $\mu = 0.002$ to 15.87 dB at $\mu = 0.1$.
- **Misadjustment** grows with $\mu$: the instantaneous gradient estimate is noisy,
  and a large step lets that noise wander the coefficients around the optimum,
  raising the steady-state error. This explains the fall from 15.87 dB at
  $\mu = 0.1$ to 11.57 dB at $\mu = 1.0$.

The optimum is where the two cross. It is not at the edge of stability
($\mu = 2$), which is why quoting the bound is not a design rule.

---

## ★5 — Why $M = 128$ is worse

The interference path is 9 samples, so $M = 8$ has one coefficient more than
needed. The extra 120 coefficients of the $M = 128$ filter have nothing left to
model; they adapt to whatever residual correlation the finite record happens to
contain — i.e. to noise. With a *fixed* $\mu = 0.02$, the larger filter also
converges more slowly, so within 4000 samples it has not settled: the excess error
of the transition is added to the excess error of over-parameterisation.

**It does not mean longer is always worse.** The correct reading is that (i) the
length should match the path, and (ii) if a longer filter is required (unknown
path length), $\mu$ must be retuned, typically upward, to keep the convergence
time acceptable.

---

## ★6 — Reference leakage

If the reference $x$ contains a component $\alpha s$ of the desired signal, then
$y$ will predict that component along with the interference, and the output
$e = d - y$ will contain $s - \widehat{\alpha s} \approx s - \alpha s$. The
canceller therefore *attenuates* the signal by roughly a factor $(1-\alpha)$ in the
overlapping band, and in the worst case (strong overlap and enough adaptation) can
almost null it.

Test from data alone:

1. Run the canceller normally and record the output.
2. Run it again with the **reference delayed** by more than the interference's
   correlation length. If the output signal reappears, the signal was being
   removed through the reference (a lag longer than the interference correlation
   breaks the interference prediction but not the signal leakage, which persists at
   all lags).
3. Compare the mean amplitude of a strong, isolated coherent event before and
   after cancellation. A systematic loss of coherent energy — not of noise — is the
   signature.

---

## ★★★7 — Excess mean squared error scaling

To first order, the steady-state excess mean squared error of NLMS is

$$\xi_{\text{ex}} \approx \frac{\mu}{2}\,\xi_{\min},$$

so it scales **linearly** with $\mu$. In decibels, halving $\mu$ reduces the excess
by about 3 dB.

The demo's cumulative-error floors at iteration 3999 are $-20.87$ dB
($\mu = 0.05$) and $-15.74$ dB ($\mu = 0.005$). Taking the smaller-step curve as
close to $\xi_{\min}$, the larger step's excess is

$$-15.74 - (-20.87) = 5.13\ \text{dB}.$$

The linear prediction for a tenfold increase in $\mu$ is $10\times$, i.e.
$10\log_{10}10 = 10$ dB, so the measured 5.13 dB is consistent in sign and order
with the first-order model but smaller, because the $\mu = 0.005$ curve has not
fully converged and therefore overstates $\xi_{\min}$. The scaling direction —
larger step, larger excess — is what the measurement supports.

---

## ★★★8 — Tracking a path that changes every 2 s

Let the record have $f_s = 500$ Hz, so a 2 s stationarity interval is 1000
samples.

- **Length $M$**: enough to span the path. If the path is unknown but physically
  bounded (say a 40 ms travel path), $M = 0.04 \times 500 = 20$ coefficients.
  Extra length slows convergence without benefit.
- **Step $\mu$**: convergence needs roughly $M/\mu$ samples. To settle within
  1000 samples with $M = 20$, require $\mu \gtrsim 0.02$. The misadjustment grows
  with $\mu$, so choose the smallest $\mu$ that converges in the available window:
  $\mu \approx 0.05$ gives a convergence time of about 400 samples, with margin.

The joint argument is therefore: **$M$ from the physical path length, then $\mu$
from the requirement $M/\mu \ll$ stationarity interval, then check the
misadjustment is below the conversion-amplitude floor.** If it is not, the options
are a longer stationarity window (if the physics allows) or a different algorithm
(recursive least squares converges in about $M$ samples instead of $M/\mu$).