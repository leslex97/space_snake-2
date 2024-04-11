from levels.level import Level
from levels.level1_instructions import Level1Instructions

class Level1(Level):
    name = "Poziom pierwszy"
    lives = 3
    song_path = "audio/1.mp3"
    counter = 0 
    instructions = Level1Instructions
    finish_points = 10
    meteorites_count = 0
    
    def init_level(self):
        super().init_level()
        self.game.change_song(self.song_path)

        
    def tail_colision(self):
        player = [int(self.player.pos[0]), int(self.player.pos[1])]
        space_delta = 15

        if len(self.player.tail_pos_list)>4:
            colision_list = self.player.tail_pos_list[3:]
            for star_pos in colision_list: 
                x_catch_pos = abs(star_pos[0]-player[0])
                y_catch_pos = abs(star_pos[1]-player[1])
                if x_catch_pos < space_delta and y_catch_pos < space_delta:            
                    self.life_lost()


    def draw(self):
        self.tail_colision()
        super().draw()
        
