# str , int , float , boolean
# list , dict , tuple , string , set
# functions
#from datatype.decorators import returns


#program 1
# int as parameter and int as a return type
def add(x,y):
    return x + y
q1 = add(12,3)
print(q1)

#program 2
# float as a parameter and float as return type
def add2(x,y):
 return x + y
q2 = add2(12.3,48.96)
print(q2)

#program 3
#string as a parameter and string as a return
def greet(word):
    return "hello" + word
q3 = greet("Ankush")
print(q3)