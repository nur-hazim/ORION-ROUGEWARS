#Answer ===================
import math
#Ask for weight
human_age = float(input("Enter your Age in Human Years :"))
#Ask for height
height = float(input("Enter your height(m) :"))


#Perform BMI calculation
age =((human_age/2)*height)**3.142 #Formula to calculate BMI
print("Your Alien Age is",age) #Modify to display the calculated BMI value