import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

g = 9.80665
dt = 0.01
num= 9000
log=[0 for i in range(num+1)]

throw_v_x = int(input("x축 방향으로의 속도: "))
throw_v_z = int(input("z축 방향으로의 속도: "))
throw_v = (throw_v_x**2+throw_v_z**2)**(1/2)
print(throw_v)
done = False

distance=0
for i in range(10,num+1):
    w= i/(num/90)
    done=False
    trajectories = [(0, 0, 0)] 
    t=0
    while not done:
        t = t + dt

        
        last_x, last_y, last_z = trajectories[-1]

        next_x = last_x + throw_v_x * math.cos(w / 180 * np.pi) * t
        next_y = last_y + throw_v * math.sin(w / 180 * np.pi) * t - 0.5 * g * t**2
        next_z = last_z + throw_v_z * math.cos(w / 180 * np.pi) * t

        if next_y <= 0:
            done = True
            distance=(last_x**2+last_z**2)**(1/2)
            continue

        trajectories.append((next_x, next_y, next_z))
    log[i]=distance     #최종 간 거리
    print(w, distance*dt)
print('#'*20)
print(f"가장 멀리 갔을 때의 던진 각도: {log.index(max(log))/(num/90)}도\n그 때 간 거리: {max(log)*dt:.2f}m")




plt.show()
