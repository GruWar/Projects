import pygame
import random

BOARD_SIZE = 720
CS = 6
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)

pygame.init()
display_size = (BOARD_SIZE, BOARD_SIZE)
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(display_size)

# default screen set
screen.fill("white")

# generate ants
ants = []
number_of_ants = 1
for _ in range(0, number_of_ants):
    ant = [pygame.Rect((random.randint(CS, BOARD_SIZE), random.randint(CS, BOARD_SIZE)), (CS, CS)), 0]
    ants.append(ant)


def ant_move(ant, direction):
    # check border
    if ant.x <= 0:
        ant.x = BOARD_SIZE - CS
    elif ant.x >= BOARD_SIZE:
        ant.x = 0 + CS
    elif ant.y <= 0:
        ant.y = BOARD_SIZE - CS
    elif ant.y >= BOARD_SIZE:
        ant.y = 0 + CS
    # get color
    color = pygame.Surface.get_at(screen, (ant.x, ant.y))
    # decide on direction
    if color == WHITE:
        direction += 1
    elif color == BLUE:
        direction += 1
    elif color == RED:
        direction -= 1
    else:
        direction -= 1

    if direction < 0:
        direction = 3
    if direction > 3:
        direction = 0
    # check for new color
    if color == WHITE:
        pygame.draw.rect(screen, "black", ant)
    elif color == BLACK:
        pygame.draw.rect(screen, "blue", ant)
    elif color == BLUE:
        pygame.draw.rect(screen, "red", ant)
    else:
        pygame.draw.rect(screen, "white", ant)

    # move ant
    if direction == 0:
        ant.y -= CS
    elif direction == 1:
        ant.x += CS
    elif direction == 2:
        ant.y += CS
    elif direction == 3:
        ant.x -= CS

    return ant, direction


# app loop
while running:

    for ant in ants:
        ant[0], ant[1] = ant_move(ant[0], ant[1])

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()