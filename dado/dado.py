import random
import pygame
from lib.spritesheet import Spritesheet as ss
import keyboard


def rotar_dado(screen, ss, n):
    anterior_cara = 0
    white = (255, 255, 255)
    font = pygame.font.Font('fonts/roboto.ttf', 18)
    black = (0, 0, 0)

    for _ in range(n):
        screen.fill(black)

        cara = random.randint(0, len(ss)-1)
        while cara == anterior_cara:
            cara = random.randint(0, len(ss)-1)

        image = ss[cara]
        screen.blit(image, (86, 86))
        anterior_cara = cara

        text = font.render("Has sacado un " + str(6 - cara), False, white)
        screen.blit(text, (92, 232))

        pygame.display.flip()
        pygame.time.wait(16)


pygame.init()
size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lanzador de dados")
img = ss(pygame.image.load("img/dado.png")).get_images((0, 0), (128, 128), 3, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    if keyboard.is_pressed("r"):
        rotar_dado(screen, img, 300)
