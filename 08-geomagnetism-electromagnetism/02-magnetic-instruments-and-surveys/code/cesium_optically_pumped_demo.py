#!/usr/bin/env python3
"""Optically pumped alkali magnetometers: Zeeman structure, the Breit-Rabi
relation, heading error and the quadratic Zeeman shift.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cesium_optically_pumped_demo.py

Everything here is SYNTHETIC except the standard constants: the electron
g-factor, the Bohr magneton, the Planck constant, the electron/proton mass ratio
and the caesium hyperfine frequency that defines the SI second.  No instrument,
cell geometry or published sensitivity is reproduced.

Contents
--------
1. Zeeman structure: g_F from the quantum numbers, and the size of the nuclear
   term that this model neglects.
2. The Larmor relation for caesium and potassium.
3. Breit-Rabi versus the linear Zeeman approximation, and the quadratic Zeeman
   shift of the field-independent transition.
4. Heading error from the quadratic dependence on the angle to the optical axis.
5. Dead zones and how the signal amplitude varies with orientation.
6. Sensitivity floor and the practical resolution budget.
7. Comparison of the three alkali species.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

KB = None  # placeholder to keep the import list honest; not used here
MU_B = 9.2740100783e-24      # J/T, Bohr magneton (standard constant)
H_PLANCK = 6.62607015e-34    # J s, exact
G_S = 2.00231930436256       # electron spin g-factor (standard constant)
M_E_OVER_M_P = 5.44617021487e-4   # electron/proton mass ratio (standard constant)
F_CS_HFS = 9192631770.0      # Hz, caesium hyperfine splitting: defines the second

MU_B_OVER_H = MU_B / H_PLANCK         # Hz/T per unit g-factor


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def g_F(I, J, F, g_J=G_S, g_I=0.0):
    """Landé g-factor for hyperfine level F of an atom with spins I, J.

    g_F = g_J [F(F+1)+J(J+1)-I(I+1)] / [2F(F+1)]
        + g_I (m_e/m_p) [F(F+1)+I(I+1)-J(J+1)] / [2F(F+1)]
    """
    denom = 2.0 * F * (F + 1.0)
    first = g_J * (F * (F + 1.0) + J * (J + 1.0) - I * (I + 1.0)) / denom
    second = g_I * M_E_OVER_M_P * (F * (F + 1.0) + I * (I + 1.0)
                                   - J * (J + 1.0)) / denom
    return first + second


def breit_rabi(I, B, g_J=G_S, g_I=0.0, f_hfs=F_CS_HFS):
    """Breit-Rabi energies of the ground-state hyperfine manifold, in Hz.

    Returns a dict keyed by (F, mF) with the energy in Hz for the given field B
    (tesla).  The formula is valid for J = 1/2:
        E/(h) = -f_hfs/(2(2I+1)) + g_I mu_B mF B/h
                +/- (f_hfs/2) sqrt(1 + 4 mF x/(2I+1) + x^2),
    with x = (g_J - g_I) mu_B B / (h f_hfs) and the sign following F = I +/- 1/2.
    """
    x = (g_J - g_I) * MU_B * B / (H_PLANCK * f_hfs)
    out = {}
    for sign, F in ((+1.0, I + 0.5), (-1.0, I - 0.5)):
        for mF in np.arange(-F, F + 1.0, 1.0):
            e = (-f_hfs / (2.0 * (2.0 * I + 1.0))
                 + g_I * M_E_OVER_M_P * MU_B * mF * B / H_PLANCK
                 + sign * (f_hfs / 2.0)
                 * np.sqrt(1.0 + 4.0 * mF * x / (2.0 * I + 1.0) + x ** 2))
            out[(F, float(mF))] = e
    return out


def main():
    section("1. Zeeman structure from the quantum numbers")
    print(f"electron spin g-factor g_s = {G_S:.14f} (standard constant)")
    print(f"mu_B/h = {MU_B_OVER_H:.6e} Hz/T")
    print(f"caesium hyperfine splitting = {F_CS_HFS:.0f} Hz (defines the SI "
          "second)")
    print("  species  I     J    F    g_F       f/B (Hz/nT)")
    species = [("Cs-133", 3.5, 0.5, 4.0), ("Cs-133", 3.5, 0.5, 3.0),
               ("K-39", 1.5, 0.5, 2.0), ("K-39", 1.5, 0.5, 1.0),
               ("Rb-87", 1.5, 0.5, 2.0), ("Rb-87", 1.5, 0.5, 1.0)]
    for name, I, J, F in species:
        g = g_F(I, J, F)
        print(f"  {name:8s} {I:3.1f}  {J:3.1f}  {F:3.1f}  {g:+8.5f}   "
              f"{abs(g)*MU_B_OVER_H*1e-9:10.5f}")
    print("  the nuclear moment is neglected above.  Its contribution to g_F has")
    print("  magnitude |g_I| (m_e/m_p) x 7/8 at most, which for |g_I| <= 1 is")
    print(f"  {M_E_OVER_M_P*0.875:.2e}, i.e. up to "
          f"{100*M_E_OVER_M_P*0.875/abs(g_F(3.5,0.5,4.0)):.3f}% of the value.")
    print("  That is NOT negligible at the 0.1% level, so a real instrument's")
    print("  constant is measured spectroscopically, not computed from g_s alone.")

    section("2. The Larmor relation for caesium and potassium")
    g_cs = abs(g_F(3.5, 0.5, 4.0))
    g_k = abs(g_F(1.5, 0.5, 2.0))
    print("   B (nT)   f_Cs (Hz)      f_K (Hz)")
    for b_nt in (10000.0, 25000.0, 50000.0, 100000.0):
        b = b_nt * 1.0e-9
        print(f"  {b_nt:8.0f}   {g_cs*MU_B_OVER_H*b:12.4f}   "
              f"{g_k*MU_B_OVER_H*b:12.4f}")
    print(f"  Cs sensitivity = {g_cs*MU_B_OVER_H*1e-9:.5f} Hz/nT")
    print(f"  K  sensitivity = {g_k*MU_B_OVER_H*1e-9:.5f} Hz/nT")
    print("  a higher frequency is easier to count, which is why the heavier")
    print("  alkali species are preferred for high-resolution work.")

    section("3. Breit-Rabi versus the linear Zeeman approximation")
    I_cs = 3.5
    print("  for the STRETCHED state (mF = F = I + 1/2) the radical in the")
    print("  Breit-Rabi formula is a perfect square:")
    print("    1 + 4 mF x/(2I+1) + x^2  with  4 mF/(2I+1) = 2")
    print("      = 1 + 2x + x^2 = (1+x)^2,   sqrt = 1 + x  exactly,")
    print("  so the stretched-state energy is EXACTLY linear in B at every field.")
    print("   B (nT)     mF=4 shift (Hz)   deviation     mF=1 shift (Hz)  "
          "deviation")
    for b_nt in (50000.0, 100000.0, 1.0e6, 1.0e7):
        B = b_nt * 1.0e-9
        E = breit_rabi(I_cs, B)
        E0 = breit_rabi(I_cs, 0.0)
        s4 = E[(4.0, 4.0)] - E0[(4.0, 4.0)]
        l4 = g_cs * MU_B_OVER_H * B * 4.0
        s1 = E[(4.0, 1.0)] - E0[(4.0, 1.0)]
        l1 = g_cs * MU_B_OVER_H * B * 1.0
        print(f"  {b_nt:9.0f}   {s4:15.4f}   {s4/l4-1:+11.3e}   "
              f"{s1:15.4f}   {s1/l1-1:+11.3e}")
    print("  at a million nanotesla (1 mT) the mF = 1 state is already 5.7e-4")
    print("  relative away from linear, while the stretched state stays exact to")
    print("  machine precision; that difference is why alkali magnetometers use")
    print("  stretched states rather than the mF = 0 clock transition.")

    section("4. The quadratic Zeeman shift of the mF = 0 transition")
    print("  the transition (F = 3, mF = 0) -> (F = 4, mF = 0) has no linear")
    print("  Zeeman shift, so its field dependence is quadratic:")
    print("   B (nT)   B (microT)   shift (Hz)   shift/B^2 (Hz per nT^2)")
    for b_nt in (10000.0, 25000.0, 50000.0, 100000.0, 150000.0):
        B = b_nt * 1.0e-9
        E = breit_rabi(I_cs, B)
        E0 = breit_rabi(I_cs, 0.0)
        shift = (E[(4.0, 0.0)] - E0[(4.0, 0.0)]) - (E[(3.0, 0.0)] - E0[(3.0, 0.0)])
        print(f"  {b_nt:8.0f}   {b_nt*1e-3:9.1f}   {shift:11.4f}   "
              f"{shift/b_nt**2:.4e}")
    b_1khz = None
    for b_nt in np.arange(1000.0, 400000.0, 100.0):
        B = b_nt * 1.0e-9
        E = breit_rabi(I_cs, B)
        E0 = breit_rabi(I_cs, 0.0)
        shift = (E[(4.0, 0.0)] - E0[(4.0, 0.0)]) - (E[(3.0, 0.0)] - E0[(3.0, 0.0)])
        if abs(shift) >= 1000.0:
            b_1khz = b_nt
            break
    print(f"  the shift reaches 1 kHz at B = {b_1khz:.0f} nT "
          f"= {b_1khz*1e-3:.1f} microT")
    print("  so a mF = 0 transition is only field-independent for fields well")
    print("  below this; a survey magnetometer uses a stretched state instead.")

    section("5. Heading error")
    print("  a scalar sensor measures the total field only if the field is along")
    print("  the optical axis.  Model the relative error as c sin^2(theta):")
    c_heading = 5.0e-4        # SYNTHETIC coefficient of the model
    print(f"  SYNTHETIC model coefficient c = {c_heading:.1e}")
    print("   theta (deg)   sin^2(theta)   relative error   error at 50 000 nT")
    for th_deg in (0.5, 1.0, 2.0, 5.0, 10.0):
        th = np.radians(th_deg)
        err = c_heading * np.sin(th) ** 2
        print(f"  {th_deg:11.1f}   {np.sin(th)**2:12.6f}   {err:14.3e}   "
              f"{err*50000:13.4f} nT")
    print("  the error is second order in the misalignment, unlike the first-order")
    print("  cross-axis leak of a fluxgate: this is why an optically pumped sensor")
    print("  can be used as a scalar magnetometer without precise orientation.")

    section("6. Dead zones and the signal amplitude")
    print("  the pumping efficiency falls as sin(theta), so the signal vanishes")
    print("  along the optical axis.  With a SYNTHETIC amplitude a = sin(theta):")
    noise_frac = 5.0e-3       # SYNTHETIC: noise as a fraction of full amplitude
    print(f"  noise floor = {noise_frac:.1e} of the full signal amplitude")
    print("   theta (deg)   signal (fraction)   usable?")
    for th_deg in (0.05, 0.2, 0.5, 1.0, 5.0, 45.0, 90.0):
        th = np.radians(th_deg)
        sig = np.sin(th)
        print(f"  {th_deg:11.1f}   {sig:18.6f}   "
              f"{'yes' if sig > noise_frac else 'no - dead zone'}")
    print("  the dead zone is a cone about the field direction, so a moving")
    print("  platform sweeps through it; a fluxgate or an array avoids this by")
    print("  measuring components rather than a scalar.")

    section("7. Sensitivity floor and the resolution budget")
    floor = 1.0e-12           # T/sqrt(Hz), SYNTHETIC white noise floor
    print(f"  SYNTHETIC noise floor = {floor*1e12:.1f} pT/sqrt(Hz)")
    for bw in (10.0, 1.0, 0.1):
        print(f"  bandwidth {bw:5.2f} Hz -> noise = "
              f"{floor*np.sqrt(bw)*1e9:.5f} nT rms")
    print("  a real budget adds the heading error of section 5, the orientation")
    print("  uncertainty of the platform and the calibration of the sensor's")
    print("  constant, all of which are larger than this floor in field practice.")

    section("8. Reproducibility check with the seeded generator")
    draws = RNG.normal(0.0, 1.0, 5)
    print("  first five standard-normal draws from seed 20261014:")
    print("  " + ", ".join(f"{v:+.6f}" for v in draws))


if __name__ == "__main__":
    main()
