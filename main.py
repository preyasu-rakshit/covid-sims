import pygame
import sys
import random
from creature import Creature

population = 100
n_infected = 1

def infect_onclick():
    susceptible_creatures = list(Creature.susceptible_group)
    if len(susceptible_creatures) > 0:
        i = random.choice(susceptible_creatures)
        i.state = 'infected'
        # susceptible_creatures.remove(i)
    else:
        return


def make_video(screen):

    _image_num = 0

    while True:
        _image_num += 1
        str_num = "000" + str(_image_num)
        file_name = "image" + str_num[-4:] + ".jpg"
        pygame.image.save(screen, 'video\ '.rstrip(' ') + file_name)
        yield


pygame.init()
clock = pygame.time.Clock()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Covid Simulation")

creatures = pygame.sprite.Group()

for i in range(population):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    creatures.add(Creature(screen_size, x, y))

for i in range(n_infected):
    guy = random.choice(list(Creature.susceptible_group))
    guy.state = 'infected'
    creatures.update()


save_screen = make_video(screen)
video = False
T = 10000
for time in range(T):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            video = not video


    collision_group = pygame.sprite.groupcollide(Creature.susceptible_group, Creature.infected_group, False, False)
    for i in collision_group:
        i.infect()
        i.x_vel *= -1
        i.y_vel *= -1
    

    screen.fill((0, 0, 0))
    creatures.update()
    creatures.draw(screen)
    pygame.display.flip()
    
    if video:
        next(save_screen)    
    
    # print(len(Creature.infected_group))
    # print(len(Creature.susceptible_group))
    print("number of deaths:", Creature.Deaths)
    print("number of recoveries:", len(list(Creature.recovered_group)))
    clock.tick(60)


pygame.quit()
# print(len(Creature.infected_group))