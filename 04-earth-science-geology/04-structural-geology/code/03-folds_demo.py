"""Fold geometry, thickness classification, buckling and the excess-area method.

Run:  .venv/bin/python 03-folds_demo.py
Requires: NumPy.

Companion to lesson 04-04-03. A fold is a shape, and a shape becomes an
interpretation only when the kinematics that produced it are constrained. This
demo computes the shape, compares it with the two classical mechanisms, and then
inverts the shape for a quantity that is not visible: the depth to the
detachment.

1. Geometry of a folded surface: dip as a function of position, maximum limb
   dip, curvature, and the arc-to-chord shortening, all from one analytic shape.
2. Recovery of the fold parameters from synthetic dip data by least squares,
   which is what actually happens when dips are measured in the field.
3. Ramsay's thickness classification: the orthogonal-thickness ratio and the
   thickness ratio as functions of limb dip, for the two end-member mechanisms
   (parallel folding by flexural slip, and similar folding by vertical shear).
4. Buckling: the classical result that the dominant wavelength of a folded
   competent layer is proportional to the cube root of the viscosity ratio,
   evaluated and checked.
5. The excess-area method: depth to detachment = excess area / shortening,
   verified by constructing a fold at a known detachment depth and recovering
   that depth from the shape alone.
6. Interlimb angle and the standard fold-tightness classification.

All folds here are SYNTHETIC constructions from stated mechanisms. The
classifications quoted are standard practice; the fold itself is not a
description of any named structure.
"""

from __future__ import annotations

import numpy as np


def fold_surface(x: np.ndarray, amplitude: float, wavelength: float,
                 phase: float = 0.0) -> np.ndarray:
    """An upright sinusoidal fold: z = A cos(2 pi x / lambda + phase)."""
    return amplitude * np.cos(2.0 * np.pi * x / wavelength + phase)


def fold_dip(x: np.ndarray, amplitude: float, wavelength: float,
             phase: float = 0.0) -> np.ndarray:
    """Dip of the folded surface, in degrees, by analytic differentiation."""
    k = 2.0 * np.pi / wavelength
    slope = -amplitude * k * np.sin(k * x + phase)
    return np.degrees(np.arctan(slope))


def part_one() -> None:
    print()
    print("1. Geometry of a sinusoidal fold")
    print("-" * 74)
    amplitude, wavelength = 200.0, 2000.0
    print(f"  amplitude {amplitude:.0f} m, wavelength {wavelength:.0f} m, "
          f"amplitude/wavelength = {amplitude / wavelength:.2f}")
    print(f"{'x (m)':>8}{'z (m)':>10}{'dip (deg)':>12}{'curvature (1/m)':>19}"
          f"{'fold position':>21}")
    for x in np.arange(0.0, wavelength + 1.0, wavelength / 8.0):
        z = fold_surface(np.array([x]), amplitude, wavelength)[0]
        dip = fold_dip(np.array([x]), amplitude, wavelength)[0]
        k = 2.0 * np.pi / wavelength
        second = -amplitude * k ** 2 * np.cos(k * x)
        first = -amplitude * k * np.sin(k * x)
        curvature = abs(second) / (1.0 + first ** 2) ** 1.5
        if x in (0.0, wavelength):
            position = "hinge (crest)"
        elif abs(x - wavelength / 2) < 1e-9:
            position = "hinge (trough)"
        elif abs(x - wavelength / 4) < 1e-9 or abs(x - 3 * wavelength / 4) < 1e-9:
            position = "inflection (max dip)"
        else:
            position = "limb"
        print(f"  {x:>6.0f}{z:>10.1f}{dip:>12.2f}{curvature:>19.4e}"
              f"{position:>21}")

    x = np.linspace(0.0, 4.0 * wavelength, 200001)
    z = fold_surface(x, amplitude, wavelength)
    dx = x[1] - x[0]
    arc = float(np.sum(np.sqrt(1.0 + np.gradient(z, dx) ** 2)) * dx)
    chord = x[-1] - x[0]
    print()
    print(f"  over four wavelengths: chord = {chord:,.1f} m, arc length = "
          f"{arc:,.1f} m")
    print(f"  excess length (shortening) = {arc - chord:,.1f} m = "
          f"{(arc - chord) / arc:.4%} of the arc length")
    print(f"  the same quantity per wavelength: "
          f"{(arc - chord) / 4:,.2f} m")
    print("  A negative dip is a surface descending towards increasing x; the")
    print("  magnitude is what a field measurement would report.")
    print("  Maximum limb dip occurs at the inflection points and is "
          f"{np.degrees(np.arctan(amplitude * 2 * np.pi / wavelength)):.2f} deg "
          "for this")
    print("  amplitude/wavelength ratio. A fold's shape is fully described by "
          "amplitude and")
    print("  wavelength; the dip and the shortening are consequences of them, "
          "not")
    print("  independent measurements, which is why reporting dips alone leaves "
          "the fold")
    print("  underdetermined.")


