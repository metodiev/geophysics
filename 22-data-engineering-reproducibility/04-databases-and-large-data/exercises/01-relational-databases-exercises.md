# Exercises — 22-04-01 Relational Databases and SQL for Earth Data

Attempt these before reading the
[solutions](./01-relational-databases-solutions.md). The lesson is
[01 Relational Databases and SQL for Earth Data](../01-relational-databases.md). All
numbers refer to the **SYNTHETIC** model of `code/relational_databases_demo.py`:
5 000 000 rows of 120 B, 8 KiB pages, 0.02 ms sequential and 0.6 ms random page reads,
B-tree fan-out 200, scan throughput 400 MB/s.

## ★ Foundational

**★1.** Write the formulas for rows per page, page count and scan time, and compute
each for the demonstration's table.

**★2.** Compute the B-tree depth for $f = 200$ and $R = 5 \times 10^{6}$, state the
pages touched by a point lookup, and compute the lookup cost and the index size.

**★3.** State the two halves of a database design that this lesson separates, and give
one example of each from §6.

## ★★ Applied

**★★4.** A query returns 250 000 rows from the demonstration's 5-million-row table.

(a) Compute the index-scan cost from the leaf-page count and the tree traversal, and
compare with the scan. (b) State which plan you expect and why. (c) State what changes
if the rows are physically clustered by the index key.

**★★5.** A table has 20 million rows of 200 B in 8 KiB pages, with a sequential page
cost of 0.02 ms and a random page cost of 0.6 ms.

(a) Compute the rows per page, page count and scan time. (b) Compute the index cost for
a 2 000-row and a 500 000-row query, and state which plan wins in each case.
(c) State your estimated crossover row count.

**★★6.** A nightly load makes every query ten times slower without any change to the
SQL, and a query that once used an index now scans.

(a) State the two most likely causes. (b) State the first diagnostic you would run and
what you would look for. (c) State the schema or policy change that prevents the
recurrence.

## ★★★ Research-oriented

**★★★7.** Design the schema and indexing for an earthquake catalogue of 200 million
events that must support (i) events in a time window, (ii) events within a radius of a
point, (iii) the largest events per year, and (iv) a join to a 10 000-row station table.
State the types, keys, constraints, indices and partitioning, and the one query your
design makes expensive. State what you would measure to check the claim.

**★★★8.** The cost model has no buffer pool. Design a measurement of the *effective*
random-page latency for a workload, state the statistic, the confounder (cache
warmth), and how you would report a crossover that a reader could check. State what the
measurement cannot tell you about a query you have not run.

**★★★9.** A colleague proposes denormalising the catalogue (storing station metadata in
every event row) to remove the join. Evaluate the proposal against §5 and §6: state the
performance case, three correctness costs, and the measurement that would decide
whether the denormalisation is worth it.
