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
for key in piano_keys:
    if isinstance(key, WhiteKey):
        key.draw_key(screen)

for key in piano_keys:
    if isinstance(key, BlackKey):
        key.draw_key(screen)
# draw hand
    left_hand.draw_hand(screen, (255, 0, 0))
    right_hand.draw_hand(screen, (0, 255, 0))

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # white keys left hand
            if event.key == pygame.K_y:
                piano_keys[left_hand.play_note("Y")].sound.play()
            if event.key == pygame.K_x:
                piano_keys[left_hand.play_note("X")].sound.play()
            if event.key == pygame.K_c:
                piano_keys[left_hand.play_note("C")].sound.play()
            if event.key == pygame.K_v:
                piano_keys[left_hand.play_note("V")].sound.play()
            if event.key == pygame.K_b:
                piano_keys[left_hand.play_note("B")].sound.play()
            if event.key == pygame.K_n:
                piano_keys[left_hand.play_note("N")].sound.play()
            if event.key == pygame.K_m:
                piano_keys[left_hand.play_note("M")].sound.play()
            # black keys left hand
            if event.key == pygame.K_a:
                piano_keys[left_hand.play_note("A")].sound.play()
            if event.key == pygame.K_s:
                piano_keys[left_hand.play_note("S")].sound.play()
            if event.key == pygame.K_d:
                piano_keys[left_hand.play_note("D")].sound.play()
            if event.key == pygame.K_f:
                piano_keys[left_hand.play_note("F")].sound.play()
            if event.key == pygame.K_g:
                piano_keys[left_hand.play_note("G")].sound.play()

            # white keys right hand
            if event.key == pygame.K_KP1:
                piano_keys[right_hand.play_note("1")].sound.play()
            if event.key == pygame.K_KP2:
                piano_keys[right_hand.play_note("2")].sound.play()
            if event.key == pygame.K_KP3:
                piano_keys[right_hand.play_note("3")].sound.play()
            if event.key == pygame.K_KP4:
                piano_keys[right_hand.play_note("4")].sound.play()
            if event.key == pygame.K_KP5:
                piano_keys[right_hand.play_note("5")].sound.play()
            if event.key == pygame.K_KP6:
                piano_keys[right_hand.play_note("6")].sound.play()
            if event.key == pygame.K_KP7:
                piano_keys[right_hand.play_note("7")].sound.play()
            # black keys right hand
            if event.key == pygame.K_KP8:
                piano_keys[right_hand.play_note("8")].sound.play()
            if event.key == pygame.K_KP9:
                piano_keys[right_hand.play_note("9")].sound.play()
            if event.key == pygame.K_KP_DIVIDE:
                piano_keys[right_hand.play_note("/")].sound.play()
            if event.key == pygame.K_KP_MULTIPLY:
                piano_keys[right_hand.play_note("*")].sound.play()
            if event.key == pygame.K_KP_MINUS:
                piano_keys[right_hand.play_note("-")].sound.play()

            # octave change
            if event.key == pygame.K_RIGHT:
                if left_hand.octave != 8 and left_hand.octave+1 != right_hand.octave:
                    left_hand.draw_hand(screen, "grey")
                    left_hand.x += 210
                    left_hand.draw_hand(screen, (255, 0, 0))
                    left_hand.octave += 1
            if event.key == pygame.K_LEFT:
                if left_hand.octave != 1:
                    left_hand.draw_hand(screen, "grey")
                    left_hand.x -= 210
                    left_hand.draw_hand(screen, (255, 0, 0))
                    left_hand.octave -= 1
            if event.key == pygame.K_UP:
                if right_hand.octave != 8:
                    right_hand.draw_hand(screen, "grey")
                    right_hand.x += 210
                    right_hand.draw_hand(screen, (0, 255, 0))
                    right_hand.octave += 1
            if event.key == pygame.K_DOWN:
                if right_hand.octave != 1 and right_hand.octave-1 != left_hand.octave:
                    right_hand.draw_hand(screen, "grey")
                    right_hand.x -= 210
                    right_hand.draw_hand(screen, (0, 255, 0))
                    right_hand.octave -= 1

    # update
    pygame.display.update()
pygame.quit()
sys.exit()
