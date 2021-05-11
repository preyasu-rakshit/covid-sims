from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fnc_anim
import pandas as pd
import pygame
import random
import time
import threading

x1 = []
y1 = []

def animate(i):
    x = random.uniform(2, 400)
    y = random.uniform(1, 10)
    x1.append(x)
    y1.append(y)

    plt.cla()
    plt.plot(x1, y1, label='Susceptible')
    # plt.plot(x, y2, label='Infected')
    # plt.plot(x, y3, label='Recovered')
    # plt.plot(x, y4, label='Dead')

    plt.legend(loc='upper right')
    plt.tight_layout()



def plot():
    ani = fnc_anim(plt.gcf(), animate, interval=1000)

plotting_thread = threading.Thread(target=plot)
plotting_thread.start()
plotting_thread.daemon = True

while True:
    print('hi')
    time.sleep(1)