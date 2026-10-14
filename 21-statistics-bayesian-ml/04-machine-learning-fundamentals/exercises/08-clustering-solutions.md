# Solutions — 21-04-08 Clustering and Unsupervised Structure Discovery

> Read after attempting. Lesson:
> [08 Clustering](../08-clustering.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — The $k$-means objective and its alternation

$$W(C) = \sum_{j=1}^{k}\sum_{x \in C_j}\|x - \mu_j\|^{2} .$$

The two steps are:

1. **Assignment.** With the centroids fixed, assign each point to the cluster whose
   centroid is nearest — this cannot increase $W$, since each point contributes its
   own squared distance and takes the minimum available.
2. **Update.** With the assignments fixed, set each centroid to the mean of its
   members — this minimises $W$ because the mean is the least-squares location.

Each step is non-increasing and $W$ is bounded below by zero, so the alternation
converges. It converges to a **local** minimum: the objective is non-convex in the
assignments, so the result depends on the initialisation, which is why multiple
restarts (the demonstration uses twenty) are standard.

---

## ★★2 — Selecting $k$

$$W = 1605.12,\ 450.04,\ 385.76,\ 329.71 \quad\text{falls monotonically},$$
$$\text{silhouette} = 0.5527,\ 0.6841,\ 0.5684,\ 0.4586 .$$

$W$ cannot select $k$ — it falls at every step and reaches zero when every point is
its own cluster. The **silhouette** peaks at $k = 3$ with $0.6841$, and it is
$0.6841/0.5527 = 1.24$ times its value at $k = 2$ and $1.20$ times its value at
$k = 4$. The recovered sizes at $k = 3$ are $[120, 120, 120]$, matching the three
generative clouds exactly.

---

## ★★3 — Why the two methods differ

**$k$-means** assigns each point to the nearest of $k$ centroids, so its clusters
are the cells of a Voronoi partition and are therefore convex and roughly spherical
in the chosen metric. Two interleaving crescents cannot be separated by two
convex cells: any pair of centroids either splits each crescent or merges them, and
the demonstration's $74.40\ \%$ is the fraction of the first crescent that happens
to fall inside one cell.

**Density-based clustering** defines a cluster as a maximal set of points
connected through dense regions, so it follows the crescent's shape regardless of
convexity. It reaches $100.00\ \%$ on the first crescent and labels `4` sparse
points as noise — an output $k$-means cannot produce at all, since every point must
belong to a cluster.

---

## ★★4 — Silhouette of a singleton partition

For a cluster containing one point, $a_i$ is undefined — there is no other point in
its own cluster with which to average a distance. The standard convention assigns
$s_i = 0$ to such points, so the mean silhouette of a partition in which every
point is its own cluster is **$0.0000$**.

This is why the silhouette does not suffer the trivial-solution problem: the
degenerate partition $k = n$ scores $0$, not $1$, while $k$-means' own objective
scores $W = 0$. The contrast is the clearest illustration that a cluster-count
criterion must not be the objective being minimised.

---

## ★★5 — The merge-height jump

$$\frac{2.677}{0.518} = 5.17, \qquad \frac{2.354}{0.556} = 4.23 .$$

Both ratios exceed four. Twenty-eight of the thirty points merge at distances below
$0.6$ — they are within-group — and the last two merges jump to $2.354$ and
$2.677$, an increase of more than **$4\times$** over the largest within-group merge.

The jump indicates a genuine three-cluster structure at the height between $0.556$
and $2.354$: cutting the dendrogram there yields exactly the three groups of ten.
The diagnostic is the **gap**, not any absolute number, and its absence — a smooth
sequence of heights with no jump — would be evidence that the data have no cluster
structure at all, which is a useful conclusion rather than a failure.

---

## ★★6 — What an internal score measures, and what it does not

**Measures.** The geometry of a partition: how tight the clusters are relative to
the distance between them (silhouette), or how much within-cluster variance the
partition accounts for. It is a property of the *data and the partition only*, and
it needs no labels.

**Does not measure.** Whether the clusters correspond to anything real. Concretely:
(i) a high silhouette is attainable on data drawn from a single continuous cloud,
because any finite sample has a locally best partition; (ii) the score is
**monotone in the number of clusters removed**, so it cannot certify the "correct"
$k$, only rank candidates; (iii) it is blind to whether the clusters are
reproducible under resampling, which is a separate and important property.

**External criterion required for a facies clustering.** Either (a) labels from a
subset: core descriptions, mud-log lithology or production tests, scored by the
adjusted Rand index against the clustering; or (b) a generative model: a stated
number of facies with stated statistics, against which the recovery is measured;
or (c) at minimum, cluster stability across resamples and wells, which is a
necessary but not sufficient condition. Naming a cluster a facies on internal
evidence alone is not supported.

---

## ★★★7 — Internal and external agreement versus shape

**Data.** Four components in two dimensions with:
elongation $\lambda_2/\lambda_1 \in \{1, 0.5, 0.25, 0.1\}$; orientation
$0^{\circ}$ to $90^{\circ}$; and centroid separation measured in units of the
component scale, $d \in \{1, 2, 3, 4\}$ standard deviations. $n = 1000$ points per
component.

**Methods.** $k$-means with $k = 4$; a Gaussian mixture with $k$ chosen by BIC;
DBSCAN with `eps` on a grid and `minPts` $= 10$.

**Metric.** The **adjusted Rand index** against the true component labels, with
the number of clusters also recorded. ARI is external and chance-corrected, so
setting a single component to itself scores near zero.

**Replicates.** $M = 500$ data sets per configuration, giving an ARI standard
error below $0.015$.

**Prediction.** At low elongation and wide separation all three methods recover the
components (ARI $> 0.95$) and the ordering is not resolvable. As elongation rises,
$k$-means degrades fastest — it cuts elongated components across their long axis —
falling below $0.7$ once the ratio is $0.1$. The Gaussian mixture degrades more
slowly, because its covariance matrix adapts to the elongation, and BIC continues
to select the correct $k$ down to moderate overlap. DBSCAN is the most sensitive to
the choice of `eps`: excellent at some settings, poor at others, and it cannot
handle the elongated low-density tails at all, but it is the only method that
reports noise when a component is spurious. The headline is therefore an ordering
that depends on the failure axis: mixtures win on shape, density methods win on
noise handling.

---

## ★★★8 — Stability of a clustering under resampling

**Design.** Resample the data $B = 200$ times: by bootstrap (sampling with
replacement) for point data, or by holding out one group or transect at a time for
grouped or spatial data. Cluster each resample with the algorithm and parameters
under test, and record the partition.

**Metric.** The mean pairwise **adjusted Rand index** between all pairs of
resampled partitions, restricted to the points present in both (for the bootstrap,
the intersection of the samples). This is the consensus, or stability, score.

**Replicates.** $B = 200$ resamples give a stability score whose standard error is
roughly $0.02$; run the whole procedure over $M = 20$ independent data sets to get
a standard error on the stability itself.

**Criterion.** A cluster is declared robust when, across at least $90\ \%$ of the
resamples, the same set of points (a Jaccard overlap above $0.75$ with the original
cluster) is recovered; and the partition as a whole is declared stable when the
mean pairwise ARI exceeds $0.75$. A clustering that survives neither test should
not be named, however attractive its silhouette.

**Why this is the right check.** Stability is a necessary condition that internal
scores cannot supply: an over-fitted partition of noise can have a good silhouette
and a terrible stability, while a real structure reproduces itself across
resamples. The study's headline is the pair (silhouette, stability) for each
candidate $k$ and algorithm, which together separate "well shaped" from
"reproducible".
