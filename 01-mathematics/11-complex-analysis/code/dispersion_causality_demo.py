"""Causality and dispersion: Kramers-Kronig, verified in both directions.

Run:  python3 dispersion_causality_demo.py
Requires: Python standard library only (``cmath``, ``math``).

Companion to lesson 01-11-06 (Dispersion Relations and Causality in Wave
Physics).

Convention
----------
Time dependence is exp(-i omega t), the convention of the Fourier module in
this repository, so the field of a wave travelling in +x is
exp(i(kx - omega t)).  With that convention a causal linear response
h(t) = 0 for t < 0 has transform H(omega) = int_0^inf h(t) exp(-i omega t) dt
that is analytic in the *lower* half of the complex omega plane, and the
Kramers-Kronig relation reads

    Re H(omega) = -(2/pi) P int_0^inf  omega' Im H(omega') / (omega'^2 - omega^2) d omega'.

Every sign in this file is measured, not asserted: each relation is tested
against a closed form whose real and imaginary parts are known exactly.

Principal values
----------------
`pv_even` evaluates P int_0^inf g(omega')/(omega'^2 - omega^2) d omega' for a
g with g(omega) = 0, using the substitution omega' = tan u (which maps the
infinite range onto a finite one exactly) together with the subtraction
g(omega') -> g(omega') - g(omega), whose omitted term carries the principal
value because P int_0^inf d omega' / (omega'^2 - omega^2) = 0.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return total * h / 3.0


def pv_even(g, w, n=200000):
    """P int_0^inf g(w')/(w'^2 - w^2) dw' for g with g(w) = 0.

    Substitutes w' = tan u and evaluates the limit g'(w)/(2w) at the single
    node where the denominator vanishes.
    """
    def value(u):
        wp = math.tan(u)
        den = wp * wp - w * w
        if abs(den) < 1e-14:
            h = 1e-7
            return ((g(math.tan(u + h)) - g(math.tan(u - h))) / (2 * h)) / (2 * w)
        return g(wp) / den * (1.0 + wp * wp)

    return simpson(value, 0.0, math.pi / 2, n)


def inverse_fourier(spec, t, omega_max, n=200000):
    """(1/2 pi) int_{-inf}^{inf} spec(omega) exp(i omega t) d omega by Simpson."""
    re = simpson(lambda w: (spec(w) * cmath.exp(1j * w * t)).real, -omega_max, omega_max, n)
    im = simpson(lambda w: (spec(w) * cmath.exp(1j * w * t)).imag, -omega_max, omega_max, n)
    return (re + 1j * im) / (2 * math.pi)


def main():
    tau = 1.0

    def H(w):
        return 1.0 / (1.0 + 1j * w * tau)

    section("1. A causal response and where its singularity sits")
    print("  h(t) = (1/tau) exp(-t/tau) for t >= 0, tau = 1")
    print("  H(omega) = int_0^inf h(t) exp(-i omega t) dt = 1/(1 + i omega tau)")
    print(f"  Conjugate symmetry H(-w) = conj(H(w)): checks at")
    ok = True
    for w in (0.3, 1.7, 6.0):
        lhs, rhs = H(-w), H(w).conjugate()
        ok = ok and abs(lhs - rhs) < 1e-15
        print(f"    w = {w:>4.1f}: H(-w) = {lhs.real:+.9f}{lhs.imag:+.9f}i,"
              f" conj H(w) = {rhs.real:+.9f}{rhs.imag:+.9f}i,"
              f" difference {abs(lhs - rhs):.1e}")
    print("  Pole of H: 1 + i omega tau = 0 gives omega = i/tau = +i, in the")
    print("  UPPER half plane.  A causal transform is analytic in the LOWER")
    print("  half plane, so the pole is exactly where the derivation of the")
    print("  dispersion relation needs it to be: on the wrong side.")

    section("2. Causality measured in the time domain")
    print("  Numerically inverting H at times on both sides of zero:")
    print(f"  {'t':>8} {'numeric h(t)':>32} {'exact':>18}")
    for t in (-2.0, -1.0, -0.5, 0.25, 1.0, 2.0):
        num = inverse_fourier(H, t, omega_max=2000.0, n=200000)
        exact = (1.0 / tau) * math.exp(-t / tau) if t >= 0 else 0.0
        print(f"  {t:>8.2f} {num.real:>18.12f}{num.imag:>+13.2e}i"
              f" {exact:>18.12f}")
    print("  For t < 0 the quadrature returns zero to about 1e-4, limited by the")
    print("  truncation of the omega integral, not by physics: the integrand there")
    print("  is exp(i omega t)/(1 + i omega tau), whose slow 1/omega decay leaves")
    print("  an oscillatory tail of order 1/(2 pi omega_max) = 8e-5 here.  The exact")
    print("  is zero by inspection, because the closed contour for t < 0 can be")
    print("  taken in the half plane that contains no singularity.")

    section("3. Kramers-Kronig, both directions, to twelve digits")
    print("  Re H(w) = -(2/pi) P int_0^inf w' Im H(w')/(w'^2 - w^2) dw'")
    print(f"  {'omega':>8} {'Re H (exact)':>20} {'-(2/pi) P.V.':>20}"
          f" {'difference':>12}")
    worst1 = 0.0
    for w in (0.1, 0.3, 1.0, 2.5, 10.0, 100.0):
        fw = w * H(w).imag
        g = lambda wp: wp * H(wp).imag - fw
        val = -(2 / math.pi) * pv_even(g, w)
        worst1 = max(worst1, abs(H(w).real - val))
        print(f"  {w:>8.2f} {H(w).real:>20.14f} {val:>20.14f}"
              f" {abs(H(w).real - val):>12.2e}")
    print(f"  worst difference: {worst1:.2e}")
    print("\n  Im H(w) = +(2w/pi) P int_0^inf Re H(w')/(w'^2 - w^2) dw'")
    worst2 = 0.0
    for w in (0.1, 0.3, 1.0, 2.5, 10.0, 100.0):
        fw = H(w).real
        g = lambda wp: H(wp).real - fw
        val = (2 * w / math.pi) * pv_even(g, w)
        worst2 = max(worst2, abs(H(w).imag - val))
        print(f"  {w:>8.2f} {H(w).imag:>20.14f} {val:>20.14f}"
              f" {abs(H(w).imag - val):>12.2e}")
    print(f"  worst difference: {worst2:.2e}")
    print("  The pair is not a numerical coincidence: it is the statement that")
    print("  the attenuation and the dispersion of this response carry the same")
    print("  information, with fixed relative weight.")

    section("4. The log-amplitude / phase pair (minimum phase)")
    print("  For a response with no zeros in the lower half plane,")
    print("  arg H(w) = (2w/pi) P int_0^inf ln|H(w')|/(w'^2 - w^2) dw'.")
    print("  Here ln|H| = -0.5 ln(1 + w^2) and arg H = -arctan(w).")
    print(f"  {'omega':>8} {'nodes':>9} {'arg H (exact)':>18} {'(2w/pi) P.V.':>18}"
          f" {'difference':>12}")
    for w in (0.3, 1.0):
        for n in (100000, 1000000):
            fw = math.log(abs(H(w)))
            g = lambda wp: math.log(abs(H(wp))) - fw
            val = (2 * w / math.pi) * pv_even(g, w, n=n)
            print(f"  {w:>8.2f} {n:>9} {cmath.phase(H(w)):>18.12f}"
                  f" {val:>18.12f} {abs(cmath.phase(H(w)) - val):>12.2e}")
    print("  The residual falls only like the node spacing, not like its fourth")
    print("  power, because ln|H| decays logarithmically: the transformed")
    print("  integrand has a logarithmic endpoint singularity.  This is a real")
    print("  property of dispersion relations for attenuation, not an artefact of")
    print("  the quadrature, and it is why the integrals converge slowly.")

    section("5. A response that is real and frequency-dependent is non-causal")

    def H_bad(w):
        return 1.0 / (1.0 + w * w * tau * tau)

    print("  Take Re H(w) = 1/(1 + w^2) and set Im H(w) = 0.  This is a")
    print("  perfectly reasonable-looking frequency response.")
    print("\n  (a) The conjugate KK relation then demands a non-zero Im H:")
    print(f"  {'omega':>8} {'Im H implied':>18} {'0 (assumed)':>14} {'conflict':>12}")
    for w in (0.1, 0.5, 1.0, 3.0):
        fw = H_bad(w)
        g = lambda wp: H_bad(wp) - fw
        val = (2 * w / math.pi) * pv_even(g, w)
        print(f"  {w:>8.2f} {val:>18.12f} {0.0:>14.12f} {abs(val):>12.2e}")
    print("  The implied imaginary part is not zero and is not small: the")
    print("  conjugate relation that a causal response must satisfy would require")
    print("  Im H(w) = -w/(1 + w^2), which is the imaginary part of the causal")
    print("  response 1/(1 + i w) studied in Sections 1 to 3.")
    print("\n  (b) Its impulse response is the two-sided exponential, which is")
    print("      non-zero for t < 0:")
    print(f"  {'t':>8} {'numeric h(t)':>18} {'(1/2)exp(-|t|)':>18}")
    for t in (-3.0, -1.5, -0.5, 0.0, 0.5, 1.5, 3.0):
        num = inverse_fourier(H_bad, t, omega_max=2000.0, n=200000)
        print(f"  {t:>8.2f} {num.real:>18.12f}"
              f" {0.5 * math.exp(-abs(t)):>18.12f}")
    print("  A frequency-dependent real response cannot be causal.  Only a")
    print("  frequency-independent real response (a constant modulus) is both")
    print("  real and causal, and a constant modulus means no attenuation.")

    section("6. The standard linear solid: attenuation, dispersion and dissipation")
    M_R, tau_e, tau_s = 1.0, 0.5, 0.25
    M_U = M_R * tau_e / tau_s

    def M(w):
        """Complex modulus for sigma + tau_s sigma' = M_R (eps + tau_e eps')."""
        return M_R * (1 - 1j * w * tau_e) / (1 - 1j * w * tau_s)

    C = M_R * (tau_e - tau_s) / tau_s ** 2
    eps0 = 1.0
    print(f"  M_R = {M_R}, tau_e = {tau_e}, tau_s = {tau_s},"
          f" so M_U = {M_U}")
    print("  Constitutive law: sigma + tau_s sigma' = M_R (eps + tau_e eps').")
    print("  Its causal solution is")
    print("    sigma(t) = M_U eps(t) - C int_{-inf}^{t} exp(-(t-s)/tau_s) eps(s) ds")
    print(f"  with C = {C}, and the complex modulus is M(w) = M_R (1 - i w tau_e)/(1 - i w tau_s).")
    print("\n  Time-domain integration of the constitutive equation versus the")
    print("  modulus description, eps = cos(w t).  The memory integral")
    print("      I(t) = int_{-inf}^{t} exp(-(t-s)/tau_s) eps(s) ds")
    print("  obeys tau_s I' + I = tau_s eps, so the causal model is an ordinary")
    print("  differential equation and can be integrated directly.")
    print(f"  {'omega':>7} {'t':>8} {'sigma from the ODE':>20}"
          f" {'Re[M exp(-i w t)]':>20} {'difference':>11}")
    for w in (0.5, 2.0, 8.0):
        T = 2 * math.pi / w
        dt = T / 500.0
        n_steps = int(round(30 * T / dt))
        I, t = 0.0, -30 * T
        tail = []
        for _ in range(n_steps):
            def rate(x, y):
                return math.cos(w * x) - y / tau_s
            k1 = rate(t, I)
            k2 = rate(t + dt / 2, I + dt * k1 / 2)
            k3 = rate(t + dt / 2, I + dt * k2 / 2)
            k4 = rate(t + dt, I + dt * k3)
            I += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += dt
            tail.append((t, I))
        for tt, II in tail[-500::250]:
            sigma_ode = M_U * eps0 * math.cos(w * tt) - C * II
            modulus = (M(w) * eps0 * cmath.exp(-1j * w * tt)).real
            print(f"  {w:>7.2f} {tt:>8.3f} {sigma_ode:>20.9f} {modulus:>20.9f}"
                  f" {abs(sigma_ode - modulus):>11.2e}")
    print("  The ODE and the complex modulus agree; they are one model written")
    print("  two ways, and either route fixes both the attenuation and the")
    print("  dispersion.")

    print("\n  Dissipated energy per cycle, W = closed integral of sigma d eps,")
    print("  from the same ODE solution:")
    print(f"  {'omega':>8} {'W (loop integral)':>20} {'-pi Im M':>16}"
          f" {'1/Q = |Im M/Re M|':>20}")
    for w in (0.5, 2.0, 8.0):
        T = 2 * math.pi / w
        dt = T / 2000.0
        n_steps = int(round(20 * T / dt))
        I, t = 0.0, -20 * T
        cycle = []
        for _ in range(n_steps):
            def rate(x, y):
                return math.cos(w * x) - y / tau_s
            k1 = rate(t, I)
            k2 = rate(t + dt / 2, I + dt * k1 / 2)
            k3 = rate(t + dt / 2, I + dt * k2 / 2)
            k4 = rate(t + dt, I + dt * k3)
            I += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            t += dt
            cycle.append((t, M_U * eps0 * math.cos(w * t) - C * I))
        cycle = cycle[-2001:]
        W = 0.0
        for (t1, s1), (t2, s2) in zip(cycle, cycle[1:]):
            W += 0.5 * (s1 + s2) * eps0 * (math.cos(w * t2) - math.cos(w * t1))
        print(f"  {w:>8.2f} {W:>20.9f} {-math.pi * M(w).imag:>16.9f}"
              f" {abs(M(w).imag / M(w).real):>20.9f}")
    print("  W is positive, which is the definition of a dissipative medium, and")
    print("  Im M is negative: for the exp(-i omega t) convention the lossless-")
    print("  sign test is W = -pi eps0^2 Im M > 0, so an attenuating modulus has")
    print("  Im M < 0.  Getting this sign wrong turns attenuation into gain.")

    print("\n  Kramers-Kronig for the modulus, on the combination M(w) - M_U that")
    print("  vanishes at high frequency:")
    print("  Re(M - M_U) = +(2/pi) P int_0^inf w' Im(M - M_U)/(w'^2 - w^2) dw'")
    print(f"  {'omega':>8} {'Re(M-M_U)':>18} {'+(2/pi) P.V.':>18} {'difference':>12}")
    worstm = 0.0
    for w in (0.1, 0.5, 1.0, 4.0, 20.0):
        fw = w * (M(w) - M_U).imag
        g = lambda wp: wp * (M(wp) - M_U).imag - fw
        val = (2 / math.pi) * pv_even(g, w)
        worstm = max(worstm, abs((M(w) - M_U).real - val))
        print(f"  {w:>8.2f} {(M(w) - M_U).real:>18.12f} {val:>18.12f}"
              f" {abs((M(w) - M_U).real - val):>12.2e}")
    print(f"  worst difference: {worstm:.2e}")
    print("  Note the sign: the modulus is an upper-half-plane object, so its")
    print("  relation carries the opposite sign to the transfer function H above.")
    print("  Both are the same theorem applied to the reflected variable.")

    print("\n  Wave quantities: rho = 1, k = w sqrt(rho/M), v = w/Re k, alpha = Im k")
    print(f"  {'omega':>8} {'v':>14} {'alpha':>12} {'1/Q exact':>14}"
          f" {'w(te-ts)/(1+w^2 te ts)':>24}")
    for w in (0.05, 0.1, 0.5, 1.0, 2.828, 8.0, 40.0):
        k = w * cmath.sqrt(1.0 / M(w))
        exact_q = w * (tau_e - tau_s) / (1 + w * w * tau_e * tau_s)
        print(f"  {w:>8.3f} {w / k.real:>14.9f} {k.imag:>12.9f} {exact_q:>14.9f}"
              f" {abs(M(w).imag / M(w).real):>24.9f}")
    print(f"  v rises from sqrt(M_R/rho) = {math.sqrt(M_R):.6f} at low frequency")
    print(f"  to sqrt(M_U/rho) = {math.sqrt(M_U):.9f} at high frequency: the ratio is")
    print(f"  sqrt(M_U/M_R) = {math.sqrt(M_U / M_R):.9f}, exact.  This is the whole")
    print("  content of 'attenuation and dispersion are not independent': the")
    print("  same tau_e and tau_s fix both alpha(w) and v(w), and the dispersion")
    print(f"  integral of alpha is what makes v at 8 rad/s reach the value above.")
    print(f"  1/Q has a peak of (M_U - M_R)/(2 sqrt(M_R M_U)) ="
          f" {(M_U - M_R) / (2 * math.sqrt(M_R * M_U)):.9f} at w = 1/sqrt(te ts) ="
          f" {1 / math.sqrt(tau_e * tau_s):.9f}")
    print(f"  measured 1/Q at that frequency:"
          f" {abs(M(1 / math.sqrt(tau_e * tau_s)).imag / M(1 / math.sqrt(tau_e * tau_s)).real):.9f}")
    print("  A single relaxation therefore has a Q that peaks: it is not a")
    print("  constant-Q medium.  A nearly constant Q requires a broad spectrum of")
    print("  relaxation times, which is what the Kolsky-Futterman and the power-law")
    print("  models supply over a limited band.")


if __name__ == "__main__":
    main()
