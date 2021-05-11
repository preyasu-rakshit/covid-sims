import pygame
import sys
import random
from creature import Creature
from ploting import graph
import csv
import os, shutil
import threading
from time import sleep

pygame.init()
clock = pygame.time.Clock()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Covid Simulation")

creatures = pygame.sprite.Group()
population = 300
n_infected = 1

_graph = graph(screen_size)
plot = pygame.sprite.Group()
plot.add(_graph)


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


def delete_all(path_to_folder):
    for filename in os.listdir(path_to_folder):
        file_path = os.path.join(path_to_folder, filename)
        try:           
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def draw_graph():
    while True:
        plot.update()
        sleep(1)
        
plotting_thread = threading.Thread(target=draw_graph)
plotting_thread.daemon = True

for i in range(population):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    creatures.add(Creature(screen_size, x, y))

for i in range(n_infected):
    guy = random.choice(list(Creature.susceptible_group))
    guy.state = 'infected'
    creatures.update()


headers = ['Time', 'Susceptible', 'Infected', 'Recovered', 'Dead']

with open('data.csv', 'w') as d:
    csv_writer = csv.DictWriter(d, fieldnames=headers)
    csv_writer.writeheader()

plotting_thread.start()
save_screen = make_video(screen)
video = False
T = 5000
for time in range(T):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            delete_all('plots\\')
            pygame.image.save(_graph.raw_fig, 'result.png')
            sys.exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            video = not video


    collision_group = pygame.sprite.groupcollide(Creature.susceptible_group, Creature.infected_group, False, False)
    for i in collision_group:
        i.infect()
        i.x_vel *= -1
        i.y_vel *= -1
    
    susceptible_num = len(list(Creature.susceptible_group))
    infected_num = len(list(Creature.infected_group))
    recovered_num = len(list(Creature.recovered_group))
    death_num = Creature.Deaths
    population_alive = susceptible_num + infected_num + recovered_num

    data = [time, susceptible_num, infected_num, recovered_num, death_num]

    with open('data.csv', 'a') as d:
        csv_writer = csv.writer(d)
        csv_writer.writerow(data)


    screen.fill((0, 0, 0))
    
    plot.draw(screen)
    creatures.update()
    creatures.draw(screen)
    pygame.display.flip()
    
    if video:
        next(save_screen)    
    
    clock.tick(60)


pygame.quit()
delete_all('plots\\')
pygame.image.save(_graph.raw_fig, 'result.png')