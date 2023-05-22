#TARGET PRACTICE IGRICA

#Assets folder sadrzi celokupan dizajn banera, poyadina, fontova, pistolja, ikona, menija, zvukova, meta 
#koji smo koristili za izradu nase igrice. Dizajn je radjen koristeci Canv-u(sam dizajn), 
#Photo Room Background Remover(sklanjanje pozadine slika u png formatu),
#Convert.com(konverzija ostalih formata u .png format), WatermarkRemover.io(sklanjanje watermarka sa slika),
#Fotor AI(za kreativno generisanje pozadina menija)

#Za upravljanje i organizaciju korisnika kroz samu igricu putem 
#klikova misem na dugmad, neprijatelje, itd., koriscene su precizne koordinate u pixelima 
#stoga vodili smo racuna o velicini elemenata u assets folderu!

#1. IMPORTUJEMO BIBLIOTEKE KOJE CEMO KORISTITI

#Pygame je popularna otvorena biblioteka u Pythonu 
#koja pruža okvir za kreiranje i razvoj 2D video igara, 
#multimedijalnih aplikacija i interaktivnih iskustava. 
#Ona pruža niz funkcionalnosti za obradu grafike, 
#zvuka i korisničkog unosa, omogućavajući programerima 
#da lako dizajniraju i implementiraju igre na različitim platformama.
import pygame
#Math biblioteka je standardna biblioteka u jeziku Python 
#koja pruža funkcionalnosti za matematičke operacije 
#i manipulaciju numeričkim podacima. Ova biblioteka sadrži 
#različite matematičke funkcije kao što su trigonometrija, 
#eksponencijalne funkcije, logaritmi, korenovanje, 
#zaokruživanje brojeva i mnoge druge
import math


#2. INICIJALIZACIJA PYGAME PROZORA I POSTAVLJANJE OSNOVNIH PARAMETARA ZA PRIKAZIVANJE IGRE

#inicijalizuje sve module Pygame biblioteke i postavlja sve neophodne parametre za pokretanje igre.
pygame.init()
#postavlja broj frejmova po sekundi na 60, što je standardna vrednost za većinu video igara.
fps = 60
#kreira objekat Clock koji će se koristiti za održavanje željenog broja frejmova po sekundi.
timer = pygame.time.Clock()
#definišu različite fontove koji će se koristiti za prikazivanje teksta u igri. 
#Ovi fontovi se učitavaju iz odgovarajućih fajlova.
font = pygame.font.Font('projekat-main/assets/font/myFont.ttf', 20)
score_font = pygame.font.Font('projekat-main/assets/font/myFont.ttf', 30)
big_font = pygame.font.Font('projekat-main/assets/font/myFont.ttf', 60)
#definišu širinu i visinu prozora igre.
WIDTH = 900
HEIGHT = 800
# kreira prozor igre sa zadatim dimenzijama.
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# postavlja naslov prozora igre na "TARGET PRACTICE".
pygame.display.set_caption("TARGET PRACTICE")
#učitava sliku ikonice igre
icon = pygame.image.load("projekat-main/assets/icon/icon.png")
#postavlja ikonicu prozora igre na prethodno učitanu sliku.
pygame.display.set_icon(icon)


#3. INICIJALIZACIJA PROMENLJIVIH KOJE CE SE KORISTITI U IGRI I UCITAVANJE ODGOVARAJUCIH SLIKA ZA PRIKAZ NA EKRANU

#niz u kome cemo smestati razlicite pozadine iz assets foldera u zavisnosti od nivoa
bgs = []
#niz u kome cemo smestati razlicite banere iz assets foldera u zavisnosti od nivoa
banners = []
#niz u kome cemo smestati razlicite puske iz assets foldera u zavisnosti od nivoa
guns = []
#dvodimenzionalna lista koja će sadržati slike za ciljeve u igri, razvrstane prema njihovim nivoima i težinama.
target_images = [[], [], []]
#rečnik koji definiše broj poena koji se dobija za svaki pogodak u zavisnosti od nivoa i težine cilja.
targets = {1: [10, 5, 3],
           2: [12, 8, 5],
           3: [15, 12, 8, 3]}
