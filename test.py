# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
eye_pos = pygame.Vector2(player_pos.x+10, player_pos.y-10)


def  moving():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      player_pos.y -= 300 * dt
      eye_pos.y -= 300 * dt
  if keys[pygame.K_s]:
      player_pos.y += 300 * dt
      eye_pos.y += 300 * dt
  if keys[pygame.K_a]:
      player_pos.x -= 300 * dt
      eye_pos.x -= 300 * dt
  if keys[pygame.K_d]:
      player_pos.x += 300 * dt
      eye_pos.x += 300 * dt

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    circle = pygame.draw.circle(screen, "red", player_pos, 40)
    eye = pygame.draw.circle(screen, "black", eye_pos, 5)
    moving()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()
