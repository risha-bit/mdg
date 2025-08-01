#print(" hello ")
"""print(' hi jo')
#this is  a comment
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
# This is a simple Python program that greets the user
# It prompts the user to enter their name and then prints a greeting message      """ 
  
#name= input(" enter your name: ")
#print(" hello student:"+ name + "to g2 section ")
#s= " hello "
#print(s)
"""""
age = 19 
weight = "52 kg"
bloodgroup= " A+"
print(age ,weight, bloodgroup  )

# taking two inputs at a time
x, y = input("Enter two values: ")
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ")
print("Total number of students: ",
 x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)"""



"""x , y= input(" enter the two values :").split()

print(" enter the first value :", x)
print(" enter the second value :", y) """


# taking three inputs at a time
# taking three inputs at a time 
"""x, y, z= input(" enter the three values :").split()
print(" enter the first value :", x)
print(" enter the second value :", y)           
print(" enter the third value :", z)"""
# program to distinguish  between age groups
"""
age= int(input("enter the age :"))
if age<0:
    print(" age is invalid ")
elif  age >= 18 and age <65 :
    print(" you are a an adult")
elif  age >=65:
    print(" you are a senior citizen")
else:
    print("you are a minor")
"""

import random
while True:
    choices=["rock","paper", "scissors"]


    computer= random.choice(choices)
    player= None
    player= input(" rock , paper , scissors ?:")

    while player not in choices:
          player = input(" rock , paper ,scissors ?:").lower()

    if player== computer:
            print(" computer", computer)
            print(" player", player)
            print(" tie!")
    elif player== "rock":
        if  computer== "paper":
            print(" computer", computer)
            print(" player", player)
            print(" you loose !")
        if  computer== "scissors":
            print(" computer", computer)
            print(" player", player)
            print("  i  loose !")
    elif player == "scissors ":
        if  computer== "paper":
            print(" computer", computer)
            print(" player", player)
            print(" i loose!")
        if  computer== "rock ":
            print(" computer", computer)
            print(" player", player)
            print("  i win  !")
    elif player== "paper":
        if computer== "scissors":
            print(" computer", computer)
            print(" player", player)
            print(" i win!")
        if computer== "rock ":
            print(" computer", computer)
            print(" player", player)
            print("  i win  !")   

        play_again=input(" play again?(yes/no):").lower()
        if play_again!="yes":
            break
print(" bye!")

   