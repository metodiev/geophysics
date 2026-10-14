# Exercises — 11-02-07 Multi-Method Targeting and Prospectivity Analysis

Attempt these before reading the
[solutions](./07-multi-method-targeting-solutions.md). The lesson is
[07 Multi-Method Targeting](../07-multi-method-targeting.md). All layers, truths,
noise levels and budgets are **SYNTHETIC** teaching constructions.

Useful: $w^{+} = \ln\frac{\mathbb{P}(B|D)}{\mathbb{P}(B|\bar D)}$,
$w^{-} = \ln\frac{\mathbb{P}(\bar B|D)}{\mathbb{P}(\bar B|\bar D)}$,
the posterior log-odds is the prior log-odds plus the sum of the layer
contributions, and
$\mathrm{AUC} = \sum_{i,j}p_i(1-p_j)\mathbf{1}[s_i>s_j]/(\sum p_i)(\sum(1-p_j))$.

## ★ Foundational

**★1.** A layer's favourable class covers $30\%$ of a $5000$-cell grid. Of $30$
training deposits, $15$ fall inside it. Compute $w^{+}$, $w^{-}$ and the contrast.

**★2.** For the same layer, compute the WofE posterior probability in the
favourable and unfavourable classes using the training density as the prior, and
verify both against the empirical rates from the contingency table.

**★3.** A second layer covers $15\%$ of the grid and contains $12$ of the $30$
deposits. Compute its $w^{+}$, $w^{-}$ and contrast, and state which layer is
stronger.

**★4.** On a $4$-cell map with intensities $p = (0.9, 0.4, 0.2, 0.1)$ and scores
$s = (4, 3, 1, 2)$, compute the weighted AUC by the rank formula, and verify it by
enumerating the pairs by hand.

## ★★ Applied

**★★5.** From ★1–★3, compute the expected number of training deposits that would
fall in *both* favourable classes if the layers were conditionally independent,
for the observed coincidence values of (a) the independent expectation,
(b) that value plus $40\%$, and (c) that value minus $40\%$. For each, state the
direction of the error introduced by summing log odds in the both-favourable class.

**★★6.** Take the mastery-checkpoint numbers of the lesson: two layers at $20\%$
coverage each, $40$ deposits, $18$ in layer 1, $16$ in layer 2, $9$ in both, with
$6\%$ of cells favourable in both. Compute the summed-log-odds posterior for the
both-favourable class and the empirical rate from the joint table, and state the
ratio. Then compute the same ratio for the layer-1-only class and state why the
error vanishes there.

**★★7.** A prospectivity map is a ranking of $10\,000$ cells with a base rate of
$0.005$. Two maps have the same AUC of $0.80$. Map A is monotone in the true
intensity; map B is monotone in a field that is $60\%$ correlated with the
intensity and $40\%$ random. Explain, using capture-curve arithmetic, why identical
AUCs can give capture counts differing by tens of per cent at a $50$-site budget,
and compute a numerical example with a two-component mixture.

**★★8.** Using the lesson's null result (mean AUC $0.5126$, sd $0.0768$ for an
irrelevant smooth layer), compute how many independent realisations would be needed
to distinguish a layer with a true AUC of $0.60$ from the null at $3\sigma$, and
state whether the lesson's $30$-realisation experiment could do it.

## ★★★ Research-oriented

**★★★9.** Prove, and then quantify, the duplicate-layer test: show that summing
log odds for a duplicated layer squares its likelihood ratio, and compute the
resulting posterior for a layer with $w^{+} = 1.0$, $w^{-} = -1.0$ and a prior of
$0.01$. State what the correct posterior is, and how the discrepancy could be
detected in a study that has no known truth.

**★★★10.** Design a validation protocol for a real prospectivity study that has no
known truth. Specify the spatial cross-validation scheme, the temporal audit, the
null simulation, the effective-sample-size reporting and the capture-curve
reporting. State, for each element, the specific failure it detects and the
failure it does *not* detect.

**★★★11.** Extend the demonstration's problem to three correlated layers, two of
which share the trend and one of which does not. Predict, before computing, the
direction of the change in (a) the AUC, (b) the calibration ratio across the trend,
and (c) the capture at a $10$-site budget; then describe the numerical experiment
that would test your prediction and the diagnostic that would reveal which layers
are responsible.
