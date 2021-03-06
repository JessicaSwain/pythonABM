# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#put a version, type of code etc __version__ 1.0.0
#basic statement regarding code

#----------------------------------------------------------------------------#

##############################################################################
#######################  IMPORTING SECTION  ##################################
'''It is important to always keep imports at the top of the page'''

import random as r
#random number generator
#used first in random.randint, then with r_seed and r.shuffle
import operator 
'''currently not in use'''
#used to import functions not already built into python
import matplotlib.pyplot as plot
#plots the agents on a graph
import time
#this times how long it takes to get through the code
import agentframework as ownclass
#class for object orientated turn in the programming course
import csv
#this is to read files outside of python e.g. excel, .txt

'''learnt that imports can be labelled as a name you may understand better
therefore decided to shorten random and labelled agent framework as own class
so I could remember that this is the class element that I produced'''

#----------------------------------------------------------------------------#

##############################################################################
######################  VARIABLE SET UP  #####################################
'''here the variables have been set up for use within the code below'''

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#----------------------------------------------------------------------------#

##############################################################################
########################  LIST SET UP  #######################################
'''before completing any code, there is a need to have lists to add to'''

environment = []
#empty environment list
agents = []
#empty list to create agents in
distances = []
#the distance calculations will be added to this list later on

#to add to this we will need to use the append command at a later date

'''NOTE: not all lists are created first, some are created within the code'''

#----------------------------------------------------------------------------#

##############################################################################
#########################  TIMING THE CODE  ##################################
'''timing the code is often a good idea to see how quickly python can complete
the commands'''

start = time.clock()
#this starts the clock running as your code begins

#----------------------------------------------------------------------------#

##############################################################################
######################  INPUTTING .TXT FILES  ################################
'''the following code is from practical 6 I/O and makes use of inputting a .txt 
#file'''

f = open('in.txt', 'r')
#r is for read only
reader = csv.reader (f)
#imports csv reader module for importing raster files etc.
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(int(value))
#int was added to prevent the error regarding image
#need to ensure this is created before the agents list otherwise agents are 
#using an empty list
f.close()
#closes the file above

#this needs to be before setting up the agents, otherwise they are set up with
#empty lists for environment, which will break the code

#----------------------------------------------------------------------------#

##############################################################################
########################  MAKING AGENTS  #####################################
'''This is the code that makes the points seen on the plotted output, without
making these agents, nothing can be moved or interacted with'''

r_seed = 15
#r_seed is the random import above and seed ensures that each time the code 
#presents the same numbers, by setting this to 15, this means the first agent 
#will always start at 15 (see the console for this)

for i in range(num_of_agents):
    #range allows us to loop through a sequence of numbers without needing to 
    #type the code out over and over again
    r_seed += 10
    #this will add 10 to each agent through the r_seed function
    
    '''CODE CHECK'''
    print("r_seed",r_seed)
    '''by printing the values of r_seed can see how the commands above are 
    working'''
    
    agents.append(ownclass.Agent(environment, agents, r_seed))
#this is adding data to the agents list we made above
#making use of the environment list produced from txt file
#list of agents is being added to from the agent framework.py file

#~~~~~~~~~~~~~~~~~~~~ ##  WHAT THE ABOVE IS DOING  ##~~~~~~~~~~~~~~~~~~~~~~~~#
#'for' command is what makes the loop
#'i' is an example letter as we use x and y in real life conversations
#this code above is asking the model, for every (i aka. agent) in the 
#list of agents, change the random number by adding 10, and then add the 
#commands written in the class 'agentframework' (known here as my class)

#----------------------------------------------------------------------------#

