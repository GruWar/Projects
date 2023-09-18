import pygame


class LeftHand:
    def __init__(self):
        self.keys = ("A", "S", "D", "F", "G", "Y", "X", "C", "V", "B", "N", "M")
        self.octave = 1
        self.x = 80

    def play_note(self, key):

        # white keys
        if key == "Y":
            return 12 * (self.octave - 1) + 3
        if key == "X":
            return 12 * (self.octave - 1) + 5
        if key == "C":
            return 12 * (self.octave - 1) + 7
        if key == "V":
            return 12 * (self.octave - 1) + 8
        if key == "B":
            return 12 * (self.octave - 1) + 10
        if key == "N":
            return 12 * (self.octave - 1) + 12
        if key == "M":
            return 12 * (self.octave - 1) + 14
        # black key
        if key == "A":
            return 12 * (self.octave - 1) + 4
        if key == "S":
            return 12 * (self.octave - 1) + 6
        if key == "D":
            return 12 * (self.octave - 1) + 9
        if key == "F":
            return 12 * (self.octave - 1) + 11
        if key == "G":
            return 12 * (self.octave - 1) + 13

    def draw_hand(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, 20, 210, 20))


class RightHand:
    def __init__(self):
        self.keys = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", "-")
        self.octave = 7
        self.x = 1340

    def play_note(self, key):

        # white keys
        if key == "1":
            return 12 * (self.octave - 1) + 3
        if key == "2":
            return 12 * (self.octave - 1) + 5
        if key == "3":
            return 12 * (self.octave - 1) + 7
        if key == "4":
            return 12 * (self.octave - 1) + 8
        if key == "5":
            return 12 * (self.octave - 1) + 10
        if key == "6":
            return 12 * (self.octave - 1) + 12
        if key == "7":
            return 12 * (self.octave - 1) + 14
        # black key
        if key == "8":
            return 12 * (self.octave - 1) + 4
        if key == "9":
            return 12 * (self.octave - 1) + 6
        if key == "/":
            return 12 * (self.octave - 1) + 9
        if key == "*":
            return 12 * (self.octave - 1) + 11
        if key == "-":
            return 12 * (self.octave - 1) + 13

    def draw_hand(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, 20, 210, 20))
