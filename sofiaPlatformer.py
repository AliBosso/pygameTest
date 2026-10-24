import sys 
import time 


#world vars
pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
velocity = 0


#player vars
player_idle = pygame.image.load("img.png")
player = player_idle



def movemnt():
    keys = pygame.key.get_pressed
    global velocity 

    if keys[K_up]:
        velocity -= 20



while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False 







