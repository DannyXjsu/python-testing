import pygame

# App Properties
appName = "Test"
scrHeight = 1900
scrWidth = 1000

# Colors
clrBlack = (0, 0, 0)
clrRed = (255, 0, 0)
clrGreen = (0, 255, 0)
clrBlue = (0, 0, 255)
clrYellow = (255, 255, 0)
clrPurple = (255, 0, 255)
clrCyan = (0, 255, 255)
clrWhite = (255, 255, 255)

# World properties
wrlGravity = 0.2
wrlGravity2 = wrlGravity
global wrlInertia
wrlInertia = 0.01

# Controller properties
ctlPos = [340, 340]
ctlVel = [0, 0]
ctlAcc = [0, 0]
global ctlGround, ctlInertia
ctlGround = False
ctlInertia = 0.01

# Main function
def main():
    # Pygame start and properties
    pygame.init()
    screen = pygame.display.set_mode((scrHeight, scrWidth))
    pygame.display.set_caption(appName)
    clock = pygame.time.Clock()

    def controller(Ground, Inertia):
        # Link physics
        ctlVel[0] += ctlAcc[0]
        ctlVel[1] += ctlAcc[1]
        ctlPos[0] += ctlVel[0]
        ctlPos[1] += ctlVel[1]

        body = pygame.draw.circle(screen, clrPurple, (ctlPos[0], ctlPos[1]), 25)
        pygame.draw.circle(screen, clrPurple, (ctlPos[0] + scrWidth * 2 - 100, ctlPos[1]), 25)
        pygame.draw.circle(screen, clrPurple, (ctlPos[0] - scrWidth * 2 + 100, ctlPos[1]), 25)

        Inertia = wrlInertia
        Ground = False

        if ctlPos[1] >= scrHeight - 25 * 37:
            Ground = True
        if Ground:
            wrlGravity = 0
            ctlVel[1] = -0
            ctlPos[1] = scrHeight - 25 * 37
            Inertia *= 10
        else:
            wrlGravity = wrlGravity2
            Ground = wrlInertia

        if ctlPos[1] <= 27:
            ctlVel[1] = -0.1
            ctlPos[1] = 27

        if ctlPos[0] >= scrWidth * 2 - 100:
            ctlPos[0] = 0.1
        if ctlPos[0] <= 0:
            ctlPos[0] = scrWidth * 2 - 100

        if abs(ctlVel[0]) > 0.0001:
            ctlVel[0] -= (Inertia * ctlVel[0])
        elif abs(ctlVel[0]) < -0.0001:
            ctlVel[0] += (Inertia * ctlVel[0])
        if abs(ctlVel[1]) > 0.1:
            ctlVel[1] -= (Inertia * ctlVel[1])
        elif abs(ctlVel[1]) < -0.1:
            ctlVel[1] -= (Inertia * ctlVel[1])

        ctlVel[1] += wrlGravity

    # Main loop
    appLoop = True
    while appLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                appLoop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ctlAcc[0] -= +1
                if event.key == pygame.K_RIGHT:
                    ctlAcc[0] += 1
                if event.key == pygame.K_UP:
                    ctlAcc[1] -= +1
                if event.key == pygame.K_DOWN:
                    ctlAcc[1] += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ctlAcc[0] = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    ctlAcc[1] = 0

        screen.fill(clrBlack)

        controller(ctlGround, ctlInertia)

        # Pygame update
        delta = clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
