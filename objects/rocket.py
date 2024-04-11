import pygame,random
from pygame.math import Vector2
import time

class Rocket(object):
    
    def __init__(self,game,difficulty, died_flag=False):
        self.gravity = difficulty['gravity']
        self.speed= difficulty['speed']
        self.rocket_length = 0
        self.game = game
        self.pos_list = []
        self.tail_pos_list = []
        self.direction = Vector2(0,0)
        self.size = self.game.screen.get_size()
        start_pos_x = self.size[0] /2
        start_pos_y =  self.size[1] -100
        self.died_flag = died_flag
        self.pos = Vector2(start_pos_x, start_pos_y)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        #Naprawa buga pierwszej gwiazdy xd
        self.pos_list.append(Vector2(9999, 9999))
        
        
        rocket_img = pygame.image.load('img/spaceship.png')
        self.rocket_img = pygame.transform.scale(rocket_img, (.04*self.size[0],.065*self.size[1]))
        self.visible = True 
        
    def add_force(self,force):
        self.acc += force

    
    def tick(self):
        #input 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if self.pos[1] > 30:
                self.add_force(Vector2(0,-self.speed))
                self.direction= Vector2(0,+0.2)
        if pressed[pygame.K_DOWN]:
            if self.pos[1] < self.size[1]-100:
                self.add_force(Vector2(0,self.speed ))
                self.direction= Vector2(0,-0.2)
        if pressed[pygame.K_LEFT]:
            if self.pos[0] >30:
                self.add_force(Vector2(-self.speed,0 ))
                self.direction = Vector2(0.2,0)
        if pressed[pygame.K_RIGHT]: 
            if self.pos[0] < self.size[0]-100:

                self.add_force(Vector2(self.speed,0))
                self.direction = Vector2(-0.2,0)
        
        #Fizyka
        self.vel *= self.gravity
        diff_x = self.pos.x - self.pos_list[-1][0]
        diff_y = self.pos.y - self.pos_list[-1][1]
        
        self.slow_move(self.direction)

        
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        
        if self.died_flag:
            self.die_animation()
        
        
        
        if abs(diff_x) >=25 or abs(diff_y) >= 25: 
            self.pos_list.append([self.pos.x,self.pos.y])

    def slow_move(self, direction):
        if direction.x > 0 :
            if self.pos[0] > 30:
                self.vel -= direction
        elif direction.x < 0 :
            if self.pos[0] <self.size[0]-100 :
                self.vel -= direction
        elif direction.y > 0 :
            if self.pos[1] > 30:
                self.vel -= direction
        elif direction.y < 0 :
            if self.pos[1] < self.size[1]-100:
                self.vel -= direction
           


    def draw_tail(self,star_pos):
            star_img = pygame.image.load('img/star_smile.png')
            star_img = pygame.transform.scale(star_img, (.02*self.size[0],.03*self.size[1]))
            self.game.screen.blit(star_img,star_pos)
            
            
    def draw(self):
        if not self.died_flag or (self.died_flag and self.visible):
            angle = self.vel.angle_to(Vector2(0,-1))
            rocket = pygame.transform.rotate(self.rocket_img, angle)
            self.game.screen.blit(rocket, self.pos)
        
        if self.rocket_length > 0:
            self.tail_pos_list = []
            for i in range(self.rocket_length): 
                
                if len(self.pos_list) >3:
                    star_pos= Vector2(self.pos_list[-i-2][0]+15,self.pos_list[-i-2][1]+15)    
                else:
                    star_pos= Vector2(self.pos_list[-i][0]+15,self.pos_list[-i][1]+15)         
                self.tail_pos_list.append([int(star_pos[0]),int(star_pos[1])])
                self.draw_tail(star_pos)



    def die_animation(self):
        current_time = pygame.time.get_ticks()
        if not hasattr(self, 'blink_start_time'):
            self.blink_start_time = current_time

        if current_time - self.blink_start_time <= 2000:
            
            if (current_time - self.blink_start_time) % 600 < 300:
                self.visible = True
            else:
                self.visible = False
        else:

            self.died_flag = False
            self.visible = True 