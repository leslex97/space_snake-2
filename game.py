import pygame
from menu import Menu
from levels.levels import levels

class Game:
    volume_level = 30
    clock = pygame.time.Clock()
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        pygame.display.set_caption("Space Snake")
        pygame.mouse.set_visible(False)
        self.clock = self.clock
        self.running = True
        self.state = "MENU"
        self.menu = Menu(self)
        self.level_list = levels
        self.level = None
        self.training_mode = False

        

        
    def run(self):
        while self.running:
            if self.state == "MENU":
                self.menu.run()
                if self.menu.start_game_selected:
                    self.state = "GAME"
                    
                elif self.menu.exit_selected:
                    self.state = "EXIT"
                    
            elif self.state == "GAME":
                self.run_game()
            elif self.state == "EXIT":
                self.running = False
                
                
            pygame.display.update()
            self.clock.tick(60) 
            
    def change_state(self, new_state):
        self.state = new_state

    def change_song(self,song_path):  
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)
    
    def adjust_volume(self):
        pygame.mixer.music.set_volume(self.volume_level/100)
        
        
    def init_game(self, difficulty, training_mode = False):
        print(training_mode)
        self.training_mode = training_mode
        self.difficulty = difficulty
        self.state = "GAME"
        self.run()


    def run_game(self):
    
        if not self.training_mode:
            for level in self.level_list.keys():
                if level >0:
                    self.level_list[level](self,self.difficulty)
        else:
            self.level_list[0](self,self.difficulty)
           
    
if __name__ == "__main__":
    game = Game()
    game.run()