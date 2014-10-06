# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy,
# and Chris Florencio-Aleman
# Homework 3; PP7

import array_plot as ap

# Part 4
ap.plot_array(ap.create_uniform_array(100, 1), "7.4: all up")    # Test all up array
ap.plot_array(ap.create_uniform_array(100, 0), "7.4: all down")  # Test all down array

# Part 5
ap.plot_array(ap.create_random_array(100, .5), "7.5")

# Part 6
ap.plot_array(ap.create_probability_array(100, .25), "7.6: p=.25")  # Test p=.25
ap.plot_array(ap.create_probability_array(100, .5), "7.6: p=.5")    # Test p=.5
ap.plot_array(ap.create_probability_array(100, .75), "7.6: p=.75")  # Test p=.75

# Part 8
# Switched to 500x500 to show lower probabilities
ap.plot_array(ap.create_boltzmann_array(500, 100), "7.8: T=100")    # Test T=100
ap.plot_array(ap.create_boltzmann_array(500, 10), "7.8: T=10")      # Test T=10
ap.plot_array(ap.create_boltzmann_array(500, 1), "7.8: T=1")        # Test T=1
ap.plot_array(ap.create_boltzmann_array(500, .1), "7.8: T=.1")      # Test T=.1
ap.plot_array(ap.create_boltzmann_array(500, .001), "7.8: T=.001")  # Test T=.001
