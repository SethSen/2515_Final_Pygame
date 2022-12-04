import pygame
from functions import run_game

LIGHT_PURPLE = (178, 102, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def start_screen():
    # Initialize the screen
    screen = pygame.display.set_mode((1000, 700))
    # Set the background color to blue
    screen.fill(LIGHT_PURPLE)

      # Create a font for the title
    title_font = pygame.font.Font(None, 48)
    # Create a text surface with the text "Impossible Maze Game"
    title = title_font.render("Impossible Maze Game", True, (BLACK))
    # Get the rectangular area of the text surface
    title_rect = title.get_rect()
    # Set the position of the rectangular area to the center of the screen
    title_rect.center = (500, 50)
    # Draw the title to the screen
    screen.blit(title, title_rect)

    # Create a font for the text under the title
    font = pygame.font.Font(None, 24)
    # Create a text surface with the text "Welcome to the impossible maze game, give up while you can"
    text = font.render("Welcome to the impossible maze game, give up while you can", True, (BLACK))
    # Get the rectangular area of the text surface
    text_rect = text.get_rect()
    # Set the position of the rectangular area to the center of the screen
    text_rect.center = (500, 100)
    # Draw the text to the screen
    screen.blit(text, text_rect)

    # Create a font for the start button
    font = pygame.font.Font(None, 36)
    # Create a text surface with the text "Start"
    text = font.render("Start", True, (WHITE))
    # Get the rectangular area of the text surface
    text_rect = text.get_rect()
    # Set the position of the rectangular area to the center of the screen
    text_rect.center = (500, 350)
    # Draw the text to the screen
    screen.blit(text, text_rect)
    
    # Display the start screen until the user clicks on the start button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game
                pygame.quit()
            # If the user clicks on the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()
                # Check if the click was inside the rectangular area of the text
                if text_rect.collidepoint(pos):
                    # If it was, return from the function to move on to the next part of the game
                    run_game()
                    return
        
        # Update the screen
        pygame.display.flip()