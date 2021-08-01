"""
133-Pygame background scroller
stevepython.wordpress.com

source:
https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame

pip install pygame
"""

import pygame
import sys

def scrollX(screenSurf, offsetX):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (offsetX, 0))
    if offsetX < 0:
        screenSurf.blit(copySurf, (width + offsetX, 0), (0, 0, -offsetX, height))
    else:
        screenSurf.blit(copySurf, (0, 0), (width - offsetX, 0, offsetX, height))



def scrollY(screenSurf, offsetY):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (0, offsetY))
    if offsetY < 0:
        screenSurf.blit(copySurf, (0, height + offsetY), (0, 0, width, -offsetY))
    else:
        screenSurf.blit(copySurf, (0, 0), (0, height - offsetY, width, offsetY))



def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 800))

    x_pos = 0
    y_pos = 0
    yellow = (255, 255, 0)
    blue = (0, 0, 255)

    # draw pattern of yellow and blue squares
    for y in range(100):
        for x in range(100):

            if (y + x) % 2 == 0:
                pygame.draw.rect(screen, yellow, (x_pos, y_pos, 50, 50))
            else:
                pygame.draw.rect(screen, blue, (x_pos, y_pos, 50, 50))

            x_pos += 50

        y_pos += 50
        x_pos = 0

    while True:  # <-- the pyGame loop

        event = pygame.event.poll()
        pressed = pygame.key.get_pressed()

        # handle window closing
        if event.type == pygame.QUIT:
            break

        if pressed[pygame.K_UP]:
            scrollY(screen, 2)
        elif pressed[pygame.K_DOWN]:
            scrollY(screen, -2)
        elif pressed[pygame.K_LEFT]:
            scrollX(screen, 2)
        elif pressed[pygame.K_RIGHT]:
            scrollX(screen, -2)

        # updates what the window displays
        pygame.display.update()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    # runs the pyGame loop
    main()