#promenljiva koja se odnosi na trenutni nivo
level = 0
#promenljiva koja se odnosi na poene
points = 0
#promenljiva koja se odnosi na ukupan broj pucanja
total_shots = 0
#promenljiva koja se odnosi na razlicite modove u igrici: 0 = freeplay, 1 - accuracy, 2 - timed
mode = 0
#promenljiva koja se odnosi na broj preostale municije
ammo = 0
#promenljiva koja se odnosi na vreme koje je proslo
time_passed = 0
#promenljiva koja se odnosi na vreme koje je preostalo
time_remaining = 0
#brojac koji cemo posle koristiti za podesavanja oko FPS-a
counter = 1
#definisanje promenljivih u kojima cemo cuvati najbolje ostvarene poene po razlicitim modovima
best_freeplay = 0
best_ammo = 0
best_timed = 0
#logicka promenljiva kojom cemo proveravati pucanje
shot = False
#Logicke promenjljive koje ce nam pomoci da menjamo kroz raylicite ekrane u igri
menu = True
game_over = False
pause = False
#koristice se za definisanje razlicitih mogucih stanja igre posle u funkcijama ispod.
clicked = False
write_values = False
new_coords = True
#su liste za koordinate koje će se koristiti za prikazivanje ciljeva različitih nivoa.
one_coords = [[], [], []]
two_coords = [[], [], []]
three_coords = [[], [], [], []]
#razliciti ekrani(meniji) u igri ucitani iz assets foldera
menu_img = pygame.image.load(f'projekat-main/assets/menus/mainMenu.png')
game_over_img = pygame.image.load(f'projekat-main/assets/menus/gameOver.png')
pause_img = pygame.image.load(f'projekat-main/assets/menus/pause.png')


#4. UCITAVANJE SLIKA ZA POZADINE, NATPISE, ORUZJE I CILJEVE U IGRI
#I NJIHOVA ORGANIZACIJA PO LISTIMA ZA KASNIJE KORISCENJE U IGRI

#prolazi kroz brojeve 1, 2 i 3 koji predstavljaju nivoe ili vrste slika koje se učitavaju.
for i in range(1, 4):
    #dodaje u listu bgs sliku pozadine za trenutni nivo i.
    bgs.append(pygame.image.load(f'projekat-main/assets/bgs/{i}.png'))
    #dodaje u listu banners sliku natpisa za trenutni nivo i.
    banners.append(pygame.image.load(f'projekat-main/assets/banners/{i}.png'))
    #dodaje u listu guns sliku oružja za trenutni nivo i. 
    #Slika oružja se takođe skalira na veličinu 100x100 piksela.
    guns.append(pygame.transform.scale(pygame.image.load(f'projekat-main/assets/guns/{i}.png'), (100, 100)))
    #za 1 i 2 nivo posto su iste tezine(postoje samo 3 tezine za ciljeve)
    if i < 3:
        #petlja koja sa j prolazi kroz brojeve 1, 2 i 3 koji predstavljaju težine ciljeva.
        for j in range(1, 4):
            # dodaje u listu target_images sliku cilja za trenutni nivo i i težinu j. 
            # Slika cilja se takođe skalira na odgovarajuću veličinu koja se smanjuje sa svakom težinom.
            target_images[i - 1].append(pygame.transform.scale(
                pygame.image.load(f'projekat-main/assets/targets/{i}/{j}.png'), (120 - (j * 18), 80 - (j * 12))))
    #za 3 nivo posto postoje 4 tezine za ciljeve        
    else:
        #prolazi kroz brojeve 1, 2, 3 i 4 koji predstavljaju težine ciljeva.
        for j in range(1, 5):
            #dodaje u listu target_images sliku cilja za trenutni nivo i 
            #i težinu j. Slika cilja se takođe skalira na odgovarajuću 
            #veličinu koja se smanjuje sa svakom težinom.
            target_images[i - 1].append(pygame.transform.scale(
                pygame.image.load(f'projekat-main/assets/targets/{i}/{j}.png'), (120 - (j * 18), 80 - (j * 12))))



#5. CITA PODATKE O NAJBOLJIM REZULTATIMA IZ FAJLA, INICIJALIZUJE ZVUKOVE U IGRI 
#I POKRECE REPRODUKCIJU POZADINSKE MUZIKE I ODGOVARAJUCIH ZVUKOVA U IGRI.

#otvara tekstualni fajl 'high_scores.txt' u režimu čitanja.
file = open('projekat-main/high_scores.txt', 'r')
#čita sadržaj fajla i čuva ga kao listu linija teksta.
read_file = file.readlines()
#zatvara fajl nakon čitanja.
file.close()
#inicijalizuju se kao brojevi konvertovani iz prvih tri linija pročitanog fajla.
#Predstavljaju najbolje skorove u sva tri od modova u igri
best_freeplay = int(read_file[0])
best_ammo = int(read_file[1])
best_timed = int(read_file[2])
#inicijalizuje Pygame mixer modul za reprodukciju zvuka.
pygame.mixer.init()
#učitava muzički fajl 'bg_music.mp3' koji će se reprodukovati kao pozadinska muzika.
pygame.mixer.music.load('projekat-main/assets/sounds/bg_music.mp3')
#učitava zvuk fajla 'Dying fish.wav' koji će se koristiti za zvuk prilikom gađanja ribe.
fish_sound = pygame.mixer.Sound('projekat-main/assets/sounds/Dying fish.wav')
#postavlja jačinu zvuka za zvuk ribe na 0.8 (80% jačine).
fish_sound.set_volume(.8)
#učitava zvuk fajla 'Drill Gear.mp3' koji će se koristiti za zvuk prilikom gađanja ptica.
bird_sound = pygame.mixer.Sound('projekat-main/assets/sounds/Drill Gear.mp3')
# postavlja jačinu zvuka za zvuk ptica na 0.5 (50% jačine).
bird_sound.set_volume(.5)
# učitava zvuk fajla 'Laser Gun.wav' koji će se koristiti za zvuk prilikom ispaljivanja lasera.
laser_sound = pygame.mixer.Sound('projekat-main/assets/sounds/Laser Gun.wav')
#postavlja jačinu zvuka za zvuk lasera na 0.5 (50% jačine).
laser_sound.set_volume(.5)
#pokreće reprodukciju pozadinske muzike.
pygame.mixer.music.play()

