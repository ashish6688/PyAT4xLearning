#conditons and loops
## Conditions
#1.  age > 18 -> you are allowed to vote. - True ? - True
#2. age < 18 -> are you allowed to vote ?  No -> False

#If else Loop

#**Syntax**

#if condition:`

#` // code you want to execute if the condition is true`

#`else:`

#`//  // code you want to execute if the condition is false`


# Syntax
'''if condition 1:
    print("do 1")
elif condition 2:
    print("do 2")
else:
    print(" do 3")'''
from sys import exception

# Asking for the user's age

age = (input("Please enter your age:-" ))
try:
  if age.isdigit(): #checking if value is stirng and interger or float
     age = int(age)
     print(f"you entered and int value:{age}")

  if age<0:
    print("Age cannot be negative. Please enter a valid age.")
    print("Invalid input. Please enter a numeric value.")
  elif age < 18:
   print("You are to small.")
  elif age<26:
   print("You are to Young.")
  elif age<55:
   print("You are a senior citizen.")
  else:
   print(f"You entered a string value: {age}. Please enter a numeric value.")
except Exception as e:
    print(f"An error occurred: {e}")