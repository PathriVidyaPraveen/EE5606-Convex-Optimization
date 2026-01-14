import cvxpy as cp
import numpy as np

np.random.seed(0)

# dimensions
n = 5
m_ineq = 4
m_eq = 2

# data
P = np.random.randn(n, n)
P = P.T @ P          # make it PSD
q = np.random.randn(n)

G = np.random.randn(m_ineq, n)
h = np.random.randn(m_ineq)

A = np.random.randn(m_eq, n)
b = np.random.randn(m_eq)

# variable
x = cp.Variable(n)

# objective
objective = cp.Minimize(0.5 * cp.quad_form(x, P) + q @ x)

# constraints
constraints = [
    G @ x <= h,
    A @ x == b
]

# problem
problem = cp.Problem(objective, constraints)
problem.solve()

print("x =", x.value)
print("optimal value =", problem.value)
print("status =", problem.status)
