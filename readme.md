# Simulations of Spread of covid-like diseases using pygame.

### Inspiration for the Project

This project is hugely inspired by 3Blue1Brown's [Simulating an Epidemic](https://www.youtube.com/watch?v=gxAaO2rsdIs) video. When I first watched the video, I did not know much about programming. It mesmerized me so much that I decided to learn programming seriously.

### Aim of this Project

With this project, I plan to achieve the following:

1. Simulate the scenarios presented in the video:
   * Spread of the disease in a population of randomly moving dots. *(done)*
   * Mechanism of quarantine. *(done)*
   * Travelling dots between different states/provinces. *(pending)*
   * Dots social distancing. *(done)*
2. Being able to plot number of susceptible, infected, recovered and dead dots in real time.*(done)*
3. Having some procedure of generating the visualization in video format (Currently achieved by saving each frame of the simulation in the video directory). *(done)*

### Important Variables

Following are the variables in the creature.py file that changes the behaviour of the simulation:

* `self.chance_of_infection` - determines probability of a susceptible dot getting infected upon coming in contact with an infected dot.
* `self.chance_of_death` - determines probability of an infected dot dying due to the infection.
* `self.duration_of_infec` - determines the number of frames for which the infection lasts.
* `Creature.social_distance_factor` - determines the percentage of dots that obey lockdown restrictions
* `Creature.quarantine_threshold` - determines after what percentage of the population gets infected, the lockdown is initiated.
* `Creature.quarantine_end_threshold`- determines at what percentage of cases lockdown ends.

Further, the following variables in main.py can also be changed for changing the conditions of the simulation:

* `population` - determines the population with which the simulation starts with.
* `n_infected` - determines the number of people that are infected at the starting of the simulation.
* `screen_size`- size of the window of the simulation.
* `video`-  determines whether or not all frames are saved from the beginning of the simulation. Saving frames can be toggled at any point in the simulation by pressing 'v' in the keyboard.

### Sample Run

A sample run of the simulation can be found [here.](https://www.youtube.com/watch?v=SqPx3Qpeq6A) *(Currently outdated, does not showcase the quarantine feature)*
