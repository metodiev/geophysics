# Exercises — 06-06-04 Full-Waveform Inversion: Objective Functions and Reliability

Worked answers are in
[04-full-waveform-inversion-solutions.md](04-full-waveform-inversion-solutions.md).
The lesson is
[04-full-waveform-inversion.md](../04-full-waveform-inversion.md) and the
demonstration is
[../code/full_waveform_inversion_demo.py](../code/full_waveform_inversion_demo.py).

## ★ Foundational

1. The demonstration grid has 600 nodes at 10 m spacing and a maximum velocity
   of 3200 m/s. Verify the time step $\Delta t = 0.8\,\Delta x/c_{\max}$, and
   state the stability condition you checked.
2. The Ricker wavelet peaks 1.2/$f_0$ after its nominal origin. For a 20 Hz
   source, compute the peak delay and compare with the measured 1.105 s arrival
   of the first primary against the predicted 1.000 s.
3. Compute the dominant wavelength of a 20 Hz wavelet in a 2600 m/s layer, and
   state how many grid points per wavelength the scheme uses.

## ★★ Applied

4. From the landscape table, compute the arrival-time shift corresponding to the
   first secondary minimum at 8, 16 and 32 Hz, and compare with 1/$f_c$. What is
   the basin half-width in milliseconds at each band?
5. The starting model in the continuation test is 48 ms off in arrival time.
   Predict which bands can and cannot recover from that starting point using the
   measured basin widths, and check your prediction against the reported
   outcomes.
6. The final-misfit normalisation block reports 0.065, 0.075 and 1.122 for the
   same residual. Explain what each denominator is, and which one you would
   require in a paper.

## ★★★ Research-oriented

7. The depth–velocity family in §6 preserves both the two-way time and the
   reflection coefficient, and only the true depth fits the windowed waveform
   (residual/trace rms 0.00 against 1.0-1.4 for the others). Explain the
   mechanism, and design a test to decide whether the same information survives
   in the presence of 10 per cent random amplitude error on every trace.
8. Design a frequency-continuation schedule for a data set with a starting-model
   error of at most 0.4 s and usable energy from 4 to 40 Hz, using the measured
   basin widths (115, 63, 27 ms at 8, 16, 32 Hz). State the criterion for
   advancing to the next band.
