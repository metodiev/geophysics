---
id: 00-01-04
title: "Deliberate Practice, Spaced Repetition and Problem-Solving Habits"
level: beginner
prereqs: ["00-01-01"]
estimated_minutes: 40
tags: [study-method, deliberate-practice, memory, problem-solving]
---

# Deliberate Practice, Spaced Repetition and Problem-Solving Habits

## Learning objectives

- State the four conditions that make practice *deliberate* rather than merely
  repetitive, and apply them to a geophysics task.
- Design a spaced-repetition schedule for technical material that requires
  derivation, not just definitions.
- Explain why interleaving topics improves transfer, even though it feels worse
  than blocked practice.
- Apply a short, reliable set of heuristics to a problem you cannot yet start.

## Prerequisites

[How to Learn Geophysics: A Method, Not a Reading List](./01-how-to-learn-geophysics.md)
for the read–derive–compute–explain loop, and ideally
[The Six Stages and Their Mastery Checkpoints](./02-six-stages.md) so that you
have a target checkpoint to practise towards.

## 1. Deliberate practice: four conditions

Practice is the largest single component of skill, but "hours spent" explains
surprisingly little of the variation between learners. What matters is whether
the practice satisfies four conditions:

1. **A well-defined task with a right answer you can check.** "Study seismology"
   fails this. "Derive the travel time of a head wave for a two-layer model and
   check it against a computed raypath" passes.
2. **Difficulty at the edge of current ability.** If you succeed every time, the
   task is too easy; if you fail every time and learn nothing from the failure,
   it is too hard.
3. **Immediate, informative feedback.** Feedback must tell you *which step* was
   wrong. Numerical answers with a known analytic case are excellent feedback.
4. **Repetition with refinement.** Repeat the *weak* component, not the whole
   task. If your derivations are right but your unit conversions keep failing,
   drill conversions.

A practical test: after a study session, can you name the single weakest
component you worked on, and did you get feedback on it during the session? If
not, the session was exposure rather than practice.

## 2. Spaced repetition for derivation-heavy material

Retention declines with time since last retrieval; retrieving before you have
fully forgotten produces far more durable memory than retrieving after. The
practical consequence is a schedule: **review at expanding intervals**, not in
one long block.

For technical subjects, most flashcard advice fails because it cards *definitions*
when the examinable skill is *procedure*. Cards that work here:

| Card type | Front | Back |
|---|---|---|
| Derivation trigger | "Derive the 1-D wave equation from a stretched string" | The steps, in order, with the physical assumption each step uses |
| Unit conversion | "$1\ \text{mGal}$ in $\text{m}\,\text{s}^{-2}$" | $10^{-5}$ |
| Limit behaviour | "What does the gravity field do inside a uniform spherical shell?" | Zero, by Newton's shell theorem |
| Failure condition | "When is the infinite-slab formula a poor approximation?" | When the source is small or shallow relative to the survey extent; edge effects matter |
| Discrimination | "Two anomalies: which measurement separates a sulphide body from a shear zone?" | Reasoning about conductivity, chargeability and density contrasts |

The last two are the valuable ones. They are retrieval cues for *judgements*,
which is what professional practice actually requires.

A workable schedule for a lesson you have just finished: revisit after 1 day,
3 days, 1 week, 3 weeks, then 2–3 months. Keep the intervals expanding while
recall stays reliable; if recall fails, shorten the next interval for that item.

Two honest caveats. First, the exact optimal spacing depends on the material and
the learner; treat the schedule as a starting point to be adjusted, not a law.
Second, spaced repetition is a *retention* tool. It will not, by itself, teach
you to solve problems you have never seen; that requires varied practice,
below.

## 3. Interleaving and varied practice

**Blocked practice** is doing twenty problems of the same type in a row.
**Interleaved practice** is mixing types so that you must first *decide which
method applies*.

Blocked practice feels better and produces better performance *during* practice.
Interleaved practice produces worse practice performance and better retention
and transfer. This is the classic "desirable difficulty": the extra effort of
identifying the right approach is exactly the skill that real problems demand,
because real problems do not arrive labelled.

How to interleave in this curriculum:

- Alternate a mathematics block with a domain block in the same session
  (for example, eigenproblems with normal-mode seismology).
- Within a problem set, mix items rather than working them in order.
- When a lesson presents several methods, do exercises that require choosing
  among them, not one drill per method.

**Vary the surface features too.** Practise the same underlying idea in different
disguises: a gravity problem written in cgs units, a magnetic problem written in
nanotesla, an anomaly given as a profile rather than a map. Transfer comes from
recognising the *structure*, and structure is only visible when surfaces differ.

