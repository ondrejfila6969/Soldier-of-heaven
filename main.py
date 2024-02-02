import pygame
from ui.character import Character

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

# Barva pozadí pro překrytí obrázku, zabraňuje duplikaci naší postavy
bg_color = (0, 200, 120)


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