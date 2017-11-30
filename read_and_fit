# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:54:19 2017

@author: pyh
"""

class AFMsim(object):
    
    def __init__(self,afm,alpha,beta,learning_rate=0.01,file_CHG="CHGCAR",file_ELF="ELFCAR"):
        
        self.file_CHG=file_CHG
        self.file_ELF=file_ELF
        self.learning_rate=learning_rate
        self.lattice=self.__read(file=self.file_CHG)[0]
        self.CHG=self.__read(file=self.file_CHG)[1]
        self.ELF=self.__read(file=self.file_ELF)[1]
        self.afm=afm
        self.input=self.pool_coll_()
        self.fitting=self.Gra_fit_exp(X=self.input,Y=self.afm,a=alpha,b=beta)
        
    @property
    def cost(self):
        return self.fitting.getting_cost()
    @property
    def optimizer(self):
        self.fitting.optimizer(learning_rate=self.learning_rate)
        
    def __read(self,file):
        ap=[[0.,0.,0.] for i in range(3)]
        atom_num=[]
        num=0
        fft_num=[]
        fft=[]
        
        fid=open(file,"rt")
        fid.readline()
        fid.readline()
        
        for i in range(3):
            line = fid.readline()
            for j in range(3):
                ap[i][j]=float(line.split()[j])
        
        fid.readline()
        line=fid.readline()
        str_num=line.split()
        
        for i in range(len(str_num)):
            atom_num.append(int(str_num[i]))
            num=num+atom_num[i]
            
        while not 'Direct' in line:
            line = str(fid.readline())
           
        for i in range(num):
            fid.readline()
        
        fid.readline()
        
        line=fid.readline()

        for i in range(len(line.split())):
            fft_num.append(int(line.split()[i]))
            
        line=fid.read()
        fft_str=line.split()
        for k in range(fft_num[2]):
            fft.append([])
            for j in range(fft_num[1]):
                fft[k].append([])
                for i in range(fft_num[0]):
                    fft[k][j].append(float(fft_str[k*fft_num[1]*fft_num[0]+j*fft_num[0]+i]))
        fid.close()
        return num,fft
    
    def pool_coll_(self):# 补充pool
        return [[self.CHG[i],self.ELF[i]] for i in range(len(self.CHG))]
    
    class Gra_fit_exp(object):
        
        def __init__(self,X,Y,a,b):
            self.input=X
            self.obtain=Y
            self.alpha=a
            self.beta=b
        
        def optimizer(self,learning_rate=0.01):
            import numpy as np
            delta_a=0
            delta_b=0
            for i in range(len(self.input)):            
                delta_a=delta_a+(self.obtain[i]-self.alpha*np.power(self.input[i][0],self.beta)*
                              self.input[i][1])*np.power(self.input[i][0],self.beta)*self.input[i][1]
                delta_b=delta_b+(self.obtain[i]-self.alpha*np.power(self.input[i][0],self.beta)*
                              self.input[i][1])*np.log(self.input[i][0])*self.alpha*np.power(self.input[i][0],self.beta)*self.input[i][1]
            delta_a=delta_a/len(self.input)
            delta_b=delta_b/len(self.input)
            self.alpha=self.alpha+learning_rate*delta_a
            self.beta=self.beta+learning_rate*delta_b
    
        def getting_cost(self):
            import numpy as np
            cost=0
            for i in range(len(self.input)):
                cost=cost+(self.obtain[i]-self.alpha*np.power(self.input[i][0],self.beta)*
                       self.input[i][1])**2
            cost=cost/len(self.input)
            return cost

if __name__=="__main__":
    a=AFMsim(0,0,0)
    print(a.ELF)            
