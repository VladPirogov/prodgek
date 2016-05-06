import pygame
directory = "/Users/mmforde1/Desktop/Flappy_Bird/" #Directory where images are loaded from

#Variables for me to tinker
speed = 8
done = False
BLUE = (184, 255, 255)

def game_over():
    pygame.quit()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(directory+"images/sprites/bird/bird.jpg"), [68, 48])

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        self.rect.y = 100
        self.rect.x = 100
        self.direction = False

    def jump(self):
        #Prepare variables used for jumping
        self.direction = True
        self.old_height = self.rect.y

    def calc_grav(self):
        if self.direction == False: #Fall
            self.rect.y += speed
        if self.direction == True: #Deal with jumping
            self.rect.y -= speed
            if self.old_height - 50 > self.rect.y:
                self.direction = False

    def update(self):
        self.calc_grav() #Calculate gravity
        if pygame.sprite.collide_rect(player_group, obstacles_group): #Detect if obstacle was hit
            game_over()

class Ground(pygame.sprite.Sprite):
    def __init__(self): #Create sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(directory+"images/sprites/ground.jpg"), [320, 96])

        #Get reference to he image rect
        self.rect = self.image.get_rect()

        self.rect.y = 616
        self.rect.x = 0

pygame.init()

# Set the height and width of the screen
size = [600, 712]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

#Sprite groups
player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
active_sprite_list = pygame.sprite.Group()

# Create the player
player = Player()
player_group.add(player)
active_sprite_list.add(player)

#Load other sprites
ground = Ground()
obstacles_group.add(ground)
active_sprite_list.add(ground)

screen.fill(BLUE)

#Main program loop
while not done:
    player.update()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
    screen.fill(BLUE)

    # Update the player.
    active_sprite_list.update()

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    active_sprite_list.draw(screen)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    clock = pygame.time.Clock()

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()