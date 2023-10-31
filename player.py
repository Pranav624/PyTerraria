import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE*2, TILESIZE*3)), position = (SCREENWIDTH//2, SCREENHEIGHT//2)) -> None:
        super().__init__(groups)
        self.image = image
        self.image.fill('brown')
        self.rect = self.image.get_rect(topleft = position)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_d]:
            self.rect.x += 5
    
    def update(self):
        self.input()