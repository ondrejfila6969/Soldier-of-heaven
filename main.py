import pygame
from pygame import *

pygame.init()

WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World War 3")

# <333
pygame.mixer_music.load("Audio/Soldier Of Heaven.mp3")
pygame.mixer_music.play()


# OOP - ať nemusím kopírovat řádky pořád dokola a jenom vytvářet instance ... :/

class Character(pygame.sprite.Sprite):
    def __init__(self, posX, posY, scale):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Images/soldier.png")
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale - 20))) # Zmenšení obrázku na požadované rozměry
        self.rectangle = image.get_rect()
        self.rectangle.x = posX
        self.rectangle.y = posY

# Vytvořené instance
soldier = Character(200, 200, 0.13)
soldier2 = Character(400, 200, 0.13)
programRunning = True

while programRunning:

    screen.blit(soldier.image, soldier.rectangle)
    screen.blit(soldier2.image, soldier2.rectangle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programRunning = False   

    pygame.display.update()
pygame.quit()