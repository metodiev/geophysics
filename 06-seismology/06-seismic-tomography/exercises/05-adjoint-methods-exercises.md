# Exercises — 06-06-05 The Adjoint Method for Efficient Sensitivity Computation

Worked answers are in
[05-adjoint-methods-solutions.md](05-adjoint-methods-solutions.md).
The lesson is [05-adjoint-methods.md](../05-adjoint-methods.md) and the
demonstration is
[../code/adjoint_methods_demo.py](../code/adjoint_methods_demo.py).

## ★ Foundational

1. A model has $2.0\times10^{5}$ parameters. Compute the number of forward
   solves a central-difference gradient needs, and compare with the adjoint.
2. The dot-product test returns $+6.07460951\times10^{-1}$ for both
   $\langle J\delta\mathbf{m},\mathbf{w}\rangle$ and
   $\langle \delta\mathbf{m},J^{\mathsf T}\mathbf{w}\rangle$. Compute their
   ratio and state what a value of 1.49 would have meant.
3. The kernel of a 16 Hz travel-time measurement is 120 m wide in a medium of
   local velocity 3.6 km/s. Compute the wavelength and the width/wavelength
   ratio.

## ★★ Applied

4. The gradient test reports a median relative difference of
   $5.58\times10^{-10}$ and a worst case of $2.36\times10^{-6}$. Explain why a
   median and a worst case differ by four orders of magnitude, and which you
   would quote.
5. In the step-length study the cosine between successive gradients is
   $0.991390$ at $f = 10^{-2}$ and $-0.842338$ at $f = 5\times10^{-2}$.
   Estimate the largest $f$ you would use for a descent step, and justify it from
   the two numbers.
6. The adjoint gradient took 0.02 s on a 300-parameter problem while the
   brute-force gradient needed 24 solves for 12 parameters. Estimate the
   brute-force time for all 300 parameters and the speed-up of the adjoint.

## ★★★ Research-oriented

7. The kernel width scales as one wavelength. A colleague wants 50 km resolution
   in the mantle (4.0 km/s shear velocity) using surface waves with a 100 s
   period. Compute the wavelength, compare with the request, and state what
   period would be needed instead.
8. The adjoint field requires the forward field at every time step. Estimate the
   memory for 1000 time steps of $10^{7}$ grid points in single precision, and
   describe one strategy that trades computation for memory without changing the
   gradient.
