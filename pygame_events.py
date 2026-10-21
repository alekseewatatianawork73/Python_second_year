import pygame as pg  # подключаем библиотеку
pg.init()  # подготавливаем все функции и методы к работе

class Character:  # класс для персонажей
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 50
        self.step = 5

    # метод для обновления положения персонажа
    def update(self):
        p = pg.key.get_pressed()  # список событий на клавиатуре
        # проверяем нажатие стрелок на клавиатуре и передвигаем игрока
        if p[pg.K_LEFT]:
            self.x -= self.step
            self.x = max(0, self.x)  # не выходим за левую границу (x = 0)
        elif p[pg.K_RIGHT]:
            self.x += self.step
            self.x = min(W - self.size, self.x)  # не выходим за правую границу (x = W)
        elif p[pg.K_UP]:
            self.y -= self.step
            self.y = max(0, self.y)  # не выходим за верхнюю границу (y = 0)
        elif p[pg.K_DOWN]:
            self.y += self.step
            self.y = min(H - self.size, self.y)  # не выходим за нижнюю границу (y = H)

    # Переопределяем поведение оператора +=
    def __iadd__(self, value):
        # увеличиваем размер игрока на value
        self.size += value
        self.size = min(H - self.y, W - self.x, self.size)   # проверяем, что игрок помещается в окне
        return self

    # Переопределяем поведение оператора -=
    def __isub__(self, value):
            # уменьшаем размер игрока на value
            self.size -= value
            self.size = max(5, self.size)  # проверяем, что игрок не меньше 5 пикселей
            return self



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
clock = pg.time.Clock()  # создаём таймер для установки частоты смены кадров (кадры в секунду)

# основной цикл игры (окно бесконечно отображается и сменяет кадры)
while running:
    # цикл событий, происходящих в игре (event)
    for event in pg.event.get():
        # проверяем, что произошло событие QUIT - нажатие на крестик в углу окна
        if event.type == pg.QUIT:
            running = False  # завершаем цикл => игра завершена, окно закрывается

        # проверяем использование клавиатуры (KEYDOWN)
        if event.type == pg.KEYDOWN:
            # если пробел - увеличиваем размер игрока на 5 пикселей
            if event.key == pg.K_SPACE:
                player += 5
            # если backspace (удалить) - уменьшаем размер игрока на 5 пикселей
            elif event.key == pg.K_BACKSPACE:
                player -= 5

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
