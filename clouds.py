import pygame
import random


class cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.assets = ['sprites/sky3.png', 'sprites/sky2.png', 'sprites/sky4.png']
        self.enemy = random.choice(self.assets)
        self.image = pygame.image.load(self.enemy)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = random.randint(100, 150)
        self.rect.x = 1200

    def update(self):
        self.rect.x -= 10
        if self.rect.x < -random.randint(1000, 1300):
            self.enemy = random.choice(self.assets)
            self.image = pygame.image.load(self.enemy)
            self.rect.x = 1300
