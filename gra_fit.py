# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:05:57 2017

@author: pyh
"""


class Gra_fit(object):
    def __init__(self,f,X,Y,parameter,learning_rate):
        self.input=X
        self.obtain=Y
        self.para=parameter
        self.function=f
        self.lr=learning_rate
    
    
    def __deri(self,x):
        para_min=[self.para[i] for i in range(len(self.para))]
        para_max=[self.para[i] for i in range(len(self.para))]
        der_para=[]
#        print(para_max,para_min)
        for i in range(len(self.para)):
            para_min[i]=para_min[i]-2e-6
            para_max[i]=para_max[i]+2e-6
            der_para.append((self.function(para_max,x)-self.function(para_min,x))/4e-6)
            para_min[i]=para_min[i]+2e-6
            para_max[i]=para_max[i]-2e-6
        return der_para
    
    
    def optimizer(self):
        delta_para=[0 for i in range(len(self.para))]
        for j in range(len(delta_para)):
            for i in range(len(self.input)):
                delta_para[j]=delta_para[j]-((self.function(self.para,self.input[i])-self.obtain[i])
                *self.__deri(self.input[i])[j])
            delta_para[j]=delta_para[j]/len(self.input)  
            self.para[j]=self.para[j]+self.lr[j]*delta_para[j]

    
    def getting_cost(self):
        cost=0
        for i in range(len(self.input)):
            cost=cost+(self.obtain[i]-self.function(self.para,self.input[i]))**2
        cost=cost/len(self.input)**0.5
        return cost

import numpy as np

def func(a,x):
    return a[0]*np.power(x,2)+a[1]

def target_function(x):
    return 5*np.power(x,2)+2

x=[10*np.random.uniform() for i in range(100)]
y=[target_function(x[i]) for i in range(len(x))]

fitting=Gra_fit(func,x,y,[4,3],[1e-3,1e-3])

for i in range(10000):
    fitting.optimizer()
    print(fitting.getting_cost(),fitting.para)
    
