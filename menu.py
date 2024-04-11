import pygame
import sys, os

class Menu(object):
    song_path = "audio/menu.mp3"
    
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.screen_res = self.screen.get_size()
        self.font = pygame.font.Font("fonts/SF Distant Galaxy.ttf",32)
        self.selected_option = 0
        self.audio_options = [f'Poziom glosnosci: {self.game.volume_level}', 'powrot']
        self.menu_options = ["Rozpocznij Gre","Trening", "Opcje", "Autorzy", "Wyjdz"]
        self.settings_options = ["Rozmiar okna", "Audio", "Wroc"]
        self.diffs_options = ["Latwy", "Normalny", "Trudny"]

        
    def init_audio(self, song_path):
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.set_volume(self.game.volume_level / 100)
        pygame.mixer.music.play(-1)
       
    def run(self):
        self.init_audio(self.song_path)
        self.control_menu(self.menu_options, self.main_menu_choice)
        
    def draw_menu(self, menu_options):
        
        self.screen.fill((0, 0, 0))
        bg = pygame.image.load('img/menu_background.png')
        bg = pygame.transform.scale(bg, self.screen_res)
        self.screen.blit(bg,(0,0))
        
        header_font = pygame.font.Font("fonts/SF Distant Galaxy.ttf",64)               
        title_text = header_font.render("Space Snake", True, (150, 200,200))
        title_rect = title_text.get_rect(center=(self.screen_res[0] / 2, 100))
        self.screen.blit(title_text, title_rect)
        self.display_options(menu_options)
      
    def display_options(self,options):    
        for i, option in enumerate(options):
            text = self.font.render(option, True, (255, 255, 255) if i != self.selected_option else (150, 200, 230))
            text_rect = text.get_rect(center=(self.screen_res[0] / 2, (self.screen_res[1]/3) + i * 50))
            self.screen.blit(text, text_rect)
        
    def control_menu(self, options, method_to_execute): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        method_to_execute()
                    elif event.key == pygame.K_ESCAPE:
                        self.control_menu(self.menu_options, self.main_menu_choice) 

                    if method_to_execute == self.audio_settings_choice:
                        if event.key == pygame.K_RIGHT:
                            self.audio_options[0] = f'Poziom glosnosci: {self.game.volume_level}'
                            self.game.volume_level = min(100, self.game.volume_level + 1)
                            self.game.adjust_volume()
                            method_to_execute()
                            
                        elif event.key == pygame.K_LEFT:
                            self.audio_options[0] = f'Poziom glosnosci: {self.game.volume_level}'
                            self.game.volume_level = max(0, self.game.volume_level - 1) 
                            self.game.adjust_volume()
                            method_to_execute()
                    
                    
            self.draw_menu(options)
            pygame.display.update()
            self.game.clock.tick(30)


    def main_menu_choice(self):
            if self.selected_option == 0:  # Start Gry
                self.control_menu(self.diffs_options, self.show_diffs) 
            elif self.selected_option == 1: # Trening
                self.control_menu(self.diffs_options, self.start_trainig)
            elif self.selected_option == 2: #opcje
                self.control_menu(self.settings_options, self.settings_choice)            
            elif self.selected_option == 3:#autorzy 
                self.control_menu(['Pawel Woroniecki'], self.go_back) 
            elif self.selected_option == 4:  # Wyjscie
                pygame.quit()
                sys.exit()
    
                
    def settings_choice(self):
        if self.selected_option == 0:  # Ustawienia okna
            self.window_options = ['Tryb pelnoekranowy',
                                   '1920x1080', '1440x900', '1280x720','960x540'
                                   ,'Powrót']
            self.control_menu(self.window_options, self.window_settings_choice)
            
        
        elif self.selected_option == 1: #audio
            
            self.control_menu(self.audio_options, self.audio_settings_choice)
        
        elif self.selected_option == 2:# Wyjście do menu
            self.control_menu(self.menu_options, self.main_menu_choice)
    
    
    def window_settings_choice(self):
        sizes = [(1920,1080),(1440,900),(1280,720),(960,540) ]
        
        if self.selected_option == 0: #fullscren
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
        elif self.selected_option == len(self.window_options)-1: #powrót
            self.control_menu(self.settings_options, self.settings_choice) 
            
        else: # Wybór rozmiaru 
            x,y = sizes[self.selected_option-1][0] , sizes[self.selected_option-1][1]
            self.screen = pygame.display.set_mode((x,y))

        self.screen_res = self.screen.get_size()    

    def go_back(self):
            self.control_menu(self.menu_options, self.main_menu_choice) 
        

    def audio_settings_choice(self):
        if self.selected_option == 0:
            self.control_menu(self.audio_options, self.audio_settings_choice)
            
        elif self.selected_option == 1:
            self.control_menu(self.settings_options, self.settings_choice) 


    def show_diffs(self):
        self.diffs = {"Łatwy":[0.8, 1],  "Normalny":[0.83,1.2], "Trudny":[0.87,1.4]}
        difficulty = list(self.diffs)[self.selected_option]
        difficulty = {"gravity":self.diffs[difficulty][0],"speed":self.diffs[difficulty][1]}
        self.game.init_game(difficulty)


    def start_trainig(self):
        self.diffs = {"Łatwy":[0.8, 1],  "Normalny":[0.83,1.2], "Trudny":[0.87,1.4]}
        difficulty = list(self.diffs)[self.selected_option]
        difficulty = {"gravity":self.diffs[difficulty][0],"speed":self.diffs[difficulty][1]}
        self.game.init_game(difficulty, training_mode = True)
    

        