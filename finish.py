import pygame
import math

class Finish(pygame.sprite.Sprite):
  
  def __init__ (self):
    super().__init__()
    #self.image = pygame.image.load("finish1.png")
    #self.image = pygame.transform.scale(self.image,(29,21))
    #self.rect = self.image.get_rect()
    self.images = []
    self.images.append(pygame.image.load("finish1.png"))
    self.images.append(pygame.image.load("finish1.png"))
    self.images.append(pygame.image.load("finish4.png"))
    self.images.append(pygame.image.load("finish3.png"))
    self.images.append(pygame.image.load("finish2.png"))
    
    self.index = 0
    self.image = self.images[self.index]
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()
    
  def update(self):
    self.index += 0.01
    
    if math.ceil(self.index) >= len(self.images):
      self.index = 0
      
    self.image = self.images[math.ceil(self.index)]
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def moveLeft (self):
    self.rect.x -= 9
  
  def moveRight(self):
    self.rect.x +=9
  
  def moveDown(self):
    self.rect.y += 9
  
  def moveUp(self):
    self.rect.y -= 9
