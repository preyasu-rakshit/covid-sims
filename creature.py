import pygame
import random
import numpy as np
import math

pygame.init()
guy_size = (10, 10)

red_ball = pygame.image.load('assets\Red.png')
infected_ball = pygame.transform.scale(red_ball, guy_size)

white_ball = pygame.image.load('assets\white.png')
susceptible_ball = pygame.transform.scale(white_ball, guy_size)

green_ball = pygame.image.load('assets\green.png')
recovered_ball = pygame.transform.scale(green_ball, guy_size)

blue_ball = pygame.image.load('assets\\blue.png')
vaccinated_ball = pygame.transform.scale(blue_ball, guy_size)


class Creature(pygame.sprite.Sprite):
    
    susceptible_group = pygame.sprite.Group()    
    infected_group = pygame.sprite.Group()    
    recovered_group = pygame.sprite.Group()    
    Deaths = 0
    quarantine_points = []
    
    def __init__(self, screen_size, x, y):
        super().__init__()
        self.image = susceptible_ball
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]

        self.state = 'healthy'
        self.pre_state = 'healthy'
        self.quarantined = False
        self.time = 0
        self.time_of_infection = 0
        self.chance_of_infection =  0.9
        self.chance_of_death =  0.2
        self.duration_of_infec = 1400
        
        Creature.susceptible_group.add(self)

        self.possible_vel = [1, -1, 2, -2]
        self.x_vel = random.choice(self.possible_vel)   
        self.y_vel = random.choice(self.possible_vel)   
        self.possible_vel.append(0)


    def update(self):
        self.time += 1

        if not self.quarantined:
            if self.time % 8 ==0:
                self.x_vel = random.choice(self.possible_vel)   
                self.y_vel = random.choice(self.possible_vel)

        else:
            self.x_vel = 0
            self.y_vel = 0
        
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.left >= self.WIDTH:
            self.rect.left = 0

        if self.rect.right <= 0:
            self.rect.right = self.WIDTH

        if self.rect.top >= self.HEIGHT:
            self.rect.top = 0

        if self.rect.bottom <= 0:
            self.rect.bottom = self.HEIGHT


        if (self.time - self.time_of_infection) > self.duration_of_infec and self.state == 'infected':
            a = random.uniform(0, 1)
            if a < self.chance_of_death:
                self.state = 'died'
            else:
                self.state = 'recovered' 

        self.check_state()

    def change_vel(self):
        self.x_vel = -self.x_vel
        self.y_vel = -self.y_vel

    def check_state(self):
        
        if self.pre_state != self.state:
            if self.state == 'infected':
                self.image = infected_ball
                self.time_of_infection = self.time
                Creature.infected_group.add(self)
                Creature.susceptible_group.remove(self)
                self.pre_state = 'infected'

            if self.state == 'recovered':
                self.image = recovered_ball
                Creature.recovered_group.add(self)
                Creature.infected_group.remove(self)
                self.pre_state = 'recovered'

            if self.state == 'died':
                Creature.Deaths += 1
                self.kill()

    
    def infect(self):
        a = random.uniform(0, 1)
        if a < self.chance_of_infection:
            self.state = 'infected'

    def quarantine(self): 
        if len(Creature.quarantine_points) > 0:
            min_dist = np.inf        
            for i in Creature.quarantine_points:
                _dist = math.sqrt((self.rect.centerx - i[0])**2 + (self.rect.centery - i[1])**2)
                if _dist < min_dist:
                    min_point = i
                    min_dist =_dist

            self.rect.center = min_point
            Creature.quarantine_points.remove(min_point)
        
        self.quarantined = True


    @classmethod
    def set_quarantine_points(self, width, height, population):
        x_points =[]
        y_points =[]
        
        for i in range(1, math.ceil(math.sqrt(population)) + 1):
            if population % i == 0:
                x_div = i

        y_div = math.floor(population/x_div)

        for j in range(x_div):
            x_points.append(j * (width/x_div))

        for k in range(y_div):
            y_points.append(k * (height/y_div))

        for l in x_points:
            for m in y_points:
                Creature.quarantine_points.append([l, m])