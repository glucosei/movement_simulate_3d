import matplotlib.pyplot as plt
import numpy as np

balls = list(map(float, input('공들을 떨어뜨릴 높이(m)(공백으로 구분): ').split(' ')))
g=9.80665
dt=0.1
t=0
dones = np.zeros_like(balls, dtype=bool)
all_done = False


trajectories = [[(balls.index(i)*50, i)] for i in balls]
fig = plt.figure()
ax = fig.add_subplot()

while not all_done:
    ax.cla()
    ax.set_title("free-fall")
    #ax.set_xlim(-1, 600)
    ax.set_ylim(0, max(balls))
    #ax.set_zlim(-1, 600)

    for i in range(len(balls)):
        x, y = zip(*trajectories[i])
        ax.scatter(x, y, label=balls[i])
    ax.legend()

    t = t + dt

    for i in range(len(balls)):
        last_x, last_y = trajectories[i][-1]
        next_y = last_y - 0.5 * g * t**2

        if next_y <= 0:
            trajectories[i].append((last_x, 0))
            dones[i] = True
            continue

        trajectories[i].append((last_x, next_y))

    all_done = dones.all()

    plt.pause(0.01)
    #print(t)

ax.cla()
ax.set_title("free-fall")
ax.set_ylim(0, max(balls))
for i in range(len(balls)):
    x, y = zip(*trajectories[i])
    ax.scatter(x, y, label=balls[i])
    ax.legend()
plt.show()