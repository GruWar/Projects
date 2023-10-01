import pygame.freetype
from keys import WhiteKey, BlackKey
import sys
from hands import LeftHand, RightHand

piano_notes = ("A0", "Bb0", "B0", "C1", "Db1", "D1", "Eb1", "E1", "F1", "Gb1", "G1", "Ab1",
               "A1", "Bb1", "B1", "C2", "Db2", "D2", "Eb2", "E2", "F2", "Gb2", "G2", "Ab2",
               "A2", "Bb2", "B2", "C3", "Db3", "D3", "Eb3", "E3", "F3", "Gb3", "G3", "Ab3",
               "A3", "Bb3", "B3", "C4", "Db4", "D4", "Eb4", "E4", "F4", "Gb4", "G4", "Ab4",
               "A4", "Bb4", "B4", "C5", "Db5", "D5", "Eb5", "E5", "F5", "Gb5", "G5", "Ab5",
               "A5", "Bb5", "B5", "C6", "Db6", "D6", "Eb6", "E6", "F6", "Gb6", "G6", "Ab6",
               "A6", "Bb6", "B6", "C7", "Db7", "D7", "Eb7", "E7", "F7", "Gb7", "G7", "Ab7",
               "A7", "Bb7", "B7", "C8")
left_hand = LeftHand()
right_hand = RightHand()
# Init Pygame
pygame.init()
pygame.mixer.set_num_channels(50)
WIDTH = 1600
HEIGHT = 200
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("grey")

piano_keys = []
x = 20
for key_id, note in enumerate(piano_notes):
    if "b" in note:
        new_key = BlackKey(key_id, note, x-10, pygame.mixer.Sound(f"notes/{note}.wav"))
    else:
        new_key = WhiteKey(key_id, note, x, pygame.mixer.Sound(f"notes/{note}.wav"))
        x += 30
    piano_keys.append(new_key)


# draw piano
def draw_piano():
    screen.fill("grey")
    for key in piano_keys:
        if isinstance(key, WhiteKey):
            key.draw_key(screen)

    for key in piano_keys:
        if isinstance(key, BlackKey):
            key.draw_key(screen)
    # draw hand
    left_hand.draw_hand(screen, (255, 0, 0))
    right_hand.draw_hand(screen, (0, 255, 0))

