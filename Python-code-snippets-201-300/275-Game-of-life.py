"""Code snippets vol-55
   275-Game-of-life

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install numpy
pip3 install pygame

Origin:
https://github.com/beltoforion/recreational_mathematics_with_python
/blob/master/game_of_life.py
"""
import pygame
import numpy as np


class Colors:
    about_to_die = (200, 200, 225)
    alive = (255, 255, 215)
    background = (10, 10, 40)
    grid = (30, 30, 60)


def update(surface, cells, sz):
    cur = cells[0]
    nxt = cells[1]

    for r in range(1, cur.shape[0] - 1):
        for c in range(1, cur.shape[1] - 1):
            num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

            if cur[r, c] == 1:
                if num_alive < 2 or num_alive > 3:
                    nxt[r, c] = 0
                    col = Colors.about_to_die

                if 2 <= num_alive <= 3:
                    nxt[r, c] = 1
                    col = Colors.alive
            elif cur[r, c] == 0 and num_alive == 3:
                nxt[r, c] = 1
                col = Colors.alive

            if cur[r, c] == 1:
                pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))
            else:
                pygame.draw.rect(surface, Colors.background, (c*sz, r*sz, sz-1, sz-1))

    cells[0] = nxt
    cells[1] = cur


def init(dimx, dimy):
    cells = np.zeros((2, dimy, dimx))
    pattern = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    mid = (3,3)
    cells[0][mid[0]:mid[0]+pattern.shape[0], mid[1]:mid[1]+pattern.shape[1]] = pattern
    return cells


def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(Colors.grid)
        update(surface, cells, cellsize)
        pygame.display.update()


if __name__ == "__main__":
    main(100, 70, 8)
