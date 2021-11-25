import pygame
import math

class Player(pygame.sprite.Sprite):
  
  def __init__ (self):
    super().__init__()
    self.images = []
    
    self.images.append(pygame.image.load('art.png'))
    self.images.append(pygame.image.load('art.png'))
    self.images.append(pygame.image.load('art (12).png'))
    self.images.append(pygame.image.load('art.png'))
    self.images.append(pygame.image.load('art (13).png'))
    
    self.index = 0
    self.image = self.images[self.index]
    self.image = pygame.transform.scale(self.image,(30,30))
    self.rect = self.image.get_rect()
    x = 30
    y = 30
  
  def idle(self):
        self.index += 0.03
 
        if math.ceil(self.index) >= len(self.images):
            self.index = 0
        
        self.image = self.images[math.ceil(self.index)]
        self.image = pygame.transform.scale(self.image,(30,30))
  
  def moveLeft (self):
    self.rect.x -=9
    self.image = pygame.image.load("art (7).png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  def moveRight(self):
    self.rect.x +=9
    self.image = pygame.image.load("art (7).png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  def moveDown(self):
    self.rect.y += 9
    self.image = pygame.image.load("art (7).png")
    self.image = pygame.transform.scale(self.image,(30,30))

  def moveUp(self):
    self.rect.y -= 9
    self.image = pygame.image.load("art (7).png")
    self.image = pygame.transform.scale(self.image,(30,30))
    
  def reset(self):
    self.image = pygame.image.load("art.png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  def flipLeft(self):
    self.image = pygame.transform.flip(self.image,True,False)
    self.image = pygame.transform.rotate(self.image, -90)

  def flipRight(self):
    self.image = pygame.transform.flip(self.image,False,False)
    self.image = pygame.transform.rotate(self.image, 90)
    
  def flip180(self):
    self.image = pygame.transform.rotate(self.image, 180)
  
