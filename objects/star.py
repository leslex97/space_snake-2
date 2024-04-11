import pygame, random
from pygame.math import Vector2

class Star(object):
    
    def __init__(self,game,meteors):
        self.meteors = meteors
        self.game = game
        self.size = self.game.screen.get_size()

        self.x = random.randint(0,self.size[0]-70)
        self.y = random.randint(60,self.size[1]-70)
        self.pos = Vector2(self.x,self.y)
        self.set_star_position()
    

    def set_star_position(self):
        for i in range(5):
            print("heja")
            for meteor in self.meteors.values():
                if meteor != []:
                    for position in meteor:
                        good_render_flag = False
                        safe_distance = 200
                        while not good_render_flag:
                            meteor_x = position[0]
                            meteor_y = position[1]
                            delta_x = abs(self.x - meteor_x) 
                            delta_y = abs(self.y - meteor_y)
                            if delta_x < safe_distance or delta_y < safe_distance:
                                print(delta_x, delta_y)
                                self.x = random.randint(0, self.size[0]-70)
                                self.y = random.randint(60, self.size[1]-70)
                            else:
                                good_render_flag = True


    def draw(self):
        star_img = pygame.image.load('img/star.png')
        star_img = pygame.transform.scale(star_img, (.020*self.size[0],.033*self.size[1]))
        self.game.screen.blit(star_img, self.pos)
