import numpy as np
import matplotlib.pyplot as plt

g, L = 9.81, 1.0          # gravity (m/s^2), pendulum length (m)
dt, steps = 0.001, 10000  # time step (s), number of steps

theta = 1.0   # starting angle in radians (about 57 degrees)
omega = 0.0   # starting angular velocity

times, angles = [], []
for i in range(steps):
    alpha = -(g / L) * np.sin(theta)  # angular acceleration
    omega += alpha * dt               # update velocity
    theta += omega * dt               # update angle
    times.append(i * dt)
    angles.append(theta)

plt.plot(times, angles)
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Pendulum swing")
plt.show()
