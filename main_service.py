import projectile_graphic
import projectile_non_graphic
import free_fall
import pendulum_graphic
import pendulum_non_delay
import pendulum_graph
#import pygame

while True:
    sel1= int(input('운동의 종류를 선택하세요\n1. 자유 낙하 운동\n2. 포물선 운동\n3. 진자 운동\n'))
    if sel1 == 1:
        free_fall.free_fall()
    elif sel1 == 2:
        sel1_2= int(input('실행할 프로그램의 종류를 선택하세요\n1. 운동 궤적 보기\n2. 최적 각도 찾기\n'))
        if sel1_2 == 1:
            projectile_graphic.projectile_graphic()
        elif sel1_2 == 2:
            projectile_non_graphic.projectile_non_graphic()
        else:
            print('잘못된 입력')
    elif sel1 == 3:
        sel1_3= int(input('실행할 프로그램의 종류를 선택하세요\n1. 운동 시뮬레이션 보기\n2. 멈추는 시간 구하기\n3. 멈추는 시간과 줄의 길이, 진자의 질량 관계 보기\n'))
        if sel1_3 == 1:
            pendulum_graphic.pendulum_graphic()
        elif sel1_3 == 2:
            pendulum_non_delay.pendulum_non_delay()
        elif sel1_3 == 3:
            pendulum_graph.pendulum_graph()
        else:
            print('잘못된 입력')
    else:
        print('잘못된 입력')


