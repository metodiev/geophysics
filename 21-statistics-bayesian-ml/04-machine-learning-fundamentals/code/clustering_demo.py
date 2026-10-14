#!/usr/bin/env python3
"""Clustering on SYNTHETIC data: k-means with a silhouette score for choosing k,
a density-based method that finds non-convex clusters and noise, and single
linkage hierarchical clustering.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python clustering_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. k-means and the silhouette score.
2. Density-based clustering on two interleaving crescents.
3. Hierarchical single linkage and its merge distances.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def kmeans(pts, k, rng, restarts=20, iters=100):
    best = None
    for _ in range(restarts):
        seeds = pts[rng.choice(pts.shape[0], k, replace=False)]
        for _ in range(iters):
            d = ((pts[:, None, :] - seeds[None, :, :]) ** 2).sum(axis=2)
            lab = d.argmin(axis=1)
            new = np.array([pts[lab == j].mean(axis=0) if np.any(lab == j)
                            else seeds[j] for j in range(k)])
            if np.allclose(new, seeds):
                break
            seeds = new
        wcss = float(((pts - seeds[lab]) ** 2).sum())
        if best is None or wcss < best[0]:
            best = (wcss, lab, seeds)
    return best


def silhouette(pts, lab):
    d = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=2))
    out = []
    for i in range(pts.shape[0]):
        same = (lab == lab[i])
        same[i] = False
        if not np.any(same):
            continue
        a = d[i, same].mean()
        b = min(d[i, lab == c].mean() for c in set(lab.tolist()) if c != lab[i])
        out.append((b - a) / max(a, b))
    return float(np.mean(out))


def dbscan(pts, eps, min_pts):
    n = pts.shape[0]
    d = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=2))
    neigh = [np.where(d[i] <= eps)[0] for i in range(n)]
    lab = np.full(n, -1)
    cluster = 0
    for i in range(n):
        if lab[i] != -1 or neigh[i].size < min_pts:
            continue
        lab[i] = cluster
        stack = list(neigh[i])
        while stack:
            j = stack.pop()
            if lab[j] == -1:
                lab[j] = cluster
                if neigh[j].size >= min_pts:
                    stack.extend(neigh[j].tolist())
        cluster += 1
    return lab


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. k-means and the silhouette score")
    centres = np.array([[-3.0, 0.0], [0.0, 3.0], [3.0, -1.0]])
    pts = np.vstack([c + 0.8 * RNG.standard_normal((120, 2)) for c in centres])
    print("  k   WCSS        silhouette   cluster sizes")
    for k in (2, 3, 4, 5):
        wcss, lab, _ = kmeans(pts, k, RNG)
        sil = silhouette(pts, lab)
        sizes = sorted(np.bincount(lab).tolist(), reverse=True)
        print(f"  {k}   {wcss:9.2f}   {sil:10.4f}   {sizes}")
    print("  the WCSS always falls with k, so it cannot select k; the silhouette")
    print("  peaks at the true number of clusters, which here is three.")

    section("2. Density-based clustering on interleaving crescents")
    t = RNG.uniform(0.0, np.pi, 250)
    moon1 = np.column_stack([np.cos(t), np.sin(t)])
    moon2 = np.column_stack([1.0 - np.cos(t), 0.5 - np.sin(t)])
    moons = np.vstack([moon1, moon2]) + 0.06 * RNG.standard_normal((500, 2))
    noise_pts = RNG.uniform(-0.2, 1.2, (20, 2))
    moons = np.vstack([moons, noise_pts])
    _, km_lab, _ = kmeans(moons, 2, RNG)
    km_agreement = float(max(np.mean(km_lab[:250] == 0), np.mean(km_lab[:250] == 1)))
    db_lab = dbscan(moons, 0.18, 6)
    n_clusters = len(set(db_lab[db_lab >= 0].tolist()))
    n_noise = int(np.sum(db_lab == -1))
    if n_clusters >= 2:
        first = db_lab[:250]
        major = np.bincount(first[first >= 0]).argmax() if np.any(first >= 0) else -1
        db_agreement = float(np.mean(first == major))
    else:
        db_agreement = float("nan")
    print(f"  data: two crescents of 250 points each, plus 20 scattered points")
    print(f"  k-means with k = 2: fraction of the first crescent in one cluster "
          f"= {km_agreement:.4f}")
    print(f"  density-based clustering: clusters found = {n_clusters}, "
          f"noise points = {n_noise}")
    print(f"  fraction of the first crescent in its majority density cluster = "
          f"{db_agreement:.4f}")
    print("  k-means splits each crescent between the two centroids because its")
    print("  clusters must be spherical; the density method follows the shape")
    print("  and labels the sparse points as noise, which k-means cannot do.")

    section("3. Hierarchical single linkage")
    small = np.vstack([np.array([[-2.0, 0.0]]) + 0.3 * RNG.standard_normal((10, 2)),
                       np.array([[2.0, 0.0]]) + 0.3 * RNG.standard_normal((10, 2)),
                       np.array([[0.0, 3.0]]) + 0.3 * RNG.standard_normal((10, 2))])
    m = small.shape[0]
    d = np.sqrt(((small[:, None, :] - small[None, :, :]) ** 2).sum(axis=2))
    clusters = [{i} for i in range(m)]
    merge_distances = []
    while len(clusters) > 1:
        best = None
        for a in range(len(clusters)):
            for b in range(a + 1, len(clusters)):
                dist = min(d[i, j] for i in clusters[a] for j in clusters[b])
                if best is None or dist < best[0]:
                    best = (dist, a, b)
        dist, a, b = best
        merge_distances.append(dist)
        clusters[a] = clusters[a] | clusters[b]
        clusters.pop(b)
    print(f"  {m} points in three tight groups of ten, each of spread about 0.3")
    print("  last eight merge distances (metres between the nearest pair of")
    print("  points in the two clusters being joined):")
    print("  " + ", ".join(f"{v:.3f}" for v in merge_distances[-8:]))
    print(f"  the smallest {m - 3} merges are within-group (below about 1.0) and")
    print(f"  the last two are between groups (about "
          f"{merge_distances[-2]:.2f} and {merge_distances[-1]:.2f}), so the")
    print("  dendrogram has an unambiguous three-cluster cut. The height at")
    print("  which the distances jump is the diagnostic, not any fixed number.")


if __name__ == "__main__":
    main()
