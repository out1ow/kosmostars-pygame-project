import pygame

FPS = 30
WIDTH = 17 * 64
HEIGHT = 11 * 64
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RES = 0  # RES - республика
SEP = 1  # SEP - сепаратисты

move_count = 0  # Подсчёт количества ходов(для статистики)

res_count = 0  # Подсчёт количества ходов в течении которых контрольная точка захвачена
sep_count = 0

res_score = 0  # Количество очков, заработанных за игру
sep_score = 0

side = RES  # Чей ход

game_state = 0
# Текущее состояние игры:
#   0 - игра не начата(стартовый экран)
#   1 - игра начата(игрвой процесс)
#   2 - победили республиканци
#   3 - победили сепаратисты

pygame.init()
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption('KOSMOSTARS')
pygame.display.set_icon(pygame.image.load('sources/icon/icon.png'))

font = pygame.font.Font('sources/font/m5x7.ttf', 60)
