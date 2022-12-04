import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Rect:
    def __init__(self, x, y, length, height, bounds=[], background=None,):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.bounds = bounds
        self.background = background
        self.window = pygame.display.set_mode((1000,700))
    
    def draw(self):
        if self.background == None:
            pygame.draw.rect(self.window, WHITE, (self.x, self.y, self.length, self.height))
        else:
            pygame.draw.rect(self.window, self.background, (self.x, self.y, self.length, self.height))

        #Draw the bounds
        for bound in self.bounds:
            pygame.draw.rect(self.window, BLACK, (bound.x, bound.y, bound.length, bound.height))