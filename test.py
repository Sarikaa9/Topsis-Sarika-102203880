from Topsis.topsis import Topsis

data = [[250, 16, 12, 5],
        [200, 16, 8, 3],
        [300, 32, 16, 4],
        [275, 32, 8, 4],
        [225, 16, 16, 2]]

weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '-', '+']

topsis = Topsis(data, weights, impacts)
scores, ranks = topsis.calculate_topsis_score()

print("TOPSIS Scores:", scores)
print("Ranks:", ranks)

