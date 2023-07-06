import matplotlib.pyplot as plt
import numpy as np
import math


# Env physics
g = 9.81
dt = 0.1
t = 0

angle = np.array([15, 30, 45, 60])
throw_v = 20
trajectories = [[(0,0)] for _ in range(len(angle))]
dones = np.zeros_like(angle, dtype=bool)
all_done = False

fig, ax = plt.subplots()

while(not all_done):
  ax.cla()
  ax.set_title("Throw the ball!")
  ax.set_xlim(-1, 600)
  ax.set_ylim(-1, 200)


  for i in range(len(angle)):
    x, y = zip(*trajectories[i])
    ax.scatter(x,y, label=angle[i])
  ax.legend()

  t = t + dt

  for i in range(len(angle)):
    last_x, last_y = trajectories[i][-1]
    w = angle[i]

    next_x, next_y = last_x + throw_v*math.cos(w/180 *3.14), last_y + throw_v*math.sin(w/180 *3.14) - g * t

    if next_y <= 0:
      dones[i] = True
      continue

    trajectories[i].append((next_x, next_y))

  all_done = dones.all()

  plt.pause(0.01)

plt.show()