#6. FUNKCIJE

#FUNKCIJA ZA AZURIRANJE INFORMACIJA O REZULTATIMA I STANJU IGRE NA EKRANU TOKOM IGRANJA
def draw_score():
    #koristi font za renderovanje teksta koji prikazuje broj osvojenih poena. 
    # Tekst se formira u obliku "Points: {points}" gde se {points} zamenjuje s
    # tvarnom vrednošću broja poena. Boja teksta je bela.
    points_text = font.render(f'Points: {points}', True, 'white')
    #iscrtava tekst na ekranu na poziciji (320, 660).
    screen.blit(points_text, (320, 660))
    #iscrtava tekst koji prikazuje ukupan broj ispaljenih metaka.
    shots_text = font.render(f'Total Shots: {total_shots}', True, 'white')
    screen.blit(shots_text, (320, 687))
    #iscrtava tekst koji prikazuje proteklo vreme u igri.
    time_text = font.render(f'Time Elapsed: {time_passed}', True, 'white')
    screen.blit(time_text, (320, 714))
    #Nakon toga, u zavisnosti od vrednosti promenljive mode, 
    #određuje se prikazivanje odgovarajućeg teksta:
    #Ako je mode jednak 0, prikazuje se tekst "Freeplay!".
    if mode == 0:
        mode_text = font.render(f'Freeplay!', True, 'white')
    #Ako je mode jednak 1, prikazuje se tekst "Ammo Remaining: {ammo}" 
    #koji prikazuje preostali broj metaka.
    if mode == 1:
        mode_text = font.render(f'Ammo Remaining: {ammo}', True, 'white')
    #Ako je mode jednak 2, prikazuje se tekst "Time Remaining: {time_remaining}" 
    #koji prikazuje preostalo vreme.
    if mode == 2:
        mode_text = font.render(f'Time Remaining {time_remaining}', True, 'white')
    #Na kraju, funkcija iscrtava odabrani tekst na ekranu na odgovarajućoj poziciji.
    screen.blit(mode_text, (320, 741))

#FUNKCIJA ZA ISCRTAVANJE ORUZJA I LASERA NA EKRANU U ZAVISNOSTI OD POZICIJE MISA I STANJA TASTERA MISA TOKOM IGRANJA
def draw_gun():
    #dobija trenutnu poziciju miša.
    mouse_pos = pygame.mouse.get_pos()
    #određuje koordinate tačke oružja na ekranu.
    gun_point = (WIDTH / 2, HEIGHT - 200)
    #predstavlja listu boja za lasere u zavisnosti od nivoa
    lasers = ['red', 'purple', 'green']
    # proverava stanje pritisnutosti tastera miša.
    clicks = pygame.mouse.get_pressed()
    #izračunava ugao rotacije oružja u odnosu na poziciju miša:
    #Ako pozicija miša nije ista kao pozicija tačke oružja
    if mouse_pos[0] != gun_point[0]:
        #računa se nagib prave koja prolazi kroz tačku oružja i poziciju miša.
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    #Ako je pozicija miša ista kao pozicija tačke oružja
    else:
        #agib se postavlja na vrlo veliku negativnu 
        #vrednost (slope = -100000) kako bi se izbeglo deljenje nulom.
        slope = -100000
    #računa ugao u radianima na osnovu nagiba prave.
    angle = math.atan(slope)
    #konvertuje ugao iz radijana u stepene
    rotation = math.degrees(angle)
    #Ako je pozicija miša levo od polovine širine ekrana (mouse_pos[0] < WIDTH / 2), 
    #oružje se reflektuje horizontalno koristeći pygame.transform.flip() 
    # kako bi se dobila simetrična slika oružja.
    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(guns[level - 1], True, False)
        if mouse_pos[1] < 600:
            # rotira se i iscrtava slika oružja gun na odgovarajućoj poziciji.
            # Ako je pritisnut levi taster miša (clicks[0]), iscrtava se kružnica lasera na poziciji miša.
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH / 2 - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
    #Ako je pozicija miša desno od polovine širine ekrana, 
    #iscrtava se neraspložena slika oružja gun na odgovarajućoj poziciji. 
    #Ako je pritisnut levi taster miša (clicks[0]), iscrtava se kružnica lasera na poziciji miša.
    else:
        gun = guns[level - 1]
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH / 2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)



