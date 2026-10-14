---
id: 00-01-01
title: "How to Learn Geophysics: A Method, Not a Reading List"
level: beginner
prereqs: []
estimated_minutes: 45
tags: [study-method, learning, metacognition]
---

# How to Learn Geophysics: A Method, Not a Reading List

## Learning objectives

- Explain why geophysics resists rote learning and demands a specific method.
- Describe the five-link inference chain that structures every topic in this
  curriculum.
- Distinguish *recognition* from *recall* from *transfer*, and identify which
  one you are actually doing when you read.
- Apply the read-derive-compute-explain loop to a worked example.

## Prerequisites

None. This is the first lesson in the curriculum.

## 1. Why the usual approach fails

Most people begin a technical subject by reading. Reading feels productive
because it is fluent — the words are English, the sentences parse, and you can
follow the argument while your eyes are on it. The failure appears later, when
you need to *use* the idea:

- You recognise the wave equation but cannot solve it for a new boundary
  condition.
- You can state Darcy's law but cannot say what happens to your answer when
  permeability varies by three orders of magnitude across a grid cell.
- You have read about non-uniqueness in gravity inversion but cannot say
  whether a particular published model is *implied* by its data or merely
  *consistent* with it.

The reason is that geophysics is not a body of facts. It is a set of
**inference procedures** that connect physical laws to imperfect measurements.
Procedures are learned by executing them, not by reading about them.

> **Recognition** — "I have seen this."
> **Recall** — "I can reproduce this from memory."
> **Transfer** — "I can use this on a problem I have not seen."
>
> Reading reliably produces recognition. Only retrieval practice and
> computation produce recall and transfer. Exams, research, and field problems
> all test transfer.

## 2. The inference chain

Every result in geophysics, from a magnetic anomaly over a buried drum to a
global mantle tomography model, is an instance of the same chain:

```text
  (1) PROPERTY CONTRAST      A rock property differs across a boundary
              |
              v
  (2) FIELD RESPONSE         The contrast perturbs a field, or perturbs wave
                             propagation, in a way governed by physics
              |
              v
  (3) MEASUREMENT            An instrument records the field/response, adding
                             noise, drift, and its own response function
              |
              v
  (4) INVERSION              We infer a model from data; this step is usually
                             ill-posed and never unique
              |
              v
  (5) MODEL + UNCERTAINTY    A defensible statement, including what the data
                             do NOT constrain
```

A concrete instance, which you will be able to do rigorously by the end of
[06-seismology](../../06-seismology/README.md):

| Link | Seismic example |
|---|---|
| Property contrast | Elastic moduli and density change across the Moho |
| Field response | A seismic wave refracts and reflects; travel times depend on velocity structure |
| Measurement | A seismometer at a given distance records an arrival time |
| Inversion | Solve for velocity structure given many distance–time pairs |
| Model + uncertainty | A velocity profile with a resolution kernel showing which depths are constrained |

**Use this table as a diagnostic.** When a derivation loses you, ask: which link
am I on? When a paper's conclusion seems too strong, ask: at which link is the
weakness — a small property contrast, an unmodelled instrument effect, an
underdetermined inversion, or an unstated uncertainty?

## 3. Equations are sentences, not obstacles

A common mistake is to treat mathematics as a barrier standing between you and
the physics. In this curriculum, mathematics is the *notation of the physics*.
Consider the one-dimensional wave equation, which you will derive from first
principles in [02-physics](../../02-physics/README.md):

$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}.$$

You can read this as a sentence with a subject and an assertion:

> "The way the field's slope changes in space is what makes the field
> accelerate in time, scaled by the squared wave speed $c^2$."

Three habits make equations readable:

1. **Say it aloud in words.** If you cannot, you do not yet understand it.
2. **Track the units.** Both sides must have identical dimensions; a dimension
   check catches a large fraction of algebra errors for free (developed fully in
   [01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)).
3. **Find the limiting cases.** What happens when $c \to 0$? When the medium is
   uniform? When the source is a delta function? Limits are where physical
   intuition lives.

## 4. The loop you will actually use

For every lesson from here on:

**Step 1 — Question before content.** Read the learning objectives and section
headings. Write down what you expect the lesson to claim. A prediction, even a
wrong one, makes the subsequent reading far more effective.

**Step 2 — Derive before reading the result.** Cover the derivation in the
lesson. Attempt it. A five-minute genuine attempt that fails teaches more than
five minutes of reading that succeeds.

**Step 3 — Compute and break.** Run the Python demonstration. Then deliberately
break it: set a parameter to an extreme, remove a term, halve the sampling
rate. **Predict the outcome before you run it.** When your prediction is wrong,
you have found a boundary of your understanding — the single most valuable
thing that can happen in a study session.

**Step 4 — Retrieve before reviewing.** Attempt exercises closed-book. Attempt
the ★ exercises at minimum, ★★ if the topic is in your research path, ★★★ if
you intend to publish in this area.

