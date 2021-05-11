from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
import pygame

class graph(pygame.sprite.Sprite):

    def __init__(self, screen_size):
        
        super().__init__()
        
        matplotlib.rc('axes',edgecolor='w')
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_xlabel('Time')
        ax.set_ylabel('No. of People')

        ax.spines['bottom'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='y', colors='white')

        self.TIME = 0
        self.fignum = 1
        self.graph_size = [480, 360]
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

        self.raw_fig = pygame.image.load(img)
        current_fig = pygame.transform.scale(self.raw_fig, self.graph_size)
        self.current_fig = current_fig

        self.image = self.current_fig

        img.close()
        self.fignum += 1