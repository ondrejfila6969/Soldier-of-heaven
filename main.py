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

# Zpomalení na FPS (snímky za sekundu)
clocks = pygame.time.Clock()
FPS = 60

# Směry:
direction_left = False
direction_right = False

# OOP - ať nemusím kopírovat řádky pořád dokola a jenom vytvářet instance ... :/
class Character(pygame.sprite.Sprite):
    def __init__(self, imageType, posX, posY, scale, speed):
        self.imageType = imageType # Budeme určovat, zda se jedná o naši hlavní postavu nebo enemáka
        self.speed = speed # Vzdálenost, o kteoru se přemisťuje
        pygame.sprite.Sprite.__init__(self)
        self.direction = 1 # Bude kontrolovat, jestli se hýbeme doleva nebo doprava a podle toho budeme překlápět obrázek
        self.flip = False # Hodnota, kterou budeme používat při překlápění obrázku
        self.animations = []
        self.animation = 0 # Jaká animace to bude
        image = pygame.image.load(f"Images/{self.imageType}.png") # Obrázek
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale - 20))) # Zmenšení obrázku na požadované rozměry
        self.rectangle = self.image.get_rect() # Musím dát pod obrázek rectangle, aby se nepřekryl pozadím
        self.rectangle.center = (posX, posY)
    
    def moveEvent(self, direction_left, direction_right):
        dx = 0 # změna souřadnice x
        dy = 0 # změna souřadnice y
        if direction_left:
            dx -= self.speed # Hýbeme se směrem doleva, čímž nám klesá souřadnice x, proto musíme nastavit rychlost na zápornou hodnotu
            self.flip = True
            self.direction = -1
        if direction_right:
            dx += self.speed
            self.flip = False
            self.direction = 1
        
        # Update pozice:
        self.rectangle.x += dx
        self.rectangle.y += dy
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rectangle)
# Barva pozadí (Prozatím, později dám do pozadí obrázky atd.) - triggruje mě, jak se mi ten obrázek neustále duplikuje .-.
bg_color = (0, 0, 0)

def renderBackground():
    screen.fill(bg_color)

# Vytvořená instance
soldier = Character("soldier", 200, 200, 0.13, 5)

# Main cyklus
programRunning = True
while programRunning:
    clocks.tick(FPS)
    renderBackground() # Pygame je pain, furt musím přemýšlet, kam to napsat, aby se něco nezkurvilo
    soldier.draw()
    soldier.moveEvent(direction_left, direction_right)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programRunning = False
        keys = pygame.key.get_pressed() # Všechny eventy se uloží do proměnné keys, je to jakýsi objekt
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                direction_left = True 
                direction_right = False
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                direction_right = True
                direction_left = False
            elif keys[pygame.K_ESCAPE]: # Pro rychlejší ukončení programu, ať nemusím najet myší na křížek jak opice
                programRunning = False
        if event.type == pygame.KEYUP:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                direction_left = False
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                direction_right = False

    pygame.display.update()
pygame.quit()