def part_two() -> None:
    print()
    print("2. Recovering fold parameters from synthetic dip data")
    print("-" * 74)
    true_amplitude, true_wavelength = 150.0, 1500.0
    x_sample = np.linspace(0.0, 3.0 * true_wavelength, 24)
    dips_true = fold_dip(x_sample, true_amplitude, true_wavelength)
    rng = np.random.default_rng(20261014)
    noise = rng.normal(0.0, 1.5, size=x_sample.size)   # 1.5 deg, SYNTHETIC
    dips_obs = dips_true + noise
    print(f"  synthetic truth: amplitude {true_amplitude:.0f} m, wavelength "
          f"{true_wavelength:.0f} m")
    print(f"  {x_sample.size} dip measurements with 1.5 deg random error "
          f"(a realistic")
    print("  field precision for a compass-clinometer reading)")

    # The dip is the arctangent of the slope; fit the slope itself.
    slope_obs = np.tan(np.radians(dips_obs))
    # slope = -A k sin(k x), so a sinusoid of known phase: fit a + b cos + c sin
    design = np.column_stack([np.ones_like(x_sample),
                              np.cos(2 * np.pi * x_sample / true_wavelength),
                              np.sin(2 * np.pi * x_sample / true_wavelength)])
    coefficients, *_ = np.linalg.lstsq(design, slope_obs, rcond=None)
    sine_amp = coefficients[2]
    recovered_amplitude = abs(sine_amp) * true_wavelength / (2 * np.pi)
    residual = slope_obs - design @ coefficients
    print()
    print(f"  fitted sine coefficient = {sine_amp:.5f} (slope units)")
    print(f"  recovered amplitude = |c| lambda/(2 pi) = "
          f"{recovered_amplitude:.1f} m against a true {true_amplitude:.1f} m")
    print(f"  error {recovered_amplitude - true_amplitude:+.1f} m "
          f"({(recovered_amplitude - true_amplitude) / true_amplitude:+.2%})")
    print(f"  rms residual {np.sqrt(np.mean(residual ** 2)):.5f} in slope units "
          f"= {np.degrees(np.arctan(np.sqrt(np.mean(residual ** 2)))):.3f} deg "
          f"in dip")
    print()
    print("  Note what the fit assumed: the wavelength was supplied. Fitting the")
    print("  frequency as well is a nonlinear problem, and with only the dips of "
          "one")
    print("  surface it is poorly conditioned when the fold is gentle. That is "
          "the")
    print("  practical reason field studies report both dip and wavelength, and "
          "why")
    print("  a map with few dip measurements supports only a rough fold shape.")


