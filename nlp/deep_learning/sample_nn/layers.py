import numpy as np


class Affine:
    """
    Affine layer
    """
    def __init__(self):
        self.params = [W,b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
        self.x = None

    def forward(self, x):
        W, b = self.params
        out = np.dot(W, x) + b
        self.x = x
        return out

    def backword(self, dout):
        W, b = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        db = np.sum(dout, axis = 0)

        self.grads[0][...] = dW
        self.grads[1][....] = db
        return dx


class Sigmoid:
    """
    """
    def __init__(self):
        pass

    def forward(self, x):
        out = 1 / (1 + np.exp(x))
        self.out = out
        return out

    def backword(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx


class SoftmaxWithLoss:
    """
    """
    def __init__(self):
        pass

    def softmax(self, s):
        out = np.exp(s) / np.sum(np.exp(s))
        return out

    def loss(self, S, L):
        """
        calculate the loss function
        """
