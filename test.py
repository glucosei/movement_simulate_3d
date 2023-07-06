import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D   #3D module


# Env physics
g = 9.80665
dt = 0.1
t = 0

angle = np.array([15, 30, 45, 60])    #각도들 리스트
throw_v = 20                          #던지는 속도
trajectories = [[(0,0,0)] for i in range(len(angle))]   #위치 기록 (x,y,z)형식의 튜플이 시간과 각도에 따라 2차원으로 배열됨
dones = np.zeros_like(angle, dtype=bool)                #각도별 도착 여부 리스트
all_done = False                      #다 True면 True가 됨

#fig, ax = plt.subplots(projection='3d')       #fig라는 figure에 ax라는 plt
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

while(not all_done):                        #다 도착하기 전까지
  ax.cla()                                  #ax를 clear
  ax.set_title("Throw the ball!")           #ax title 설정
  ax.set_xlim(-1, 600 )                     #x한계 설정
  ax.set_ylim(-1, 600)                      #y한계 설정
  ax.set_zlim(-1, 200)


  for i in range(len(angle)):               #각도별 현재 위치 찍기
    x, y, z = zip(*trajectories[i])         #
    ax.scatter(x,z,y, label=angle[i])       #찍기
  ax.legend()                               #범례

  t = t + dt

  for i in range(len(angle)):
    last_x, last_y,last_z = trajectories[i][-1]
    w = angle[i]

    next_x, next_y = last_x + throw_v*math.cos(w/180 *3.14), last_y + throw_v*math.sin(w/180 *3.14) - g * t
    next_z= last_z + 15

    if next_y <= 0:
      dones[i] = True
      continue

    trajectories[i].append((next_x, next_y, next_z))

  all_done = dones.all()

  plt.pause(0.01)

plt.show()