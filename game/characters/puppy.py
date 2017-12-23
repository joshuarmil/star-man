import os
import pygame


class Puppy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image('pup.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 50

    @staticmethod
    def load_image(name):
        fullname = os.path.join('assets', name)
        try:
            image = pygame.image.load(fullname)

        except pygame.error:
            print('Cannot load image: ', name)
            raise SystemExit

        return image, image.get_rect()
