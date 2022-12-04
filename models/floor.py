import pygame
from models.maze import Rect

GREEN = (153, 255, 153)

def floor():
    start_floor = Rect(40, 500, 60, 50, [Rect(40, 500, 60, 3), Rect(40, 500, 3, 50), Rect(40, 550, 60, 3)], GREEN)
    floor_two = Rect(100, 400, 800, 200, [Rect(100, 400, 753, 3), Rect(100, 400, 3, 103), Rect(100, 550, 3, 50), Rect(100, 600, 803, 3), Rect(900, 400, 3, 200), Rect(550, 400, 5, 170)])
    checkpoint_floor = Rect(850, 350, 50, 50, [Rect(850, 350, 3, 50), Rect(900, 350, 3, 50)], GREEN)
    floor_four = Rect(750, 100, 190, 250, [Rect(750, 200, 3, 150), Rect(750, 350, 100, 3), Rect(900, 350, 40, 3), Rect(940, 100, 3, 253), Rect(750, 100, 190, 3)])
    floor_five = Rect(400, 100, 540, 100, [Rect(700, 100, 50, 3), Rect(700, 200, 50, 3)])
    floor_six = Rect(400, 100, 300, 250, [Rect(400, 100, 300, 3), Rect(400, 100, 3, 153), Rect(400, 350, 300, 3), Rect(700, 200, 3, 153)])
    floor_seven = Rect(300,250, 100, 100, [Rect(300, 250, 100, 3), Rect(300, 350, 100, 3), Rect(300, 250, 3, 60)])
    floor_eight = Rect(100,100, 200, 250, [Rect(300, 100, 3, 150), Rect(200, 100, 100, 3), Rect(100, 100, 53, 3), Rect(100, 100, 3, 250), Rect(100, 350, 290, 3)])
    end_floor = Rect(150, 50, 50, 50, [Rect(150, 50, 3, 50), Rect(150, 50, 50, 3), Rect(200, 50, 3, 50)], GREEN)

    list_of_floors = [start_floor, floor_two, checkpoint_floor, floor_four, floor_five, floor_six, floor_seven, floor_eight, end_floor]
    return list_of_floors