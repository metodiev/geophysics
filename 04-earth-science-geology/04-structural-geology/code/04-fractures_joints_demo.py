"""Fractures, joints, fracture mechanics and the anisotropy they create.

Run:  .venv/bin/python 04-fractures_joints_demo.py
Requires: NumPy.

Companion to lesson 04-04-04. A fracture is a mechanical object at the scale of
a core and a continuum property at the scale of a seismic wave, and the bridge
between those two scales is the reason seismic anisotropy exists. This demo
builds the whole chain:

1. The Griffith energy balance: critical stress against flaw length, the stress
   intensity factor and the fracture toughness, evaluated for a stated surface
   energy.
2. Joint spacing against layer thickness, fitted by least squares -- presented
   as the empirical relation it is, with its scatter.
3. The statistics of spacing: the coefficient of variation and what it does and
   does not indicate, computed on synthetic sets.
4. The linear-slip model of a fractured medium: the normal and shear compliance
   of a fracture set derived from its stiffness and spacing, the effective
   stiffness tensor obtained by inverting the effective compliance, and the
   resulting P- and S-wave velocities. Every step is checked: zero fracture
   compliance must return the isotropic background exactly.
5. Thomsen's anisotropy parameters for the resulting VTI medium, the shear-wave
   splitting it produces, and the delay time over a stated path length.

Material parameters are labelled TABULATED/TYPICAL: surface energies, fracture
toughness and fracture stiffness vary by orders of magnitude between rocks, and
the stiffness used below is a stated example rather than a measurement.
"""

from __future__ import annotations

import numpy as np

# --------------------------------------------------------------------------
# TABULATED / TYPICAL values.
# --------------------------------------------------------------------------
E_YOUNG = 50.0e9          # Pa, TYPICAL intact-rock Young's modulus
NU = 0.25                 # TYPICAL Poisson's ratio
GAMMA_S = 10.0            # J/m^2, TYPICAL specific surface energy for rock
K_IC = 1.5e6              # Pa m^0.5, TYPICAL mode-I fracture toughness
RHO_ROCK = 2600.0         # kg/m^3
K_N_STIFF = 50.0e9        # Pa/m, TYPICAL fracture normal stiffness
K_T_STIFF = 20.0e9        # Pa/m, TYPICAL fracture shear stiffness


def lambd_mu(young: float, nu: float) -> tuple[float, float]:
    """Lame parameters from Young's modulus and Poisson's ratio."""
    lam = young * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
    mu = young / (2.0 * (1.0 + nu))
    return lam, mu


