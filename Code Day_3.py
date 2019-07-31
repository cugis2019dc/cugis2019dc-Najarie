# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import plotly
dir(plotly)
print("My name is Najarie")
print("Hello how are you doing")
print(5*2)
print(5/2)
print(5-2)
print(5**2)
print((8/9)*3)
print("5*2")

def multiply(a,b):
    multiply = a*b 
    
    print(multiply)

multiply(3,4)    
    
def sum(a,b,c):
    sum = a+b+c
    print(sum)
sum(12,3,5)

def area(a,base,height):
    area = a*base*height
    print(area)
    
area(1/2,6,3)

def area(base,height):
    area = (0.5)*base*height

    print('The area of the triangle with the base of',base,'and a height of',height, 'is',area,)
    
area(6,3)

   
    
    
def cadburyBox(w,d,m):
    print("There is", m, ",", d, "," , w, "in the box")
    
cadburyBox("White Chocolate", "Dark Chocolate", "Milk Chocolate")



Cadbury1="Milk Chocolate"
Cadbury2="Dark Chocolate"
Cadbury3="White Chocolate"

print("There is",Cadbury1,",",Cadbury2,",", "and",Cadbury3, "in the box.")



name= input("please enter your name")

print("your name is", name)

age= input ("please enter your age")

print("Thank you. You entered ", age)




ageint = int(age)
ageint 



    
    
    
    
import math 

dir(math)
math.pow(6,15)

    
    
    
def cubic(x):
    cubic= math.pow(x,.33)
    print("The Cubic root of" ,x, "is" ,cubic,)
    
cubic(8)
    x

cubic= input("Please enter your variable")
v= int(cubic)
cubic2= math.pow(v,.33)
print("This is your answer" ,cubic2,)

    
    
def cadburyBox(w,d,m):
    print("There is", m, ",", d, "," , w, "in the box")
    
cadburyBox("White Chocolate", "Dark Chocolate", "Milk Chocolate")
    
    
Cadbury1= "White Chocolate"
Cadbury2= "Dark Chocolate"
Cadbury3= "Milk Chocolate"

print("There is" , Cadbury1, "," ,Cadbury2, ", and" ,Cadbury3, "bars in the box.")

Cadbury1= "8 White Chocolate"
Cadbury2= "5 Dark Chocolate"
Cadbury3= "6 Milk Chocolate"

print("There are" , Cadbury1, "," ,Cadbury2, ", and" ,Cadbury3, "bars in the box.")


name= input("please enter your name")
age= input ("please enter your age")
print("Your name is",name, "and you are",age, "years old.")
 
studentage= {"Steve":32,"Lia":28,"Vin":45,"Katie":38}
studentage

studentgender = {"Steve":M,"Lia":F,"Vin":M,"Katie":F}

Studentlist=[["Steve" ,32, "M"],["Lia" ,28, "F"],["Vin" ,45, "M"],["Katie" ,38, "F"]]
Studentlist

student =[studentage,studentgender]  
student  
    
import pandas 
dir(pandas)

studentdf = pandas.DataFrame(Studentlist,columns=("name","age","gender"))
studentdf


chocolate = [["Milk",5],["Dark",8],["White",3]]
chocodf = pandas.DataFrame(chocolate, columns=("Chocolate","Quantity")
print(chocodf)


























