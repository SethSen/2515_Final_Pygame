import pygame
from models.player import Player
from models.scoreboard import Scoreboard
from models.floor import floor
from functions import draw, leave_bounds
from create_obstacle import create_obstacle
from screen.start_screen import start_screen

BLACK = (0, 0, 0)
LIGHT_BLUE = (180, 181, 254)
BLUE = (0, 0, 255)
GREEN = (153, 255, 153)
LIGHT_PURPLE = (178, 102, 255)


def main():
    #Initialize pygame
    pygame.init()

    #Start screen
    start_screen()

    #Window Size
    window = pygame.display.set_mode((1000,700))

    #Initiazlize the player
    user = Player(65, 515)

    #Initialize the scoreboard
    score_board = Scoreboard(835, 2, 160, 50)

    list_of_floors = floor()

    obstacles = create_obstacle()

    #Event Loop
    running = True
    while running:
        #FPS
        clock = pygame.time.Clock()
        clock.tick(60)
        #stop the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Moves the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            user.x += 3
            if leave_bounds(user, list_of_floors):
                user.x -= 3
        if keys[pygame.K_LEFT]:
            user.x -= 3
            if leave_bounds(user, list_of_floors):
                user.x += 3
        if keys[pygame.K_UP]:
            user.y -= 3
            if leave_bounds(user, list_of_floors):
                user.y += 3
        if keys[pygame.K_DOWN]:
            user.y += 3
            if leave_bounds(user, list_of_floors):
                user.y -= 3

        draw(window, list_of_floors, obstacles, user, score_board)

        #print coordinates of the player
        # print(user.x, user.y)
    
if __name__ == "__main__":
    main()