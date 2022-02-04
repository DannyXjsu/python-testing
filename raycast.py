import pygame
from globals import *
from map import world_map


def ray_casting(screenDisplay, player_position, player_angle):
    cur_angle = player_angle - FOVHalf
    xo, yo = player_position
    for ray in range(numOfRays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(maxDepthOfRays):
            x = xo + depth * cos_a
            y = yo + depth * sin_a

            # pygame.draw.line(screenDisplay, (200, 200, 200), player_position, (x, y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                projectionHeight = projectionCoeff / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(screenDisplay, color,
                                 (ray * scale, sHeightHalf - projectionHeight // 2, scale, projectionHeight))
                break
        cur_angle += DeltaAngle
