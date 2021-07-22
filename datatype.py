# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:25:11 2021

@author: velmani
"""
#Numbers(int,float,complex)
x=17
y=4.6
z=3+5j
print(x,y,z)
print(z,type(z))

#String
lan_name='python scripting'
print(lan_name)

my_name="vel"
print(my_name,type(my_name))

#Boolean Data type --> bool
value=True
new_value=False
print(value,type(value))
print(new_value,type(new_value))

#Type conversion
#bool(0),bool(None),bool([]) = False
#bool(non-empty) = True
x=26
y=str(x)
print(y,type(y))
z=bool(x)
print(z,type(z))
p=0
print(p,type(p))
q=bool(p)
print(q,type(q))

#Arithmetic operations
a=10
b=15
c=a+b
d=a-b
e=a*b
print(c,d,e)
f=a%b
print(f)

#In string
first_msg="Hi"
sec_msg="How r u?"
print(first_msg+" "+sec_msg)
print(first_msg*5)
print(sec_msg[4])
print(sec_msg[0:6])
print(sec_msg[-1])
print(len(sec_msg))
print(sec_msg[:-5])
