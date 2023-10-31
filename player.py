import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE*2, TILESIZE*3)), position = (SCREENWIDTH//2, SCREENHEIGHT//2)) -> None:
        super().__init__(groups)
        self.image = image
        self.image.fill('brown')
        self.rect = self.image.get_rect(topleft = position)

        self.velocity = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity.y = -5
        if keys[pygame.K_a]:
            self.velocity.x = -5
        if keys[pygame.K_s]:
            self.velocity.y = 5
        if keys[pygame.K_d]:
            self.velocity.x = 5
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = 0
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.velocity.y = 0
    
    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    
    def update(self):
        self.input()
        self.move()