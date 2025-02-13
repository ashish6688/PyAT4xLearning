
class Dog: # class Name will always start from the Capital letter
    #A
    name= None
    breed = None
    color = None

    #B
    def sleep(self):
        print("sleeping")

    def bark(self):
            print("bark")

    def eat(self, food):
                print(food)
dog1 = Dog()
print(dog1.name)
dog1.name ="Meaw"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")

dog2 = Dog()
print(dog2.name)
dog2.name="Mow"
print(dog2.name)

dog3 = dog1

