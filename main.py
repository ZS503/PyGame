import pygame  # pyright: ignore[reportMissingImports]
import random
pygame.init()


window=pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Temp caption")

player = pygame.surface.Surface((100,100))
player.fill((255,255,255))
player = pygame.image.load("imgs\LittleGuy.png").convert_alpha()
player = pygame.transform.scale(player, (300,300))
player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

rising_object = pygame.surface.Surface((50,50))
rising_object.fill((255,255,255))

rising_object_x = 0
rising_object_y = 0
rising_object_vel_x = 0
rising_object_vel_y = 0
while True:

    #take input
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  quit(0)
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_vel_x = -0.2
                    if event.key == pygame.K_RIGHT:
                        player_vel_x = 0.2
            else:
                  player_vel_x = 0
                  player_vel_y = 0
    if rising_object_y >= window.height:
          rising_object_y = 0;
          rising_object_x = random.randint(0,window.width - 50)
    #output
    window.fill((255,255,255))

    player_x += player_vel_x
    player_y += player_vel_y
    window.blit(player, (player_x, player_y))
    window.blit(rising_object, (rising_object_x,rising_object_y))

    rising_object_x += rising_object_vel_x
    rising_object_y += rising_object_vel_y
    window.blit(rising_object, (rising_object_x, rising_object_y))
    pygame.display.flip()