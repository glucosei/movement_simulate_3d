import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

g = 9.80665
dt = 0.1
t = 0

angle = list(map(int,input("각도들(공백으로 구분): ").split()))
throw_v_x = 15
throw_v_z = 30
throw_v = (throw_v_x**2+throw_v_z**2)**(1/2)
print(throw_v)
trajectories = [[(0, 0, 0)] for _ in range(len(angle))]
dones = np.zeros_like(angle, dtype=bool)
all_done = False

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

while not all_done:
    ax.cla()
    ax.set_title("Throw the ball!")
    #ax.set_xlim(-1, 600)
    #ax.set_ylim(-1, 600)
    #ax.set_zlim(-1, 600)

    for i in range(len(angle)):
        x, y, z = zip(*trajectories[i])
        ax.scatter(x, z, y, label=angle[i])
    ax.legend()

    t = t + dt

    for i in range(len(angle)):
        last_x, last_y, last_z = trajectories[i][-1]
        w = angle[i]

        next_x = last_x + throw_v_x * math.cos(w / 180 * np.pi) * t
        next_y = last_y + throw_v * math.sin(w / 180 * np.pi) * t - 0.5 * g * t**2
        next_z = last_z + throw_v_z * math.cos(w / 180 * np.pi) * t

        if next_y <= 0:
            dones[i] = True
            continue

        trajectories[i].append((next_x, next_y, next_z))

    all_done = dones.all()

    plt.pause(0.01)
for i in range(len(angle)):
    print(f"{angle[i]}도로 던졌을 때 간 거리: {(trajectories[i][-1][0]**2+trajectories[i][-1][2]**2)**(1/2):.2f}")
plt.show()