##############################################################################
##########################  MOVING AGENTS  ###################################
'''NOTE: This code has been shortened to make the code more secure in running, 
older versions can be found within the GitHub repository

This code moves the agent around the grid we have set, further additions have
also told the agents to eat and share food with their neighbours too'''

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        '''CODE CHECK - TO MAKE SURE IT IS WORKING
        print (agents[i]._y)'''
        r.shuffle (agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#~~~~~~~~~~~~~~~~~~~~ ##  WHAT THE ABOVE IS DOING  ##~~~~~~~~~~~~~~~~~~~~~~~~#
#'for' command is the loop as explained above
#'i' and 'j' are example letters
#this code tells the model, for every iteration of the model, and for every
#agent in the agent list, shuffle the actions below (which is moving, eating
#and sharing with neighbours)
        
#----------------------------------------------------------------------------#

##############################################################################
########################  ADDITIONAL CODE  ###################################
'''this section here is trying to ensure the properties of the .x and .y are 
protected with with the changes made (instead of .x and .y now ._x and ._y)

agents[i]._y = 10
print (agents[i]._y) 
The understanding was, the underscore should prevent any changes such as the
one above being able to be processed without an error message about it

However, the line of code above did change the value...

Learnt that the underscore is not something that will protect the code 
officially, instead it is a polite notice to other coders to not mess with the 
variables -just incase any changes break the code etc. in more advanced 
programming, doing the above code would cause an error, 
in python it does not.'''

#----------------------------------------------------------------------------#

##############################################################################
####################  DEFINING OWN FUNCTIONS  ################################
'''It is possible to create your own functions, these are created using 'def'
these are like their own world, and they do not link to any code within the
model, code in here then allows the code beneath it to be tidier as we can
just use this function instead of having to retype long equations each time'''

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) + 
    ((agents_row_a._y - agents_row_b._y)**2))**0.5

#~~~~~~~~~~~~~~~~~~~~ ##  WHAT THE ABOVE IS DOING  ##~~~~~~~~~~~~~~~~~~~~~~~~#
#def defines our own functions and reuses them throughout the programme
#this function is finding the distance (as a value) between row a and row b 
#(this is our area of interest)
#the function involves a long equation that finds this distance
#this function returns the equation while using the class built in the agent
#framework (own class) .py file

#----------------------------------------------------------------------------#

##############################################################################
########################  CODE IMPROVEMENTS  #################################

'''r_seed = 1
r.seed(r_seed)
#this sets the random function'''

'''After adding R.shuffle realised nothing was moving as expected, although
r.seed sets the starting point, the command needed to be bult within other code
for r.shuffle to then work and allow agents to change each iteration'''

#----------------------------------------------------------------------------#

##############################################################################
#########  CALCULATING THE DISTANCE BETWEEN VARIABLES  #######################
'''this code uses a for loop to calculate the distances between the agents'''

'''CODE IMPROVEMENT'''

'''for agents_row_a in agents:
    for agents_row_b in agents:
        if (agents_row_a > agents_row_b):
            #this optimises the loop so no repetitions
#this is a for loop in a loop so A will stay as 1 and B will go through to 10,
 and then A will move to 2 and keep going to find all distances
            distance = distance_between(agents_row_a, agents_row_b)
            distances.append (distance)
#for random agent 1(out of 10) and for agent 2 (out of 10) find the distance 
between them, and it will continue'''

#noticed this was wrong and only doing the calculation if one y was larger 
#than the other, the correct code for figuring out the distances is below
 
'''CODE IMPROVEMENT'''

#distance = distance_between(agents[0], agents[1])
#print(distance)

'''above is no longer needed given the more sophisticated code below'''


for i in range (0, num_of_agents):
    for j in range(0, i):
        distance = distance_between(agents[i], agents[j])
        distances.append(distance)

#~~~~~~~~~~~~~~~~~~~~ ##  WHAT THE ABOVE IS DOING  ##~~~~~~~~~~~~~~~~~~~~~~~~#       
#continuous loop in finding the distance between two agents
#less computationally expensive than using if, which has to check everything 
#this continues with the process more smoothly


'''CODE CHECK'''
#print(distances)
'''used this just to make sure the code regarding distances was successful'''


high = max(distances)
low = min(distances)
#high and low are assigned the highest and lowest variable in the distance 
#list, by using the max and min function
print (high, low)

#----------------------------------------------------------------------------#

##############################################################################
#######################  VISUALISING RESULTS  ################################

plot.xlim(0, 99)
plot.ylim(0, 99)
plot.imshow(environment)
for i in range(num_of_agents):
    plot.scatter(agents[i]._x, agents[i]._y)
plot.show()
#this section is just to produce the graph in the console
#plot is the shortcut name I have produced for matplot

#----------------------------------------------------------------------------#

##############################################################################
#########################  TIMING THE CODE  ##################################

end = time.clock()
#this ends the clock running time

print("time = " + str(end - start))
#how long did that block of code take to load? This will show the time taken.

#----------------------------------------------------------------------------#