import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, screen.get_size())

ground_y = 590
velocity_y = 1
on_ground = False


#player vars

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (40, 100))
player_start = 50
player_rect = player.get_rect(midbottom=(player_start, ground_y))
temp_posx = player_rect.x
temp_posy = player_rect.y


level = 0

boxes = [
    pygame.Rect((600, 400), (100, 50)),
    pygame.Rect((400, 400), (100, 50)),
]

def levels():
    global level, boxes  # FIXED: Added global keywords so we can change level and boxes
    if player_rect.x >= 1250:
        player_rect.x = player_start  # Moved player back to the left side instead of middle
        level += 1
        
        # FIXED: Update boxes based on the new level
        if level == 1:
            boxes.clear()  # This removes all the boxes for level 1
            # If you want new boxes for level 1 instead, you could do:
            # boxes = [pygame.Rect((200, 300), (100, 50))]

def moving():
    global velocity_y, on_ground  
    keys = pygame.key.get_pressed()
    previous_bottom = player_rect.bottom
    previous_top = player_rect.top
    previous_left = player_rect.left
    previous_right = player_rect.right

    if keys[pygame.K_UP] and on_ground:
        velocity_y = -20
    # LEFT / RIGHT
    if keys[pygame.K_LEFT]:
        player_rect.x -= 15
    if keys[pygame.K_RIGHT]:
        player_rect.x += 15

    velocity_y += 1 
    player_rect.y += velocity_y
    on_ground = False  

    # FLOOR:
    for box in boxes:
        # land on top
        if (velocity_y >= 0 and previous_bottom <= box.top and player_rect.colliderect(box)):
            player_rect.bottom = box.top
            velocity_y = 0
            on_ground = True

        # hit the bottom
        if (velocity_y < 0 and previous_top >= box.bottom and player_rect.colliderect(box)):
            player_rect.top = box.bottom
            velocity_y = 0

        # left side
        if (previous_right <= box.left and player_rect.colliderect(box)):
            player_rect.right = box.left

        # right side
        if (previous_left >= box.right and player_rect.colliderect(box)):
            player_rect.left = box.right

    if player_rect.bottom >= ground_y:
        player_rect.bottom = ground_y
        velocity_y = 0
        on_ground = True  

def objects(color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position, size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    levels()  # Checks for level up and handles removing/changing boxes
    moving()
    screen.blit(background, (0, 0))
    
    for box in boxes:
        objects("dark Green", box.topleft, box.size)
        
    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(1000)
    dt = clock.tick(100) / 1000  # Delta time in seconds.

pygame.quit()

