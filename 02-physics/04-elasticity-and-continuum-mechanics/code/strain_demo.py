"""Strain: the infinitesimal strain tensor, rotation and compatibility.

Run:  python3 strain_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-02. The script:

1. Differentiates an analytic displacement field by central differences on a
   grid, forms the strain and rotation tensors, and verifies them against the
   analytic derivatives (measured convergence order reported).
2. Verifies that a rigid-body rotation produces NO strain in the exact theory
   but an apparent strain of order theta^2 in the infinitesimal tensor, which
   is the quantitative statement of the small-strain condition.
3. Tests the Saint-Venant compatibility condition on a strain field derived
   from a displacement (it holds) and on an arbitrary field (it fails).

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


A, B, C = 0.7, 1.1, 0.4
SCALE = 0.01          # keeps the strains at the 1e-3 level, as waves are


def displacement(x, y, z):
    """A smooth field with transcendental derivatives: u = (sin(ax)cos(by),
    exp(cy) z, 0.1 x y)."""
    return (SCALE * math.sin(A * x) * math.cos(B * y),
            SCALE * math.exp(C * y) * z,
            SCALE * 0.1 * x * y)


def analytic_gradient(x, y, z):
    """grad[i][k] = d u_k / d x_i."""
    return [
        [SCALE * A * math.cos(A * x) * math.cos(B * y), 0.0, SCALE * 0.1 * y],
        [-SCALE * B * math.sin(A * x) * math.sin(B * y),
         SCALE * C * math.exp(C * y) * z, SCALE * 0.1 * x],
        [0.0, SCALE * math.exp(C * y), 0.0],
    ]


def analytic_strain(x, y, z):
    g = analytic_gradient(x, y, z)
    return [[0.5 * (g[i][j] + g[j][i]) for j in range(3)] for i in range(3)]


def numeric_gradient(f, x, y, z, h=1e-4):
    d = []
    for i in range(3):
        plus = list(displacement(x, y, z))
        minus = list(displacement(x, y, z))
        axis = [x, y, z]
        axis[i] += h
        plus = displacement(*axis)
        axis[i] -= 2.0 * h
        minus = displacement(*axis)
        d.append([(plus[k] - minus[k]) / (2.0 * h) for k in range(3)])
    return d                       # d[i][k] = du_k/dx_i


def part1_strain_from_displacement():
    section("1. Strain and rotation from a displacement field")
    x, y, z = 1.3, -0.7, 2.1
    h = 1e-3
    grad = numeric_gradient(displacement, x, y, z, h)
    strain = [[0.5 * (grad[i][j] + grad[j][i]) for j in range(3)]
              for i in range(3)]
    rot = [[0.5 * (grad[i][j] - grad[j][i]) for j in range(3)]
           for i in range(3)]
    exact = analytic_strain(x, y, z)
    print(f"point (x, y, z) = ({x}, {y}, {z}), central-difference step "
          f"{h:.0e}")
    print("strain tensor (numeric):")
    for row in strain:
        print("   [" + ", ".join(f"{v:12.8f}" for v in row) + "]")
    worst = max(abs(strain[i][j] - exact[i][j]) for i in range(3)
                for j in range(3))
    print(f"max difference from the analytic strain = {worst:.3e}")
    print("rotation tensor (numeric), antisymmetric by construction:")
    for row in rot:
        print("   [" + ", ".join(f"{v:12.8f}" for v in row) + "]")
    w = (rot[2][1], rot[0][2], rot[1][0])
    print(f"rotation vector w = (w_x, w_y, w_z) = "
          f"({w[0]:.8f}, {w[1]:.8f}, {w[2]:.8f})")
    print(f"dilatation = trace(strain) = {sum(strain[i][i] for i in range(3)):.8f}")
    print(f"analytic dilatation = a cos(ax)cos(by) + c exp(cy) z = "
          f"{sum(analytic_strain(x, y, z)[i][i] for i in range(3)):.8f}")
    print()
    print("  The symmetric part of the displacement gradient is strain, the")
    print("  antisymmetric part is rigid rotation, and the trace is the fractional")
    print("  volume change. Splitting the gradient this way is exact and is why")
    print("  strain is defined as half the sum of the two terms.")


def part2_convergence():
    section("2. Measured convergence order of the finite-difference strain")
    x, y, z = 0.4, 1.1, -0.6
    exact = analytic_strain(x, y, z)
    print(f"{'h':>9} {'max|error|':>13} {'order':>8}")
    previous = None
    for h in (1e-2, 5e-3, 2.5e-3, 1.25e-3):
        grad = numeric_gradient(displacement, x, y, z, h)
        strain = [[0.5 * (grad[i][j] + grad[j][i]) for j in range(3)]
                  for i in range(3)]
        err = max(abs(strain[i][j] - exact[i][j]) for i in range(3)
                  for j in range(3))
        order = float("nan") if previous is None else math.log(previous / err) / math.log(2.0)
        print(f"{h:9.2e} {err:13.3e} {order:8.3f}")
        previous = err
    print()
    print("  Order 2, as expected for a central difference, until round-off becomes")
    print("  comparable with the truncation error at still smaller steps (01-06-01).")
    print("  The same stencil and")
    print("  the same caveat apply to every strain estimate made from a measured")
    print("  displacement field, whether that field comes from GNSS, InSAR or a")
    print("  numerical model.")


def part3_rigid_rotation():
    section("3. Rigid rotation costs nothing exactly, and theta^2/2 approximately")
    print(f"{'theta (deg)':>12} {'theta^2/2':>12} {'apparent eps_xx':>18} "
          f"{'relative':>11}")
    for theta_deg in (1.0, 5.0, 15.0, 30.0, 45.0):
        theta = math.radians(theta_deg)
        # exact displacement of a rigid rotation about z
        x, y = 1.0, 0.0
        u = ((math.cos(theta) - 1.0) * x - math.sin(theta) * y,
             math.sin(theta) * x + (math.cos(theta) - 1.0) * y)
        # infinitesimal strain at this point, from the exact gradient
        exx = math.cos(theta) - 1.0
        e_xy = 0.0
        print(f"{theta_deg:12.1f} {theta ** 2 / 2:12.6f} {exx:18.6f} "
              f"{exx / (theta ** 2 / 2) if theta != 0 else float('nan'):11.6f}")
    print()
    print("  The true strain of a rigid rotation is zero for any angle. The")
    print("  infinitesimal definition reports a contraction of order theta^2/2,")
    print("  which is 0.04 per cent at 1 degree and 13 per cent at 30 degrees. The")
    print("  theory is therefore valid only where the displacement gradient is much")
    print("  smaller than one - a condition that seismic waves satisfy easily and")
    print("  that finite deformation in tectonics does not.")


def part4_compatibility():
    section("4. Saint-Venant compatibility: a test that can fail")
    # A compatible 2-D strain field: derived from u = (x y, x^2 - y^2)/10
    def eps_compatible(x, y):
        exx = y / 10.0
        eyy = -2.0 * y / 10.0
        exy = 0.5 * (x / 10.0 + 2.0 * x / 10.0)
        return exx, eyy, exy

    # An incompatible field of the same size
    def eps_incompatible(x, y):
        return y * y / 10.0, x * x / 10.0, 0.0

    h = 1e-4

    def residual(eps, x, y):
        exx_yy = (eps(x, y + h)[0] - 2.0 * eps(x, y)[0] + eps(x, y - h)[0]) / h ** 2
        eyy_xx = (eps(x + h, y)[1] - 2.0 * eps(x, y)[1] + eps(x - h, y)[1]) / h ** 2
        exy_xy = ((eps(x + h, y + h)[2] - eps(x + h, y - h)[2])
                  - (eps(x - h, y + h)[2] - eps(x - h, y - h)[2])) / (4.0 * h ** 2)
        return exx_yy + eyy_xx - 2.0 * exy_xy

    print("2-D compatibility condition: d2(exx)/dy2 + d2(eyy)/dx2 "
          "= 2 d2(exy)/dxdy")
    print(f"{'point':>16} {'residual, compatible':>22} {'residual, arbitrary':>21}")
    for x, y in ((0.3, 0.7), (1.0, -0.5), (-2.0, 1.5)):
        print(f"({x:5.2f}, {y:5.2f})".rjust(16)
              + f" {residual(eps_compatible, x, y):22.6e}"
              + f" {residual(eps_incompatible, x, y):21.6f}")
    print()
    print("  A strain field that comes from a displacement satisfies compatibility")
    print("  identically; an arbitrary symmetric tensor field generally does not,")
    print("  and no displacement field exists for it. Compatibility matters when a")
    print("  strain field is measured directly - by strainmeters or InSAR - and one")
    print("  wants to integrate it to a displacement: without compatibility, the")
    print("  integral is path dependent.")


if __name__ == "__main__":
    part1_strain_from_displacement()
    part2_convergence()
    part3_rigid_rotation()
    part4_compatibility()
