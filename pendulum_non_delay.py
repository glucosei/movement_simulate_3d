import pygame
from pygame.locals import *
import numpy as np
#import time

#질량, 줄 길이 입력
#

h = 0.05
t = v = 0
x = 30*np.pi/180
pen_fm = 0.01
pen_m = float(input("진자의 질량: "))*0.1
pen_l = float(input("줄의 길이: "))*0.1
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

#pygame.init()

#srf = pygame.display.set_mode((600,600))

#font = pygame.font.SysFont('Vernada.ttf', 25)
#aurthorSrf = font.render('by PinkWink', True, (50,50,50))


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
		print("속력의 극댓값:", np.abs(bef_v))
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

print(f"정지할 때 까지 걸린시간: {duration*0.05:.2f}")