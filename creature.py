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
    social_distance_factor = 0.9
    good_people = 0
    quarantine_threshold = 0.10
    
    def __init__(self, screen_size, x, y, population):
        super().__init__()
        self.image = susceptible_ball
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]

        self.state = 'healthy'
        self.pre_state = 'healthy'
        self.population = population
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

        self.moving = False
        self.assign_habits()


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
        self.check_moving()
        self.check_quarantine()

    def change_vel(self):
            self.x_vel = -self.x_vel
            self.y_vel = -self.y_vel

    def check_moving(self):
        if self.moving:
            point = next(self.path, "end")
            if point == "end":
                self.moving = False
            else:
                self.rect.center = point

    def assign_habits(self):
        chance = random.uniform(0, 1)
        if chance < Creature.social_distance_factor:
            self.type = "law_abiding"
            Creature.good_people += 1
        else:
            self.type = "rowdy"


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

    def check_quarantine(self):
        num = len(list(Creature.infected_group))
        if num > Creature.quarantine_threshold * self.population:
            self.quarantine()


    
    def infect(self):
        a = random.uniform(0, 1)
        if a < self.chance_of_infection:
            self.state = 'infected'

    def quarantine(self):
        if self.type == "law_abiding":
            if len(Creature.quarantine_points) > 0:
                min_dist = np.inf        
                for i in Creature.quarantine_points:
                    _dist = math.sqrt((self.rect.centerx - i[0])**2 + (self.rect.centery - i[1])**2)
                    if _dist < min_dist:
                        min_point = i
                        min_dist =_dist

                self.move(min_point, 100)
                Creature.quarantine_points.remove(min_point)
        
            self.quarantined = True

    def move(self, target, step):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = target[0]
        y2 = target[1]
        path = []

        for m in range(1, step + 1):
            n = step - m
            x = ((m*x2) + (n*x1))/(m + n) 
            y = ((m*y2) + (n*y1))/(m + n)
            path.append([x,y])

        self.path = iter(path)
        self.moving = True


    @classmethod
    def set_quarantine_points(self, width, height):
        x_points =[]
        y_points =[]
        Creature.quarantine_points = []
        
        for i in range(1, math.ceil(math.sqrt(Creature.good_people)) - 1):
            if Creature.good_people % i == 0:
                x_div = i

        y_div = math.floor(Creature.good_people/x_div)


        for j in range(0, x_div):
            x = (j * width)/(x_div - 1)
            x_points.append(x)


        for k in range(0, y_div):
            y = (k * height)/(y_div - 1)
            y_points.append(y)

        for l in x_points:
            for m in y_points:
                Creature.quarantine_points.append([l, m])

        return Creature.quarantine_points



if __name__ == "__main__":
    test = Creature.set_quarantine_points(1280, 720, 150)
    print(test)