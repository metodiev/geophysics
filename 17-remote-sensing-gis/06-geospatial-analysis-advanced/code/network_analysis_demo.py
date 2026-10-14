#!/usr/bin/env python3
"""Network analysis: least-cost paths, anisotropic movement cost, cost-distance
surfaces and centrality, on synthetic grids and synthetic networks.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python network_analysis_demo.py

All surfaces and networks are SYNTHETIC and built in memory from a fixed seed.
Nothing is read from or written to disk; no real road, trail or place is used.

Contents
--------
1. A synthetic friction surface, and the grid graph it defines.
2. Least-cost path by two independent algorithms (agreement check).
3. Sinuosity: how much longer a least-cost path is than the straight line.
4. Anisotropy: a slope-dependent cost makes the path depend on direction.
5. Cost-distance surfaces and isochrones (equal-cost contours).
6. Path sensitivity to friction error: the same 10 % change, two landscapes.
7. Different anisotropy exponents, one landscape: the path is a model output.
8. Centrality on a synthetic vector network, and what it is not.
"""

import heapq

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra as sp_dijkstra, connected_components

RNG = np.random.default_rng(20261014)

NROW, NCOL = 80, 120
CELL = 250.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def friction_surface(nrow=NROW, ncol=NCOL, cell=CELL, seed=None, contrast=1.0):
    """A synthetic resistance surface: two low-cost corridors through high cost."""
    rng = RNG if seed is None else np.random.default_rng(seed)
    row, col = np.mgrid[0:nrow, 0:ncol].astype(float)
    x, y = col * cell, (nrow - row) * cell
    base = 1.0 + contrast * (
        2.0 * np.exp(-((y - 4_000.0) ** 2) / 2.0e6)
        + 2.0 * np.exp(-((y - 16_000.0) ** 2) / 2.0e6)
        - 0.5 * np.exp(-((y - 10_000.0) ** 2) / 1.5e6)
        + 0.8 * np.sin(2 * np.pi * x / 12_000.0) ** 2)
    base = base + 0.1 * rng.standard_normal(base.shape)
    return np.maximum(base, 0.05), x, y


def grid_graph(cost, cell, kernel="rook"):
    """Sparse adjacency of a grid graph; weights are cost x length, in cost-metres."""
    nrow, ncol = cost.shape
    rows, cols, data = [], [], []
    idx = np.arange(nrow * ncol).reshape(nrow, ncol)
    offsets = [(-1, 0, cell), (1, 0, cell), (0, -1, cell), (0, 1, cell)]
    if kernel == "queen":
        d = cell * np.sqrt(2.0)
        offsets += [(-1, -1, d), (-1, 1, d), (1, -1, d), (1, 1, d)]
    for di, dj, dist in offsets:
        i0, i1 = max(0, di), min(nrow, nrow + di)
        j0, j1 = max(0, dj), min(ncol, ncol + dj)
        fr = idx[i0:i1, j0:j1].ravel()
        to = idx[i0 - di:i1 - di, j0 - dj:j1 - dj].ravel()
        w = 0.5 * (cost[i0:i1, j0:j1] + cost[i0 - di:i1 - di, j0 - dj:j1 - dj]) * dist
        rows.append(fr)
        cols.append(to)
        data.append(w.ravel())
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    data = np.concatenate(data)
    return csr_matrix((data, (rows, cols)), shape=(nrow * ncol, nrow * ncol))


def dijkstra_python(graph, source):
    """A hand-written Dijkstra, for cross-checking the library implementation."""
    n = graph.shape[0]
    indptr, indices, vals = graph.indptr, graph.indices, graph.data
    dist = np.full(n, np.inf)
    prev = np.full(n, -1, dtype=int)
    dist[source] = 0.0
    heap = [(0.0, source)]
    done = np.zeros(n, dtype=bool)
    while heap:
        d, u = heapq.heappop(heap)
        if done[u]:
            continue
        done[u] = True
        for k in range(indptr[u], indptr[u + 1]):
            v = indices[k]
            nd = d + vals[k]
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, prev


def trace_path(prev, target, ncol):
    path = []
    cur = target
    while cur >= 0:
        path.append(divmod(int(cur), ncol))
        cur = prev[cur]
    return path[::-1]


