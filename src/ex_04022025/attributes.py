# PyATB Students
# Attributes / Properties / Data members
# Behaviour / Methods / members functions
from xmlrpc.server import DocCGIXMLRPCRequestHandler


# Attributes - name, id, phoneNo, gender, color_eyes, city, location, address.
# By Which you recognize


# Behaviour - walk, talk, write, sing, dance, watch, listen, sleep, cry, simile
# You can do something.

class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # NRNG  # self - this , self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")


    def sing(self):
        print("I am Singing")

        def walk_return(self):  # No Arg with Return
            return "I am walking"

#Create an Object of the Class
# ObjectRef = ClassName() -> Object
ashish = Person()
ashish.name = "Ashish"
print(ashish.name)
ashish.talk()
ashish.sleep(ashish.name)


