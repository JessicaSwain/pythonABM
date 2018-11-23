# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:56:50 2018

@author: gy15js
"""

'''NEED TO COMMENT OUT THIS SECTION OF CODE'''


import random as r

class Agent():
        def __init__ (self, environment, agents, r_seed):
            self._y = r.randint(0,99)
            self._x = r.randint(0,99)
        #def __init__(environment): added the two together to ensure use of 
        #init
            self.environment = environment
            self.store = 0
            self.agents = agents
            self.store = 0
            self.r_seed = 1
            self.store = 0

        def move(self):
            if r.random() < 0.5:
                self._y = (self._y + 1) % 100
            else:
                self._y = (self._y - 1) % 100

            if r.random() < 0.5:
                self._x = (self._x + 1) % 100
            else:
                self._x = (self._x - 1) % 100
                
        def eat(self): #can you make it eat what is left?
            if  self.environment[self._y][self._x] > 10:
                self.environment[self._y][self._x] -= 10
                self.store += 10
         
         #this method tells the agents to share with their nearby neighbours 
         #that are closest
        def share_with_neighbours (self, neighbourhood):
            for agent in self.agents:
                dist = self.distance_between(agent)
                #for agents, find the distance between them
            if dist <= neighbourhood:
                #if the distance is lower than or equals to the neighbourhood
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                #averaging self.store and agent.store out
                agent.store = ave
                #print("sharing" + str(dist) + "" + str(ave)) 
                '''this is just to make sure it works, now that it does can 
                comment out'''
                
        def distance_between (self,agent):
            return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5