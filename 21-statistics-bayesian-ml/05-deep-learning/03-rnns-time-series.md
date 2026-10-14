---
id: 21-05-03
title: "Recurrent Networks and Temporal Earth Data"
level: research
prereqs: ["21-05-01", "21-07-02"]
estimated_minutes: 60
tags: [deep-learning, rnn, bptt, vanishing-gradient, lstm, time-series]
---

# Recurrent Networks and Temporal Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the recurrence of a simple recurrent network and **state** what the
   hidden state carries.
2. **Derive** backpropagation through time and **explain** why the gradient is a
   product of one Jacobian per step.
3. **Measure** the vanishing and exploding gradient as a function of sequence
   length and spectral radius, and **state** the window a plain recurrence can
   learn.
4. **Explain** how a gate changes the decay into a learned, input-dependent
   quantity, and **compute** the effect for two gate values.
5. **Choose** between a recurrence, a windowed convolutional model and an
   attention model for a stated temporal problem.
6. **State** what a recurrent model assumes about stationarity in time.

All sequences in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the layer and gradient machinery the recurrence reuses.
- [21-07-02 State-Space Models and Kalman Filtering](../07-time-series-and-forecasting/02-state-space.md) —
  the classical recursive state estimator a recurrent network generalises.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the forward-chaining validation a time series requires.

## 1. Intuition: a state that carries the past

A recurrent network processes a sequence one step at a time, maintaining a hidden
state that summarises what it has seen. At each step the state is updated from the
new input and the previous state:

$$h_t = \phi\big(W_x x_t + W_h h_{t-1} + b\big), \qquad
\hat y_t = W_y h_t + c .$$

The same weights are used at every step, so the parameter count is independent of
the sequence length — the temporal analogue of the convolutional layer's weight
sharing. The hidden state is the model's entire memory: everything the network
knows about the past is in that vector, which is a strong and testable
assumption.

The classical counterpart is the Kalman filter, with the difference that the
recurrence is *learned* rather than derived from a stated linear-Gaussian model.
That is the trade: more flexibility, and no guarantee that the state means anything
physically.

## 2. Backpropagation through time

Unrolling the recurrence over $T$ steps turns it into a $T$-layer network with
shared weights, so ordinary backpropagation applies. The gradient with respect to
the state at step $t$ involves the product

$$\frac{\partial h_T}{\partial h_t}
= \prod_{s=t+1}^{T}\frac{\partial h_s}{\partial h_{s-1}}
= \prod_{s=t+1}^{T} \operatorname{diag}\big(\phi'(a_s)\big) W_h .$$

Three consequences follow immediately:

- If the spectral radius $\rho$ of $W_h$ is below one, the product **decays
  exponentially**: the gradient from a step $T-t$ away scales like $\rho^{T-t}$,
  and a long-range dependence is invisible to the optimiser.
- If $\rho > 1$, it **grows exponentially**, and training diverges.
- With saturation, $\phi'$ multiplies the decay further, since a saturated unit
  contributes a factor near zero.

Gradient clipping addresses the exploding case; the vanishing case requires an
architectural change, which is what gates supply.

## 3. Gates

A gated recurrence replaces the fixed weight matrix in the state update with an
input-dependent multiplier:

$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde c_t, \qquad
f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f),$$

where $f_t$ is the **forget gate**. If the gate is near one the cell state is
carried almost unchanged, so the gradient product no longer has to traverse a
fixed weight matrix; if it is near zero the memory is discarded. The decay
therefore becomes a **learned, input-dependent quantity** rather than a fixed
$\rho^{T-t}$.

The demonstration measures exactly that, with one gate:

| gate value | coefficient after 40 steps |
|---|---|
| plain recurrence, $\rho = 0.9$ | $1.478\times10^{-2}$ |
| forget gate closed, $g = 0.6225$ | $5.814\times10^{-9}$ |
| forget gate open, $g = 0.9959$ | $8.495\times10^{-1}$ |

The same layer, with the same weights, either discards the dependence entirely or
carries $85\ \%$ of it over forty steps — determined by the input through the
gate. That is the entire idea of an LSTM or GRU, expressed in one line of
arithmetic.

## 4. Training a recurrence

The demonstration trains a plain RNN by full-batch BPTT on a synthetic task:
predict the running mean of a random sequence, with $T = 20$ steps, $200$
sequences and a hidden dimension of $8$.

| epoch | MSE |
|---|---|
| 1 | $0.13097$ |
| 20 | $0.12370$ |
| 120 | $0.09385$ |

The target's variance is $0.18570$, so the network accounts for a substantial
fraction of it, and the convergence is slow and steady — the characteristic
behaviour of a plain recurrence on a task whose dependence spans many steps. The
running mean is a *global* function of the sequence, and with $T = 20$ and
$\rho < 1$ the early steps contribute almost nothing to the gradient at the last
step; most of the learning comes from the recent few.

