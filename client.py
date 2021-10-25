import pygame
from network import Network
width  = 500
height = 500

win= pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

clientNumber = 0

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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player1,player2):
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    network = Network()
    startPos = read_pos(network.getPos())
    Player1 = Player(startPos[0],startPos[1],100,100,(0,255,0))
    Player2 = Player(0, 0 ,100,100,(255,0,0))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)

        p2Pos = read_pos(network.send(make_pos((Player1.x, Player1.y))))
        Player2.x = p2Pos[0]
        Player2.y = p2Pos[1]
        Player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        Player1.move()
        redrawWindow(win,Player1,Player2)

main()