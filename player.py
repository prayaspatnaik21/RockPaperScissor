import pygame

class Player():
    def __init__(self,x,y,width,height,color):
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.color  = color
        self.rect   = (x,y,width,height)
        self.vel    = 3

    def draw(self,win):
        """Draw a rectangle in the window"""
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        """To check the movement in the screen (Left movement , Right movement)"""
        keys = pygame.key.get_pressed() #Gives the dictionary of the key(Which key has been pressed ( 0 or 1))

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.update()

    def update(self): 
        self.rect   = (self.x,self.y,self.width,self.height)