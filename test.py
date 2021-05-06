import pygame
import sys
import random

screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Simulation")

clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Creature(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.color = color

        pygame.draw.rect(self.image, self.color, [x, y, 20, 20])
        self.rect = self.image.get_rect()


creatures = pygame.sprite.Group()
creature = Creature(red, 20, 40)
creatures.add(creature)

# for i in range(10):
#     x = random.randint(0, 800)
#     y = random.randint(0, 600)
#     creatures.add(Creature(red, x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    
    creatures.update()
    screen.fill((0, 0, 0))

    creatures.draw(screen)

    pygame.display.flip()
    clock.tick(60)

