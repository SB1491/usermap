import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
secret_number = random.randint(1, 100)
attempts = 0

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def main():
    global attempts

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        
        draw_text("Welcome to the Guessing Game!", 30, 30)
        draw_text("I'm thinking of a number between 1 and 100.", 30, 70)

        guess_text = font.render("Enter your guess:", True, BLACK)
        screen.blit(guess_text, (30, 120))

        pygame.display.flip()

        if attempts == 0:
            attempts += 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isnumeric():
                    guess = int(event.unicode)
                    if guess < secret_number:
                        draw_text("Try higher!", 30, 200)
                    elif guess > secret_number:
                        draw_text("Try lower!", 30, 200)
                    else:
                        draw_text(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.", 30, 200)

        pygame.display.flip()

if __name__ == "__main__":
    main()