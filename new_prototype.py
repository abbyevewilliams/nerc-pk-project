import matplotlib.pylab as plt
import numpy as np
import scipy.integrate
import pkmodel as pk

def dose(t, X):
    return X

def rhs(t, y, Q_p1, V_c, V_p, CL, X):
    q = y
    transition = []
    for i in range(len(V_p)):
        transition.append(q[0] / V_c - q[i+1] / V_p[i])
    dqc_dt = dose(t, X) - q[0] / V_c * CL - sum(transition)
    return [dqc_dt, *transition]

model = pk.Model(name = "model", Q_p = [1, 2, 4], V_p = [1, 2, 4])
print(model)

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0 for i in range(len(model.V_p)+1)])

fig = plt.figure()
args = [model.Q_p, model.V_c, model.V_p, model.CL, model.X]
sol = scipy.integrate.solve_ivp(
    fun=lambda t, y: rhs(t, y, *args),
    t_span=[t_eval[0], t_eval[-1]],
    y0=y0, t_eval=t_eval
)
plt.plot(sol.t, sol.y[0, :], label=f"{model.name} - q_c")
for i in range(1, len(sol.y)):
    plt.plot(sol.t, sol.y[i, :], label=f"{model.name} - q_p{str(i)}")

plt.legend()
plt.show()