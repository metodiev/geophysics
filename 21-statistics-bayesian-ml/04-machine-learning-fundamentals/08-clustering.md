---
id: 21-04-08
title: "Clustering and Unsupervised Structure Discovery"
level: graduate
prereqs: ["21-04-01", "21-04-07"]
estimated_minutes: 60
tags: [machine-learning, clustering, k-means, dbscan, hierarchical-clustering, silhouette]
---

# Clustering and Unsupervised Structure Discovery

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the $k$-means objective and **state** the shape of cluster it
   prefers.
2. **Compute** a silhouette score and **use** it to choose the number of
   clusters.
3. **Contrast** centroid, density-based and hierarchical clustering on the same
   data and **state** why they disagree.
4. **Diagnose** the failures: non-convex clusters, unequal sizes, noise points and
   the absence of any cluster structure at all.
5. **Validate** a clustering against an external label or a generative model, and
   **state** what an internal score does and does not measure.
6. **Report** a clustering with the algorithm, parameters and validation.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) —
  the paradigm and why its objective cannot validate itself.
- [21-04-07 PCA, ICA and Manifold Learning](07-dimensionality-reduction.md) —
  the continuous counterpart of a cluster label.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  the density view of where clusters live.

## 1. Intuition: a cluster is a definition, not a discovery

Every clustering algorithm defines a cluster by an objective, and the objective
decides the answer. $k$-means insists that a cluster is a ball of roughly equal
size; density-based methods insist that it is a connected region of high density;
hierarchical methods insist on nothing at all until the analyst chooses a cut.
Feed the same data to all three and you get three different partitions, each
optimal for its own definition.

That is not a defect to be engineered away. It means an unsupervised result is
only as meaningful as the generative story behind it, and the deliverable is
therefore *the algorithm, its parameters and an external check* — never a bare
partition.

## 2. $k$-means

The objective is the within-cluster sum of squares,

$$W(C) = \sum_{j=1}^{k}\sum_{x \in C_j}\|x - \mu_j\|^{2},$$

minimised by alternating between assigning each point to its nearest centroid and
recomputing the centroids. The alternation guarantees a non-increasing objective
and convergence to a **local** minimum, so multiple random restarts are required.
Three properties follow from the objective and explain every failure mode:

- The clusters are **spherical** in the metric used, because distance to a
  centroid is Euclidean.
- The clusters tend to be **equal in size**, because a large cluster pays a large
  squared penalty for its spread.
- The objective **decreases monotonically with $k$**, reaching zero when every
  point is its own cluster, so $W$ cannot choose $k$.

## 3. Choosing $k$ and validating the result

The **silhouette** for point $i$ compares its mean distance to its own cluster,
$a_i$, with its mean distance to the nearest other cluster, $b_i$:

$$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}, \qquad s_i \in [-1, 1],$$

and the score of a partition is the mean of the $s_i$. It rewards tight, well
separated clusters and, unlike $W$, has no monotone bias in $k$. It is still an
**internal** criterion: it measures the geometry of the partition, not whether the
partition corresponds to anything real.

External validation requires either labels or a generative model. Given labels, the
**adjusted Rand index** measures agreement beyond chance; given a known generator,
the accuracy with which each cluster recovers a true component is the natural
metric. Without either, the honest report states the algorithm, the parameters,
the internal score and the caveat.

## 4. Density-based and hierarchical methods

**Density-based clustering** (DBSCAN and its relatives) defines a cluster as a
maximal set of points connected through regions where at least `minPts` points lie
within radius `eps`. It finds arbitrarily shaped clusters, needs no $k$, and
explicitly **labels noise** — points in sparse regions are assigned to no cluster.
Its cost is two parameters that interact: a single `eps` cannot handle clusters of
very different densities, which is the standard failure.

**Hierarchical clustering** builds a tree of merges. Single linkage merges the two
clusters whose closest pair is nearest, complete linkage the farthest pair, and
Ward's method the pair that minimises the increase in within-cluster variance.
Single linkage follows chains and can merge two well-separated clusters through a
thin bridge; complete linkage and Ward prefer compact clusters. The output is a
dendrogram whose **merge heights** carry the information: a large jump between
consecutive heights marks a natural cut, and the absence of a jump is evidence
that there is no cluster structure at all.

## 5. Worked example

**$k$-means and the silhouette.** Three Gaussian clouds of $120$ points each:

| $k$ | $W$ | silhouette | cluster sizes |
|---|---|---|---|
| 2 | 1605.12 | 0.5527 | $[238, 122]$ |
| 3 | **450.04** | **0.6841** | $[120, 120, 120]$ |
| 4 | 385.76 | 0.5684 | $[120, 119, 63, 58]$ |
| 5 | 329.71 | 0.4586 | $[120, 63, 61, 58, 58]$ |

$W$ falls monotonically, as the objective requires, so it cannot select $k$. The
silhouette peaks at $k = 3$ with $0.6841$ and the recovered sizes are exactly
$[120, 120, 120]$ — the truth. The contrast between the two columns is the entire
argument for using an internal criterion that is not the objective.

