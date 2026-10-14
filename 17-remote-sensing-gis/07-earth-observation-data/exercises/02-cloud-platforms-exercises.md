# Exercises — 17-07-02 Cloud Platforms: GEE, Copernicus, NASA Earthdata

Attempt these before reading the
[solutions](./02-cloud-platforms-solutions.md). The lesson is
[02 Cloud Platforms](../02-cloud-platforms.md). All models and values are
**SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** Define a *reducer* and give one reducer used in the lesson. State one
respect in which reducing at source differs from downloading and reducing
locally.

**★2.** A region is composited as $0.2801$ (version A) and $0.2901$ (version B).
Compute the shift and express it as a percentage of version A.

**★3.** A pixel has $60$ observations, cloud cover $25\%$, and a cloud mask that
detects $80\%$ of true clouds. Compute the flagged cloud-free count, the actually
clear count, and the over-count.

## ★★ Applied

**★★4.** A reduction needs the mean of a $5000\times5000$ pixel region for
$100$ observations, $4$ bands, $2$ bytes per value. Compute the full-stack volume,
the one-value-per-pixel summary volume, and the ratio.

**★★5.** Compositing gives unmasked bias $+0.0397$ with RMS $0.0743$, and masked
bias $+0.0211$ with RMS $0.0600$. Compute the percentage reduction in bias and in
RMS. State whether the mask is a small or a large improvement, quoting both
numbers.

**★★6.** Why does a temporal *median* tolerate a minority of bright clouds but
fail when cloud cover exceeds $50\%$? Answer in two sentences, using the words
*order statistic* and *fraction*.

## ★★★ Research-oriented

**★★★7.** Design a study to decide, for a fixed task, whether to download or to
reduce at source. State the task, the quantity you would compute for each option,
the break-even condition, and the confounds (quota, latency, ability to vary the
mask) you would include. A specification that could not be executed is a failed
answer.

**★★★8.** A platform evaluates a mean over a chunked, distributed array. Explain
why the returned mean may not be bit-identical to a mean computed over the whole
array locally, and state how a reproducible study should handle this.
