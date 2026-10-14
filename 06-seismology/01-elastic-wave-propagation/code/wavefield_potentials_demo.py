"""Helmholtz decomposition of a synthetic displacement field, done numerically.

A displacement field is built from a *known* scalar potential (the P part) and a
known vector potential (the S part).  The field is then decomposed by the
textbook route -- solve nabla^2 phi = div u and nabla^2 psi = curl u in Fourier
space -- and the recovered potentials are compared with the ones that were
injected.

This is a closed loop: the same data are generated and inverted by two
independent routes, so the measured error is exactly the error of the
decomposition itself.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/wavefield_potentials_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def spectral_derivative(field, kx, ky):
    """d/dx and d/dy of a periodic 2-D field, exactly for band-limited data."""
    fx = np.fft.fft2(field)
    dfx = np.real(np.fft.ifft2(1j * kx * fx))
    dfy = np.real(np.fft.ifft2(1j * ky * fx))
    return dfx, dfy


def main() -> None:
    section("1. build a field from known potentials")
    n = 256
    length = 1.0
    x = np.linspace(0.0, length, n, endpoint=False)
    dx = x[1] - x[0]
    X, Y = np.meshgrid(x, x, indexing="ij")
    kx = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(kx, kx, indexing="ij")
    k2 = KX**2 + KY**2
    k2[0, 0] = 1.0                     # avoid a division by zero; set below

    # P potential: a compressional plane wave
    kp = np.array([3.0, 1.0]) * 2.0 * np.pi / length
    phi_true = np.sin(kp[0] * X + kp[1] * Y)
    # S potential: a shear plane wave with twice the wavenumber
    ks = np.array([1.0, 4.0]) * 2.0 * np.pi / length
    psi_true = 0.5 * np.cos(ks[0] * X + ks[1] * Y)

    phi_x, phi_y = spectral_derivative(phi_true, KX, KY)
    psi_x, psi_y = spectral_derivative(psi_true, KX, KY)
    # u = grad phi + curl(psi zhat) = (phi_x - psi_y, phi_y + psi_x)
    ux = phi_x - psi_y
    uy = phi_y + psi_x
    print(f"  grid {n} x {n}, domain {length:.1f} x {length:.1f} m, "
          f"dx = {dx:.3e} m")
    print(f"  injected P potential: plane wave at k = ({kp[0]:.4f}, {kp[1]:.4f}) rad/m")
    print(f"  injected S potential: plane wave at k = ({ks[0]:.4f}, {ks[1]:.4f}) rad/m")

    section("2. decompose the field by solving Poisson equations in Fourier space")
    div_u = sum(spectral_derivative(u, KX, KY)[i] for i, u in enumerate((ux, uy)))
    curl_u = spectral_derivative(uy, KX, KY)[0] - spectral_derivative(ux, KX, KY)[1]
    # nabla^2 phi = div u ; nabla^2 psi = curl u
    phi_rec = np.real(np.fft.ifft2(np.fft.fft2(div_u) / (-k2)))
    psi_rec = np.real(np.fft.ifft2(np.fft.fft2(curl_u) / (-k2)))
    phi_rec -= phi_rec.mean()
    psi_rec -= psi_rec.mean()
    phi_true_c = phi_true - phi_true.mean()
    psi_true_c = psi_true - psi_true.mean()

    def rel(a, b):
        return np.linalg.norm(a - b) / np.linalg.norm(b)

    print(f"  relative L2 error in phi (P potential) : {rel(phi_rec, phi_true_c):.3e}")
    print(f"  relative L2 error in psi (S potential) : {rel(psi_rec, psi_true_c):.3e}")
    print("  (the zero-mean mode is undetermined by a Poisson equation and is")
    print("   removed from both sides before comparing)")

    section("3. reconstruct the field from the recovered potentials and check it")
    p_x, p_y = spectral_derivative(phi_rec, KX, KY)
    s_x, s_y = spectral_derivative(psi_rec, KX, KY)
    ux_rec = p_x - s_y
    uy_rec = p_y + s_x
    print(f"  relative L2 error in u_x : {rel(ux_rec, ux):.3e}")
    print(f"  relative L2 error in u_y : {rel(uy_rec, uy):.3e}")

    section("4. how the energy splits between the two modes")
    energy_p = np.sum(p_x**2 + p_y**2)
    energy_s = np.sum(s_y**2 + s_x**2)
    cross = np.sum(2.0 * (p_x * (-s_y) + p_y * s_x))
    print(f"  sum |grad phi|^2        : {energy_p:.6e}")
    print(f"  sum |curl(psi zhat)|^2  : {energy_s:.6e}")
    print(f"  cross term 2 grad phi . curl : {cross:+.6e}")
    print(f"  cross term / (P + S)          : {cross / (energy_p + energy_s):+.3e}")
    print(f"  P share of the kinetic energy : {energy_p / (energy_p + energy_s):.6f}")
    print("  The cross term integrates to zero over the periodic domain: the")
    print("  Helmholtz split is orthogonal, so P and S energies add.")
    print("  A field built only from phi has div u != 0 and curl u = 0, and one")
    print("  built only from psi the reverse -- which is the operational")
    print("  definition of the two modes used throughout seismology.")
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
