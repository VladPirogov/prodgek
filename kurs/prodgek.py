import time
import math
import random
import pygame

zetT=False
def game(self):
    global zetT
    size=(700, 530)
    white=(255, 255, 255)
    black=(0, 0, 0)
    red=(255,0, 0)
    blue=(0, 0, 255)
    green=(0, 255, 0)
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("firefighter")
    Is=pygame.Surface((700,30))
    pygame.font.init()
    done=False
    clock=pygame.time.Clock()
    info=pygame.font.Font(None,32)
    i=0
    zetT=False
    chance_human=40
    chance_stone=150
    maxT=0
    f = open('Record lis', 'a')
    #sound = pygame.mixer.Sound("C:\\Users\\Влад\\Desktop\\python\\kurs\\iponomaty.wav")
    #класс игрока
    class You(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("batut.gif").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
        def left(self):
            self.rect.x -= 10
            if self.rect.x<0:
                self.rect.x=self.rect.x+10
        def right(self):
            self.rect.x += 10
            if self.rect.x>400:
                self.rect.x=self.rect.x-10
    #класс людей
    class people(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("fp1.png").convert()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()

        def update (self):
            global zetT
            self.rect.y =self.rect.y + random.randrange(3,8)
            if self.rect.y > size[1]:
                zetT = True

    class stone(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("ston.png").convert_alpha()
            self.image.set_colorkey(white)
            self.rect = self.image.get_rect()
        def update (self):
            self.rect.y =self.rect.y + random.randrange(3,8)
    #Создал списки
    people_list = pygame.sprite.Group()
    stone_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    #создал батут
    player =You()
    player.rect.x=0
    player.rect.y=420
    all_sprites_list.add(player)
    ston= False
    background=pygame.image.load("fon.jpg").convert()
    sh=30
    t=0
    pygame.key.set_repeat(1,1)
    #главный цикл игры
    pygame.key.set_repeat(1,1)
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN:
                if not zetT and event.key==pygame.K_LEFT:
                    player.left()
                if not zetT and event.key==pygame.K_RIGHT:
                    player.right()
        people_hit_list = pygame.sprite.spritecollide(player, people_list, True)
        if len(people_hit_list) > 0:
            t +=len(people_hit_list)
            if t> maxT:
                maxT=t
        #люди
        if i%chance_human==0:
            pp=people()
            zx=int(random.randrange(20,480))
            zy=int(0-150)
            pp.rect.x = zx
            pp.rect.y =zy
            people_list.add(pp)
            all_sprites_list.add(pp)
        i=random.randint(1,150)
        if len(people_list) > 0  and  zetT==False:
            people_list.update()
        #для камня
        if t<0 and not zetT :
            zetT=True
        if t>15:
            ston= True
        if ston==True and len(stone_list)>0 and zetT==False:
            stone_list.update()
        if len(stone_list)>1:
            for istone in stone_list:
                if istone.rect.y > size[1]:
                    istone.remove()
        if i%chance_stone==0 and ston==True:
            ss=stone()
            zx=int(random.randrange(20,480))
            zy=int(0-150)
            ss.rect.x = zx
            ss.rect.y =zy
            stone_list.add(ss)
            all_sprites_list.add(ss)
        stone_hit_list = pygame.sprite.spritecollide(player,stone_list, True)
        t=t-(15*(len(stone_hit_list)))
        screen.blit(background, (0,0))
        all_sprites_list.draw(screen)
        Is.fill((45,88,40))
        Is.blit(info.render("point: "+ str(t),1,(0,0,200)),(0,0))
        screen.blit(Is,(0,500))
        pygame.display.flip()
        clock.tick(24)
    f.write(str(maxT) + '\n')
    pygame.QUIT()
    pygame.font.quit()
    f.close()
    return