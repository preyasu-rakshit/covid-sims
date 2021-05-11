from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fnc_anim
import pandas as pd
import pygame

class graph(pygame.sprite.Sprite):

    def __init__(self, screen_size):
        
        super().__init__()
        self.TIME = 0
        self.fignum = 1
        self.graph_size = [280, 192]
        self.draw_plot()

        self.image = self.current_fig
        self.rect = self.image.get_rect()
        self.WIDTH = screen_size[0]
        self.HEIGHT = screen_size[1]
        self.rect.topright = (self.WIDTH, 0)
        

    def update(self):
        self.draw_plot()

    def draw_plot(self):
        self.data = pd.read_csv('data.csv')
        self.x = self.data['Time']
        self.y1 = self.data['Susceptible']
        self.y2 = self.data['Infected']
        self.y3 = self.data['Recovered']
        self.y4 = self.data['Dead']

        plt.cla()
        plt.plot(self.x, self.y1, label='Susceptible')
        plt.plot(self.x, self.y2, label='Infected')
        plt.plot(self.x, self.y3, label='Recovered')
        plt.plot(self.x, self.y4, label='Dead')
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.savefig(f'plots\plot{self.fignum}.png', transparent=True, backend='cairo')

        img = open(f'plots\plot{self.fignum}.png')

        raw_fig = pygame.image.load(img)
        current_fig = pygame.transform.scale(raw_fig, self.graph_size)
        self.current_fig = current_fig

        self.image = self.current_fig

        img.close()
        self.fignum += 1