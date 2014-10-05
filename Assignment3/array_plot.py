# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy, Chris Florencio-Alerman
# Homework 3; PP7

import matplotlib.pyplot as plt
import numpy as np
import random

def plot_array(array, title):
    '''Part 1: Plot an array using pcolor and title it'''
    plt.pcolor(array, vmin=0, vmax=1) #1/up=red, 0/down=blue
    plt.title=title
    print title
    plt.show()

def create_uniform_array(n, state):
    '''Part 4: Returns an nxn array with all up or all down'''
    if state: #1=up, 0=down
        return np.ones((n,n))
    else:
        return np.zeros((n,n))

def create_random_array(n,p):
    '''Part 5: Returns an nxn array with random cell values'''
    #Evaluate a random number in [0,1) for each cell in an nxn array
    return np.array([[int(random.random()<.5)\
             for i in range(n)] for j in range(n)])

def create_probability_array(n,p):
    '''Part 6: Returns an nxn array with p probability of up in each cell'''
    #Evaluate a random number in [0,1) for each cell in an nxn array
    return np.array([[int(random.random()<p)\
             for i in range(n)] for j in range(n)])

def boltzmann(E,T):
    '''Part 7: Determine the Boltzmann probability for a given E and T'''
    return np.exp(-E/T)

def create_boltzmann_array(n,T):
    '''Part 8: Create an nxn array using Boltzmann probability at E=1, T'''
    return create_probability_array(n,.5*boltzmann(1,T))