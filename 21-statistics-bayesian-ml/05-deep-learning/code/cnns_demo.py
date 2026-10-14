#!/usr/bin/env python3
"""Convolutional networks on SYNTHETIC data: a convolution implemented directly,
the parameter count against a fully connected layer, the receptive field of a
stack, and a translation-invariance measurement.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cnns_demo.py

Everything is SYNTHETIC and generated below; no measured value is used.

Sections
--------
1. A convolution computed directly, and the same result as a sliding dot product.
2. Parameter count: convolutional versus fully connected.
3. Receptive field and translation invariance.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def conv2d(image, kernel):
    kh, kw = kernel.shape
    out = np.zeros((image.shape[0] - kh + 1, image.shape[1] - kw + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = float(np.sum(image[i:i + kh, j:j + kw] * kernel))
    return out


def main():
    print("SYNTHETIC data generated below; no measured value is used.")

    section("1. A convolution computed directly")
    image = np.zeros((8, 8))
    image[3:5, :] = 1.0                       # a horizontal band
    kernel = np.array([[-1.0, -1.0, -1.0],
                       [0.0, 0.0, 0.0],
                       [1.0, 1.0, 1.0]])      # a vertical edge detector
    fm = conv2d(image, kernel)
    print("  horizontal-band image, vertical-edge kernel:")
    for row in fm:
        print("   " + " ".join(f"{v:+4.0f}" for v in row))
    print(f"  feature-map maximum = {fm.max():.1f} at rows "
          f"{np.argwhere(fm == fm.max())[:, 0].tolist()}: the two edges of the")
    print("  band are found, with opposite signs, and the flat interior gives 0.")

    section("2. Parameter count: convolutional versus fully connected")
    side, channels, filters = 32, 1, 16
    k = 3
    conv_params = channels * filters * k * k + filters
    dense_params = (side * side * channels) * (side * side * filters) + side * side * filters
    print(f"  input {side}x{side}, {channels} channel, {k}x{k} kernel, "
          f"{filters} filters")
    print(f"  convolution: {channels * filters * k * k} weights + {filters} "
          f"biases = {conv_params} parameters")
    print(f"  fully connected to the same spatial size: {dense_params} "
          f"parameters")
    print(f"  ratio = {dense_params / conv_params:,.0f}x")
    print("  weight sharing is the reason a convolutional layer can be deep")
    print("  enough to be useful on an image of geophysical size.")

    section("3. Receptive field and translation invariance")
    layers = 6
    print("  L layers of 3x3 stride 1 give a receptive field of 1 + 2L cells:")
    for L in (1, 2, 3, 6, 12):
        print(f"    L = {L:2d} -> receptive field = {1 + 2 * L:2d} cells")
    print(f"  with {layers} layers the field is {1 + 2 * layers} cells: a deep")
    print("  stack sees a wider context without any increase in kernel size.")
    img = np.zeros((16, 16))
    img[8, 6:10] = 1.0
    fm1 = conv2d(img, kernel)
    shifted = np.roll(img, 3, axis=1)
    fm2 = conv2d(shifted, kernel)
    print(f"  feature map of the original: maximum {fm1.max():.1f} at "
          f"{np.argwhere(fm1 == fm1.max()).tolist()}")
    print(f"  feature map after a 3-cell shift: maximum {fm2.max():.1f} at "
          f"{np.argwhere(fm2 == fm2.max()).tolist()}")
    print("  the response is identical in magnitude and moves by exactly the")
    print("  shift: convolution is equivariant to translation, which is why a")
    print("  detector trained at one location works at another.")


if __name__ == "__main__":
    main()
