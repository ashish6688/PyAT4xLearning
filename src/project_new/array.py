## create / add
## update
## remove
# # retrive
##

#create
cities = ["pune","mumbai","banglore","Kolkata"]

print(len(cities))

 ## retrive
print(cities[0])

## update
cities[0]= "Nagpur"
print(cities)

#dictionary
         # 0         1      3  4
info = ["ashish","Ankush",24,34]

infoB = {
    "firstname":"ashish",
    "lastname":"Ankush",
    "rollNo":24,
    "age":34
}
# dict does not stores the value by index
#print(infoB[0])
#print(infoB)


#retrive
print(infoB["firstname"])
#update
infoB["firstname"]="tanmay"
print(infoB)

#add command
infoB["city"] ="Ajmer"
print(infoB)

#delete
infoB.pop("age")
print(infoB)


vehical = {
    #property:value
    #key:value

    "type":"sedane",
    "model":"G3",
    "companyName":"Audi"

}

# check particular property exist
print("model" in vehical)

#retrive
print(vehical['model'])

#update
vehical['model']="64"
print(vehical)

#add
vehical['model'] = "123"
print(vehical)

#delete

