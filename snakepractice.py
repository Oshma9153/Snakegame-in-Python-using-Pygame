import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
wel_img = pygame.image.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\WEL5.jpg")
wel_img = pygame.transform.scale(wel_img, (screen_width, screen_height)).convert_alpha()
Gm_img = pygame.image.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\gameove (1).jpg")
Gm_img = pygame.transform.scale(Gm_img, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        gameWindow.blit(wel_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(50)


# Game loop
def gameloop():
    # Game specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, int(screen_width / 1.3))
    food_y = random.randint(20, int(screen_height / 1.3))
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 50
    snake_length = 1
    snake_list = []

    # check if highscore file exists
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(Gm_img, (0, 0))
            text_screen("Score : " + str(score), black, 360, 500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 10
                food_x = random.randint(20, int(screen_width / 1.3))
                food_y = random.randint(20, int(screen_height / 1.3))
                pygame.mixer.music.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\beep.mp3")
                pygame.mixer.music.play()
                snake_length += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(green)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score : " + str(score), blue, 5, 5)
            text_screen("HighScore : " + str(highscore), blue, 610, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\gameover.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\gameover.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


pygame.mixer.music.load("C:\\Users\\ACER\\Desktop\\snakegame\\snakegame\\Snakebg.mp3")
pygame.mixer.music.play()
welcome()
