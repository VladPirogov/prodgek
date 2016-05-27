import time
import math
import random
import pygame
size=(700, 530)
white=(255, 255, 255)
black=(0, 0, 0)
red=(255,0, 0)
blue=(0, 0, 255)
green=(0, 255, 0)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("firefighter")
Is=pygame.Surface((500,30))
done=False
clock=pygame.time.Clock()
i=0
k=1
hero=pygame.image.load("batut.gif").convert()
background=pygame.image.load("fon.jpg").convert()
zet=pygame.image.load("fp.gif").convert()
zet1=pygame.image.load("fp.gif").convert()
zet.set_colorkey(white)
hero.set_colorkey(white)
zetT=True
def collision(s1x,s2x,s1y,s2y):
    if (s1x>=s2x) and (s1x<=s2x+300) and (s1y>s2y-176) and (s1y<s2y+176):
        return 1
    else:
        return 0
xh=int(0)
yh=int(420)
zx=int(300)
zy=int(0)-100
#zx1=int(300)
#zy=int(0)-120
sh=30
pygame.key.set_repeat(1,1)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if  event.key==pygame.K_LEFT:
                hero=pygame.image.load("batut.gif").convert()
                xh=xh-10
                if xh<0:
                    xh= xh+10
                hero.set_colorkey(white)
            if event.key==pygame.K_RIGHT:
                hero=pygame.image.load("batut.gif").convert()
                xh=xh+10
                if xh>420:
                    xh= xh-10
                hero.set_colorkey(white)
    if collision(zx,xh,zy,yh)==True:
        zy=0-110
        zx = random.randint(50,550)
        k=random.randint(2,6)
    zy=zy+k
    if collision(zx,xh,zy,yh)==True:
        zy=0-110
        zx = random.randint(50,550)
        k=random.randint(2,6)
    zy1=zy+k
    screen.blit(zet,(zx,zy))
    #screen.blit(zet,(zx1,zy1))
    screen.blit(background, (0,0))
    screen.blit(hero, (xh, yh))
    screen.blit(zet,(zx,zy))
    screen.blit(Is,(0,500))
    Is.fill((45,88,40))
    pygame.display.flip()
    clock.tick(60)
pygame.QUIT()