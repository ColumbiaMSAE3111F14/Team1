Assignment3
===========

Meeting on Saturday, September 27th
-----------------------------------

Goal: get git working for everyone

  Member      |     Role
------------- | -------------
Ben Israel    | question asker
Chris Florencio-Aleman  | leader
Kathleen Kennedy  | Zuckerberg
Sean Ballinger  | scribe

- Tried to install git
    - Old OS X version on Chris' computer, can't install command line git
    - Is graphical client enough?
- Tried to use git
    - Resolve conflicts
    - Committing to master
    - Individual forks

Meeting time: 1hr 30 min

Meeting on Thursday, October 2nd
--------------------------------

Goal: start assignment 3 questions 6, 7

  Member      |     Role
------------- | -------------
Ben Israel    | scribe
Chris Florencio-Aleman  | absent
Kathleen Kennedy  | question asker
Sean Ballinger  | Zuckerberg

- Kathleen and Sean worked on PV plot
    - Results make sense, curves have expected shapes
    - To do:
        - PEP8 compliance
        - Discuss results in README of SolutionOutputs
        - Double check R used, units
- Ben started array plot
- Chris busy

Meeting time: 2hr 30 min

Meeting on Sunday, October 5th
------------------------------

Observations/Notes for 7.9:
The grid is approximately half up and half down for T=100,10. T=1 has somewhat more down than up. T=.1 has very very few up and T=.001 has none. This is consistent with the properties of the Boltzmann function.
Calculated probabilities of e^(1/T)/2 for each would be:
   T    p
.001 -  2.537979448774728×10^-435
.1   -  0.0000227
1    -  0.18394
10   -  0.452419
100  -  0.495025
p for T=.001 is effectively zero since the computer would round it to zero.
This generally makes physical sense. Temperature has disordering effect. This must taper off at high temperature since there is an upper limit to the disorder of the system, which is defined by a perfectly even and random distribution of states. This is why the difference between T=1 and T=10 is much larger than the difference btween T=10 and T=100. The curve of the Boltzmann function has a region of exponential growth for very low T, a brief relatively linear for a middle range of T, and an assymptote at 1 for large T. The differences in probability and the resulting grids for each temperature demonstarte this.