def part_three() -> None:
    print()
    print("3. Ramsay's thickness classification")
    print("-" * 74)
    print("  For a fold with limb dip alpha, define the thickness ratio")
    print("  t' = t_alpha / t_0 (thickness normal to the layer at dip alpha,")
    print("  divided by the thickness at the hinge) and the dip ratio")
    print("  alpha' = alpha / 90 deg. The two end-member mechanisms give")
    print("  t' = cos(alpha)  (parallel folding, constant orthogonal thickness)")
    print("  t' = 1           (similar folding, constant vertical thickness).")
    print()
    print(f"{'alpha (deg)':>12}{'alpha-prime':>13}{'parallel t-prime':>19}"
          f"{'similar t-prime':>18}{'class':>12}")
    for alpha in (10.0, 30.0, 50.0, 70.0, 90.0):
        t_parallel = np.cos(np.radians(alpha))
        t_similar = 1.0
        if t_parallel > 0.9:
            cls = "1A/1B"
        elif t_parallel > 0.5:
            cls = "1C"
        else:
            cls = "3"
        print(f"  {alpha:>12.1f}{alpha / 90.0:>13.3f}{t_parallel:>19.4f}"
              f"{t_similar:>18.4f}{cls:>12}")
    print("  The classification is a shape measurement, and it is diagnostic of "
          "the")
    print("  mechanism only because the two mechanisms predict different curves:")
    print("  t' falling as cos(alpha) means the layers stayed parallel (so the")
    print("  deformation was by flexural slip between layers), whereas t' staying")
    print("  near 1 while the dip grows means the layers were flattened in the")
    print("  vertical direction, which is similar folding.")
    print()
    print("  The area check that makes the two mechanisms different:")
    for alpha in (30.0, 60.0):
        r = np.radians(alpha)
        # Layer-parallel slip accumulated across a parallel (flexural-slip) fold.
        slip_factor = 2.0 * np.tan(r / 2.0)
        print(f"    alpha = {alpha:>4.1f} deg: flexural-slip shear strain "
              f"gamma = 2 tan(alpha/2) = {slip_factor:.4f};")
        print(f"      homogeneous simple shear to the same dip would need "
              f"gamma = tan(alpha) = {np.tan(r):.4f}")
    print("  The two numbers differ, which is why the measurement of finite "
          "strain")
    print("  across a limb, not just the shape, is what identifies a mechanism.")


def dominant_wavelength_ratio(viscosity_ratio: float) -> float:
    """Dominant wavelength / layer thickness for buckling of a viscous layer.

    The classical result for a single competent layer of viscosity eta_l in a
    matrix of viscosity eta_m is that the amplification rate is maximal at
        lambda_d / d = 2 pi (G / 6)^(1/3),  G = eta_l / eta_m,
    so the wavelength depends only on the cube root of the viscosity ratio. This
    is a derived scaling of the viscous buckling analysis, not a fitted relation.
    """
    return 2.0 * np.pi * (viscosity_ratio / 6.0) ** (1.0 / 3.0)


def part_four() -> None:
    print()
    print("4. Buckling: the dominant wavelength of a folded layer")
    print("-" * 74)
    print("  lambda_d / d = 2 pi (G/6)^(1/3) with G = layer/matrix viscosity")
    print(f"{'G':>8}{'G^1/6':>9}{'lambda_d/d':>13}{'for d = 100 m (m)':>20}")
    for g in (10.0, 30.0, 100.0, 300.0, 1000.0):
        ratio = dominant_wavelength_ratio(g)
        print(f"  {g:>8.1f}{g ** (1.0 / 6.0):>9.3f}{ratio:>13.4f}"
              f"{ratio * 100.0:>20.1f}")
    print("  A factor of 100 in the viscosity ratio changes the wavelength by a")
    print("  factor of 100^(1/3) = "
          f"{100 ** (1 / 3):.3f}, from "
          f"{dominant_wavelength_ratio(10):.2f} to "
          f"{dominant_wavelength_ratio(1000):.2f} layer thicknesses.")
    print("  The third-power dependence, and its inverse, is the single most")
    print("  useful thing about this result: a measured fold wavelength gives the")
    print("  viscosity ratio only as its CUBE, so a factor of two in wavelength")
    print("  is a factor of eight in viscosity ratio. Wavelengths are easy to")
    print("  measure and viscosity ratios are hard to measure, so the relation is")
    print("  used in this direction -- as a consistency check, not a")
    print("  measurement.")
    print()
    print("  Verification of the scaling by finite difference on the formula:")
    g1, g2 = 30.0, 240.0
    ratio_measured = (dominant_wavelength_ratio(g2)
                      / dominant_wavelength_ratio(g1))
    exponent = np.log(ratio_measured) / np.log(g2 / g1)
    print(f"    from G = {g1:.0f} to G = {g2:.0f} (factor {g2 / g1:.0f}), the")
    print(f"    wavelength ratio is {ratio_measured:.6f} = "
          f"{g2 / g1:.0f}^({exponent:.6f})")
    print(f"    fitted exponent {exponent:.6f} against the predicted 1/3 = "
          f"{1 / 3:.6f}")


