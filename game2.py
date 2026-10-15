import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Sprites
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, screen.get_size())

spikes = pygame.image.load("spike.png")

# Load both player directions
player_right_img = pygame.image.load("player.png")
player_right_img = pygame.transform.scale(player_right_img, (40, 100))

player_left_img = pygame.image.load("player-left.png")
player_left_img = pygame.transform.scale(player_left_img, (40, 100))

player_idle_img = pygame.image.load("idle.png")
player_idle_img = pygame.transform.scale(player_idle_img, (40, 100))

# Set the active player image to start facing right
player = player_right_img


# player vars
ground_y = 590
velocity_y = 1
on_ground = False
alive = True  # FIXED: Needs to be global so functions can change it

player_start = 50
player_rect = player.get_rect(midbottom=(player_start, ground_y))

level = 0
spikes_rect = spikes.get_rect() # CHANGED: Initialize the rect globally so collision detection can see it


font = pygame.font.SysFont(None, 48)

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

def spikes_func():#loops through the objetc list with the positions for the hitboxes, adn then in .blit(image var, pos of the hitbox)
    if level == 1:
        for spike in spikes_rects:
            screen.blit(spikes, spike)
    elif level == 2:
        for spike in spikes_rects2:
            screen.blit(spikes, spike)


# Create these right next to where you defined your boxes and boxes2 lists
spikes_rects = [
    pygame.Rect((920, 400 - 30), (30, 30)),     # Level 1 Spike on the box (Adjust 30, 30 to your image size)
    pygame.Rect((400, ground_y - 30), (30, 30)), # Level 1 Spike on the ground
]

spikes_rects2 = [
    pygame.Rect((600, ground_y - 30), (30, 30)), # Level 2 Spike on the ground
]



def levels():
    global level, boxes
    if player_rect.x >= 1250:
        player_rect.midbottom = (player_start, ground_y) # FIXED: Safely snaps player back to ground
        level += 1
        if level == 1:
            boxes.clear()
        if level == 2:
            boxes2.clear()
    elif player_rect.x <= 25:
        player_rect.midbottom = (player_start, ground_y)

def moving():
    global velocity_y, on_ground, player  # Added player to globals
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
        player_rect.x -= 5
        player = player_left_img   # Switch to left image
    elif keys[pygame.K_RIGHT]:     # Use elif so right takes priority or handles movement smoothly
        player_rect.x += 5
        player = player_right_img  # Switch to right image\
    elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        player = player_idle_img

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
    
    if level == 1:
        for spike in spikes_rects:
            if player_rect.colliderect(spike):
                alive = False
                
    elif level == 2:
        for spike in spikes_rects2:
            if player_rect.colliderect(spike):
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
            
    moving() # FIXED: Added back to loop
    living()
    levels()  



    level_text = "Level: " + str(level)
    text_surface = font.render(level_text, True, "White")
    # Drawing Everything
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (50, 50))

    for box in boxes:
        objects("dark green", box.topleft, box.size)

    if level == 1:
        for box2 in boxes2:
            objects("dark red", box2.topleft, box2.size)
        spikes_func() # Render spikes
    if level == 2:
        spikes_func()
        
    screen.blit(player, player_rect)

    is_touching_danger()

    pygame.display.flip()
    clock.tick(65) 

