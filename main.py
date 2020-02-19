import pygame
import os

pygame.init
WIN_WIDTH = 600 + 15
WIN_HEGIHT = 600 + 15
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
score = 0
SNAKE_SEG = pygame.image.load('Red_block.png')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEGIHT))
running = True


class Snake:
    VEL = score + 7
    def __init__(self, x = 300, y = 300, dirX = 0, dirY = 0):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY
    
    def draw(self):
        screen.fill(BLACK)
        # pygame.draw.rect(screen, WHITE, [self.x, self.y, 15, 15])
        screen.blit(SNAKE_SEG, (self.x, self.y))
        if self.x > 615:
            self.x = -15
        elif self.x < 0:
            self.x = 615
        elif self.y > 615:
            self.y = -15
        elif self.y < 0:
            self.y = 615
         
        self.x = self.x + self.dirX
        self.y = self.y + self.dirY

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.x = self.x + self.dirX
                    self.y = self.y + self.dirY
                    sys.exit()
                    break
                elif event.key == pygame.K_DOWN:
                    self.dirX = 0
                    self.dirY = 15
                    break
                elif event.key == pygame.K_RIGHT:
                    self.dirX = 15
                    self.dirY = 0
                    break
                elif event.key == pygame.K_LEFT:
                    self.dirX = -15
                    self.dirY = 0
                    break
            
        self.x = self.x + self.dirX
        self.y = self.y + self.dirY
        
        
clock = pygame.time.Clock()
snake = Snake()

while running:
    clock.tick(snake.VEL)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dirX = 0
                snake.dirY = -15

            elif event.key == pygame.K_DOWN:
                snake.dirX = 0
                snake.dirY = 15

            elif event.key == pygame.K_RIGHT:
                snake.dirX = 15
                snake.dirY = 0
            
            elif event.key == pygame.K_LEFT:
                snake.dirX = -15
                snake.dirY = 0
    # snake.x = snake.x + snake.dirX
    # snake.y = snake.y + snake.dirY
                
    snake.draw()
    
    
    # pygame.display.flip()
    pygame.display.update()
