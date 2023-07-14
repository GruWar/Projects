import pygame
import random

GREEN = (47, 183, 0)
CS = 10
HEIGHT = 600
WIDTH = 800
IMG_SIZE_DEF = (100, 100)
X = 100
Y = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(GREEN)

dice_1 = pygame.image.load('images/dice_1.png')
dice_2 = pygame.image.load('images/dice_2.png')
dice_3 = pygame.image.load('images/dice_3.png')
dice_4 = pygame.image.load('images/dice_4.png')
dice_5 = pygame.image.load('images/dice_5.png')
dice_6 = pygame.image.load('images/dice_6.png')
dice_1 = pygame.transform.scale(dice_1, IMG_SIZE_DEF)
dice_2 = pygame.transform.scale(dice_2, IMG_SIZE_DEF)
dice_3 = pygame.transform.scale(dice_3, IMG_SIZE_DEF)
dice_4 = pygame.transform.scale(dice_4, IMG_SIZE_DEF)
dice_5 = pygame.transform.scale(dice_5, IMG_SIZE_DEF)
dice_6 = pygame.transform.scale(dice_6, IMG_SIZE_DEF)
running = True


def generate_dice():
    pos = 0
    for _ in range(6):
        dice = random.randint(1, 6)
        if dice == 1:
            screen.blit(dice_1, (X + pos, Y))
        elif dice == 2:
            screen.blit(dice_2, (X + pos, Y))
        elif dice == 3:
            screen.blit(dice_3, (X + pos, Y))
        elif dice == 4:
            screen.blit(dice_4, (X + pos, Y))
        elif dice == 5:
            screen.blit(dice_5, (X + pos, Y))
        elif dice == 6:
            screen.blit(dice_6, (X + pos, Y))
        pos += 100


while True:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if running:
        generate_dice()
        running = False

