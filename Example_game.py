import pygame
import random
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

fon = pygame.image.load('images/fon.png')
der = pygame.image.load('images/der.png')
fons = pygame.transform.scale(fon, (1200, 630))
ders = pygame.transform.scale(der, size)


# per=pygame.mixer.Sound('sounds/per1.wav')
# pygame.mixer.music.load('sounds/game.mp3')
#
# pygame.mixer.music.play(-1)


f_end = pygame.font.SysFont('Arial',35, True, True)




f_image = ['images/f1.png', 'images/f2.png', 'images/f3.png', 'images/f4.png', 'images/f5.png',
           'images/f6.png','images/f7.png', 'images/f8.png', 'images/f9.png']

f = []
for link in f_image:
    im = pygame.image.load((link))
    im = pygame.transform.scale(im, size)
    f.append(im)


pygame.time.set_timer(pygame.USEREVENT, 1000)

z = [(300, 200), (402, 200), (504, 200), (606, 200), (708, 200), (810, 200), (300, 300), (402, 300), (504, 300),
     (606, 300), (708, 300), (810, 300), (300, 400), (402, 400), (504, 400), (606, 400), (708, 400), (810, 400)]
random.shuffle(z)


pygame.time.set_timer(pygame.USEREVENT, 2000)

sek = 0
schet = 0
c = 0
draw = [True] * 18
run = True
close = False

pl1=0
pl2=0
q=0
d = {}
for i in range(9):
    d[f[i]] = set()
    d[f[i]].add(z[2 * i])
    d[f[i]].add(z[2 * i + 1])

cur = 0
flag = 1
while run:

    while close:
        screen.blit(fons, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(120)
        screen.blit(area, (0, 0))
        ex = f_end.render(f'EXCELLEN!', True, BLACK)
        r1 = ex.get_rect(center=(w//2, h//2))
        vrs = f_end.render(f'You did it for {sek} seconds', True, BLACK)
        r2 = vrs.get_rect(center=(w//2, h//2+200))
        PL1 = f_end.render(f'Player1 win!', True, (255, 78, 0))
        r3 = ex.get_rect(center=(w // 2, h //2+ 100))
        PL2 = f_end.render(f'Player2 win!', True, (255, 78, 0))
        r4 = ex.get_rect(center=(w // 2, h //2 + 100))
        if pl1 > pl2:
            screen.blit(PL1, r3)
        if pl2 > pl1:
            screen.blit(PL2, r4)
        screen.blit(ex, r1)
        screen.blit(vrs, r2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
                run = False

    screen.blit(fons, (0, 0))




    for pos in range(300, 811, 102):
        pygame.draw.rect(screen, BLACK, (pos, 200, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 300, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 400, 90, 90), 1)

    for i in range(9):
        screen.blit(f[i], z[2 * i])
        screen.blit(f[i], z[2 * i + 1])

    pp = pygame.key.get_pressed()
    if pp[pygame.K_SPACE]:
        for x in draw:
            if x != 5:
                x = True

    p = pygame.mouse.get_pressed()
    if p[0]:
        pos = pygame.mouse.get_pos()
        for i in range(len(rct)):
            rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
            if rt.collidepoint(pos) and draw[i] != 5:
                draw[i] = False
                cur = i

    s = 0
    rct = []
    for x in draw:
        if x and x != 5:
            screen.blit(ders, z[s])
        r = ders.get_rect(topleft= z[s])
        rct.append(r.topleft)
        s += 1

    for event in pygame.event.get():
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for i in range(len(rct)):
                    rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
                    if rt.collidepoint(pos) and draw[i] != 5:
                        draw[i] = False
                        cur = i'''
        if event.type == pygame.USEREVENT:
            sek += 1
        if event.type == pygame.QUIT:
            run = False
    if schet == 9:
        close = True

    if draw.count(False) == 2:
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

    vr = f_end.render(f'Time:{sek}', True, BLACK)
    sch = f_end.render(f'Score:{schet}/9', True, BLACK)
    r2 = sch.get_rect(topright=(w, 0))
    pl11 = f_end.render(f'PL1={pl1}', True, BLACK)
    r3 = pl11.get_rect(topleft=(0, 35))
    pl22 = f_end.render(f'PL2={pl2}', True, BLACK)
    r4 = pl22.get_rect(topleft=(0, 70))

    screen.blit(vr, (0, 0))
    screen.blit(sch, r2)
    screen.blit(pl11, r3)
    screen.blit(pl22, r4)

    pygame.display.flip()


pygame.quit()
