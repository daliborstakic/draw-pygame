""" Importing Pygame """
import pygame

pygame.init()

# Screen
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Draw")

# Colors
WHITE = (255, 255, 255)

def draw():
    WIN.fill(WHITE)
    pygame.display.update()

def main():
    run = True

    draw()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