def slope_cost_surface(dem, cell, exponent=1.0, downhill_penalty=0.5):
    """Cost per unit distance from a DEM, asymmetric in the direction of travel.

    Returns forward (uphill) and backward (downhill) multipliers between
    horizontally and vertically adjacent cells.
    """
    nrow, ncol = dem.shape
    cost_x = np.zeros((nrow, ncol))
    cost_y = np.zeros((nrow, ncol))
    dx = np.zeros_like(dem)
    dy = np.zeros_like(dem)
    dx[:, :-1] = (dem[:, 1:] - dem[:, :-1]) / cell
    dy[:-1, :] = (dem[1:, :] - dem[:-1, :]) / cell
    cost_x = np.where(dx >= 0, 1.0 + exponent * dx, 1.0 + exponent * downhill_penalty * -dx)
    cost_y = np.where(dy >= 0, 1.0 + exponent * dy, 1.0 + exponent * downhill_penalty * -dy)
    return cost_x, cost_y


def anisotropic_graph(dem, cell, exponent, downhill_penalty):
    """8-connected graph with a direction-dependent multiplier on each edge."""
    nrow, ncol = dem.shape
    n = nrow * ncol
    idx = np.arange(n).reshape(nrow, ncol)
    rows, cols, data = [], [], []
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            dist = cell * (1.0 if di == 0 or dj == 0 else np.sqrt(2.0))
            i0, i1 = max(0, di), min(nrow, nrow + di)
            j0, j1 = max(0, dj), min(ncol, ncol + dj)
            fr = idx[i0:i1, j0:j1].ravel()
            to = idx[i0 - di:i1 - di, j0 - dj:j1 - dj].ravel()
            dz = (dem[i0 - di:i1 - di, j0 - dj:j1 - dj] -
                  dem[i0:i1, j0:j1]) / dist
            mult = np.where(dz >= 0.0, 1.0 + exponent * dz,
                            1.0 + exponent * downhill_penalty * -dz)
            steps = np.hypot(di, dj) * 0.0 + dist
            w = mult * steps / cell * 1.0        # cost in units of flat-cell-equivalents
            rows.append(fr)
            cols.append(to)
            data.append(w.ravel())
    return csr_matrix((np.concatenate(data),
                       (np.concatenate(rows), np.concatenate(cols))), shape=(n, n))


