import pygame


class dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/player/dino_jump.png')
        self.rect = self.image.get_rect()
        self.rect.y = 254
        self.rect.x = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.frame = 0
        self.animlist = [pygame.image.load('sprites/player/dino1.png'), pygame.image.load('sprites/player/dino2.png')]
        self.gravity = 1

    def start_position(self):
        self.rect.x = 0
        self.rect.y = 254

    def anim(self):
        self.frame = (self.frame + 1) % len(self.animlist)
        self.image = self.animlist[self.frame]
        if self.rect.bottom != 578:
            self.image = pygame.image.load('sprites/player/dino_jump.png')

    def cmoon(self):
        self.image = pygame.image.load('sprites/player/dino_jump.png')
        self.gravity += 0.6
        self.rect.y += self.gravity
        if self.rect.bottom >= 578:
            self.rect.bottom = 578

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 578:
            self.gravity = -20

    def update(self):
        self.cmoon()
        self.jump()
        self.anim()
