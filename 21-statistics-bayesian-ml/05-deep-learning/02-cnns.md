---
id: 21-05-02
title: "Convolutional Networks for Seismic and Image Data"
level: research
prereqs: ["21-05-01", "20-01-03"]
estimated_minutes: 60
tags: [deep-learning, cnn, convolution, receptive-field, translation-invariance, seismic]
---

# Convolutional Networks for Seismic and Image Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a discrete convolution and **explain** what a learned kernel
   detects.
2. **Derive** the parameter count of a convolutional layer and **compare** it
   with a fully connected layer of the same output size.
3. **Compute** the receptive field of a stack of convolutions and **relate** it to
   the geological scale the network can see.
4. **Explain** translation equivariance and **state** exactly what it does and does
   not provide.
5. **Interpret** convolution as a matched filter and **state** the connection to
   classical seismic processing.
6. **State** what a convolutional network cannot do about non-stationarity,
   anisotropy and absolute position.

All data in this lesson are **SYNTHETIC**: a hand-built image and a fixed kernel.
No measured value is used.

## Prerequisites

- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the framework the convolutional layer sits in.
- [20-01-03 Convolution, Correlation and Filtering](../../20-signal-processing/01-signals-and-systems/03-convolution-and-filters.md) —
  the convolution the layer implements.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../04-machine-learning-fundamentals/03-model-assessment.md) —
  the validation that spatial data requires in blocked form.

## 1. Intuition: a shared filter, applied everywhere

A fully connected layer treats every input pixel as unrelated: it learns a
separate weight for each, and it must learn each of them from scratch. A
convolutional layer assumes something about the data instead — that the same
pattern is meaningful wherever it occurs — and encodes that assumption by
**sharing** one small kernel across all positions. Two gains follow immediately:

- **Fewer parameters**, by a factor of thousands for an image of realistic size,
  which is what makes deep stacks trainable.
- **Equivariance**: a feature detected at one location is detected at any other,
  so a model trained on one part of a survey transfers to another.

The assumption is not free. A shared kernel asserts **stationarity** — that the
same filter is the right filter everywhere — and that assertion is exactly what
fails across a facies boundary, a change of acquisition, or a transition from
sediment to basement. A convolutional network is a stationarity assumption with a
trainable kernel.

## 2. The convolution layer

For an input $X$, kernel $K$ of size $k\times k$ and output channel $c$,

$$Y_c(i,j) = \phi\Big(b_c + \sum_{c'}\sum_{u,v} K_c(u,v)\,X_{c'}(i+u, j+v)\Big).$$

The kernel is the learnable object; the summation pattern is fixed. In signal
terms this is a **matched filter** for the pattern in $K$, and the classical
seismic analogues are immediate: a spatial derivative kernel detects edges, a
band-pass kernel detects a frequency band, a first-break-referenced kernel detects
a moveout. A convolutional network's first layer learns a bank of such filters,
and the training is the search for the bank that best predicts the target.

**Parameter count.** For $C_{\text{in}}$ input channels, $C_{\text{out}}$ output
channels and a $k\times k$ kernel:

$$\#\text{conv} = C_{\text{in}}C_{\text{out}}k^{2} + C_{\text{out}}, \qquad
\#\text{dense} = (HW C_{\text{in}})(HW C_{\text{out}}) + HW C_{\text{out}} .$$

The ratio grows as $(HW)^{2}/(k^{2}C_{\text{out}})$: weight sharing is the reason
a convolutional layer can be deep enough to be useful.

**Receptive field.** With stride 1 and no dilation, $L$ layers of $k\times k$
kernels see a region of $1 + L(k-1)$ cells. The receptive field is the geological
scale the network can integrate, and it must be chosen to match the scale of the
feature being predicted: a network with a $13\times13$ field cannot use a
$50\times50$ context.

## 3. Equivariance, and what it does not give

Convolution is **equivariant** to translation: shifting the input shifts the
feature map by the same amount and changes nothing else. That is a genuine
symmetry, and it is why a detector learned on one part of a survey works
elsewhere. It is not invariance: the feature map still knows *where* the pattern
was, which is usually desirable, since position carries geological information.

What convolution does **not** provide:

- **Rotation or scale invariance.** A rotated fault image is a different pattern
  unless the architecture or the augmentation supplies the symmetry.
- **Anisotropy handling.** A square kernel treats vertical and horizontal
  structure alike, but sedimentary layering is anisotropic; rectangular kernels,
  directional stacks or dilated convolutions are needed to encode that.
- **Global context.** A receptive field of $13$ cells cannot know about a
  structure $100$ cells away; that requires pooling, dilation or attention.

## 4. Worked example

The demonstration implements the convolution directly and measures each property.

**A kernel detects an edge.** An $8\times8$ image with a horizontal band at rows
$3$–$4$ is convolved with the vertical-edge detector

$$K = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}.$$

The feature-map maximum is $3.0$ at rows $1$ and $2$ of the $6\times6$ output —
one edge of the band — with $-3.0$ at rows $3$ and $4$ for the other edge and
exactly $0$ in the flat interior: the response is the row-to-row difference, so
only the two boundaries of the band register.

**Parameter sharing.** A $32\times32$ single-channel image with $16$ filters of
size $3\times3$ uses

$$\#\text{conv} = 1\times16\times3^{2} + 16 = 160 \text{ parameters},$$

while a fully connected layer mapping the same input to the same
$32\times32\times16$ output uses

$$(32\times32\times1)(32\times32\times16) + 32\times32\times16 = 16\,793\,600
\text{ parameters},$$

