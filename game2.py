import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Sprites
# For testing purposes, substitute fallback surfaces if images are missing
# Sprites
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, screen.get_size())

spikes = pygame.image.load("spike.png")

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (40, 100))

# player vars
ground_y = 590
velocity_y = 1
on_ground = False
alive = True  # FIXED: Needs to be global so functions can change it

player_start = 50
player_rect = player.get_rect(midbottom=(player_start, ground_y))

level = 0
spikes_rect = spikes.get_rect() # CHANGED: Initialize the rect globally so collision detection can see it

def objects(color, position, size):
    pygame.draw.rect(screen, color, pygame.Rect(position, size))

boxes = [
    pygame.Rect((600, 450), (100, 50)),
    pygame.Rect((400, 450), (100, 50)),
]

boxes2 = [
    pygame.Rect((900, 400), (100, 50)),
    pygame.Rect((700, 450), (100, 50)),
]

def spikes_func():
    global spikes_rect
        # Properly position the spike rect
    spikes_rect.topleft = (400, ground_y - spikes_rect.height) # FIXED: Subtract height so it sits on top of the ground
    screen.blit(spikes, spikes_rect)  # FIXED: Added the missing blit to actually show the spike

def levels():
    global level, boxes
    if player_rect.x >= 1250:
        player_rect.midbottom = (player_start, ground_y) # FIXED: Safely snaps player back to ground
        level += 1
        if level == 1:
            boxes.clear()
        if level == 2:
            boxes2.clear()

def moving():
    global velocity_y, on_ground  
    keys = pygame.key.get_pressed()
    
    # Store old positions for collision checks
    previous_bottom = player_rect.bottom
    previous_top = player_rect.top
    previous_left = player_rect.left
    previous_right = player_rect.right

    if keys[pygame.K_UP] and on_ground:
        velocity_y = -18
        on_ground = False 
    if keys[pygame.K_LEFT]:
        player_rect.x -= 20
    if keys[pygame.K_RIGHT]:
        player_rect.x += 20

    # Apply Gravity
    velocity_y += 1 
    player_rect.y += velocity_y

    # FIXED: Check ground collision FIRST before box checks
    if player_rect.bottom >= ground_y:
        player_rect.bottom = ground_y
        velocity_y = 0
        on_ground = True

    # Check Box 1 Collisions
    for box in boxes:
        if player_rect.colliderect(box):
            if velocity_y >= 0 and previous_bottom <= box.top:
                player_rect.bottom = box.top
                velocity_y = 0
                on_ground = True
            elif velocity_y < 0 and previous_top >= box.bottom:
                player_rect.top = box.bottom
                velocity_y = 0
            elif previous_right <= box.left:
                player_rect.right = box.left
            elif previous_left >= box.right:
                player_rect.left = box.right
    
    # Check Box 2 Collisions (Only active on Level 1)
    if level == 1:
        for box2 in boxes2:
            if player_rect.colliderect(box2):
                if velocity_y >= 0 and previous_bottom <= box2.top:
                    player_rect.bottom = box2.top
                    velocity_y = 0
                    on_ground = True
                elif velocity_y < 0 and previous_top >= box2.bottom:
                    player_rect.top = box2.bottom
                    velocity_y = 0
                elif previous_right <= box2.left:
                    player_rect.right = box2.left
                elif previous_left >= box2.right:
                    player_rect.left = box2.right

def is_touching_danger():
    global alive
    # FIXED: Re-enabled and checked against spikes_rect instead of the raw image
    if level == 1 and player_rect.colliderect(spikes_rect):
        alive = False

def living():
    global alive
    if not alive:
        player_rect.midbottom = (player_start, ground_y)  # Reset player position
        velocity_y = 0
        alive = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    moving()
    is_touching_danger() # FIXED: Added back to loop
    living()
    levels()  
    
    # Drawing Everything
    screen.blit(background, (0, 0))
    
    for box in boxes:
        objects("dark green", box.topleft, box.size)

    if level == 1:
        for box2 in boxes2:
            objects("dark red", box2.topleft, box2.size)
        spikes_func() # Render spikes
        
    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(144) 

