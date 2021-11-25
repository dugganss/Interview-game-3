import pygame
import math

class Dot(pygame.sprite.Sprite):
  
  def __init__ (self):
    super().__init__()
    #self.image = pygame.image.load("dot_yellow.png")
    #self.image = pygame.transform.scale(self.image,(5,5))
    #self.rect = self.image.get_rect()
    self.images = []
    self.images.append(pygame.image.load("dot_yellow.png"))
    self.images.append(pygame.image.load("dot_pink.png"))
    self.images.append(pygame.image.load("dot_yellow.png"))
    self.images.append(pygame.image.load("dot_pink.png"))
    
    self.index = 0
    self.image = self.images[self.index]
    self.image = pygame.transform.scale(self.image,(5,5))
    self.rect = self.image.get_rect()
    
  def update(self):
    self.index += 0.03
    
    if math.ceil(self.index) >= len(self.images):
      self.index = 0
      
    self.image = self.images[math.ceil(self.index)]
    self.image = pygame.transform.scale(self.image,(5,5))
  
  def moveLeft (self):
    self.rect.x -= 9
  
  def moveRight(self):
    self.rect.x +=9
  
  def moveDown(self):
    self.rect.y += 9

  def moveUp(self):
    self.rect.y -= 9