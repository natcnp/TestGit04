import numpy as np
from scipy.optimize import linear_sum_assignment

# Create a cost matrix
cost_matrix = np.array([
    [4, 1, 3],
    [2, 3, 5],
    [3, 2, 1]
])

# Names for the workers
worker_names = ["John", "Cream", "Dream"]

# Tasks
task_names = ["Car Wash", "Wash the Dishes", "Sweep the House"]

# Solve the assignment problem
row_indices, col_indices = linear_sum_assignment(cost_matrix)

# Extract the optimal assignment
assignment = [(worker_names[row], task_names[col]) for row, col in zip(row_indices, col_indices)]

print("Optimal Assignment:")
for name, task in assignment:
    print(f"{name} assigned to {task}")
