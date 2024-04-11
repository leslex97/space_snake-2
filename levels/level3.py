from levels.level1 import Level1
from levels.level3_instructions import Level3Instructions

import random
import pygame


class Level3(Level1):
    name = "Poziom trzeci"
    lives = 3
    song_path = "audio/3.mp3"
    counter = 0 
    finish_points = 20
    instructions = Level3Instructions
    meteorites_count = 4


    
