import sys
import pygame
from pygame.math import Vector2

class DRAW:
    def __init__(self):
        self.drawed_item = []
        self.width = 10
        self.height = 10
    def draw(self):

        self.mouse_position = pygame.mouse.get_pos()
        self.key = pygame.key.get_pressed()
        self.left, self.middle, self.right = pygame.mouse.get_pressed()

        if self.left:
            self.x, self.y = self.mouse_position
            self.drawed_item.append(Vector2(int(self.x), int(self.y)))
        elif self.right:
            self.drawed_item.clear()
        elif self.key[pygame.K_UP]:
            self.width += 1
            self.height += 1
        elif self.key[pygame.K_DOWN]:
            self.width -= 1
            self.height -= 1

    def draw_table(self):
        for rect in self.drawed_item:
            pygame.draw.ellipse(screen, 'black', pygame.Rect(rect.x, rect.y, self.width, self.height))




pygame.init()
cell_size = 10
cell_number = 80
screen = pygame.display.set_mode((800, 800))
screen_rect = screen.get_rect(topleft=(0, 0))
print(screen_rect)

draw = DRAW()
Clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    draw.draw()
    draw.draw_table()




    pygame.display.update()
    Clock.tick(1200)
#Project Completed