import numpy as np


def reg(u):
    u_reg = 1 / (np.linalg.norm(u)) * u
    u_reg_norm = np.linalg.norm(u_reg)

    print(f"{u_reg} , norm {u_reg_norm}")


reg(np.array([2, -7]))
reg(np.array([-9, 3, 7]))
reg(np.array([-3, 5, 8, 6]))
reg(np.array([-6, 2, 8, 3, 5]))

reg(np.array([5, 10, 4]))



vals = np.array([1,30,20,99,100,4])
n = np.linalg.norm(vals)

vals_n = vals * (1/n)
print(f"Norm {n}")
print(f"Norm vals {vals_n},  {np.linalg.norm(vals_n)}")
