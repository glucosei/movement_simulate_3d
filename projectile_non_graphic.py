import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D


def projectile_non_graphic():
    g = 9.80665
    dt = 0.01
    num= int(90*(1/dt))
    log=[0 for i in range(num+1)]

    throw_v = float(input("초기 속도(m/s): "))
    xz = float(input("xz평면에 내린 수선의 발과 원점을 이은 직선과 x축이 이루는 각도(°): "))


    done = False

    distance=0
    for i in range(10,num+1):
        w= i/(num/90)
        v_x_z= throw_v * np.cos(w/180*np.pi)
        throw_v_x = v_x_z* np.cos(xz/180*np.pi)
        throw_v_y = throw_v * np.sin(w/180*np.pi)
        throw_v_z = v_x_z* np.sin(xz/180*np.pi)
        done=False
        trajectories = [(0, 0, 0)] 
        t=0
        while not done:
            t = t + dt

            
            last_x, last_y, last_z = trajectories[-1]
            """0.1*dt
            next_x = last_x + throw_v_x * math.cos(w / 180 * np.pi) * t
            next_y = last_y + throw_v * math.sin(w / 180 * np.pi) * t - 0.5 * g * t**2
            next_z = last_z + throw_v_z * math.cos(w / 180 * np.pi) * t
            """

            next_x = throw_v_x * t
            next_y = throw_v_y * t - 0.5 * g * t**2
            next_z = throw_v_z  * t

            if next_y <= 0:
                done = True
                distance=(last_x**2+last_z**2)**(1/2)
                continue

            trajectories.append((next_x, next_y, next_z))
        log[i]=distance     #최종 간 거리
        print(w, distance)
    print('#'*20)
    print(f"가장 멀리 갔을 때의 던진 각도: {log.index(max(log))/(num/90)}도\n그 때 간 거리: {max(log):.2f}m")




    plt.show()



if __name__ == '__main__':
    projectile_non_graphic()