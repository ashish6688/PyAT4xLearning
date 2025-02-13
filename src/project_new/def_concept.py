#functions learning

#program1

# int as parameter and int as a return type

def add(x,y):
    return x+y

e = add(12,3)
print(e)
print(type(e))


#float as a paramter and float as a return type
def addE(x,y):
    return x + y
f = addE(12.5,11.5)
print(f)
print(type(f))

# boolean as a parameter and boolean as a return type
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False

e = canDrive(17,True)
print(e)

def greet(name):
   return "welcome "+name+"!"
f = greet("chinmay")
print(f)

# list as parameter and list as a return type
cities = ["pune","mumbai","banglore","kolkata","chennai"]
def addCity(lst):
    lst.append("nagpur")
    return lst
f = addCity(cities)
print(f)

# dict as a parameter and dictionary as a return type

info = {

    "firstname":"ashish",
    "lastname":"Panwar",
    "age":"30",

}

def addLanguage(d):
    d.update({"language":"marwadi"})
    return d
d = addLanguage(info)
print(d)

def addcity(g):
    g.update({"city":"Ajmer"})
    return g
g = addcity(info)
print(g)

#tuple as parameter and tuple as a return type
#tuple start with small brackets
tupC = (22,33,44,55,66,77)
def addElementToTuple(tupA):
    tupA = list(tupA)
    tupA.append(88)
    tupA = tuple(tupA)
    return tupA
t = addElementToTuple(tupC)
print((t))

#set as parameter and set as a return
setA = {22,33,44,55,66,77}
def addValToSet(setP):
    setP.add(99000)
    return setP
e = addValToSet(setA)
print(e)

# list , tuple , dictionary , set , string