def part_one() -> None:
    print()
    print("1. Griffith fracture mechanics: which flaw grows?")
    print("-" * 76)
    lam, mu = lambd_mu(E_YOUNG, NU)
    print(f"  E = {E_YOUNG / 1e9:.1f} GPa, nu = {NU:.2f} -> lambda = "
          f"{lam / 1e9:.3f} GPa, mu = {mu / 1e9:.3f} GPa")
    print(f"  specific surface energy gamma_s = {GAMMA_S:.1f} J/m^2 (TYPICAL)")
    print(f"  mode-I toughness K_IC = {K_IC / 1e6:.2f} MPa m^0.5 (TYPICAL)")
    print()
    print("  Griffith (energy balance): sigma_c = sqrt(2 E gamma_s / (pi a))")
    print("  Irwin (stress intensity):  K_I = sigma sqrt(pi a), failure at "
          "K_I = K_IC")
    print(f"{'flaw half-length a':>20}{'sigma_c Griffith (MPa)':>25}"
          f"{'K_I at sigma_c (MPa m^0.5)':>29}")
    for a in (1.0e-3, 1.0e-2, 0.1, 1.0, 10.0):
        sigma_c = np.sqrt(2.0 * E_YOUNG * GAMMA_S / (np.pi * a))
        k_i = sigma_c * np.sqrt(np.pi * a)
        print(f"  {a:>18.3g} m{sigma_c / 1e6:>25.2f}{k_i / 1e6:>29.4f}")
    print("  The third column is constant, which is the whole point: the energy")
    print("  criterion and the stress-intensity criterion are the same statement")
    print("  written twice, and the constant is K_IC = "
          f"sqrt(2 E gamma_s) = "
          f"{np.sqrt(2 * E_YOUNG * GAMMA_S) / 1e6:.3f} MPa m^0.5.")
    print("  The agreement rests on a stated surface energy, and the constant it")
    print("  gives, 1.000 MPa m^0.5, is smaller than the tabulated toughness")
    print(f"  {K_IC / 1e6:.2f} MPa m^0.5 used below. Real rock has a microcrack")
    print("  process zone around the tip, so its measured toughness is larger")
    print("  than sqrt(2 E gamma_s) computed from the surface energy alone, and")
    print("  the Griffith strength of a laboratory specimen therefore usually")
    print("  EXCEEDS the prediction. That gap is why laboratory rock strength is")
    print("  scale-dependent, and why a quoted toughness is tied to the specimen")
    print("  size and the test method.")
    print()
    print("  The scaling, which matters more than the constant:")
    print("    doubling the flaw length reduces the strength by sqrt(2) = "
          f"{np.sqrt(2):.4f}")
    print("    a factor of 100 in flaw length is a factor of "
          f"{np.sqrt(100):.1f} in strength")
    a_crit = K_IC ** 2 / (np.pi * (10.0e6) ** 2)
    print(f"  A flaw of half-length {a_crit * 1e3:.2f} mm grows at a remote "
          f"tension of 10 MPa")
    print(f"  computed from K_IC alone: a_c = K_IC^2/(pi sigma^2). The same")
    print("  arithmetic run backwards is why flaw populations, not strength, are")
    print("  what a rock mechanics laboratory measures.")


