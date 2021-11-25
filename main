import pygame
from settings import *
from player import Player
from wall import Wall
from dot import Dot
from star import Star
from finish import Finish
import random
import time

# INITIATES PYGAME
pygame.init()
# SCREEN CREATION
size = (WINDOW_W, WINDOW_H)
screen = pygame.display.set_mode(size)

# SPRITE GROUPS
players = pygame.sprite.Group()
walls = pygame.sprite.Group()
dots = pygame.sprite.Group()
stars = pygame.sprite.Group()
finishs = pygame.sprite.Group()

# CLOCK
clock = pygame.time.Clock()


def game():
    for col in range(20):
        for row in range(34):
            if LAYOUT[row][col] == 1:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
            if LAYOUT[row][col] == 2:
                player = Player()
                player.rect.x = col * grid_size
                player.rect.y = row * grid_size
                players.add(player)
            if LAYOUT[row][col] == 3:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.verticalFaceLeft()
            if LAYOUT[row][col] == 4:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.verticalFaceRight()
            if LAYOUT[row][col] == 5:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.topLeftEdge()
            if LAYOUT[row][col] == 6:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.topRightEdge()
            if LAYOUT[row][col] == 7:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.bottomLeftEdge()
            if LAYOUT[row][col] == 8:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.bottomRightEdge()
            if LAYOUT[row][col] == 9:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.verticalFlip()
            if LAYOUT[row][col] == "b":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.endPieceRIGHT()
            if LAYOUT[row][col] == "a":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.platformPieceHorizontal()
            if LAYOUT[row][col] == "c":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.endPieceLEFT()
            if LAYOUT[row][col] == "d":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.endPieceUP()
            if LAYOUT[row][col] == "e":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.endPieceDOWN()
            if LAYOUT[row][col] == "f":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.platformPieceVertical()
            if LAYOUT[row][col] == "g":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.topRightCorner()
            if LAYOUT[row][col] == "h":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.topLeftCorner()
            if LAYOUT[row][col] == "i":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.bottomLeftCorner()
            if LAYOUT[row][col] == "j":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
                wall.bottomRightCorner()
            if LAYOUT[row][col] == "k":
                dot = Dot()
                dot.rect.x = col * grid_size + 15
                dot.rect.y = row * grid_size + 15
                dots.add(dot)
            if LAYOUT[row][col] == "l":
                star = Star()
                star.rect.x = col * grid_size + 8
                star.rect.y = row * grid_size + 8
                stars.add(star)
            if LAYOUT[row][col] == "m":
                finish = Finish()
                finish.rect.x = col * grid_size
                finish.rect.y = row * grid_size
                finishs.add(finish)
    # ~COLOURS~#

    stars_collected = 0
    dots_collected = 0

    BLACK = (0, 0, 0)

    directionCheck = 4

    MOVING = False
    LEFT = False
    RIGHT = False
    UP = False
    DOWN = False

    show_particles = False

    zooming = False
    boost = False

    particles = []
    zoom = []

    # ~~~~~~GAME LOOP~~~~~~#
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if MOVING == False:
                    if event.key == pygame.K_LEFT:
                        LEFT = True
                        MOVING = True
                    elif event.key == pygame.K_RIGHT:
                        RIGHT = True
                        MOVING = True
                    elif event.key == pygame.K_UP:
                        UP = True
                        MOVING = True
                    elif event.key == pygame.K_DOWN:
                        DOWN = True
                        MOVING = True
        # ~~~~~~GAME LOGIC~~~~~~#

        for x in range(len(dots)):
            dots.sprites()[x].update()
        for x in range(len(stars)):
            stars.sprites()[x].update()
        for x in range(len(finishs)):
            finishs.sprites()[x].update()

        if MOVING == False:
            player.reset()
            if directionCheck == 0:
                player.idle()
                player.flipRight()
            elif directionCheck == 1:
                player.idle()
                player.flipLeft()
            elif directionCheck == 3:
                player.idle()
                player.flip180()
            elif directionCheck == 4:
                player.idle()

        if player.rect.y > 550:
            player.rect.y -= 15
            for x in range(len(walls)):
                walls.sprites()[x].rect.y -= 15
            for x in range(len(dots)):
                dots.sprites()[x].rect.y -= 15
            for x in range(len(stars)):
                stars.sprites()[x].rect.y -= 15
            for x in range(len(finishs)):
                finishs.sprites()[x].rect.y -= 15

        if player.rect.y < 150:
            player.rect.y += 15
            for x in range(len(walls)):
                walls.sprites()[x].rect.y += 15
            for x in range(len(dots)):
                dots.sprites()[x].rect.y += 15
            for x in range(len(stars)):
                stars.sprites()[x].rect.y += 15
            for x in range(len(finishs)):
                finishs.sprites()[x].rect.y += 15

        if player.rect.x > 700:
            player.rect.x -= 15
            for x in range(len(walls)):
                walls.sprites()[x].rect.x -= 15
            for x in range(len(dots)):
                dots.sprites()[x].rect.x -= 15
            for x in range(len(stars)):
                stars.sprites()[x].rect.x -= 15
            for x in range(len(finishs)):
                finishs.sprites()[x].rect.x -= 15

        if player.rect.x < 100:
            player.rect.x += 15
            for x in range(len(walls)):
                walls.sprites()[x].rect.x += 15
            for x in range(len(dots)):
                dots.sprites()[x].rect.x += 15
            for x in range(len(stars)):
                stars.sprites()[x].rect.x += 15
            for x in range(len(finishs)):
                finishs.sprites()[x].rect.x += 15

        player_Collide = pygame.sprite.groupcollide(players, walls, False, False)

        if LEFT == True:
            zooming = True
            use = 1
            part_x = player.rect.x
            part_y = player.rect.y + 15
            directionCheck = 1
            RIGHT = False
            UP = False
            DOWN = False
            if player.rect.x > 300:
                player.moveLeft()
            else:
                for x in range(len(walls)):
                    walls.sprites()[x].moveRight()
                for x in range(len(dots)):
                    dots.sprites()[x].moveRight()
                for x in range(len(stars)):
                    stars.sprites()[x].moveRight()
                for x in range(len(finishs)):
                    finishs.sprites()[x].moveRight()
                boost = True

        if RIGHT == True:
            zooming = True
            use = 2
            part_x = player.rect.x + 30
            part_y = player.rect.y + 15
            directionCheck = 0
            LEFT = False
            UP = False
            DOWN = False
            if player.rect.x < 500:
                player.moveRight()
            else:
                for x in range(len(walls)):
                    walls.sprites()[x].moveLeft()
                for x in range(len(dots)):
                    dots.sprites()[x].moveLeft()
                for x in range(len(stars)):
                    stars.sprites()[x].moveLeft()
                for x in range(len(finishs)):
                    finishs.sprites()[x].moveLeft()
                boost = True

        if UP == True:
            zooming = True
            use = 3
            part_x = player.rect.x + 15
            part_y = player.rect.y
            directionCheck = 3
            LEFT = False
            DOWN = False
            RIGHT = False
            if player.rect.y > 300:
                player.moveUp()
            else:
                for x in range(len(walls)):
                    walls.sprites()[x].moveDown()
                for x in range(len(dots)):
                    dots.sprites()[x].moveDown()
                for x in range(len(stars)):
                    stars.sprites()[x].moveDown()
                for x in range(len(finishs)):
                    finishs.sprites()[x].moveDown()
                boost = True

        if DOWN == True:
            zooming = True
            use = 4
            part_x = player.rect.x + 15
            part_y = player.rect.y + 30
            directionCheck = 4
            LEFT = False
            RIGHT = False
            UP = False
            if player.rect.y < 450:
                player.moveDown()
            else:
                for x in range(len(walls)):
                    walls.sprites()[x].moveUp()
                for x in range(len(dots)):
                    dots.sprites()[x].moveUp()
                for x in range(len(stars)):
                    stars.sprites()[x].moveUp()
                for x in range(len(finishs)):
                    finishs.sprites()[x].moveUp()
                boost = True

        dot_Collide = pygame.sprite.groupcollide(players, dots, False, True)
        if dot_Collide:
            dots_collected += 1
        star_Collide = pygame.sprite.groupcollide(players, stars, False, True)
        if star_Collide:
            stars_collected += 1

        finish_Collide = pygame.sprite.groupcollide(players, finishs, False, False)
        if finish_Collide:
            print("you finished with", stars_collected, "stars collected and", dots_collected, "dots collected")
            run = False

        if player_Collide:

            start = time.perf_counter()

            show_particles = True
            MOVING = False
            zooming = False
            zoom.clear()
            boost = False

            # ~~LEFT OR RIGHT~~#

            for x in range(len(players)):
                for y in range(len(walls)):
                    if walls.sprites()[y].rect.x + 40 >= players.sprites()[x].rect.x and walls.sprites()[
                        y].rect.x - 30 <= players.sprites()[x].rect.x and walls.sprites()[y].rect.y + 10 >= \
                            players.sprites()[x].rect.y and walls.sprites()[y].rect.y - 10 <= players.sprites()[
                        x].rect.y:
                        if players.sprites()[x].rect.x > walls.sprites()[y].rect.x:
                            players.sprites()[x].rect.x = walls.sprites()[y].rect.x + 40
                        elif players.sprites()[x].rect.x < walls.sprites()[y].rect.x:
                            players.sprites()[x].rect.x = walls.sprites()[y].rect.x - 30

            # ~~ABOVE OR BELOW~~#

            for x in range(len(players)):
                for y in range(len(walls)):
                    if walls.sprites()[y].rect.y + 40 >= players.sprites()[x].rect.y and walls.sprites()[
                        y].rect.y - 30 <= players.sprites()[x].rect.y and walls.sprites()[y].rect.x + 10 >= \
                            players.sprites()[x].rect.x and walls.sprites()[y].rect.x - 10 <= players.sprites()[
                        x].rect.x:
                        if players.sprites()[x].rect.y > walls.sprites()[y].rect.y:
                            players.sprites()[x].rect.y = walls.sprites()[y].rect.y + 40
                        elif players.sprites()[x].rect.y < walls.sprites()[y].rect.y:
                            players.sprites()[x].rect.y = walls.sprites()[y].rect.y - 30

            LEFT = False
            RIGHT = False
            UP = False
            DOWN = False

        if show_particles:
            end = time.perf_counter()
            currentTime = end - start
            if currentTime > 0.2:
                start = time.perf_counter()
                show_particles = False
                particles.clear()

            #  show_particles = False

        # ~~DRAWING CODE~~#

        screen.fill(BLACK)

        colours = [(141, 4, 176), (255, 255, 0), (255, 255, 255)]

        players.draw(screen)
        walls.draw(screen)
        dots.draw(screen)
        stars.draw(screen)
        finishs.draw(screen)

        side_bar = pygame.image.load("side bar.png")
        side_bar = pygame.transform.scale(side_bar, (200, 800))
        screen.blit(side_bar, (600, 0))
        side_bar2 = pygame.image.load("side bar.png")
        side_bar2 = pygame.transform.scale(side_bar2, (200, 800))
        side_bar2 = pygame.transform.flip(side_bar2, True, True)
        screen.blit(side_bar2, (0, 0))

        pause_button = pygame.image.load("pause.png")
        pause_button = pygame.transform.scale(pause_button, (80, 80))
        screen.blit(pause_button, (690, 690))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render("Dots:", 1, (255, 255, 255))
        screen.blit(title, (680, 100))

        font = pygame.font.Font('8-BitMadness.ttf', 40)
        title = font.render(str(dots_collected), 1, (255, 255, 255))
        screen.blit(title, (700, 150))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render("Stars:", 1, (255, 255, 255))
        screen.blit(title, (40, 100))

        font = pygame.font.Font('8-BitMadness.ttf', 40)
        title = font.render(str(stars_collected), 1, (255, 255, 255))
        screen.blit(title, (60, 150))

        if show_particles:

            if use == 1:
                particles.append([[part_x, part_y], [-1, random.randint(0, 15) / 10 - 1], random.randint(2, 4)])
            elif use == 2:
                particles.append([[part_x, part_y], [1, random.randint(0, 15) / 10 - 1], random.randint(2, 4)])
            elif use == 3:
                particles.append([[part_x, part_y], [random.randint(0, 15) / 10 - 1, -1], random.randint(2, 4)])
            elif use == 4:
                particles.append([[part_x, part_y], [random.randint(0, 15) / 10 - 1, 1], random.randint(2, 4)])

            for particle in particles:
                particle[0][0] += particle[1][0]
                particle[0][1] += particle[1][1]
                particle[2] -= 0.01
                particle[1][1] -= 0.05
                a = str(particle[0])
                pygame.draw.circle(screen, random.choice(colours), (int(particle[0][0]), int(particle[0][1])),
                                   int(particle[2]))
                if particle[2] <= 0:
                    particles.remove(particle)

        if zooming:
            if use == 1:
                zoom.append([[part_x, part_y], [5, random.randint(0, 15) / 10 - 1], random.randint(4, 6)])
            elif use == 2:
                zoom.append([[part_x, part_y], [-5, random.randint(0, 15) / 10 - 1], random.randint(4, 6)])
            elif use == 3:
                zoom.append([[part_x, part_y], [random.randint(0, 15) / 10 - 1, 5], random.randint(4, 6)])
            elif use == 4:
                zoom.append([[part_x, part_y], [random.randint(0, 15) / 10 - 1, -5], random.randint(4, 6)])

            for part in zoom:
                part[0][0] += part[1][0]
                part[0][1] += part[1][1]
                if boost:
                    part[2] -= 0.2
                else:
                    part[2] -= 0.5
                part[1][1] += 0.01
                a = str(part[0])
                pygame.draw.circle(screen, (255, 255, 0), (int(part[0][0]), int(part[0][1])), int(part[2]))
                if part[2] <= 0:
                    zoom.remove(part)

        # SET FPS
        clock.tick(120)
        pygame.display.update()
    pygame.quit()


game()
