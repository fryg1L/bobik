import pygame
from pygame.locals import *
from clouds import cloud
from buttons import Button


pygame.init()
size = 1200, 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Динозаврик')


main_surface = pygame.image.load('sprites/background.png')
ground_surface = pygame.image.load('sprites/ground.png')


pygame.display.flip()

decor_sprites = pygame.sprite.Group()
cloud = cloud()
decor_sprites.add(cloud)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(main_surface, (0, 0))
    screen.blit(ground_surface, (0, 578))

    pygame.display.update()

    decor_sprites.draw(screen)
    decor_sprites.update()

    pygame.display.update()

    clock.tick(20)

pygame.quit()