#FUNKCIJA ZA POMERANJE META U IGRI SA LEVE NA DESNU STRANU
def move_level(coords):
    #Prvo se proverava vrednost promenljive level 
    #da bi se odredio maksimalni broj meta na tom nivou. 
    #Ako je level jednak 1 ili 2, maksimalna vrednost je 3, inače je 4.
    if level == 1 or level == 2:
        max_val = 3
    else:
        max_val = 4
    #i je maksimalni broj meta
    for i in range(max_val):
        #Zatim se prolazi kroz sve koordinate meta u listi coords
        for j in range(len(coords[i])):
            my_coords = coords[i][j]
            #Ako x-koordinata meta (my_coords[0]) postane manja od -150, 
            #to znači da je meta prešla levi kraj ekrana. U tom slučaju, 
            #ažuriramo x-koordinatu tako da se meta pojavi sa desne strane 
            #ekrana na istoj y-koordinati.
            if my_coords[0] < -150:
                coords[i][j] = (WIDTH, my_coords[1])
            #Ako x-koordinata meta nije manja od -150, 
            #ažuriramo x-koordinatu tako što joj oduzmemo vrednost 2 na osnovu 
            #nivoa igre (2 ** i). To postepeno pomeranje će izazvati kretanje 
            #meta s leve strane ekrana ka desnoj strani.
            else:
                coords[i][j] = (my_coords[0] - 2 ** i, my_coords[1])
    #ažurirane koordinate meta se vraćaju kao rezultat funkcije.
    return coords



#FUNKCIJA ZA ISCRTAVANJE META NA EKRANU I DOBIJANJE 
#PRAVOUGAONIKA KOJI IH OGRANIČAVAJU. PRAVOUGAONICI SE KORISTE ZA 
#DETEKCIJU SUDARA I INTERAKCIJU SA METAMA TOKOM IGRE.
def draw_level(coords):
    #Prvo se proverava vrednost promenljive level 
    #da bi se odredio broj različitih vrsta meta na tom nivou. 
    # Ako je level jednak 1 ili 2, inicijalizuje se lista target_rects sa tri prazne liste. 
    # Inače, inicijalizuje se sa četiri prazne liste.
    if level == 1 or level == 2:
        target_rects = [[], [], []]
    else:
        target_rects = [[], [], [], []]
    #Zatim se prolazi kroz sve koordinate meta u listi coords
    for i in range(len(coords)):
        for j in range(len(coords[i])):
            #Kreira se pravougaonik target_rect za svaku koordinatu. 
            #Koordinate pravougaonika se formiraju na osnovu koordinata mete 
            #tako da se pomera za 20 po x-osi i ostaje na istoj poziciji po y-osi, 
            #dok se dimenzije pravougaonika smanjuju kako se ide na viši nivo (60 - i * 12).
            target_rects[i].append(pygame.rect.Rect((coords[i][j][0] + 20, coords[i][j][1]),
                                                    (60 - i * 12, 60 - i * 12)))
            #Iscrtavaju se slike meta target_images[level - 1][i] na 
            #odgovarajućim koordinatama coords[i][j] na ekranu.
            screen.blit(target_images[level - 1][i], coords[i][j])
    #Na kraju, funkcija vraća listu pravougaonika target_rects koji predstavljaju okvire oko svake mete.
    return target_rects



#FUNKCIJA ZA PROVERU DA LI JE META POGODJENA KLIKOM MIŠA I ZA AŽURIRANJE REZULTATA IGRE
#prima listu pravougaonika koje predstavljaju mete targets i listu koordinata meta coords kao argumente
def check_shot(targets, coords):
    #globalna promenljiva points kako bi se omogućilo ažuriranje broja poena tokom funkcije.
    global points
    #Zatim se uzima trenutna pozicija miša mouse_pos koristeći funkciju pygame.mouse.get_pos().
    mouse_pos = pygame.mouse.get_pos()
    #Zatim se prolazi kroz sve mete u listi targets:
    for i in range(len(targets)):
        #Unutar petlje se prolazi kroz sve pravougaonike mete targets[i][j]
        for j in range(len(targets[i])):
            #Za svaki pravougaonik se proverava da li je pozicija miša 
            #unutar tog pravougaonika pomoću funkcije collidepoint(mouse_pos). 
            #Ako jeste, to znači da je meta pogodjena.
            if targets[i][j].collidepoint(mouse_pos):
                #Kada se meta pogodi, koordinata te mete se uklanja iz liste coords, 
                #a broj poena se povećava za 10 plus 10 puta kvadrat nivoa igre (10 + 10 * (i ** 2)).
                coords[i].pop(j)
                points += 10 + 10 * (i ** 2)
                #Zatim se na osnovu nivoa igre (level) reprodukuje odgovarajući zvuk. 
                #Ako je nivo 1, reprodukuje se zvuk bird_sound, ako je nivo 2, 
                #reprodukuje se zvuk fish_sound, a ako je nivo 3, 
                #reprodukuje se zvuk laser_sound.
                if level == 1:
                    bird_sound.play()
                elif level == 2:
                    fish_sound.play()
                elif level == 3:
                    laser_sound.play()
    #funkcija vraća ažuriranu listu koordinata coords
    return coords




