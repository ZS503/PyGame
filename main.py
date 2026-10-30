import pygame  # pyright: ignore[reportMissingImports]
pygame.init()


window=pygame.display.set_mode((800,600))
window.fill(0,0,0)
pygame.display.set_caption("Temp caption")

player = pygame.surface.Sufrace((100,100))
player.fill((255,255,255))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

falling_object = pygame.surface.Sufrace((50,50))
falling_object.fill((255,255,255))

falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0
while True:

    #take input
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  quit(0)
    #output
    window.fill((255,255,255))

    window.blit(player, dest=(player_x, player_y))
    window.blit(falling_object, dest= (falling_object_x,falling_object_y))
    pygame.display.flip()