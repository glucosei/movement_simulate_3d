import pygame
from pygame.locals import *
import numpy as np
import matplotlib.pyplot as plt
#import time

#질량, 줄 길이 입력
#둘중 하나 입력, 하나는 바꿈


result = [[ ],[ ]]

choice = input("정하고자 하는 변수를 입력하세요(1: 진자의 질량, 2: 줄의 길이)\n")
if choice == '1':
    pen_m = float(input("진자의 질량: "))*0.1
    pen_l_range = list(map(int, input("줄의 자연수 길이의 범위(시작 끝): ").split(' ')))
    for i in range(pen_l_range[0],pen_l_range[1]+1):
        pen_l = i*0.1
        h = 0.05
        t = v = 0
        x = 30*np.pi/180
        pen_fm = 0.01
        pen_J = 0.02
        pen_g = 9.8
        gndCenterX = 300
        gndConterY = 20
        penLength = pen_l*100*2
        #print(penLength, pen_m)
        
        #미분방정식 표현
        def calcODEFunc(tVal, xVal, vVal):
            return -pen_fm/(pen_m*pen_l*pen_l+pen_J)*vVal-pen_m*pen_g*pen_l/(pen_m*pen_l*pen_l+pen_J)*xVal

            #룽게-쿠타 방법으로 미분방정식 풀기
        def solveODEusingRK4(t, x, v):
            kx1 = v
            kv1 = calcODEFunc( t, x, v )
                
            kx2 = v + h*kv1/2
            kv2 = calcODEFunc( t + h/2, x + h*kx1/2, v + h*kv1/2 )
                
            kx3 = v + h*kv2/2
            kv3 = calcODEFunc( t + h/2, x + h*kx2/2, v + h*kv2/2 )
            kx4 = v + h*kv3
            kv4 = calcODEFunc( t + h, x + h*kx3, v + h*kv3 )
                
            dx = h*(kx1 + 2*kx2 + 2*kx3 + kx4)/6
            dv = h*(kv1 + 2*kv2 + 2*kv3 + kv4)/6
                
                
            return x+dx, v+dv



        loopFlag = True


        bef2_v=0
        bef_v=0

        duration=0
        while loopFlag:
            duration+=1


            t = t + h
            bef2_v=bef_v
            bef_v=v
            x, v = solveODEusingRK4(t,x,v)
            
            if np.abs(bef2_v)<np.abs(bef_v) and np.abs(bef_v)>np.abs(v):
                #print("속력의 극대:", np.abs(bef_v))
                if np.abs(bef_v)<0.05:
                    loopFlag=False
            updatedX = gndCenterX + penLength*np.sin(x)
            updatedY = gndConterY + penLength*np.cos(x)



        print(f"길이: {int(pen_l*10)}, 정지할 때 까지 걸린시간: {duration*0.05:.2f}")
        result[0].append(int(pen_l*10))
        result[1].append(duration*0.05)

elif choice == '2':
    pen_m_range = list(map(int, input("진자의 자연수 질량의 범위(시작 끝): ").split(' ')))
    pen_l = float(input("줄의 길이: "))*0.1

    for i in range(pen_m_range[0],pen_m_range[1]+1):
        pen_m = i*0.1
        h = 0.05
        t = v = 0
        x = 30*np.pi/180
        pen_fm = 0.01
        pen_J = 0.02
        pen_g = 9.8
        gndCenterX = 300
        gndConterY = 20
        penLength = pen_l*100*2



        #미분방정식 표현
        def calcODEFunc(tVal, xVal, vVal):
            return -pen_fm/(pen_m*pen_l*pen_l+pen_J)*vVal-pen_m*pen_g*pen_l/(pen_m*pen_l*pen_l+pen_J)*xVal

            #룽게-쿠타 방법으로 미분방정식 풀기
        def solveODEusingRK4(t, x, v):
            kx1 = v
            kv1 = calcODEFunc( t, x, v )
                
            kx2 = v + h*kv1/2
            kv2 = calcODEFunc( t + h/2, x + h*kx1/2, v + h*kv1/2 )
                
            kx3 = v + h*kv2/2
            kv3 = calcODEFunc( t + h/2, x + h*kx2/2, v + h*kv2/2 )
            kx4 = v + h*kv3
            kv4 = calcODEFunc( t + h, x + h*kx3, v + h*kv3 )
                
            dx = h*(kx1 + 2*kx2 + 2*kx3 + kx4)/6
            dv = h*(kv1 + 2*kv2 + 2*kv3 + kv4)/6
                
                
            return x+dx, v+dv


        loopFlag = True


        bef2_v=0
        bef_v=0

        duration=0
        while loopFlag:
            duration+=1
            """
            for event in pygame.event.get(QUIT):
                loopFlag = False
            """
            #srf.fill((255,255,255))

            t = t + h
            bef2_v=bef_v
            bef_v=v
            x, v = solveODEusingRK4(t,x,v)
            
            if np.abs(bef2_v)<np.abs(bef_v) and np.abs(bef_v)>np.abs(v):
                #print("극대:", np.abs(bef_v))
                if np.abs(bef_v)<0.05:
                    loopFlag=False
            updatedX = gndCenterX + penLength*np.sin(x)
            updatedY = gndConterY + penLength*np.cos(x)

            #pygame.draw.line(srf, (100,100,100), (gndCenterX, gndConterY), (updatedX, updatedY), 2)
            #pygame.draw.circle(srf, (100,100,100), (int(updatedX), int(updatedY)), 10)
            #pygame.draw.circle(srf, (100,100,100), (int(updatedX), int(updatedY)), 10,0)

            #pygame.draw.line(srf, (0,0,0), (10,20), (580,20), 10)
            #srf.blit(aurthorSrf, (180,270))

            #1프레임=4/100초=0.04초
            #pygame.time.delay(40)
            #pygame.display.flip()

        print(f"질량: {int(pen_m*10)}, 정지할 때 까지 걸린시간: {duration*0.05:.2f}")
        result[0].append(int(pen_m*10))
        result[1].append(duration*0.05)

else:
    print('잘못된 입력')




plt.plot(result[0], result[1], 'ro')
plt.ylabel('time taken')
if choice == '1':
    plt.xlabel('length of string')
elif choice == '2':
    plt.xlabel('mass of pendulum')
plt.show()