#FUNKCIJA ZA ISCRTAVANJE GLAVNOG MENIJA IGRE 
#I OBRADU INTERAKCIJA KORISNIKA SA MENIJEM, OMOGUĆAVAJUĆI 
#ODABIR REŽIMA IGRE I POČETAK NOVE IGRE.
def draw_menu():
    #Unutar funkcije se koristi globalne promenljive 
    #kako bi se omogućilo ažuriranje njihovih vrednosti tokom izvršavanja funkcije.
    global game_over, pause, mode, level, menu, time_passed, total_shots, points, ammo
    global time_remaining, best_freeplay, best_ammo, best_timed, write_values, clicked, new_coords
    game_over = False
    pause = False
    #Zatim se koristi funkcija screen.blit() za iscrtavanje 
    #slike menija menu_img na početnu poziciju (0, 0) na ekranu.
    screen.blit(menu_img, (0, 0))
    #Nakon toga se dobija trenutna pozicija miša mouse_pos i 
    # stanje pritisaka na dugme miša clicks pomoću funkcije 
    # pygame.mouse.get_pos() i pygame.mouse.get_pressed().
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    #Definišu se pravougaonici za dugmiće na meniju 
    #(freeplay_button, ammo_button, timed_button, reset_button) pomoću funkcije pygame.rect.Rect().
    #Koristeći funkciju screen.blit(), ispisuju se vrednosti najboljih rezultata 
    #(best_freeplay, best_ammo, best_timed) na odgovarajućim pozicijama na ekranu.
    freeplay_button = pygame.rect.Rect((170, 524), (260, 100))
    screen.blit(score_font.render(f'{best_freeplay}', True, 'white'), (320, 565))
    ammo_button = pygame.rect.Rect((475, 524), (260, 100))
    screen.blit(score_font.render(f'{best_ammo}', True, 'white'), (650, 565))
    timed_button = pygame.rect.Rect((170, 661), (260, 100))
    screen.blit(score_font.render(f'{best_timed}', True, 'white'), (340, 713))
    reset_button = pygame.rect.Rect((475, 661), (260, 100))
    #Zatim se vrši provera da li je miš unutar pravougaonika određenih dugmića 
    #i da li je korisnik kliknuo levim tasterom miša. Ako je to slučaj i 
    # ako klik još nije registrovan (da bi se izbegla višestruka obrada klika), 
    # vrši se odgovarajuće ažuriranje promenljivih mode, level, menu, time_passed, 
    # total_shots, points, ammo, time_remaining, best_freeplay, best_ammo, best_timed, 
    # clicked i new_coords.

    #1)Ako je pritisnuto dugme za Freeplay, postavljaju se odgovarajuće vrednosti za režim, nivo i ostale promenljive.
    if freeplay_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 0
        level = 1
        menu = False
        time_passed = 0
        total_shots = 0
        points = 0
        clicked = True
        new_coords = True
    #2)Ako je pritisnuto dugme za Ammo, postavljaju se odgovarajuće vrednosti za režim, nivo, broj metaka i ostale promenljive.
    if ammo_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 1
        level = 1
        menu = False
        time_passed = 0
        ammo = 81
        total_shots = 0
        points = 0
        clicked = True
        new_coords = True
    #3)Ako je pritisnuto dugme za Timed, postavljaju se odgovarajuće vrednosti za režim, 
    # nivo, preostalo vreme, ukupno vreme, broj pogodaka i ostale promenljive.
    if timed_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        mode = 2
        level = 1
        menu = False
        time_remaining = 30
        time_passed = 0
        total_shots = 0
        points = 0
        clicked = True
        new_coords = True
    #4)Ako je pritisnuto dugme za Reset, resetuju se najbolji rezultati na nulu.
    if reset_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        best_freeplay = 0
        best_ammo = 0
        best_timed = 0
        clicked = True
        write_values = True


