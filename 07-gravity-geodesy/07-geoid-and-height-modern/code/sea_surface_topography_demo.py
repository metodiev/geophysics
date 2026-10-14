#!/usr/bin/env python3
"""The geoid, part 3: sea surface topography -- the geostrophic velocity implied
by a synthetic jet, and the wavelength at which a geoid error swamps the signal.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_surface_topography_demo.py

Everything here is SYNTHETIC: the jet, the geoid and its error spectrum, and the
error levels are teaching values.  No measured sea surface, geoid model or ocean
current is used.

Contents
--------
1. A synthetic mean dynamic topography (a jet) and the geostrophic velocity and
   transport it implies.
2. The geoid error appears directly in the dynamic topography: the velocity error
   it produces.
3. Wavelength by wavelength: where the geoid error stops being negligible.
4. The crossover length scale, and why it is a property of the geoid model.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G_ACC = 9.81                 # m s^-2
OMEGA = 7.2921150e-5         # rad s^-1
R_EARTH = 6371.0e3           # m
LAT = 40.0                   # deg, the synthetic jet's latitude

# --- SYNTHETIC parameters ---------------------------------------------------
JET_AMP = 1.00               # m, peak sea-surface height of the jet
JET_WIDTH = 100.0e3          # m, e-folding half-width
OCEAN_DEPTH = 1000.0         # m, effective depth of the jet for transport
GEOID_ERR_ABS = 0.05         # m, synthetic geoid error amplitude
GEOID_ERR_L0 = 200.0e3       # m, wavelength at which that error applies
SIGNAL_SLOPE_FRAC = 1.0      # the 'signal' velocity is the jet's own velocity


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    f_cor = 2.0 * OMEGA * np.sin(np.deg2rad(LAT))
    print(f"  Coriolis parameter at {LAT:.0f} deg N: f = {f_cor:.6e} rad/s")

    section("1. A synthetic jet and its geostrophic velocity")
    x = np.linspace(-600e3, 600e3, 2401)
    eta = JET_AMP / np.cosh(x / JET_WIDTH) ** 2
    deta = np.gradient(eta, x)
    v = G_ACC / f_cor * deta            # geostrophic velocity (m/s)
    print(f"  SYNTHETIC mean dynamic topography: eta = {JET_AMP:.2f} m * "
          f"sech^2(x/{JET_WIDTH/1e3:.0f} km)")
    print(f"  geostrophic balance: v = (g/f) d(eta)/dx")
    print(f"   x (km)      eta (m)      v (m/s)")
    for xk in (-300.0, -150.0, -60.0, 0.0, 60.0, 150.0, 300.0):
        i = int(np.argmin(np.abs(x - xk * 1e3)))
        print(f"   {xk:8.0f} {eta[i]:12.4f} {v[i]:12.4f}")
    vmax = np.max(np.abs(v))
    print(f"  peak velocity = {vmax:.3f} m/s at x = "
          f"{x[np.argmax(np.abs(v))]/1e3:.0f} km")
    transport = float(np.sum(np.abs(v)) * (x[1] - x[0]) * OCEAN_DEPTH)
    print(f"  transport with an effective depth of {OCEAN_DEPTH:.0f} m: "
          f"{transport/1e6:.1f} Sv")
    print("  A 1 m dynamic topography over a 100 km half-width is a ~1 m/s jet")
    print("  and a ~100 Sv transport: the ocean's signal lives in the MDT.")

    section("2. The geoid error enters the dynamic topography directly")
    print("  MDT = SSH - geoid, so an error in the geoid is an error in the MDT,")
    print("  and through the geostrophic balance an error in the velocity.")
    for err in (0.01, 0.05, 0.20):
        wavelength = GEOID_ERR_L0
        k = 2 * np.pi / wavelength
        dv = G_ACC / f_cor * k * err
        print(f"   geoid error {err*100:5.1f} cm at a wavelength of "
              f"{wavelength/1e3:.0f} km -> velocity error {dv:7.4f} m/s "
              f"({dv/vmax*100:5.1f}% of the jet)")
    print("  The comparison is the whole problem of the marine geoid: a geoid")
    print("  error of a few centimetres at a few hundred kilometres produces a")
    print("  velocity error comparable with the current.")

    section("3. Wavelength by wavelength: the MDT against a constant geoid error")
    print("  Spectrum of the synthetic jet (from its Fourier transform) against a")
    print("  geoid error of a constant amplitude at all wavelengths:")
    dx = x[1] - x[0]
    spec = np.abs(np.fft.rfft(eta - eta.mean())) * 2.0 / eta.size
    kx = 2.0 * np.pi * np.fft.rfftfreq(eta.size, d=dx)
    print("   wavelength (km)   MTD amplitude (cm)   geoid error (cm)   "
          "ratio signal/error")
    for lam_km in (50.0, 100.0, 200.0, 400.0, 800.0, 1200.0):
        lam = lam_km * 1e3
        i = int(np.argmin(np.abs(kx - 2 * np.pi / lam)))
        amp = spec[i] * 100.0
        print(f"   {lam_km:15.0f} {amp:20.3f} {GEOID_ERR_ABS*100:18.2f} "
              f"{amp/(GEOID_ERR_ABS*100):16.3f}")
    print("  The jet's amplitude falls with wavelength as its spectrum requires,")
    print("  while the (constant) geoid error does not: below some wavelength the")
    print("  MDT is smaller than the geoid error and the circulation cannot be")
    print("  recovered there.  This comparison — MTD spectrum against geoid error")
    print("  spectrum — is the honest form of 'the geoid limits oceanography'.")
    print("  A separate, stricter comparison uses the VELOCITY error:")
    print("   wavelength (km)   velocity error (m/s)   peak jet velocity (m/s)")
    for lam_km in (50.0, 100.0, 200.0, 400.0, 800.0):
        lam = lam_km * 1e3
        dv = G_ACC / f_cor * (2 * np.pi / lam) * GEOID_ERR_ABS
        print(f"   {lam_km:15.0f} {dv:22.4f} {vmax:25.3f}")
    print("  The velocity error grows as 1/wavelength because the geostrophic")
    print("  balance differentiates the (errored) height field; a constant height")
    print("  error therefore hurts the SHORT scales most.  This is why a geoid")
    print("  model that is excellent in the mean can still be useless for a")
    print("  western-boundary current, whose signal is at a few hundred km.")

    section("4. The crossover, stated as a property of the error spectrum")
    i_cross = None
    for lam_km in np.linspace(1200.0, 20.0, 4000):
        lam = lam_km * 1e3
        i = int(np.argmin(np.abs(kx - 2 * np.pi / lam)))
        amp = spec[i]
        if amp < GEOID_ERR_ABS and i_cross is None:
            i_cross = lam_km
    print(f"  With the stated geoid error ({GEOID_ERR_ABS*100:.0f} cm) and this")
    print(f"  synthetic jet, the MDT amplitude falls below the geoid error at")
    print(f"  wavelengths shorter than about {i_cross:.0f} km.")
    print("  That number is a property of the ASSUMED error spectrum and of the")
    print("  jet, not a universal constant.  What is universal is the argument:")
    print("  the MDT is a 1-2 m signal on a 100 m geoid, so a geoid model must be")
    print("  accurate to about 1% IN THE BAND OF INTEREST, and the band is set by")
    print("  the oceanographic target — basin-scale transports need the long")
    print("  wavelengths, jet dynamics need the short ones.")
    print("  Two consequences that hold for any error model:")
    print("    (i) the MDT is a 1-m signal on a 100-m geoid, so the geoid model")
    print("        must be accurate to better than 1% IN THE BAND OF INTEREST;")
    print("    (ii) independent information -- in-situ velocity, drifting buoys,")
    print("        Argo, a longer altimetric record -- is what validates a")
    print("        geoid-based circulation, because the geoid and the ocean")
    print("        cannot check each other.")


if __name__ == "__main__":
    main()
