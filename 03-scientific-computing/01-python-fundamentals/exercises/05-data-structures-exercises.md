# Exercises — 03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity

Attempt these **closed-book** before opening the
[solutions](./05-data-structures-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/data_structures_demo.py`](../code/data_structures_demo.py) require you
to run it and report its **actual** output.

---

## ★ Foundational

**★1.** For each task, name the container you would use and the complexity of the
operation.

(a) Look up a station's elevation by its station code, one million times.
(b) Store the stations of one profile in acquisition order.
(c) Test whether a candidate station code already exists in a survey.
(d) Count how many events fall in each 0.1-magnitude bin.
(e) Hold `(network, station, channel, start_time)` as a key in a dictionary.

---

**★2.** State the complexity in $n$ (and in $n$ and $m$ where relevant) of each,
and say which one you would fix first for a 10⁵-element input.

```python
# (a)
for station in stations:
    if station in station_list:
        pass          # body omitted: the question is about the membership test

# (b)
for i in range(len(stations)):
    for j in range(i + 1, len(stations)):
        if stations[i].code == stations[j].code:
            pass      # body omitted: the question is about the double loop

# (c)
total = 0.0
for row in rows:
    total += row.magnitude
```

---

**★3.** Explain, in one sentence each, why:

(a) a `list` cannot be a dictionary key but a `tuple` can;
(b) `sorted()` is usually never the bottleneck while `sorted()` inside a loop
usually is;
(c) a `set` is described as "a dictionary without values".

---

## ★★ Applied

**★★4.** Run `python3 data_structures_demo.py` and report:

(a) the two lookup timings, the per-lookup costs and the speed-up;
(b) the three membership timings and the list/set ratio;
(c) the two duplicate-detection timings, the comparison count and the speed-up;
(d) the four container sizes in bytes per element.

Then state which of the four measurements is *least* representative of the
underlying complexity and why.

---

**★★5.** A pipeline must exclude 500 "bad" station codes from a stream of 300 000
records.

(a) Write the naive version with `if code not in bad_list` and state its
complexity.
(b) Rewrite it with a set and state the new complexity.
(c) Compute the number of comparisons avoided, and estimate the wall-clock saving
using the demo's measured cost per comparison.
(d) State what would change if the stream had only 20 records.

---

**★★6.** For each scenario name the container and justify it in one sentence:

(a) 10⁵ station codes to be checked for presence, no ordering needed;
(b) a 4-element record of `(code, lat, lon, elev)` iterated 10⁷ times;
(c) a record whose fields need latitude validation on construction;
(d) a magnitude histogram with 60 bins;
(e) a stack of pending files to process depth-first (LIFO).

---

## ★★★ Research-oriented

**★★★7.** Scale a measurement.

The demo measures a list scan at 12.35 µs per lookup for a 2 000-station list with
20 000 lookups, and a dictionary lookup at 0.02 µs.

(a) Derive the *per-comparison* cost from the list measurement, stating the
assumption about how many comparisons an average lookup performs.
(b) Predict the wall-clock time for 10⁵ lookups into a 10⁵-entry list, and for the
equivalent dictionary.
(c) State the ratio and compare it with the demo's 512× at $n = 2\,000$.
(d) Set up and run the experiment at $n = 20\,000$ with 20 000 lookups and report
whether the ratio grew as predicted. If it did not, give two reasons.

---

**★★★8.** A quadratic routine versus its linear replacement.

The demo's nested-loop duplicate count costs 65.005 ms for $n = 3\,000$, doing
4 498 500 comparisons, and the `Counter` version costs 0.321 ms.

(a) Compute the comparisons per second.
(b) Predict the wall clock at $n = 10^{5}$ and at $n = 10^{6}$ for the nested loop.
(c) Predict the same for the `Counter` version, stating the assumption.
(d) At what $n$ does the nested loop exceed one hour? One day?
(e) State the single sentence you would write in the code comment explaining why
the `Counter` version was chosen.

---

**★★★9.** Find the crossover.

A dictionary costs about 31 ns per entry to build (measured with `dict(zip(...))`
on this machine) and a list scan costs about 12 ns per comparison.

(a) Write the total cost of $k$ lookups by each method as a function of $n$ and $k$,
stating the assumption about the average number of comparisons per scan.
(b) Solve for the number of lookups $k$ at which the dictionary becomes faster,
for $n = 2\,000$.
(c) Measure it: time $k = 1, 2, 5$ lookups by both methods with the dictionary
rebuilt inside the timed region, and report the measured crossover.
(d) Explain why the answer does not depend on $n$ (to first order) and why that is
the practical rule "build the index if you will look anything up more than once".
