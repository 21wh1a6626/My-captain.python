#task1
import math

radius = float(input("Enter the radius of the circle : "))

area = math.pi * radius * radius

print("Area of the circle is : {0}".format(area))



#tas2
filename = input("Write the filename")

file_extns = filename.split(".")

print("The extension is " +repr(file_extns[-1]))
          

