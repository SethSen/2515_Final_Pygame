import pygame

BLUE = (0, 0, 255)

class Obstacle():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.length = 20
        self.height = 20
        self.direction = direction
        self.image = pygame.Surface((20, 20))
        self.image.fill((BLUE))
        self.window = pygame.display.set_mode((1000,700))

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        
    # move the obstacle up and down continuously
    def move(self, angle, bound_one, bound_two, vel):
        if angle == "vertical":
            if self.direction == "up":
                self.y -= vel
            elif self.direction == "down":
                self.y += vel

            if self.y < bound_one:
                self.direction = "down"
            elif self.y > bound_two:
                self.direction = "up"

        if angle == "horizontal":
            if self.direction == "left":
                self.x -= vel
            elif self.direction == "right":
                self.x += vel

            if self.x < bound_one:
                self.direction = "right"
            elif self.x > bound_two:
                self.direction = "left"

def enemy():
    