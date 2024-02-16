import pygame
import math

# Пользователь вводит данные
user_input_weight = float(input("Введите массу шара >>> "))
user_input_radius = float(input("Введите радиус шара >>> "))

# Цвета
RED = (255, 8, 8)
WHITE = (255, 255, 255)

# Ширина и высота экрана
display_width = 400
display_height = 400

x_position = display_width // 2 - 15
y_position = display_height // 2 - 15

# Инициализируем игру
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()


# Функция для расчета гравитации
def gravity(height, weight):
    g = 9.81
    coefficient = weight / 10
    time = math.sqrt(2 * height / g)
    speed = g * time * coefficient
    return time, speed


# Падение шарика
def fall(speed):
    global y_position
    y_position += speed

    if y_position + user_input_radius >= display_height:
        y_position = display_height - user_input_radius
        speed = 0

# цикл для завершения
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, RED, (x_position, int(y_position)), user_input_radius)
    pygame.display.update()

    time, speed = gravity(y_position - user_input_radius, user_input_weight)
    fall(speed * dt)

    pygame.draw.circle(screen, RED, (x_position, int(y_position)), user_input_radius)

    pygame.display.update()