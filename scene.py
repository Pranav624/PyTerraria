import pygame
from globals import *
from sprite import Entity
from player import Player

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.sprites = pygame.sprite.Group()
        Entity([self.sprites])
        Entity([self.sprites], position = (100, 100))
        Entity([self.sprites], position = (200, 200))

        self.player = Player([self.sprites])
    
    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill('lightblue')
        self.sprites.draw(self.app.screen)