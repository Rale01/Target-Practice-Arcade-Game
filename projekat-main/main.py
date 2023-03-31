#paketi koje cemo koristiti
import pygame
import math

#bazicna podesavanja ekrana, fps-a, tajmera i nizova objekata u nasoj igri
pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('projekat-main/assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 1

#METODE ZA UCITAVANJE OBJEKATA U IGRICI
#ucitavanje pozadina, banera i pistolja
for i in range(1, 4):
    bgs.append(pygame.image.load(f'projekat-main/assets/bgs/{i}.png'))
    banners.append(pygame.image.load(f'projekat-main/assets/banners/{i}.png'))
    guns.append(pygame.image.load(f'projekat-main/assets/guns/{i}.png'))






#pocetna verzija ekrana
run = True
while run:
    timer.tick(fps)

    screen.fill('black')
    screen.blit(bgs[level-1], (0,0))
    screen.blit(banners[level-1], (0,HEIGHT - 200))

    #ako smo kliknuli X i zatvorili prozor prekida se igrica
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()