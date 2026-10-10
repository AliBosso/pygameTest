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

player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (40, 100))
player_rect = player.get_rect(midbottom=(640, ground_y))


#player vars
temp_posx = player_rect.x
temp_posy = player_rect.y



def levels():
    if (player_rect.x <= 1250):
        player_rect.x = 640
        player_rect.y = ground_y



def moving():
  global velocity_y, on_ground  # NEW: on_ground added
  keys = pygame.key.get_pressed()
  previous_bottom = player_rect.bottom
  previous_top = player_rect.top
  previous_left = player_rect.left
  previous_right = player_rect.right

  if keys[pygame.K_UP] and on_ground:
    velocity_y = -20
  # LEFT / RIGHT
  if keys[pygame.K_LEFT]:
    player_rect.x -= 5
  if keys[pygame.K_RIGHT]:
    player_rect.x += 5

  velocity_y += 1 # NEW: where the feet were before moving
  player_rect.y += velocity_y
  on_ground = False  # NEW: assume in the air until a check says otherwise

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
    on_ground = True  # NEW


def objects(color, position,size):
  pygame.draw.rect(screen, color, pygame.Rect(position, size))
boxes = [
    pygame.Rect((600, 400), (100, 50)),
    pygame.Rect((400, 400), (100, 50)),
  ]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    moving()

    screen.blit(background, (0, 0))
    for box in boxes:
      objects("dark Green", box.topleft, box.size)
    screen.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(144)
    dt = clock.tick(144) / 1000

pygame.quit()