#FUNKCIJA ZA ISCRTAVANJE EKRANA SA PORUKOM "GAME OVER" I OPCIJAMA ZA 
#POVRATAK NA GLAVNI MENI ILI IZLAZ IZ IGRE NAKON ŠTO IGRAČ ZAVRŠI IGRU.
def draw_game_over():
    #Unutar funkcije se koristi globalne promenljive 
    #kako bi se omogućilo ažuriranje njihovih vrednosti 
    #tokom izvršavanja funkcije.
    global clicked, level, pause, game_over, menu, points, total_shots, time_passed, time_remaining
    #Zatim se vrši odabir vrednosti koja će biti prikazana kao rezultat na ekranu na osnovu vrednosti promenljive mode. 
    #Ako je mode jednako 0, prikazuje se vreme proteklo tokom igre (time_passed), 
    #u suprotnom prikazuje se broj poena (points).
    if mode == 0:
        display_score = time_passed
    else:
        display_score = points
    #oristeći funkciju screen.blit(), iscrtava se slika ekrana sa porukom "Game Over" 
    #(game_over_img) na poziciji (0, 0) na ekranu.
    screen.blit(game_over_img, (0, 0))
    #Nakon toga se dobija trenutna pozicija miša mouse_pos i stanje pritisaka na dugme miša clicks 
    #pomoću funkcija pygame.mouse.get_pos() i pygame.mouse.get_pressed().
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    #Definišu se pravougaonici za dugmiće na ekranu za povratak na glavni meni (menu_button) i 
    #izlaz iz igre (exit_button) pomoću funkcije pygame.rect.Rect().
    exit_button = pygame.rect.Rect((170, 661), (260, 100))
    menu_button = pygame.rect.Rect((475, 661), (260, 100))
    #Koristeći funkciju screen.blit(), ispisuje se vrednost rezultata 
    #(display_score) na odgovarajućoj poziciji na ekranu.
    screen.blit(big_font.render(f'{display_score}', True, 'white'), (640, 560))
    #Zatim se vrši provera da li je miš unutar pravougaonika određenih dugmića i 
    #da li je korisnik kliknuo levim tasterom miša. Ako je to slučaj i ako klik 
    #još nije registrovan (da bi se izbegla višestruka obrada klika), vrši se 
    #odgovarajuće ažuriranje promenljivih clicked, level, pause, game_over, menu, 
    #points, total_shots, time_passed i time_remaining.

    #1)Ako je pritisnuto dugme za povratak na glavni meni, 
    #postavljaju se odgovarajuće vrednosti za promenljive 
    #kako bi se vratio na glavni meni i resetovali rezultati.
    if menu_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        clicked = True
        level = 0
        pause = False
        game_over = False
        menu = True
        points = 0
        total_shots = 0
        time_passed = 0
        time_remaining = 0
    #2)Ako je pritisnuto dugme za izlaz iz igre, postavljaju se 
    #odgovarajuće vrednosti za promenljive kako bi se završila igra.
    if exit_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        global run
        run = False



#FUNKCIJA ZA ISCRTAVANJE EKRANA SA PORUKOM "PAUSE" 
#I OPCIJAMA ZA NASTAVAK IGRE ILI POVRATAK NA GLAVNI 
#MENI KADA IGRAČ PRITISNE TASTER ZA PAUZU.
def draw_pause():
    #Unutar funkcije se koriste globalne promenljive 
    #kako bi se omogućilo ažuriranje njihovih vrednosti tokom izvršavanja funkcije.
    global level, pause, menu, points, total_shots, time_passed, time_remaining, clicked, new_coords
    #Koristeći funkciju screen.blit(), iscrtava se slika ekrana 
    #sa porukom "Pause" (pause_img) na poziciji (0, 0) na ekranu.
    screen.blit(pause_img, (0, 0))
    #Nakon toga se dobija trenutna pozicija miša mouse_pos 
    #i stanje pritisaka na dugme miša clicks pomoću 
    #funkcija pygame.mouse.get_pos() i pygame.mouse.get_pressed().
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()
    #Definišu se pravougaonici za dugmiće na ekranu za nastavak 
    #igre (resume_button) i povratak na glavni meni (menu_button) pomoću funkcije pygame.rect.Rect().
    resume_button = pygame.rect.Rect((170, 661), (260, 100))
    menu_button = pygame.rect.Rect((475, 661), (260, 100))
    #Zatim se vrši provera da li je miš unutar pravougaonika određenih dugmića 
    #i da li je korisnik kliknuo levim tasterom miša. Ako je to slučaj i 
    #ako klik još nije registrovan (da bi se izbegla višestruka obrada klika), 
    #vrši se odgovarajuće ažuriranje promenljivih level, pause, clicked i menu.

    #1)Ako je pritisnuto dugme za nastavak igre, 
    #postavlja se prethodni nivo (resume_level) kako bi se 
    #igra nastavila, a pauza se isključuje.
    if resume_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        level = resume_level
        pause = False
        clicked = True
    #2)Ako je pritisnuto dugme za povratak na glavni meni, 
    #postavljaju se odgovarajuće vrednosti za promenljive 
    #kako bi se vratio na glavni meni i resetovali rezultati.
    if menu_button.collidepoint(mouse_pos) and clicks[0] and not clicked:
        pygame.mixer.music.play()
        level = 0
        pause = False
        menu = True
        points = 0
        total_shots = 0
        time_passed = 0
        time_remaining = 0
        clicked = True
        new_coords = True



