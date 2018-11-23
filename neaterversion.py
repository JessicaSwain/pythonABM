#put a version, type of code etc __version__ 1.0.0
#basic statement regarding code

#put it in as steps? step one initalise etc.



#IMPORTING SECTION#
'''It is important to always keep imports at the top of the page'''
import random as r
#random number generator, to be used as the function random.randint
import operator #currently not in use
'''find out where operator was used so can comment this out'''
import matplotlib.pyplot as plot
#plots the agents on a graph
import time
import agentframework as ownclass
'''learnt that imports can be labelled as a name you may understand better
therefore decided to shorten random and labelled agent framework as own class
so I could remember that this is the class element that I produced'''
import csv



#VARIABLE SET UP#
'''here the variables have been set up for use within the code below'''
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20



#def defines our own functions and reuses them throughout the programme
def distance_between(agents_row_a, agents_row_b):
    """
    distance between row a and row b is the element of interest
    this function then returns the equation, with use of the class built in the
    agent framework file
    """
    return (((agents_row_a._x - agents_row_b._x)**2) + 
    ((agents_row_a._y - agents_row_b._y)**2))**0.5
#two rows in the list and the value between them

#r_seed = 1
#r.seed(r_seed)
#this sets the random function

environment = []
#empty environment list

#the following code is from practical 6 I/O and makes use of inputting a .txt 
#file
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

agents = []
distances = []
#this is creating an empty list
#to add to this we will need to use the append command later on


#range allows us to loop through a sequence of numbers
#'for' command is what makes the loop
#this below is making the agents
for i in range(num_of_agents):
    agents.append(ownclass.Agent(environment, agents, r_seed))
#this is adding data to the agents list we made above
#making use of the environment list produced from txt file
#list of agents is being added to from the agent framework .py file

'''print (agents[i]._y)'''
#need to check how to print one agent?

# Move the agents with this code below
#i,j,k is like how x is used as an example letter
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print (agents[i].y())
        #print (agents[i]._y)
        r.shuffle (agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
'''this section here is trying to ensure the properties of the .x and .y is 
working
agents[i]._y = 10
update: the underscore is a polite notice to other coders to not mess with the 
variable
print (agents[i]._y) in more advanced programming, 
doing the above code would cause an error, in python it does not'''

#distance = distance_between(agents[0], agents[1])
#print(distance)
'''above is no longer needed given the more sophisticated code below'''


start = time.clock()
#this starts the clock running as your code begins


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
#than the other, see code below
      
for i in range (0, num_of_agents):
    for j in range(0, i):
        distance = distance_between(agents[i], agents[j])
        distances.append(distance)
#continuous loop in finding the distance between two agents
#less computationally expensive than using if, which has to check everything 
#this continues with the process more smoothly

#print(distances)
#used this just to make sure the code regarding distances was successful

high = max(distances)
low = min(distances)
#high and low are assigned the highest and lowest variable in the distance list
print (high, low)


plot.xlim(0, 99)
plot.ylim(0, 99)
plot.imshow(environment)
for i in range(num_of_agents):
    plot.scatter(agents[i]._x, agents[i]._y)
plot.show()
#this section is just to produce the graph in the console
#plot is the shortcut name I have produced for matplot


end = time.clock()
#this ends the clock running time

print("time = " + str(end - start))
#how long did that block of code take to load?