import pygame as pg  # подключаем библиотеку
pg.init()  # подготавливаем все функции и методы к работе

class Character:  # класс для персонажей
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 50
        self.direction = 'right'  # направление движения

    # метод для обновления положения персонажа
    def update(self):
        if self.direction == 'right':
            self.x += 5
            if self.x > W:
                self.direction = 'left'
        else:
            self.x -= 5
            if self.x < 0:
                self.direction = 'right'

    # метод для отрисовки персонажа (здесь просто квадрат)
    def draw(self, screen):
        pg.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.size, self.size)
        )


W, H = 1000, 700  # размеры окна
screen = pg.display.set_mode((W, H))  # создаём окно
pg.display.set_caption('My game')  # меняем заголовок окна

# создаём игрока - объект класса Character (в координатах (0, 300), красный)
player = Character(0, 300, (255, 0, 0))

running = True  # переменная для состояния игры: True - работает, False - завершена
clock = pg.time.Clock()  # создаём "часы" для установки частоты смены кадров (кадры в секунду)

# основной цикл игры (окно бесконечно отображается и сменяет кадры)
while running:
    # цикл событий, происходящих в игре (event)
    for event in pg.event.get():
        # проверяем, что произошло событие QUIT - нажатие на крестик в углу окна
        if event.type == pg.QUIT:
            running = False  # завершаем цикл => игра завершена, окно закрывается

    # закрашиваем окно голубым цветом
    screen.fill((0, 255, 255))
    # обновляем положение игрока (метод класса Character)
    player.update()
    # отрисовываем игрока после обновления его положения
    player.draw(screen)

    # после всех проверок и изменений обновляем экран
    pg.display.flip()

    clock.tick(60)  # задаём частоту смены кадров (в секунду)

# закрываем окно после завершения цикла
pg.quit()

