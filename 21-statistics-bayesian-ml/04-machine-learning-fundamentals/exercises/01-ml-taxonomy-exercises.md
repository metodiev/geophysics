# Exercises — 21-04-01 ML Taxonomy: Supervised, Unsupervised, Reinforcement

Attempt these before reading the [solutions](./01-ml-taxonomy-solutions.md). The
lesson is [01 ML Taxonomy](../01-ml-taxonomy.md). All data are **SYNTHETIC**;
numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** Classify each task as supervised regression, supervised classification,
unsupervised or reinforcement learning, and state what plays the role of the
label or reward: (a) predicting porosity from a density log; (b) grouping seismic
traces by waveform without lithology labels; (c) deciding where to drill next to
maximise expected information; (d) predicting whether a station will detect an
event.

**★2.** A regression with noise standard deviation $\sigma = 0.3$ is fitted, and
the training MSE is $0.0859$. Compute the irreducible MSE if the model recovered
the truth exactly, and state what the difference between the two numbers means.

**★3.** A $k$-means run gives within-cluster sums of squares $1230.23$, $303.25$,
$260.47$ and $223.85$ for $k = 2,3,4,5$. Compute the successive reductions as
percentages and state which one suggests the elbow.

## ★★ Applied

**★★4.** Write the empirical risk minimisation objective and identify
$\mathcal F$, $\ell$ and $\Omega$ for (a) ridge regression and (b) logistic
regression with an $L_2$ penalty.

**★★5.** The $\epsilon$-greedy bandit earned $1269$ of a possible $1300$ over
$2000$ pulls with arm means $(0.20, 0.50, 0.65, 0.40)$. Compute the regret in
reward units and as a percentage, and state the regret you would expect from a
policy that always pulled the best arm.

**★★6.** The logistic fit recovered coefficients $+0.9111$ and $-0.8054$ against
a truth of $+1.2$ and $-0.8$. Compute the ratio of each estimate to its truth and
explain why neither is biased towards zero by the same factor.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that measures the **regret of three bandit
policies** — $\epsilon$-greedy, upper-confidence-bound and Thompson sampling — on
the demonstration's bandit, as a function of the pulls. State the policies with
their parameters, the replicate count, the metric and the predicted ordering. A
specification that could not be executed is a failed answer.

**★★★8.** Design an experiment that tests whether an **unsupervised** facies
clustering recovers a known generative structure: state the data-generating
process, the clustering algorithm, the external metric, the replicate count, and
the condition under which the clustering would fail despite a good objective
value.
