import pygame

class Wall(pygame.sprite.Sprite):
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("art (3).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()
  
  def verticalFaceLeft (self):
    self.image = pygame.transform.rotate(self.image, 90)
  
  def verticalFaceRight (self):
    self.image = pygame.transform.rotate(self.image, -90)
  
  def verticalFlip(self):
    self.image = pygame.transform.flip(self.image,False,True)
  
  def topLeftEdge (self):
    self.image = pygame.image.load("art (5).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def topRightEdge (self):
    self.image = pygame.image.load("art (6).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def bottomRightEdge (self):
    self.image = pygame.image.load("art (14).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def bottomLeftEdge (self):
    self.image = pygame.image.load("art (15).png")
    self.image = pygame.transform.scale(self.image,(40,40))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
  def platformPieceHorizontal(self):
    self.image = pygame.image.load("art (17).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def platformPieceVertical(self):
    self.image = pygame.image.load("art (17).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.rotate(self.image, 90)
  
  def endPieceRIGHT(self):
    self.image = pygame.image.load("art (16).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def endPieceLEFT(self):
    self.image = pygame.image.load("art (16).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.flip(self.image,True,False)
  
  def endPieceUP(self):
    self.image = pygame.image.load("art (16).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.rotate(self.image, 90)
  
  def endPieceDOWN(self):
    self.image = pygame.image.load("art (16).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.rotate(self.image, -90)
  
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def topRightCorner(self):
    self.image = pygame.image.load("art (18).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def topLeftCorner(self):
    self.image = pygame.image.load("art (19).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def bottomLeftCorner(self):
    self.image = pygame.image.load("art (20).png")
    self.image = pygame.transform.scale(self.image,(40,40))
  
  def bottomRightCorner(self):
    self.image = pygame.image.load("art (21).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
  def moveLeft (self):
    self.rect.x -= 9
  
  def moveRight(self):
    self.rect.x +=9
  
  def moveDown(self):
    self.rect.y += 9

  def moveUp(self):
    self.rect.y -= 9