## 4. Retrieval, not reviewing

Reading notes again is reviewing. Closing the notes and writing the derivation
is retrieving. Only the second one measurably improves long-term retention, and
learners systematically mis-predict which one helped.

Three retrieval formats, in increasing difficulty:

1. **Free recall.** Close everything; write what the lesson was about. Compare
   with the objectives. Gaps are your study list.
2. **Cued recall.** Given a heading, reproduce the content. This is what the
   exercise sections are for.
3. **Cued production.** Given a physical situation, choose a method, do the
   computation, and state the uncertainty. This is the transfer level, and it is
   what the ★★★ exercises and the projects in
   [25-projects-capstone](../../25-projects-capstone/README.md) aim at.

Do format 1 for every lesson, even if you only have ten minutes. A blank page
and a two-paragraph summary is the cheapest high-value study activity there is.

## 5. Problem-solving heuristics that work on geophysics problems

Most "stuck" moments are not a failure of knowledge but a failure to *start*.
The heuristics below are ordered; apply them in sequence.

**H1 — Say what is measured before what is modelled.** Ask: what instrument
would observe this, and what physical quantity does it record? If you cannot
answer, you are missing the physics, not the algebra.

**H2 — Estimate the answer before computing it.** Rough magnitudes first:
is the anomaly in milliGals or microGals? Is the velocity $3\ \text{km}\,\text{s}^{-1}$
or $30$? An estimate converts "I got a number" into "I got a *plausible* number".

**H3 — Check dimensions.** Write the dimensions of every term. In geophysics this
catches a large fraction of errors, especially in potential-field formulae where
a factor of $G$ or $4\pi$ can vanish silently.

**H4 — Go to the limits.** Let the depth go to zero; let the contrast vanish; let
the frequency go to infinity. If a formula does not behave sensibly at the
limits, something is wrong with the formula or your interpretation of it.

**H5 — Use symmetry and superposition.** Symmetry collapses dimensional
reductions: a spherically symmetric body is effectively one-dimensional. For a
body that is *not* symmetric, split it into symmetric pieces and superpose,
which is the basis of most forward modelling.

**H6 — Draw the cartoon and label the unknowns.** A cross-section with a source,
a ray path, a depth axis, and the quantity you want, labelled with units, is
often enough to reveal the equation you need.

**H7 — Ask what would break the conclusion.** Name one measurement that would
falsify your interpretation. If none exists, your interpretation is not yet
scientific; it is a description.

**H8 — Find the smallest version of the problem.** Replace the 2-D model with a
1-D model, the irregular source with a point, the viscoelastic medium with an
elastic one. Solve that, then add back one complication at a time. This is also
how you debug a numerical model: it must reproduce the simple case first.

**H9 — Timebox and park.** Twenty minutes of genuine struggle, then consult a
reference, then return to the problem cold within 24 hours. Consulting after a
serious attempt is not cheating; consulting immediately is.

## 6. Worked example: applying these habits to the wave equation

Suppose your target checkpoint is the intermediate-stage one: derive the 1-D
wave equation and verify a finite-difference solution.

**Week 1 — deliberate practice on the weak component.** Attempt the derivation
from a stretched string without notes. You get the string force balance but
confuse the sign of the tension restoring force. That single component is your
target. Redo *only* the force balance, three times, on separate days, each time
checking the sign against the physical picture (a positive curvature must pull
the element down towards the straight line).

**Week 2 — varied practice.** Do the same derivation for (i) a rod in torsion,
(ii) a column of gas, (iii) a transmission line. The mathematics is nearly
identical; the physical interpretation is not. Producing the same equation from
three different physics is what turns the equation into a *pattern* rather than a
memorised result.

**Week 3 — retrieval under transfer.** Without looking anything up, write the
finite-difference update for the 1-D wave equation on a staggered grid, choose
the time step from a stability condition, and run it. Then break it: raise the
time step past the stability limit and predict the failure mode *before* running
it. Refine the Courant condition numerically — find the largest stable ratio for
your scheme and compare it with the analytic prediction. Now you are doing
deliberate practice on a numerical task, not reading about one.

**Monthly — spaced retrieval.** Re-derive the equation and re-run the check from
memory. The first time, expect to need the notes. The fifth time, you will not,
and the knowledge is durable.

## 7. Worked example: diagnosing a failed attempt

You attempt a gravity problem, get an answer, and it is wrong by a factor of
$10^{4}$. Instead of re-deriving everything, run a checklist:

