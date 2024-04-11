from objects.rocket import Rocket
from objects.star import Star
import pygame
import sys, time
from levels.level_instructions import LevelInstructions
from objects.meteors import Meteors

class Level:
    name = "Trening"
    counter = 0   
    lives = False
    instructions = LevelInstructions
    finish_points = 9999
    meteorites_count = 0
    
    def __init__(self, game, difficulty = None):
        self.game = game
        self.screen = self.game.screen
        self.screen_res = self.screen.get_size()
        self.difficulty = difficulty
        self.font_size = int(.027*self.screen_res[0])
        self.level_active = True
        self.init_level()
        self.update()

        
    def init_level(self):
        self.show_instructions()
        self.player = Rocket(self,self.difficulty)
        self.meteors = Meteors(self.game, self.meteorites_count)
        self.star = Star(self,self.meteors.positions)
        self.max_tps = 85
        self.tps_delta = 0.0

        bg = pygame.image.load("img/space.png")
        self.bg = pygame.transform.scale(bg, self.screen_res)



    def update(self):
        while self.level_active:
            if self.lives == 0 and type(self.lives) == int:
                self.game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                            self.game.state= "MENU"
                            self.level_active = False
                            self.game.run()
                    

            self.tps_delta+=self.game.clock.tick()/1000.0
            while self.tps_delta> 1 / self.max_tps:
                self.tick()
                self.tps_delta -=1 /self.max_tps

            self.draw()
            self.catch()
            if self.meteorites_count > 0:
                self.meteor_colision()
            
            
    def draw(self):
        if self.counter == self.finish_points:
            self.finish_level()
        self.screen.fill((0,0,0))    
        self.screen.blit(self.bg,(0,0))
        self.player.draw()
        self.star.draw()
        self.meteors.draw()
        self.draw_level_name()
        self.draw_score()
        self.draw_lives()         
        pygame.display.update()
    
    def tick(self):
        self.player.tick()


    def draw_level_name(self):
        font = pygame.font.Font("fonts/SF Distant Galaxy.ttf", self.font_size)               
        text = font.render(self.name, True, (0,0,83))
        textRect = text.get_rect()
        textRect.center = (self.screen_res[0]/7, 40)
        self.screen.blit(text, textRect)
        
                    
    def draw_score(self):
        font = pygame.font.Font("fonts/SF Distant Galaxy.ttf", self.font_size)                   
        text = font.render(f'Wynik: {self.counter}', True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (self.screen_res[0]/2, 40)
        self.screen.blit(text, textRect)
    
    def draw_lives(self):
        if self.lives:
            heart = pygame.image.load("img/heart.png")
            heart_gray = pygame.image.load("img/heart_gray.png")
            heart_size =  (.037*self.screen_res[0],.06*self.screen_res[1])
            for i in range(1,4):
                heart = pygame.transform.scale(heart,heart_size)   
                if i>self.lives:
                    heart = pygame.transform.scale(heart_gray, heart_size)     
                self.screen.blit(heart, (self.screen_res[0]-(i*78), 20))
                     

    def catch(self):
        space_delta = 30
        x_catch_pos = abs(self.player.pos[0]-self.star.pos[0])
        y_catch_pos = abs(self.player.pos[1]-self.star.pos[1])
        
        if x_catch_pos < space_delta and y_catch_pos < space_delta:
            self.player.rocket_length+=1
            self.counter +=1
            del self.star
            self.star = Star(self,self.meteors.positions)
    
    
    def meteor_colision(self):
        space_delta = 30
        for meteor_positions in self.meteors.positions.values():
            for pos in meteor_positions:
                x_collision_pos = abs(self.player.pos[0]-pos[0])
                y_collision_pos = abs(self.player.pos[1]-pos[1])
                if x_collision_pos < space_delta and y_collision_pos < space_delta:    
                    self.life_lost()
                    
                    
    def life_lost(self):
        self.player = Rocket(self,self.difficulty, True)
        self.lives -= 1
        self.counter = 0 

    def game_over(self):
        game_over = pygame.image.load("img/game_over.png")
        game_over = pygame.transform.scale(game_over, self.screen_res)
        self.screen.blit(game_over,(0,0))
        pygame.display.update()
        time.sleep(5)
        self.game.state= "MENU"
        self.level_active = False
        self.game.run()
    def finish_level(self):
        self.level_active = False
        

    def show_instructions(self):
        self.instructions(game = self.game).draw() 


            

        