**Step 5 — Explain from memory.** Close everything and write two paragraphs:
what this was about, and why anyone cares. If you cannot, you have identified
precisely what you have not learned.

## 5. A worked example of the loop

Applied to the gravity field of a buried sphere — a standard potential-field
exercise you will meet properly in
[07-gravity-geodesy](../../07-gravity-geodesy/README.md):

**Question first.** "The gravitational acceleration outside a uniform sphere
should behave as if all the mass were at the centre — but only *outside*. What
happens inside, and does that matter for a buried orebody?"

**Derive.** Use Gauss's law for the gravitational field,

$$\oint_{S} \mathbf{g} \cdot d\mathbf{A} = -4\pi G M_{\text{enc}}.$$

For a spherical surface of radius $r$ inside a body of uniform density $\rho$,
the enclosed mass is $M_{\text{enc}} = \tfrac{4}{3}\pi r^{3}\rho$, so

$$g(r) \cdot 4\pi r^{2} = -4\pi G \cdot \tfrac{4}{3}\pi r^{3}\rho
\quad\Longrightarrow\quad
g(r) = -\tfrac{4}{3}\pi G \rho\, r \qquad (r \le R).$$

Outside the body ($r > R$) the enclosed mass is the constant $M = \tfrac{4}{3}\pi R^{3}\rho$,
giving the familiar inverse-square law

$$g(r) = -\frac{GM}{r^{2}} \qquad (r > R).$$

So the field is **linear in radius inside** and **inverse-square outside**, and
the two expressions agree at $r = R$.

**Compute and break.** Now break it: what if the body is a thin *spherical
shell* rather than a solid sphere? Predict first, then compute. Inside a uniform
shell the enclosed mass is zero, so $g = 0$ — this is Newton's shell theorem,
and it explains why a gravimeter lowered into a deep mine does not register the
full mass of the rock above it.

**Explain.** "Outside a spherically symmetric body, only the total mass is
visible: the mass distribution is hidden. Inside, it is not. This is why a deep
target and a shallow target of equal mass produce detectably different anomaly
shapes — the depth is recoverable from the *shape*, even though the mass is all
that matters for the *amplitude*."

## 6. How to spend your time

A rough allocation that serves most learners, per hour of study:

| Activity | Share | Why |
|---|---|---|
| Deriving on paper | 30% | Builds transferable procedure |
| Writing and debugging code | 30% | Turns theory into a usable tool |
| Attempting problems | 25% | Retrieval practice |
| Reading | 15% | Necessary, but easily over-done |

If your reading share is above 50%, you are almost certainly learning less than
you feel you are. This is the most common failure mode in self-directed study.

## Common mistakes

1. **Reading as studying.** Fluency while reading is mistaken for understanding.
2. **Copying code rather than writing it.** Typing someone else's code teaches
   syntax and none of the design decisions.
3. **Skipping the limiting cases.** The limits are where physics becomes visible.
4. **Treating the solution file as the answer key.** It is one valid route, not
   the only one; a different correct route is not a mistake.
5. **Chasing breadth.** Systematic coverage of three well-understood methods
   beats shallow acquaintance with twenty.

## Real-world applications

This is not abstract advice. In professional practice these habits appear as:

- **Reviewing a consultant's report.** The inference-chain table is exactly how
  experienced geophysicists locate the weak link in someone else's argument.
- **Peer review.** Most methodological criticism in refereed papers identifies a
  specific link — usually the inversion or the uncertainty claim.
- **Field decisions.** "This anomaly could be a sulphide body or a shear zone;
  which measurement would discriminate?" is a step-3 question.

## Further reading

- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T.
  (2013). Improving students' learning with effective learning techniques.
  *Psychological Science in the Public Interest*, 14(1), 4–58. — A systematic
  review ranking ten study techniques by measured effectiveness; practice
  testing and distributed practice rank highest, rereading and highlighting
  lowest. Level: accessible to any reader.
- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of
  deliberate practice in the acquisition of expert performance.
  *Psychological Review*, 100(3), 363–406. — The original definition of
  deliberate practice, emphasising immediate feedback and repetition of
  weaknesses rather than strengths.
- Wieman, C. E. (2014). Large-scale comparison of science teaching methods
  sends clear message. *PNAS*, 111(23), 8319–8320. — Short, readable summary of
  evidence that active engagement beats passive instruction.
  Citations are given as bibliographic records; confirm current availability
  through your library or a DOI resolver before citing them yourself, as this
  curriculum does not reproduce or host copyrighted text.

## Related lessons

- [The Six Stages and Their Mastery Checkpoints](./02-six-stages.md)
- [Deliberate Practice, Spaced Repetition and Problem-Solving Habits](./04-study-habits.md)
- [Research Milestones from Beginner to Independent Investigator](./05-milestones.md)