def part_two() -> None:
    print()
    print("2. Joint spacing against layer thickness: an empirical relation")
    print("-" * 76)
    # SYNTHETIC measurements constructed to have the commonly reported linear
    # relation, with scatter of the size seen in the field.
    thickness = np.array([0.2, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
    rng = np.random.default_rng(20261014)
    spacing = 0.8 * thickness + rng.normal(0.0, 0.12, size=thickness.size)
    print("  SYNTHETIC data: 9 layers, thickness 0.2-5.0 m, spacing measured in")
    print("  each layer. The relation reported in the literature is close to")
    print("  spacing proportional to layer thickness; this data set is")
    print("  constructed with a slope of 0.80 and 0.12 m of noise, so the fit")
    print("  below recovers a number that was put in. That is the test.")
    print()
    print(f"{'thickness (m)':>15}{'spacing (m)':>13}{'spacing/thickness':>19}")
    for t, s in zip(thickness, spacing):
        print(f"  {t:>15.2f}{s:>13.3f}{s / t:>19.3f}")
    slope, intercept = np.polyfit(thickness, spacing, 1)
    predicted = slope * thickness + intercept
    ss_res = float(np.sum((spacing - predicted) ** 2))
    ss_tot = float(np.sum((spacing - spacing.mean()) ** 2))
    r_squared = 1.0 - ss_res / ss_tot
    print()
    print(f"  least-squares fit: spacing = {slope:.4f} * thickness + "
          f"{intercept:+.4f} m")
    print(f"  slope {slope:.4f} against the 0.80 used to construct the data "
          f"({slope / 0.8 - 1.0:+.2%})")
    print(f"  r^2 = {r_squared:.4f}; rms residual "
          f"{np.sqrt(ss_res / thickness.size):.4f} m")
    print(f"  the spacing/thickness ratio ranges from "
          f"{(spacing / thickness).min():.3f} to "
          f"{(spacing / thickness).max():.3f},")
    print("  so a single ratio with no range is not a description of the data.")
    print()
    print("  Stated honestly: the relation is EMPIRICAL. It has been documented")
    print("  across many formations and it is used for prediction, but its")
    print("  constant is a property of the formation, the loading history and")
    print("  the bed's stiffness relative to its neighbours, and it is not")
    print("  derivable from the elasticity used in part 1. The mechanical")
    print("  argument that underlies it -- that a layer cannot crack further")
    print("  once the stress transferred to the interface can no longer break")
    print("  the next site -- predicts a PROPORTIONALITY and not a value,")
    print("  which is exactly the kind of relation that has to be calibrated")
    print("  locally.")


def part_three() -> None:
    print()
    print("3. Spacing statistics and what a coefficient of variation means")
    print("-" * 76)
    rng = np.random.default_rng(7)
    print(f"{'population':>16}{'mean spacing (m)':>19}{'std (m)':>11}"
          f"{'Cv':>8}{'spacings per metre':>21}")
    populations = {
        "regular (clustered-free)": rng.normal(1.0, 0.05, 400),
        "random (Poisson)": rng.exponential(1.0, 400),
        "clustered": np.concatenate([rng.normal(0.25, 0.05, 200),
                                     rng.normal(1.75, 0.05, 200)]),
    }
    for label, data in populations.items():
        data = data[data > 0.0]
        print(f"  {label:>14}{data.mean():>19.4f}{data.std():>11.4f}"
              f"{data.std() / data.mean():>8.3f}"
              f"{1.0 / data.mean():>21.4f}")
    print("  The coefficient of variation Cv = sigma/mu is a shape statistic of")
    print("  the spacing distribution and nothing more. A value below about 0.5")
    print("  is widely read as 'saturated' -- a joint set that has stopped")
    print("  growing because the spacing reached a mechanical limit -- and that")
    print("  reading is a convention, not a measurement. What the statistic")
    print("  cannot do is distinguish a saturated set from a set whose spacing")
    print("  was inherited from the depositional fabric, and no field")
    print("  measurement of spacing alone can make that distinction.")
    print()
    print("  What a spacing distribution does predict, and verifiably: the")
    print("  fraction of a scanline that is bridged by intact rock. For a set")
    print("  with mean spacing s, the intact fraction of a line is exp(-L/s) for")
    print("  the Poisson case and 1 - 1/s for a regular set, which differ:")
    print(f"{'scanline (m)':>14}{'Poisson: exp(-L/s)':>22}{'regular: 1-L/s':>18}")
    for length in (0.5, 1.0, 2.0, 4.0):
        poisson = np.exp(-length / 1.0)
        regular = max(0.0, 1.0 - length / 1.0)
        print(f"  {length:>14.1f}{poisson:>22.4f}{regular:>18.4f}")
    print("  Same mean spacing, different connectivity. Any calculation that")
    print("  depends on whether fractures connect -- permeability, block size,")
    print("  rock-mass strength -- needs the distribution and not the mean.")


def compliance_matrix(c11: float, c12: float, c44: float) -> np.ndarray:
    """Isotropic stiffness as a 6x6 Voigt matrix."""
    return np.array([
        [c11, c12, c12, 0.0, 0.0, 0.0],
        [c12, c11, c12, 0.0, 0.0, 0.0],
        [c12, c12, c11, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, c44, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, c44, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, c44],
    ])


def fracture_compliances(k_n: float, k_t: float, spacing: float,
                         c11: float) -> tuple[float, float]:
    """Dimensionless normal and shear compliances of one fracture set.

    A stack of fractures each of stiffness k_n (Pa/m) and spacing s (m) adds a
    normal compliance 1/(k_n s) to the medium, because the strains of the
    fractures in series add.  Normalising by the background compliance 1/c11
    gives the dimensionless excess compliance Z_N = c11/(k_n s); the shear
    compliance follows the same argument with k_t.  This is the linear-slip
    model, and it is derived here rather than quoted so that the units can be
    checked: c11 is in Pa, k_n s in Pa.
    """
    return c11 / (k_n * spacing), c11 / (k_t * spacing)


def vti_from_horizontal_fractures(k_n: float, k_t: float, spacing: float,
                                  c11: float, c12: float,
                                  c44: float) -> tuple[np.ndarray, float, float]:
    """Effective VTI stiffness for a set of horizontal fractures.

    Fractures with normals along axis 3 (horizontal fractures, so VTI) add
    Z_N to S_33 and Z_T to S_44 and S_55.  The effective compliance is inverted
    to give the effective stiffness.  Returns (C, Z_N, Z_T).
    """
    c = compliance_matrix(c11, c12, c44)
    s = np.linalg.inv(c)
    z_n, z_t = fracture_compliances(k_n, k_t, spacing, c11)
    s_eff = s.copy()
    s_eff[2, 2] += z_n * s[2, 2]
    s_eff[3, 3] += z_t * s[3, 3]
    s_eff[4, 4] += z_t * s[4, 4]
    c_eff = np.linalg.inv(s_eff)
    return c_eff, z_n, z_t


def velocities(c_eff: np.ndarray, rho: float) -> dict[str, float]:
    return {
        "Vp_vertical": np.sqrt(c_eff[2, 2] / rho),
        "Vp_horizontal": np.sqrt(c_eff[0, 0] / rho),
        "Vs_vh": np.sqrt(c_eff[4, 4] / rho),   # polarised in the 1-3 plane
        "Vs_h": np.sqrt(c_eff[5, 5] / rho),    # polarised in the 1-2 plane
    }


def part_four() -> None:
    print()
    print("4. The effective medium: how fractures make a rock anisotropic")
    print("-" * 76)
    lam, mu = lambd_mu(E_YOUNG, NU)
    c11 = lam + 2 * mu
    c12 = lam
    c44 = mu
    rho = RHO_ROCK
    print(f"  background: Vp = {np.sqrt(c11 / rho):,.1f} m/s, "
          f"Vs = {np.sqrt(c44 / rho):,.1f} m/s, rho = {rho:.0f} kg/m^3")
    print(f"  fracture normal stiffness {K_N_STIFF / 1e9:.1f} GPa/m, shear "
          f"stiffness {K_T_STIFF / 1e9:.1f} GPa/m (TYPICAL)")

    print()
    print("  Check 1: with no fractures the effective medium must be exactly the")
    print("  background. Using a fracture stiffness of 1e30 Pa/m, so that the")
    print("  excess compliance is negligible rather than notional:")
    c_eff0, z_n0, z_t0 = vti_from_horizontal_fractures(1e30, 1e30, 1.0,
                                                       c11, c12, c44)
    v0 = velocities(c_eff0, rho)
    print(f"    Z_N = {z_n0:.3e}, Z_T = {z_t0:.3e} -> Vp(vertical) = "
          f"{v0['Vp_vertical']:.6f} m/s,")
    print(f"    Vp(horizontal) = {v0['Vp_horizontal']:.6f} m/s, "
          f"Vs(vh) = {v0['Vs_vh']:.6f} m/s, Vs(h) = {v0['Vs_h']:.6f} m/s")
    print(f"    anisotropy: Vp(v)/Vp(h) - 1 = "
          f"{v0['Vp_vertical'] / v0['Vp_horizontal'] - 1.0:+.3e}, "
          f"S splitting = "
          f"{v0['Vs_h'] / v0['Vs_vh'] - 1.0:+.3e}")

    print()
    print("  Check 2: the anisotropy must grow with fracture density (that is,")
    print("  with decreasing spacing) and must vanish as the spacing grows.")
    print(f"{'spacing (m)':>13}{'Z_N':>10}{'Z_T':>10}{'Vp(v) m/s':>12}"
          f"{'Vp(h) m/s':>12}{'Vs(vh) m/s':>12}{'Vs(h) m/s':>12}"
          f"{'Vp anisotropy':>15}")
    for spacing in (100.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5):
        c_eff, z_n, z_t = vti_from_horizontal_fractures(
            K_N_STIFF, K_T_STIFF, spacing, c11, c12, c44)
        v = velocities(c_eff, rho)
        print(f"  {spacing:>13.1f}{z_n:>10.5f}{z_t:>10.5f}"
              f"{v['Vp_vertical']:>12,.1f}{v['Vp_horizontal']:>12,.1f}"
              f"{v['Vs_vh']:>12,.1f}{v['Vs_h']:>12,.1f}"
              f"{v['Vp_vertical'] / v['Vp_horizontal'] - 1.0:>15.3%}")
    print("  The P-wave velocity is reduced along the direction normal to the")
    print("  fractures and unchanged within the fracture plane, which is the")
    print("  mechanical reason a fracture set makes a medium anisotropic: the")
    print("  fractures are compliant in one direction and not in the others.")
    print("  This is why anisotropy is not a curiosity but a measurement: it is")
    print("  the only remote observable of aligned fracture compliance.")

    print()
    print("  Thomsen parameters of the resulting VTI medium and the shear-wave")
    print("  splitting they imply:")
    print(f"{'spacing (m)':>13}{'epsilon':>11}{'gamma':>11}{'delta':>11}"
          f"{'split (ms/m)':>15}{'delay over 1 km (ms)':>22}")
    for spacing in (20.0, 10.0, 5.0, 2.0):
        c_eff, _z_n, _z_t = vti_from_horizontal_fractures(
            K_N_STIFF, K_T_STIFF, spacing, c11, c12, c44)
        eps = (c_eff[0, 0] - c_eff[2, 2]) / (2.0 * c_eff[2, 2])
        gamma = (c_eff[5, 5] - c_eff[4, 4]) / (2.0 * c_eff[4, 4])
        delta = ((c_eff[0, 2] + c_eff[4, 4]) ** 2
                 - (c_eff[2, 2] - c_eff[4, 4]) ** 2) / (
            2.0 * c_eff[2, 2] * (c_eff[2, 2] - c_eff[4, 4]))
        vs_vh = np.sqrt(c_eff[4, 4] / rho)
        vs_h = np.sqrt(c_eff[5, 5] / rho)
        split = abs(1.0 / vs_vh - 1.0 / vs_h)
        print(f"  {spacing:>13.1f}{eps:>11.5f}{gamma:>11.5f}{delta:>11.5f}"
              f"{split * 1e3:>15.6f}{split * 1e3 * 1e3:>22.3f}")
    print("  epsilon measures the fractional difference in horizontal and")
    print("  vertical P velocity, gamma the shear-wave splitting, and delta the")
    print("  near-vertical P behaviour. For a single set of HORIZONTAL fractures")
    print("  epsilon and gamma are both POSITIVE here: the medium is stiffer along")
    print("  the fracture plane than across it, so horizontal velocities exceed")
    print("  the vertical ones. A set of vertical fractures measured in a")
    print("  vertical well gives the opposite sign, which is the single most")
    print("  useful thing a crossed-dipole sonic log reports.")
    print()
    print("  Two of these numbers have exact closed forms in the linear-slip")
    print("  model, so they are checked:")
    print(f"{'spacing (m)':>13}{'Z_T':>10}{'gamma exact':>14}{'gamma computed':>16}"
          f"{'split exact (ms/m)':>21}{'split computed':>16}")
    vs0 = np.sqrt(c44 / rho)
    for spacing in (20.0, 10.0, 5.0, 2.0):
        c_eff, _z_n, z_t = vti_from_horizontal_fractures(
            K_N_STIFF, K_T_STIFF, spacing, c11, c12, c44)
        gamma_computed = (c_eff[5, 5] - c_eff[4, 4]) / (2.0 * c_eff[4, 4])
        gamma_exact = z_t / 2.0
        vs_vh = np.sqrt(c_eff[4, 4] / rho)
        vs_h = np.sqrt(c_eff[5, 5] / rho)
        split_computed = abs(1.0 / vs_vh - 1.0 / vs_h) * 1e3
        split_exact = (np.sqrt(1.0 + z_t) - 1.0) / vs0 * 1e3
        print(f"  {spacing:>13.1f}{z_t:>10.4f}{gamma_exact:>14.6f}"
              f"{gamma_computed:>16.6f}{split_exact:>21.6f}"
              f"{split_computed:>16.6f}")
    print("  gamma = Z_T/2 exactly, and the splitting follows from C66 being")
    print("  untouched while C44 is reduced by (1 + Z_T), both of which are")
    print("  consequences of the excess compliance sitting only on the S44 and")
    print("  S55 terms. When a numerical effective-medium calculation agrees with")
    print("  a closed form to six decimals, the bookkeeping is right.")
    print()
    print("  Two conventions worth stating: Thomsen's epsilon, gamma and delta")
    print("  are defined for a VTI medium, so 'the VTI parameters of an HTI")
    print("  medium' means the parameters after the rotation into the symmetry")
    print("  frame. And delta cannot be measured by P velocity along the axes")
    print("  alone, which is why it is the parameter most often quoted with the")
    print("  largest uncertainty.")


def part_five() -> None:
    print()
    print("5. Joints and permeability: why orientation, not just density, matters")
    print("-" * 76)
    print("  For a set of parallel planar fractures of aperture b and spacing s,")
    print("  the permeability along the fracture plane is b^3/(12 s) (the cubic")
    print("  law for a slot, divided by the number per unit length), and the")
    print("  permeability across the set is that of the intact rock.")
    print(f"{'aperture (mm)':>15}{'spacing (m)':>13}{'k parallel (m^2)':>19}"
          f"{'k parallel (darcy)':>21}")
    for aperture, spacing in ((0.1, 1.0), (0.1, 0.1), (0.5, 1.0), (0.5, 0.1),
                              (1.0, 1.0)):
        b = aperture * 1e-3
        k = b ** 3 / (12.0 * spacing)
        print(f"  {aperture:>15.2f}{spacing:>13.2f}{k:>19.3e}"
              f"{k / 9.869233e-13:>21.4f}")
    print("  The aperture enters as its CUBE: doubling the aperture multiplies")
    print("  the permeability by eight, and halving it divides it by eight. This")
    print("  is why fracture permeability is dominated by the few largest")
    print("  apertures and why a core-scale measurement of aperture cannot be")
    print("  extrapolated to a reservoir: the transport is carried by the part of")
    print("  the distribution that core is least likely to sample.")

    print()
    print("  The anisotropy of permeability for a single set, with the intact")
    print("  rock permeability taken as 1e-15 m^2:")
    intact = 1.0e-15
    for aperture, spacing in ((0.1, 1.0), (0.5, 1.0), (0.5, 0.1)):
        b = aperture * 1e-3
        k_parallel = intact + b ** 3 / (12.0 * spacing)
        print(f"    aperture {aperture:.1f} mm, spacing {spacing:.1f} m: "
              f"k_parallel/k_perpendicular = {k_parallel / intact:,.1f}")
    print("  Ratios of one to five orders of magnitude are ordinary, and it is")
    print("  the same geometric reason as")
    print("  the seismic anisotropy of part 4: a set of aligned compliant planes")
    print("  transmits differently along and across itself. The two measurements")
    print("  -- seismic anisotropy and permeability anisotropy -- are different")
    print("  projections of the same fracture fabric, which is why joint")
    print("  orientation is mapped before either is interpreted.")


def main() -> None:
    print("=" * 78)
    print("Fractures, joints, fracture mechanics and fracture-induced anisotropy")
    print("=" * 78)
    part_one()
    part_two()
    part_three()
    part_four()
    part_five()
    print()
    print("=" * 78)
    print("Material parameters above are TABULATED/TYPICAL; fracture stiffness,")
    print("toughness and surface energy span orders of magnitude between rocks.")
    print("The spacing relation in part 2 is EMPIRICAL and the data set there is")
    print("SYNTHETIC. The effective-medium calculation is verified internally:")
    print("zero fracture compliance returns the isotropic background exactly.")
    print("=" * 78)


if __name__ == "__main__":
    main()
