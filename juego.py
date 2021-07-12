import pygame, sys
import random


class Runner():
    
    __costumes = ("octopus", "carpincho","turtle", "prawn")
    
    def __init__(self, x=0, y=0, costume = "turtle"):
        self.costume = pygame.image.load('images/{}.png'.format(costume))
        self.position = [x, y]
        self.name = costume
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)


class Game():
    runners = []
    __posi = (160, 200, 240, 280)
    __startLine = 5
    __finishLine = 620
    __names = ("Octi", "Carpi", "Morrocoy", "Dobladita")
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load('images/background.jpg')
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posi[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            for r in range(4):
                self.runners[r].avanzar()
            
            for r in range(4):
                if self.runners[r].position[0] >= self.__finishLine:
                    print("{} ha ganado".format(self.runners[r].name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0, 0))
            for r in range(4):
                self.__screen.blit(self.runners[r].costume, self.runners[r].position)
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    pygame.font.init() 
    game.competir()


