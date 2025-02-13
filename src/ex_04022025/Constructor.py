# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Dog:
    name = None # Instance VARIABLE
    age = None
   # color = "Black" - Hardcoded - not generic to all - blueprint?

    def __init__(self, name, age):
        print("Called, Object is created code learning")
        self.name = name
        self.age = age


    def sleep(self):
        local_variable = 10
        print("Sleeping")
        print("Who is sleeping -> ", self.name, self.age)
        return None

    def walk(self):
      print("running fast")
      print("dog is running fast->", self.name,self.age)

dog1 = Dog("chow", 10)
print(dog1.name)
dog1.sleep()
dog1.walk()
# print(dog1.color)
print(id(dog1))

dog2 = Dog("mow", 20)
print(dog2.name)
dog2.sleep()
dog2.walk()
# print(dog2.color)
print(id(dog2))

dog3 = Dog("ching",30)
print(dog3.name)
dog3.walk()
print(id(dog3))

# print(name)