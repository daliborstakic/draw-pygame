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

class Tool():
    def __init__(self, color, thickness):
        self._color = color
        self._thickness = thickness

    @property
    def color(self):
        """ Color getter """
        return self._color

    @color.setter
    def color(self, color):
        """ Color setter """
        self._color = color

    @property
    def thickness(self):
        """ Thickness getter """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness):
        """ Thickness setter """
        self._thickness = thickness 

def init_grid():
    """ Initializes the grid """
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            grid.append((i, j))
    
    return grid

def draw():
    """ Draws the screen """
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    """ Main function """
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
