import time

import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CS = 10
HEIGHT = 600
WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
cells = np.zeros((HEIGHT // CS, WIDTH // CS))
running = False
print(running)


def game(screen, cells):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        num = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        if cells[row, col] == 1:
            if num < 2:
                updated_cells[row, col] = 0
            elif num == 2 or num == 3:
                updated_cells[row, col] = 1
            elif num > 3:
                updated_cells[row, col] = 0

        elif cells[row, col] == 0:
            if num == 3:
                updated_cells[row, col] = 1

        if cells[row, col] == 0:
            color = BLACK
        elif cells[row, col] == 1:
            color = WHITE

        pygame.draw.rect(screen, color, (col * CS, row * CS, CS - 1, CS - 1))
    return updated_cells


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
                print(running)
                game(screen, cells)
                pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            cells[pos[1] // CS, pos[0] // CS] = 1 - cells[pos[1] // CS, pos[0] // CS]
            game(screen, cells)
            pygame.display.update()
    if running:
        cells = game(screen, cells)
        pygame.display.update()
        pygame.time.delay(100)

