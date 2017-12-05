import pygame
import os, sys

def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
        #image = pygame.transform.scale(image, (90, 90))
    except pygame.error:
        print('Cannot load image: ', name)
        raise SystemExit
    #image = image.convert()
    return image, image.get_rect()