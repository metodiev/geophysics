# Exercises — 17-07-03 Data Discovery, Access and Licensing

Attempt these before reading the
[solutions](./03-data-discovery-solutions.md). The lesson is
[03 Data Discovery, Access and Licensing](../03-data-discovery.md). All models
and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** A query returns $\mathrm{TP} = 13$, $\mathrm{FP} = 4$,
$\mathrm{FN} = 3$. Compute precision, recall and $F_1$.

**★2.** Write the boolean overlap predicate for two axis-aligned boxes
$\mathbf{a}$ and $\mathbf{b}$, and state what each of the four conditions means.

**★3.** For the region of interest $(40, 40, 60, 60)$ (in $\mathrm{km}$), decide
whether each reported box intersects it: (i) $(55, 58, 70, 72)$;
(ii) $(70, 70, 80, 80)$.

## ★★ Applied

**★★4.** A query returns $50$ records; the true relevant set has $40$; the
overlap is $32$. Compute precision, recall and $F_1$.

**★★5.** In the lesson's metadata-error sweep, precision and recall both fall as
$\sigma$ grows from $0$ to $16\ \mathrm{km}$. Explain in three sentences why
increasing *position error* degrades both at once, whereas adding a stricter
query filter typically trades one against the other.

**★★6.** In the licence table, $14$ records are free to view but only $10$ are
free to redistribute. State how many are lost for a mosaic-publishing project,
and name the permission the project must filter on.

## ★★★ Research-oriented

**★★★7.** Design a metadata-completeness audit for a catalogue. State the fields
you would check, the metric for each (a rate, not a count), the threshold you
would set, and the decision the audit informs. A specification that could not be
executed is a failed answer.

**★★★8.** The lesson notes that *systematic* metadata error is worse than random
error. Explain the mechanism, and describe an experiment on the synthetic
catalogue (add a constant $+3\ \mathrm{km}$ shift to every reported centre) that
would demonstrate the difference in precision/recall.
