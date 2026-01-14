import cvxpy as cp
import numpy as np

# data
np.random.seed(0)
m,n = 50,20
A = np.random.randn(m,n)
b = np.random.randn(m)
lambda_val = 0.1

# variable
x = cp.Variable(n)

# objective
objective = cp.Minimize(cp.sum_squares(A@x - b) + lambda_val*cp.norm(x,1))

# problem
problem = cp.Problem(objective)
problem.solve()

print("x =", x.value)
print("optimal value =", problem.value)
