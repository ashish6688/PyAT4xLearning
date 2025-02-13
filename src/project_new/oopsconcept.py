# dictionary
#          0          1           2       3  4

info = ["chinmay","deshpande",7709292441,34,56]

dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":45,
    "phoneNumber":7709192441
}
print(type(dictA))
# dictionary does not stores the value by index
#print(dictA[0])

#program 2
#retrive
q1 = dictA['firstName']
print(q1)

info = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
print(info)

# check whether property exist in dictionary
print("type in info")

info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23
}
#print(info2)

info3 = info2
info2['firstName'] = 'Ashsih'
print(info3)

info3 = info2.copy()
info3['firstName'] = 'Vishal'
#print(info3)
#print(info2)


info4 = {
    "firstName":"rahul",
    "lastName":"panwar",
    "age":23
}

print(info4.items())
print(info4.keys())
print(info4.values())

for x in info4.values():
    print(x)

for x in info4.keys():
    print(x)

for x in info4.items():
    print(x)

info5 = {
    "firstName":"Yatharth",
    "lastName":"panwar",
    "age":5
}
print(type(info5))
e = dict.fromkeys(["firstName","lastName","age","rollNo"])
print(e)

e = info5.setdefault('city','pune')
print(info5)


#[] ---> list
#{key:value} ---> dictionary
#()   ----> tuple
#{11,22,33} ---> set

#revision

info6 = {
    "firsName":"Ankit",
    "lastname":"deshpande",
    "age":"78",
    "rollNo":34
}

e = info6.get("rollno")
#info6.clear()
info6.update({"city":"pune"})
#info6.popitem()
#info6.pop("age")
for k in  info6.keys():
 print(k)

for v in info.values():
    print(v)

for item in  info6.items():
    print(item)

print(info6)
info7 = info6.copy()
print(info7)
info7['firstName'] = "amit"
print(info7)
print(info6)
e = dict.fromkeys(["color","type","model"])
print(e)

info6.setdefault('language',"Marathi")
print(info6)