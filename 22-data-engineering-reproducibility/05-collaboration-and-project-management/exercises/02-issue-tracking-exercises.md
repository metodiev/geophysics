# Exercises — 22-05-02 Issue Tracking, Milestones and Kanban for Research

Attempt these before reading the
[solutions](./02-issue-tracking-solutions.md). The lesson is
[02 Issue Tracking, Milestones and Kanban for Research](../02-issue-tracking.md). All
numbers refer to the **SYNTHETIC** model of `code/issue_tracking_demo.py`: 6 arrivals
per week, capacity 12 per week, median work 9 days, lognormal shape $\sigma = 1.1$.

## ★ Foundational

**★1.** Write Little's law and define each term for a research queue.

**★2.** With arrivals of 6 per week: (a) compute the throughput in issues per working
day; (b) compute the lead time implied by WIP of 2 and of 24; (c) explain in one
sentence what the difference means for a user of the queue.

**★3.** State the median, 90th percentile, mean and maximum work time in the
demonstration's model, and explain why the mean exceeds the median.

## ★★ Applied

**★★4.** A team's tracker receives 10 issues per week with a capacity of 15 per week.

(a) Compute the throughput per working day. (b) Compute the queueing wait for WIP of 3
and 15. (c) If the median work time is 12 days, compute the median and 90th percentile
lead times for both WIP levels using a lognormal scaling of the demonstration's shape
($p_{90}/p_{50} = 36.4/8.9$).

**★★5.** A university group's arrivals rise from 8 to 20 issues per week, and its
capacity is 12.

(a) Compute the backlog growth per week and per year. (b) State the three available
responses and one concrete action for each. (c) State what a WIP limit of 4 achieves
here.

**★★6.** A group's tracker has only an "open/closed" state and a free-text comment
field.

(a) State the three measurements the group cannot make. (b) State the two field
changes that would make them possible. (c) State the report you would produce weekly
from the improved fields, in three lines.

## ★★★ Research-oriented

**★★★7.** Design a supervision and reporting system for a group of eight (four
students, two postdocs, two staff), stating the tracker's states and fields, the WIP
policy, the weekly review agenda, the milestone arithmetic, and the reports produced
for the group and for funders. State the one metric you would deliberately *not*
publish and why.

**★★★8.** Design a measurement of a real research queue's cycle time: state the data
(transitions with timestamps), the statistic (percentiles, by issue type), the
confounder (issues that are re-opened, or split, or never intended to finish), and how
you would handle each. State what the measurement cannot tell you about the research's
quality.

**★★★9.** The lesson's model treats arrivals as a constant rate. A grant deadline or a
field campaign produces a burst. Model a burst (say 30 issues in one week against a
capacity of 12) and compute the recovery time after it, stating the assumption about
service that makes recovery possible. State what the burst reveals about the WIP limit
policy.
