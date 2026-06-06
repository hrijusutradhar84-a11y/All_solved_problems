"""
Connect 4 GUI Game - Pygame Implementation

A playable Connect4 game with visual interface using pygame.
Players click columns to drop discs. First to 4 in a row wins!

Requirements:
    - pygame: pip install pygame

Usage:
    python connect_4_game.py

Controls:
    - Click any column (0-6) to drop your disc
    - Red circles = Player 1
    - Blue circles = Player 2
    - Close window to exit

Time Complexity: O(1) per move (board checking is constant for 4-in-a-row)
Space Complexity: O(42) = O(1) (6x7 board)
"""

import sys
import importlib.util

# Load Connect_4.py directly from file path to avoid 'array' builtin conflict
spec = importlib.util.spec_from_file_location("Connect_4", r"E:\All_solved_problems\array\Connect_4.py")
Connect_4_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Connect_4_module)

Connect4 = Connect_4_module.Connect4

import pygame

# Game constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600
CELL_SIZE = 100
CIRCLE_RADIUS = 45
CIRCLE_PADDING = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def main():
    """Main game loop for Connect4 GUI."""
    # Initialize game
    game = Connect4()
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Connect 4 - Click to Play")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Game loop
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if the player clicked the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]  # Grab the horizontal pixel coordinate
                col = int(posx // CELL_SIZE)  # Convert pixel to column index

                # Validate column range
                if 0 <= col <= 6:
                    result = game.play(col)
                    print(result)

        # Draw the board visually based on board matrix
        screen.fill(WHITE)

        # Draw grid background
        for r in range(6):
            for c in range(7):
                pygame.draw.rect(screen, YELLOW, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(screen, BLACK, (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS)

        # Draw pieces
        for r in range(6):
            for c in range(7):
                if game.board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS - CIRCLE_PADDING)
                elif game.board[r][c] == 2:
                    pygame.draw.circle(screen, BLUE, (c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS - CIRCLE_PADDING)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