a ratio of **$104\,960\times$**. The reduction is not a detail: it is the difference
between a two-layer network and a thirty-layer one.

**Receptive field.** With $3\times3$ kernels, $L$ layers give $1+2L$ cells:
$3$, $5$, $7$, $13$ and $25$ cells for $L = 1, 2, 3, 6, 12$. A six-layer stack
integrates a $13\times13$ neighbourhood, which for a $4\ \mathrm m$ seismic
sample is a $52\ \mathrm m$ window — the scale of a thin bed rather than of a
reservoir.

**Equivariance.** The feature map of the original image has its maximum $3.0$ at
positions $[[6,6],[6,7]]$; after shifting the image by three cells, the maximum
is $3.0$ at $[[6,9],[6,10]]$ — identical in magnitude and displaced by exactly
the shift. No retraining, no loss of response.

## Assumptions and regime of validity

1. **Stationarity.** A shared kernel asserts the same filter applies everywhere;
   across a facies boundary or an acquisition change it does not.
2. **Local correlation.** The architecture assumes that nearby samples are more
   informative jointly than distant ones; a long-range dependence needs dilation,
   pooling or attention.
3. **Blocked validation.** Spatial data must be split by region or transect, never
   at random, or neighbouring pixels leak.
4. **Boundary conditions.** Padding choices change the edges of the output and
   can dominate small volumes; report the padding.
5. **Amplitude scaling.** Seismic amplitudes vary with depth and gain; per-window
   normalisation is usually required and is itself a modelling choice.
6. **Equivariance is not invariance.** The network still sees absolute position
   unless it is explicitly removed, which is desirable for mapping and
   undesirable for classification across surveys.

## The honest summary

A convolutional network is a stationarity assumption with learnable kernels, and
the demonstration priced both sides of it. Weight sharing cut the parameter count
from $16\,793\,600$ to $160$ — a factor of $104\,960$ — and a six-layer stack reached a
$13\times13$ receptive field without any increase in kernel size. The symmetry is
exact: shifting the image by three cells moved the response by exactly three cells
with the same magnitude. What the architecture does **not** supply is invariance
to rotation or scale, any handling of anisotropy, or global context; and its
central assumption — that the same filter is right everywhere — is precisely what
fails across the geological boundaries a seismic interpretation is usually about.

## Python demonstration

[`code/cnns_demo.py`](./code/cnns_demo.py) prints every number quoted above. It:

1. computes a convolution directly and prints the feature map;
2. compares convolutional and fully connected parameter counts;
3. computes receptive fields and measures translation equivariance.

```bash
cd 21-statistics-bayesian-ml/05-deep-learning/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cnns_demo.py
```

It runs in under a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/02-cnns-exercises.md`](./exercises/02-cnns-exercises.md) with worked
solutions in
[`exercises/02-cnns-solutions.md`](./exercises/02-cnns-solutions.md).

## Mastery checkpoint

Without notes, a $32\times32$ input with $16$ filters of $3\times3$ uses $160$
convolutional parameters against $16\,793\,600$ for the equivalent fully connected
layer; $L$ layers of $3\times3$ kernels give $1+2L$ cells of receptive field; and
a three-cell image shift moves the response by exactly three cells.

1. Compute the parameter ratio and state the formula it follows.
2. Compute the receptive field of eight $5\times5$ layers with stride 1.
3. State the operation that would give the network a $50$-cell context without
   deepening the stack.
4. State what the shared kernel assumes about the field and one geological
   situation where that assumption fails.

## Common pitfalls

1. **Assuming invariance instead of equivariance.** The feature map retains
   position.
2. **Choosing the kernel size without computing the receptive field.** A field
   smaller than the target's scale cannot see it.
3. **Random splitting of spatial data.** Neighbouring pixels leak; use blocked
   splits.
4. **Ignoring anisotropy.** Square kernels treat layering and faulting alike.
5. **Forgetting padding and boundary effects.** They can dominate small volumes.
6. **Reading first-layer kernels as geology.** They are fitted filters; the
   interpretation requires an independent argument.

## Where this is used

- **Seismic facies classification** from post-stack volumes.
- **Fault and channel detection** on amplitude or attribute volumes.
- **Denoising and interpolation** of seismic or GPR data.
- **Phase picking** on three-component records represented as images.
- **Remote-sensing segmentation** of geological and land-cover classes.

## Related lessons

- [21-05-01 Neural Networks: Architecture, Activation, Backpropagation](01-neural-networks.md) —
  the layer stack and its gradients.
- [20-01-03 Convolution, Correlation and Filtering](../../20-signal-processing/01-signals-and-systems/03-convolution-and-filters.md) —
  the classical operator the layer generalises.
- [21-05-04 Attention and Transformers for Geophysical Sequences](04-transformers.md) —
  the architecture that supplies global context.
- [21-05-06 GANs, VAEs and Diffusion Models](06-generative-models.md) —
  generative models that use convolutional encoders and decoders.
- [21-06-01 ML for Seismic Detection, Picking and Classification](../06-ml-in-geophysics/01-seismic-ml.md) —
  the applied version of this lesson.

## Self-assessment checklist

- [ ] I can compute a convolution and interpret a kernel.
- [ ] I can count the parameters of a convolutional layer and compare with dense.
- [ ] I can compute a receptive field and choose a kernel size accordingly.
- [ ] I can state what equivariance does and does not give.
- [ ] I can connect convolution to classical filtering.
- [ ] I can name the assumption that fails across geological boundaries.
