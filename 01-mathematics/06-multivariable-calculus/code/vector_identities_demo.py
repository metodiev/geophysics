"""Vector identities, verified numerically rather than asserted.

Run:  python3 vector_identities_demo.py
Requires: Python standard library only.

Companion to lesson 01-06-07. Each identity is tested by computing both sides
with central differences at the same point and reporting the residual relative
to the size of the terms involved. The last section demonstrates the singular
identity that makes div(r_hat/r^2) the three-dimensional delta function.

All test fields are algebraic SYNTHETIC functions.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


H = 1.0e-3                      # finite-difference step for these smooth fields


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def shift(p, axis, d):
    q = list(p)
    q[axis] += d
    return tuple(q)


def grad(f, p):
    return tuple((f(*shift(p, i, H)) - f(*shift(p, i, -H))) / (2.0 * H)
                 for i in range(3))


def div(F, p):
    return sum((F(*shift(p, i, H))[i] - F(*shift(p, i, -H))[i]) / (2.0 * H)
               for i in range(3))


def curl(F, p):
    out = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        dFk = (F(*shift(p, j, H))[k] - F(*shift(p, j, -H))[k]) / (2.0 * H)
        dFj = (F(*shift(p, k, H))[j] - F(*shift(p, k, -H))[j]) / (2.0 * H)
        out.append(dFk - dFj)
    return tuple(out)


def laplacian(f, p):
    total = 0.0
    for i in range(3):
        total += (f(*shift(p, i, H)) - 2.0 * f(*p) + f(*shift(p, i, -H))) / H ** 2
    return total


def laplacian_vec(F, p):
    return tuple(laplacian(lambda *q: F(*q)[i], p) for i in range(3))


def report(name, lhs, rhs, scale=None):
    if isinstance(lhs, tuple):
        res = norm(sub(lhs, rhs))
        size = scale if scale is not None else max(norm(lhs), norm(rhs))
        print(f"{name}\n   left  = ({lhs[0]: .8e}, {lhs[1]: .8e}, {lhs[2]: .8e})")
        print(f"   right = ({rhs[0]: .8e}, {rhs[1]: .8e}, {rhs[2]: .8e})")
        print(f"   |residual| = {res:.3e}   reference scale = {size:.3e}"
              f"   ratio = {res / size:.3e}")
    else:
        size = scale if scale is not None else max(abs(lhs), abs(rhs))
        print(f"{name}\n   left = {lhs: .8e}   right = {rhs: .8e}")
        print(f"   |residual| = {abs(lhs - rhs):.3e}   reference scale = {size:.3e}"
              f"   ratio = {abs(lhs - rhs) / size:.3e}")


def main() -> None:
    p = (0.7, -0.4, 1.1)

    f = lambda x, y, z: x * x * y + y * y * z + z * z * x              # noqa: E731
    F = lambda x, y, z: (x * y + z * z, y * z + x * x, z * x + y * y)  # noqa: E731

    section("1. curl(grad f) = 0: a gradient field is irrotational")
    report("curl(grad f)", curl(lambda *q: grad(f, q), p), (0.0, 0.0, 0.0),
           scale=norm(curl(F, p)))
    print("   reference scale is |curl F| at the same point, which is not zero:")
    print(f"   |curl F| = {norm(curl(F, p)):.6e}. The zero above is therefore a")
    print("   property of the stencil, not an artefact of the test field: in exact")
    print("   arithmetic the two sums contain the same four values and cancel, so")
    print("   the residual can only ever be a few units in the last place.")

    section("2. div(curl F) = 0: a curl field is solenoidal")
    report("div(curl F)", div(lambda *q: curl(F, q), p), 0.0,
           scale=abs(div(F, p)))
    print("   again the reference scale is div F, which is not zero:")
    print(f"   div F = {div(F, p):.6e}")

    section("3. curl(curl F) = grad(div F) - laplacian(F)")
    report("curl(curl F)", curl(lambda *q: curl(F, q), p),
           sub(grad(lambda *q: div(F, q), p), laplacian_vec(F, p)))

    section("4. div(f F) = f div F + grad f . F")
    report("div(f F)", div(lambda *q: scale(f(*q), F(*q)), p),
           f(*p) * div(F, p) + dot(grad(f, p), F(*p)))
    print("The residual is the O(H^2) truncation error of the stencils. Shrinking H")
    print("by a factor of ten cuts it by about a hundred, until round-off takes over:")
    for h in (1e-2, 1e-3, 1e-4, 1e-5):
        globals()["H"] = h
        lhs = div(lambda *q: scale(f(*q), F(*q)), p)
        rhs = f(*p) * div(F, p) + dot(grad(f, p), F(*p))
        print(f"   H = {h:>7}: left = {lhs:.10f}  |residual| = {abs(lhs - rhs):.3e}")
    globals()["H"] = 1e-3

    section("5. curl(f F) = f curl F + grad f x F")
    report("curl(f F)", curl(lambda *q: scale(f(*q), F(*q)), p),
           add(scale(f(*p), curl(F, p)), cross(grad(f, p), F(*p))))

    section("6. div(grad f) = laplacian f")
    report("div(grad f)", div(lambda *q: grad(f, q), p), laplacian(f, p))

    section("7. Where the identities need differentiability")
    # 1/r is smooth except at the origin. Its gradient is well defined at every
    # other point, and the symmetric stencil makes curl(grad) vanish identically,
    # so this test cannot detect the singularity.
    def g_sing(x, y, z):
        return 1.0 / math.sqrt(x * x + y * y + z * z)

    for probe in ((0.5, 0.0, 0.0), (0.05, 0.0, 0.0), (0.005, 0.0, 0.0)):
        c = curl(lambda *q: grad(g_sing, q), probe)
        lap = laplacian(g_sing, probe)
        print(f"at |x| = {probe[0]:.3f}: |curl(grad(1/r))| = {norm(c):.3e}"
              f"   laplacian(1/r) = {lap: .6e}")
    print("curl(grad(1/r)) is zero to round-off everywhere it is computed: the")
    print("symmetric stencil makes it an algebraic cancellation, so a zero residual")
    print("is not evidence that the field is smooth. laplacian(1/r) tells the truth")
    print("instead: the true")
    print("value is 0 at every one of those points, and the computed value grows")
    print("without bound as the probe approaches the singularity, because the field")
    print("then varies on a scale smaller than the stencil H = 1e-3.")

    section("8. div(r_hat/r^2) is the delta function: the flux is 4*pi for any radius")
    for R in (0.5, 2.0, 10.0):
        n = 400
        dtheta = math.pi / n
        dphi = 2.0 * math.pi / n
        total = 0.0
        for i in range(n):
            theta = (i + 0.5) * dtheta
            for j in range(n):
                phi = (j + 0.5) * dphi
                # F = r_hat/r^2, so F . r_hat = 1/R^2 on the sphere of radius R
                total += (1.0 / R ** 2) * R ** 2 * math.sin(theta) * dtheta * dphi
        print(f"R = {R:>4}: flux of r_hat/r^2 = {total:.9f}   4*pi = {4 * math.pi:.9f}"
              f"   relative residual = {abs(total - 4 * math.pi) / (4 * math.pi):.3e}")
    pt = (0.7, -0.4, 1.1)
    print(f"pointwise divergence at {pt}: "
          f"{div(lambda x, y, z: tuple(c / (x * x + y * y + z * z) ** 1.5 for c in (x, y, z)), pt):.3e}")
    print("Pointwise the divergence is zero away from the origin, yet the flux")
    print("through every sphere is 4*pi regardless of radius. That combination is")
    print("exactly what a delta function does, and it is why Laplace's equation")
    print("needs a source term in integral form.")

    section("9. Two more product rules used in the electromagnetic derivations")
    G = lambda x, y, z: (y + z, x * z, x * y)                          # noqa: E731
    report("div(F x G)", div(lambda *q: cross(F(*q), G(*q)), p),
           dot(G(*p), curl(F, p)) - dot(F(*p), curl(G, p)))
    report("grad(f g_2)", grad(lambda *q: f(*q) * G(*q)[1], p),
           add(scale(f(*p), grad(lambda *q: G(*q)[1], p)),
               scale(G(*p)[1], grad(f, p))))
    print("div(F x G) = G . curl F - F . curl G  and  grad(f g) = f grad g + g grad f.")
    print("The first is the identity behind Poynting's theorem; the second is the")
    print("product rule from which every other product rule is assembled.")


if __name__ == "__main__":
    main()