| Check | What you did | What it revealed |
|---|---|---|
| Dimensions | Wrote units on every term | All consistent — so not a dimension drop |
| Magnitudes | Estimated $\sim 10^{-5}$ before computing | Predicted milliGals; got $10^{-1}$, so the error is a unit factor |
| Units of input | Re-read the input density | It was given in $\text{g}\,\text{cm}^{-3}$, used as $\text{kg}\,\text{m}^{-3}$ |
| Fix and re-check | Converted density, repeated the estimate | Answer now matches the estimate |

The lesson is structural: **the estimate found the error, and the estimate took
thirty seconds**. Error localisation, not re-derivation, is what rescues a failed
problem attempt.

## 8. Habit design and time management

Willpower is a poor foundation for a multi-year skill. Design habits instead:

- **Fixed time, fixed place.** A daily 45-minute block beats a weekly five-hour
  block, because the start-up cost is paid once per day rather than once per
  session, and because retrieval benefits from being spread.
- **Implementation intentions.** Specify the cue and the action: "after lunch on
  weekdays, I derive one result on paper." Cue-based plans outperform vague
  intentions reliably.
- **A study log.** One line per session: date, material, the *weak component*
  worked on, and whether feedback arrived. The log makes drift visible within
  weeks.
- **Deliberate stopping.** End a session mid-problem, at a point where you know
  the next step. Restarting is then trivial, because the plan is already in your
  head.
- **Protect the hard block.** Derivation and debugging need uninterrupted time;
  reading and note-formatting can absorb interruptions. Schedule accordingly.

A weekly template that satisfies the four conditions of deliberate practice,
using roughly ten hours:

| Block | Activity |
|---|---|
| 4 × 45 min | Derivation practice with immediate checks |
| 3 × 45 min | Computing: implement, verify against an analytic case, break it |
| 2 × 45 min | Graded exercises, interleaved, closed-book |
| 1 × 45 min | Spaced retrieval across all current material, plus review of the log |

## Common mistakes

1. **Confusing hours with practice.** Unfocused time does not compound.
2. **Practising what you are already good at.** It feels productive precisely
   because it is easy.
3. **Collecting resources.** Twenty saved papers is not progress; one reproduced
   figure is.
4. **Blocked-only practice.** Comfortable, and it hides the skill of *choosing* a
   method.
5. **Never testing recall.** Re-reading is fluency, not memory.
6. **Abandoning a problem after five minutes, or after two hours.** Twenty
   minutes of genuine struggle, then reference, then a cold return, is the
   productive pattern.
7. **Ignoring the estimate.** The thirty-second estimate is the cheapest error
   detector available.

## Real-world applications

- **Project work.** A research project is a sequence of weak-component
  identifications: which part of the pipeline is failing, and how do I get
  feedback on that part specifically?
- **Code review and peer review.** The same habit — locating the weakest
  component and asking what would falsify it — is how reviewers find real
  problems rather than stylistic ones.
- **Emergency response.** Aftershock forecasting during a response runs on
  routines performed under time pressure; those routines must have been
  practised to automaticity beforehand.

## Further reading

- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of
  deliberate practice in the acquisition of expert performance.
  *Psychological Review*, 100(3), 363–406. — The original formulation of
  deliberate practice; note that later work debates how far it explains
  expertise, but the design conditions remain useful.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T.
  (2013). Improving students' learning with effective learning techniques.
  *Psychological Science in the Public Interest*, 14(1), 4–58. — Practice
  testing and distributed practice are rated highest; rereading and highlighting
  lowest.
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking
  memory tests improves long-term retention. *Psychological Science*, 17(3),
  249–255. — The standard demonstration that retrieval beats restudy.
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006).
  Distributed practice in verbal recall tasks: A review and quantitative
  synthesis. *Psychological Bulletin*, 132(3), 354–380. — Meta-analysis of the
  spacing effect, including how optimal gaps scale with retention interval.
- Pólya, G. (1945). *How to Solve It.* Princeton University Press. — The origin
  of most modern problem-solving heuristic lists, including several of the items
  in section 5.
  These are bibliographic records; verify current availability through your
  library or a DOI resolver before citing them yourself.

## Related lessons

- [How to Learn Geophysics: A Method, Not a Reading List](./01-how-to-learn-geophysics.md)
- [Diagnostic Self-Assessment and Placement Quiz](./03-self-assessment.md)
- [Research Milestones from Beginner to Independent Investigator](./05-milestones.md)
- [Cross-Cutting Skills: Mathematics, Computing, Inverse Theory](../02-curriculum-map/04-cross-cutting.md)
