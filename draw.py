""" Importing Pygame """
import pygame

pygame.init()

# Global parameters
WIDTH = 500

# Screen
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Draw")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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

def draw_on_clicked(tool, pos):
    """ Draws a rectangle on the clicked position """
    x, y = pos

    pygame.draw.rect(WIN, tool.color, (x, y, tool.thickness, tool.thickness))

def main():
    """ Main function """
    run = True

    # Drawing tools
    brush = Tool(RED, 5)
    eraser = Tool(WHITE, 10)

    # Initial fill
    WIN.fill(WHITE)

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Quits the game
            if pygame.mouse.get_pressed()[0]: # Left mouse button draws
                pos = pygame.mouse.get_pos()
                draw_on_clicked(brush, pos)
            elif pygame.mouse.get_pressed()[2]: # Right mouse button erases
                pos = pygame.mouse.get_pos()
                draw_on_clicked(eraser, pos)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