draw_piano()

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # white keys left hand octave 1/2
            if event.key == pygame.K_TAB:
                piano_keys[left_hand.play_note("tab")].sound.play()
                print(piano_keys[left_hand.play_note("tab")].note)
            if event.key == pygame.K_q:
                piano_keys[left_hand.play_note("Q")].sound.play()
                print(piano_keys[left_hand.play_note("Q")].note)
            if event.key == pygame.K_w:
                piano_keys[left_hand.play_note("W")].sound.play()
                print(piano_keys[left_hand.play_note("W")].note)
            if event.key == pygame.K_e:
                piano_keys[left_hand.play_note("E")].sound.play()
                print(piano_keys[left_hand.play_note("E")].note)
            if event.key == pygame.K_r:
                piano_keys[left_hand.play_note("R")].sound.play()
                print(piano_keys[left_hand.play_note("R")].note)
            if event.key == pygame.K_t:
                piano_keys[left_hand.play_note("T")].sound.play()
                print(piano_keys[left_hand.play_note("T")].note)
            if event.key == pygame.K_y:
                piano_keys[left_hand.play_note("Y")].sound.play()
                print(piano_keys[left_hand.play_note("Y")].note)
            # black keys left hand octave 1/2
            if event.key == pygame.K_1:
                piano_keys[left_hand.play_note("1")].sound.play()
                print(piano_keys[left_hand.play_note("1")].note)
            if event.key == pygame.K_2:
                piano_keys[left_hand.play_note("2")].sound.play()
                print(piano_keys[left_hand.play_note("2")].note)
            if event.key == pygame.K_4:
                piano_keys[left_hand.play_note("4")].sound.play()
                print(piano_keys[left_hand.play_note("4")].note)
            if event.key == pygame.K_5:
                piano_keys[left_hand.play_note("5")].sound.play()
                print(piano_keys[left_hand.play_note("5")].note)
            if event.key == pygame.K_6:
                piano_keys[left_hand.play_note("6")].sound.play()
                print(piano_keys[left_hand.play_note("6")].note)

            # white keys left hand octave 2/2
            if event.key == pygame.K_a:
                piano_keys[left_hand.play_note("A")].sound.play()
                print(piano_keys[left_hand.play_note("A")].note)
            if event.key == pygame.K_s:
                piano_keys[left_hand.play_note("S")].sound.play()
                print(piano_keys[left_hand.play_note("S")].note)
            if event.key == pygame.K_d:
                piano_keys[left_hand.play_note("D")].sound.play()
                print(piano_keys[left_hand.play_note("D")].note)
            if event.key == pygame.K_f:
                piano_keys[left_hand.play_note("F")].sound.play()
                print(piano_keys[left_hand.play_note("F")].note)
            if event.key == pygame.K_g:
                piano_keys[left_hand.play_note("G")].sound.play()
                print(piano_keys[left_hand.play_note("G")].note)
            if event.key == pygame.K_h:
                piano_keys[left_hand.play_note("H")].sound.play()
                print(piano_keys[left_hand.play_note("H")].note)
            if event.key == pygame.K_j:
                piano_keys[left_hand.play_note("J")].sound.play()
                print(piano_keys[left_hand.play_note("J")].note)
            # black keys left hand octave 2/2
            if event.key == pygame.K_z:
                piano_keys[left_hand.play_note("Z")].sound.play()
                print(piano_keys[left_hand.play_note("Z")].note)
            if event.key == pygame.K_x:
                piano_keys[left_hand.play_note("X")].sound.play()
                print(piano_keys[left_hand.play_note("X")].note)
            if event.key == pygame.K_v:
                piano_keys[left_hand.play_note("V")].sound.play()
                print(piano_keys[left_hand.play_note("V")].note)
            if event.key == pygame.K_b:
                piano_keys[left_hand.play_note("B")].sound.play()
                print(piano_keys[left_hand.play_note("B")].note)
            if event.key == pygame.K_n:
                piano_keys[left_hand.play_note("N")].sound.play()
                print(piano_keys[left_hand.play_note("N")].note)

            # white keys right hand octave 2/2
            if event.key == pygame.K_k:
                piano_keys[right_hand.play_note("K")].sound.play()
                print(piano_keys[right_hand.play_note("K")].note)
            if event.key == pygame.K_l:
                piano_keys[right_hand.play_note("L")].sound.play()
                print(piano_keys[right_hand.play_note("L")].note)
            if event.key == pygame.K_SEMICOLON:
                piano_keys[right_hand.play_note(";")].sound.play()
                print(piano_keys[right_hand.play_note(";")].note)
            if event.key == pygame.K_QUOTE:
                piano_keys[right_hand.play_note("'")].sound.play()
                print(piano_keys[right_hand.play_note("'")].note)
            if event.key == pygame.K_HASH:
                piano_keys[right_hand.play_note("#")].sound.play()
                print(piano_keys[right_hand.play_note("#")].note)
            if event.key == pygame.K_KP4:
                piano_keys[right_hand.play_note("4")].sound.play()
                print(piano_keys[right_hand.play_note("4")].note)
            if event.key == pygame.K_KP5:
                piano_keys[right_hand.play_note("5")].sound.play()
                print(piano_keys[right_hand.play_note("5")].note)

            # black keys right hand octave 2/2
            if event.key == pygame.K_COMMA:
                piano_keys[right_hand.play_note(",")].sound.play()
                print(piano_keys[right_hand.play_note(",")].note)
            if event.key == pygame.K_PERIOD:
                piano_keys[right_hand.play_note(".")].sound.play()
                print(piano_keys[right_hand.play_note(".")].note)
            if event.key == pygame.K_RSHIFT:
                piano_keys[right_hand.play_note("shift")].sound.play()
                print(piano_keys[right_hand.play_note("shift")].note)
            if event.key == pygame.K_KP1:
                piano_keys[right_hand.play_note("1")].sound.play()
                print(piano_keys[right_hand.play_note("1")].note)
            if event.key == pygame.K_KP2:
                piano_keys[right_hand.play_note("2")].sound.play()
                print(piano_keys[right_hand.play_note("2")].note)

            # white keys right hand octave 1/2
            if event.key == pygame.K_u:
                piano_keys[right_hand.play_note("U")].sound.play()
                print(piano_keys[right_hand.play_note("U")].note)
            if event.key == pygame.K_i:
                piano_keys[right_hand.play_note("I")].sound.play()
                print(piano_keys[right_hand.play_note("I")].note)
            if event.key == pygame.K_o:
                piano_keys[right_hand.play_note("O")].sound.play()
                print(piano_keys[right_hand.play_note("O")].note)
            if event.key == pygame.K_p:
                piano_keys[right_hand.play_note("P")].sound.play()
                print(piano_keys[right_hand.play_note("P")].note)
            if event.key == pygame.K_LEFTBRACKET:
                piano_keys[right_hand.play_note("[")].sound.play()
                print(piano_keys[right_hand.play_note("[")].note)
            if event.key == pygame.K_RIGHTBRACKET:
                piano_keys[right_hand.play_note("]")].sound.play()
                print(piano_keys[right_hand.play_note("]")].note)
            if event.key == pygame.K_DELETE:
                piano_keys[right_hand.play_note("delete")].sound.play()
                print(piano_keys[right_hand.play_note("5")].note)

            # black keys right hand octave 1/2
            if event.key == pygame.K_8 :
                piano_keys[right_hand.play_note("8")].sound.play()
                print(piano_keys[right_hand.play_note("8")].note)
            if event.key == pygame.K_9:
                piano_keys[right_hand.play_note("9")].sound.play()
                print(piano_keys[right_hand.play_note("9")].note)
            if event.key == pygame.K_MINUS:
                piano_keys[right_hand.play_note("-")].sound.play()
                print(piano_keys[right_hand.play_note("-")].note)
            if event.key == pygame.K_EQUALS:
                piano_keys[right_hand.play_note("=")].sound.play()
                print(piano_keys[right_hand.play_note("=")].note)
            if event.key == pygame.K_BACKSPACE:
                piano_keys[right_hand.play_note("backspace")].sound.play()
                print(piano_keys[right_hand.play_note("backspace")].note)

            # octave change
            if event.key == pygame.K_RIGHT:
                if left_hand.octave != 7 and left_hand.octave+2 != right_hand.octave:
                    left_hand.draw_hand(screen, "grey")
                    left_hand.x += 210
                    left_hand.draw_hand(screen, (255, 0, 0))
                    left_hand.octave += 1
                    draw_piano()
            if event.key == pygame.K_LEFT:
                if left_hand.octave != 1:
                    left_hand.draw_hand(screen, "grey")
                    left_hand.x -= 210
                    left_hand.draw_hand(screen, (255, 0, 0))
                    left_hand.octave -= 1
                    draw_piano()
            if event.key == pygame.K_UP:
                if right_hand.octave != 8:
                    right_hand.draw_hand(screen, "grey")
                    right_hand.x += 210
                    right_hand.draw_hand(screen, (0, 255, 0))
                    right_hand.octave += 1
                    draw_piano()
            if event.key == pygame.K_DOWN:
                if right_hand.octave != 1 and right_hand.octave-2 != left_hand.octave:
                    right_hand.draw_hand(screen, "grey")
                    right_hand.x -= 210
                    right_hand.draw_hand(screen, (0, 255, 0))
                    right_hand.octave -= 1
                    draw_piano()

    # update
    pygame.display.update()
pygame.quit()
sys.exit()
