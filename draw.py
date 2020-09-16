""" Importing Pygame """
import pygame
from pygame.draw import rect

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
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class Button():
    def __init__(self, color, width, height, x, y):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw_button(self):
        """ Draws the button """
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
    
    def is_clicked(self, pos):
        """ If a button has been clicked """
        x, y = pos

        if self.x > x > self.x + self.width and self.y > y > self.y + self.height:
            return True
        
        return False

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

def clear_screen():
    """ Clears the screen """
    WIN.fill(WHITE)

def main():
    """ Main function """
    run = True

    # Drawing tools
    brush = Tool(BLACK, 5)
    eraser = Tool(WHITE, 10)

    # Color buttons
    red_button = Button(RED, 20, 10)
    green_button = Button(GREEN, 20, 10)
    blue_button = Button(BLUE, 20, 10)
    yellow_button = Button(YELLOW, 20, 10)

    # Initial fill
    WIN.fill(WHITE)

    # Main loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Quits the game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    brush.color = RED
                if event.key == pygame.K_d:
                    brush.color = BLACK
                if event.key == pygame.K_g:
                    brush.color = GREEN
                if event.key == pygame.K_b:
                    brush.color = BLUE
                if event.key == pygame.K_y:
                    brush.color = YELLOW
                if event.key == pygame.K_c:
                    clear_screen()
                if event.key == pygame.K_EQUALS:
                    brush.thickness += 5
                if event.key == pygame.K_MINUS:
                    if brush.thickness >= 10:
                        brush.thickness -= 5

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
