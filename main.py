import pygame

pygame.init
WIN_WIDTH = 600 + 15
WIN_HEGIHT = 600 + 15
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
score = 0
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEGIHT))
running = True


class Snake:
    VEL = 0
    def __init__(self, x = 300, y = 300, dirX = 0, dirY = 0):
        self.x = x
        self.y = y
        self.dirX = dirX
        self.dirY = dirY
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, 15, 15]) 

    def move(self, event):
        # for event in pygame.event.get():
        while event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                self.dirX = 0
                self.dirY = -15
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
            # elif event.mouse == pygame.MOUSEBUTTONDOWN:
            #     print('press')
        self.x = self.x + self.dirX
        self.y = self.y + self.dirY
        
        
clock = pygame.time.Clock()
snake = Snake()

while running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        snake.move(event)
    snake.draw()
    
    
    pygame.display.flip()
    pygame.display.update()
    




    

