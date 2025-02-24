import math
import pygame
from pygame import sprite
from settings import *
from bot import draw_monster


def ray_casting(screen, pos, angle):
    cur_angle = math.radians(angle) - HALF_FOV + DELTA_ANGLE / 2
    x1, y1 = pos
    dist = 0
    is_draw_bot = False
    draw_bot_dist = 0
    draw_bot_i = 0

    for i in range(NUM_RAYS):
        wall = 0
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for j in range(MAX_DEPTH):
            x = x1 + j * cos_a
            y = y1 + j * sin_a
            dist = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            pygame.draw.line(screen, 'grey', player_coord, (x, y))
            if (int(x), int(y)) == (int(bot_coord[0]), int(bot_coord[1])):
                is_draw_bot = True
                draw_bot_dist = dist
                draw_bot_i = i
            try:
                wall = map_world[int(x // minimap_size)][int(y // minimap_size)]
                if wall:
                    break
            except IndexError:
                continue

        height_rect = (WALLS_SIZE / (dist + 0.0000000000001)) * HEIGHT
        width_rect = WIDTH / NUM_RAYS
        if wall == 1:
            r = (255 - dist) / 2
            g = (255 - dist) / 2
            b = (255 - dist) / 2

        else:
            r = (153 - dist) / 1.5
            g = (102 - dist) / 1.5
            b = (204 - dist) / 1.5

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0

        pygame.draw.rect(screen, (r, g, b),
                         (i * width_rect, (HEIGHT - height_rect) / 2, width_rect + 1, height_rect))
        if is_draw_bot:
            height_rect_bot = (WALLS_SIZE / (draw_bot_dist + 0.0000000000001)) * HEIGHT
            monster_scale = height_rect_bot / 20
            width_rect_bot = WIDTH / NUM_RAYS

            draw_monster(screen, (draw_bot_i * width_rect_bot, HEIGHT / 2), monster_scale)
            # pygame.draw.rect(screen, "brown", (draw_bot_i * width_rect_bot, (HEIGHT - height_rect_bot) / 2,
            #                                    width_rect_bot + 1, height_rect_bot))

        cur_angle += DELTA_ANGLE
        angle %= 360
        cur_angle %= 6.28
