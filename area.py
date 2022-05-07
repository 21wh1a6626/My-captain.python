#task1
import math

radius = float(input("Enter the radius of the circle : "))

area = math.pi * radius * radius

print("Area of the circle is : {0}".format(area))



#tas2
fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
