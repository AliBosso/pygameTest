import sys 
import time 
import pygame


#world vars
pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
velocity = 0

ground_y = 540
onGround = True


#player vars
try:
    player_idle = pygame.image.load("img.png")
    player = player_idle
except:
    player = pygame.draw.rect(screen, "purple", (200, ground_y, 20, 50))


def movement():
    keys = pygame.key.get_pressed
    global velocity, player, ground_y, onGround 

    if keys[K_UP]:
        velocity -= 20
        onGround = False    
    if keys[K_LEFT]:
        player.x -= 5
    if keys[K_RIGHT]:
        player.x += 5

    velocity += 1
    player.y += velocity # techincally i dont need teh velocity var but it makes everytihning better for scaling teh project








while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    movement()
    
    screen.fill("blue")#bg color

    pygame.display.flip()
    screen.blit(player)
pygame.quit()
sys.exit()







