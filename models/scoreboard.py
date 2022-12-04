BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

import pygame

class Scoreboard:
    def __init__(self, x, y, length, height):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.window = pygame.display.set_mode((1000,700))

    def draw(self, user):
        pygame.draw.rect(self.window, BLACK, (self.x, self.y, self.length, self.height))

        font = pygame.font.SysFont('Comic Sans MS', 30)
        deaths = font.render('Deaths: ' + str(user.deaths), True, WHITE)
        self.window.blit(deaths, (850, 2))