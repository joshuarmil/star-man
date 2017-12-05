import pygame
from functions import load_image

class Puppy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('assets\pup.png', -1)

