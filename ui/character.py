import pygame

# Tyto 3 řádky bylo třeba zkopírovat do vedlejšího souboru, protože se mi házel Circular Import
WIDTH = 800
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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