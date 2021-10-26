import pygame
from network import Network
from player import Player
width  = 500
height = 500

win= pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

def redrawWindow(win,player1,player2):
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    network = Network()
    p = network.getP()
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2 = network.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)

main()