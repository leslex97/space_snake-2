import pygame
import time

class LevelInstructions(object):
    name = "TRENING"
    instructions = ["Nieograniczona liczba zyc",
                        "Nie mozna umrzec",
                        "Poziom sluzy do trenowania umiejetnosci"]
    def __init__(self,game):
        self.game = game
        self.screen = self.game.screen
        self.screen_res = self.screen.get_size()
        self.font_size = 0

    

    def draw(self):
        self.screen.fill((0,0,0)) 
        self.draw_background()
        self.draw_instructions()
        pygame.display.update()
        self.stay_6_seconds()

    def draw_background(self):
        bg = pygame.image.load("img/pre_level.png")
        self.background = pygame.transform.scale(bg, self.screen_res)   
        self.screen.blit(self.background,(0,0))        
              
        
    def draw_instructions(self):
        header = self.render_text(self.name, 60)
        header[1].center = (self.screen_res[0]/2, 100)
        self.screen.blit(header[0],(header[1]))
        
        for idx,i in enumerate(self.instructions):
            number = idx + 1
            text = self.render_text(f"{number}.{i}", 32)
            text[1].center = (self.screen_res[0]/2, self.screen_res[1]/3 +((number)*50))
            self.screen.blit(text[0],text[1])

    def render_text(self, text, font_size):
        font = pygame.font.Font("fonts/SF Distant Galaxy.ttf",font_size)
        text_rendered = font.render(text,True,(40,0,50))
        textRect = text_rendered.get_rect()
        return [text_rendered, textRect]
    
    def stay_6_seconds(self):
        start_time = pygame.time.get_ticks()
        flag = True
        while flag:
            pressed = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 6000:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if pressed[pygame.K_SPACE]:
                    flag = False
                    return  
            # pygame.display.update()


            pygame.time.delay(100)