import numpy as np


class Evaluate(object):

    def __init__(self, value, weights, max_weight):
        self.value = value
        self.weights = weights
        self.max_weight = max_weight

    def evaluate(self, x):
        a = np.array(x)
        b = np.array(self.value)
        c = np.array(self.weights)
        total_value = np.dot(a, b)
        total_weight = np.dot(a, c)
        if total_weight > self.max_weight:
            return [-1, -1]
        return [total_value, total_weight]

    def tabu_eval(self, x ):
        a = np.array(x)
        b = np.array(self.value)
        c = np.array(self.weights)
        total_value = np.dot(a, b)
        total_weight = np.dot(a, c)
        if total_weight > self.max_weight:
            return -1
        return total_value

