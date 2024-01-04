import pygame
import random
from math import sin, cos

screenWidth = 800
screenHeight = 800


class Planet:
    def __init__(
        self, name, speed, image, radius, initialLocation, width, height, angle
    ):
        self.name = name
        self.speed = speed
        self.image = image
        self.radius = radius
        self.location = initialLocation
        self.width = width
        self.height = height
        self.angle = angle


class Rocket:
    def __init__(self, image):
        self.isReady = True
        self.speed = 0.5
        self.image = image
        self.location = [0, 0]


class Game:
    pygame.init()
    print()

    file = "veronica.ogg"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

    # Constants
    numAsteroids = 6
    numPlanets = 8
    numBonus = 2
    numObstacles = numAsteroids + numBonus + numPlanets

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    font = pygame.font.Font("freesansbold.ttf", 18)

    planetsImg = []
    planetsObj = []

    def getLoc(planet):
        return [planet.location[0], planet.location[1]]

    def makePlanet(planet, images, objects, screenWidth, screenHeight):
        objects.append(planet)
        img = pygame.image.load(planet.image)
        img = pygame.transform.scale(img, (planet.width, planet.height))
        images.append(img)
        planet.image = img
        planet.location = [
            screenWidth // 2 - planet.width // 2,
            screenHeight // 2 - planet.height // 2,
        ]
        planet.angle = random.randint(0, 360)

    def nextLocation(planet, center):
        global pi
        result = []
        x = (planet.radius * cos(planet.angle) + center[0] - (planet.width // 2)) // 1
        result.append(x)
        y = (planet.radius * sin(planet.angle) + center[1] - (planet.height // 2)) // 1
        result.append(y)
        return result

    def isCollision(planet, rocket):
        if planet.name == "earth":
            return False
        if (
            rocket.location[0] < (planet.location[0] + planet.width)
            and rocket.location[0] > planet.location[0]
        ):
            if (
                rocket.location[1] < (planet.location[1] + planet.height)
                and rocket.location[1] > planet.location[1]
            ):
                return True
        return False

    sun = Planet("sun", 0, "sun.png", 0, [], screenWidth // 35, screenHeight // 35, 0)
    makePlanet(sun, planetsImg, planetsObj, screenWidth, screenHeight)

    mercury = Planet(
        "mercury",
        0.0048,
        "mercury.png",
        20,
        [],
        screenWidth // 85,
        screenHeight // 85,
        0,
    )
    makePlanet(mercury, planetsImg, planetsObj, screenWidth, screenHeight)

    venus = Planet(
        "venus",
        0.0035,
        "venus.png",
        38,
        [],
        screenWidth // 65,
        screenHeight // 65,
        0,
    )
    makePlanet(venus, planetsImg, planetsObj, screenWidth, screenHeight)

    earth = Planet(
        "earth",
        0.00298,
        "earth.png",
        60,
        [],
        screenWidth // 65,
        screenHeight // 65,
        0,
    )
    makePlanet(earth, planetsImg, planetsObj, screenWidth, screenHeight)

    mars = Planet(
        "mars",
        0.00241,
        "mars.png",
        90,
        [],
        screenWidth // 72,
        screenHeight // 72,
        0,
    )
    makePlanet(mars, planetsImg, planetsObj, screenWidth, screenHeight)

    jupiter = Planet(
        "jupiter",
        0.00131,
        "jupiter.png",
        170,
        [],
        screenWidth // 35,
        screenHeight // 35,
        0,
    )
    makePlanet(jupiter, planetsImg, planetsObj, screenWidth, screenHeight)

    saturn = Planet(
        "saturn",
        0.00097,
        "saturn.png",
        200,
        [],
        screenWidth // 36,
        screenHeight // 36,
        0,
    )
    makePlanet(saturn, planetsImg, planetsObj, screenWidth, screenHeight)

    uranus = Planet(
        "uranus",
        0.00068,
        "uranus.png",
        245,
        [],
        screenWidth // 47,
        screenHeight // 47,
        0,
    )
    makePlanet(uranus, planetsImg, planetsObj, screenWidth, screenHeight)

    neptune = Planet(
        "neptune",
        0.00054,
        "neptune.png",
        290,
        [],
        screenWidth // 39,
        screenHeight // 46,
        0,
    )
    makePlanet(neptune, planetsImg, planetsObj, screenWidth, screenHeight)

    pluto = Planet(
        "pluto",
        0.000464,
        "pluto.png",
        340,
        [],
        screenWidth // 90,
        screenHeight // 90,
        0,
    )
    makePlanet(pluto, planetsImg, planetsObj, screenWidth, screenHeight)

    # Rockets
    rocketImg = pygame.image.load("rocket.png")
    rocketImg = pygame.transform.scale(rocketImg, (18, 18))

    rocketImgUp = pygame.transform.rotate(rocketImg, 0)
    rocketImgDown = pygame.transform.rotate(rocketImg, 180)
    rocketImgLeft = pygame.transform.rotate(rocketImg, 90)
    rocketImgRight = pygame.transform.rotate(rocketImg, 270)

    rUp = Rocket(rocketImgUp)
    rDown = Rocket(rocketImgDown)
    rLeft = Rocket(rocketImgLeft)
    rRight = Rocket(rocketImgRight)

    rockets = [rUp, rDown, rLeft, rRight]

    score = 0

    # space_pressed = False
    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False

    running = True
    while running:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]
            ):  # checks for x-out
                running = False
        screen.fill((0, 0, 20))  # fill background

        # update image locations
        for planet in planetsObj:
            planet.angle += planet.speed
            newLoc = nextLocation(planet, [screenWidth // 2, screenHeight // 2])
            planet.location[0] = newLoc[0]
            planet.location[1] = newLoc[1]

        if pygame.key.get_pressed()[pygame.K_UP]:
            up_pressed = pygame.key.get_pressed()[pygame.K_UP]
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            down_pressed = pygame.key.get_pressed()[pygame.K_DOWN]
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            left_pressed = pygame.key.get_pressed()[pygame.K_LEFT]
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            right_pressed = pygame.key.get_pressed()[pygame.K_RIGHT]

        # UP (or SPACE)
        if (up_pressed) and rUp.isReady:
            rUp.isReady = False
            rUp.location = getLoc(earth)
        if up_pressed and not rUp.isReady:
            rUp.location[1] -= rUp.speed
            screen.blit(rocketImgUp, (rUp.location[0], rUp.location[1]))
        if rUp.location[1] < 10:
            rUp.isReady = True
            up_pressed = False

        # DOWN
        if down_pressed and rDown.isReady:
            rDown.isReady = False
            rDown.location = getLoc(earth)
        if down_pressed and not rDown.isReady:
            rDown.location[1] += rDown.speed
            screen.blit(rocketImgDown, (rDown.location[0], rDown.location[1]))
        if rDown.location[1] > screenHeight - 10:
            rDown.isReady = True
            down_pressed = False

        # LEFT
        if left_pressed and rLeft.isReady:
            rLeft.isReady = False
            rLeft.location = getLoc(earth)
        if left_pressed and not rLeft.isReady:
            rLeft.location[0] -= rLeft.speed
            screen.blit(rocketImgLeft, (rLeft.location[0], rLeft.location[1]))
        if rLeft.location[0] < 10:
            rLeft.isReady = True
            left_pressed = False

        # RIGHT
        if right_pressed and rRight.isReady:
            rRight.isReady = False
            rRight.location = getLoc(earth)
        if right_pressed and not rRight.isReady:
            rRight.location[0] += rRight.speed
            screen.blit(rocketImgRight, (rRight.location[0], rRight.location[1]))
        if rRight.location[0] > screenWidth - 10:
            rRight.isReady = True
            right_pressed = False

        for planet in planetsObj:
            for rocket in rockets:
                if isCollision(planet, rocket):
                    planetsObj.remove(planet)
                    planetsImg.remove(planet.image)
                    rocket.isReady = True
                    up_pressed = False
                    down_pressed = False
                    left_pressed = False
                    right_pressed = False
                    if planet == sun:
                        print("You hit the sun! You lose.")
                        # gameOver = "SCORE: " + str(score // 1)
                        # gameOvertext = font.render(gameOver, True, (0, 255, 0))
                        # gameOvertext_rect = gameOvertext.get_rect()
                        # gameOvertext_rect.center = (400, 340)
                        # screen.blit(gameOvertext, gameOvertext_rect)
                        # for i in planetsObj:
                        #     planetsObj.remove(i)
                        running = False
                    score += planet.radius + (10 / (planet.width * planet.height))

        # display updated images
        if len(planetsObj) > 0:
            for i in range(len(planetsImg)):
                screen.blit(
                    planetsImg[i],
                    (planetsObj[i].location[0], planetsObj[i].location[1]),
                )

        scoreStr = "SCORE: " + str(score // 1)
        text = font.render(scoreStr, True, (0, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        screen.blit(text, text_rect)

        controls = "Up, Down, Left, Right to Shoot"
        text = font.render(controls, True, (100, 155, 50))
        text_rect = text.get_rect()
        text_rect.center = (400, 750)
        screen.blit(text, text_rect)

        quit = "q to quit"
        text = font.render(quit, True, (250, 20, 20))
        text_rect = text.get_rect()
        text_rect.center = (400, 775)
        screen.blit(text, text_rect)

        if len(planetsObj) == 2:
            print("CONGRATULATIONS!")
            running = False

        score -= 0.01

        pygame.display.flip()
    print("Score: " + str(((score * 1000) // 1) / 1000))
