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
    guns.append(pygame.transform.scale(pygame.image.load(f'projekat-main/assets/guns/{i}.png'), (100, 100)))

#metoda za pistolj i rotaciju njegovu
def draw_gun():
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH / 2, HEIGHT - 200)
    #boja kursora
    lasers = ['red', 'green', 'orange']
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != gun_point[0]:
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    else:
        slope = -100000
    angle = math.atan(slope)
    rotation = math.degrees(angle)
    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(guns[level - 1], True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH / 2 - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
    else:
        gun = guns[level - 1]
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH / 2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)





#pocetna verzija ekrana
run = True
while run:
    timer.tick(fps)

    screen.fill('black')
    screen.blit(bgs[level-1], (0,0))
    screen.blit(banners[level-1], (0,HEIGHT - 200))


    if level > 0 :
        draw_gun()

    #ako smo kliknuli X i zatvorili prozor prekida se igrica
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()