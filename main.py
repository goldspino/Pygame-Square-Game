import pygame
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('First game')
x = 300
y = 200
SPEED = 30
while True:
  pygame.time.delay(100)
  screen.fill((0,250,0))
  for event in pygame.event.get():
    if event.type ==  pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    x = x + SPEED
  if keys [pygame.K_LEFT]:
    x = x - SPEED
  if keys[pygame.K_UP]:
    y = y - SPEED
  if keys[pygame.K_DOWN]:
    y = y + SPEED
  print(x)
  pygame.draw.rect(screen, (0,250,200),(x,y,90,90))

  pygame.display.update()
pygame.quit()