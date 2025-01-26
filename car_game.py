import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Load the car images
car_image = pygame.image.load("car1.png")
obstacle_image = pygame.image.load("car2.png")

# Get the dimensions of the car images
car_width = car_image.get_width()
car_height = car_image.get_height()
obstacle_width = obstacle_image.get_width()
obstacle_height = obstacle_image.get_height()

# Function to detect collision
def check_collision(car_x, car_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
    if car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x:
            return True
    return False

# Main game loop
def game_loop():
    # Initial car position
    car_x = (SCREEN_WIDTH * 0.45)
    car_y = (SCREEN_HEIGHT * 0.8)
    car_x_change = 0

    # Obstacle parameters
    obstacle_x = random.randrange(0, SCREEN_WIDTH - obstacle_width)
    obstacle_y = -600
    obstacle_speed = 5

    # Game clock
    clock = pygame.time.Clock()

    # Game over flag
    game_over = False

    # Main loop
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                if event.key == pygame.K_RIGHT:
                    car_x_change = 5

            # Keyup events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        # Update car position
        car_x += car_x_change

        # Fill the background with black color
        screen.fill(BLACK)

        # Move the obstacle
        obstacle_y += obstacle_speed

        # Draw the obstacle using car2.png
        screen.blit(obstacle_image, (obstacle_x, obstacle_y))

        # Draw the car using car.png
        screen.blit(car_image, (car_x, car_y))

        # Reset the obstacle when it goes off-screen
        if obstacle_y > SCREEN_HEIGHT:
            obstacle_y = -obstacle_height
            obstacle_x = random.randrange(0, SCREEN_WIDTH - obstacle_width)

        # Check for collision
        if check_collision(car_x, car_y, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
            game_over = True
            print("You crashed!")

        # Update the screen
        pygame.display.update()

        # Set the frames per second
        clock.tick(60)

    pygame.quit()
    quit()

# Run the game
game_loop()
