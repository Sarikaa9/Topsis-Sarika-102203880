 import numpy as np

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = np.array(data, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.impacts = np.array(impacts)

    def normalize(self):
        norm_data = self.data / np.sqrt((self.data**2).sum(axis=0))
        return norm_data

    def weighted_normalized(self):
        return self.normalize() * self.weights

    def ideal_best_worst(self, weighted_data):
        ideal_best = np.where(self.impacts == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
        ideal_worst = np.where(self.impacts == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))
        return ideal_best, ideal_worst

    def calculate_topsis_score(self):
        weighted_data = self.weighted_normalized()
        ideal_best, ideal_worst = self.ideal_best_worst(weighted_data)

        distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

        topsis_score = distance_worst / (distance_best + distance_worst)
        return topsis_score, np.argsort(-topsis_score) + 1  # Rankings

