def moving():
  global velocity_y, on_ground  # NEW: on_ground added
  keys = pygame.key.get_pressed()
  previous_bottom = player_rect.bottom
  previous_top = player_rect.top
  previous_left = player_rect.left
  previous_right = player_rect.right

  # JUMP: CHANGED: uses on_ground so you can also jump from the box
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