## Assumptions and regime of validity

1. **Stationarity in time.** A recurrence assumes the same dynamics at every
   step; a regime change invalidates the trained weights.
2. **A sufficient state dimension.** The hidden state must be large enough to
   carry whatever the task requires; too small and the model cannot represent the
   dependence at all.
3. **Forward-chaining validation.** Time series must be split so that validation
   is always *after* training; a random split leaks the future.
4. **Sequence length matters.** With BPTT truncated to $k$ steps, the model cannot
   learn a dependence longer than $k$; report the truncation.
5. **Exogenous variables are not state.** Inputs the model cannot influence (a
   tide, a temperature) must be supplied as inputs, not inferred as state.
6. **The hidden state has no physical units.** It is a learned summary; naming it
   after a physical quantity requires an independent argument.

## The honest summary

A recurrent network is weight sharing in time plus a learned state, and its
central difficulty is arithmetic rather than conceptual. The demonstration showed
the gradient coefficient of a dependence $T$ steps away falling as $0.9^{T}$:
$0.122$ after $20$ steps and $0.0148$ after $40$, with no fixed choice of weights
avoiding either that decay or the $45.3$-fold explosion at $\rho = 1.1$. A single
forget gate changed the $40$-step coefficient from $5.8\times10^{-9}$ to $0.850$
depending on the input — the mechanism that makes gated recurrences able to learn
long-range structure at all. What the numbers do **not** establish is that a
recurrence is the right model for a real record: whether the dynamics are
stationary, whether the state has a physical meaning, and whether the validation
is forward-chaining are questions about the data, not the architecture.

## Python demonstration

[`code/rnns_time_series_demo.py`](./code/rnns_time_series_demo.py) prints every
number quoted above. It:

1. trains a plain RNN by full-batch BPTT on a running-mean task;
2. tabulates the gradient coefficient against sequence length and spectral
   radius;
3. computes the $40$-step coefficient for two forget-gate values.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rnns_time_series_demo.py
```

It runs in about two and a half seconds and prints only text.

## Exercises

Graded problems are in
[`exercises/03-rnns-time-series-exercises.md`](./exercises/03-rnns-time-series-exercises.md)
with worked solutions in
[`exercises/03-rnns-time-series-solutions.md`](./exercises/03-rnns-time-series-solutions.md).

## Mastery checkpoint

Without notes, a plain recurrence with $\rho = 0.9$ retains $1.478\times10^{-2}$
of a $40$-step dependence, and a gate with $g = 0.9959$ retains $0.8495$.

1. Compute $\rho^{T}$ for $\rho = 1.05$ and $T = 40$, and state the consequence
   for training.
2. Compute the gate value at which the $40$-step coefficient is $0.5$.
3. State why the running-mean task is harder than it looks for a plain RNN.
4. State the validation scheme a recurrent model on real records requires and
   what a random split would do.

## Common pitfalls

1. **Ignoring the vanishing gradient.** A plain RNN cannot learn a dependence
   longer than a few effective steps.
2. **Clipping as a cure.** Clipping fixes explosions, not decays.
3. **Truncating BPTT without reporting it.** The truncation length bounds the
   learnable dependence.
4. **Random splitting a time series.** It leaks the future into training.
5. **Assuming stationarity.** A trained recurrence applied to a changed regime is
   wrong without warning.
6. **Interpreting the hidden state physically.** It is a learned summary, not a
   measured quantity.

## Where this is used

- **Ground-motion and shaking forecasting** from past records.
- **GNSS and tide-gauge time series**: prediction and gap filling.
- **Seismic phase picking** on continuous waveforms, where the state carries the
  recent signal.
- **Hydrological forecasting**: rainfall-runoff with exogenous inputs.
- **Instrument monitoring**: detecting regime changes in sensor networks.

## Related lessons

- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the gradient machinery unrolled in time.
- [21-05-04 Attention and Transformers for Geophysical Sequences](04-transformers.md) —
  the alternative to a recurrence for long sequences.
- [21-07-02 State-Space Models and Kalman Filtering](../07-time-series-and-forecasting/02-state-space.md) —
  the classical recursive state estimator.
- [21-07-05 Point Processes and Seismicity Rate Models](../07-time-series-and-forecasting/05-point-processes.md) —
  temporal rate models of a different kind.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  forward-chaining validation.

## Self-assessment checklist

- [ ] I can write the recurrence and the BPTT gradient product.
- [ ] I can compute the gradient decay for a given spectral radius and length.
- [ ] I can explain what a forget gate changes.
- [ ] I can choose between a recurrence, a convolution and attention.
- [ ] I can state the validation scheme a time series requires.
- [ ] I can say what a hidden state does not mean.
