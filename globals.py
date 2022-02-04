import math

# screen
sWidth = 1200
sHeight = 750

sWidthHalf = (sWidth /2)
sHeightHalf = (sHeight / 2)

FPS = 30
TILE = 75

#player
spawnPoint = (sWidthHalf, sHeightHalf)

player_pos = spawnPoint
player_ang = 0
player_speed = 3

#ray casting
FOV = math.pi / 3
FOVHalf = FOV /2
numOfRays = 64
maxDepthOfRays = 800
DeltaAngle = FOV / numOfRays
distance = numOfRays / (2 * math.tan(FOVHalf))
projectionCoeff = 3 * distance * TILE
scale = sWidth // numOfRays