#7. GLAVNA PETLJA IGRE KOJA SE IZVRŠAVA SVE DOK JE PROMENLJIVA RUN POSTAVLJENA NA TRUE
run = True
while run:
    #Unutar petlje se vrši osvežavanje vremenskog intervala (ticks) 
    #pomoću funkcije timer.tick(fps), gde je timer objekat koji meri vreme,
    #a fps predstavlja željeni broj frejmova u sekundi.
    timer.tick(fps)
    #Nakon toga se proverava da li je vrednost promenljive level različita od 0.
    # Ako jeste, to znači da se trenutno igra neki nivo, pa se izvršava odgovarajući kod.
    if level != 0:
        #U nastavku se proverava vrednost promenljive counter. 
        #Ako je manja od 60, inkrementira se za 1. 
        #Ova promenljiva se koristi za praćenje vremena u 
        #okviru jedne sekunde (60 frejmova u sekundi). 
        #To znači da se svaki put kada se izvrši ova deonica koda,
        #vreme se uvećava za jedan frejm.
        if counter < 60:
            counter += 1
        else:
            #Ako je vrednost counter jednaka ili veća od 60, to znači da je prošla jedna sekunda, 
            #pa se vrednost counter resetuje na 1, a vreme koje je prošlo (time_passed) se uvećava za jednu sekundu.
            counter = 1
            time_passed += 1
            #ako je mod igre (mode) postavljena na 2 (timed mode), 
            #smanjuje se preostalo vreme (time_remaining) za jednu sekundu.
            if mode == 2:
                time_remaining -= 1
    #U sledećem delu se proverava da li je promenljiva new_coords postavljena na True. 
    #Ako jeste, to znači da su potrebne nove koordinate ciljeva, 
    #pa se one inicijalizuju na osnovu vrednosti u promenljivim targets i 
    #smeštaju u promenljive one_coords, two_coords i three_coords.
    if new_coords:
        # initialize enemy coordinates
        one_coords = [[], [], []]
        two_coords = [[], [], []]
        three_coords = [[], [], [], []]
        for i in range(3):
            my_list = targets[1]
            for j in range(my_list[i]):
                one_coords[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
        for i in range(3):
            my_list = targets[2]
            for j in range(my_list[i]):
                two_coords[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
        for i in range(4):
            my_list = targets[3]
            for j in range(my_list[i]):
                three_coords[i].append((WIDTH // (my_list[i]) * j, 300 - (i * 100) + 30 * (j % 2)))
        new_coords = False

    #Zatim se popunjava ekran crnom bojom pomoću funkcije screen.fill('black') i 
    #iscrtavaju se pozadine (bgs) i baneri (banners) za trenutni nivo pomoću funkcija screen.blit().
    screen.fill('black')
    screen.blit(bgs[level - 1], (0, 0))
    screen.blit(banners[level - 1], (0, HEIGHT - 200))
    #Ako smo na nekom od ekrana i ne igrmao jos
    if menu:
        level = 0
        draw_menu()
    if game_over:
        level = 0
        draw_game_over()
    if pause:
        level = 0
        draw_pause()
    #Nakon toga se proverava u kojem se nivou igra nalazi (level) i izvršava odgovarajući kod.

    #1)Ako je nivo 1, pozivaju se funkcije draw_level(one_coords), 
    #move_level(one_coords) i check_shot(target_boxes, one_coords).
    if level == 1:
        target_boxes = draw_level(one_coords)
        one_coords = move_level(one_coords)
        #pucanje
        if shot:
            one_coords = check_shot(target_boxes, one_coords)
            shot = False
    #2)Ako je nivo 2, pozivaju se funkcije draw_level(two_coords), 
    #move_level(two_coords) i check_shot(target_boxes, two_coords).
    elif level == 2:
        target_boxes = draw_level(two_coords)
        two_coords = move_level(two_coords)
        #pucanje
        if shot:
            two_coords = check_shot(target_boxes, two_coords)
            shot = False
    #3)Ako je nivo 3, pozivaju se funkcije draw_level(three_coords), 
    #move_level(three_coords) i check_shot(target_boxes, three_coords).
    elif level == 3:
        target_boxes = draw_level(three_coords)
        three_coords = move_level(three_coords)
        #pucanje
        if shot:
            three_coords = check_shot(target_boxes, three_coords)
            shot = False
    #Nakon toga se pozivaju funkcije draw_gun() i draw_score() 
    #koje iscrtavaju vatreno oružje i prikazuju rezultat na ekranu, 
    #samo ako se trenutno igra neki nivo (level > 0).
    if level > 0:
        draw_gun()
        draw_score()

    #Zatim se prolazi kroz sve događaje (event) koji su se desili od poslednjeg osvežavanja ekrana.
    for event in pygame.event.get():
        #Ako je događaj tipa pygame.QUIT, to znači da je korisnik zatvorio prozor igre, 
        #pa se postavlja vrednost run na False i petlja se prekida.
        if event.type == pygame.QUIT:
            run = False
        #Ako je događaj tipa pygame.MOUSEBUTTONDOWN i 
        #taster miša koji je pritisnut je levi taster 
        #(event.button == 1), vrši se provera pozicije klika miša.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            #1. Ako se klik nalazi unutar određenog područja na ekranu, 
            #postavlja se promenljiva shot na True, uvećava se broj ukupnih 
            #ispaljenih metaka (total_shots) i smanjuje se broj preostalih 
            #metaka (ammo) ako je moda igre postavljena na 1.
            if (0 < mouse_position[0] < WIDTH) and (0 < mouse_position[1] < HEIGHT - 200):
                shot = True
                total_shots += 1
                if mode == 1:
                    ammo -= 1
            #2. Ako se klik nalazi na dugmiću za nastavak igre (resume_button), 
            #postavljaju se vrednosti resume_level na trenutni nivo, 
            #pause na True i clicked na True.
            if (670 < mouse_position[0] < 860) and (660 < mouse_position[1] < 715):
                resume_level = level
                pause = True
                clicked = True
            #3. Ako se klik nalazi na dugmiću za povratak na glavni meni (menu_button),
            #postavljaju se vrednosti menu na True, pušta se muzika (pygame.mixer.music.play()),
            #clicked na True i new_coords na True.
            if (670 < mouse_position[0] < 860) and (715 < mouse_position[1] < 760):
                menu = True
                pygame.mixer.music.play()
                clicked = True
                new_coords = True
        #Ako je događaj tipa pygame.MOUSEBUTTONUP i taster miša koji je 
        #otpušten je levi taster (event.button == 1) i clicked je 
        #postavljena na True, postavlja se clicked na False.
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked:
            clicked = False


    #Nakon provere događaja, ako je vrednost level veća od 0, vrše se dodatne provere.
    if level > 0:
        #Ako su sve kutije ciljeva prazne (target_boxes == [[], [], []]) i nivo je manji od 3, 
        #inkrementira se vrednost level kako bi se prešao na sledeći nivo.
        if target_boxes == [[], [], []] and level < 3:
            level += 1
        #Ako je nivo 3 i sve kutije ciljeva su prazne (target_boxes == [[], [], [], []]) ili 
        # ako je moda igre postavljena na 1 i broj preostalih metaka (ammo) je 0 ili 
        # ako je moda igre postavljena na 2 i preostalo vreme (time_remaining) je 0, 
        # postavlja se new_coords na True, pušta se muzika, a zatim se vrši provera rezultata 
        # i postavljanje promenljive game_over na True.
        if (level == 3 and target_boxes == [[], [], [], []]) or (mode == 1 and ammo == 0) or (
                mode == 2 and time_remaining == 0):
            new_coords = True
            pygame.mixer.music.play()
            #u yavisnosti od mod-a proverava se najbolji score na odredjeni nacin
            #i ukoliko jeste ostvaren cuva se kako bi se pposle upisao u fajl
            if mode == 0:
                if time_passed < best_freeplay or best_freeplay == 0:
                    best_freeplay = time_passed
                    write_values = True
            if mode == 1:
                if points > best_ammo:
                    best_ammo = points
                    write_values = True
            if mode == 2:
                if points > best_timed:
                    best_timed = points
                    write_values = True
            game_over = True
    #Ako je potrebno upisati vrednosti rezultata u datoteku, 
    # otvara se datoteka 'projekat-main/high_scores.txt' u režimu pisanja ('w'), 
    # upisuje se vrednosti best_freeplay, best_ammo i best_timed, 
    # a zatim se datoteka zatvara i postavlja se write_values na False
    if write_values:
        file = open('projekat-main/high_scores.txt', 'w')
        file.write(f'{best_freeplay}\n{best_ammo}\n{best_timed}')
        file.close()
        write_values = False
    #funkcija pygame.display.flip() da bi se prikazao ažurirani sadržaj na ekranu.
    pygame.display.flip()
#Na kraju se koristi funkcija pygame.display.flip() da bi se prikazao ažurirani sadržaj na ekranu.
pygame.quit()

#Mi smo na kraju preko pip Python biblioteke napravili .exe(EXECUTABLE FILE) kako bi
#igrica mogla lakse da se pokrece i omoguci bolje korisnicko iskustvo!
#Prvo smo kreirali ikonicu za nasu igricu i konvertovali je u .ico format i podesili joj veoma male dimenzije
#i smestili je u assets icon folder-u!

#To smo odradili tako sto smo u terminalu koji se odnosi na file path do foldera gde se nalazi 
# nasa igrica kucali sledeci kod: pyinstaller -w -F -i "fajl path do ikonice" main.py
#Nakon pokretanja datog koda napravice dva foldera: 

#1. dist(Ovaj folder je rezultat izgradnje. 
#U njemu se nalazi završna verzija vaše izvršne datoteke, kao i sve druge neophodne datoteke 
#za pokretanje program) 

#2. build(Ovaj folder sadrži privremene datoteke koje se generišu tokom procesa izgradnje. 
# U njemu se nalaze razni međufajlovi, kao i fajlovi koji su prekopirani 
# iz vašeg projekta radi izvršavanja i povezivanja), 

#3. kao i jedan SPEC fajl "main.spec(Ovo je konfiguracioni fajl koji generiše PyInstaller. 
# On sadrži informacije o konfiguraciji projekta, kao što su putanje do ulazne tačke (u ovom slučaju main.py),
# eksterni moduli koji su korišćeni i druge opcije koje ste specificirali prilikom izvršavanja naredbe.)"

#Nas .exe se nalazi u dist folderu i samo kreiramo shortcut za desktop i to je to.






