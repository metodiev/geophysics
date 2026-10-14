# Exercises — 21-04-08 Clustering and Unsupervised Structure Discovery

Attempt these before reading the
[solutions](./08-clustering-solutions.md). The lesson is
[08 Clustering](../08-clustering.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the $k$-means objective and state the two steps of the alternation
that minimises it.

**★2.** $k$-means gives $W = 1605.12, 450.04, 385.76, 329.71$ and silhouettes
$0.5527, 0.6841, 0.5684, 0.4586$ for $k = 2,3,4,5$. State which criterion selects
$k$ and which value it selects.

**★3.** On interleaving crescents, $k$-means places $74.40\ \%$ of the first
crescent in one cluster while density-based clustering places $100.00\ \%$ and
labels four points as noise. State the property of each method that explains the
difference.

## ★★ Applied

**★★4.** Compute the silhouette of a two-point, two-cluster partition in which
each point is its own cluster, and state what the value is and why.

**★★5.** The last eight single-linkage merge heights are
$0.362, 0.381, 0.481, 0.506, 0.518, 0.556, 2.354, 2.677$. Compute the ratio of the
last height to the eighth-from-last and state what the jump indicates.

**★★6.** State what an internal score such as the silhouette measures and what it
does not, and give the external criterion you would require for a facies
clustering.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures the **adjusted Rand index** of
$k$-means, a Gaussian mixture and DBSCAN against a known generative model, as a
function of cluster elongation and inter-cluster overlap. State the design, the
metric, the replicate count and the predicted ordering. A specification that could
not be executed is a failed answer.

**★★★8.** Design a study of the **stability of a clustering** under resampling,
stating the metric (for example the mean pairwise adjusted Rand index between
bootstrap partitions), the number of resamples, and the criterion for declaring a
cluster robust.
