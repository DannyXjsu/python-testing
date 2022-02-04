import sys
import math
from multiprocessing import Pool
from map import world_map
from raycast import ray_casting

import pygame

from globals import *
from player import *

if __name__ == '__main__':

    pygame.init()

    pygame.font.init()
    fps = pygame.font.SysFont('DejaVu Sans', 30)

    pygame.display.set_caption("Testing")
    DISPLAY = pygame.display.set_mode((sWidth, sHeight))

    player = Player()

    clock = pygame.time.Clock()
    with Pool(processes=8) as pool:
        gameLoop = True
        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameLoop = False

            DISPLAY.fill((0, 0, 0))

            pygame.draw.rect(DISPLAY, (10, 50, 100), (0, 0, sWidth, sHeightHalf))
            pygame.draw.rect(DISPLAY, (50, 50, 50), (0, sHeightHalf, sWidth, sHeightHalf))

            player.movement()

            # for x,y in world_map:
            # pygame.draw.rect(DISPLAY, (150,150,150), (x, y, TILE, TILE), 2)

            # pygame.draw.circle(DISPLAY, (150, 0, 150), (int(player.x), int(player.y)), 10)
            # pygame.draw.line(DISPLAY, (150, 0, 150), player.pos, (player.x + sWidth * math.cos(player.angle), player.y + sWidth * math.sin(player.angle)), 2)

            ray_casting(DISPLAY, player.pos, player.angle)

            rFPS = int(clock.get_fps())

            textsurface = fps.render(str(rFPS), False, (0, 0, 0))
            DISPLAY.blit(textsurface, (0, 0))

            pygame.display.update()

            clock.tick(FPS)
