import pygame


class LeftHand:
    def __init__(self):
        self.Wkeys = ["Tab", "Q", "W", "E", "R", "T", "Y", "A", "S", "D", "F", "G", "H", "J"]
        self.Bkeys = ["1", "2", "4", "5", "6", "Z", "X", "V", "B", "N"]
        self.octave = 1
        self.x = 80

    def play_note(self, key):

        # white keys
        if key == "tab":
            return 12 * (self.octave - 1) + 3
        if key == "Q":
            return 12 * (self.octave - 1) + 5
        if key == "W":
            return 12 * (self.octave - 1) + 7
        if key == "E":
            return 12 * (self.octave - 1) + 8
        if key == "R":
            return 12 * (self.octave - 1) + 10
        if key == "T":
            return 12 * (self.octave - 1) + 12
        if key == "Y":
            return 12 * (self.octave - 1) + 14
        # black key
        if key == "1":
            return 12 * (self.octave - 1) + 4
        if key == "2":
            return 12 * (self.octave - 1) + 6
        if key == "4":
            return 12 * (self.octave - 1) + 9
        if key == "5":
            return 12 * (self.octave - 1) + 11
        if key == "6":
            return 12 * (self.octave - 1) + 13

        # white keys octave 2/2
        if key == "A":
            return 12 * (self.octave - 1) + 15
        if key == "S":
            return 12 * (self.octave - 1) + 17
        if key == "D":
            return 12 * (self.octave - 1) + 19
        if key == "F":
            return 12 * (self.octave - 1) + 20
        if key == "G":
            return 12 * (self.octave - 1) + 22
        if key == "H":
            return 12 * (self.octave - 1) + 24
        if key == "J":
            return 12 * (self.octave - 1) + 26
        # black key octave 2/2
        if key == "Z":
            return 12 * (self.octave - 1) + 16
        if key == "X":
            return 12 * (self.octave - 1) + 18
        if key == "V":
            return 12 * (self.octave - 1) + 21
        if key == "B":
            return 12 * (self.octave - 1) + 23
        if key == "N":
            return 12 * (self.octave - 1) + 25

    def draw_hand(self, screen, color):
        offset = 0
        pygame.draw.rect(screen, color, (self.x, 20, 420, 20))

        for key in self.Wkeys:
            font = pygame.font.Font(None, 20)
            text = font.render(key, True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (self.x + 15 + offset, 160)
            screen.blit(text, text_rect)
            offset += 30
        offset = 0
        space = 0

        for key in self.Bkeys:
            font = pygame.font.Font(None, 20)
            text = font.render(key, True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (self.x + 30 + offset, 100)
            screen.blit(text, text_rect)

            if space == 0 or space == 2 or space == 3:
                offset += 30
                space += 1
            elif space == 4:
                space = 0
                offset += 60
            else:
                offset += 60
                space += 1



class RightHand:
    def __init__(self):
        self.Wkeys = ["U", "I", "O", "P", "[", "]", "Del", "K", "L", ";", "'", "#", "4", "5"]
        self.Bkeys = ["8", "9", "-", "=", "<-", ",", ".", "RSh", "1", "2"]
        self.octave = 6
        self.x = 1130

    def play_note(self, key):

        # white keys octave 1/2
        if key == "U":
            return 12 * (self.octave - 1) + 3
        if key == "I":
            return 12 * (self.octave - 1) + 5
        if key == "O":
            return 12 * (self.octave - 1) + 7
        if key == "P":
            return 12 * (self.octave - 1) + 8
        if key == "[":
            return 12 * (self.octave - 1) + 10
        if key == "]":
            return 12 * (self.octave - 1) + 12
        if key == "delete":
            return 12 * (self.octave - 1) + 14
        # black key octave 1/2
        if key == "8":
            return 12 * (self.octave - 1) + 4
        if key == "9":
            return 12 * (self.octave - 1) + 6
        if key == "-":
            return 12 * (self.octave - 1) + 9
        if key == "=":
            return 12 * (self.octave - 1) + 11
        if key == "backspace":
            return 12 * (self.octave - 1) + 13

        # white keys octave 2/2
        if key == "K":
            return 12 * (self.octave - 1) + 15
        if key == "L":
            return 12 * (self.octave - 1) + 17
        if key == ";":
            return 12 * (self.octave - 1) + 19
        if key == "'":
            return 12 * (self.octave - 1) + 20
        if key == "#":
            return 12 * (self.octave - 1) + 22
        if key == "4":
            return 12 * (self.octave - 1) + 24
        if key == "5":
            return 12 * (self.octave - 1) + 26
        # black key octave 2/2
        if key == ",":
            return 12 * (self.octave - 1) + 16
        if key == ".":
            return 12 * (self.octave - 1) + 18
        if key == "shift":
            return 12 * (self.octave - 1) + 21
        if key == "1":
            return 12 * (self.octave - 1) + 23
        if key == "2":
            return 12 * (self.octave - 1) + 25

    def draw_hand(self, screen, color):
        offset = 0
        pygame.draw.rect(screen, color, (self.x, 20, 420, 20))

        for key in self.Wkeys:
            font = pygame.font.Font(None, 20)
            text = font.render(key, True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (self.x + 15 + offset, 160)
            screen.blit(text, text_rect)
            offset += 30
        offset = 0
        space = 0

        for key in self.Bkeys:
            font = pygame.font.Font(None, 20)
            text = font.render(key, True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (self.x + 30 + offset, 100)
            screen.blit(text, text_rect)

            if space == 0 or space == 2 or space == 3:
                offset += 30
                space += 1
            elif space == 4:
                space = 0
                offset += 60
            else:
                offset += 60
                space += 1
