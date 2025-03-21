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

fon = pygame.image.load('images/fon.jpg')
der = pygame.image.load('images/der.jpg')
fons = pygame.transform.scale(fon, (1200, 630))
ders = pygame.transform.scale(der, size)

# per=pygame.mixer.Sound('sounds/per1.wav')
# pygame.mixer.music.load('sounds/game.mp3')
#
# pygame.mixer.music.play(-1)

f_end = pygame.font.SysFont('Arial',35, True, True)

f_image = ['images/f1.png', 'images/f2.png', 'images/f3.png', 'images/f4.png', 'images/f5.png', 'images/f6.png',
           'images/f7.png', 'images/f8.png', 'images/f9.png']

f = []
for link in f_image:
    im = pygame.image.load((link))
    im = pygame.transform.scale(im, size)
    f.append(im)

pygame.time.set_timer(pygame.USEREVENT, 1000)

z = [(300, 200), (402, 200), (504, 200), (606, 200), (708, 200), (810, 200), (300, 300), (402, 300), (504, 300),
     (606, 300), (708, 300), (810, 300), (300, 400), (402, 400), (504, 400), (606, 400), (708, 400), (810, 400)]
random.shuffle(z)



sek = 0
schet = 0
c = 0
draw = [True] * 18
run = True
close = False

# не нужно при каждом обновлении экрана заполнять словарь, достаточно сделать это один раз вне игрового цикла,
# когда уже опрпеделено положение картинок
foto = 0
po = 0
d = {}
for i in range(9):
    d[f[foto]] = set()
    d[f[foto]].add(z[po])
    d[f[foto]].add(z[po + 1])
    foto += 1
    po += 2

while run:

    while close:
        ex = f_end.render(f'EXCELLEN!', True, BLACK)
        vrs = f_end.render(f'You did it for {sek} seconds', True, BLACK)
        screen.blit(ex, (w/2-150,h/2-20))
        screen.blit(vrs, (w / 2 - 200, h / 2 + 50))
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

    # возможно, этот цикл можно упростить (использовать список z с индексами?), нужно подумать
    s = -1
    a1, b1 = 300, 200
    rct = []
    for x in draw:
        s += 1
        if s == 6:
            a1, b1 = 300, 300
        elif s == 12:
            a1, b1 = 300, 400
        if x and x != 5:
            screen.blit(ders, (a1, b1))
        r = ders.get_rect(topleft=(a1, b1))
        rct.append(r.topleft)
        a1 += 102

    p = pygame.mouse.get_pressed()
    if p[0]:
        pos = pygame.mouse.get_pos()
        for i in range(len(rct)):
            rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
            if rt.collidepoint(pos) and draw[i] != 5:  # дополнительно проверяем, что эти картинки ещё не отгаданы
                draw[i] = False

    # обрабатываем нажатие на две картинки
    if draw.count(False) == 2:
        z_true = set()
        k = []
        for i in range(len(draw)):
            if not draw[i]:
                k.append(i)
                z_true.add(rct[i])
        flag = 1  # флажок для случая, когда картинки оказались разными
        for foto, z_set in d.items():
            if z_set == z_true:
                schet += 1
                # уже отгаданные картинки будем обозначать цифрой 5
                draw[k[0]] = 5
                draw[k[1]] = 5
                flag = 0  # меняем флажок на 0, так как были нажаты одинаковые картинки
                break  # прерываем цикл, если картинки уже найдены
        # если были нажаты разные картинки, то есть если флажок остался равным 1
        if flag:
            draw[k[0]] = True
            draw[k[1]] = True




    vr = f_end.render(f'Time:{sek}', True, BLACK)
    sch = f_end.render(f'Score:{schet}/9', True, BLACK)
    screen.blit(vr, (0, 0))
    screen.blit(sch, (w - 160, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            sek += 1
        if event.type == pygame.QUIT:
            run = False
    if schet == 9:
        close = True

pygame.quit()
