import pygame,sys
from pygame.locals import QUIT
import random
import time

pygame.init()

screen = pygame.display.set_mode((500, 600))
bg_color = (255, 255, 245)
width,height = 500,600
main_font = pygame.font.Font(None, 50)
font_color = (0, 0, 0)
box_color = (204, 229, 255)
game_won_color = (152, 251, 152)
game_loss_color = (255, 69, 0)

global name
global attempt
global g
global y
global r
global gray
global start_time
global end_time

word_list = []
f = open("C:\pythonProject1\P4\google-10000-english-usa-no-swears.txt.txt")

for x in f:
    new_w = str(x)
    new_w = new_w.rstrip("\n")
    if(len(new_w)==5):
        word_list.append((new_w))


# word_list = ["stare","bathe","spike","ruble","flock","unsad","gauze","paint","train","aside","serve"
#    ,"clasp","swear","north","clung","olden","silky","shore","break","brank","brick","blind","smite"
#     ,"refer","foxed","llama","flint","spank","chafe","frisk","prone","baked","stole","point","chill"
#     ,"helix","shove","floor","flyer","mount","boron","basin","piece","relay","flaky","colon","scour"
#     ,"sheet","fight","brake","knelt","embed","scald","godly","scold","sword","drunk","candy","drink"
#     ,"wired","table","beach","cloak","elbow","notch","nomad","offer","shark","field","badge","thyme"
#     ,"slept","swept","blaze","egret","vigor","braid","delta","dwelt","tower","boxer","lefty","cover"
#     ,"chasm"]

global word

def draw_squares():
    line_color = (0, 0, 0)
    square_size = 100
    # draws horizontal lines
    for i in range(0, 6):
        # checks if it needs a bolded line
        pygame.draw.line(screen, line_color, (0, i * square_size), (900, i * square_size), 5)
    # draws vertical lines
    for j in range(0, 5):
        # checks if it needs a bolded line
        pygame.draw.line(screen, line_color, (j * square_size, 0), (j * square_size, 900), 5)

def win_lose_screen(win,attempt,word,name):
    if(win):
        screen.fill(game_won_color)

        # prints out "Game Won!"
        game_won_title = main_font.render("Game Won!", 0, font_color)
        game_won_rectangle = game_won_title.get_rect(center=(width // 2, height // 2 - 100))
        screen.blit(game_won_title, game_won_rectangle)

        quit_text = main_font.render("Restart", 0, font_color)
        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        quit_surface.fill(box_color)
        quit_surface.blit(quit_text, (10, 10))
        restart_rectangle = quit_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(quit_surface, restart_rectangle)

        square_size = 100
        text_font = pygame.font.Font(None, 50)

        for i in range(0, len(word)):
            letter = text_font.render(word[i], 0, font_color)
            letter_rect = letter.get_rect(
                center=(square_size * i + square_size // 2, square_size * attempt + square_size // 2))
            screen.blit(letter, letter_rect)

    else:
        screen.fill(game_loss_color)

        # prints out "Game Over :("
        game_won_title = main_font.render("Game Over :(", 0, font_color)
        game_won_rectangle = game_won_title.get_rect(center=(width // 2, height // 2 - 100))
        screen.blit(game_won_title, game_won_rectangle)

        quit_text = main_font.render("Restart", 0, font_color)
        quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
        quit_surface.fill(box_color)
        quit_surface.blit(quit_text, (10, 10))
        restart_rectangle = quit_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(quit_surface, restart_rectangle)

        # print correct word
        square_size = 100
        text_font = pygame.font.Font(None, 50)

        for i in range(0, len(word)):
            pygame.draw.rect(screen, game_loss_color, [(i * 100, 5 * 100), (100, 100)], 100)


            letter = text_font.render(word[i], 0, font_color)
            letter_rect = letter.get_rect(
                center=(square_size * i + square_size // 2, square_size * attempt + square_size // 2))
            screen.blit(letter, letter_rect)

def check_name(word,name,attempt):
    g = []
    y = []
    r = []
    gray = []

    # if letter is in right place
    for i in range(0,len(name)):
        if(word[i]==name[i]):
            g.append(i)
            # print("green ",i)

    # if letter is in word but not right place
    for i in range(0,len(name)):
        if(word.__contains__(name[i]) and word[i] != name[i]):
            y.append(i)
            # print("yellow ",i)

    # if letter isnt in word at all
    for i in range(0, len(name)):
        if (not word.__contains__(name[i])):
            r.append(i)
            gray.append(name[i])
            # print(gray)
            # print("red ", i)

    # color in squares after guess
    for i in range(0,len(g)):
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(100*g[i], 100*attempt, 100, 100))
    for i in range(0,len(y)):
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(100*y[i], 100*attempt, 100, 100))
    for i in range(0,len(r)):
        pygame.draw.rect(screen, (128,128,128), pygame.Rect(100*r[i], 100*attempt, 100, 100))

    draw_squares()

    if (len(g) == 5):
        win_lose_screen(True,attempt,word,name)

    elif (attempt>=5):
        win_lose_screen(False,attempt,word,name)

    return gray

def print_name(name, attempt):
    square_size = 100
    text_font = pygame.font.Font(None, 50)

    for i in range(0,len(name)):
        letter = text_font.render(name[i], 0, font_color)
        letter_rect = letter.get_rect(center=(square_size * i + square_size // 2, square_size * attempt + square_size // 2))
        screen.blit(letter, letter_rect)

def backspace(name,attempt):
    square_size = 100
    text_font = pygame.font.Font(None, 50)
    white_font_color = (255, 255, 245)

    letter = text_font.render(name[-1], 0, white_font_color)
    index = len(name)-1
    letter_rect = letter.get_rect(center=(square_size * index + square_size // 2, square_size * attempt + square_size // 2))
    screen.blit(letter, letter_rect)

    # num0_rect = num0.get_rect(center=(square_size * self.col + square_size // 2, square_size *self.row + square_size // 2))

def run():
    screen.fill(bg_color)
    title = main_font.render("Welcome to Wordle", 0, font_color)
    title_rectangle = title.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(title, title_rectangle)

    start_text = main_font.render("Start Wordle", 0, font_color)
    start_surface = pygame.Surface((start_text.get_size()[0] + 20,
                                    start_text.get_size()[1] + 20))
    start_surface.fill(box_color)
    start_surface.blit(start_text, (10, 10))
    start_rectangle = start_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(start_surface, start_rectangle)

    g = []
    y = []
    r = []
    gray = []

    # name = "rates"
    attempt = 0
    name = ""
    word = random.choice(word_list)
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    screen.fill(bg_color)
                    draw_squares()
                    attempt = 0
                    name = ""
                    word = random.choice(word_list)
                    gray = []
                    print(word)
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    # print(gray)
                    if(event.unicode not in gray):
                        if(len(name)<5):
                            name += event.unicode
                            print_name(name, attempt)
                            # print("len ",len(name)
                if event.key== pygame.K_RETURN:
                    if(len(name)==5):
                        gray += check_name(word,name,attempt)
                        if(attempt<5):
                            print_name(name, attempt)
                        attempt+=1
                        name = ""
                if event.key == pygame.K_BACKSPACE:
                    if(len(name)>=1):
                        # print("backspace")
                        backspace(name,attempt)
                        name = name[:-1]
        pygame.display.update()

run()