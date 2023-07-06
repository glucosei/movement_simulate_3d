"""
작성자: 임재욱
추가 기능: 3차원에서의 포물선 운동
주의사항(지우지 말고 적을 거 있으면 아래다가 쭉 적어줘):
1. 우리가 생각하는 z축이 이 모듈에서 y축임. 변수는 우리가 일상적으로 생각하는 것으로 해놓았음
2. 점을 추가해나가는 것이 아니라 이때까지 있었던 모든 점을 계속 찍는 방식임
"""



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
  ax.set_ylim(-1, 600)                      #y한계 설정(우리가 일상적으로 z라고 생각하는 축)
  ax.set_zlim(-1, 200)


  for i in range(len(angle)):               #각도별 현재 위치 찍기
    x, y, z = zip(*trajectories[i])         #trajectories에서 i(특정 각도)라는 인덱스를 가지는 애를 뽑아서 묶음
    ax.scatter(x,z,y, label=angle[i])       #찍기
  ax.legend()                               #범례

  t = t + dt                                #시간 증가

  for i in range(len(angle)):               #각도별 다음 위치 저장, (x,y,z)형의 튜플 형식
    last_x, last_y,last_z = trajectories[i][-1]
    w = angle[i]

    next_x = last_x + throw_v*math.cos(w/180 *np.pi)
    next_y = last_y + throw_v*math.sin(w/180 *np.pi) - g * t
    next_z= last_z + throw_v*math.cos(w/180 *np.pi)

    if next_y <= 0:                         #땅에 도착했는지 검사
      dones[i] = True
      continue                              #이동한 결과가 땅을 뚫고 들어가는 것이면 continue(append하지 않음)

    trajectories[i].append((next_x, next_y, next_z))

  all_done = dones.all()                    #dones의 모든 원소가 True면

  plt.pause(0.01)

plt.show()