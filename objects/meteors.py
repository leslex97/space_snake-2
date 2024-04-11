import pygame, random
from pygame.math import Vector2
    
class Meteors(object):
    
    def __init__(self,game, meteors_count):
        self.meteorites = ['img/meteorite.png',
                      'img/meteorite_2.png',
                      'img/meteorite_3.png']
        self.game = game
        self.screen = self.game.screen
        self.size = self.game.screen.get_size()
        self.meteors_count = meteors_count
        self.positions = {}
        self.get_positions()
        
    def get_positions(self):
        for i in range(len(self.meteorites)):
            meteor_positions =[]

            for j in range(self.meteors_count):
                self.x = random.randint(0,self.size[0]-70)
                self.y = random.randint(60,self.size[1]-70)
                self.pos = Vector2(self.x,self.y)
                
                meteor_positions.append(self.pos)
                
            self.positions[i] = meteor_positions     
        print(self.positions)
        
    def draw(self):
        for idx,meteor in enumerate(self.meteorites):
            meteor_img = pygame.image.load(meteor)
            meteor_img = pygame.transform.scale(meteor_img, (.03*self.size[0],.05*self.size[1]))
            for pos in self.positions[idx] :
                self.screen.blit(meteor_img,pos)
    