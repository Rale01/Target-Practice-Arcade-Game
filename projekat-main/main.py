#paketi koje cemo koristiti
import pygame
import math

#bazicna podesavanja ekrana, fps-a, tajmera i nizova objekata u nasoj igri
pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 0