from levels.level1 import Level1
from levels.level2_instructions import Level2Instructions

import random
import pygame


class Level2(Level1):
    name = "Poziom drugi"
    lives = 3
    song_path = "audio/2.mp3"
    counter = 0 
    finish_points = 10
    instructions = Level2Instructions
    meteorites_count = 2


    
