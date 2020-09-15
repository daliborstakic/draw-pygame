""" Importing Pygame """
import pygame

pygame.init()

# Global parameters
WIDTH = 500
ROWS = 50
GAP = WIDTH // ROWS

# Screen
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Draw")

# Colors
WHITE = (255, 255, 255)

def init_grid():
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            grid.append((i, j))
    
    return grid

def draw():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
