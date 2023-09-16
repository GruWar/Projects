import pygame


class WhiteKey:
    def __init__(self, key_id, note, x, sound):
        self.id = key_id
        self.note = note
        self.x = x
        self.sound = sound

    def draw_key(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, 50, 30, 150))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, 50, 30, 150), 2)

        font = pygame.font.Font(None, 25)
        text = font.render(self.note, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.x + 15, 180)
        screen.blit(text, text_rect)


class BlackKey:
    def __init__(self, key_id, note, x, sound):
        self.id = key_id
        self.note = note
        self.x = x
        self.sound = sound

    def draw_key(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, 50, 20, 100))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, 50, 20, 100), 2)

        font = pygame.font.Font(None, 15)
        text = font.render(self.note, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.x + 10, 75)
        screen.blit(text, text_rect)