**Non-convex clusters.** Two interleaving crescents of $250$ points each, plus
$20$ scattered points. $k$-means with $k = 2$ puts only $74.40\ \%$ of the first
crescent into one cluster: it splits each crescent in half, because the crescents
interlock and no pair of centroids can separate them. Density-based clustering with
`eps` $= 0.18$ and `minPts` $= 6$ finds **two** clusters, places $100.00\ \%$ of
the first crescent in one of them, and labels **four** points as noise. Same data,
different definition, different answer — and here the density definition matches
the generative story.

**Hierarchical.** Thirty points in three tight groups of ten, each of spatial
spread about $0.3$. The last eight single-linkage merge heights are
$0.362, 0.381, 0.481, 0.506, 0.518, 0.556, 2.354, 2.677$: the first twenty-seven
merges are all below $0.6$ — within-group — and the final two jump to $2.354$ and
$2.677$, an increase by a factor of more than four. The jump is the natural
three-cluster cut, and it is visible without any cluster-count criterion.

## Assumptions and regime of validity

1. **$k$-means assumes convex, similarly sized clusters**; it will split an
   elongated cluster and merge two nearby dense ones.
2. **A distance metric encodes units.** Features must be scaled, or the clustering
   is a function of the units.
3. **DBSCAN assumes a single density scale**; clusters of very different densities
   cannot both be found with one `eps`.
4. **Hierarchical linkage choice changes the answer.** Single linkage chains;
   complete linkage and Ward prefer compact groups.
5. **Internal scores measure geometry, not truth.** A high silhouette is possible
   on data with no generative clusters.
6. **Clusters are not classes.** A partition of an unlabelled sample says nothing
   about whether the groups correspond to recognisable categories.

## The honest summary

Clustering finds the structure its objective defines, and the demonstration shows
three answers to the same question. $k$-means recovered $[120, 120, 120]$ from
three Gaussian clouds with a silhouette of $0.6841$ — and split two interleaving
crescents evenly, capturing only $74.40\ \%$ of the first crescent. Density-based
clustering found both crescents completely ($100.00\ \%$ of the first) and labelled
four points as noise, which $k$-means cannot do. Single linkage revealed the
three-group structure through a merge-height jump from $0.556$ to $2.354$. The
numbers do **not** establish that any partition is the truth: the Gaussian example
had a known generator, and only there can the recovery be scored. On real
geophysical data the validation must come from geology.

## Python demonstration

[`code/clustering_demo.py`](./code/clustering_demo.py) prints every number quoted
above. It:

1. runs $k$-means for $k = 2$–$5$ with the within-cluster sum of squares and the
   silhouette;
2. runs a density-based clusterer on interleaving crescents with noise points;
3. performs single-linkage agglomeration and prints the last merge heights.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python clustering_demo.py
```

It runs in about a fifth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/08-clustering-exercises.md`](./exercises/08-clustering-exercises.md)
with worked solutions in
[`exercises/08-clustering-solutions.md`](./exercises/08-clustering-solutions.md).

## Mastery checkpoint

Without notes, $k$-means gives $W = 450.04$ and a silhouette of $0.6841$ at
$k = 3$ with cluster sizes $[120, 120, 120]$; on interleaving crescents it places
$74.40\ \%$ of the first crescent in one cluster while density-based clustering
manages $100.00\ \%$ and four noise points; and single linkage's last merge
heights are $0.556$, $2.354$, $2.677$.

1. Compute the silhouette of a partition in which every point is its own cluster,
   and state why the score alone does not prevent trivial solutions here.
2. Compute the ratio of the last merge height to the eighth-from-last and state
   what it indicates.
3. State why $k$-means splits the crescents and what property of its objective
   causes it.
4. State the external validation you would require before naming a cluster a
   facies.

## Common pitfalls

1. **Choosing $k$ by the objective.** It falls monotonically to zero.
2. **Assuming $k$-means finds any shape.** It prefers equal, convex clusters.
3. **Forgetting to scale.** The clustering then follows the units.
4. **Using one `eps` for clusters of different densities.** DBSCAN merges or
   discards them.
5. **Reading a high silhouette as truth.** It measures geometry.
6. **Naming clusters as classes without evidence.** A partition is a partition.

## Where this is used

- **Facies and electrofacies** from well logs, validated against core.
- **Seismic waveform classification**: density-based methods for arbitrary shapes.
- **Geochemical fingerprinting**: hierarchical clustering of sample similarity.
- **Seismicity clustering**: earthquake families and aftershock sequences.
- **Anomaly detection**: points labelled as noise are the deliverable.

## Related lessons

- [21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement](01-ml-taxonomy.md) —
  why an unsupervised objective cannot validate itself.
- [21-04-07 PCA, ICA and Manifold Learning](07-dimensionality-reduction.md) —
  reducing dimension before clustering.
- [21-04-06 Feature Engineering for Earth Data](06-feature-engineering.md) —
  the features that decide what a clustering can find.
- [21-06-04 Facies and Lithology Prediction from Well Logs](../06-ml-in-geophysics/04-facies-and-lithology.md) —
  clustering and classification for facies.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  the density the mode-based methods estimate.

## Self-assessment checklist

- [ ] I can write the $k$-means objective and state its cluster shape.
- [ ] I can compute a silhouette score and use it to choose $k$.
- [ ] I can contrast centroid, density and hierarchical methods.
- [ ] I can diagnose the four standard failure modes.
- [ ] I can name the external validation a clustering needs.
- [ ] I can report an algorithm, its parameters and its validation.
