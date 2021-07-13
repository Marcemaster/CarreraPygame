import pygame, sys
import random


class Runner():
    
    
    
    def __init__(self, x=0, y=0):
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 3)


class Game():
    runners = []
    __posi = (140, 180, 220, 260, 300)
    __startLine = 5
    __finishLine = 620
    __names = ("Octi", "Pichi", "Morrocoy", "Gambi", "Dobladita")
    __costumes = ("octopus", "fish","turtle", "prawn","moray")
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load('images/background.png')
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(5):
            theRunner = Runner(self.__startLine, self.__posi[i])
            theRunner.name = self.__names[i]
            theRunner.costume = pygame.image.load('images/{}.png'.format(self.__costumes[i]))
            self.runners.append(theRunner)
            
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            for activerunner in self.runners:
                activerunner.avanzar()
                if activerunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activerunner.name))
                    gameOver = True                    
            
            self.__screen.blit(self.__background, (0, 0))
            
            for runner in self.runners:
                self.__screen.blit(runner.costume, runner.position)
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                

if __name__ == '__main__':
    game = Game()
    pygame.init() 
    game.competir()


