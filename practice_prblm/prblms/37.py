'''
mapping function in a dictionary
map={1:["a","b"],2:["f","h"]}

lamda
add=x,y:x+y # function in one line

import sys
print("command line arguments[place where python is stored]:",sys.argv)
print("python version: ",sys.version)

import time
      varuous time related functions

#dir :-> list of built - in functions
         its a library (dictionary) not a function
         returns a list of names in the current local scope or a list of attributes of an object if passed as an argument
         
import math

l=[1,23,4,62]
a=4
print("attributes of a list: ",dir(l))
print("attributes of math lib :",dir(math))
print("attributes of integer :",dir(a))




import time
print(time.time()) # current time in seconds since the epoch (the epoch is a predefined : nearly in the beginning of 1974)
print("Start")
time.sleep(1) #sleep for 1 sec
print("END")
print("local time :",time.localtime()) # system time

current_time=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S ",current_time)
print("formatted_time: ",formatted_time)




'''
j[]={}
j[2]={};