def belt_excess_area_and_shortening(amplitude: float, wavelength: float,
                                    n_waves: int, n_points: int = 2000001):
    """Excess area and bed-length shortening of a sinusoidal fold belt.

    The marker is w(x) = A (1 - cos(2 pi x / lambda)) / 2 for x over n_waves
    wavelengths, which is non-negative and periodic and so has no overall tilt.
    The excess area is the integral of w, and the shortening is the arc length
    of the folded marker minus its chord length.
    """
    x = np.linspace(0.0, n_waves * wavelength, n_points)
    dx = x[1] - x[0]
    w = amplitude * (1.0 - np.cos(2.0 * np.pi * x / wavelength)) / 2.0
    dw = amplitude * np.pi / wavelength * np.sin(2.0 * np.pi * x / wavelength)
    excess_area = float(np.sum(w) * dx)
    arc = float(np.sum(np.sqrt(1.0 + dw ** 2)) * dx)
    shortening = arc - (x[-1] - x[0])
    return excess_area, shortening


def detachment_depth_closed_form(amplitude: float, wavelength: float) -> float:
    """h = 2 lambda^2 / (pi^2 A) for a balanced sinusoidal fold belt.

    With n waves, A_excess = n lambda A / 2.  The arc-line excess to second
    order in the limb dip is S = (1/2) integral of (dw/dx)^2 dx
    = n pi^2 A^2 / (4 lambda).  Hence h = A_excess / S = 2 lambda^2 / (pi^2 A),
    in which the number of waves cancels: the recovered depth depends only on
    the amplitude and the wavelength of the fold belt.
    """
    return 2.0 * wavelength ** 2 / (np.pi ** 2 * amplitude)


def part_five() -> None:
    print()
    print("5. Excess area and the depth to detachment, inverted numerically")
    print("-" * 74)
    print("  Chamberlin's excess-area method states h = A / S, with A the excess")
    print("  area of the folded section above its regional datum and S the")
    print("  bed-length shortening. It is a statement about where the shortening")
    print("  is accommodated, so it is a kinematic model and not a measurement.")
    print()
    print("  For a sinusoidal fold belt it has a closed form. With n waves of")
    print("  amplitude A and wavelength lambda:")
    print("    A_excess = n lambda A / 2")
    print("    S        = n pi^2 A^2 / (4 lambda)   (to second order in the dip)")
    print("    h        = 2 lambda^2 / (pi^2 A), independent of n")
    print("  That prediction is testable, so it is tested:")
    amplitude, wavelength = 800.0, 4000.0
    print()
    print(f"  amplitude {amplitude:.0f} m, wavelength {wavelength:.0f} m, "
          f"maximum limb dip "
          f"{np.degrees(np.arctan(2 * np.pi * amplitude / wavelength)):.1f} deg,")
    print(f"  predicted h = {detachment_depth_closed_form(amplitude, wavelength):,.1f} m")
    print(f"{'waves n':>9}{'A_excess (m^2)':>17}{'S (m)':>11}"
          f"{'h = A/S (m)':>14}{'closed form (m)':>17}{'difference':>13}")
    for n_waves in (2, 5, 10, 20):
        area, shortening = belt_excess_area_and_shortening(amplitude, wavelength,
                                                           n_waves)
        h_num = area / shortening
        h_closed = detachment_depth_closed_form(amplitude, wavelength)
        print(f"  {n_waves:>9}{area:>17,.0f}{shortening:>11,.2f}"
              f"{h_num:>14,.1f}{h_closed:>17,.1f}{h_num - h_closed:>+13.2f}")
    h_numeric = area / shortening
    h_closed = detachment_depth_closed_form(amplitude, wavelength)
    print("  The recovered depth is independent of how many waves the belt")
    print("  contains, which is the content of the closed form. The numerical")
    print(f"  value {h_numeric:,.1f} m exceeds the closed form {h_closed:,.1f} m by")
    print(f"  {(h_numeric - h_closed) / h_closed:.2%}, and that gap is not an error in the")
    print("  numerics: it is the second-order arc-length approximation breaking")
    print("  down. At this maximum limb dip the expansion of sqrt(1 + w'^2) in w'")
    print("  is no longer adequate, and the approximation understates the")
    print("  shortening and therefore understates the depth. The rule that")
    print("  follows is to use the exact arc length whenever the limbs are")
    print("  steeper than about 30 deg, which is most folds of interest.")
    print()
    print("  What the method is sensitive to, and how much (numerical, exact arc):")
    print(f"{'amplitude (m)':>15}{'wavelength (m)':>16}{'h (m)':>11}"
          f"{'h for A+10% (m)':>18}{'h for lambda+10% (m)':>22}")

    def numeric_depth(amp: float, wl: float) -> float:
        a_area, s_short = belt_excess_area_and_shortening(amp, wl, 4,
                                                          n_points=200001)
        return a_area / s_short

    for amp in (600.0, 800.0, 1000.0):
        for wl in (3000.0, 4000.0):
            h_val = numeric_depth(amp, wl)
            h_amp = numeric_depth(amp * 1.1, wl)
            h_wl = numeric_depth(amp, wl * 1.1)
            print(f"  {amp:>15,.0f}{wl:>16,.0f}{h_val:>11,.0f}{h_amp:>18,.0f}"
                  f"{h_wl:>22,.0f}")
    h_ref = numeric_depth(800.0, 4000.0)
    print(f"  the two perturbed columns change h by "
          f"{numeric_depth(880.0, 4000.0) / h_ref - 1.0:+.1%} and "
          f"{numeric_depth(800.0, 4400.0) / h_ref - 1.0:+.1%} respectively")
    print("  The asymmetry is the point: h is proportional to 1/A but to lambda")
    print("  squared, so the two 10 per cent perturbations above move the depth by")
    print("  different amounts in different directions. Detachment depths from")
    print("  this method are limited by the wavelength estimate, and the fold-belt")
    print("  wavelength is the quantity most sensitive to how much of the belt is")
    print("  exposed.")
    print()

    print("  The kinematic caveat, stated rather than hidden: h = A/S is exact")
    print("  only if the shortening is accommodated entirely by the detachment")
    print("  and the section is balanced. A single ramp with no flat gives")
    print("  A = h S / 2 instead, so the same fold belt would be inverted to")
    print(f"  h = 2 A / S = {2 * h_numeric:,.0f} m -- a factor of two, which is")
    print("  larger than every measurement error in the tables above. The")
    print("  kinematic model, not the measurements, sets the uncertainty.")


