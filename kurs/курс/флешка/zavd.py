import pygame
x = 1000
y = 1000
size = (x,y)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("first progect")
done = False
clock = pygame.time.Clock()
background = pygame.image.load("Koala.jpg").convert()
hero = pygame.image.load("Snimok.png").convert()
hero1 = pygame.image.load("2.png").convert()

def draw_hero(pos,size,color1,color2,color3):
    pygame.draw.circle(screen,color1,pos,size)
    pygame.draw.circle(screen,color2,(pos[0],pos[1]+int(size/5)),int(size*3/5))
    pygame.draw.circle(screen,color1,pos,int(size*3/5))
    pygame.draw.circle(screen,color3,(pos[0]+int(size*2/5),pos[1]-int(size*2/5)),int(size/5))
    pygame.draw.circle(screen,color3,(pos[0]-int(size*2/5),pos[1]-int(size*2/5)),int(size/5))
i = 0
sh=50
xh = int(size[0]/2)
yh = int(size[1]/2)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xh =xh -10
            if event.key == pygame.K_RIGHT:
                xh = xh +10
            if event.key == pygame.K_UP:
                yh = yh -10
            if event.key == pygame.K_DOWN:
                yh = yh +10
            if event.key == pygame.K_s:
                sh=sh-5
            if event.key == pygame.K_b:
                sh=sh+5
    screen.blit(background,(0,0))
    screen.blit(hero1,(xh,yh))



    pygame.display.flip()
    clock.tick(60)


pygame.QUIT
