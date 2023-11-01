import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple, parameters: dict) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)

        # Parameters
        self.block_group = parameters['block_group']
        
        self.velocity = pygame.math.Vector2()
        self.mass = 5
        self.terminal_velocity = self.mass * TERMINALVELOCITY

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x = -1
        if keys[pygame.K_d]:
            self.velocity.x = 1
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.velocity.x = 0
    
    def move(self):
        self.velocity.y += GRAVITY * self.mass
        # Terminal velocity check
        if self.velocity.y > self.terminal_velocity:
            self.velocity.y = self.terminal_velocity

        self.rect.x += self.velocity.x * PLAYERSPEED # applying horizontal velocity
        self.check_collisions("horizontal")
        self.rect.y += self.velocity.y # applying vertical velocity
        self.check_collisions("vertical")
    
    def check_collisions(self, direction):
        if direction == "horizontal":
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0: # moving right
                        self.rect.right = block.rect.left
                    if self.velocity.x < 0: # moving left
                        self.rect.left = block.rect.right
        elif direction == "vertical":
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0: # moving down
                        self.rect.bottom = block.rect.top
                    if self.velocity.y < 0: # moving up
                        self.rect.top = block.rect.bottom

    def update(self):
        self.input()
        self.move()