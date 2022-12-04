import pygame

BLACK = (0, 0, 0)
LIGHT_BLUE = (180, 181, 254)
BLUE = (0, 0, 255)
GREEN = (153, 255, 153)
LIGHT_PURPLE = (178, 102, 255)

def run_game():
    #Window Size
    window = pygame.display.set_mode((1000,700))

    #Create a name for the window
    pygame.display.set_caption("Impossible Maze Game")

    # colour
    window.fill(LIGHT_BLUE)

    #Initialize font
    pygame.font.init()


def intersect(rect1, rect2):
    if abs((rect1.x + rect1.length/2) - (rect2.x + rect2.length/2)) < 0.5 * (rect1.length + rect2.length):
        if abs((rect1.y + rect1.height/2) - (rect2.y + rect2.height/2)) < 0.5 * (rect1.height + rect2.height):
            return True
    return False

def leave_bounds(user, list_of_floors):
    for floors in list_of_floors:
        if intersect(user, floors):
            for bound in floors.bounds:
                if intersect(user, bound):
                    return True
    return False

def draw(window, list_of_floors, enemy, user, score_board):
    #background colour
    window.fill(LIGHT_PURPLE)

    #Draw the floors
    for floor in list_of_floors:
        floor.draw()

    #Obstacle one
    for obstacle in enemy[0]:
        if obstacle.direction == "down":
            obstacle.move("vertical", 410, 575, 3)
        elif obstacle.direction == "up":
            obstacle.move("vertical", 410, 575, 3)
        obstacle.draw()

    #Obstacle two
    for obstacle in enemy[1]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 585, 860, 3)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 585, 860, 3)
        obstacle.draw()

    #Obstacle three
    for obstacle in enemy[2]:
        if obstacle.direction == "down":
            obstacle.move("vertical", 410, 575, 2)
        elif obstacle.direction == "up":
            obstacle.move("vertical", 410, 575, 2)
        obstacle.draw()

    #Obstacle four
    for obstacle in enemy[3]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 920, 320, 2)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 755, 320, 2)
        obstacle.draw()

    #Obstacle five
    for obstacle in enemy[4]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 920, 360, 2)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 755, 360, 2)
        obstacle.draw()
    
    #Obstacle six
    for obstacle in enemy[5]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 920, 400, 2)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 755, 400, 2)
        obstacle.draw()

    #Obstacle seven
    for obstacle in enemy[6]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 410, 920, 2)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 410, 920, 2)
        obstacle.draw()

    for obstacle in enemy[7]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 410, 920, 1)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 410, 920, 1)
        obstacle.draw()

    for obstacle in enemy[8]:
        if obstacle.direction == "right":
            obstacle.move("horizontal", 410, 920, 3)
        elif obstacle.direction == "left":
            obstacle.move("horizontal", 410, 920, 3)
        obstacle.draw()

    for obstacle in enemy[9]:
        obstacle.draw()

    for obstacle in enemy[10]:
        if obstacle.direction == "down":
            obstacle.move("vertical", 255, 330, 2)
        elif obstacle.direction == "up":
            obstacle.move("vertical", 255, 330, 2)
        obstacle.draw()

    count = 1
    for obstacle in enemy[11]:
        count += 0.5
        if obstacle.direction == "down":
            obstacle.move("vertical", 105, 305, count)
        elif obstacle.direction == "up":
            obstacle.move("vertical", 105, 305, count)
        obstacle.draw()

    for obstacle in enemy[12]:
        obstacle.draw()

    "Kill the player if they touch an obstacle"
    for i in enemy:
        for obstacle in i:
            # print(obstacle)
            if intersect(user, obstacle):
                user.x = 65
                user.y = 515
                user.deaths += 1
            else:
                if intersect(user, obstacle):
                    user.x = 870
                    user.y = 370
                    user.deaths += 1

        

    user.draw()

    score_board.draw(user)

    pygame.display.update()