#Write a python program that accepts the length of three sides of a triangle as inputs. The program should indicate whether or not the triangle is a right-angled triangle. (Use Pythagorean theorem) Also find out its area using Heron’s formula.
import math
def isvalidtriangle(sides): #check if given sides forms a valid triangle
    return (sides[0]<sides[1]+sides[2] and sides[1]<sides[0]+sides[2] and sides[2]<sides[1]+sides[0])
def right_triangle(sides): # check if the sides form right triangle or not
    sides=sorted(sides) #hypoteneous at last -> sides[2]
    return sides[2]**2==sides[1]**2+sides[0]**2 #pythagorous
def area(sides): #heron's formula to calculate area of triangle 
    s=sum(sides)/2
    ar=math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))
    return ar

#input 
sides=[0,0,0] #max at index[0]
for i in range(3):
    sides[i]=float(input(f"Enter side {i+1}: "))
#main
if isvalidtriangle(sides):
    if right_triangle(sides):
         print("It is a right angled triangle\n")
    else:
        print("It is not a right angled triangle\n")
    
    print(f"Area of given triangle is {area(sides)}")
else:
        print("It is not a valid triangle\n")


