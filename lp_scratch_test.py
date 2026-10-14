from fractions import Fraction

def solve_lp(c, a, b):
    m, n = len(a), len(c)
    need = [i for i in range(m) if Fraction(b[i]) < 0]
    total = n + m + len(need)
    art_col = {i: n + m + k for k, i in enumerate(need)}
    rows, basis = [], []
    for i in range(m):
        row = [Fraction(0)] * (total + 1)
        rhs = Fraction(b[i]); sign = 1
        if rhs < 0:
            sign, rhs = -1, -rhs
        for j in range(n):
            row[j] = sign * Fraction(a[i][j])
        if sign == 1:
            row[n + i] = Fraction(1); basis.append(n + i)
        else:
            row[n + i] = Fraction(-1); row[art_col[i]] = Fraction(1); basis.append(art_col[i])
        row[total] = rhs
        rows.append(row)

    def reduced_costs(rows, basis, cost):
        r = [Fraction(v) for v in cost]
        for i, var in enumerate(basis):
            if r[var] != 0:
                f = r[var]
                r = [r[j] - f * rows[i][j] for j in range(len(r))]
        return r

    def optimise(rows, basis, cost, allowed):
        iters = 0
        while True:
            r = reduced_costs(rows, basis, cost)
            entering = next((j for j in allowed if r[j] < 0), None)
            if entering is None:
                z = sum(cost[basis[i]] * rows[i][-1] for i in range(len(basis)))
                return r, iters, z
            leaving, best = None, None
            for i in range(len(basis)):
                if rows[i][entering] > 0:
                    ratio = rows[i][-1] / rows[i][entering]
                    if best is None or ratio < best:
                        leaving, best = i, ratio
            if leaving is None:
                return r, iters, None
            pv = rows[leaving][entering]
            rows[leaving] = [v / pv for v in rows[leaving]]
            for i in range(len(rows)):
                if i != leaving and rows[i][entering] != 0:
                    f = rows[i][entering]
                    rows[i] = [rows[i][j] - f * rows[leaving][j] for j in range(len(rows[i]))]
            basis[leaving] = entering
            iters += 1

    cost1 = [Fraction(0)] * (total + 1)
    for col in art_col.values():
        cost1[col] = Fraction(1)
    _, it1, _ = optimise(rows, basis, cost1, list(range(total)))
    phase1 = sum(rows[i][-1] for i in range(len(basis)) if basis[i] in art_col.values())
    if phase1 != 0:
        return None, None, it1, None, "infeasible"
    # Drive artificials out of the basis; drop rows that are redundant.
    keep = []
    for i in range(len(basis)):
        if basis[i] in art_col.values():
            pivoted = False
            for j in range(total):
                if j not in art_col.values() and rows[i][j] != 0:
                    pv = rows[i][j]
                    rows[i] = [v / pv for v in rows[i]]
                    for k in range(len(rows)):
                        if k != i and rows[k][j] != 0:
                            f = rows[k][j]
                            rows[k] = [rows[k][t] - f * rows[i][t] for t in range(len(rows[k]))]
                    basis[i] = j
                    pivoted = True
                    break
            if not pivoted:
                continue
        keep.append(i)
    rows = [rows[i] for i in keep]
    basis = [basis[i] for i in keep]
    cost2 = [Fraction(v) for v in c] + [Fraction(0)] * (total + 1 - n)
    allowed2 = [j for j in range(total) if j not in art_col.values()]
    r, it2, z = optimise(rows, basis, cost2, allowed2)
    if z is None:
        return None, None, it1 + it2, None, "unbounded"
    x = [Fraction(0)] * n
    for i, var in enumerate(basis):
        if var < n:
            x[var] = rows[i][-1]
    dual = [-r[n + i] for i in range(m)]
    return x, z, it1 + it2, dual, "optimal"

# Test 1: min x1+x2 s.t. x1+x2 >= 1  (as -x1-x2 <= -1)
x,z,it,dual,st = solve_lp([1,1],[[-1,-1]],[-1])
print("T1", st, [str(v) for v in x], z, it, [str(d) for d in dual])

# Test 2: max-ish blending
x,z,it,dual,st = solve_lp([1,3,2],
    [[1,1,1],[-1,-1,-1],[2.6,2.7,2.75],[-2.6,-2.7,-2.75],[5.8,5.2,4.4],[-5.8,-5.2,-4.4]],
    [1,-1,2.6725,-2.6725,5.24,-5.24])
print("T2", st, [str(v) for v in x], z, it, [str(d) for d in dual])

# Test 3: unbounded
x,z,it,dual,st = solve_lp([-1],[[1]],[2])
print("T3", st)

# Test 4: infeasible
x,z,it,dual,st = solve_lp([1],[[1],[-1]],[1,-2])
print("T4", st)

# dual consistency check on T2
print("dual b.y =", sum(Fraction(str(b_))*d for b_,d in zip([1,-1,2.6725,-2.6725,5.24,-5.24], dual)))
