import pygame
import random

from button import Button
pygame.init()
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
w, h = 1200, 630
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('My Game')

size = (90, 90)

fon = pygame.image.load('images/fon.jpg')
der = pygame.image.load('images/der.jpg')
res = pygame.image.load('images/button.png')
fons = pygame.transform.scale(fon, (1200, 630))
ders = pygame.transform.scale(der, size)


# per=pygame.mixer.Sound('sounds/per1.wav')
# pygame.mixer.music.load('sounds/game.mp3')
#
# pygame.mixer.music.play(-1)


f_end = pygame.font.SysFont('Segoe UI',32, True, True)
f_end1 = pygame.font.SysFont('Segoe UI',25, True, True)

res='Начать заново!'
strt = 'Начать игру!'




f_image = ['images/f1.png', 'images/f2.jpg', 'images/f3.png', 'images/f4.png', 'images/f5.jpg', 'images/f6.jpg',
           'images/f7.png', 'images/f8.jpg', 'images/f9.jpg']
f = []
for link in f_image:
    im = pygame.image.load((link))
    im = pygame.transform.scale(im, size)
    f.append(im)

TIME = pygame.USEREVENT + 1
pygame.time.set_timer(TIME, 1000)


z = [(300, 200), (402, 200), (504, 200), (606, 200), (708, 200), (810, 200), (300, 300), (402, 300), (504, 300), (606, 300), (708, 300), (810, 300), (300, 400), (402, 400), (504, 400), (606, 400), (708, 400), (810, 400)]
random.shuffle(z)




sek, schet = 0, 0
run = True
close = False
flag = 1
pl1, pl2 = 0, 0
q = 0
draw = [True] * 18
d = {}
for i in range(9):
    d[f[i]] = set()
    d[f[i]].add(z[i * 2])
    d[f[i]].add(z[i * 2 + 1])

# добавим название игры
start_lbl = f_end.render(f'Игра "Найди пару"', True, BLACK)
r_start = start_lbl.get_rect(center=(w // 2, 50))
screen.blit(start_lbl, r_start)

pygame.display.flip()
restart = Button((w//2, h//2+200), 190, 50, 'images/button.png', res)
start = Button((w//2, h//2+200), 250, 100, 'images/button.png', strt)

start_menu = True
help_flag = False
while run:
    while start_menu:
        screen.blit(fons, (0, 0))
        screen.blit(start_lbl, r_start)
        start.draw(screen)
        pygame.display.update()
        start.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == start:
                start_menu = False
                screen.blit(fons, (0, 0))
                screen.blit(start_lbl, r_start)
                for i in range(9):
                    screen.blit(f[i], z[2 * i])
                    screen.blit(f[i], z[2 * i + 1])
                pygame.display.flip()
                pygame.time.delay(3000)
            if event.type == pygame.QUIT:
                close = False
                run = False

    while close:
        screen.blit(fons, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(20)
        screen.blit(area, (0, 0))
        restart.draw(screen)
        ex = f_end.render(f'EXCELLEN!', True, BLACK)
        r1 = ex.get_rect(center=(w//2, h//2-100))
        vrs = f_end.render(f'You did it for {sek} seconds', True, BLACK)
        r2 = vrs.get_rect(center=(w//2, h//2))
        PL1 = f_end.render(f'Player1 win!', True, RED)
        r3 = ex.get_rect(center=(w // 2, h //2 + 100))
        PL2 = f_end.render(f'Player2 win!', True, RED)
        if pl1 > pl2:
            screen.blit(PL1, r3)
        if pl2 > pl1:
            screen.blit(PL2, r3)
        screen.blit(ex, r1)
        screen.blit(vrs, r2)
        pygame.display.update()
        restart.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == restart:
                random.shuffle(z)
                sek, schet = 0, 0
                run = True
                close = False
                flag = 1
                pl1, pl2 = 0, 0
                q = 0
                draw = [True] * 18
                d = {}
                for i in range(9):
                    d[f[i]] = set()
                    d[f[i]].add(z[i*2])
                    d[f[i]].add(z[i*2 + 1])

                screen.blit(fons, (0, 0))
                for i in range(9):
                    screen.blit(f[i], z[2 * i])
                    screen.blit(f[i], z[2 * i + 1])
                pygame.display.flip()
                pygame.time.delay(3000)
            if event.type == pygame.QUIT:
                close = False
                run = False

    screen.blit(fons, (0, 0))
    screen.blit(start_lbl, r_start)


    for pos in range(300, 811, 102):
        pygame.draw.rect(screen, BLACK, (pos, 200, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 300, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 400, 90, 90), 1)

    for i in range(9):
        screen.blit(f[i], z[2 * i])
        screen.blit(f[i], z[2 * i + 1])
    s = -1
    rct = []
    for x in draw:
        s += 1
        if x and x != 5:
            screen.blit(ders, z[s])
        r = ders.get_rect(topleft=z[s])
        rct.append(r.topleft)


    p = pygame.mouse.get_pressed()
    if p[0]:
        pos = pygame.mouse.get_pos()
        for i in range(len(rct)):
            rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
            if rt.collidepoint(pos) and draw[i] != 5:
                # per.play(1)
                draw[i] = False

    if draw.count(False) == 2:
        help_flag = True
        z_true = set()
        k = []
        for i in range(len(draw)):
            if not draw[i]:
                k.append(i)
                z_true.add(rct[i])
        if q % 2 == 0:
            for foto, z_set in d.items():
                if z_set == z_true:
                    schet += 1
                    draw[k[0]] = 5
                    draw[k[1]] = 5
                    flag = 0
                    pl1 += 1
                    break
        if q % 2 != 0:
            for foto, z_set in d.items():
                if z_set == z_true:
                    schet += 1
                    draw[k[0]] = 5
                    draw[k[1]] = 5
                    flag = 0
                    pl2 += 1
                    break

    if draw.count(False) == 3:
        if flag:
            q += 1
            draw[k[0]] = True
            draw[k[1]] = True
        flag = 1




    vr = f_end1.render(f'Время: {sek}',True, BLACK)
    sch = f_end1.render(f'Общий счёт:{schet}/9', True, BLACK)
    r2 = sch.get_rect(topright=(w-10, 0))
    pl11 = f_end.render(f'Игрок 1: {pl1}', True, BLACK)
    r3 = pl11.get_rect(topleft=(10, 30))
    pl22 = f_end.render(f'Игрок 2: {pl2}', True, BLACK)
    r4 = pl22.get_rect(topleft=(10, 70))

    screen.blit(vr, (10, 0))
    screen.blit(sch, r2)
    screen.blit(pl11, r3)
    screen.blit(pl22, r4)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == TIME:
            sek += 1
        if event.type == pygame.QUIT:
            run = False
    if schet == 9:
        close = True

pygame.quit()
