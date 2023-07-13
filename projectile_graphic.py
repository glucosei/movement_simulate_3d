import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

def projectile_graphic():
    g = 9.80665
    dt = 0.1
    t = 0

    angle = list(map(float,input("각도들(°)(공백으로 구분): ").split()))
    throw_v = float(input("초기 속도(m/s): "))
    xz = float(input("xz평면에 내린 수선의 발과 원점을 이은 직선과 x축이 이루는 각도(°): "))

    trajectories = [[(0, 0, 0)] for _ in range(len(angle))]
    dones = np.zeros_like(angle, dtype=bool)
    all_done = False

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    while not all_done:
        ax.cla()
        ax.set_title("projectile movement")
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
            v_x_z= throw_v * np.cos(w/180*np.pi)
            throw_v_x = v_x_z* np.cos(xz/180*np.pi)
            throw_v_y = throw_v * np.sin(w/180*np.pi)
            throw_v_z = v_x_z* np.sin(xz/180*np.pi)

            if throw_v_x<0.00000000001:
                throw_v_x=0
            if throw_v_z<0.00000000001:
                throw_v_z=0
            next_x = throw_v_x * t
            next_y = throw_v_y * t - 0.5 * g * t**2
            next_z = throw_v_z * t

            if next_y <= 0:
                dones[i] = True
                #print(i,t)
                continue

            trajectories[i].append((next_x, next_y, next_z))

        all_done = dones.all()

        plt.pause(0.01)
        #print(t)
    for i in range(len(angle)):
        print(f"{angle[i]}도로 던졌을 때 간 거리: {((trajectories[i][-1][0]**2+trajectories[i][-1][2]**2)**(1/2)):.2f}m")
    plt.show()

if __name__ == '__main__':
    projectile_graphic()