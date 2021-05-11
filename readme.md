# Simulations of Spread of covid-like diseases using pygame.

### Inspiration for the Project

This project is hugely inspired by 3Blue1Brown's [Simulating an Epidemic](https://www.youtube.com/watch?v=gxAaO2rsdIs) video. When I first watched the video, I did not know much about programming. It mesmerized me so much that I decided to learn programming seriously.

### Aim of this Project

With this project, I plan to achieve the following:

1. Simulate the scenarios presented in the video:
   * Spread of the disease in a population of randomly moving dots.
   * Mechanism of quarantine
   * Travelling dots between different states/provinces
   * Dots social distancing
2. Being able to plot number of susceptible, infected, recovered and dead dots in real time.
3. Having some procedure of generating the visualization in video format (Currently achieved by saving each frame of the simulation in the video directory).

### Important Variables

Following are the variables in the creature.py file that changes the behaviour of the simulation:

* `self.chance_of_infection` - determines probability of a susceptible dot getting infected upon coming in contact with an infected dot.
* `self.chance_of_death` - determines probability of an infected dot dying due to the infection.
* `self.duration_of_infec` - determines the number of frames for which the infection lasts.

Further, the following variables in main.py can also be changed for changing the conditions of the simulation:

* `population` - determines the population with which the simulation starts with.
* `n_infected` - determines the number of people that are infected at the starting of the simulation.
* `screen_size`- size of the window of the simulation.