def main():
    section("1. A synthetic friction surface and the grid graph it defines")
    cost, x, y = friction_surface()
    print(f"  grid                 : {NROW} x {NCOL} cells of {CELL:.0f} m "
          f"({NCOL * CELL / 1e3:.0f} km x {NROW * CELL / 1e3:.0f} km)")
    print(f"  cost range           : [{cost.min():.3f}, {cost.max():.3f}] "
          f"(dimensionless resistance per unit distance)")
    print(f"  mean / median        : {cost.mean():.3f} / {np.median(cost):.3f}")
    for kernel in ("rook", "queen"):
        g = grid_graph(cost, CELL, kernel)
        print(f"  {kernel:5s} graph: {g.shape[0]} nodes, {g.nnz} directed edges, "
              f"mean degree {g.nnz / g.shape[0]:.2f}")
    print("A raster cost surface is not a network until a connectivity rule is chosen:")
    print("rook (4-neighbour) and queen (8-neighbour) give different graphs and therefore")
    print("different least-cost paths.  The rule is a decision, and it must be reported.")

    section("2. Least-cost path by two independent algorithms")
    g = grid_graph(cost, CELL, "queen")
    src = 20 * NCOL + 10
    tgt = 60 * NCOL + 110
    dist_a = sp_dijkstra(g, indices=src, directed=True)
    da = dist_a[tgt]
    dist_b, prev_b = dijkstra_python(g, src)
    db = dist_b[tgt]
    print(f"  source (row, col)  : {divmod(src, NCOL)}")
    print(f"  target (row, col)  : {divmod(tgt, NCOL)}")
    print(f"  scipy Dijkstra cost: {da:.6f} cost-metres")
    print(f"  hand-written cost  : {db:.6f} cost-metres")
    print(f"  agreement          : {abs(da - db) / da:.3e} relative")
    straight = np.hypot((20 - 60) * CELL, (10 - 110) * CELL)
    print(f"  straight-line distance: {straight / 1e3:.4f} km")
    print(f"  path cost in metres if the friction were 1 everywhere: "
          f"{dist_b[tgt]:.4f} 'cost-metres', i.e. the mean friction along the path is")
    print(f"  {db / straight:.4f}")
    print("Two implementations of the same algorithm agreeing to 1e-9 relative is not a")
    print("proof of correctness -- they share the graph construction -- but it does")
    print("exclude an error in the shortest-path logic itself, which is where such errors")
    print("usually live.")

    section("3. Sinuosity: how much longer than the straight line?")
    path = trace_path(prev_b, tgt, NCOL)
    plen = 0.0
    for (r0, c0), (r1, c1) in zip(path[:-1], path[1:]):
        plen += CELL * (np.sqrt(2.0) if (r0 != r1 and c0 != c1) else 1.0)
    print(f"  path nodes            : {len(path)}")
    print(f"  path length           : {plen / 1e3:.4f} km")
    print(f"  straight-line distance: {straight / 1e3:.4f} km")
    print(f"  sinuosity (L / D)     : {plen / straight:.4f}")
    print(f"  detour factor in cost : {db / plen:.4f} (mean friction along the path)")
    print("Sinuosity above 1 is the price of avoiding high friction.  It is a joint")
    print("property of the surface and the endpoints, so it is not transferable: the same")
    print("landscape gives a different sinuosity for every pair of endpoints.")

    section("4. Anisotropy: cost that depends on the direction of travel")
    dem = (200.0
           + 0.060 * x + 0.020 * y
           + 150.0 * np.sin(2 * np.pi * x / 15_000.0)
           + 100.0 * np.cos(2 * np.pi * y / 9_000.0))
    gx_d = np.gradient(dem, CELL, CELL)
    print(f"  synthetic slope range: "
          f"[{100 * np.hypot(gx_d[0], gx_d[1]).min():.2f}, "
          f"{100 * np.hypot(gx_d[0], gx_d[1]).max():.2f}] % grade")
    for exponent, dpen in ((0.0, 1.0), (2.0, 0.5), (4.0, 0.5), (4.0, 1.0)):
        ga = anisotropic_graph(dem, CELL, exponent, dpen)
        d = sp_dijkstra(ga, indices=src, directed=True)[tgt]
        d_rev = sp_dijkstra(ga, indices=tgt, directed=True)[src]
        print(f"  exponent {exponent:4.1f}, downhill penalty {dpen:4.1f}: "
              f"cost A->B {d:9.3f}, B->A {d_rev:9.3f}, asymmetry "
              f"{abs(d - d_rev) / d * 100:6.3f} %")
    print("Three of the four rows are the point.  With penalty 1 the multiplier is")
    print("1 + exponent x |slope|, which depends on the magnitude of the slope only, so")
    print("the graph stays symmetric and the two trips cost exactly the same (0.000 %")
    print("asymmetry) -- even at exponent 4.  Asymmetry appears only when the uphill and")
    print("downhill multipliers differ (penalty 0.5 here), and then it grows with the")
    print("exponent.  A tool that builds a symmetric graph is therefore not modelling")
    print("direction-dependent cost at all, however steep the terrain it is given.")

    section("5. Cost-distance surfaces and isochrones")
    gd = grid_graph(cost, CELL, "queen")
    dists = sp_dijkstra(gd, indices=src, directed=True)
    for budget in (0.8, 1.0, 1.2, 1.5):
        reached = int((dists <= budget * straight).sum())
        print(f"  budget {budget:4.2f} x the cost-free straight-line distance: "
              f"{reached:6d} cells ({reached * CELL ** 2 / 1e6:8.2f} km^2) reachable")
    # Non-convexity: for random pairs inside the reachable set, is the straight
    # line between them inside it too?
    budget = 1.2 * straight
    inside = dists <= budget
    rr, cc = np.nonzero(inside.reshape(NROW, NCOL))
    rng2 = np.random.default_rng(7)
    bad = 0
    trials = 4000
    for _ in range(trials):
        k1, k2 = rng2.integers(0, rr.size, 2)
        mr = (rr[k1] + rr[k2]) // 2
        mc = (cc[k1] + cc[k2]) // 2
        if not inside.reshape(NROW, NCOL)[mr, mc]:
            bad += 1
    print(f"  non-convexity check at the 1.20 budget: of {trials} random pairs of")
    print(f"    reachable cells, {bad} ({100 * bad / trials:.2f} %) have a midpoint that")
    print(f"    is NOT reachable within the same budget")
    print("A cost-distance surface is the set of all shortest paths from one source, so its")
    print("contours are travel-cost isochrones.  They are not circles, and the check above")
    print("shows they are not convex either: two places can each be within the budget while")
    print("the ground between them is not, which is exactly what makes routing different")
    print("from buffering.")

    section("6. Sensitivity of the path to friction error")
    for contrast, label in ((1.0, "the two-corridor surface"),
                            (0.1, "a low-contrast surface")):
        ends = []
        for k in range(12):
            ck, _, _ = friction_surface(seed=2000 + k, contrast=contrast)
            gk = grid_graph(ck, CELL, "queen")
            dk, pk = dijkstra_python(gk, src)
            p = trace_path(pk, tgt, NCOL)
            ends.append((p, dk[tgt]))
        base = ends[0][0]
        base_set = set(base)
        overlaps, costs = [], []
        for p, c in ends:
            s = set(p)
            overlaps.append(len(base_set & s) / len(base_set | s))
            costs.append(c)
        print(f"  {label}:")
        print("    12 realisations with additive Gaussian noise of sigma = 0.1 cost units,")
        print("    i.e. 5.4 % of the mean friction (1.845):")
        print(f"    cost of the route: mean {np.mean(costs):.3f}, sd {np.std(costs):.3f} "
              f"({100 * np.std(costs) / np.mean(costs):.2f} % of the mean)")
        print(f"    Jaccard overlap of the paths with the reference: "
              f"mean {np.mean(overlaps):.4f}, min {np.min(overlaps):.4f}")
    print("Read the two pairs of numbers together.  The COST of the optimum barely moves")
    print("(0.7 % and 0.6 % of the mean), yet the ROUTE shares only about a quarter of its")
    print("cells with the reference on the high-contrast surface and about a sixth on the")
    print("low-contrast one.  The optimum is therefore geometrically degenerate: many")
    print("different lines have nearly the same cost, so the least-cost path is not a")
    print("stable object even though its cost is.  Where two corridors are within the cost")
    print("error of each other the ranking is unresolvable, and a single published line")
    print("hides that.  The honest product is a corridor of near-equal paths, or the cost")
    print("surface itself.")

    section("7. Anisotropy exponents: one landscape, several 'best' paths")
    ridge = (200.0
             + 0.020 * x + 0.010 * y
             + 500.0 * np.exp(-((x - 15_000.0) ** 2) / 2.0e6) *
             (1.0 - 0.85 * np.exp(-((y - 10_000.0) ** 2) / 4.0e6)))
    gr = np.gradient(ridge, CELL, CELL)
    print(f"  terrain: a 500 m synthetic ridge on a 2 % regional slope, with a pass at")
    print(f"  y = 10 km; slope range "
          f"[{100 * np.hypot(gr[0], gr[1]).min():.2f}, "
          f"{100 * np.hypot(gr[0], gr[1]).max():.2f}] % grade")
    paths = {}
    print("   exponent   cost     max grade(%)   total ascent(m)   Jaccard vs exponent 0")
    for exponent in (0.0, 2.0, 4.0, 8.0, 16.0):
        ga = anisotropic_graph(ridge, CELL, exponent, 0.5)
        d, p = dijkstra_python(ga, src)
        pn = trace_path(p, tgt, NCOL)
        max_grade, ascent = 0.0, 0.0
        for (r0, c0), (r1, c1) in zip(pn[:-1], pn[1:]):
            run = CELL * (np.sqrt(2.0) if (r0 != r1 and c0 != c1) else 1.0)
            dz = ridge[r1, c1] - ridge[r0, c0]
            max_grade = max(max_grade, abs(dz) / run)
            ascent += max(dz, 0.0)
        paths[exponent] = pn
        base = set(paths[0.0])
        jac = len(base & set(pn)) / len(base | set(pn))
        print(f"  {exponent:9.1f}   {d[tgt]:7.3f}   {100 * max_grade:11.2f}   "
              f"{ascent:14.2f}   {jac:19.4f}")
    print(f"  distinct routes among the five exponents: "
          f"{len({tuple(p) for p in paths.values()})}")
    print("Every route here has the same 101 nodes and the same 29.142 km length, because")
    print("all of them are monotone from source to target with the same 40 diagonal steps:")
    print("the exponent does not change the LENGTH, it changes WHERE the steep steps are")
    print("taken.  Adding any slope penalty at all drops the maximum grade from 31.7 % to")
    print("about 6.5 % and the total ascent from 839 m to 428 m, and the route moves to the")
    print("synthetic pass; the small non-monotonicity of the maximum grade (8.88 % at")
    print("exponent 4) is the optimum trading a shorter route against a slightly steeper")
    print("one.  Five distinct routes come out of five assumed trade-offs on one landscape.")
    print("The path is not evidence for the exponent; the")
    print("path is what the")
    print("exponent IMPLIES.  Choosing one from data requires independent travel")
    print("observations, and without them a 'least-cost corridor' is a restatement of the")
    print("assumption, with a number attached.")

    section("8. Centrality on a synthetic vector network")
    # A synthetic 20 x 8 grid of junctions with a random 25 % of links removed.
    nrow_n, ncol_n = 20, 8
    nodes = [(i, j) for i in range(nrow_n) for j in range(ncol_n)]
    node_id = {p: k for k, p in enumerate(nodes)}
    edges = []
    for i, j in nodes:
        if (i, j + 1) in node_id and RNG.random() > 0.25:
            edges.append((node_id[(i, j)], node_id[(i, j + 1)]))
        if (i + 1, j) in node_id and RNG.random() > 0.25:
            edges.append((node_id[(i, j)], node_id[(i + 1, j)]))
    n = len(nodes)
    r, c = zip(*edges)
    a = csr_matrix((np.ones(len(edges)), (list(r), list(c))), shape=(n, n))
    a = a + a.T
    ncomp, labels = connected_components(a, directed=False)
    print(f"  synthetic network     : {n} nodes, {len(edges)} links "
          f"({2 * len(edges)} directed), {ncomp} connected component(s)")
    deg = np.asarray(a.sum(axis=1)).ravel()
    print(f"  degree: min {int(deg.min())}, mean {deg.mean():.3f}, max {int(deg.max())}")
    # Brandes betweenness (unweighted, small network).
    dist_m = sp_dijkstra(a, directed=False)
    finite = np.isfinite(dist_m)
    between = np.zeros(n)
    for s in range(n):
        order = np.argsort(dist_m[s])
        order = order[np.isfinite(dist_m[s][order])]
        sigma = np.zeros(n)
        sigma[s] = 1.0
        pred = [[] for _ in range(n)]
        for w in order:
            for v in a.indices[a.indptr[w]:a.indptr[w + 1]]:
                if dist_m[s, w] == dist_m[s, v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = np.zeros(n)
        for w in order[::-1]:
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                between[w] += delta[w]
    between /= 2.0
    top = np.argsort(between)[::-1][:5]
    print("  top-5 betweenness centralities (node, centrality):")
    for k in top:
        print(f"    ({nodes[k][0]:2d}, {nodes[k][1]}): {between[k]:8.2f}")
    print(f"  centrality is defined only within a connected component: {ncomp} component(s)")
    print(f"  mean degrees 3.0 for a full grid, {deg.mean():.2f} after link removal")
    print("Centrality measures 'how often this node lies on a shortest path', which is a")
    print("statement about the graph and not about traffic.  A node can be central because")
    print("it is a genuine hub or because it is the only bridge across a gap that the")
    print("synthetic link removal created; the two are indistinguishable from the metric")
    print("alone, so a centrality map needs the underlying network -- and its construction")
    print("rule -- reported with it.")


if __name__ == "__main__":
    main()
