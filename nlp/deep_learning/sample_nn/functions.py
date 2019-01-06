import numpy as np


def relu(x):
    return np.maximum(0, x)


def softmax(x):
    if x.ndim == 2:
        x = x - x.max(axis=1, keepdims=True)
        x = np.exp(x)
        x = x / x.sum(axis=1, keepdims=True)
    elif x.ndim == 1:
        x = x - x.max(keepdims=True)
        x = np.exp(x) / np.sum(np.exp(x))
    return x
