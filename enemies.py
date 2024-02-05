import pygame
import random


class enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.assets = ['sprites/enemies/kaktus1.png', 'sprites/enemies/kaktus2.png',
                       'sprites/enemies/kaktus3.png', 'sprites/enemies/kaktus4.png', 'sprites/enemies/tony1.png',
                       'sprites/enemies/ptero/ptero_1.png']
        self.enemy = random.choice(self.assets)
        self.image = pygame.image.load(self.enemy)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1200
        # only for pterodactyl
        self.frame = 0
        self.animlist = [pygame.image.load('sprites/enemies/ptero/ptero_1.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_2.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_3.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_4.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_5.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_6.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_7.png'),
                         pygame.image.load('sprites/enemies/ptero/ptero_8.png')]

    def start_position(self):
        self.rect.x = -1000
        self.update()

    def anim(self):
        if self.enemy == 'sprites/enemies/ptero/ptero_1.png':
            self.frame = (self.frame + 1) % len(self.animlist)
            self.image = self.animlist[self.frame]

    def update(self):
        if self.enemy != 'sprites/enemies/ptero/ptero_1.png':
            if self.enemy == "sprites/enemies/tony1.png":
                self.rect.bottom = 690
            if self.enemy != "sprites/enemies/tony1.png":
                self.rect.bottom = 579
            self.rect.x -= 20
            if self.rect.x < -random.randint(1000, 5000):
                self.enemy = random.choice(self.assets)
                self.image = pygame.image.load(self.enemy)
                self.rect.x = 1300
        else:
            self.rect.bottom = 300
            self.anim()
            self.rect.x -= 20
            if self.rect.x < -random.randint(1000, 5000):
                self.rect.x = 2000
                self.enemy = random.choice(self.assets)
                self.image = pygame.image.load(self.enemy)
