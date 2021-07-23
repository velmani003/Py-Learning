# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:19:52 2021

@author: velmani
"""

#Broadcasting(Req shape and perform operations)
#Arrays of diff size and shape
import numpy as np
a=np.array([[1,2],
           [3,4],
           [4,5]])
b=np.array([10,20])
print(a.shape)
print(b.shape)
#Rules 
#Size should be same
#or size of the dimensions should be 1
c=a+b
print(c)
v=np.array([[1],
            [2],
            [3]])
l=np.array([10,20,30]) 
print(l+v)

#Reshaping the array
#reshape--> without affecting the data it will change the shape of an array
#Arguments ---> array(input),shape(new),order(c->row,F->col,A->Fortran like order)
g=np.arange(10)
print(g)
z=np.reshape(g,(5,2))
print(z)
j=np.reshape(g,(5,2),order="F")
print(j)

#Resize (change the size of the array)
#arguments - array name(input),shape
#It will repeating the elements depends upon the size we give 
#2*3=6 => we have again having 0 in [2,3] place
k=np.arange(5)
print(np.resize(5,3))

