import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Rock, Paper, Scissors")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Define choices
choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(choices)

def main():
    running = True
    player_choice = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_choice = "Rock"
                elif event.key == pygame.K_p:
                    player_choice = "Paper"
                elif event.key == pygame.K_s:
                    player_choice = "Scissors"
        
        if player_choice:
            computer_choice = get_computer_choice()
            result = None

            if player_choice == computer_choice:
                result = "It's a tie!"
            elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                 (player_choice == "Paper" and computer_choice == "Rock") or \
                 (player_choice == "Scissors" and computer_choice == "Paper"):
                result = "You win!"
            else:
                result = "Computer wins!"

            # Display result
            screen.fill(WHITE)
            screen.blit(rock_img, (50, 150))
            screen.blit(paper_img, (150, 150))
            screen.blit(scissors_img, (250, 150))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Player: {player_choice}  Computer: {computer_choice}", True, BLACK)
            text_rect = text.get_rect(center=(200, 50))
            screen.blit(text, text_rect)
            text = font.render(result, True, BLACK)
            text_rect = text.get_rect(center=(200, 350))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(2000)  # Display result for 2 seconds
            player_choice = None

        screen.fill(WHITE)
        screen.blit(rock_img, (50, 150))
        screen.blit(paper_img, (150, 150))
        screen.blit(scissors_img, (250, 150))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
