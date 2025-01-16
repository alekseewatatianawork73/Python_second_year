# При нажатии левой кнопкой мыши на пчелу она исчезает с игрового экрана
import pygame
pygame.init()

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Game')

bg = pygame.image.load('images/bg.png')  # установка фона
bee = pygame.image.load('images/bee.png')  # картинка пчелы

draw = True  # переменная, отвечающая за отрисовку пчелы на экране

# начальное положение картинки-пчелы
x = w / 2
y = h / 2

run = True
while run:

    screen.blit(bg, (0, 0))

    # условие: рисуем пчелу, только если draw = True
    if draw:
        screen.blit(bee, (x, y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    p = pygame.mouse.get_pressed()  # получаем состояния кнопок мыши (нажаты или нет)

    # если нажата левая кнопка мыши
    if p[0]:
        rct = bee.get_rect(topleft=(x, y))  # получаем прямоугольник, в котором находится пчела
        pos = pygame.mouse.get_pos()  # получаем позицию курсора

        # если курсор при нажатии находится на картинке (в пределах прямоугольника rct),
        # то меняем значение draw на False => пчела не будет отображаться
        if rct.collidepoint(pos):
            draw = False

pygame.quit()
