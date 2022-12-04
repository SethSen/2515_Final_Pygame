import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 0, 0))
        self.x = x
        self.y = y
        self.length = 16
        self.height = 16
        self.vel = 3
        self.spawn = (x, y)
        self.deaths = 0
        self.window = pygame.display.set_mode((1000,700))

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))