import pygame
import random

pygame.init
pygame.font.init()
WIN_WIDTH = 600 + 15
WIN_HEGIHT = 600 + 45
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
score = 0
SNAKE_SEG = pygame.image.load('Red_block.png')
BAIT = pygame.image.load('Green_block.png')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEGIHT))
running = True
myfont = pygame.font.SysFont('score font', 30, True)
seglist = []


def draw_grid():
    screen.fill(WHITE)
    for i in range(0, 42):
        pygame.draw.line(screen, BLACK, (i*15, 0), (i*15, 615))
        pygame.draw.line(screen, BLACK, (0, i*15), (615, i*15))
    score_text = myfont.render(f'score = {score}', True, BLACK)
    screen.blit(score_text, (10, 625))

class Snake:
    VEL = score + 5
    def __init__(self, x = 300, y = 300, dirX = 0, dirY = 0):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY
    
    def move(self, event):
        if event.key == pygame.K_UP and self.dirY != 15:
            self.dirX = 0
            self.dirY = -15

        elif event.key == pygame.K_DOWN and self.dirY != -15:
            self.dirX = 0
            self.dirY = 15

        elif event.key == pygame.K_RIGHT and self.dirX != -15:
            self.dirX = 15
            self.dirY = 0
        
        elif event.key == pygame.K_LEFT and self.dirX != 15:
            self.dirX = -15
            self.dirY = 0
    
    def draw(self):
        Snake.snake_target(self)
        screen.blit(SNAKE_SEG, (self.x, self.y))
        if self.x > 600:
            self.x = -15
        elif self.x < 0:
            self.x = 615
        elif self.y >= 615:
            self.y = -15
        elif self.y < 0:
            self.y = 615
         
        self.x = self.x + self.dirX
        self.y = self.y + self.dirY 

        # Body.draw(self)          

    
    def snake_target(self):
        pygame.draw.line(screen, BLUE, (self.x + 7, 0), (self.x + 7, 615), 2)
        pygame.draw.line(screen, BLUE, (0, self.y + 7), (615, self.y + 7), 2)

class Bait:
    def __init__(self, eaten = True, x = random.randint(0, 615), y = random.randint(0, 615)):
        self.x = x
        self.y = y
        self.eaten = eaten

    def generator(self):
        if self.eaten == True:
            # while self.x != snake.x and self.y != snake.y:
            self.x = random.randint(1, 40)*15
            self.y = random.randint(1, 40)*15
            self.eaten = False
        return self.x, self.y

    def draw(self):
        screen.blit(BAIT, Bait.generator(self))
        
    def check_eaten(self):
        global score
        if self.x == snake.x and self.y == snake.y:
            self.eaten = True
            score += 1
            seglist.append(Body(body.add_seg()[0], body.add_seg()[1]))


class Body:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def draw(self):
        for seg in seglist:
            if len(seglist) == 0:
                seg.x = snake.x - snake.dirX
                seg.y = snake.y - snake.dirY
            else:
                last_seg = len(seglist) - 1
                seg.x = seglist[last_seg].x - snake.dirX
                seg.y = seglist[last_seg].y - snake.dirY
            screen.blit(SNAKE_SEG, (seg.x, seg.y))

    def add_seg(self):
        if len(seglist) == 0:
            self.x = snake.x - snake.dirX
            self.y = snake.y - snake.dirY
        else:
            last_seg = len(seglist) - 1
            self.x = seglist[last_seg].x - snake.dirX
            self.y = seglist[last_seg].y - snake.dirY
        return self.x, self.y

clock = pygame.time.Clock()
snake = Snake()
bait = Bait()
body = Body()


while running:
    clock.tick(snake.VEL)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            snake.move(event)

    draw_grid()
    bait.draw()
    snake.draw()
    body.draw()
    bait.check_eaten()          
    
    pygame.display.update()
