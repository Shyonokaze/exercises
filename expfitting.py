# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 12:00:41 2017

@author: pyh
"""
import numpy as np

def target_function(x):
    return 3*x[0]*np.exp(-4*x[1])

class fit(object):
    def __init__(self,X,Y,a,b):
        self.input=X
        self.obtain=Y
        self.alpha=a
        self.beta=b
    
    def optimizer(self):
        delta_a=0
        delta_b=0
        for i in range(len(self.input)):
            ee=np.exp(-self.beta*self.input[i][1])
            delta_a=delta_a+(self.obtain[i]-self.alpha*self.input[i][0]*
                              ee)*self.input[i][0]*ee
            delta_b=delta_b+(self.obtain[i]-self.alpha*self.input[i][0]*
                              ee)*self.alpha*self.input[i][0]*self.input[i][1]*ee
        delta_a=delta_a/len(self.input)
        delta_b=delta_b/len(self.input)
        self.alpha=self.alpha+0.001*delta_a
        self.beta=self.beta-0.001*delta_b
        

x=[[10*np.random.uniform(),np.random.uniform()] for i in range(100)]
y=[target_function(x[i]) for i in range(len(x))]
fitting=fit(x,y,2,5)

for i in range(10000):
    fitting.optimizer()
    print(fitting.alpha,fitting.beta)
