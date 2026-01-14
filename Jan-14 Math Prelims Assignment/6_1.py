import cvxpy as cp
import numpy as np

x1 = cp.Variable()
x2 = cp.Variable()

objective = cp.Minimize(x1**2 + x2**2)

problem = cp.Problem(objective)

problem.solve()

print("x1 = ",x1.value)
print("x2 = ",x2.value)
print("Optimal value = " , problem.value)

# x1 = 0 , x2 = 0 , optimal value = 0
