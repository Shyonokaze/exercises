# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:00:41 2017

@author: pyh
"""
import numpy as np
import matplotlib.pyplot as plt

def target_function(x):
    return 3*(x[0]**2)*np.exp(-4*x[1])+np.random.uniform()

class fit(object):
    def __init__(self,X,Y,a,b,c):
        self.input=X
        self.obtain=Y
        self.alpha=a
        self.beta=b
        self.theta=c
        
    def optimizer(self):
        delta_a=0
        delta_b=0
        delta_c=0
        for i in range(len(self.input)):
            ee=np.exp(-self.beta*self.input[i][1])
            delta_a=delta_a+(self.obtain[i]-self.alpha*(self.input[i][0]**self.theta)*
                              ee)*(self.input[i][0]**self.theta)*ee
            delta_b=delta_b+(self.obtain[i]-self.alpha*(self.input[i][0]**self.theta)*
                              ee)*self.alpha*(self.input[i][0]**self.theta)*self.input[i][1]*ee
            delta_c=delta_c+(self.obtain[i]-self.alpha*(self.input[i][0]**self.theta)*
                              ee)*(self.input[i][0]**self.theta)*np.log(self.input[i][0])*self.alpha*ee
        delta_a=delta_a/len(self.input)
        delta_b=delta_b/len(self.input)
        delta_c=delta_c/len(self.input)
        self.alpha=self.alpha+0.001*delta_a
        self.beta=self.beta-0.001*delta_b
        self.theta=self.theta+0.0001*delta_c
    
    def getting_cost(self):
        cost=0
        for i in range(len(self.input)):
            cost=cost+(self.obtain[i]-self.alpha*(self.input[i][0]**self.theta)*
                       np.exp(-self.beta*self.input[i][1]))**2
        cost=cost/len(self.input)
        return cost
    
    def getting_fitting(self,x):
        y=[]
        for i in range(len(x)):
            y.append(self.alpha*x[i][0]*np.exp(-self.beta*x[i][1]))
        return y               
        

x=[[10*np.random.uniform(),np.random.uniform()] for i in range(100)]
y=[target_function(x[i]) for i in range(len(x))]
fitting=fit(x,y,2,5,2)
cost=[]

for i in range(1000):
    fitting.optimizer()
    print(fitting.theta)
#    cost.append(fitting.getting_cost())
    
#plt.plot(range(1000),cost)
#plt.show()

    
