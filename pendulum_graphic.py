import pygame
from pygame.locals import *
import numpy as np
#import time

#질량, 줄 길이 입력

h = 0.05					#시간 변화
t = v = 0
x = 30*np.pi/180
pen_fm = 0.01				#마찰계수
pen_m = float(input("진자의 질량: "))*0.1
pen_l = float(input("줄의 길이: "))*0.1
play_speed = float(input("배속(50이하): "))
delay = int(50/play_speed)
pen_J = 0.02				#진자의 관성모멘트
pen_g = 9.8
gndCenterX = 300
gndConterY = 20
penLength = pen_l*100*2


#미분방정식 계산
def calcODEFunc(tVal, xVal, vVal):
	return -pen_fm/(pen_m*pen_l*pen_l+pen_J)*vVal-pen_m*pen_g*pen_l/(pen_m*pen_l*pen_l+pen_J)*xVal			#=d^2x/dt^2(각가속도)

#룽게-쿠타 방법으로 미분방정식 풀기
def solveODEusingRK4(t, x, v):

	#v=dx/dt
	#calcODEFFunc의 return = dv/dt
	kx1 = v						#kx1은 현재 각속도 v에 의한 각도 변화량입니다.
	kv1 = calcODEFunc( t, x, v )
	 
	kx2 = v + h*kv1/2			#kx2는 t + h/2 시점에서 각속도 v + h*kv1/2에 의한 각도 변화량입니다.
	kv2 = calcODEFunc( t + h/2, x + h*kx1/2, v + h*kv1/2 )
	 
	kx3 = v + h*kv2/2			#kx3는 t + h/2 시점에서 각속도 v + h*kv2/2에 의한 각도 변화량입니다.
	kv3 = calcODEFunc( t + h/2, x + h*kx2/2, v + h*kv2/2 )
								
	kx4 = v + h*kv3				#kx4는 t + h 시점에서 각속도 v + h*kv3에 의한 각도 변화량입니다
	kv4 = calcODEFunc( t + h, x + h*kx3, v + h*kv3 )
	 
	#중간 변수들의 가중 평균
	dx = h*(kx1 + 2*kx2 + 2*kx3 + kx4)/6		#x(각도)의 증분
	dv = h*(kv1 + 2*kv2 + 2*kv3 + kv4)/6		#v(dx/dt, 각속도)의 증분
    
    
	return x+dx, v+dv

pygame.init()

srf = pygame.display.set_mode((600,600))

font = pygame.font.SysFont('Vernada.ttf', 25)
#aurthorSrf = font.render('by PinkWink', True, (50,50,50))


loopFlag = True


bef2_v=0
bef_v=0

duration=0
while loopFlag:
	duration+=1
	for event in pygame.event.get(QUIT):
		loopFlag = False

	srf.fill((255,255,255))

	t = t + h
	bef2_v=bef_v
	bef_v=v
	x, v = solveODEusingRK4(t,x,v)
	
	if np.abs(bef2_v)<np.abs(bef_v) and np.abs(bef_v)>np.abs(v):
		print("속력의 극대:", np.abs(bef_v))
		if np.abs(bef_v)<0.05:
			loopFlag=False
	updatedX = gndCenterX + penLength*np.sin(x)
	updatedY = gndConterY + penLength*np.cos(x)

	pygame.draw.line(srf, (100,100,100), (gndCenterX, gndConterY), (updatedX, updatedY), 2)
	pygame.draw.circle(srf, (100,100,100), (int(updatedX), int(updatedY)), 10)
    #pygame.draw.circle(srf, (100,100,100), (int(updatedX), int(updatedY)), 10,0)

	pygame.draw.line(srf, (0,0,0), (10,20), (580,20), 10)
	#srf.blit(aurthorSrf, (180,270))

	
	pygame.time.delay(delay)
	pygame.display.flip()

print(f"정지할 때 까지 걸린시간: {duration*0.05:.2f}초")