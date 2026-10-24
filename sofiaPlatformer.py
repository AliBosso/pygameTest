import sys 
import time 
import pygame


#world vars
pygame.init()
running = True
screen = pygame.display.set_mode((1280, 600))
clock = pygame.time.Clock()
dt = 0
velocity = 0

ground_y = 540
onGround = True


#player vars
player = pygame.Surface((20, 50))
player.fill("purple")
player_rect = player.get_rect(topleft=(200, ground_y))


def movement():
    keys = pygame.key.get_pressed()
    global velocity, player, ground_y, onGround 

    if keys[pygame.K_UP] and onGround == True:
        velocity -= 20
        onGround = False    
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    velocity += 1
    player_rect.y += velocity # techincally i dont need teh velocity var but it makes everytihning better for scaling teh project



def collisions():
    global velocity, onGround

    if player_rect.bottom >= ground_y:
        player_rect.bottom = ground_y
        velocity = 0
        onGround = True
    else:
        onGround = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    movement()
    collisions()

    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(60)






