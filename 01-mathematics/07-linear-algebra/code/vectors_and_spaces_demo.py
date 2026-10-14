"""Vectors, vector spaces and basis changes, on geophysical examples.

Run:  python3 vectors_and_spaces_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-01.

Section 1 fixes the notation of a three-component recording. Section 3 builds an
orthonormal basis out of three *non*-orthogonal vectors and shows the point of a
basis: the coordinates change, the vector does not. Section 5 does the same thing
inside model space, where "the same model" has two perfectly legal coordinate
triples.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def vec(*components: float) -> list[float]:
    return list(components)


def add(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def sub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def scale(a: list[float], s: float) -> list[float]:
    return [s * x for x in a]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def unit(a: list[float]) -> list[float]:
    n = norm(a)
    return [x / n for x in a]


def angle_deg(a: list[float], b: list[float]) -> float:
    cosine = dot(a, b) / (norm(a) * norm(b))
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def fmt(a: list[float], places: int = 6) -> str:
    return "(" + ", ".join(f"{x:.{places}f}" for x in a) + ")"


def gram_schmidt(vectors: list[list[float]]) -> list[list[float]]:
    """Classical Gram-Schmidt, returning orthonormal vectors in input order."""
    basis: list[list[float]] = []
    for v in vectors:
        w = list(v)
        for e in basis:
            w = sub(w, scale(e, dot(w, e)))
        if norm(w) < 1e-12:
            print(f"  [warning] vector {fmt(v, 4)} is dependent on the previous "
                  f"ones; it contributes nothing to the basis")
            continue
        basis.append(unit(w))
    return basis


def main() -> None:
    section("1. A three-component recording is a vector in R^3")
    # Illustrative particle-motion amplitudes in counts, one time sample:
    # north, east, vertical. No units are claimed for the numbers themselves.
    u = vec(0.80, -0.52, 1.70)
    print(f"  u                = {fmt(u, 4)}   (N, E, Z amplitudes, counts)")
    print(f"  ||u||            = {norm(u):.6f}  counts")
    print(f"  u / ||u||        = {fmt(unit(u), 6)}")
    print(f"  angle to N axis  = {angle_deg(u, vec(1, 0, 0)):.4f} deg")
    print(f"  angle to E axis  = {angle_deg(u, vec(0, 1, 0)):.4f} deg")
    print(f"  angle to Z axis  = {angle_deg(u, vec(0, 0, 1)):.4f} deg")
    print(f"  incidence from vertical      = {angle_deg(u, vec(0, 0, 1)):.4f} deg")
    print(f"  back azimuth from north      = {math.degrees(math.atan2(-0.52, 0.80)) % 360:.4f} deg")
    print("\nReading: the same physical displacement has three coordinate")
    print("representations depending on which axes you chose. A vector is an")
    print("object; the triple of numbers is its coordinates in one basis.")

    section("2. The inner product measures agreement, not similarity of size")
    a = vec(3.0, -1.0, 2.0)
    b = vec(1.0, 4.0, -2.0)
    print(f"  a = {fmt(a, 4)}, b = {fmt(b, 4)}")
    print(f"  a . b            = {dot(a, b):.6f}   (negative => obtuse)")
    print(f"  angle(a, b)      = {angle_deg(a, b):.4f} deg")
    print(f"  a . (a+5b)       = {dot(a, add(a, scale(b, 5.0))):.6f}")
    print(f"  |a| |b|          = {norm(a) * norm(b):.6f}")
    print(f"  |a . b| <= |a||b|          : {abs(dot(a, b)) <= norm(a) * norm(b) + 1e-12}")
    print(f"  |a + b| <= |a| + |b|       : "
          f"{norm(add(a, b)) <= norm(a) + norm(b) + 1e-12}"
          f"  ({norm(add(a, b)):.6f} <= {norm(a) + norm(b):.6f})")
    print(f"  |a + b|^2 - (|a|^2+|b|^2)  = {norm(add(a, b)) ** 2 - (norm(a) ** 2 + norm(b) ** 2):.6f}"
          f"   (= 2 a.b = {2 * dot(a, b):.6f})")
    print("\nReading: orthogonality is the zero of the inner product. It is the")
    print("whole basis of the least-squares machinery of lesson 01-07-07.")

    section("3. Gram-Schmidt: an orthonormal basis from non-orthogonal vectors")
    v1 = vec(2.0, 1.0, 0.0)
    v2 = vec(1.0, 2.0, -1.0)
    v3 = vec(0.0, 1.0, 2.0)
    print(f"  v1 = {fmt(v1, 6)}")
    print(f"  v2 = {fmt(v2, 6)}")
    print(f"  v3 = {fmt(v3, 6)}")
    print(f"  angle(v1, v2) = {angle_deg(v1, v2):.4f} deg, "
          f"angle(v1, v3) = {angle_deg(v1, v3):.4f} deg, "
          f"angle(v2, v3) = {angle_deg(v2, v3):.4f} deg")
    basis = gram_schmidt([v1, v2, v3])
    for index, e in enumerate(basis, start=1):
        print(f"  e{index} = {fmt(e, 9)}")
    print("  orthonormality check |e_i . e_j|:")
    for i in range(len(basis)):
        row = " ".join(f"{dot(basis[i], basis[j]): .3e}" for j in range(len(basis)))
        print(f"    {row}")
    print("\nReading: each new vector is stripped of the components it already")
    print("has in the directions found so far. The residual norm after each")
    print("projection is the numerical measure of linear dependence.")

    section("4. Coordinates in the new basis; the vector is unchanged")
    for name, v in (("v1", v1), ("v2", v2), ("v3", v3)):
        coords = [dot(v, e) for e in basis]
        rebuilt = [0.0, 0.0, 0.0]
        for c, e in zip(coords, basis):
            rebuilt = add(rebuilt, scale(e, c))
        print(f"  {name}: coordinates {fmt(coords, 6)}")
        print(f"      reconstructed {fmt(rebuilt, 9)}   "
              f"error {norm(sub(rebuilt, v)):.3e}")
    print("\nReading: in the *original* basis, v1 has coordinates")
    print("(2, 1, 0). In the orthonormal basis it has three nonzero")
    print("coordinates. Both triples describe the same arrow; only the second")
    print("makes inner products trivial to compute (they are just dot products).")

    section("5. The same model in two parameterisations")
    # The model is a 2-D perturbation: a vertical slowness change and a
    # horizontal one, in s/km. Basis A is the natural (vertical, horizontal)
    # pair; basis B is the same plane rotated by 30 degrees, a perfectly legal
    # alternative parameterisation of the same model space.
    m = vec(1.0, 1.0)
    theta = math.radians(30.0)
    b1 = vec(math.cos(theta), math.sin(theta))
    b2 = vec(-math.sin(theta), math.cos(theta))
    print(f"  model vector m = {fmt(m, 6)}  (s/km)")
    print(f"  basis A: a1 = (1, 0), a2 = (0, 1)")
    print(f"  basis B: b1 = {fmt(b1, 6)}")
    print(f"          b2 = {fmt(b2, 6)}")
    print(f"  coordinates in A: {fmt([dot(m, vec(1, 0)), dot(m, vec(0, 1))], 6)}")
    print(f"  coordinates in B: {fmt([dot(m, b1), dot(m, b2)], 6)}")
    check = add(scale(b1, dot(m, b1)), scale(b2, dot(m, b2)))
    print(f"  reconstructed from B: {fmt(check, 9)}   error {norm(sub(check, m)):.3e}")
    print(f"  ||m|| in both bases: {norm(m):.6f} and "
          f"{math.hypot(dot(m, b1), dot(m, b2)):.6f}   (rotation is an isometry)")
    print("\nReading: ||m|| is a property of the model, not of the basis. The")
    print("optimality of a regularised inversion must therefore be stated in a")
    print("norm, and whoever chooses the norm chooses the inversion.")

    section("6. Independence is a numerical threshold, not a yes/no fact")
    v = vec(1.0, 1.0, 0.0)
    for delta in (1e-1, 1e-3, 1e-6, 1e-9, 1e-12):
        w = vec(1.0, 1.0 + delta, 0.0)
        basis2 = gram_schmidt([v, w])
        print(f"  delta = {delta:8.0e}   rank of span(v, w) found numerically "
              f"= {len(basis2)}   angle = {angle_deg(v, w):.6e} deg")
    print("\nReading: v and w are independent for every delta > 0, but the")
    print("arithmetic cannot tell them apart once delta is at the level of the")
    print("round-off. 'Independent' and 'numerically independent' are different")
    print("claims, and only the second one survives in a computer.")


if __name__ == "__main__":
    main()