def part_six() -> None:
    print()
    print("6. Interlimb angle and fold tightness")
    print("-" * 74)
    print("  The interlimb angle is the angle between the two limbs of the fold,")
    print("  measured in the profile plane through the two hinge lines.")
    print(f"{'limb dip (deg)':>16}{'interlimb angle (deg)':>24}{'class':>16}")
    for limb in (5.0, 20.0, 40.0, 60.0, 80.0, 90.0):
        interlimb = 180.0 - 2.0 * limb
        if interlimb > 120.0:
            cls = "gentle/open"
        elif interlimb > 70.0:
            cls = "close"
        elif interlimb > 30.0:
            cls = "tight"
        elif interlimb > 0.0:
            cls = "isoclinal"
        else:
            cls = "not a fold"
        print(f"  {limb:>16.1f}{interlimb:>24.1f}{cls:>16}")
    print("  The interlimb angle is a shape descriptor with a standard set of")
    print("  names, and the names differ slightly between schemes; the honest")
    print("  practice is to report the angle and the scheme. What the angle does")
    print("  not tell you is the amplitude, the wavelength, or the shortening:")
    print("  a tight fold at one wavelength and a gentle fold at many "
          "wavelengths")
    print("  can shorten the same bed by the same amount.")


def main() -> None:
    print("=" * 76)
    print("Fold geometry, thickness classification, buckling, excess area")
    print("=" * 76)
    part_one()
    part_two()
    part_three()
    part_four()
    part_five()
    part_six()
    print()
    print("=" * 76)
    print("All folds above are SYNTHETIC constructions from the stated")
    print("mechanisms. The buckling relation and the excess-area method are")
    print("standard results quoted with their kinematic assumptions; the")
    print("verifications are internal (a least-squares recovery against a known")
    print("input, and a finite-difference exponent against 1/3).")
    print("=" * 76)


if __name__ == "__main__":
    main()
